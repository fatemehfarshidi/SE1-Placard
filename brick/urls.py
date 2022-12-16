from django.contrib import admin
from django.urls import path
from brick import views

urlpatterns = [
    path("", views.brick),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("posts/", views.post_list),
    path('posts/<int:id>/', views.post_detail),
]
