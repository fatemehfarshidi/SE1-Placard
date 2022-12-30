from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'user_field', 'type')
    list_editable = ('type', 'price')
    ordering = ('title',)
    search_fields = ('title','type', 'tags')
