from django.db import models
import uuid

class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique = True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Create your models here.
