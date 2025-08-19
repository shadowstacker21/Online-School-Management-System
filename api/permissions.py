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
        if request.user.role == 'teacher' and obj.teacher == request.user :
            if request.method == 'DELETE':
               return False
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

class IsAdminOrStudentPurchase(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user  

        if not user.is_authenticated:
            return False

        if user.role == 'admin':
            if request.method == 'POST':
                return False
            return True
        if user.role == 'student':
            if request.method in permissions.SAFE_METHODS or request.method == 'POST':
                return True
            return False
        return False
    
    def has_object_permission(self, request, view, obj):
       user = request.user
       if user.role == 'admin':
           return True
       if user.role == 'student':
           if request.method in permissions.SAFE_METHODS:
               return obj.student == user 
           return False
       return False
            


class IsAdminOnlyDashboard(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        if request.user.role == "admin":
            return True
        
        return False
