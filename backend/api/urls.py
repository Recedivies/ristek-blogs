from django.contrib import admin
from django.urls import include, path

from sessions.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("users/", include("users.urls")),
    path("posts/", include("comments.urls")),
    path("login/", view=LoginView.as_view(), name="login"),
    path("logout/", view=LogoutView.as_view(), name="logout"),
]
