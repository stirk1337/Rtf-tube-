from django.db import models
from .validators import validate_file_extension

class Video(models.Model):
    title = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=300)
    video = models.FileField(upload_to='video/static/video/videos', validators=[validate_file_extension])
    likes = models.PositiveIntegerField('Лайки')
    dislikes = models.PositiveIntegerField('Дизлайки')
    views = models.PositiveIntegerField('Просмотры')
    comments = models.JSONField('Комментарии')
    preview = models.ImageField('Превью', upload_to='video/static/video/preview', default='video/static/video/preview/v_review.jpg')
    author_id = models.IntegerField('ID автора')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
