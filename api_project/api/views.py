from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookList(viewsets.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer