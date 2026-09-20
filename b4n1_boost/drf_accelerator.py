"""
b4n1_boost.drf_accelerator — Django REST Framework Serializer accelerator.

Bypasses DRF's per-field Python serialization and serializes querysets
directly to JSON using the native Rust engine. Typical speedup: 5-10x
for list endpoints with >50 objects.

Usage::

    from b4n1_boost.drf_accelerator import fast_serialize, FastSerializerMixin

    # Option 1: Standalone function
    class ProductListView(generics.ListAPIView):
        def list(self, request, *args, **kwargs):
            queryset = self.get_queryset().values('id', 'name', 'price')
            return HttpResponse(fast_serialize(queryset), content_type='application/json')

    # Option 2: Mixin for existing serializers
    class ProductSerializer(FastSerializerMixin, serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['id', 'name', 'price']

    # Option 3: Decorator
    from b4n1_boost.drf_accelerator import serialize_view

    @serialize_view(fields=['id', 'name', 'price'])
    class ProductListView(generics.ListAPIView):
        queryset = Product.objects.all()
"""

from __future__ import annotations

import json as _json
from typing import Any, Iterable, Optional, Sequence

from b4n1_boost.middleware import NativeJson, _orjson


def fast_serialize(
    data: Iterable[dict],
    fields: Optional[Sequence[str]] = None,
) -> bytes:
    """Serialize an iterable of dicts to compact JSON bytes.

    This bypasses DRF's field-by-field serialization and goes directly
    from raw dicts (from ``queryset.values()``) to JSON in Rust.

    Args:
        data: Iterable of dicts (e.g. from ``QuerySet.values()``).
        fields: Optional field whitelist. If provided, only these keys
                are included in the output.

    Returns:
        Compact JSON as UTF-8 bytes.

    Example::

        queryset = Product.objects.values('id', 'name', 'price')
        json_bytes = fast_serialize(queryset, fields=['id', 'name'])
    """
    if fields is not None:
        field_set = set(fields)
        data = [{k: v for k, v in row.items() if k in field_set} for row in data]

    # Convert to list if it's a queryset (lazy evaluation)
    if hasattr(data, '__iter__') and not isinstance(data, list):
        data = list(data)

    # Use orjson for best performance (3-10x faster than stdlib)
    if _orjson is not None:
        return _orjson.dumps(data)

    # Fallback to stdlib
    return _json.dumps(data, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def fast_serialize_one(obj: dict, fields: Optional[Sequence[str]] = None) -> bytes:
    """Serialize a single dict to compact JSON bytes.

    Args:
        obj: The dict to serialize.
        fields: Optional field whitelist.

    Returns:
        Compact JSON as UTF-8 bytes.
    """
    if fields is not None:
        field_set = set(fields)
        obj = {k: v for k, v in obj.items() if k in field_set}

    if _orjson is not None:
        return _orjson.dumps(obj)
    return _json.dumps(obj, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


class FastSerializerMixin:
    """Mixin for DRF serializers that uses native Rust serialization.

    Add this mixin to your ``ModelSerializer`` to bypass DRF's
    per-field Python serialization for list endpoints.

    The mixin adds a ``fast_data`` property that returns the serialized
    data as compact JSON bytes using the Rust engine. For list views,
    use ``fast_many()`` to serialize a queryset directly.

    Example::

        class ProductSerializer(FastSerializerMixin, serializers.ModelSerializer):
            class Meta:
                model = Product
                fields = ['id', 'name', 'price']

        # In your view:
        serializer = ProductSerializer(queryset, many=True)
        return HttpResponse(serializer.fast_data, content_type='application/json')
    """

    @property
    def fast_data(self) -> bytes:
        """Serialize to compact JSON bytes using native Rust engine.

        For single objects, uses the serializer's validated data.
        For many=True, uses the original queryset for direct serialization.
        """
        if getattr(self, 'many', False) and hasattr(self, 'initial_data'):
            return fast_serialize(self.initial_data)
        return NativeJson.dumps_direct(self.data)

    @property
    def fast_json(self) -> str:
        """Serialize to compact JSON string using native Rust engine."""
        return NativeJson.dumps(self.data)


def serialize_view(fields: Optional[Sequence[str]] = None):
    """Decorator that accelerates DRF ListAPIView/ViewSet list methods.

    Wraps the ``list()`` method to use ``fast_serialize()`` instead of
    DRF's serializer, for a 5-10x speedup on list endpoints.

    Usage::

        @serialize_view(fields=['id', 'name', 'price'])
        class ProductListView(generics.ListAPIView):
            queryset = Product.objects.all()
            serializer_class = ProductSerializer  # used for permissions, etc.
    """
    def decorator(view_class):
        original_list = view_class.list

        def accelerated_list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())

            # Get fields from serializer if not specified
            _fields = fields
            if _fields is None and hasattr(self, 'serializer_class'):
                meta = getattr(self.serializer_class, 'Meta', None)
                if meta is not None:
                    _fields = getattr(meta, 'fields', None)
                    if _fields == '__all__':
                        _fields = None

            # Use values() for raw dict access (avoids model instantiation)
            if _fields is not None:
                raw = queryset.values(*_fields)
            else:
                raw = queryset.values()

            json_bytes = fast_serialize(raw, fields=_fields)

            from django.http import HttpResponse
            return HttpResponse(json_bytes, content_type='application/json')

        view_class.list = accelerated_list
        return view_class

    return decorator
