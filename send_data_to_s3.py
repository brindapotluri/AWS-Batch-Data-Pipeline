import json
import boto3
import datetime

def lambda_handler(event, context):
    #print(event)
    # To print just responsePayload instead of everything
    print(event['responsePayload'])
    employee_data = event['responsePayload']
    # Use boto 3 library to create file inside the S3
    BUCKET_NAME = "employee-data-from-lambda2"
    # We will generate some sort of epoch time(to generate unique file name or random file name can be generated
    # Now everytime(lambda gets triggered) we are writing a file it will have new name for it. Epoch is basically a long int value that represents time. 
    # We will attach it in front of name of file and for that we will convert epoch into str(in line 21)
    current_epoch_time = datetime.datetime.now().timestamp()
    
    print("Start Data Write in S3")
    s3 = boto3.resource('s3')
    # We created a folder named inbox in which the data should be transferred. We are just dumping our json data in the form of bytes that will be written
    # into S3 and from there we will read the data.
    s3object = s3.Object(BUCKET_NAME, f"inbox/{str(current_epoch_time)}_employee_data.json")
    s3object.put(
        Body=(bytes(json.dumps(employee_data).encode('UTF-8')))
    )
    print("Data Write Successfull in S3")
    
