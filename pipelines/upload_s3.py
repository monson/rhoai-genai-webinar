import boto3
import botocore
import os
from os import environ
from boto3 import session
from botocore import client


def upload_directory_to_s3(local_directory, s3_prefix):
    s3_endpoint_url = environ.get('AWS_S3_ENDPOINT')
    s3_access_key = environ.get('AWS_ACCESS_KEY_ID')
    s3_secret_key = environ.get('AWS_SECRET_ACCESS_KEY')
    s3_bucket_name = environ.get('AWS_S3_BUCKET')
    
    session = boto3.session.Session(aws_access_key_id=s3_access_key,
                                aws_secret_access_key=s3_secret_key)

    s3_resource = session.resource(
    's3',
    config=botocore.client.Config(signature_version='s3v4'),
    endpoint_url=s3_endpoint_url)

    bucket = s3_resource.Bucket(s3_bucket_name)
    for root, dirs, files in os.walk(local_directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, local_directory)
            s3_key = os.path.join(s3_prefix, relative_path)
            print(f"{file_path} -> {s3_key}")
            bucket.upload_file(file_path, s3_key)


if __name__ == '__main__':
    upload_directory_to_s3(local_directory='./data/google/converted/flan-t5-small', s3_prefix='flan-t5-small')