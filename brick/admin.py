from django.contrib import admin
from . import models



# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user_id','type')
    list_editable = ('type',)
    ordering = ('title',)
    search_fields = ('title','type')
    