from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from sessions.models import Session
from sessions.serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    """
    Allowed Method: POST
    POST  api/login - create session when login user
    """

    serializer_class = LoginSerializer


class LogoutView(DestroyAPIView):
    """
    Allowed Method: DELETE
    DELETE  api/logout - Delete a session with correspond user
    """

    queryset = Session.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        Session.objects.filter(user=request.user).delete()
        return Response({"message": "token revoken"}, status=status.HTTP_200_OK)
