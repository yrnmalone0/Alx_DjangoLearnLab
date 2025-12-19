from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

from django.forms.widgets import PasswordInput, TextInput
from taggit.forms import TagField



# - Register/Create a user (ModelForm)
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# - Authenticate a user (ModelForm)
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']


# - Post Creation Form (ModelForm)
class PostForm(forms.ModelForm):
    tags = TagField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']



# - Comment Form (ModelForm)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']