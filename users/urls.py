from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Create DRF DefaultRouter
router = DefaultRouter()
# Bind the 'users' endpoint to the UserViewSet
# As a result, automatic CRUD URLs are generated
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)), # Add all ViewSet URLs via Router
]