from django.urls import path

from . import views
from .views import CreateView, ListView, DetailView, UpdateView, DeleteView

urlpatterns = [
    path('', views.homepage, name=""),
    path('register/', views.user_registration, name="register"),
    path('user-login', views.user_login, name="user-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('profile', views.profile, name="profile"),
    path('post/new/', CreateView.as_view(), name="create-post"),
    path('posts/', ListView.as_view(), name="posts"),
    path('post/<int:pk>/', DetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', UpdateView.as_view(), name="update-post"),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name="delete-post"),
]