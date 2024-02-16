from django.db import models

class Board(models.Model):
    tag = models.CharField(max_length = 64, unique = True)
    title = models.CharField(max_length = 24)
    description = models.TextField(blank = True)
    all_posts = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return f"{self.id}. /{self.tag}/ {self.title}"
    

    class Meta:
        verbose_name = "Доски"
        verbose_name_plural = "Доски"



class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default = 0)

    title = models.CharField(max_length= 64)
    text = models.TextField(blank = True)
    image = models.ImageField(upload_to="images/")
    user_ip = models.GenericIPAddressField(default = 0)
    creation_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    all_posts = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return f"{self.id}. /{self.board.tag}/ {self.title}"
    
    class Meta:
        verbose_name = "Треды"
        verbose_name_plural = "Треды"
        ordering = ['-creation_time']
    
class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, default = 0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default = 0)
    user_name = models.CharField(max_length = 64, default = "Аноним")
    user_ip = models.GenericIPAddressField(default = 0)
    text = models.TextField(blank = True)
    image = models.ImageField(upload_to="images/", blank= True, null=True)
    creation_time = models.DateTimeField(auto_now_add = True)


    def __str__(self) -> str:
        return f"{self.id}. /{self.board.tag}/->{self.thread.title}"
    
    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Посты"

