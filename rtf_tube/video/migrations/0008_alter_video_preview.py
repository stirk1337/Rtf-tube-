# Generated by Django 4.1.7 on 2023-03-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_video_description_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=models.ImageField(null=True, upload_to='video/static/video/preview', verbose_name='Превью'),
        ),
    ]
