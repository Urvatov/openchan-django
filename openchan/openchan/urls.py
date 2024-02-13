from django.contrib import admin
from django.urls import path

from main_app.views import index, board

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name="home"),

    path('<str:board_tag>/', board, name="board"),

]
