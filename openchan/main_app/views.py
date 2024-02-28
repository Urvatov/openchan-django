from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from main_app.models import Post

from main_app.models import Board, Thread, File


def index(request):
    boards = Board.objects.all()
    data = {"boards" : boards}
    return render(request, "main_app/index.html", context=data)
    
def board(request, board_tag):
    board_instance = Board.objects.get(tag=board_tag)
    threads = Thread.objects.filter(board=board_instance)
    data = {"threads" : threads, "board_tag" : board_tag}

    if request.method == "POST":
        return create_thread(request, board_instance)
    return render(request, "main_app/board.html", context=data)

def create_thread(request, board):
        thread = Thread()
        thread.title = request.POST.get("thread_title")
        thread.text = request.POST.get("thread_text")
        thread.image = request.FILES['image']
        thread.user_ip = request.META.get('REMOTE_ADDR', None)
        thread.board = board
        thread.save()
        print(f"Тред {thread.title} создан")

        thread_url = reverse('thread', args=[board.tag, thread.id])
        return redirect(thread_url)

        

def thread(request, board_tag, thread_id):
    board_instance = Board.objects.get(tag=board_tag)
    thread_instance = Thread.objects.get(id=thread_id)
    posts = Post.objects.filter(thread_id=thread_id)

    data = {"posts" : posts, 
            "thread" : thread_instance, 
            "board" : board_instance}
    
    if request.method == "POST":
        return create_post(request, board_instance, thread_instance)

    return render(request, "main_app/thread.html", context=data)


def create_post(request, board, thread):
    post = Post()
    post.user_name = request.POST.get("user_name")
    post.user_ip = request.META.get('REMOTE_ADDR', None)
    post.text = request.POST.get("post_text")

    post.board = board
    post.thread = thread

    thread.all_posts += 1
    thread.save()
    board.all_posts += 1
    board.save()

    post.save()


    if 'file' in request.FILES:
        for f in request.FILES.getlist('file'):
            file = File()
            file.file = f
            file.save()

            post.files.add(file)



    print(f"Пост {post.id} создан")

    return redirect(request.path)
