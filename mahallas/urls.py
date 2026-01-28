from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahallaViewSet

# # Create DRF DefaultRouter
router = DefaultRouter()
# Bind the 'mahallas' endpoint to the MahallaViewSet
# Basename='mahalla' -> used for reverse URL name
router.register(r'mahallas', MahallaViewSet, 'mahalla')

urlpatterns = [
    path('', include(router.urls)),  # Add all ViewSet URLs via Router
]