from django.db import models

class Board(models.Model):
    tag = models.CharField(max_length = 64)
    title = models.CharField(max_length = 24)
    description = models.TextField(blank = True)
    all_posts = models.IntegerField()

    def __str__(self) -> str:
        return self.tag

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete = models.CASCADE, default = 0)
    title = models.CharField(max_length= 64)
    text = models.TextField(blank = True)
    creation_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    user_name = models.CharField(max_length = 64, default = "Аноним")
    text = models.TextField(blank = True)
    creation_time = models.DateTimeField(auto_now_add = True)



