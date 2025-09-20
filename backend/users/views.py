from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import PydanticUserRegistrationSerializer
from core import db_utils

# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    """
    An API endpoint that allows new users to be created.
    Uses the CreateAPIView for a clean, single-purpose implementation.
    """
    serializer_class = PydanticUserRegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """
        The default 'perform_create' calls serializer.save(), which tries
        to save to a Django model. We override it to call our custom
        db_utils function instead.
        """
        serializer.save()

