from django.db import models
from django.contrib.auth.models import AbstractUser
from django_mongodb_backend.fields import ObjectIdAutoField
from django.apps import apps  # for lazy get_model

from django.apps import apps  # for lazy get_model


class User(AbstractUser):
    id = ObjectIdAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=100, blank=True)

    # List of source IDs the user follows
    followed_source_ids = models.JSONField(default=list, blank=True)


    # List of source IDs the user follows
    followed_source_ids = models.JSONField(default=list, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        db_table = 'users'


    def __str__(self):
        return self.email

    # Add a source to the followed list
    def follow_source(self, source_id):
        Source = apps.get_model('aggregator', 'Source')  # Lazy import
        if not Source.objects.filter(id=source_id).exists():
            raise ValueError("Source does not exist")
        if source_id not in self.followed_source_ids:
            self.followed_source_ids.append(str(source_id))  # store as string
            self.save()

    # Remove a source from the followed list
    def unfollow_source(self, source_id):
        Source = apps.get_model('aggregator', 'Source')  # Lazy import
        if not Source.objects.filter(id=source_id).exists():
            raise ValueError("Source does not exist")
        if source_id in self.followed_source_ids:
            self.followed_source_ids.remove(str(source_id))
            self.save()


    # Add a source to the followed list
    def follow_source(self, source_id):
        Source = apps.get_model('aggregator', 'Source')  # Lazy import
        if not Source.objects.filter(id=source_id).exists():
            raise ValueError("Source does not exist")
        if source_id not in self.followed_source_ids:
            self.followed_source_ids.append(str(source_id))  # store as string
            self.save()

    # Remove a source from the followed list
    def unfollow_source(self, source_id):
        Source = apps.get_model('aggregator', 'Source')  # Lazy import
        if not Source.objects.filter(id=source_id).exists():
            raise ValueError("Source does not exist")
        if source_id in self.followed_source_ids:
            self.followed_source_ids.remove(str(source_id))
            self.save()
