from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return f"{self.content[:50] if len(self.content) > 50 else ...}"


class Post(models.Model):
    comment = models.CharField(max_length=512)
    users = models.ForeignKey(
        to=User,
        related_name="post_user",
        related_query_name="post_user",
        on_delete=models.CASCADE,
    )
    blogs = models.ForeignKey(
        to=Blog,
        related_name="post_blog",
        related_query_name="post_blog",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.users}"
