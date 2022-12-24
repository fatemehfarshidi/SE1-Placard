from django.contrib import admin
from . import models


admin.site.register(models.Customer)

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'owner','type')
    list_editable = ('type', 'price')
    ordering = ('title',)
    search_fields = ('title','type', 'tags')
