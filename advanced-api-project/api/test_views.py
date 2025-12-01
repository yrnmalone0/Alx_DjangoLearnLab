"""
Focus on testing CRUD operations for the Book model endpoints.
Test the filtering, searching, and ordering functionalities to verify they work as intended.
Ensure that permissions and authentication mechanisms are correctly enforcing access controls.
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Author 1')
        self.book1 = Book.objects.create(title='Book 1', author=self.author, publication_year=2000)
        self.book2 = Book.objects.create(title='Book 2', author=self.author, publication_year=2010)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book 1')

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {'title': 'Book 3', 'author': self.author.id, 'publication_year': 2020}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {'title': 'Book 3', 'author': self.author.id, 'publication_year': 2020}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Updated Book 1', 'author': self.author.id, 'publication_year': 2001}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book 1')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
