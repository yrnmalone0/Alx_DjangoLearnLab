# CRUD Operation Commands and outputs for Book Model in Django

This document provides the commands and expected outputs for performing CRUD (Create, Retrieve, Update, Delete) operations on the Book model in a Django application. Each section corresponds to a specific CRUD operation.

## 1. Create a Book Instance

**Python Command:**
```>>> create_book = Book(title = "1984", author = "George Orwell", publication_year = "1949")```
```>>> create_book.save()```

**Output:**
```>>> <QuerySet [<Book: 1984>]>```


## 2. Retrieve and Display All Attributes of the Book

**Python Command:**
```>>> Book.objects.all()```

**Output:**
```>>> <QuerySet [<Book: 1984>]>```


## 3. Update Title Attribute of the Book

**Python Command:**
**__Get the book instance by its primary key (id)__**
```>>> update_book = Book.objects.get(pk=1)```

**__Update the title attribute and save the changes__**
```>>> update_book.title = 'Nineteen Eighty-Four'```
```>>> update_book.save()```

**Output:**
```>>> Book.objects.all()```
```<QuerySet [<Book: Nineteen Eighty-Four>]>```


## 4. Delete Book Instance and Confirm Deletion

**Python Command:**
**__Get the book instance by its primary key (id)__**
```>>> delete_book = Book.objects.get(pk=1)```

**__Delete the book instance__**
```>>> delete_book.delete()```
```(1, {'bookshelf.Book': 1})```

**Output:**
```>>> Book.objects.all()```
```<QuerySet []>```