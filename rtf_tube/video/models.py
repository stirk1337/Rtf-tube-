from django.db import models
from .validators import validate_file_extension

class Video(models.Model):
    video = models.FileField(upload_to='video/static/video/videos', validators=[validate_file_extension])
    likes = models.PositiveIntegerField('Лайки')
    dislikes = models.PositiveIntegerField('Дизлайки')
    views = models.PositiveIntegerField('Просмотры')
    comments = models.JSONField('Комментарии')
<<<<<<< HEAD
    preview = models.ImageField('Превью', upload_to='video/static/video/preview')
=======
>>>>>>> 4bbde0008656c4cb302b285825b771b9da628c4c

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
