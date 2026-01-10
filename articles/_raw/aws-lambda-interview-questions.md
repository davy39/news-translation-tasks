---
title: AWS Lambda Interview Questions and Answers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-07T20:54:49.000Z'
originalURL: https://freecodecamp.org/news/aws-lambda-interview-questions
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/AWS-Lambda-Interview-Questions.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: coding interview
  slug: coding-interview
- name: interview questions
  slug: interview-questions
seo_title: null
seo_desc: "By Mugilan Ragupathi\nIn this article, I'll go over some of the most commonly\
  \ asked questions that come up in interviews about AWS Lambda. \nNote that this\
  \ is not an exhaustive list – but you can use this guide as a reference to refresh\
  \ your knowledge ..."
---

By Mugilan Ragupathi

In this article, I'll go over some of the most commonly asked questions that come up in interviews about AWS Lambda. 

Note that this is not an exhaustive list – but you can use this guide as a reference to refresh your knowledge and get pointers for further study.

Most of the questions will be based on your experience or on certain scenarios. The questions are in the headings and you'll find the notes for the rationale behind asking the questions just below them.

## Explain your last project involving AWS Lambda

_The interviewer wants to know about your real-life experience using AWS Lambda. Don't bluff here, as the interviewer may ask further questions based on the answers to this question._ 

You might have built a serverless API, systems involving microservices, image/video conversion, log analysis, and many more. Just explain your project in detail and tell about the business benefits of that project so that the interviewer knows you're seeing the big picture.

## What services have you integrated with AWS Lambda?

_This is an extension of the previous question. This is not a laundry list of all event sources that can connect to AWS Lambda. Only tell about the services that you've really used._ 

You may have used S3, SNS, SQS, Kinesis, DynamoDB, SES, or others. Not all projects will be completely serverless. 

If you've used any non-serverless component along with AWS Lambda, mention those too. For example, you might've used AWS Lambda with RDS. If you've used such a configuration,  you can explain about that along with your reasoning.

## Explain the concept of cold and warm starts in AWS Lambda

_There are 2 reasons for asking this question. They want to know the runtimes that you've used, and they want to know if you know the other runtimes that could cause a cold start._

Lambda services receive a request to run a lambda function. The service prepares the execution environment by downloading the handler function code and by allocating memory along with other configuration. 

Even though you're not billed for this `execution environment` preparation time, you'll have to face the delay in invoking your lambda function. This delay is called a "cold start".

The cold start timing is less significant for TypeScript and Python runtime environments, whereas it's a bit higher for Java or C# runtime environments.

To improve performance, the lambda service will keep the execution environment for some time. When you receive the request for the same lambda function again during this period, your handler can start executing immediately. This type of invocation is called a "_warm start_".

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-18.png)
_[Image source](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)_

## What's the difference between synchronous and asynchronous invocation in AWS Lambda?

_Even though this seems to be straightforward question, this has many implications for your design and error handling._ 

In synchronous invocation, the caller will wait for the execution to complete. But in asynchronous invocation, the caller will put the event in an internal queue which will later be processed in the lambda function.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-19.png)
_[Image source](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)_

An important point to note here is that you can't dictate the type of invocation and it depends on the service that you use with AWS Lambda.

For example, if you're building serverless APIs using API Gateway, it'll be a synchronous invocation. But if you're using S3, it'll be an asynchronous invocation.

## How do you implement error handling and retry logic in Lambda?

_Any component in event driven system that may fail will fail. So interviewer wants to know how you've handled the error and how you retried in your previous projects. Below are some examples. Always explain with concrete examples._

This depends on the service that you're using with AWS Lambda. Let's discuss this with some examples.

If you're building a serverless API, it is better to return that error to the calling client (could be a front end app in this case). Then you let your front end logic decide what to display to the user based on the type of the error.

If you're using Lambda with SQS, it is better to use a Dead Letter Queue so that you know what messages have failed to process. For this same reason, many of the systems that use SNS may use SQS, too.

In the below code, we're using a dead letter queue. If any message fails to process after a certain number of times (as specified by `maxReceiveCount`), it's sent to the dead letter queue. This behaviour is specific to lambda when used along with queues.

