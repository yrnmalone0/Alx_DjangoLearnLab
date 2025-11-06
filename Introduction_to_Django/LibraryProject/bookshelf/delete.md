# DELETE BOOK INSTANCE AND CONFIRM DELETION
To delete a book instance in Django, you can use the Django shell or create a view to handle the deletion of book instances. Below are the command and output from Django shell in this module.

**Python Command:**
**__Get the book instance by its primary key (id)__**
```>>> delete_book = Book.objects.get(pk=1)```

**__Delete the book instance__**
```>>> delete_book.delete()```
```(1, {'bookshelf.Book': 1})```

**Expected Output:**
```>>> Book.objects.all()```
```<QuerySet []>```
