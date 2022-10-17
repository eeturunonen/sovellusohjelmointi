from django.urls import path
from . import views

app_name = 'BookApp'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all reviews
    path('reviews/', views.reviews, name='reviews'),
    # Detail page for a single review.
    path('reviews/<int:review_id>/', views.review, name='review'),
    # Page that shows all books
    path('books/', views.books, name='books'),
    # Detail page for a single book.
    path('books/<int:book_id>/', views.book, name='book'),
]
