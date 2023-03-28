# Generated by Django 4.1.7 on 2023-03-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0018_remove_video_comments_comment_video_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.AddField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to='video.ip'),
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='video.ip'),
        ),
    ]
