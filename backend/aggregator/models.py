from django.db import models
from django.conf import settings


class Article(models.Model):
    source = models.ForeignKey(
        'Source',
        on_delete=models.CASCADE,
        related_name='articles'
    )
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    original_url = models.URLField(unique=True)
    published_at = models.DateTimeField()
    scraped_at = models.DateTimeField(auto_now_add=True)

    bookmarked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bookmarked_articles',
        blank=True
    )
    tags = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = 'articles'
        ordering = ['-published_at']


class Source(models.Model):
    """Separate collection for managing sources"""
    name = models.CharField(max_length=200)
    url = models.URLField()
    is_rss = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    last_scraped = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'sources'
