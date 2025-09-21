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
        count = int(request.query_params.get('count', 15))
        source: Source = Source.objects.get(id=guid)
        d: feedparser.FeedParserDict = feedparser.parse(source.url)
        out = []

        for entry in d.entries[:count]:
            image_url = None

            # Check media tags
            media = entry.get("media_thumbnail") or entry.get("media_content")
            if media and "url" in media[0]:
                image_url = media[0]["url"]

            # Check enclosures
            if not image_url:
                enclosures = entry.get("enclosures")
                if enclosures and len(enclosures) > 0 and "href" in enclosures[0]:
                    image_url = enclosures[0]["href"]

            # Fallback to feed-level image/logo/icon
            if not image_url:
                if "image" in d.feed and "href" in d.feed.image:
                    image_url = d.feed.image["href"]
                elif "logo" in d.feed:
                    image_url = d.feed.logo
                elif "icon" in d.feed:
                    image_url = d.feed.icon

            out.append({
                'title': entry.get('title', None),
                'link': entry.get('link', None),
                'date_published': dateparser.parse(entry.get('published', None)),
                'aggregated_at': datetime.now(),
                'image_url': image_url,   # ✅ now included
            })

        out.sort(key=lambda x: x['date_published'], reverse=True)
        return Response({'results': out}, status=status.HTTP_200_OK)
