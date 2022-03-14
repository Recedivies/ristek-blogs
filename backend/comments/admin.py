from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin View for Comment"""

    list_display = ("id", "content", "created_at")
    list_filter = ("id", "content", "created_at")
