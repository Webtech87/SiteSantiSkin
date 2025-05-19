from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.permissions import IsSuperUser

class PodcastCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        #print('*****', request.user, request.user.is_authenticated, request.user.IsSuperUser)
        return request.user and request.user.is_authenticated and request.user.is_superuser
