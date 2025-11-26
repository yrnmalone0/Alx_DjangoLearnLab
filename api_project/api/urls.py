from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view({'get': 'list'}), name='book-list'),  # Maps to the BookList view
    path('books/<int:pk>/', BookList.as_view({'get': 'retrieve'}), name='book-detail'),  # Detail view for a single book
]