from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, blank=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=256)
    content = models.TextField()
