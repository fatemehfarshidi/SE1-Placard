from django.contrib import admin
from . import models


admin.site.register(models.User)


# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user_id','type')
    list_editable = ('type',)
    ordering = ('title',)
    search_fields = ('title','type')
<<<<<<< HEAD
    
=======
>>>>>>> bfa63df0b5cf5830a8615a34507b52d219e945fd
