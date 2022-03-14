from django.urls import path

from blogs.views import BlogList, Test

urlpatterns = [
    path("", BlogList.as_view(), name="blog-list"),
    path("test/", Test.as_view(), name="test"),
]