```typescript
const queue = new sqs.Queue(this, 'AwsLambdaSqsQueue', {
      visibilityTimeout: cdk.Duration.seconds(300),
      receiveMessageWaitTime: cdk.Duration.seconds(20),
      deadLetterQueue: {
        queue: new sqs.Queue(this, 'AwsLambdaDlq'),
        maxReceiveCount: 5,
      },
    });
```

When lambda is invoked with any other services, you can configure the number of retries with a maximum value of 2. This means that you can have maximum of 2 retries apart from the initial invocation. For example, you want to trigger based on the S3 object upload and your lambda will try at most 3 times.

## Explain your workflows for development and deployment of AWS Lambda functions

_Talk about the frameworks that you've used. The interviewer may expect you to talk about testing lambda functions as well._ 

You can explain which framework(s) you've used to develop and deploy lambda functions. You can also talk about any IaC (Infrastructure as Code) tool that you've used. 

Below is non-exhaustive list of the most commonly used frameworks:

* Serverless
* AWS CDK
* AWS SAM
* CloudFormation
* Pulumi

If you've used Terraform, you can talk about that as well.

## Can Lambda be invoked when you get an email to a particular support email address? If yes, design that system. If not, explain why.

Yes, you can. You can create receipt rule set and add a rule which triggers the lambda function.

You should store the email to S3 and trigger the lambda after that so that you can have the copy of the email for any further reference.

