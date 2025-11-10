from .models import Book, Library, Librarian, Author
# Query all books by a specific author.
Author.objects.get(name = author_name).objects.filter(author=author)

# List all books in a library.
Library.objects.get(name=library_name).books.all()


# Retrieve the librarian for a library.
librarian = Library.objects.get(name="Central Library").librarian