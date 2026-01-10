---
title: How to Read a CSV File from S3 Bucket in AWS Lambda - A Definitive Guide
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2023-09-12T10:44:09.000Z'
originalURL: https://freecodecamp.org/news/read-csv-file-from-s3-bucket-in-aws-lambda
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/unnamed.jpg
tags:
- name: AWS
  slug: aws
- name: Python
  slug: python
seo_title: null
seo_desc: "Amazon Simple Storage Service (S3) is a highly scalable, durable, and available\
  \ object storage service.\nIt is designed to store any amount of data, anytime,\
  \ from anywhere on the web. \nS3 is a key component of the Amazon Web Services (AWS)\
  \ cloud platf..."
---

Amazon Simple Storage Service (S3) is a highly scalable, durable, and available object storage service.

It is designed to store any amount of data, anytime, from anywhere on the web. 

S3 is a key component of the Amazon Web Services (AWS) cloud platform.

AWS Lambda is a serverless computing service that lets you run code without provisioning or managing servers. 

Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second. 

You are billed only for the compute time you consume – there is no charge when your code is not running.

S3 and Lambda are two of the most popular AWS services. They can be used together to create robust, scalable, cost-effective applications. 

S3 can be used to store data that is processed by Lambda functions. 

Lambda's event-driven architecture seamlessly interfaces with S3 events, allowing developers to effortlessly trigger serverless functions in response to changes within S3 buckets. This allows you to build applications that automatically process data as it is added to S3.

This tutorial will teach you how to read a CSV file from an S3 bucket in AWS Lambda using the `requests` library or the `boto3` library.

## How to Create a Lambda Execution Role with S3 Read permissions

For the Lambda service to read the files from the S3 bucket, you need to create a lambda execution role that has S3 read permissions. 

To create a lambda execution role:

1. Sign in to the AWS Console and navigate to the Identity and Access Management (IAM) console
2. Click Roles and then click Create role:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-52.png)
_Create Role_

3.  Choose AWS service as a Trusted Entity and Lambda as the Use Case as shown in the following image:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-54.png)
_Select Trusted Entity and Use case_



4.  Add the AmazonS3ReadOnlyAccess policy for read-only S3 access:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-56.png)
_Adding permissions_

 5. Give the role a name and description and review the attached policies. Finally, click Create role to create the IAM role as shown in the following image:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-58.png)
_Creating Role_

To Attach Role to the Lambda Function:

1. Go to your Lambda function in the Lambda console if it is already existing, or create a Lambda function if you need to create a new one
2. In the Execution role section, click Edit
3. Choose the IAM role you created
4. Save to attach the role to your Lambda function:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-59.png)
_Attaching the Role to the Lambda Function_

Now, let's see how to read a CSV file.

## How to Read a CSV File from S3 Bucket Using the Requests Library in AWS Lambda

The Requests library is a popular Python module for making HTTP requests and interacting with web services. 

It simplifies the process of sending HTTP requests, handling responses, and managing various aspects of web communication.

With an easy-to-use and intuitive API, Requests allows developers to send `GET`, `POST`, `PUT`, `DELETE`, and other HTTP requests with minimal code. This makes it a valuable tool for tasks such as fetching web data, interacting with RESTful APIs, and more. 

You can use the requests library to send a `GET` request and read a CSV file from S3 bucket. 

Once the `GET` request is complete, you'll receive a response with appropriate response codes. 

If the get request is successful, it will return the status code `200`. You can get the data from `response.text`. 

The following code demonstrates how to send the `GET` request and read the response:

```python
response = requests.get(url)

if response.status_code == 200:
    # Parse the CSV data from the response content
    csv_data = response.text
```

Next, use the `CSV` reader to read the CSV content from `csv_data` and iterate over the reader object to access each row of the CSV file: 

```python
    reader = csv.reader(csv_data.splitlines())
    
    for row in reader:
        
        print(row)
```

The following code demonstrates the complete program to get the CSV file from S3 using the requests library: 

