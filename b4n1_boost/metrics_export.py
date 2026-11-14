"""Prometheus / OpenTelemetry export for the crate's compression counters.

``CompressionMetrics`` has counted compressions, bytes in/out and
per-algorithm usage since 0.3.x, but nothing exposed them. An accelerator the
customer cannot measure is an accelerator they cannot justify, so this module
turns those counters into the two formats every observability stack accepts.

Design rules:

* **One source of truth.** Both exporters read ``get_snapshot()``; neither
  keeps its own numbers, so they cannot drift apart.
* **Bounded cardinality (§9f).** Algorithm labels come from a fixed set. An
  unknown algorithm name is folded into ``other`` rather than creating a new
  series — otherwise a hostile request could grow the metric table without
  limit.
* **Counters stay counters.** ``compression_ratio`` is derived, so it is
  exported as a gauge (Prometheus) and a plain number (OTel); declaring it a
  counter would break every ``rate()`` query against it.
* **Explicit formats.** An unknown format raises ``UnknownFormatError``
  instead of silently rendering a default (§5).
* **No dependencies.** The exposition is text; the handler is plain WSGI/ASGI.
  A metrics endpoint must never be the reason an install fails.
"""

from __future__ import annotations

import json
from typing import Any, Callable, Iterable, Optional

__all__ = [
    "ALLOWED_ALGORITHMS",
    "METRIC_PREFIX",
    "MetricsExporter",
    "UnknownFormatError",
    "otel_snapshot",
    "prometheus_text",
]

#: Prefix every exported metric carries, so a scraper can select `b4n1_boost_*`.
METRIC_PREFIX = "b4n1_boost_"

#: The only algorithm label values allowed. Anything else becomes ``other``.
ALLOWED_ALGORITHMS = ("gzip", "brotli", "zstd")

#: Prometheus content type for the text exposition format.
PROMETHEUS_CONTENT_TYPE = "text/plain; version=0.0.4; charset=utf-8"

#: Content type for the JSON snapshot.
OTEL_CONTENT_TYPE = "application/json; charset=utf-8"

#: Formats ``MetricsExporter.render`` accepts.
FORMATS = ("prometheus", "otel")

_ERROR_UNKNOWN_FORMAT = "urn:b4n1:error:boost:metrics-unknown-format"


class UnknownFormatError(ValueError):
    """Raised when a caller asks for a format the exporter does not produce.

    Carries the house error code so logs and HTTP responses can name it
    without re-deriving the string.
    """

    code = _ERROR_UNKNOWN_FORMAT

    def __init__(self, fmt: str) -> None:
        super().__init__(
            f"unknown metrics format {fmt!r}; supported: {', '.join(FORMATS)}"
        )
        self.fmt = fmt


def _snapshot(metrics_source: Any) -> dict:
    """Read a snapshot from a ``CompressionMetrics`` or a plain dict."""
    if hasattr(metrics_source, "get_snapshot"):
        return metrics_source.get_snapshot()
    if isinstance(metrics_source, dict):
        return metrics_source
    raise TypeError(
        "metrics source must expose get_snapshot() or be a dict, "
        f"got {type(metrics_source).__name__}"
    )


def _algorithm_counts(snapshot: dict) -> dict[str, int]:
    """Per-algorithm counts, with everything unknown folded into ``other``.

    Keeping the label set closed is what bounds the series count: no request
    can grow the metric table.
    """
    counts = {name: int(snapshot.get(f"{name}_count", 0)) for name in ALLOWED_ALGORITHMS}
    known = sum(counts.values())
    total = int(snapshot.get("total_compressions", 0))
    other = total - known
    if other > 0:
        counts["other"] = other
    return counts


def prometheus_text(metrics_source: Any) -> str:
    """Render the counters in the Prometheus text exposition format.

    The result is scrapeable by a stock Prometheus: ``# HELP`` / ``# TYPE``
    before each metric, one ``name{labels} value`` line per series, and a
    trailing newline.
    """
    snapshot = _snapshot(metrics_source)

    # (name, type, help) — order is stable so the output diffs cleanly.
    counters = (
        ("total_compressions", "counter", "Total responses compressed."),
        ("total_bytes_in", "counter", "Uncompressed bytes seen."),
        ("total_bytes_out", "counter", "Compressed bytes emitted."),
    )
    # Derived values are gauges: a ratio must never be a counter.
    gauges = (
        ("compression_ratio", "Ratio of compressed to uncompressed bytes."),
        ("space_saved_pct", "Percentage of bytes saved by compression."),
    )

    lines: list[str] = []

    for name, kind, help_text in counters:
        lines.append(f"# HELP {METRIC_PREFIX}{name} {help_text}")
        lines.append(f"# TYPE {METRIC_PREFIX}{name} {kind}")
        value = int(snapshot.get(name, 0))
        lines.append(f"{METRIC_PREFIX}{name} {value}")

    for name, help_text in gauges:
        lines.append(f"# HELP {METRIC_PREFIX}{name} {help_text}")
        lines.append(f"# TYPE {METRIC_PREFIX}{name} gauge")
        lines.append(f"{METRIC_PREFIX}{name} {float(snapshot.get(name, 0.0))}")

    lines.append(
        f"# HELP {METRIC_PREFIX}compressions_by_algorithm "
        "Compressions per algorithm (bounded label set)."
    )
    lines.append(f"# TYPE {METRIC_PREFIX}compressions_by_algorithm counter")
    for algorithm, count in _algorithm_counts(snapshot).items():
        lines.append(
            f'{METRIC_PREFIX}compressions_by_algorithm{{algorithm="{algorithm}"}} {count}'
        )

    return "\n".join(lines) + "\n"


