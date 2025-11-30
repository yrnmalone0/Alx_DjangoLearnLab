"""
Serializer Details:

Create a BookSerializer that serializes all fields of the Book model.
Create an AuthorSerializer that includes:
The name field.
A nested BookSerializer to serialize the related books dynamically.
Validation Requirements:

Add custom validation to the BookSerializer to ensure the publication_year is not in the future.
"""
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#api/serializers.py doesn't contain: ["(many=True, read_only=True)"]

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['name', 'books']

    def get_books(self, obj):
        books = obj.books.all()
        return BookSerializer(books, many=True, read_only=True)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value