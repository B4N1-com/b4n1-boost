# Django & DRF Accelerators

Two modules target the places Django spends the most time under load: bulk
writes and serialization.

## Django ORM accelerator

```python
from b4n1_boost.django_accelerator import bulk_insert_native, FastModelMixin

bulk_insert_native(MyModel, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob",   "email": "bob@example.com"},
])
```

`bulk_insert_native` writes through PostgreSQL `COPY` instead of generating
one `INSERT` statement per row. For bulk loads this is typically **5-10x
faster** than the ORM path.

### When it helps

| Situation | Gain |
|---|---|
| Seeding, migrations backfill, imports | **Large** |
| Periodic ETL / aggregation reloads | **Large** |
| Inserting a handful of rows per request | Negligible — use the ORM |

### When not to use it

- The table has triggers or constraints that `COPY` bypasses or handles differently
- You depend on per-row `save()` overrides, signals or `auto_now` behaviour
- You need the objects back with their assigned primary keys

In those cases the ORM path is the correct one. `COPY` is a bulk transport,
not a drop-in replacement for `Model.save()`.

### FastModelMixin

```python
from b4n1_boost.django_accelerator import FastModelMixin

class MyModel(FastModelMixin, models.Model):
    class Meta:
        model = MyModel
        fields = ["id", "name"]
```

Mix into an existing model to gain the fast path without rewriting call
sites.

## DRF serializer accelerator

```python
from b4n1_boost.drf_accelerator import fast_serialize, FastSerializerMixin

json_bytes = fast_serialize(queryset, fields=["id", "name", "email"])
```

Serializes a queryset straight to JSON without walking the serializer
pipeline — typically **5-10x faster** than the equivalent DRF serializer.

```python
from b4n1_boost.drf_accelerator import FastSerializerMixin
from rest_framework import serializers

class MySerializer(FastSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ["id", "name"]
```

Existing serializers keep their class declaration and gain the fast path.

### Trade-off

Fast serialization means fewer hooks. If a serializer relies on
`to_representation()` overrides, per-field sources or custom nesting, verify
the output matches byte for byte before switching — a serializer that is
faster but emits different JSON is a bug, not an optimization.

A practical check:

```python
slow = DefaultSerializer(queryset, many=True).data
fast = fast_serialize(queryset, fields=[...])
assert json.loads(slow) == json.loads(fast)
```

## Applying both

```python
import b4n1_boost

b4n1_boost.install_django()      # middleware: compression, ETag, headers...
# plus, in the views that write or read bulk data:
#   bulk_insert_native(...)      for writes
#   fast_serialize(...)          for list endpoints
```

List endpoints are usually where both meet: a paginated response pulls a
queryset and serializes it on every request.

## See also

- [Python SDK](python.md) — the rest of the API surface
- [Middleware Reference](middleware.md) — compression, caching and headers
- [Performance](performance.md) — how the numbers were measured
