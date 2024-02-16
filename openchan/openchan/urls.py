from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main_app.views import index, board, thread

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name="home"),

    path('<str:board_tag>/', board, name="board"),

    path('<str:board_tag>/<int:thread_id>', thread, name="thread")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "OpenChan admin"