from rest_framework import serializers
from .models import *



class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
        



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['content', 'book', 'reviewer']

    def validate(self, data):
        book = data.get('book')
        reviewer = data.get('reviewer')

        if self.instance is None:
            if Review.objects.filter(book=book, reviewer=reviewer).exists():
                raise serializers.ValidationError("You have already reviewed this book.")
        
        return data