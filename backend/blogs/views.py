from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog
from blogs.serializers import BlogSerializer
from users.models import User


class Test(APIView):
    def get(self, request):
        text = request.query_params.get("text", "")
        return Response({"text": text.upper()}, status=status.HTTP_200_OK)


class BlogList(ListCreateAPIView):
    """
    Allowed Method: GET, POST
    GET     api/blogs/ - List Blogs
    POST    api/blogs/ - Create a Blog
    """

    permission_classes = [AllowAny]
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            user = None

        if not user or user.is_staff != True:
            return Response({"error": "forbidden"}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            Blog.objects.create(**serializer.data)
            return Response(
                {"status": "successfully created a blog."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
