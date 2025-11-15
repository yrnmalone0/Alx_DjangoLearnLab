from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=250)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Library(models.Model):
    name = models.CharField(max_length=250)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
    
class Librarian(models.Model):
    name = models.CharField(max_length=250)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""Create a UserProfile model that includes a role field with predefined roles. This model should be linked to Django’s built-in User model with a one-to-one relationship.

Fields Required:
user: OneToOneField linked to Django’s User.
role: CharField with choices for ‘Admin’, ‘Librarian’, and ‘Member’."""

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

#Automatic Creation: Use Django signals to automatically create a UserProfile when a new user is registered.

