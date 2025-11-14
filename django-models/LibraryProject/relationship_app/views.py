from django.shortcuts import render
from . models import Book
from LibraryProject import views

# function-based view that lists all books stored in db
def book_list(request):
    """Retrieves all books and renders a template displaying the list"""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list' : books}  #create a context dictionary with book list
    return render(request, 'books/list_books.html', context)