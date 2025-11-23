# from django.shortcuts import render
# from django.contrib.auth.models import Group, Permission
#
# """
# Set up user groups in Django and assign the newly created permissions to these groups. Use Django’s admin site to manage these groups and their permissions.
#
# Groups to Setup:
# Create groups like Editors, Viewers, and Admins.
# Assign appropriate permissions to each group. For example, Editors might have can_edit and can_create permissions.
# """
#
# def setup_user_groups():
#     editors, created = Group.objects.get_or_create(name='Editors')
#     viewers, created = Group.objects.get_or_create(name='Viewers')
#     admins, created = Group.objects.get_or_create(name='Admins')
#
#     can_view = Permission.objects.get(codename='can_view')
#     can_create = Permission.objects.get(codename='can_create')
#     can_edit = Permission.objects.get(codename='can_edit')
#     can_delete = Permission.objects.get(codename='can_delete')
#
#     editors.permissions.add(can_create, can_edit)
#     viewers.permissions.add(can_view)
#     admins.permissions.add(can_view, can_create, can_edit, can_delete)
#
#
# """
# Modify your views to check for these permissions before allowing users to perform certain actions. Use decorators such as permission_required to enforce these permissions in your views.
#
# Views to Modify or Create:
# Ensure views that create, edit, or delete model instances check for the correct permissions.
# Example: Use @permission_required('app_name.can_edit', raise_exception=True) to protect an edit view.
#  """
# from django.contrib.auth.decorators import permission_required
# from django.http import HttpResponseForbidden
# from .models import Book
# @permission_required('bookshelf.can_edit', raise_exception=True)
# def edit_book(request, book_id):
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         return HttpResponseForbidden("You do not have permission to edit this book.")
#
#     if request.method == 'POST':
#         book.title = request.POST.get('title')
#         book.author = request.POST.get('author')
#         book.publication_year = request.POST.get('publication_year')
#         book.save()
#         return render(request, 'bookshelf/book_detail.html', {'book': book})
#
#     return render(request, 'bookshelf/edit_book.html', {'book': book})
#
#
# @permission_required('bookshelf.can_view', raise_exception=True)
#
# def view_book(request, book_id):
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         return HttpResponseForbidden("You do not have permission to view this book.")
#
#     return render(request, 'bookshelf/book_detail.html', {'book': book})
#
# @permission_required('bookshelf.can_create', raise_exception=True)
# def create_book(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         publication_year = request.POST.get('publication_year')
#         book = Book.objects.create(title=title, author=author, publication_year=publication_year)
#         return render(request, 'bookshelf/book_detail.html', {'book': book})
#
#     return render(request, 'bookshelf/create_book.html')
#
#
# @permission_required('bookshelf.can_delete', raise_exception=True)
# def delete_book(request, book_id):
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         return HttpResponseForbidden("You do not have permission to delete this book.")
#
#     if request.method == 'POST':
#         book.delete()
#         return render(request, 'bookshelf/book_deleted.html')
#
#     return render(request, 'bookshelf/confirm_delete.html', {'book': book})
#


from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book

# ----------------------------------------------------
# GROUP SETUP
# ----------------------------------------------------
def setup_user_groups():
    editors, created = Group.objects.get_or_create(name='Editors')
    viewers, created = Group.objects.get_or_create(name='Viewers')
    admins, created = Group.objects.get_or_create(name='Admins')

    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    editors.permissions.add(can_create, can_edit)
    viewers.permissions.add(can_view)
    admins.permissions.add(can_view, can_create, can_edit, can_delete)

# ----------------------------------------------------
# REQUIRED book_list VIEW (you were missing this)
# ----------------------------------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ----------------------------------------------------
# VIEW A BOOK
# ----------------------------------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponseForbidden("You do not have permission to view this book.")

    return render(request, 'bookshelf/book_detail.html', {'book': book})

# ----------------------------------------------------
# EDIT BOOK
# ----------------------------------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponseForbidden("You do not have permission to edit this book.")

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return render(request, 'bookshelf/book_detail.html', {'book': book})

    return render(request, 'bookshelf/edit_book.html', {'book': book})

# ----------------------------------------------------
# CREATE BOOK
# ----------------------------------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        book = Book.objects.create(title=title, author=author, publication_year=publication_year)
        return render(request, 'bookshelf/book_detail.html', {'book': book})

    return render(request, 'bookshelf/create_book.html')

# ----------------------------------------------------
# DELETE BOOK
# ----------------------------------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponseForbidden("You do not have permission to delete this book.")

    if request.method == 'POST':
        book.delete()
        return render(request, 'bookshelf/book_deleted.html')

    return render(request, 'bookshelf/confirm_delete.html', {'book': book})

