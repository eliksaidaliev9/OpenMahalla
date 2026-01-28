from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppealViewSet

router = DefaultRouter()
# Associate the 'appeals' endpoint with AppealViewSet
# Basename='appeal' -> used for reverse URL name
router.register(r'appeals', AppealViewSet, basename='appeal')

urlpatterns = [
    # Add all ViewSet URLs via Router
    path('', include(router.urls)),
]