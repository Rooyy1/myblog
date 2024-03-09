from django.db import models

class Post(models.Model):
    heading = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField()
    author = models.TextField()
