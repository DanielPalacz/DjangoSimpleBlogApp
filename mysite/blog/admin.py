from django.contrib import admin
from .models import Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "slug", "author")


admin.site.register(Post, AuthorAdmin)
