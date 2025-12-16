from django.urls import path

from . import views
from .views import CreateView, ListView, DetailView, UpdateView

urlpatterns = [
    path('', views.homepage, name=""),
    path('register/', views.user_registration, name="register"),
    path('user-login', views.user_login, name="user-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('profile', views.profile, name="profile"),
    path('posts/new/', CreateView.as_view(), name="create-post"),
    path('posts/', ListView.as_view(), name="posts"),
    path('posts/<int:pk>/', DetailView.as_view(), name="post-detail"),
    path('posts/<int:pk>/edit/', UpdateView.as_view(), name="update-post"),
    #path('posts/<int:pk>/delete/', DeletePost.as_view(), name="delete-post"),
]