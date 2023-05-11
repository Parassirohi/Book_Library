from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "publisher",
                  "publication_year", "number_of_copies", "number_of_available_copies"]
