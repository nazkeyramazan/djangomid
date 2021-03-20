from django.contrib import admin
from bookjournalbase.models import Book , BookJournalBase , Journal

# Register your models here.
admin.site.register(BookJournalBase)
admin.site.register(Book)
admin.site.register(Journal)
