from django.shortcuts import render
from .models import Video

def main_page(request):
    videos = Video.objects.all()
    return render(request, 'video/video.html', {'data': videos})
