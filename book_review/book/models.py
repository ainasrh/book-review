from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', db_index=True)
    content = models.TextField()
    reviewer= models.CharField()


    def __str__(self):
        return f"Review for {self.book.title} "
