from django.urls import path
from .views import register_view, login_view, logout_user

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import LoginForm

app_name = 'users'

urlpatterns = [

	path('register/', register_view, name="register"),
	path("logout/", auth_views.LogoutView.as_view(next_page="/user/login/"), name="logout"),
	    path(
        "login/",
        auth_views.LoginView.as_view(template_name="Login.html", next_page="/api/", form_class=LoginForm),
        name="login",
    ),

]
