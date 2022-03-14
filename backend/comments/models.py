from django.db import models

from blogs.models import Blog
from users.models import User


class Comment(models.Model):
    content = models.CharField(max_length=512)
    user = models.ForeignKey(
        to=User,
        related_name="post_user",
        related_query_name="post_user",
        on_delete=models.CASCADE,
    )
    blog = models.ForeignKey(
        to=Blog,
        related_name="comments",
        related_query_name="comments",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.content}"

    class Meta:
        ordering = ["-created_at"]
