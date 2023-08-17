import aws_cdk as core
import aws_cdk.assertions as assertions

from st_stack_cont.st_stack_cont_stack import StStackContStack

# example tests. To run these tests, uncomment this file along with the example
# resource in st_stack_cont/st_stack_cont_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StStackContStack(app, "st-stack-cont")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
