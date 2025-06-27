from rest_framework.test import APITestCase
from django.core.cache import cache
from django.urls import reverse
from .models import Book

class BookCacheIntegrationTest(APITestCase):
    def setUp(self):
        cache.clear()
        self.book = Book.objects.create(title="Cache Test Book", author="Test Author")
        self.url = reverse("book-list") 

    def test_cache_not_available(self):
        self.assertIsNone(cache.get("books_list"))
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Cache Test Book")

        cached_data = cache.get("books_list")
        self.assertIsNotNone(cached_data)
        self.assertEqual(cached_data[0]['title'], "Cache Test Book")
