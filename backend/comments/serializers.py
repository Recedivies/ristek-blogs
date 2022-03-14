from rest_framework import serializers

from comments.models import Comment
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["content", "user"]
        read_only_fields = [
            "user",
        ]
