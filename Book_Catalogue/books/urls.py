from django.urls import path
from books import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'), #Captures whatever integer is in the URL and passes it into the view as pk (books/1/ , book/2/, book/3/  etc) achieved through leveraging the primary key (PK) 
    path('add/', views.add_book, name='add_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
]