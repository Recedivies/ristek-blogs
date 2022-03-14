from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

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


class MeView(RetrieveAPIView):
    """
    GET     api/users/me/ - Details of current user
    """

    permission_classes = [IsAuthenticated, IsTokenValid]
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
