from django.core.exceptions import ValidationError


def validate_video_extension(value):
    import os

    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".mp4", ".avi", ".mkv", ".webm"]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Формат файла не поддерживается")


def validate_image_extension(value):
    import os

    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".png", ".jpg", ".jpeg", ".webm"]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Формат файла не поддерживается")


def file_size(value):
    limit = 31000 * 1024 * 1024
    print(value.size)
    if value.size > limit:
        raise ValidationError("Файл слишком большой. Максимальный вес: 31000 МБ")
