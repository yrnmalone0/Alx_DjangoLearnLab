# Updating Title Attribute of the Book
To update the title attribute of a book instance in Django, you can use the Django shell or create a view to handle the update of book instances. Below are the command and output from Django shell in this module.

**Python Command:**
**__Get the book instance by its primary key (id)__**
```
update_book = Book.objects.get(pk=1)

```

**__Update the title attribute and save the changes__**
```
update_book.title = 'Nineteen Eighty-Four'
update_book.save()

```

**Expected Output:**
```
Book.objects.get()

<Book: 1984>

```
