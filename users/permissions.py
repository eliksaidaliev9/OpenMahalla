from rest_framework import permissions
from appeals.models import Appeal

# User can only edit/delete his/her own application and only if status = NEW
class IsOwnerAndEditable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # The user must be logged in
        # The applicant must be
        # Only NEW status application
       return request.user.is_authenticated and obj.user == request.user and obj.status == Appeal.Status.NEW

# Permission for Staff
class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

# Permission only for Admin (superuser)
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only a user who is a superuser will have permission
        return request.user.is_authenticated and request.user.is_superuser
