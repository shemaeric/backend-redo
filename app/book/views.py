from django.shortcuts import render
from app.book.documents import BookDocument
from rest_framework import (
    generics,
    status,
)
from rest_framework.response import Response
from app.book.serializers import BookSearchSerializer

class SearchBooks(generics.ListCreateAPIView):

    serializer_class = BookSearchSerializer

    # def get_queryset(self):

    #     return self.search


    def search(request):
        q = request.GET.get('q')

        if q:
            books = BookDocument.search().query("match", title=q)
            # response = {
            #     'data': books
            # }
            # return Response(response, status=status.HTTP_201_CREATED)
        else:
            # response = {
            #     'message': 'No books found'
            # }
            books = ''
            # return Response(response, status=status.HTTP_400_bad_request)

        return render(request, 'search/search.html', {'books': books})