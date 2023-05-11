from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    number_of_copies = models.IntegerField()
    number_of_available_copies = models.IntegerField()

    def __str__(self):
        return self.title, self.author

