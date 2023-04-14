# Generated by Django 4.1.7 on 2023-03-08 22:38

from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='static/video/videos', validators=[video.validators.validate_video_extension]),
        ),
    ]
