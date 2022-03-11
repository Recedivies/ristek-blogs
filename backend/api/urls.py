from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("users", include("users.urls")),
]
