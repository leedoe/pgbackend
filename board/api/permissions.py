from rest_framework import permissions


class IsWriterOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True

        if object.password is not None:
            return object.password == request.data['password']
        
        return object.writer == request.user

