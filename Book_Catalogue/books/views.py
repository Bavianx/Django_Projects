from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def book_list(request):
    books = Book.objects.all()  #Only grabs the LIST of books rather than individual books (Displays all content)
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)  #Grabs a SINGULAR book by the primary key identifier similar to ( self.stocks[ticker] where we take the ticker from the main body ) 
    return render(request, 'books/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':        # user submitted the form
        form = BookForm(request.POST)   # get the submitted data
        if form.is_valid():             # validate the data
            form.save()                 # save to database
            return redirect('/books/')  # go back to book list
    else:
        form = BookForm()               # empty form for GET request
    
    return render(request, 'books/add_book.html', {'form': form})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('/books/')

def edit_book(request, pk):
    book = Book.objects.get(pk=pk)  # get existing book
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # update existing
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm(instance=book)  # pre-fill with existing data
    return render(request, 'books/edit_book.html', {'form': form})