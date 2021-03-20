from django.urls import path
from .views import BookViewSet , JournalViewSet
urlpatterns = [
    # path('book/', ),
    # path('journal/', ),
    path('books/', BookViewSet.as_view({'get': 'list'})),
    path('journals/', JournalViewSet.as_view({'get': 'list'}))

]
