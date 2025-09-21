from rest_framework import serializers
from .models import Source, Article

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name','url', 'category', 'is_rss'] 
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['last_scraped'] = instance.last_scraped
        return data

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'summary', 'author', 'original_url', 
            'published_at', 'scraped_at', 'source', 'tags'
        ]