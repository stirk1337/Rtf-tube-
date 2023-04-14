from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'rtf-tube'
    print(bucket_name)
    custom_domain = '{}.hb.bizmrg.com'.format(bucket_name)
