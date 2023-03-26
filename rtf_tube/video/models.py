from django.db import models
from .validators import validate_file_extension, file_size
from django.contrib.auth.models import User

class Ip(models.Model): 
    ip = models.CharField(max_length=100)

class Video(models.Model):
    title = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=300)
    video = models.FileField(upload_to='video/static/video/videos', validators=[validate_file_extension, file_size])
    likes = models.PositiveIntegerField('Лайки')
    dislikes = models.PositiveIntegerField('Дизлайки')
    views = models.ManyToManyField(Ip, related_name="views", blank=True)
    preview = models.ImageField('Превью', upload_to='video/static/video/preview', default='video/static/video/preview/v_review.jpg')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    video_id = models.ForeignKey(Video, on_delete = models.CASCADE, null=True)

