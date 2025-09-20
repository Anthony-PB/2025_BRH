from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .serializers import ArticleSerializer
from core import db_utils
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the index.")



class ArticleListCreateView(generics.ListCreateAPIView):
    """
    A Generic View adapted for a non-ORM (PyMongo) backend.
    """
    # serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # We don't define 'queryset' because we don't have an ORM QuerySet.

    # --- Override for GET (List) ---
    def get_queryset(self):
        """
        Instead of using a 'queryset' attribute, we override this method
        to provide the list of objects directly from our db_utils.
        """
        return db_utils.get_all_articles()

    # --- Override for POST (Create) ---
    def perform_create(self, serializer):
        """
        The default 'perform_create' calls serializer.save(), which tries
        to save to a Django model. We override it to call our custom
        db_utils function instead.
        """
        # The serializer has already validated the data at this point.
        # We pass the validated data to our database function.
        db_utils.create_article(serializer.validated_data)