from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from main_app.models import Post

from main_app.models import Board, Thread


def index(request):
    boards = Board.objects.all()
    data = {"boards" : boards}
    return render(request, "main_app/index.html", context=data)
    
def board(request, board_tag):
    board_instance = Board.objects.get(tag=board_tag)
    threads = Thread.objects.filter(board=board_instance)
    data = {"threads" : threads, "board_tag" : board_tag}

    if request.method == "POST":
        create_thread(request, board_instance)
    return render(request, "main_app/board.html", context=data)

def create_thread(request, board):
        thread = Thread()
        thread.title = request.POST.get("thread_title")
        thread.text = request.POST.get("thread_text")
        thread.board = board
        thread.save()
        print(f"Тред {thread.title} создан")

        return redirect('board/')

        

def thread(request, board_tag, thread_id):
    board_instance = Board.objects.get(tag=board_tag)
    thread_instance = Thread.objects.get(id=thread_id)
    posts = Post.objects.all()
    data = {"posts" : posts}

    if request.method == "POST":
        create_post(request, board_instance, thread_instance)

    return render(request, "main_app/thread.html", context=data)


def create_post(request, board, thread):
    post = Post()
    post.user_name = request.POST.get("user_name")
    post.text = request.POST.get("post_text")
    post.board = board
    post.thread = thread
    thread.all_posts += 1
    board.all_posts += 1
    post.save()
