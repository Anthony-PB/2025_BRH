from django.db import models
from django.conf import settings
from django_mongodb_backend.fields import EmbeddedModelField, ArrayField, EmbeddedModelArrayField
from django_mongodb_backend.models import EmbeddedModel
# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=254)
    display_name = models.CharField(max_length=64)
    password_hash = models.CharField()

    # the Strings are the IDs from the sources table
    sources = ArrayField(models.CharField(max_length=24))
    # the strings are the IDs from the posts table
    liked_posts = ArrayField(models.CharField(max_length=24))

