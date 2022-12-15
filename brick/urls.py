from django.contrib import admin
from django.urls import path
from brick import views

urlpatterns = [
    path("", views.hello),
    path("posts/", views.post_list),
    path('posts/<int:id>/', views.post_detail),

]
