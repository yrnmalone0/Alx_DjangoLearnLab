from .models import Book, Library, Librarian
# Query all books by a specific author.
Book.objects.filter(authors_name = "John Doe")

# List all books in a library.
Library.objects.get(name=library_name)


# Retrieve the librarian for a library.
librarian = Library.objects.get(name="Central Library").librarian