import logging
import time

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
        logging.info("Starting preview updater scheduler")

        client = boto3.client(
            service_name='sqs',
            endpoint_url='https://message-queue.api.cloud.yandex.net',
            region_name='ru-central1',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        queue_url = client.create_queue(QueueName=settings.QUEUE_NAME).get('QueueUrl')

        while True:
            videos_without_preview = Video.objects.filter(preview='')
            for video in videos_without_preview:
                client.send_message(
                    QueueUrl=queue_url,
                    MessageBody=str(video.id),
                )
                logging.info(f'Sent message with video id {video.id}')

            logging.info("Sleep for 30 sec")
            time.sleep(30)
