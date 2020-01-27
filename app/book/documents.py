from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Book


@registry.register_document
class BookDocument(Document):
    class Index:
        # Name of index
        name = 'books'
    
    class Django:
        model = Book

        fields = [
            'uuid',
            'title',
            'main_image',
            'price',
            'description' 
        ]