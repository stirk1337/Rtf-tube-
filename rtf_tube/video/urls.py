from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('video/<int:video_id>', views.play_video),

]