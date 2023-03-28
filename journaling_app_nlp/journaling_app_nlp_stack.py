from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lightsail as lightsail, 
    aws_s3 as s3, 
    aws_lambda as _lambda,
    aws_s3_notifications as s3_notify
)
from constructs import Construct

class JournalingAppNlpStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # s3 bucket to store user journal entries 
        journal_entries_s3_bucket = s3.Bucket(self, "JournalingNLPAppJournalEntries",
                                               encryption=s3.BucketEncryption.KMS, bucket_name="JournalingNLPAppJournalEntries")
        
        # lambda to handle journal entries 
        lambda_func = _lambda.Function(self, 'Journal_Entry_Created_Lambda',
                       runtime=_lambda.Runtime.PYTHON_3_8,
                       handler='Journal_Entry_Created_Lambda.handler',
                       code=_lambda.Code.asset('src'),
                       environment={'BUCKET_NAME':
                                    journal_entries_s3_bucket.bucket_name})

        
        notification = s3_notify.LambdaDestination(lambda_func)
        notification.bind(self, journal_entries_s3_bucket)

        journal_entries_s3_bucket.add_object_created_notification(
           notification, s3.NotificationKeyFilter(suffix='.txt'))

         # Step function / eventbridge here to handle data formatting 

        # Sage maker 
        
        # dynamodb to store user data 

        # light sail instance that's going to be hosting the flask app 
        

        # Lambdas 