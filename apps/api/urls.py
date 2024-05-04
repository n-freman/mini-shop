from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from categories.views import CategoryViewSet
from lookbooks.views import LookBookViewSet
from users.views import RegistrationViewSet
from products.views import ProductViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, 'categories')
router.register('register', RegistrationViewSet, 'users')
router.register('products', ProductViewSet, 'products')
router.register('lookbooks', LookBookViewSet, 'lookbooks')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    *router.urls
]

