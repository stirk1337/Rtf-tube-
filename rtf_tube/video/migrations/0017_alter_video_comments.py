# Generated by Django 4.1.7 on 2023-03-26 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0016_alter_video_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.comment'),
        ),
    ]
