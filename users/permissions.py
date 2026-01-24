from rest_framework import permissions
from appeals.models import Appeal


class IsOwnerAndEditable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       return request.user.is_authenticated and obj.user == request.user and obj.status == Appeal.Status.NEW


class IsStaffOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser
