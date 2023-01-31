from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'user', 'post_type')
    prepopulated_fields = {'slug': ('title',), }