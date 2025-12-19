from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

from django.forms.widgets import PasswordInput, TextInput
from taggit.forms import TagWidget  # Import TagWidget from django-taggit
from taggit.models import Tag  # Import Tag model from django-taggit



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
    tags = forms.CharField(
        widget=TagWidget(),  # Use TagWidget to display tag input field
        required=False  # Tags are optional in this case
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        """
        Overriding the save method to handle tags properly.
        If the tags are entered, they will be processed and saved.
        """
        post = super().save(commit=False)
        # Process the tags
        tag_names = self.cleaned_data['tags']
        if tag_names:
            tags = [tag.strip() for tag in tag_names.split(',')]  # Split tags by comma
            post.save()  # Save the post first
            post.tags.add(*tags)  # Add tags to the post
        if commit:
            post.save()
        return post


# - Comment Form (ModelForm)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']