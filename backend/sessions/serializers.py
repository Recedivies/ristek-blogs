from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from sessions.models import Session
from users.models import User


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.get(username=username)
        data = super().validate(attrs)
        Session.objects.create(user=user, token=data["access"])
        return data
