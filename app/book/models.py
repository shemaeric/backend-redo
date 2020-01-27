# from django.db import models
from __future__ import unicode_literals
from djongo import models

class Book(models.Model):

    uuid = models.CharField(max_length = 40, null = False)
    title = models.CharField(max_length = 40, null = False)
    main_image = models.CharField(max_length = 40, null = False)
    price = models.IntegerField(null = False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        """Saves all the changes of the Book model"""
        super().save(*args, **kwargs)


    def __str__(self):
        self.uuid





