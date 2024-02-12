from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "main_app/index.html", {"title": "Главная"} )
    


def board_b(request):
    return render(request, "main_app/board.html")