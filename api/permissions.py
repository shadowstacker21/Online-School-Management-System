from rest_framework import permissions

class IsAdminOrTeacherOwner(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "admin":
            return True
        if request.user.role == "teacher":
            return True

        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == 'admin':
            return True
        if request.user.role == 'teacher' and obj.teacher == request.teacher :
            return True
        return False
    
class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "admin":
            return True
        

        return False
        # return request.user.is_authenticated and request.user.role == 'admin'