from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except ValueError as e:
            print(e)
        return user

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "username",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
        depth = 1


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "full_name", "username")
