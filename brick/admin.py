from django.contrib import admin
from . import models


admin.site.register(models.Customer)
admin.site.register(models.Tag)

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','owner','type')
    list_editable = ('type',)
    ordering = ('title',)
    search_fields = ('title','type', 'tags')
