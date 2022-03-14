from django.db import models

from users.models import User


class Session(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="sessions",
        related_query_name="sessions",
    )
    token = models.CharField(blank=False, max_length=256)
