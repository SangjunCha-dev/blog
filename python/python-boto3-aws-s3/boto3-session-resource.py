import boto3
from conf import *

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# s3에 대한 권한 및 상태를 s3변수에 저장
s3 = session.resource('s3')

# bucket 목록조회
for bucket in s3.buckets.all():
    print(bucket.name)

print("------------------------------")

bucket = s3.Bucket(AWS_BUCKET_NAME)

for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)