import aws_cdk as core
import aws_cdk.assertions as assertions

from journaling_app_nlp.journaling_app_nlp_stack import JournalingAppNlpStack

# example tests. To run these tests, uncomment this file along with the example
# resource in journaling_app_nlp/journaling_app_nlp_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = JournalingAppNlpStack(app, "journaling-app-nlp")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
