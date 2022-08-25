from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)
