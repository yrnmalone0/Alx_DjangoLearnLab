from django.urls import path

from . import views
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, CommentCreateView, CommentListView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', views.homepage, name=""),
    path('register/', views.user_registration, name="register"),
    path('user-login', views.user_login, name="user-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('profile', views.profile, name="profile"),
    path('post/new/', PostCreateView.as_view(), name="create-post"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="update-post"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="delete-post"),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name="comment"),
    path('post/<int:post_id>/comments/', CommentListView.as_view(), name="comments"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name="edit-comment"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="delete-comment"),
]