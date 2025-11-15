from django.shortcuts import render
from django.views.generic import DetailView
from . models import Book
from LibraryProject import views

# function-based view that lists all books stored in db
def book_list(request):
    """Retrieves all books and renders a template displaying the list"""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list' : books}  #create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

# class-based view that displays details for a specific library, listing all books 
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        book = self.get_object()  # Retrieve the current book instance
        context['authors'] = book.authors.all()  # Add authors related to the book
        return context
