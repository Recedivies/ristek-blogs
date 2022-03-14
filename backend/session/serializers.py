from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from session.models import Session
from users.models import User


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        user = get_object_or_404(User, username=username)
        data = super().validate(attrs)
        Session.objects.create(user=user, token=data["access"])
        return data
