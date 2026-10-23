"""JSON serialization fallback with the SAME semantics as the fast paths.

The crate has three JSON engines: the native one (always present in the
wheel) and, in the accelerators, `orjson` when it happens to be installed.
All of them render a non-finite float as ``null`` — which is what JSON can
represent. The standard library does NOT: ``json.dumps`` emits ``NaN`` and
``Infinity``, which are **not valid JSON** (a browser's ``JSON.parse``
rejects the whole response).

So the fallback used to produce a different — and sometimes invalid —
payload depending on whether a third-party package was installed. This
module makes the fallback emit exactly what the fast paths emit.
"""

from __future__ import annotations

import json as _json
import math
from typing import Any

#: Compact separators: the same shape the native engine and orjson produce.
_SEPARATORS = (",", ":")


def sanitize_non_finite(value: Any) -> Any:
    """Replace every non-finite float with ``None`` (the JSON-safe value).

    Recursive over dicts/lists/tuples; anything else is returned as is.
    """
    if isinstance(value, float):
        return None if not math.isfinite(value) else value
    if isinstance(value, dict):
        return {k: sanitize_non_finite(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [sanitize_non_finite(v) for v in value]
    return value


def dumps_bytes(value: Any, sort_keys: bool = False) -> bytes:
    """Compact JSON bytes, identical to the fast paths' output.

    The fast path (no non-finite floats) is the common case and pays
    nothing extra: ``allow_nan=False`` only makes the stdlib REFUSE those
    values instead of writing invalid JSON, and the sanitizer runs only
    when it actually refused.

    ``sort_keys`` produces the CANONICAL form (sorted keys, recursively) -
    the shape the native canonical writer and the reader emit.
    """
    return dumps_str(value, sort_keys=sort_keys).encode("utf-8")


def dumps_str(value: Any, sort_keys: bool = False) -> str:
    """Compact JSON text, identical to :func:`dumps_bytes`."""
    try:
        return _json.dumps(
            value,
            separators=_SEPARATORS,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=sort_keys,
        )
    except ValueError:
        return _json.dumps(
            sanitize_non_finite(value),
            separators=_SEPARATORS,
            ensure_ascii=False,
            sort_keys=sort_keys,
        )
