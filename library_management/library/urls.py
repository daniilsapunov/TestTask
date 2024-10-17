from django.urls import path
from library import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/update/<int:pk>/', views.author_update, name='author_update'),
    path('authors/delete/<int:pk>/', views.author_delete, name='author_delete'),

    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),

    path('readers/', views.reader_list, name='reader_list'),
    path('readers/create/', views.reader_create, name='reader_create'),
    path('readers/update/<int:pk>/', views.reader_update, name='reader_update'),
    path('readers/delete/<int:pk>/', views.reader_delete, name='reader_delete'),
]