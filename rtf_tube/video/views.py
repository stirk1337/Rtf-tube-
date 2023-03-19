from django.shortcuts import render
from .models import Video
from .forms import UploadVideoForm, CommentForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
import datetime
from datetime import datetime

def get_time() -> str:
    return datetime.today().strftime('%d-%m-%Y') + ' ' + datetime.now().strftime("%H:%M")

def main_page(request):
    videos = Video.objects.all()
    for video in videos:
        video.author_id = User.objects.get(id=video.author_id).username
    return render(request, 'video/index.html', {'data': videos})

def play_video(request, video_id):
    video = Video.objects.get(id=video_id)
    comment_form = CommentForm()
    
    return render(request, 'video/video.html', {'data': video, 'form': comment_form})

def user_videos(request):
    videos = Video.objects.filter(author_id=request.user.id)
    return render(request, 'video/your_videos.html', {'data': videos})

def upload_video(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = Video(author_id = request.user.id,
                          title=request.POST.get('title'),
                          description=request.POST.get('description'),
                          video=request.FILES['video'],
                          likes=0,
                          dislikes=0,
                          views=0,
                          preview=request.POST.get('preview'),
                          comments={"comments": []})
            video.save()
            return HttpResponseRedirect('/accounts/videos/')

    else:
        form = UploadVideoForm()
        
    print(request.POST.get('title'))
    return render(request, 'video/upload.html', {'form': form})

def post_commentary(request):
    if request.method == 'POST':
        if len(request.POST.get('comment')) != 0:
            video = Video.objects.get(id=int(request.GET.get('video_id')))
            comments = video.comments['comments']
            comments.append({'id': request.user.id, 'time': get_time(), 'comment': request.POST.get('comment')})
            video.save()
            return HttpResponseRedirect('/video/' + str(video.id))
        else:
            return HttpResponseRedirect('/video/' + str(video.id))
       
                



    

    