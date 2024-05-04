from rest_framework.exceptions import status
from rest_framework.serializers import Serializer
from rest_framework.views import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer


class RegistrationViewSet(GenericViewSet):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

