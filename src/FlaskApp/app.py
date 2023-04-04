# app.py
from flask import Flask ,render_template, request
import boto3 
import datetime 

app = Flask(__name__)
# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return render_template("Home.html") 


# backend routes to handle user requests (not publicly accessible urls)
@app.route("/usersubmitsjournalentry", methods=["POST"])
def usersubmitsjournalentry(): 
    user_form = request.form 
    print("[app.py usersubmitsjournalentry() line 15] user: {}".format(user_form))
    print("immutable dict keys: {}".format(user_form.keys())) 
    #print("[app.py usersubmitsjournalentry() line 17] journal title: {}".format(user_form.get("journal_title")))
    journal_title, journal_data = user_form.get("journal_title"), user_form.get("journal_data")

    # from here this should convert this data into a file and save that file in an s3 bucket, which should trigger the 
    # event notification to trigger the lambda 
    #s3_bucket = "arn:aws:s3:::journalingappnlpstack-journalingnlpappjournalentr-sx75n97n9" #arn of s3 bucket for journal entires 
    s3_bucket = "journalingappnlpstack-journalingnlpappjournalentr-sx75n97n9"
    client = None 
    

    try: 
        # getting timestamp for user 
        print("[app.py usersubmitsjouranlentry() line 32] Getting timestamp for user ")
        ct = datetime.datetime.now() 
        client = boto3.client("s3") 
        print("[app.py usersubmitsjournalentry() line 26] Uploading user journal entry data into s3 bucket")
        # (TODO) the key should be the email of the user and the timestamp; format: <email>-<timestamp>
        client.put_object(Body=journal_data, Bucket=s3_bucket, Key="UserJournalEntry-{}".format(ct)) 

    except Exception as ex: 
        print ("[app.py usersubmitsjournalentry() line 32] ERROR OCCURED - Exception message: {}".format(ex))
        return ex 
    
    print("[app.py usersubmitsjouranlentry() line 43] Put object in s3 bucket operation successful!")

    # render a webpage to thank a user for the journal entry - this is where the user will get 
    # reccomendations about meditations to use, wisdom, articles, etc. 

    # the user can also access their workspace 
    return render_template("JournalEntrySubmitted.html")
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')