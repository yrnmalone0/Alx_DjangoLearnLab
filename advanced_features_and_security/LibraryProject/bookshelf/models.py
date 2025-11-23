from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    
    def __str__(self):
        return self.title

# Create a custom user model by extending AbstractUser,
# adding custom fields (date_of_birth: A date field, profile_photo: An image field)
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)


"""
Implement a custom user manager that handles user creation and queries, ensuring it can manage the added fields effectively.

Custom Manager Functions to Implement:
create_user: Ensure it handles the new fields correctly.
create_superuser: Ensure administrative users can still be created with the required fields.
"""
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


#Create permissions such as can_view, can_create, can_edit, and can_delete
class Meta:
    permissions = [
        ("can_view", "Can view user"),
        ("can_create", "Can create user"),
        ("can_edit", "Can edit user"),
        ("can_delete", "Can delete user"),
    ]

