from .models import Book, Library
# Query all books by a specific author.
Book.objects.filter(authors_name = "John Doe")

# List all books in a library.
library = Library.objects.get(name="Central Library")
library.books.all()

# Retrieve the librarian for a library.
librarian = library.name