from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blogs.models import Blog
from comments.models import Comment
from comments.serializers import CommentSerializer
from session.permissions import IsTokenValid
from users.models import User


class CommentView(CreateAPIView, UpdateAPIView, DestroyAPIView):
    """
    Allowed Method: GET, POST, DELETE
    POST   api/posts/<int:id>/ - Create a Comment
    PUT    api/posts/<int:id>/ - Update a Comment
    DELETE api/posts/<int:id>/ - Delete a Comment
    """

    permission_classes = [IsAuthenticated, IsTokenValid]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def create(self, request, pk):
        user = User.objects.get(id=request.user.id)
        blog = Blog.objects.get(id=pk)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            Comment.objects.create(**serializer.data, blog=blog, user=user)
            return Response(
                {"status": "ok", "message": "successfully created a blog."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk):
        comment = get_object_or_404(self.get_queryset(), pk=pk)
        content = request.data.get("content", "")

        if not content:
            return Response(
                {"status": "error", "message": "no content"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if comment.user != request.user:
            return Response(
                {"status": "error", "message": "invalid user"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        comment.content = content
        comment.save()
        return Response(
            {"status": "ok", "message": "comment successfully updated"},
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk):
        comment = get_object_or_404(self.get_queryset(), pk=pk)

        if comment.user != request.user:
            return Response(
                {"status": "error", "message": "invalid user"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        comment.delete()
        return Response(
            {"status": "ok", "message": "comment successfully deleted"},
            status=status.HTTP_200_OK,
        )
