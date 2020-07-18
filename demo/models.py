from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    title_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    title_published = models.BooleanField(default=True, blank=True, null=True)


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
