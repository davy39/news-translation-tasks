---
title: How to Offer Custom APIs to Your Users with AWS API Gateway
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-06-21T13:56:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-offer-custom-apis-to-your-users-aws-api-gateway
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/AWS-API-Gateway-Banner.png
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: null
seo_desc: "In the world of cloud computing and serverless architecture, AWS API Gateway\
  \ is a powerful tool that helps you build robust, secure, and scalable APIs. \n\
  In this tutorial, I'll introduce you to API Gateway and explain the benefits of\
  \ using this helpfu..."
---

In the world of cloud computing and serverless architecture, AWS API Gateway is a powerful tool that helps you build robust, secure, and scalable APIs. 

In this tutorial, I'll introduce you to API Gateway and explain the benefits of using this helpful tool. Then I'll show you how to create and deploy a Rest API, and create usage plans to offer API keys. Alright, let's get started. 

## What is API Gateway?

AWS API Gateway is a fully managed service provided by Amazon Web Services (AWS) that simplifies the creation, deployment, and management of APIs at any scale. 

It acts as a front door for applications, and allows you to create APIs that act as bridges between clients and back-end services. This enables secure and efficient communication.

## Why Do You Need API Gateway?

AWS API Gateway offers many benefits for businesses and developers. Here are a few benefits of using API Gateway. 

### Scalability and High Availability

With AWS API Gateway, scaling your APIs becomes much easier. It seamlessly handles traffic spikes by automatically scaling the underlying infrastructure. This results in high availability and helps prevent service disruptions.

### Security and Authentication

API Gateway offers robust security features, including built-in authentication and authorization mechanisms. 

It supports User Authentication through IAM Roles for internal applications, Cognito for external applications (for example Mobile users), and it also supports custom authorizers. 

### Integration with other AWS Services

As part of the AWS ecosystem, API Gateway seamlessly integrates with a range of other AWS services. This enables you to leverage additional functionalities like AWS Lambda functions, AWS Cognito for user management, and AWS CloudWatch for monitoring and logging.

### API Lifecycle Management

With API Gateway, you can easily version, deploy, and manage different stages of your APIs. This simplifies the process of rolling out updates, testing new features, and managing different environments such as development, staging, and production.

I hope by now you understood what API Gateway is and why it's valuable. Let's dive into creating our very own API Gateway.

## How to Create an AWS API Gateway

In this section, we will:

* Create a Rest API with the GET method
* Integrate it with a simple hello world lambda function and deploy it

Let's begin with creating a lambda function

## How to Create an AWS Lambda Function

Log in to the AWS Management [Console](https://console.aws.amazon.com/) and search for "Lambda" in the AWS Management Console search bar. Click on Create Function. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-145.png)
_Navigate to AWS Lambda Console_

Select the "Author from scratch" option, enter a name for your lambda function, select the "Python" runtime, and click the Create Function button at the bottom right. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-146.png)
_Create a AWS Lambda Function_

Once the function is created, update the following code and deploy the changes:

