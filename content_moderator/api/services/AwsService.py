import os

import boto3
from dotenv import load_dotenv

from simple_django_project.celery import app

from ...config import AWSendpoint_url, AWSservice_name, presignedUrlExpiration


load_dotenv()


def getAwsConnection():
    session = boto3.session.Session()
    return session.client(
        service_name=AWSservice_name,
        endpoint_url=AWSendpoint_url,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )


AwsConnection = getAwsConnection()


@app.task
def uploadFile(file_path, file_name=None):
    if file_name is None:
        file_name = file_path
    AwsConnection.upload_file(file_path, os.getenv("AWS_BUCKET_NAME"), file_name)

def generatePrinsignedURL(file_name, expiration=presignedUrlExpiration):
    return AwsConnection.generate_presigned_url(
        'get_object',
        Params={'Bucket': os.getenv("AWS_BUCKET_NAME"), 'Key': file_name},
        ExpiresIn=expiration
    )