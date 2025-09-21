from django.db import models
from django.contrib.auth.models import AbstractUser
from django_mongodb_backend.fields import ObjectIdAutoField

class User(AbstractUser):
    id = ObjectIdAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=100, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.email