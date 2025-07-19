from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to grant access only to Admin users.
    """
    def has_permission(self, request, view):
        print(f"User Type: {request.user.user_type}") 
        return request.user.is_authenticated and request.user.is_admin_user  # No parentheses

class IsNormalUser(permissions.BasePermission):
    """
    Custom permission to grant access only to Normal users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_normal_user  # No parentheses

class IsPaidUser(permissions.BasePermission):
    """
    Custom permission to grant access only to Paid users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_paid_user  # No parentheses

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow Admin users to create, update, delete.
    Normal and Paid users can only view.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_type == 'admin':  # Check for 'admin' user type
                return True  # Admin can do anything
            elif request.user.user_type in ['normal', 'paid']:  # Check for normal or paid users
                return request.method in permissions.SAFE_METHODS  # Normal/Paid users can only read
        return False