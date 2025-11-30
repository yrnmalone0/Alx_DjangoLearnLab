"""
Configure URL patterns in api/urls.py to connect the aforementioned views with specific endpoints.
Each view should have a unique URL path corresponding to its function
(e.g., /books/ for the list view, /books/<int:pk>/ for the detail view).

"""

from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView


urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:id>/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/<int:id>/update/', UpdateView.as_view(), name='book-update'),
    path('books/<int:id>/delete/', DeleteView.as_view(), name='book-delete'),
]