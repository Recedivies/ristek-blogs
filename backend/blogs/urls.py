from django.urls import path
from blogs.views import BlogList

urlpatterns = [
    path("test/", BlogList.as_view(), name="test"),
]
