import boto3
import logging
import sys
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


bucket_name = "prueba-tecnica-gns-mp-bucket"
s3 = boto3.client("s3")

file_name = "file.txt"


def upload_file(file_name, bucket_name):
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        logger.info(f"The file {file_name} was uploaded")
        return True
    except Exception as e:
        logger.error(f"Error uploading {file_name}: {e}")
        return False


def get_file(file_name, bucket_name):
    try:
        s3.download_file(bucket_name, file_name, file_name)
        logger.info(f"The file {file_name} was downloaded")
        return True
    except Exception as e:
        logger.error(f"Error downloading {file_name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Upload or download files to/from AWS S3"
    )
    parser.add_argument(
        "action",
        choices=["upload", "download"],
        help="Action to perform: upload or download"
    )
    parser.add_argument(
        "--file",
        default=file_name,
        help=f"File name to process (default: {file_name})"
    )
    parser.add_argument(
        "--bucket",
        default=bucket_name,
        help=f"S3 bucket name (default: {bucket_name})"
    )

    args = parser.parse_args()

    if args.action == "upload":
        logger.info(f"Uploading {args.file} to {args.bucket}...")
        success = upload_file(args.file, args.bucket)
    else:
        logger.info(f"Downloading {args.file} from {args.bucket}...")
        success = get_file(args.file, args.bucket)

    if success:
        logger.info("Operation completed successfully!")
        sys.exit(0)
    else:
        logger.error("Operation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
