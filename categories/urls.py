from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

# DRF DefaultRouter yaratish
router = DefaultRouter()
# Bind the 'categories' endpoint to the CategoryViewSet
# Basename='category' -> used for reverse URL name
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),  # Add all ViewSet URLs via Router
]