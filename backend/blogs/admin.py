from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Admin View for Blog"""

    list_display = ("id", "title", "body", "created_at", "likes")
    list_filter = (
        "title",
        "body",
        "created_at",
        "likes",
    )
