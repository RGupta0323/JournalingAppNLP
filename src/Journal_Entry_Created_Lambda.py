"""
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 
'eventTime': '2023-04-04T19:15:02.851Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': 
{'principalId': 'AWS:AIDA3NCGCBMDJN2K54XTQ'}, 'requestParameters': {'sourceIPAddress': '173.215.110.3'},
 'responseElements': {'x-amz-request-id': 'PQ4FZNQ0Q2R646PV', 
 'x-amz-id-2': 'kjzTO0yjBR3zsT05bXfUxkV3Bcgkfyvnc2UVf1BEGhHH039QZTjOnw1t4LWh0lON5prhAJjzvstp3Dc6jCxKddQZn1U84JG2'}, 
 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'ZmQxMDY5NDMtN2NjNS00NjRmLWI3ZjEtMGQxNjUwODg3NDEx', 
 'bucket': {'name': 'journalingappnlpstack-journalingnlpappjournalentr-sx75n97n9',
   'ownerIdentity': {'principalId': 'AR223LMC2GQLQ'}, 
   'arn': 'arn:aws:s3:::journalingappnlpstack-journalingnlpappjournalentr-sx75n97n9'}, 
   'object': {'key': 'UserJournalEntry-2023-04-04+14%3A15%3A01.673145.txt', 'size': 23, 
   'eTag': '96e29a6011b52746e0ba1ae100988610', 'sequencer': '00642C7736A2D29B08'}}}]}
"""

# this lambda is going to take the input event (see above) and it will open up the file that was just uploaded 
# from there its going to take the data and section it out to list of lists (for now)
# then it will put this data into s3 or directly input it into sagemaker 
# from there the ml model will be triggered. 
def handler(event, context): 
    print("[Journal_Entry_Created_Lambda.py handler() line 2] event: {}".format(event)) 

    return {'statuscode':200, 'body':"Successful!"}