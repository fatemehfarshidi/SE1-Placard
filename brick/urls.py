from django.contrib import admin
from django.urls import path
from brick import views

urlpatterns = [
    path("", views.home_page),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("posts/", views.post_list),
    path('posts/<int:id>/', views.post_detail),
]