def otel_snapshot(metrics_source: Any) -> dict:
    """Render the same numbers as an OpenTelemetry-friendly JSON snapshot.

    This is deliberately a flat, JSON-serialisable dict: an OTel exporter can
    map it to instruments without this crate taking a dependency on the OTel
    SDK, and a plain HTTP consumer can read it as-is.
    """
    snapshot = _snapshot(metrics_source)
    return {
        "total_compressions": int(snapshot.get("total_compressions", 0)),
        "total_bytes_in": int(snapshot.get("total_bytes_in", 0)),
        "total_bytes_out": int(snapshot.get("total_bytes_out", 0)),
        "compression_ratio": float(snapshot.get("compression_ratio", 0.0)),
        "space_saved_pct": float(snapshot.get("space_saved_pct", 0.0)),
        "compressions_by_algorithm": _algorithm_counts(snapshot),
    }


class MetricsExporter:
    """Serves the crate's counters to Prometheus or an OTel pipeline.

    ``metrics`` may be a ``CompressionMetrics`` instance (the live one, e.g.
    ``b4n1_boost.middleware.metrics``) or a plain dict snapshot.

    Both handlers are framework-agnostic: ``wsgi_app(environ)`` returns a
    WSGI application, ``asgi_app(scope, receive, send)`` is an ASGI
    application. Mount it at ``/metrics`` in whatever router the app already
    uses — this class does not assume one.
    """

    def __init__(self, metrics: Any, default_format: str = "prometheus") -> None:
        if default_format not in FORMATS:
            raise UnknownFormatError(default_format)
        self.metrics = metrics
        self.default_format = default_format

    def render(self, fmt: Optional[str] = None) -> str:
        """Render the counters. An unknown ``fmt`` raises ``UnknownFormatError``."""
        chosen = fmt or self.default_format
        if chosen not in FORMATS:
            raise UnknownFormatError(chosen)
        if chosen == "prometheus":
            return prometheus_text(self.metrics)
        return json.dumps(otel_snapshot(self.metrics), sort_keys=True)

    # ── WSGI ──────────────────────────────────────────────────────────────

    def wsgi_app(self, environ: dict) -> Callable:
        """Return a WSGI app serving the exposition.

        Only GET (and HEAD) is allowed: a metrics endpoint is read-only, and
        answering a POST would imply a mutation nobody implemented.
        """

        def app(_environ: dict, start_response: Callable) -> Iterable[bytes]:
            method = (environ.get("REQUEST_METHOD") or "GET").upper()
            if method not in ("GET", "HEAD"):
                body = b"method not allowed\n"
                start_response(
                    "405 Method Not Allowed",
                    [
                        ("Content-Type", "text/plain; charset=utf-8"),
                        ("Content-Length", str(len(body))),
                        ("Allow", "GET, HEAD"),
                    ],
                )
                return [body]

            fmt = self._format_from_query(environ.get("QUERY_STRING", ""))
            try:
                text = self.render(fmt)
            except UnknownFormatError as exc:
                body = (f"{exc.code}: {exc}\n").encode()
                start_response(
                    "400 Bad Request",
                    [
                        ("Content-Type", "text/plain; charset=utf-8"),
                        ("Content-Length", str(len(body))),
                    ],
                )
                return [body]

            body = text.encode()
            content_type = (
                PROMETHEUS_CONTENT_TYPE if (fmt or self.default_format) == "prometheus" else OTEL_CONTENT_TYPE
            )
            start_response(
                "200 OK",
                [
                    ("Content-Type", content_type),
                    ("Content-Length", str(len(body))),
                ],
            )
            return [body]

        return app

    # ── ASGI ──────────────────────────────────────────────────────────────

    async def asgi_app(self, scope: dict, receive: Callable, send: Callable) -> None:
        """Serve the exposition over ASGI. Non-HTTP scopes pass through."""
        if scope.get("type") != "http":
            return

        method = (scope.get("method") or "GET").upper()
        if method not in ("GET", "HEAD"):
            body = b"method not allowed\n"
            await send(
                {
                    "type": "http.response.start",
                    "status": 405,
                    "headers": [
                        (b"content-type", b"text/plain; charset=utf-8"),
                        (b"content-length", str(len(body)).encode()),
                        (b"allow", b"GET, HEAD"),
                    ],
                }
            )
            await send({"type": "http.response.body", "body": body})
            return

        fmt = self._format_from_query(scope.get("query_string", b"").decode("latin-1"))
        try:
            text = self.render(fmt)
        except UnknownFormatError as exc:
            body = (f"{exc.code}: {exc}\n").encode()
            await send(
                {
                    "type": "http.response.start",
                    "status": 400,
                    "headers": [
                        (b"content-type", b"text/plain; charset=utf-8"),
                        (b"content-length", str(len(body)).encode()),
                    ],
                }
            )
            await send({"type": "http.response.body", "body": body})
            return

        body = text.encode()
        content_type = (
            PROMETHEUS_CONTENT_TYPE if (fmt or self.default_format) == "prometheus" else OTEL_CONTENT_TYPE
        )
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    (b"content-type", content_type.encode()),
                    (b"content-length", str(len(body)).encode()),
                ],
            }
        )
        await send({"type": "http.response.body", "body": body})

    @staticmethod
    def _format_from_query(query: str) -> Optional[str]:
        """Read ``?format=otel`` from a query string, or ``None`` for default."""
        if not query:
            return None
        for pair in query.split("&"):
            key, _, value = pair.partition("=")
            if key == "format" and value:
                return value
        return None
