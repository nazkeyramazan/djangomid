from .models import Book , BookJournalBase ,Journal
from django.shortcuts import get_object_or_404
from bookjournalbase.serializers import BaseSerializer , BookSerializer , JournalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser , AllowAny

from rest_framework.response import Response

class BookViewSet(viewsets.ViewSet ) :
    permission_classes = (IsAdminUser,)
    serializer_class =BookSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        base = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(base)
        return Response(serializer.data)


    def create(self, request):
        pass
    def update(self, request, pk=None):
        pass

class JournalViewSet(viewsets.ViewSet ) :
    permission_classes = (IsAdminUser,)
    serializer_class = JournalSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]
    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        base = get_object_or_404(queryset, pk=pk)
        serializer = JournalSerializer(base)
        return Response(serializer.data)


    def create(self, request):
        pass
    def update(self, request, pk=None):
        pass