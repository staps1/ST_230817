from aws_cdk import (
    App,
    Stack,
    Tags,
    aws_s3 as s3
)
from constructs import Construct

class StStackContStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
