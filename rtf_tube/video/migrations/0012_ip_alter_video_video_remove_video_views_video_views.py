# Generated by Django 4.1.7 on 2023-03-26 16:24

from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0011_alter_video_author_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(
                upload_to="video/static/video/videos",
                validators=[
                    video.validators.validate_video_extension,
                    video.validators.file_size,
                ],
            ),
        ),
        migrations.RemoveField(
            model_name="video",
            name="views",
        ),
        migrations.AddField(
            model_name="video",
            name="views",
            field=models.ManyToManyField(
                blank=True, related_name="views", to="video.ip"
            ),
        ),
    ]
