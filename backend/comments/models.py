from django.db import models

from users.models import User
from blogs.models import Blog


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
        related_name="post_blog",
        related_query_name="post_blog",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.users}"

    class Meta:
        ordering = ["-created_at"]
