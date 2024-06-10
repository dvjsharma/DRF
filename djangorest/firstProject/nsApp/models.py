from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')