from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import Book, Review
from .serializer import BookSerializer, ReviewSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



class BookListCreateAPIView(APIView):
    def get(self, request):
        try:
            books_data = cache.get("books_list")
            
            if books_data is None:
                books = Book.objects.all()
                
                if not books.exists():
                    return Response({"message": "Books not available"}, status=status.HTTP_200_OK)

                serializer = BookSerializer(books, many=True)
                books_data = serializer.data

                cache.set("books_list", books_data, timeout=60)

            return Response(books_data, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Redis error: {e}")

            books = Book.objects.prefetch_related('reviews').all()


            if not books.exists():
                return Response({"message": "Books not available"}, status=status.HTTP_200_OK)

            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete("books_list")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewListCreateAPIView(APIView):
    def get(self, request, book_id):
        reviews = Review.objects.filter(book_id=book_id)
        serializer = ReviewSerializer(reviews,many=True)
        return Response(serializer.data)

    def post(self, request, book_id):
        data = request.data.copy()
        data["book"] = book_id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            review = serializer.save()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "reviews",
                {
                    "type": "send.review",
                    "review": {
                        "content": review.content,
                        "book": review.book.title,
                        "reviewer": review.reviewer,
                    }
                }
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


