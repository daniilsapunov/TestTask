import requests
from django.core.management.base import BaseCommand
from library.models import Book, Author
from datetime import datetime


class Command(BaseCommand):
    help = 'Fetch random books from Google Books API'

    def handle(self, *args, **kwargs):
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=python')
        data = response.json()

        for item in data.get('items', []):
            volume_info = item['volumeInfo']
            title = volume_info.get('title')
            authors = volume_info.get('authors', [])
            published_date = volume_info.get('publishedDate')
            if published_date:
                try:

                    if len(published_date) == 4:
                        publication_date = datetime.strptime(published_date, '%Y').date()
                    else:
                        publication_date = datetime.strptime(published_date, '%Y-%m-%d').date()
                except ValueError:
                    self.stdout.write(self.style.ERROR(f'Invalid date format for: {title}'))
                    continue
            else:
                publication_date = None

            author, created = Author.objects.get_or_create(
                first_name=authors[0].split()[0],
                last_name=authors[0].split()[1] if len(authors[0].split()) > 1 else ''
            )
            Book.objects.create(title=title, author=author, publication_date=publication_date, is_available=True)

        self.stdout.write(self.style.SUCCESS('Books fetched successfully!'))
