from django.shortcuts import render
from .models import Video, Ip, Comment
from .forms import UploadVideoForm, CommentForm, LikeForm, DislikeForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
import datetime
from datetime import datetime
from django.contrib.auth.decorators import login_required

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_time() -> str:
    return datetime.today().strftime('%d-%m-%Y') + ' ' + datetime.now().strftime("%H:%M")

def main_page(request):
    videos = Video.objects.all()
    return render(request, 'video/index.html', {'data': videos})

def play_video(request, video_id):
    video = Video.objects.get(id=video_id)
    comment_form = CommentForm()
    like_form = LikeForm()
    dislike_form = DislikeForm()
    comment_form['video_id'].initial = video_id
    like_form['video_id'].initial = video_id
    dislike_form['video_id'].initial = video_id
    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        video.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        video.views.add(Ip.objects.get(ip=ip))
       
    return render(request, 'video/video.html', {'data': video, 
                                                'comment_form': comment_form, 
                                                'like_form': like_form,
                                                'dislike_form': dislike_form})

@login_required(login_url='/accounts/login/')
def user_videos(request):
    videos = Video.objects.filter(author_id=request.user.id)
    return render(request, 'video/your_videos.html', {'data': videos})


@login_required(login_url='/accounts/login/')
def upload_video(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = Video(author_id = request.user,
                          title=request.FILES['video'].name.split('.')[0][:30],
                          description=request.POST.get('description'),
                          video=request.FILES['video'],
                          preview=request.POST.get('preview'),
                          )
            video.save()
            return HttpResponseRedirect('/accounts/videos/')

    else:
        form = UploadVideoForm()
        
    return render(request, 'video/upload.html', {'form': form})


def post_commentary(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/login/')
        if len(request.POST.get('comment')) != 0:
            video = Video.objects.get(id=request.POST.get('video_id'))
            video.comment_set.create(user=request.user,
                                  message=request.POST.get('comment'),
                                  )
            video.save()
            return HttpResponseRedirect('/video/' + str(video.id))
        else:
            return HttpResponseRedirect('/video/' + str(video.id))
       
                
def post_like(request):
    video = Video.objects.get(id=request.POST.get('video_id'))
    if request.user in video.likes.all():
        video.likes.remove(request.user)
    else:
        video.likes.add(request.user)
        video.dislikes.remove(request.user)
    return HttpResponseRedirect('/video/' + str(video.id))

def post_dislike(request):
    video = Video.objects.get(id=request.POST.get('video_id'))
    if request.user in video.dislikes.all():
        video.dislikes.remove(request.user)
    else:   
        video.dislikes.add(request.user)
        video.likes.remove(request.user)
    return HttpResponseRedirect('/video/' + str(video.id))

    