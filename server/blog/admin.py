from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        list_display = ('title', 'author', 'created_at')

admin.site.register(Post, PostAdmin)
