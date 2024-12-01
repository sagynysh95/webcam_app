import logging
from datetime import datetime

from minio import Minio
import cv2
import io
# import boto3

# s3 = boto3.client('s3',
#                   endpoint_url='http://127.0.0.1:9000',
#                   aws_access_key_id='sagynysh1',
#                   aws_secret_access_key='sagynysh1'
#                   )


minio_client = Minio("play.min.io",
                     access_key="Q3AM3UQ867SPQQA43P2F",
                     secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
                     )


def upload_to_minio(image, file_name, b_name='bucket-faces-sagynysh'):
    try:
        if not minio_client.bucket_exists(b_name):
            minio_client.make_bucket(b_name)
        print('Есть подключение к MinIO')
    except:
    # raise error if storage not reachable
        logging.critical("Object storage not reachable")
        return False

    # buffer = cv2.imencode('.png', image)[1].tobytes()
    # minio_client.put_object(b_name, file_name, io.BytesIO(buffer), len(buffer))
    #
    # return f"http://play.min.io/{b_name}/{file_name}"
    obj_name = f'{datetime.now().isoformat()}.png'
    minio_client.fput_object(b_name, obj_name, file_name)

    return minio_client.presigned_get_object(b_name, obj_name)


