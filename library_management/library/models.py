from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.CharField(null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    read_books = models.ManyToManyField(Book, related_name='readers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"