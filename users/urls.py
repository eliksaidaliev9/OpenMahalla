from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, UserViewSet


router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('', include(router.urls)),
]