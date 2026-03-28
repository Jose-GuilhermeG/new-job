from rest_framework.permissions import BasePermission , IsAuthenticated

class isJobEnrollmentOwner(
    IsAuthenticated
):
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user