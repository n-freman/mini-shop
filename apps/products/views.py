from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters

from .filters import ProductFilter
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects \
            .prefetch_related('sizes', 'images', 'colors') \
            .all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

