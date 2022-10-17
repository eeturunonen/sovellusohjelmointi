from unittest.util import _MAX_LENGTH
from django.db import models

class Book(models.Model):
    """A topic the user is learning about."""

    name = models.CharField(max_length = 200)                       # This is the name of the book
    authors = models.JSONField(max_length = 200)                    # Authors who wrote the book
    year_published = models.IntegerField()                          # Year when the book is published
    date_added = models.DateTimeField(auto_now_add=True)            # Timestamp when the book is addedd to the library
    date_modified = models.DateTimeField(auto_now_add=True)         # Timestamp when the book is modified


    def __str__(self):                                          # Represents the book model
        """Return a string reprenstation of the model."""
        return self.name

class Review(models.Model):

    my_review = models.TextField()                                  # Holds the author of the review 
    stars = models.IntegerField()                                   # How many stars this book has as review, the lower the number, the worse it is
    unfinished = models.BooleanField()                              # Wether the book is ready or still under progress
    date_added = models.DateTimeField(auto_now_add=True)            # Timestamp when the book is addedd to the library
    date_modified = models.DateTimeField(auto_now_add=True)         # Timestamp when the book is modified
    book = models.ForeignKey(Book, on_delete=models.CASCADE)        # Deletes the object and all the stored data of it

    def __str__(self):                                          # Represents the review model
        """Return a string representation of the model."""
        return f"{self.my_review[:50]}..."

