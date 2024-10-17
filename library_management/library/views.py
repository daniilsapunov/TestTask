from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, Reader
from .forms import AuthorForm, BookForm, ReaderForm

# Author CRUD
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'library/author_form.html', {'form': form})

# Book CRUD
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

# Reader CRUD
def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'library/reader_list.html', {'readers': readers})

def reader_create(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm()
    return render(request, 'library/reader_form.html', {'form': form})