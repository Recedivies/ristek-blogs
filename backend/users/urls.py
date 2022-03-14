from django.urls import path

from users.views import CreateUserView, MeView

urlpatterns = [
    path("", CreateUserView.as_view(), name="create_user"),
    path("me/", MeView.as_view(), name="me"),
]
