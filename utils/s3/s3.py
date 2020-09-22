import base64
import environ
import uuid
import logging

import boto3
from botocore.exceptions import ClientError


def upload_file(imagefile):
    key = f'{str(uuid.uuid4())}.jpg'
    
    client = boto3.client('s3')
    try:
        client.upload_fileobj(
            imagefile,
            'leatherleather',
            key,
        )
    except ClientError as e:
        logging.error(e)
        return False
    
    return f'https://leatherleather.s3.ap-northeast-2.amazonaws.com/{key}'