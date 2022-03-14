from rest_framework.permissions import BasePermission

from session.models import Session


class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        return (
            Session.objects.filter(user=request.user, token=request.auth)
            .filter()
            .count()
            == 1
        )
