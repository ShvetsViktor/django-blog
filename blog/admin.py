from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Configures the admin interface for :model:`blog.Post`
    with search, filtering and Summernote rich-text editing.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)