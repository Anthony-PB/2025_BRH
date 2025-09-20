from django.db import models
from django.contrib.auth import get_user_model
from django_mongodb_backend.fields import ObjectIdAutoField, EmbeddedModelField
from django_mongodb_backend.models import EmbeddedModel

User = get_user_model()

class SourceInfo(EmbeddedModel):
    """Embedded source information"""
    name = models.CharField(max_length=200)
    base_url = models.URLField()
    category = models.CharField(max_length=100, blank=True)
    
    class Meta:
        abstract = True

class Article(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    
    source = EmbeddedModelField(
        embedded_model = SourceInfo
    )
    
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    original_url = models.URLField(unique=True)
    published_at = models.DateTimeField()
    scraped_at = models.DateTimeField(auto_now_add=True)
    
    # User interactions - store user IDs as arrays
    bookmarked_by_ids = models.JSONField(default=list, blank=True)
    tags = models.JSONField(default=list, blank=True)
    
    class Meta:
        db_table = 'articles'
        ordering = ['-published_at']

class Source(models.Model):
    """Separate collection for managing sources"""
    id = ObjectIdAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    base_url = models.URLField()
    feed_url = models.URLField(blank=True, null=True)
    is_rss = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    last_scraped = models.DateTimeField(null=True, blank=True)
    follower_ids = models.JSONField(default=list, blank=True)
    
    class Meta:
        db_table = 'sources'