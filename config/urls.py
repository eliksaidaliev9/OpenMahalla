"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView
)

#  Swagger security setup for JWT Token
class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        security_definitions = super().get_security_definitions()
        security_definitions['Bearer'] = {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
        return security_definitions

# Swagger / OpenAPI documentation
schema_view = get_schema_view(
    openapi.Info(
        title="OpenMahalla API",
        default_version='v1',
        description="OpenMahalla API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="elyor1996em@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=JWTSchemaGenerator,
)


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/v1/', include('users.urls')),  # Users app endpoints

    path('api/v1/users_auth/', include('djoser.urls')),  # Djoser auth endpoints
    path('api/v1/users_auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT create
    path('api/v1/users_auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT renewal
    path('api/v1/users_auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # JWT validation

    path('api/v1/', include('appeals.urls')),  # appeals app endpoints
    path('api/v1/', include('categories.urls')),  # categories app endpoints
    path('api/v1/', include('mahallas.urls')),  # mahallas app endpoints

    # Swagger / OpenAPI endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

