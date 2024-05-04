from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import LookBook
from .serializers import LookBookSerializer


class LookBookViewSet(ReadOnlyModelViewSet):
    serializer_class = LookBookSerializer
    queryset = LookBook.objects.prefetch_related('images').all()

