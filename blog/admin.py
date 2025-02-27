from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'slug')  # Display title, creation date, and slug in the admin list
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug based on the title
    search_fields = ('title', 'content')  # Allow searching by title and content

admin.site.register(Post, PostAdmin)
