from rest_framework import permissions

from config import API_TOKEN


class AccessPermission(permissions.BasePermission):
    """
    Global permission, needed to access api
    """
    message = 'No access.'

    def has_permission(self, request, view):
        if request.META.get('HTTP_AUTHORIZATION') == API_TOKEN:
            return True