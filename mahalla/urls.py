from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahallaViewSet

router = DefaultRouter()
router.register(r'mahallas', MahallaViewSet, 'mahalla')

urlpatterns = [
    path('', include(router.urls)),
]