from django.test import TestCase
from .models import Book, Review
from .serializer import ReviewSerializer

class ReviewUnitTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Test Book", author="Author A")

    def test_create_review_success(self):
        data = {
            "content": "Nice book!",
            "book": self.book.id,
            "reviewer": "sample_user"
        }
        serializer = ReviewSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        review = serializer.save()
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.content, "Nice book!")
        self.assertEqual(review.reviewer, "sample_user")

    def test_duplicate_review_fail(self):
        Review.objects.create(book=self.book, reviewer="sample_user", content="Nice book!")
        data = {
            "content": "Trying to submit again",
            "book": self.book.id,
            "reviewer": "sample_user"
        }
        serializer = ReviewSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("You have already reviewed this book.", str(serializer.errors))
