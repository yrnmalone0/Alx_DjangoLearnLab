# CRUD Operation Commands and outputs for Book Model in Django

This document provides the commands and expected outputs for performing CRUD (Create, Retrieve, Update, Delete) operations on the Book model in a Django application. Each section corresponds to a specific CRUD operation.

## 1. Create a Book Instance

**Python Command:**
```
Book.objects.create(title = "1984", author = "George Orwell", publication_year = "1949")

```

**Output:**
```
<Book: 1984>

```

## 2. Retrieve and Display All Attributes of the Book

**Python Command:**
```
Book.objects.get()

```

**Output:**
```
<Book: 1984>

```

## 3. Update Title Attribute of the Book

**Python Command:**
```
update_book = Book.objects.get(pk=1)
update_book.title = 'Nineteen Eighty-Four'
update_book.save()

```

**Output:**
```
Book.objects.all()
<Book: 1984>

```

## 4. Delete Book Instance and Confirm Deletion

**Python Command:**
```
delete_book = Book.objects.get(pk=1)
delete_book.delete()

(1, {'bookshelf.Book': 1})

```

**Output:**
```
Book.objects.get()

<QuerySet []>

```