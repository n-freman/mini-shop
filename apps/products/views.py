from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects \
            .prefetch_related('sizes', 'images', 'colors') \
            .all()

