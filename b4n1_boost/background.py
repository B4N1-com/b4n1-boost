"""b4n1-boost background tasks: @background and @native_async.

Phase 1 (no Redis, no Celery): offload heavy callables out of the request
path with a shared thread pool plus a sqlite-backed durable journal, so a
restart never silently loses a submitted task record.

Honest limits: arbitrary Python bytecode still takes the GIL while it runs;
the win is non-blocking requests + persistence + zero infra. True GIL-free
execution is only for Rust-side ops (see worker_* in __init__).
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import functools
import os
import pickle
import sqlite3
import threading
import time
import uuid

_POOL_LOCK = threading.Lock()
_POOL: concurrent.futures.ThreadPoolExecutor | None = None


def _pool() -> concurrent.futures.ThreadPoolExecutor:
    global _POOL
    with _POOL_LOCK:
        if _POOL is None:
            workers = max(4, (os.cpu_count() or 4) * 2)
            _POOL = concurrent.futures.ThreadPoolExecutor(
                max_workers=workers, thread_name_prefix="b4n1-bg"
            )
    return _POOL


def _db(path: str) -> sqlite3.Connection:
    con = sqlite3.connect(path, timeout=10)
    con.execute(
        "CREATE TABLE IF NOT EXISTS tasks"
        " (id TEXT PRIMARY KEY, func TEXT, status TEXT,"
        "  created REAL, finished REAL, error TEXT)"
    )
    return con


class TaskHandle:
    """Handle for a background task (Future-like, minimal surface)."""

    def __init__(self, task_id: str, fut: concurrent.futures.Future,
                 journal: str | None):
        self.id = task_id
        self._fut = fut
        self._journal = journal
        fut.add_done_callback(self._record)

    def _record(self, fut: concurrent.futures.Future) -> None:
        if not self._journal:
            return
        try:
            err = None if fut.exception() is None else repr(fut.exception())
            with _db(self._journal) as con:
                con.execute(
                    "UPDATE tasks SET status=?, finished=?, error=? WHERE id=?",
                    ("done" if err is None else "failed", time.time(), err, self.id),
                )
        except OSError:
            pass

    def done(self) -> bool:
        return self._fut.done()

    def result(self, timeout: float | None = None):
        return self._fut.result(timeout)


def _resolve(func_path: str):
    mod_name, _, qual = func_path.rpartition(".")
    if not mod_name:
        raise ValueError(f"cannot resolve {func_path!r}")
    import importlib

    mod = importlib.import_module(mod_name)
    obj = mod
    for part in qual.split("."):
        obj = getattr(obj, part)
    return obj


def background(_fn=None, *, journal: str | None = None):
    """Decorator: run the function in the shared pool, return TaskHandle.

    Usage::

        @background
        def send_email(user_id): ...

        @background(journal="/tmp/b4n1-tasks.db")
        def build_report(ids): ...

    With ``journal``, every submission is recorded in sqlite before running;
    ``pending_tasks(journal)`` lists records not yet marked done/failed
    (crash recovery: re-submit what you need, nothing is silently lost).
    Args must be picklable when a journal is used.
    """

    def wrap(fn):
        name = f"{fn.__module__}.{fn.__qualname__}"

        @functools.wraps(fn)
        def inner(*args, **kwargs):
            task_id = uuid.uuid4().hex
            if journal is not None:
                pickle.dumps((args, kwargs))  # fail loud if not picklable
                with _db(journal) as con:
                    con.execute(
                        "INSERT INTO tasks VALUES (?,?,?, ?,?,?)",
                        (task_id, name, "pending", time.time(), None, None),
                    )
            fut = _pool().submit(fn, *args, **kwargs)
            return TaskHandle(task_id, fut, journal)

        inner._b4n1_background_ = True
        return inner

    if _fn is None:
        return wrap
    return wrap(_fn)


def pending_tasks(journal: str):
    """List journal records still pending (for crash recovery)."""
    with _db(journal) as con:
        rows = con.execute(
            "SELECT id, func, created FROM tasks WHERE status='pending'"
            " ORDER BY created"
        ).fetchall()
    return [{"id": r[0], "func": r[1], "created": r[2]} for r in rows]


def native_async(_fn=None):
    """Decorator: run sync function in a thread from async code.

    Usage::

        @native_async
        def heavy(n): ...

        result = await heavy(10)
    """

    def wrap(fn):
        @functools.wraps(fn)
        async def inner(*args, **kwargs):
            return await asyncio.to_thread(fn, *args, **kwargs)

        inner._b4n1_native_async_ = True
        return inner

    if _fn is None:
        return wrap
    return wrap(_fn)
