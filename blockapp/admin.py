from django.contrib import admin
from .models import Post, User

admin.site.register([Post, User])

# Register your models here.
