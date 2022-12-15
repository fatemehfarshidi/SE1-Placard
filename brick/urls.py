from django.contrib import admin
from django.urls import path
from brick import views

urlpatterns = [
    path("", views.hello),
]
