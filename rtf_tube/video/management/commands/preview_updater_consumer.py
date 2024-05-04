import logging
import os
import time
import subprocess

import requests
import boto3

from django.core.management.base import BaseCommand
from django.conf import settings
from video.models import Video

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


class Command(BaseCommand):
    help = "Run preview updater"

    def handle(self, *args, **options) -> None:
        logging.info("Starting preview updater consumer")

        client = boto3.client(
            service_name='sqs',
            endpoint_url='https://message-queue.api.cloud.yandex.net',
            region_name='ru-central1',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url='https://storage.yandexcloud.net'
        )

        queue_url = client.create_queue(QueueName='video-preview').get('QueueUrl')

        while True:
            messages = client.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,
                VisibilityTimeout=60,
                WaitTimeSeconds=20
            ).get('Messages')
            if messages:
                for msg in messages:
                    video_id = int(msg.get('Body'))
                    video = Video.objects.get(id=video_id)
                    video_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/static/{video.video}'

                    r = requests.get(video_url, stream=True)
                    file_name = video_url.split('/')[-1]

                    with open(file_name, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024 * 1024):
                            if chunk:
                                f.write(chunk)

                    img_output_path = f'{video_id}.jpg'
                    subprocess.call(
                        ['ffmpeg', '-i', file_name, '-ss', '00:00:00.000', '-vframes', '1', img_output_path, '-y'])

                    s3_key = f'static/video/preview/{video_id}'[:90] + '.jpg'
                    s3.upload_file(img_output_path, settings.AWS_STORAGE_BUCKET_NAME, s3_key)
                    # we want to store it to our db model called **Image** after s3 upload is complete so,
                    video.preview.name = f'video/preview/{video_id}'[:90] + '.jpg'
                    video.save()
                    os.remove(img_output_path)
                    os.remove(file_name)

                for msg in messages:
                    client.delete_message(
                        QueueUrl=queue_url,
                        ReceiptHandle=msg.get('ReceiptHandle')
                    )
                    logging.info(f'Successfully ack message with body {msg.get("Body")}')

            logging.info("Sleep for 10 sec")
            time.sleep(10)
