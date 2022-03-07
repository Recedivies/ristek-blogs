from django.urls import path, include

urlpatterns = [
    path("blogs", include("blogs.urls")),
    path("users", include("users.urls")),
]
