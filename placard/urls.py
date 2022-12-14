from django.contrib import admin
from django.urls import path, include
from brick import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("brick/", include("brick.urls")),
    path("register/", views.register_request, name="register"),
    path.("login/", views.login_request, name="login"),
]
