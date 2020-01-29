from django.core.exceptions import ValidationError
from rest_framework import serializers
from app.book.models import Book


class BookSearchSerializer(serializers.ModelSerializer):
    """
        Handle all the search serializers
    """

    class Meta:
        model = Book
        fields = ('__all__')