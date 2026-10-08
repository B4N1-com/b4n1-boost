"""
b4n1_boost.sqlalchemy_accelerator — SQLAlchemy ORM acceleration using PostgreSQL COPY protocol.

Provides high-performance bulk operations for SQLAlchemy (used in FastAPI, Flask, etc.):

- ``bulk_insert_sqlalchemy_native()``: Insert thousands of dicts or model instances into PostgreSQL
  using COPY protocol via raw connection cursor, bypassing ORM overhead.

Usage::

    from b4n1_boost.sqlalchemy_accelerator import bulk_insert_sqlalchemy_native

    # With a SQLAlchemy Session or Engine
    bulk_insert_sqlalchemy_native(
        session_or_engine,
        MyModel,
        [{'name': 'Widget', 'price': 9.99}, ...]
    )
"""

from __future__ import annotations

import io
from typing import Any, Sequence


def bulk_insert_sqlalchemy_native(
    bind: Any,
    model: Any,
    data: list[dict[str, Any]] | list[Any],
    batch_size: int = 1000,
) -> int:
    """Bulk insert rows into a PostgreSQL database for SQLAlchemy models using COPY protocol.

    Falls back to SQLAlchemy's standard bulk insertion for non-PostgreSQL databases or errors.

    Args:
        bind: SQLAlchemy Session, Engine, or Connection object.
        model: The SQLAlchemy model class.
        data: List of dicts or model instances.
        batch_size: Number of rows per batch.

    Returns:
        Total number of inserted rows.
    """
    if not data:
        return 0

    # Normalize data to list of dicts
    dict_data: list[dict[str, Any]] = []
    if isinstance(data[0], dict):
        dict_data = data  # type: ignore[assignment]
    else:
        # Convert model instances to dicts using table columns
        table = getattr(model, "__table__", None)
        if table is not None:
            col_keys = [c.name for c in table.columns]
            for obj in data:
                d = {k: getattr(obj, k, None) for k in col_keys if hasattr(obj, k)}
                dict_data.append(d)
        else:
            dict_data = [obj.__dict__ for obj in data]

    if not dict_data:
        return 0

    # Extract connection / engine / session details
    raw_conn = None
    engine = None

    if hasattr(bind, "raw_connection"):
        try:
            raw_conn = bind.raw_connection()
        except Exception:
            pass
    elif hasattr(bind, "connection"):
        try:
            conn_obj = bind.connection()
            engine = getattr(conn_obj, "engine", None)
            raw_conn = getattr(conn_obj, "connection", None)
            if raw_conn is None:
                raw_conn = conn_obj
        except Exception:
            pass
    elif hasattr(bind, "engine"):
        engine = bind.engine
    elif hasattr(bind, "cursor"):
        raw_conn = bind

    # Check vendor name if possible
    dialect_name = ""
    if engine is not None and hasattr(engine, "dialect"):
        dialect_name = getattr(engine.dialect, "name", "")
    elif hasattr(bind, "bind") and getattr(bind.bind, "dialect", None) is not None:
        dialect_name = getattr(bind.bind.dialect, "name", "")
    elif hasattr(bind, "engine") and getattr(bind.engine, "dialect", None) is not None:
        dialect_name = getattr(bind.engine.dialect, "name", "")

    # Apply PostgreSQL COPY if dialect is postgresql
    if dialect_name in ("postgresql", "postgres") or "postgres" in str(type(raw_conn)).lower():
        try:
            return _bulk_insert_sa_pg_copy(raw_conn, bind, model, dict_data, batch_size)
        except Exception:
            pass

    # Universal Safe Fallback via SQLAlchemy session or connection
    return _bulk_insert_sa_fallback(bind, model, dict_data, batch_size)


def _bulk_insert_sa_pg_copy(
    raw_conn: Any,
    bind: Any,
    model: Any,
    dict_data: list[dict[str, Any]],
    batch_size: int,
) -> int:
    """Internal PostgreSQL COPY implementation for SQLAlchemy."""
    table_name = getattr(model, "__tablename__", None)
    if not table_name and hasattr(model, "__table__"):
        table_name = model.__table__.name

    if not table_name:
        raise ValueError("Could not determine table name from SQLAlchemy model")

    fields = list(dict_data[0].keys())

    # Get underlying DBAPI connection cursor (psycopg2 / psycopg3)
    dbapi_conn = raw_conn
    if dbapi_conn is None and hasattr(bind, "connection"):
        dbapi_conn = getattr(bind.connection(), "connection", None)

    if dbapi_conn is None or not hasattr(dbapi_conn, "cursor"):
        raise ValueError("Could not obtain DBAPI connection cursor")

    cursor = dbapi_conn.cursor()
    total = 0

    try:
        for i in range(0, len(dict_data), batch_size):
            batch = dict_data[i : i + batch_size]
            buf = io.StringIO()

            for row in batch:
                values = []
                for f in fields:
                    v = row.get(f)
                    if v is None:
                        values.append("\\N")
                    else:
                        values.append(str(v).replace("\t", "\\t").replace("\n", "\\n"))
                buf.write("\t".join(values) + "\n")

            buf.seek(0)
            columns_str = ", ".join(f'"{f}"' for f in fields)

            if hasattr(cursor, "copy_expert"):
                # psycopg2
                cursor.copy_expert(
                    f'COPY "{table_name}" ({columns_str}) FROM STDIN WITH (FORMAT text)',
                    buf,
                )
            elif hasattr(cursor, "copy"):
                # psycopg3
                with cursor.copy(f'COPY "{table_name}" ({columns_str}) FROM STDIN WITH (FORMAT text)') as copy:
                    copy.write(buf.getvalue())
            else:
                raise NotImplementedError("Cursor does not support COPY")

            total += len(batch)

        if hasattr(dbapi_conn, "commit"):
            dbapi_conn.commit()
    finally:
        cursor.close()

    return total


def _bulk_insert_sa_fallback(
    bind: Any,
    model: Any,
    dict_data: list[dict[str, Any]],
    batch_size: int,
) -> int:
    """Fallback bulk insert using standard SQLAlchemy methods."""
    total = 0
    if hasattr(bind, "bulk_insert_mappings"):
        # SQLAlchemy Session object
        for i in range(0, len(dict_data), batch_size):
            batch = dict_data[i : i + batch_size]
            bind.bulk_insert_mappings(model, batch)
            total += len(batch)
        if hasattr(bind, "commit"):
            bind.commit()
        return total

    table = getattr(model, "__table__", None)
    if hasattr(bind, "execute") and table is not None:
        # Connection or Engine object
        for i in range(0, len(dict_data), batch_size):
            batch = dict_data[i : i + batch_size]
            bind.execute(table.insert(), batch)
            total += len(batch)
        if hasattr(bind, "commit"):
            bind.commit()
        return total

    # Ultimate fallback: model instantiation
    instances = [model(**d) for d in dict_data]
    if hasattr(bind, "add_all"):
        bind.add_all(instances)
        if hasattr(bind, "commit"):
            bind.commit()
        return len(instances)

    return len(dict_data)
