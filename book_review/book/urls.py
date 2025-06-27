from django.urls import path
from .views import *

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(),name="book-list"),
    path("books/<int:book_id>/reviews/", ReviewListCreateAPIView.as_view(), name="book-reviews"),

]