```python
import json

def lambda_handler(event, context):
    body = "Hello from 5minslearn!"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-147.png)
_Deploy a Lambda Function_

Congratulations! You have successfully created an AWS Lambda function. Now let's create the Rest API. 

## How to Create a Rest API and Integrate it with AWS Lambda

Search for API Gateway in the search bar. In the REST API section, click on the Build button. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-183.png)
_Create a Rest API_

Choose the Protocol as Rest and select New API in the Create new API section. In the settings section enter the API name of your choice and leave Endpoint Type as the default. Then click the Create API button. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-148.png)
_Configure creating a Rest API_

Click the Actions Button on the top left. Next, Click Method and select the method as GET and click the Tick icon. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-149.png)
_Create a Method_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-150.png)
_Choose "GET" method_

Select Lambda Function as the Integration type and enter the name of the Lambda function you created previously. Then save the function. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-151.png)
_Select Method configuration_

Once you click save, "Add Permission to Lambda Function" will prompt for confirmation. This basically means that you're allowing the API Gateway to invoke a Lambda function. In this case, it is "DemoFunction" Lambda function. Accept the confirmation and proceed to the next step. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-152.png)
_Allow Permission to invoke Lambda Function from API Gateway_

Click on Test. It will take you to a new page. Click on the "Test" button. You'll be able to see the response from the Lambda function on the right side panel. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-153.png)
_Our API Architecture_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-184.png)
_Test our API Gateway_

As you have successfully tested your API, you're ready to deploy the API. To deploy the API, click on the Actions button once again and click on Deploy API. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-185.png)
_Deploy the API Gateway_

The Deploy API dialogue will popup. Select New Stage for Deployment stage and name it whatever you want. Click the Deploy button. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-155.png)
_Configure API Gateway deployment_

Click on Invoke URL shown at the top. You can see the response from the Lambda function. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-156.png)
_API Gateway Created_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-186.png)
_Test our API_

Great! We successfully created the Rest API, integrated it with the Lambda function, and deployed it.

But you can do this with multiple services available on the market. Why would you choose AWS API Gateway? 

Well. That's a interesting question. First of all, you can configure the usage plan for your API. The best part is you don't have to write any code for it. 

Now let's create a Usage Plan, generate an API key, and make our Rest API accessible only by passing the API key in the Header. 

## How to Create an API Gateway Usage Plan

In the left side bar click on Usage Plans and click the Create button. Enter the Name of your plan – I chose "Basic". Enter the Throttling and Quota sections as per your requirements and click Next. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-159.png)
_Create AWS API Gateway usage plan_

Click on the Add API Stage button. Select the API and its stage. Click on the tick icon at right corner and select Next. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-19-10-46-19.png)
_Create a Stage for our API_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-164.png)
_Create a Stage for our API_

Click on Create API Key and add to Usage Plan. A modal will pop up. Enter the Name for API Key. For the API key, I selected Auto Generate but if you want to give a custom key you can enter a custom key. Hit the Save button. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-160.png)
_Create a API Key to access the service_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-161.png)
_Configure the API Key_

Select Resources from the Sidebar, click on the GET API you just created, and click the Method Request. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-162.png)
_Select the method_

In the Settings section, update the API Key Required field to true and click the Tick icon. Once updated, don't forget to deploy the changes by hitting the Action dropdown. Your changes will not be updated otherwise. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-187.png)
_Enable API Key Required field_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-165.png)
_Deploy the API_

Hit the same URL now and see the magic. 

Forbidden!

Because our API layer is protected now. You have to pass the API key in the header to access the data. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-163.png)
_Forbidden access if no API Key is provided_

Now Click on the Usage Plans from the Sidebar. Select your plan and navigate to the API Keys tab. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-166.png)
_Access your API Key_

Click on the API key you created in Step 3. Click Show. Copy the API key. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-188.png)
_List of API Keys_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-167.png)
_Reveal your API Key_

You have to pass the API Key in the 'x-api-key' header. Let's switch to the terminal to test this out. 

Verify your Rest API without passing the API key at first. Open the terminal, and enter the following curl command. You will once again see the forbidden message. 

```bash
curl --location --request GET '[enter your invoke url]'
--header 'Content-Type: application/json
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-189.png)
_Forbidden access without API Key in Terminal_

Now pass the API key this time. Run the following curl command:

```bash
curl --location --request GET '[your invoke url]' \
--header 'x-api-key: [your api key]' \
--header 'Content-Type: application/json' \
--data-raw ''
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-190.png)
_Data received on passing API Key in x-api-key Header_

You can see the output of the Lambda function because you passed 'x-api-key' in the header. 

Awesome! You have successfully created the Usage plan, generated the API key, and attached it to the Rest API method and verified the integration. 

## Conclusion

In this tutorial, you learned what AWS API gateway is and how to create Usage Plans for the Rest API. 

If you wish to learn more about AWS Services, subscribe to my [email newsletter](https://5minslearn.gogosoon.com/?ref=fcc_aws_api_gateway) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_aws_api_gateway)) and follow me on social media.


