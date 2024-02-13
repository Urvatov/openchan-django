from django.shortcuts import render, get_object_or_404
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
    data = {"threads" : threads}
    return render(request, "main_app/board.html", context=data)