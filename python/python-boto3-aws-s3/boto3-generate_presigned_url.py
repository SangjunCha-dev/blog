import boto3
from conf import *

s3_client  = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

key_name = "copy_cat.jpg"

url = s3_client.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': AWS_BUCKET_NAME,
        'Key': key_name,
    },
    # url 유효기간 (단위:second)
    ExpiresIn=10
)

print(url)