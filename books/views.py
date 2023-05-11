from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializer import BookSerializer
from .pagination import DefaultPagination


class BookViewSet(ModelViewSet):
    # queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author', 'publisher']
    ordering_fields = ['title', 'author', 'publication_year']

    def get_queryset(self):
        queryset = Book.objects.all()
        if self.request.query_params.get('available') == 'true':
            return Book.objects.filter(number_of_available_copies__gt=0)
        return queryset

    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        book = self.get_object()
        num_copies = int(request.data.get('num_copies', 1))
        if book.number_of_available_copies > num_copies:
            book.number_of_available_copies -= num_copies
            book.save()
            serializer = self.get_serializer(book)
            return Response(serializer.data)
        return Response({'detail': f'Only {book.num_of_available_copies} copies of this book are available'},
                        status=status.HTTP_400_BAD_REQUEST)



