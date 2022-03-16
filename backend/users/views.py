from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from session.permissions import IsTokenValid
from users.models import User
from users.serializers import MeSerializer, UserSerializer


class CreateUserView(CreateAPIView):
    """
    Allowed Method: POST
    POST    api/users/ - Create a user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(**serializer.data)
            return Response(
                {"status": "user successfully created."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeView(RetrieveAPIView):
    """
    GET     api/users/me/ - Details of current user
    """

    permission_classes = [IsAuthenticated]
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
