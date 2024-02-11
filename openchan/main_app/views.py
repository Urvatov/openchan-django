from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {"gamer" : "hui",
            "jamer" : "penis",
            "cock" : 228
            }
    
    return render(request, "main_app/index.html", context=data)
    


def board_b(request):
    return HttpResponse("/b/")