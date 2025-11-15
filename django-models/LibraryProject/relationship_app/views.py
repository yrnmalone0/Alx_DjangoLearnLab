from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from . models import Book
from .models import Library
from LibraryProject import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import Login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in automatically after registration
            return redirect('home')  # Redirect to a homepage or a specific page after registration
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


# Login and logout views can be handled using Django's built-in views, so no need to redefine them here.
class LoginView(views.LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(views.LogoutView):
    template_name = 'relationship_app/logged_out.html'



"""Create three separate views to manage content access based on user roles:

Views to Implement:

An ‘Admin’ view that only users with the ‘Admin’ role can access, the name of the file should be admin_view
A ‘Librarian’ view accessible only to users identified as ‘Librarians’. The file should be named librarian_view
A ‘Member’ view for users with the ‘Member’ role, the name of the file should be member_view
Access Control:

Utilize the @user_passes_test decorator to check the user’s role before granting access to each view."""

from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile 
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')  

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Signal to create a UserProfile whenever a new User is created."""
    if created:
        UserProfile.objects.create(user=instance)


"""Update Views to Enforce Permissions
Adjust your views to check if a user has the necessary permissions before allowing them to perform create, update, or delete operations.

Views to Modify:
Use Django’s permission_required decorator to secure views that add, edit, or delete books.
For each view, apply the corresponding permission."""


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Logic to add a book
    pass
      
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass    

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    # Logic to delete a book
    pass