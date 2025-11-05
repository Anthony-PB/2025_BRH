import feedparser
import dateparser
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .models import Source, Article
from .serializers import SourceSerializer, ArticleSerializer


class SourceView(generics.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    # Allow anyone to view sources, but maybe restrict creation in the future
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        # The is_active filter was removed as the field no longer exists
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'sources': serializer.data,
            'count': queryset.count()
        }, status=status.HTTP_200_OK)


class SourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, or deleting a single source instance.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [AllowAny] # Adjust permissions as needed, e.g., IsAdminUser


class ArticleListView(generics.ListAPIView):
    """
    View to list all articles, with optional filtering by source.
    """
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-published_at')
        source_id = self.request.query_params.get('source_id')
        if source_id:
            queryset = queryset.filter(source__id=source_id)
        return queryset


class ArticleDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single article instance.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class BookmarkArticleView(APIView):
    """
    Allows a user to bookmark or unbookmark an article.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, article_id):
        user = request.user
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        article.bookmarked_by.add(user)
        return Response({'message': 'Article bookmarked successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, article_id):
        user = request.user
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        article.bookmarked_by.remove(user)
        return Response({'message': 'Article bookmark removed successfully'}, status=status.HTTP_200_OK)


class LoadFromSource(APIView):
    """
    Endpoint to load the most recent items from the given source's RSS feed.
    This is a utility view and does not save items to the database.
    """
    permission_classes = [AllowAny]

    def get(self, request, source_id, format=None):
        count = int(request.query_params.get('count', 15))
        try:
            source = Source.objects.get(id=source_id)
        except Source.DoesNotExist:
            return Response({'error': 'Source not found'}, status=status.HTTP_400_BAD_REQUEST)

        d = feedparser.parse(source.url)
        out = []

        for entry in d.entries[:count]:
            image_url = None
            if "media_thumbnail" in entry and entry.media_thumbnail:
                image_url = entry.media_thumbnail[0]['url']
            elif "media_content" in entry and entry.media_content:
                image_url = entry.media_content[0]['url']
            elif "enclosures" in entry and entry.enclosures:
                image_url = entry.enclosures[0]['href']

            if not image_url:
                if "image" in d.feed:
                    image_url = d.feed.image.get("href")
                elif "logo" in d.feed:
                    image_url = d.feed.logo
                elif "icon" in d.feed:
                    image_url = d.feed.icon

            out.append({
                'title': entry.get('title'),
                'link': entry.get('link'),
                'date_published': dateparser.parse(entry.get('published')) if entry.get('published') else None,
                'aggregated_at': datetime.now(),
                'image_url': image_url,
            })

        out.sort(key=lambda x: x['date_published'] or datetime.min, reverse=True)
        return Response({'results': out}, status=status.HTTP_200_OK)