```python
import requests

import csv

# URL of the CSV file
url = "https://mrcloudgurudemo.s3.us-east-2.amazonaws.com/sample_csv.csv"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the CSV data from the response content
        csv_data = response.text
        
        # You can now process the CSV data as needed
        # For example, you can use the csv.reader to read the data
        reader = csv.reader(csv_data.splitlines())
        
        # Iterate through the rows in the CSV
        for row in reader:
            # Process each row as needed
            print(row)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


```

Output:

```
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']
    ['4.9', '3', '1.4', '0.2', 'Iris-setosa']
    ['4.7', '3.2', '1.3', '0.2', 'Iris-setosa']
    ['4.6', '3.1', '1.5', '0.2', 'Iris-setosa']
    ['5', '3.6', '1.4', '0.2', 'Iris-setosa']

```

Note that if you’re using the `requests` library version 2.30.0 in AWS lambda, you might get a [Cannot Import Name DEFAULT_CIPHERS from urllib3.util.ssl_](https://www.mrcloud.guru/solve-error-cannot-import-name-default-ciphers-from-urllib3-util-ssl-aws-lambda/) error when any of the dependent libraries try to import the `default_ciphers` variable from `urllib3`. 

You can solve this error by downgrading the requests library to 2.29.0.

## How to Read a CSV File Using the Boto3 Client `get_Object()` Method in AWS Lambda

The second option to read a CSV file is using the [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library.

Boto3 is the AWS SDK for Python. It provides an object-oriented API as well as low-level access to AWS services. 

Boto3 makes it easy to create, configure, and manage AWS resources from your Python applications. 

For example, you can [read the content of a file from an S3 bucket](https://www.mrcloud.guru/reading-file-content-from-aws-s3-bucket-using-boto3/) programmatically.

Note that in order  to interact with the AWS service using Boto3, you must [configure the security credentials to avoid the unable to locate credentials error](https://www.mrcloud.guru/fix-the-boto3-nocredentialserror-unable-to-locate-credentials-error/). 

You can configure the security credentials using the `aws configure` command.

To read a CSV File Using the Boto3 Client [get_Object()](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object.html) Method in AWS Lambda first create the Boto3 client:

```
s3 = boto3.client('s3') 

```

Next, invoke the `get_object()` method from the Boto3 client and pass the bucket name and the object name:

```
response = s3.get_object(Bucket=bucket_name, Key=file_key)

```

Now, read the response body using `response['Body'].read()`:

```
csv_content = response['Body'].read().decode('utf-8')

```

Use the Pandas library [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) method to parse the response text as CSV content and create a pandas dataframe out of it. You can also print the first five lines to see if the data is successfully read:

```
df = pd.read_csv(io.StringIO(csv_content))
print(df.head(5))

```

The following code demonstrates the complete program to read a CSV file from S3 bucket using Boto3:

```python
import boto3

import pandas as pd

import io

def lambda_handler(event, context):
    # Initialize the S3 client
    s3 = boto3.client('s3')

    # Specify the S3 bucket and object key of the CSV file
    bucket_name = 'mrcloudgurudemo'
    file_key = 'sample_csv.csv'

    try:
        # Read the CSV file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        csv_content = response['Body'].read().decode('utf-8')

        # Create a Pandas DataFrame
        df = pd.read_csv(io.StringIO(csv_content))

        # Now you have your DataFrame (df) for further processing
        # Example: Print the first 5 rows
        print(df.head(5))

        return {
            'statusCode': 200,
            'body': 'File read successfully into DataFrame.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


```

Output:

```
sepal_length  sepal_width  petal_length  petal_width      species
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa

```

## Conclusion

In this article, you learned two methods for reading a CSV file from an S3 bucket in AWS Lambda: using the `requests` library and the `Boto3` library. 

Both methods are effective and have their own advantages. The requests library is a simple and lightweight library that is easy to use. 

Boto3 is the official AWS SDK for Python and provides a more comprehensive set of features and functionality.

Ultimately, the best method for reading a CSV file from S3 in AWS Lambda depends on your specific needs. 

If you need a simple and easy-to-use solution, the `requests` library is a good choice. 

If you need a more comprehensive and feature-rich solution, then `Boto3` is a better choice.

