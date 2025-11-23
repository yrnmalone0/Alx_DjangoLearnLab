"""Ensure that all your forms use CSRF tokens to protect against CSRF attacks. This involves modifying form templates to include {% csrf_token %}.
Template Modifications:
Update form templates to explicitly include the CSRF token tag if not already present."""

from django import forms
from .models import Book, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.safestring import mark_safe
from django.middleware.csrf import get_token

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def as_p(self):
        """Render the form as HTML <p> elements, including CSRF token."""
        form_html = super().as_p()
        if self.request:
            csrf_token = get_token(self.request)
            csrf_input = f'<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">'
            form_html = mark_safe(csrf_input + form_html)
        return form_html
