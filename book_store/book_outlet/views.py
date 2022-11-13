from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })


def book_details(request, slug):
    # try:
    #     book = Book.objects.get(pk=slug)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_details.html", {
        "title": book.title,
        "author": book.author,
        "is_bestselling": book.is_bestselling,
        "rating": book.rating
    }
    )
