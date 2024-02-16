from django.contrib import admin
from main_app.models import Board, Thread, Post
# Register your models here.


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title', 'description', 'all_posts')
    list_display_links = ('id', 'tag', 'title')

    search_fields = ('id', 'tag', 'title')



@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'board_id', 'title', 'creation_time', 'user_ip', 'update_time', 'all_posts')
    list_display_links = ('id', 'title')

    search_fields = ('id', 'title')

    ordering = ['-creation_time']


@admin.register(Post)
class PostdAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread_id', 'board_id', 'user_name', 'user_ip', 'creation_time')

    search_fields = ('id', 'user_name')

    ordering = ['-creation_time']

