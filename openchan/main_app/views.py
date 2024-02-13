from django.shortcuts import render
from django.http import HttpResponse

from main_app.models import Post

from main_app.models import Board
# Create your views here.



def index(request):
    boards = Board.objects.all()
    print(boards)
    data = {"boards" : boards}
    print(data)
    return render(request, "main_app/index.html", context=data)
    
def board_b(request):
    return render(request, "main_app/board.html")