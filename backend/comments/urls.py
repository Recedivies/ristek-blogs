from django.urls import path

from comments.views import CommentView

urlpatterns = [
    path("<int:pk>/", CommentView.as_view(), name="comments"),
]
