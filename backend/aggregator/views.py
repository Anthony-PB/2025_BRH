import feedparser
import dateparser
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Source, Article
from .serializers import SourceSerializer, ArticleSerializer

class SourceView(generics.ListCreateAPIView):
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
    
    def list(self, request, *args, **kwargs):
        sources = Source.objects.filter(is_active=True)
        serializer = self.get_serializer(sources, many=True)
        return Response({
            'sources': serializer.data,
            'count': sources.count()
        }, status=status.HTTP_200_OK)
    
class LoadFromSource(APIView):
    """
    Endpoint to load the most recent items from the given source.
    """
    permission_classes = [AllowAny]

    def get(self, request, guid, format=None):
        """
        Gets the most request.data['count'] recent items from the source found by guid.
        """
        count = int(request.query_params.get('count', 10))
        source : Source = Source.objects.get(id=guid)
        d : feedparser.FeedParserDict = feedparser.parse(source.url)
        out = []
        for entry in d.entries[:count]:
            out.append({'title': entry.get('title', None), 
                      'link': entry.get('link', None), 
                      'date_published': dateparser.parse(entry.get('published', None)),
                      'aggregated_at': datetime.now()})
        out.sort(key=lambda x: x['date_published'], reverse=True)
        return Response({'results': out}, status=status.HTTP_200_OK)