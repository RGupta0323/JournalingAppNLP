def handler(event, context): 
    print("[Journal_Entry_Created_Lambda.py handler() line 2] event: {}".format(event)) 

    return {'statuscode':200, 'body':"Successful!"}