import os

import boto3
from dotenv import load_dotenv

load_dotenv()


class AwsService:
    def __init__(self):
        session = boto3.session.Session()
        self.s3 = session.client(
            service_name="s3",
            endpoint_url="https://storage.yandexcloud.net",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")

    def upload_file(self, file_name):
        self.s3.upload_file(file_name, self.bucket_name, file_name)

AwsService().upload_file('README.md')