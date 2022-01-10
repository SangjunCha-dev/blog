import boto3
from conf import *

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# s3에 대한 권한 및 상태를 s3변수에 저장
s3 = session.resource('s3')

buckets = s3.Bucket(name=AWS_BUCKET_NAME)

file_name = 'cat2.jpg'
file_path = os.path.join(IMAGE_DIR, file_name)
key_name = "copy_cat.jpg"

# buckets.download_file(bucket_filepath, local_filepath)
buckets.download_file(key_name, file_path)
