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

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'library/author_confirm_delete.html', {'author': author})

# Book CRUD
def book_list(request):
    authors = Author.objects.all()  # Получаем всех авторов для фильтрации
    selected_author = request.GET.get('author')  # Получаем выбранного автора из параметров запроса
    books = Book.objects.all()  # Получаем все книги

    if selected_author:
        books = books.filter(author_id=selected_author)  # Фильтруем книги по автору

    return render(request, 'library/book_list.html', {'books': books, 'authors': authors, 'selected_author': selected_author})
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})

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

def reader_update(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        form = ReaderForm(request.POST, instance=reader)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm(instance=reader)
    return render(request, 'library/reader_form.html', {'form': form})
def reader_delete(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        reader.delete()
        return redirect('reader_list')
    return render(request, 'library/reader_confirm_delete.html', {'reader': reader})