You can refer to [this article](https://www.freecodecamp.org/news/how-to-receive-emails-via-your-sites-contact-us-form-with-aws-ses-lambda-api-gateway/) on how to receive emails from a contact form.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-20.png)
_[Image source](https://www.freecodecamp.org/news/how-to-receive-emails-via-your-sites-contact-us-form-with-aws-ses-lambda-api-gateway/)_

## Can one lambda function call another lambda function?

_The interviewer wants to know whether you know this anti-pattern._

You can do this, but it is not recommended. If you want to design a workflow which involves multiple lambda functions, you can use step functions. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-21.png)
_[Image source](https://aws.amazon.com/step-functions/)_

You can read more about step functions [here](https://aws.amazon.com/step-functions/).

Another standard approach is to emit an event and trigger a lambda based on the event. You can use SQS, SNS, or EventBridge as intermediary for these events.

## Can you execute queries on an RDS instance (in a private subnet) using Lambda?

Yes, you can execute the query in RDS using AWS Lambda. For that you can have your lambda inside the same VPC. 

There may be some performance implications if you use AWS Lambda directly with RDS because of the database connection creation time. To avoid those, you can use an RDS Proxy.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-22.png)
_[Image source](https://www.freecodecamp.org/news/aws-lambda-rds/)_

Here's a [detailed step by step guide](https://www.freecodecamp.org/news/aws-lambda-rds/) that shows you how to do that.

## AWS Lambda provides many benefits. What are the cons of using AWS Lambda?

_The interviewer wants to know about your thought process. Don't say AWS Lambda solves all the problems :-)_ 

Yeah, Lambda provides many benefits such as cost and scalability without any need to maintain the servers. But it's not the answer to everything – like any service, it has its own problems (and you should be able to discuss them):

* Debugging: If you're using serverless architectures using Lambda, you might have to rely on logging to find the root cause of the issue. This is because your application will be distributed across many services/ lambda functions. 
* Testing: You can mock AWS services in your local testing. But it is better to have a separate environment in AWS to test your lambdas. This makes testing a bit complex.
* Background jobs: Lambda has a timeout limit of 15 minutes. If you want any particular task to take more than 15 minutes, you might have to move to Fargate or some other solution.
* Cost: If you're running a high traffic application which processes the requests 24/7, using lambda can be expensive. It is better to use Fargate, EC2 or other services, if you have constant high traffic.

## How do you manage concurrency and scaling in AWS Lambda?

_Bonus points if you talk about the issues that you've faced in these situations._

Concurrency is the ability to execute multiple lambda functions at the same time. Scaling is the process of increasing the number of copies of your lambda function to handle the incoming requests.

You can control concurrency by setting the value of `reserved concurrency` so that only the mentioned number of lambda functions will be invoked.

Below is the high level diagram of how lambda scales in accordance with number of messages in the queue.

![AWS Lambda with SQS](https://www.freecodecamp.org/news/content/images/2022/12/image-23.png)
_[Image source](https://www.cloudtechsimplified.com/aws-lambda-sqs/)_

Note: There is some [weird behavior](https://www.cloudtechsimplified.com/aws-lambda-sqs/#weird-behavior) if you try to throttle AWS Lambda when used with SQS standard queue. You can use a FIFO queue to solve that issue.

## How do you pass environment variables to AWS Lambda?

_The interviewer might want to know how you pass sensitive information, for example._

There are different ways to pass environment variables to AWS Lambda, and it depends on the type of value is getting passed.

**Non-sensitive data**: If you want to pass any non-sensitive information, you can pass the values directly to your lambda function environment variables. But these values would be visible in the AWS console in the Lambda service.  
  
In the below code example, we're passing the name of the DynamoDB table directly as environment variable, as it is not sensitive data:

```
   const readDDBLambdaFn = new NodejsFunction(this, 'readDDBLambdaFn', {
      entry: path.join(__dirname, '../src/lambdas', 'read-ddb.ts'),
      ...nodeJsFunctionProps,
      functionName: 'readDDBLambdaFn',
      environment: {
        tableName: table.tableName,
      },
    });
```

**Sensitive data**: If you want to pass sensitive data such as passwords and API keys, you can use either a Secret Manager or Parameter store. But, you need to make sure you provide necessary roles to Lambda for accessing and decrypting secrets from the respective services.

In the below code snippet, we're NOT passing the actual secret. Instead, we're just passing the ARN (Amazon Resource Name) of the secret.  

```typescript
const rdsLambdaFn = new NodejsFunction(this, 'rdsLambdaFn', {
      entry: path.join(__dirname, '../src/lambdas', 'rds-lambda.ts'),
      ...nodeJsFunctionProps,
      functionName: 'rdsLambdaFn',
      environment: {
        DB_ENDPOINT_ADDRESS: dbInstance.dbInstanceEndpointAddress,
        DB_NAME: databaseName,
        DB_SECRET_ARN: dbInstance.secret?.secretFullArn || '',
      },
      vpc,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      }),
    });
```

Then, in lambda you can get the actual secret dynamically within the lambda function as shown below:

```typescript
export const handler = async (event: any, context: any): Promise<any> => {
    const host = process.env.DB_ENDPOINT_ADDRESS || '';
    const database = process.env.DB_NAME || '';
    const dbSecretArn = process.env.DB_SECRET_ARN || '';
    const secretManager = new AWS.SecretsManager({
      region: 'us-east-1',
    });
    const secretParams: AWS.SecretsManager.GetSecretValueRequest = {
      SecretId: dbSecretArn,
    };
    const dbSecret = await secretManager.getSecretValue(secretParams).promise();
    const secretString = dbSecret.SecretString || '';

    const { password } = JSON.parse(secretString);

}
```

I've written a detailed tutorial [here](https://www.cloudtechsimplified.com/environment-variables-secrets-database-password-aws-lambda/) on the same topic.

## Say you have a Windows-dependent executable sometool.exe. You can upload it into an S3 bucket. Can you execute this binary with some parameters using AWS Lambda?

_This is more of a question to make sure you understand the AWS Lambda execution environment – specifically the operating system it uses._

No, you would not be able to do that as AWS Lambda uses Linux as its operating system. Linux would not be able to execute a Windows-dependent binary.

## How do you re-use code across AWS Lambda functions?

There are 2 ways to re-use code across many AWS Lambda functions:

* Use Lambda Layers: You can store your code or logic in lambda layers, which you can re-use across different lambda functions. 

Below is some high level code for creating and consuming lambda layers using `aws cdk`:

```
    const logicLayer = new lambda.LayerVersion(this, 'logic-layer', {
      compatibleRuntimes: [
        lambda.Runtime.NODEJS_14_X,
        lambda.Runtime.NODEJS_16_X,
      ],
      layerVersionName: 'business-logic-layer',
      code: lambda.Code.fromAsset('src/layers/business-logic'),
      description: 'Business logic layer',
    });


    const lambdaWithLayer = new NodejsFunction(this, 'lambdaWithLayer', {
      entry: path.join(__dirname, '../src/lambdas', 'lambda.ts'),
      ...nodeJsFnProps,
      functionName: 'lambdaWithLayer',
      handler: 'handler',
      layers: [logicLayer, utilsLayer],
    });
```

* Use `monorepo`: You can use mono repo and dynamically build packages at deploy time.

## What happens to your lambda functions if you delete a Lambda Layer?

_In this question, the interviewer wants to see how well you understand lambda layers._ 

Existing lambda functions which use that deleted layer will continue to work – as lambda layers are merged with lambda functions at deployment time. 

But you can't create a new lambda function using that deleted lambda layer.

You can learn more about Lambda layers [here](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) and I've written a guide on the same topic [here](https://www.cloudtechsimplified.com/aws-lambda-layers/).

## Can you increase the size of a deployment package if you use Lambda Layers?

No, you can't increase the size of the deployment package if you use Lambda Layers. The maximum deployment size of 50 MB zipped includes both the size of the lambda function and its associated lambda layers.

If you have a large codebase and want to increase the deployment, you can run containers in AWS Lambda.

## Can I take my existing dockerized web application and run it using Lambda?

Nope. You can't take any Express, Springboot, or .NET Core application (or any other application for that matter) as they are and put them inside lambda. 

But that being said, there are a few libraries which allow you to put applications that use these web frameworks into AWS Lambda. Internally, those libraries convert those web applications into AWS lambda-compatible APIs. You can see one such example [here](https://aws.amazon.com/blogs/aws/running-express-applications-on-aws-lambda-and-amazon-api-gateway/).

By using these frameworks, the size of your lambda functions will be bigger and will result in longer start up times.

Remember that even when using containers with Lambda, the existing runtime API of Lambda remains the same. Lambda will still:

* be a single function 
* be invoked by an event or manually
* have a timeout of 15 minutes.

As you can see in the below code, there will be no change to the lambda API. The advantage of using Docker is that you would be able to use large packages without worrying about size.

```typescript
import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';

export const handler = async (
  event: APIGatewayEvent,
  context: Context
): Promise<APIGatewayProxyResult> => {
  console.log(`Event: ${JSON.stringify(event, null, 2)}`);
  console.log(`Context: ${JSON.stringify(context, null, 2)}`);
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Running this handler from docker',
    }),
  };
};
```

And, this is how you use it:

```
 const repo = ecr.Repository.fromRepositoryName(
      this,
      'dockerLambda',
      'docker-lambda'
    );

    const dockerLambda = new lambda.DockerImageFunction(
      this,
      'DockerLambdaFunction',
      {
        code: lambda.DockerImageCode.fromEcr(repo),
      }
    );
```

I wrote a step-by-step tutorial on running Docker containers for your application in `aws lambda` [here](https://www.cloudtechsimplified.com/run-docker-containers-images-from-ecr-in-aws-lambda-along-with-cicd/).

## How do you share large files between lambda functions?

You can use the Elastic File System (EFS) to share large files between different functions.  

You can create an `access point` in the created EFS with the appropriate permissions and use that `access point` in your `mount path` in your lambda. 

Any files written on that mount path will be accessible to all other lambda functions provided they have the mount path with appropriate permissions.

Below is the high level logical diagram on how to use AWS Lambda with Elastic File System (EFS):

![Using EFS with Lambda](https://www.freecodecamp.org/news/content/images/2022/12/image-24.png)
_[Image source](https://www.cloudtechsimplified.com/elastic-file-system-efs-aws-lambda/)_

You can read about this [here](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/) (bit old). I wrote a more recent practical step-by-step guide [here](https://www.cloudtechsimplified.com/elastic-file-system-efs-aws-lambda/) on EFS with Lambda functions.

## **Conclusion**

I hope this article helped you to prepare for interviews involving AWS Lambda.

Thanks for reading to this point. I write about `aws` and serverless technologies at [https://www.cloudtechsimplified.com](https://www.cloudtechsimplified.com/). If you're interested, you can [subscribe](https://www.cloudtechsimplified.com/) to my blog.


