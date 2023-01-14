from django.contrib import admin
from django.urls import path
# from api import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import home, create_post
from django.views.generic import TemplateView

app_name = 'api'

urlpatterns = [

    # path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', views.RegisterView.as_view(), name='auth_register'),
    # path('test/', views.testEndPoint, name='test'),
    # path('', views.getRoutes),
    # path('create/', views.add_posts, name='create'),
    # path('all/', views.view_posts, name='all'),
    # path('update/<int:pk>/', views.update_posts, name='update-posts'),
    # path('post/<int:pk>/delete/', views.delete_posts, name='delete-posts'),
    # path('create-post/', views.CreatePost.as_view(), name='create-post'),

    # path('', PostList.as_view(), name='listpost'),
    # path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    # path('author/create/', CreatePost.as_view(), name='createpost'),
    # path('author/edit/postdetail/<int:pk>/', AuthorPostDetail.as_view(), name='authordetailpost'),
    # path('author/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    # path('author/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
    
    path('', home, name="home"),
    path('createpost/<str:pk>', create_post, name='create_post'),

]
