from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):

    username = models.CharField(max_length=100, primary_key=True, unique= True, blank=False, null= False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.username + '->' + self.email
    

class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    



# Create your models here.
