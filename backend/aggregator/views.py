import feedparser
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Source, Article
from .serializers import SourceSerializer, ArticleSerializer

class SourceView(generics.CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        source = serializer.save()

        return Response({
            'message': 'Source created successfully',
            'source': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    def getAll(self, request, *args, **kwargs):
        sources = Source.objects.filter(is_active=True)
        serializer = self.get_serializer(sources, many=True)
        return Response({
            'sources': serializer.data,
            'count': sources.count()
        }, status=status.HTTP_200_OK)