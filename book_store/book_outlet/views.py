from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-title")
    num_book = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_book,
        "average_rating": avg_rating
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
