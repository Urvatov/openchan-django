from django.db import models

# Create your models here.

class Board(models.Model):
    tag = models.CharField(max_length = 64)
    title = models.CharField(max_length = 24)
    description = models.TextField(blank = True)
    all_posts = models.IntegerField()
