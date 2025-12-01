from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import permissions
from rest_framework import filters
from django_filters import rest_framework

"""
Implement a set of generic views for the Book model to handle CRUD operations. This includes:
A ListView for retrieving all books.
A DetailView for retrieving a single book by ID.
A CreateView for adding a new book.
An UpdateView for modifying an existing book.
A DeleteView for removing a book.
"""

"""
Customize the CreateView and UpdateView to ensure they properly handle form submissions and data validation.
Integrate additional functionalities such as permission checks or filters directly into the views using DRF’s built-in features or custom methods.
"""

"""
Apply Django REST Framework’s permission classes to protect API endpoints based on user roles.
For example, restrict CreateView, UpdateView, and DeleteView to authenticated users only, 
while allowing read-only access to unauthenticated users for ListView and DetailView.
"""

"""
Integrate Django REST Framework’s filtering capabilities to allow users to filter the book list 
by various attributes like title, author, and publication_year.
Use DRF’s DjangoFilterBackend or similar tools to set up comprehensive filtering options in your ListView.
"""


class ListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

"""
Enable search functionality on one or more fields of the Book model, such as title and author.
Configure the SearchFilter in your API to allow users to perform text searches on these fields.
"""




