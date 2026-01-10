---
title: How to Speed Up Your Lambda Functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-25T19:43:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-speed-up-lambda-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-zhang-kaiyv-842654.jpg
tags:
- name: lambda
  slug: lambda
- name: performance
  slug: performance
seo_title: null
seo_desc: "By Ali Haydar\nLambda has gained massive popularity over the past few years.\
  \ It has various use cases, from running simple scripts to gluing flows and processes\
  \ within a serverless architecture or when running microservices. \nStill, if you've\
  \ just sta..."
---

By Ali Haydar

Lambda has gained massive popularity over the past few years. It has various use cases, from running simple scripts to gluing flows and processes within a serverless architecture or when running microservices. 

Still, if you've just started working in a new environment or organisation, you might feel cautious about using it because it's complex to configure. 

This is fair with any new technology you're getting ready to start using, and being careful is a sign of good business sense. 

An argument you might often hear is that lambda might slow down your operation because of cold starts.

This is also a common topic in technical interviews, so it's worth digging a bit deeper if you're keeping an eye on that next dream cloud engineering position.

|![cold-start-image](https://www.freecodecamp.org/news/content/images/2022/04/cold-start-image.jpeg)|
|:--:|
| Photo by [Myriams-Fotos](https://pixabay.com/users/myriams-fotos-1627417/) on [pixabay](https://pixabay.com/photos/dawn-winter-snow-nature-frost-3142990/)|

In this article, we'll talk about one way that can help enhance the performance of your Lambda functions. 

But let's start first with an overview of what happens when you execute a Lambda function, touching on cold starts.

## How is a Lambda Function Executed?

When your Lambda function is triggered, the Lambda service runs the code in an "Execution Environment" with three phases: `Init`, `Invoke` and `Shutdown`.

![execution-environment-1](https://www.freecodecamp.org/news/content/images/2022/04/execution-environment-1.png)

- In the `Init` phase, Lambda creates the execution environment, downloads the code, sets up the configuration (for example, memory), and runs the _code_ that lives outside of the `handler` function. (You might already have the gist of the article at this point – but read on for further explanation and a demo.)
- In the `Invoke` phase, Lambda runs the code inside the `handler` function
- In the `Shutdown` phase, Lambda terminates the environment

There could be multiple `Invocations` between an `Init` phase and a `Shutdown` phase if the Lambda got triggered a bunch of times in a row in a fairly short period of time (this time is not precisely determined in the Lambda docs). 

This means that if multiple consecutive executions of the Lambda happened in a short timeframe, the Lambda service would leverage the first created execution environment to run the following invokation. That is, it would only call the handler function with every new call to the Lambda without having to create a new execution environment and without having to run the code that's outside the handler function.

The `Init` phase happens only once upon the first execution, and we can visualise it as two parts (both of them run once per execution):

- The part where a new execution environment is created and the code is downloaded is the _cold start_.
- The part where the code outside the Lambda handler is run is the initialisation code.

From the [AWS docs](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html), this picture provides a proper visualisation of the 3 phases:
![execution-environment-phases](https://www.freecodecamp.org/news/content/images/2022/04/execution-environment-phases.png)

The Function INIT (the last block of the INIT phase) will run only once, along with the first two blocks that form the cold start.

Ok enough talk – show us the code!

## Lambda Function Code

In the previous section, we discussed that Lambda would run the initialisation code (code outside the handler function) once upon first execution. And it would run the code inside the handler using the same execution environment if the following invocations did not happen too far from each other. 

That's a perfect way to leverage the initialisation code to run the reusable code and save time re-running this code every time with every invocation.

Assume we have a Lambda function that's interacting with a DynamoDB to retrieve a set of items (please keep in mind that this code is for demo purposes only, so it's not the cleanest you'll see).

Create an `index.js` file:

```
const { DynamoDB } = require("@aws-sdk/client-dynamodb");

exports.handler = async (event, context) => {
  const dynamodb = new DynamoDB({ region: "ap-southeast-2" }); // creating a new instance of DynamoDB
  const params = {
    TableName: "company",
  };

  const results = await dynamodb.scan(params); // avoid using scan in production - it's expensive and not performant

  return {
    statusCode: 200,
    body: JSON.stringify(results),
  };
};
```

In the previous snippet, the initialisation code is the following:

```
const { DynamoDB } = require('@aws-sdk/client-dynamodb');
```

It will run once upon first execution and won't run in the following executions if they happen in a short time – that is, the subsequent executions happened before the Shutdown phase was reached.

## Lambda Demo

Awesome, now we're ready for the demo. In this section, we will build the infrastructure and test the performance of the Lambda.

### Build the Infrastructure

As this tutorial aims to demonstrate how to enhance the performance of our Lambda, we won't be putting much focus on the infrastructure as code.

Follow these steps to build and deploy your app:

- Install the dependencies: `npm install`
- Zip your Lambda File: `zip -r ./get-companies-lambda.zip index.js node_modules`
- Download the following Terraform file: https://gist.github.com/AHaydar/bfc173db2078b2eeb884da8632248c5d
- Apply the Terraform changes: `terraform apply`

Open the AWS console and validate that both DynamoDB and Lambda got created correctly (I am using the `ap-southeast-2` region in this example).

### Test the performance

First, navigate to your Lambda function in the AWS console and click the `Test` button to run your code. You will get a result similar to the following: ![init-duration](https://www.freecodecamp.org/news/content/images/2022/04/init-duration.png)

Notice the following in the last line:

`Duration: 569.85 ms`

and

`Init Duration: 429.13 ms`

The `Init Duration` is the duration to run the code outside the Lambda handler – that's the code requiring the DynamoDB SDK.

The `Duration` is the duration of running the code inside your Lambda handler – instantiating DynamoDB passing the "ap-southeast-2" region and scanning the table.

Click the `Test` button again. You should get a response like this: ![second-execution](https://www.freecodecamp.org/news/content/images/2022/04/second-execution.png)

Notice the last line – it does NOT contain an `Init Duration`. If your result included an Init Duration, it means the execution environment was shutdown before you clicked the `Test` button again. In this case, click it another time.

So in the second execution, we saved the `Init Duration`. It's a hint to optimise our function and add more common code outside the Lambda handler. How can we do that?

```
const { DynamoDB } = require("@aws-sdk/client-dynamodb");

const dynamodb = new DynamoDB({ region: "ap-southeast-2" }); // creating a new instance of DynamoDB
const params = {
  TableName: "company",
};

exports.handler = async (event, context) => {
  const results = await dynamodb.scan(params); // avoid using scan in production - it's expensive and not performant

  return {
    statusCode: 200,
    body: JSON.stringify(results),
  };
};
```

In the above snippet, I moved the instantiation of DynamoDB outside of the handler, along with the params object. 

So this would increase the execution time of the Init Code (outside the lambda handler), which runs only during the first execution of the Execution environment lifecycle. And it would decrease the execution time of the Lambda Handler, which happens upon every invocation.

Keep in mind that you should never write business logic that relies on having a running execution environment. Your code should always assume it needs to init the execution environment upon every invocation.

What other tips do you have on optimising your Lambda performance? Share them with me on [Twitter](https://twitter.com/Alee_Haydar) or [LinkedIn](https://www.linkedin.com/in/ahaydar/)



