from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    #path("", views.home_page),
    #path("register/", views.register_request, name="register"),
    #path("login/", views.login_request, name="login"),
    #path('logout/', views.logoutUser, name="logout"),
    #path("posts/", views.post_list),
    #path('posts/<int:id>/', views.post_detail),

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    path('create/', views.add_posts, name='create'),
    path('all/', views.view_posts, name='all'),
    path('update/<int:pk>/', views.update_posts, name='update-posts'),
    path('post/<int:pk>/delete/', views.delete_posts, name='delete-posts'),

]
