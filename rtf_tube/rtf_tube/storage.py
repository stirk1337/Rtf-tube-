from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class MediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get(settings.AWS_STORAGE_BUCKET_NAME)
    custom_domain = "storage.yandexcloud.net/{}".format(bucket_name)
