import boto3
from conf import *

client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# bucket 목록조회
response = client.list_buckets() 
print(f"list_buckets = {response}")

# bucket 모든 파일 정보 조회
response = client.list_objects(Bucket=AWS_BUCKET_NAME)
for content in response['Contents']:
    obj_dict = client.get_object(Bucket=AWS_BUCKET_NAME, Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])
