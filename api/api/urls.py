from django.contrib import admin
from django.urls import path
# from api import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import home, create_post, post_detail, delete_post
from django.views.generic import TemplateView

app_name = 'api'

urlpatterns = [
    
    path('', home, name="home"),
    path('createpost/<str:pk>', create_post, name='create_post'),
    path('deletepost/<str:pk>/', delete_post, name="delete_post"),
    path("post/<str:pk>", post_detail, name="post_detail"),

]
