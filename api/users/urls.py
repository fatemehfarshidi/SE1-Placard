from django.urls import path
from .views import register_view
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from .forms import UserLoginForm

app_name = 'users'

urlpatterns = [
    # path('create/', CustomUserCreate.as_view(), name="create_user"),
    path("register/", register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="account/Login.html", form_class=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/user/login/"), name="logout"),

]
