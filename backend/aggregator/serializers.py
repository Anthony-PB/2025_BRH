from rest_framework import serializers
from .models import Source, Article


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'url', 'category', 'is_rss', 'last_scraped']
        read_only_fields = ['last_scraped']


class ArticleSerializer(serializers.ModelSerializer):
    # Make the source field read-only and show its string representation
    source = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'summary', 'author', 'original_url',
            'published_at', 'scraped_at', 'source', 'tags', 'bookmarked_by'
        ]
        # bookmarked_by is a ManyToMany field, it's good to make it read-only
        # in the general serializer to avoid accidental updates.
        read_only_fields = ['scraped_at', 'bookmarked_by']
