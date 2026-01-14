import boto3
import logging

logger = logging.getLogger()


bucket_name = "prueba-tecnica-gns-mp-bucket"
s3 = boto3.client("s3")

file_name = "file.txt"


def upload_file(file_name, bucket_name):
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        logger.info(f"The file {file_name} was uploaded")
        return True
    except Exception as e:
        logger.error(f"Error uploading {file_name}")
        return False


def get_file(file_name, bucket_name):
    try:
        s3.download_file(bucket_name, file_name, file_name)
        logger.info(f"The file {file_name} was uploaded")
        return True
    except Exception as e:
        logger.error(f"Error uploading {file_name}")
        return False
