import boto3
from conf import *

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# s3에 대한 권한 및 상태를 s3변수에 저장
s3 = session.resource('s3')

object_key = "media/image/21/11/26/14A9A265-3CC9-498C-9004-3F072413BA8A.jpeg"

object_ = s3.Object(AWS_BUCKET_NAME, object_key)
print(object_)

print("------------------------------")

object_ = s3.ObjectSummary(AWS_BUCKET_NAME, object_key)
print(object_)
print(f"object_.size = {object_.size}")
print(f"object_.last_modified = {object_.last_modified}")
print(f"object_.Acl() = {object_.Acl()}")

print("------------------------------")

object_acl = s3.ObjectAcl(AWS_BUCKET_NAME, object_key)
print(object_acl)
print(f"object_acl.owner = {object_acl.owner}")
print(f"object_acl.grants = {object_acl.grants}")
