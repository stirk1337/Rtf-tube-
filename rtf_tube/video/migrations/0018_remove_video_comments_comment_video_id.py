# Generated by Django 4.1.7 on 2023-03-26 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0017_alter_video_comments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="comments",
        ),
        migrations.AddField(
            model_name="comment",
            name="video_id",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="video.video"
            ),
        ),
    ]
