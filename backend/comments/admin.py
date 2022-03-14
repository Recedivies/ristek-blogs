from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin View for Comment"""

    list_display = ("content", "created_at")
    list_filter = ("content", "created_at")
