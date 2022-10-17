from django.shortcuts import render
from .models import Review
from .models import Book

# Create your views here.
def index(request):
    """The home page for dBook"""
    return render(request, 'BookApp/index.html')

def reviews(request):
    """Show all reviews"""
    reviews = Review.objects.order_by('date_added')
    context = {'reviews' : reviews}
    return render(request, 'BookApp/reviews.html', context)

def review(request, review_id):
    """Show a single review and all its entries."""
    review = Review.objects.get(id=review_id)
    entries = Review.objects.order_by('-date_added')
    context = {'review': review, 'entries': entries}
    return render(request, 'BookApp/review.html', context)

def books(request):
    """Show all books"""
    books = Book.objects.order_by('date_added')
    context = {'books' : books}
    return render(request, 'BookApp/books.html', context)

def book(request, book_id):
    """Show a single book and all its entries."""
    book = Book.objects.get(id=book_id)
    entries = Book.objects.order_by('-date_added')
    context = {'book': book, 'entries': entries}
    return render(request, 'BookApp/book.html', context)