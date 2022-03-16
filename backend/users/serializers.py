from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        label="Confirm Password",
        write_only=True,
        style={"input_type": "password"},
        required=True,
    )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    class Meta:
        model = User
        fields = ["id", "full_name", "username", "password", "password2"]
        extra_kwargs = {
            "password2": {"write_only": True},
        }


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "full_name", "username", "is_staff")
