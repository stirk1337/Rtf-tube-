from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('video/<int:video_id>', views.play_video),
    path('accounts/videos/', views.user_videos),
    path('accounts/upload/', views.upload_video),
    path('video/post_commentary/', views.post_commentary),
    path('video/upload', views.upload_video)
]