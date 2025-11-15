from django.shortcuts import render
from django.views.generic.detail import DetailView
from . models import Book
from .models import Library
from LibraryProject import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import Login
from django.urls import reverse_lazy
from django.views.generic import CreateView

# function-based view that lists all books stored in db
def book_list(request):
    """Retrieves all books and renders a template displaying the list"""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list' : books}  #create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

# class-based view that displays details for a specific library, listing all books 
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the library."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object()  # Retrieve the current library instance
        context['books'] = library.books.all()  # Add books related to the library
        return context
        

# Utilize Django’s built-in views and forms for handling user authentication. You will need to create views for user login, logout, and registration.

# Registration view
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


# Login and logout views can be handled using Django's built-in views, so no need to redefine them here.
class LoginView(views.LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(views.LogoutView):
    template_name = 'relationship_app/logged_out.html'



