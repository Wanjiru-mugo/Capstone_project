from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    #allow admin users CRUD functions, users have read-only permissions
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            #SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True 
        else:
            return request.user.is_staff



