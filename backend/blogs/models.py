from django.core.validators import MinValueValidator
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self) -> str:
        return f"{self.content[:50] if len(self.content) > 50 else ...}"

    class Meta:
        ordering = ["-created_at"]
