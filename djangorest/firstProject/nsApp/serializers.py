from .models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) #read only means we can't create a new book object from author object
    class Meta:
        model = Author
        fields = '__all__'