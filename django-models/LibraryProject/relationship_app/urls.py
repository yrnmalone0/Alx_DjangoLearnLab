from django.urls import path
from . import views
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

"""Define URL patterns that will route to the newly created role-specific views. Ensure that each URL is correctly linked to its respective view and that the URLs are named for easy reference.

URLs to Define:
A URL for the ‘Admin’ view.
A URL for the ‘Librarian’ view.
A URL for the ‘Member’ view."""

"""
Create distinct paths for adding, editing, and deleting books.
Link each path to its respective view with the appropriate permissions.
"""

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('admin-view/', views.admin_view, name='admin-view'),
    path('librarian-view/', views.librarian_view, name='librarian-view'),
    path('member-view/', views.member_view, name='member-view'),
    path('book/add_book/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit_book/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete_book/', views.delete_book, name='delete_book'),
]