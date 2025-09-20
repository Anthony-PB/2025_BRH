from django.db import models
from django.contrib.auth.models import AbstractUser
from django_mongodb_backend.fields import ObjectIdAutoField

class User(AbstractUser):
    # Use MongoDB-specific ID field
    id = ObjectIdAutoField(primary_key=True)
    
    # Make email unique as required
    email = models.EmailField(unique=True)
    
    display_name = models.CharField(max_length=100, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.email