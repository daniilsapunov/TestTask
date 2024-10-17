from django.core.management.base import BaseCommand
from library.models import Author, Book, Reader
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate the database with authors, books, and readers'

    def handle(self, *args, **kwargs):
        authors = [
            ("J.K.", "Rowling"),
            ("George", "Orwell"),
            ("J.R.R.", "Tolkien"),
            ("Isaac", "Asimov"),
            ("Agatha", "Christie"),
        ]

        books = [
            ("Harry Potter and the Sorcerer's Stone", "1997-06-26", True),
            ("1984", "1949-06-08", True),
            ("The Hobbit", "1937-09-21", True),
            ("Foundation", "1951-06-01", False),
            ("Murder on the Orient Express", "1934-01-01", True),
        ]

        readers = [
            ("Alice", "Smith"),
            ("Bob", "Johnson"),
            ("Charlie", "Williams"),
            ("Diana", "Brown"),
            ("Edward", "Jones"),
        ]

        for first_name, last_name in authors:
            author = Author.objects.create(first_name=first_name, last_name=last_name)
            self.stdout.write(self.style.SUCCESS(f'Created author: {author}'))

        for title, pub_date, is_available in books:
            author = random.choice(Author.objects.all())
            book = Book.objects.create(title=title, author=author,
                                       publication_date=datetime.strptime(pub_date, "%Y-%m-%d"),
                                       is_available=is_available)
            self.stdout.write(self.style.SUCCESS(f'Created book: {book}'))

        for first_name, last_name in readers:
            reader = Reader.objects.create(first_name=first_name, last_name=last_name)
            self.stdout.write(self.style.SUCCESS(f'Created reader: {reader}'))

            read_books = random.sample(list(Book.objects.all()), k=random.randint(1, 3))
            reader.read_books.set(read_books)
            self.stdout.write(self.style.SUCCESS(f'{reader} has read: {", ".join([str(b) for b in read_books])}'))