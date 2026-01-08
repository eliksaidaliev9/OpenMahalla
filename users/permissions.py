from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if user.is_authenticated and user.is_superuser:
            return True

        if hasattr(obj, 'status') and hasattr(obj, 'user'):
            if obj.user != request.user:
                return False
            return obj.status == 'new'

        if obj == request.user:
            if hasattr(request.user, 'appeals'):
                if request.user.appeals.filter(status__in=['under_review', 'answered']).exists():
                    return False
            return True
        return False


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if user.is_authenticated and user.is_superuser:
            return True

        if user.is_authenticated and user.is_staff:
            if hasattr(obj, 'status'):
                return True
            return False
        return False


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_superuser