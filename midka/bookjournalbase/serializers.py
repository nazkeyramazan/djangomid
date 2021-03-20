from rest_framework import serializers
from bookjournalbase.models import Book, BookJournalBase, Journal


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournalBase
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    num_pages = serializers.IntegerField(write_only=True)
    genre = serializers.CharField(write_only=True)
    base = serializers.BaseSerializer()
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('id', 'num_pages', 'genre', 'base')


class JournalSerializer(serializers.ModelSerializer):
    role = serializers.IntegerField(write_only=True)
    publisher = serializers.CharField(write_only=True)
    base = serializers.BaseSerializer()
    class Meta:
        model = Journal
        fields = ('id', 'role', 'publisher', 'base')
