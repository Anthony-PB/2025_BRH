from django.db import models

# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=200)
    resource_uri = models.URLField(unique=True)
    is_rss = models.BooleanField()
    # ... any other fields like 'is_rss_feed', 'favicon_url', etc.

    def __str__(self):
        return self.name

class Article(models.Model):
    # This is a one-to-many relationship: One Source has many Articles.
    # We store the ID of the parent Source here.
    source_id = models.CharField(max_length=24)
    title = models.CharField(max_length=300)
    post_url = models.URLField(unique=True)

    def __str__(self):
        return self.title