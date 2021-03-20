from django.db import models
from utils.constants import JOURNAL_TYPE_BULLET , JOURNAL_TYPE_FOOD , JOURNAL_TYPE_SPORT ,JOURNAL_TYPE_TRAVEL ,JOURNAL_TYPES

# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=1000 , verbose_name='Book name')
    price = models.IntegerField( verbose_name='Book price')
    description = models.TextField(verbose_name='Book description')
    created_at = models.DateField(verbose_name='Book creation date')

    class Meta:
        verbose_name = "Base"
        verbose_name_plural = "Bases"
    def __str__(self):
        return self.name

class Book(BookJournalBase):
    num_pages = models.IntegerField(verbose_name="Number of pages" )
    genre = models.CharField(max_length=255, verbose_name='Book genre')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Journal(BookJournalBase):
    role = models.SmallIntegerField(choices=JOURNAL_TYPES, default=JOURNAL_TYPE_TRAVEL)
    publisher = models.CharField( max_length=500 ,  verbose_name='Book publisher')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'