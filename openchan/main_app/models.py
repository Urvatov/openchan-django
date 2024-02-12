from django.db import models

# Create your models here.

class Board(models.Model):
    tag = models.CharField(max_length = 64)
    title = models.CharField(max_length = 24)
    description = models.TextField(blank = True)
    all_posts = models.IntegerField()

class Thread(models.Model):
    title = models.CharField(max_length= 64)
    text = models.TextField(blank = True)
    creation_time = models.DateTimeField(auto_now_add = True)