from aws_cdk import (
    App,
    Stack,
    Tags,
    aws_s3 as s3,
)
from constructs import Construct

class StStackContStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
       super().__init__(scope, construct_id, **kwargs)

       s3.Bucket(
           self,
           id = "stbucket",
           bucket_name = "snowflake-bucket-st4321",
           encryption = s3.BucketEncryption.KMS,
           bucket_key_enabled = True
           )        

