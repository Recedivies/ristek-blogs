from rest_framework import serializers

from blogs.models import Blog
from comments.serializers import CommentSerializer


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at", "likes", "comments"]
        read_only_fields = ["id"]
