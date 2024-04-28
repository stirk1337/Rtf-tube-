from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = "rtf-tubee"
    custom_domain = "storage.yandexcloud.net/{}".format(bucket_name)
