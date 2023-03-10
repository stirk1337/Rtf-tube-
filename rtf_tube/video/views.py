from django.shortcuts import render
from .models import Video

def main_page(request):
    videos = Video.objects.all()
    return render(request, 'video/index.html', {'data': videos})

def play_video(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video/video.html', {'data': video})