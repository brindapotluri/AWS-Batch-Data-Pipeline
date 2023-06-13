# AWS-Batch-Data-Pipeline
In this project, we will explore 5 AWS services by creating a Data Pipeline. Below is the architecture of this project.
![image](https://github.com/brindapotluri/AWS-Batch-Data-Pipeline/assets/90103454/ae120f2c-6d01-445d-a1c8-b670bb98af34)
Architecture Explanation:

Goal: Transfer data from Lambda1 to DynamoDB batch wise.

Steps:

 •	Lambda1 generates mock data using Python.

 •	EventBridge triggers Lambda1 to generate mock data every 2 minutes.

 •	Lambda1 sends data to Lambda2 as we added Lambda2 as the destination for Lambda1.

 •	Lambda2 converts data to JSON format, creates files in an S3 bucket using the boto3 library.

 •	Lambda2 generates a unique file name using date and time every time our Lambda gets triggered as this file will be written into the S3 bucket.

 •	Policies are attached to Lambda2 for writing data to the S3 bucket.

 •	Glue Crawler is created to crawl through the data in the S3 bucket and sent it to DynamoDB.

 •	An empty Database is created for metadata in DynamoDB.

 •	A Spark job is written in Glue.

 •	The Spark job runs, sending the data to the DynamoDB table.

 •	Our target table is DynamoDB table and we should not have duplicates there so specific Spark script is used to handle duplicate data.

Loading data into DynamoDB:

 •	Data can be loaded in batches.

 •	Set a trigger for every 30 minutes (adjustable based on requirements) after data is sent to S3, run the Glue Job/Spark Script.

 •	Check if the data has been received successfully in DynamoDB.
