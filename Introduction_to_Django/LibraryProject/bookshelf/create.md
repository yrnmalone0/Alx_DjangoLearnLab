# Create a Book Instance
To create a book instance in Django, you can use the Django shell or create a view to handle the creation of book instances. Below are the command and output from Django shell in this module.

**Python Command:**
```
Book.objects.create(title = "1984", author = "George Orwell", publication_year = "1949")

```

**Expected Output:**
In this case, there is no direct output from the save() method, but the book instance is created and saved to the database. Also, you can verify to see it **id** assigned to the instance.

```
create_book.id

```




