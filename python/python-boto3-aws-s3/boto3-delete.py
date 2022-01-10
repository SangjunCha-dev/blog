import boto3
from conf import *

key_name = "copy_cat.jpg"

# 방법1
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

s3 = boto3.resource('s3')
buckets = s3.Bucket(name=AWS_BUCKET_NAME)
s3.Object(AWS_BUCKET_NAME, key_name).delete()

# 방법2
# client = boto3.client(
#     's3',
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#     region_name=AWS_REGION
# )

# client = boto3.client('s3')
# client.delete_object(Bucket=AWS_BUCKET_NAME, Key=key_name)