# Generated by Django 4.1.7 on 2023-03-10 21:03

from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='preview',
            field=models.ImageField(null=True, upload_to='', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/static/video/videos', validators=[video.validators.validate_video_extension]),
        ),
    ]
