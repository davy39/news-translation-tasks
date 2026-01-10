---
title: How to Setup a Basic Serverless REST API with AWS Lambda and API Gateway
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-14T19:10:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-a-basic-serverless-backend-with-aws-lambda-and-api-gateway
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Serverless-computing-768x402-1.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: null
seo_desc: "By Nyior Clement\nAs developers, we are always trying to optimize everything\
  \ from how people communicate to how people buy things. The goal is to make humans\
  \ arguably more productive. \nIn the spirit of making humans more productive, the\
  \ software devel..."
---

By Nyior Clement

As developers, we are always trying to optimize everything from how people communicate to how people buy things. The goal is to make humans arguably more productive. 

In the spirit of making humans more productive, the software development landscape has seen a dramatic rise in the emergence of developer productivity tools.

This is especially true of the software infrastructure space. Innovators are creating solutions that allow developers to focus more on writing actual business logic and less on mundane deployment concerns.

The need to improve developer experience and cut down costs are some of the core drivers of serverless computing. But what is serverless computing? That's the crux of this guide. It's the one question that matters here, and we will get to it.

To help you walk through this guide, I've divided it into two parts: 

* In part one, we are going to start off by learning what serverless is. 
* In part two, we will set up a rudimentary serverless REST API with AWS Lambda and API Gateway.

Let's get started already, shall we?

## What is Serverless?

To understand what serverless is, first we need to understand what servers are and how they had evolved over time. Wait, servers?

Yes, when we build software systems, most times we build them for people. For that reason, we make these applications findable on the interwebs.

Making an application discoverable, ideally, entails uploading that application to a special computer that runs 24/7 and is super fast. This special computer is called a **server.**

### The Evolution of Servers

Two decades ago, when companies wanted to upload a piece of software they'd built to a server, they'd have to purchase a physical computer, configure the computer, and then deploy their application to that computer. 

In cases where they needed to upload several applications, they'd have to get and setup multiple servers, too. Everything was done on-premise.

But it didn't take long for people to notice the many problems that came with approaching servers that way. 

There is the problem of developer productivity: a developer's attention is divided between writing code and dealing with the infrastructure that serves the code. This issue could easily be addressed by getting other people to deal with the infrastructure issues – but this leads to a second problem:

The problem of cost. These people dealing with the infrastructure concerns would have to be paid, right? In fact, just having to purchase a server even for seemingly basic test applications is in itself a costly affair.

Furthermore, if we begin to factor in other elements like scaling a server's computing capability when there's a spike in traffic or simply just updating the server's OS and drivers over time...well, you'll begin to see how exhausting it is to keep an in-house server. People craved something better. There was a need.

Amazon responded to that need when it announced the release of Amazon Web Services (AWS) in 2006. AWS notoriously disrupted the software infrastructure domain. It was a revolutionary shift from traditional servers.

AWS took away the need for organizations to set up their in-house server. Instead, organizations and even individuals could just upload their applications to Amazon's computers over the internet for some fee. And this _server-as-a-service_ model announced the start of cloud computing.

## What is Cloud Computing?

Cloud Computing is fundamentally about storing files or executing code (sometimes both) on someone else's computer, usually, over a network.

Cloud computing platforms like AWS, Microsoft Azure, Google Cloud Platform, Heroku, and others exist to save people the stress of having to setup and maintain their own servers.

What is outstandingly unique about cloud computing is the fact that you could be in Nigeria, and rent a computer that's in the US. You can then access that computer you've rented and do stuff with it over the internet. Essentially, cloud vendors provide us with compute environments to upload and run our custom software.

The environment we get from these providers is something that has progressed, and now exists in different forms.

In cloud computing parlance, we use the term **cloud computing models** to refer to the different environments most cloud vendors offer. Each new model in the cloud computing scene is usually created to enhance developer productivity and shrink infrastructure and labor costs.

For example, when AWS was first launched, it had the Elastic Compute Cloud (EC2) service. The EC2 is structurally a bare-bones machine. People that pay for EC2 service would have to do a lot of configuration like installing an OS, a database, and maintaining these things for as long as they own the service. 

While EC2 offers lots of flexibility (for example, you can install whatever OS you want), it also requires lots of effort to work with. EC2 and other services like it across other cloud providers fall under the cloud computing model called **Infrastructure as a Service (IaaS).**

Not having to purchase a physical machine and set it up on-premise makes the IaaS model quite superior to the on-premise server model. But still, the fact that owners have to configure and maintain lots of things makes the IaaS model makes it a not so easy model to work with. 

The somewhat labor intensive requirements (from the developer's/customer's perspective) of the IaaS model eventually also became a source of concern. To address that, the next cloud computing model, **Platform as a Service (PaaS),** was born.

The major problem with IaaS is having to configure and maintain a lot of things. For example, OS installation, patch upgrades, discovery, and so on. 

In the PaaS model, all that is abstracted. A machine in the PaaS model comes pre-installed with an OS, and patch upgrades on the machine amongst others are the vendor's responsibility. 

In the PaaS model, developers only deploy their applications, and the cloud providers handle some of the low level stuff. While this model is easier to work with, it also implies less flexibility. Elastic Beanstalk from AWS and Heroku are some of the examples of offerings in this model. 

The PaaS model undeniably took away most of the dreary configuration and maintenance tasks. But beyond just the tasks that make our software available on the internet, people began to recognize some of the limitations of the PaaS model too. 

For example, in both the IaaS and PaaS models, developers had to manually deal with scaling up/down a server's computing capability. Additionally, with both the IaaS and PaaS platforms, most vendors charge a flat fee (Think Heroku) for their services – it's not based on usage. 

In situations where the fee is based on usage, it's usually not very precise. Lastly, in both the IaaS and PaaS models, applications are long-lived (always running even when there are no requests coming in). That in turn results in the inefficient use of server resources.

The above concerns stirred the next evolution of the cloud.

### The Rise of Serverless Computing

Just like IaaS and PaaS, Serverless is a cloud computing model. It is the most recent evolution of the cloud just after PaaS. Like IaaS and PaaS, with serverless, you don't have to buy physical computers. 

Furthermore, just as it is in the PaaS model, you don't have to significantly configure and maintain servers. Additionally, the serverless model went a step further: it took away the need to manage long lived application instances, and to manually scale server resources up or down based on traffic. Payment is precisely based on usage, and security concerns are also abstracted. 

In the serverless model, you no longer have to worry about anything infrastructure-related because the cloud providers handle all that. And this is exactly what the serverless model is all about: allowing developers and whole organizations to focus on the dynamic aspects of their project while leaving _all_ the infrastructure concerns to the cloud provider.

Literally _all_ the infrastructure concerns from setting up and maintaining the server to auto scaling server resources up from and down to zero and security concerns. And in fact one of the killer features of the serverless model is the fact that users are charged precisely based on the number of requests the software they deployed has handled. 

So we can now say that serverless is the term we use to refer to any cloud solution that takes away all the infrastructure concerns we normally would have to worry about. For example, AWS Lambda, Azure functions, and others.

We also use the term serverless to describe applications that are designed to be deployed to or interact with a serverless environment. Hmmm, how so?

### Function as a Service vs Backend as a Service

All serverless solutions belong to one of two categories: 

* **Function as a Service (FaaS)** and 
* **Backend as a Service (BaaS).**

**BaaS, FaaS –** Nyior, this is getting quite complicated :-(

I know, but don't worry – you'll get it <3

A cloud offering is considered a **BaaS** and by extension serverless if it replaces certain components of our application that we'd normally code or manage ourselves. 

For example, when you use Google's Firebase authentication service or Amazon's Cognito service to handle user authentication in your project, then you've leveraged a **BaaS** offering.

A cloud offering is considered a **FaaS** and by extension serverless if it takes away the need to deploy our applications as single instances that are then run as processes within a host. Instead, we break down our application into granular functions (with each function ideally encapsulating the logic of a single operation). Each function is then deployed to the **FaaS** platform. 

Way too abstract? Okay, see the image below:

![Image](https://www.freecodecamp.org/news/content/images/2024/08/app-deployment-methods.jpg)
_From Left-to-Right: Deploying an Application to a FaaS platform, Deploying an application to a non-FaaS platform. Source: Author_

From the image above you can see that FaaS platforms offer an entirely different way of deploying applications. We've seen nothing like it before: there are no hosts and application processes. As a result, we don't have some code that's constantly running and listening for requests.

Instead, we have functions that only run when invoked, and they're being torn down as soon as they're done processing the task they were called upon to perform. 

If these functions aren't always running and listening for requests, how then are they invoked, you might ask?

All FaaS platforms are event-driven. Essentially, every function we deploy is mapped to some event. And when that event occurs, the function is triggered.

Summarily, we use the term serverless to describe a Function as a Service or Backend as Service cloud solution where:

1. We don't have to manage long lived application instances or hosts for applications we deploy.
2. We don't have to manually scale up/down computing resources depending on traffic because the server automatically does that for us.
3. The pricing is precisely based on usage

Also, any application that's built on a significant number of BaaS solutions or designed to be deployed to a FaaS platform or even both can also be considered serverless.

Now that we're fully grounded in what serverless is, let's see how we can set up a minimal serverless REST API with AWS Lambda in tandem with AWS API Gateway.

## Serverless Example Project

Here, we will be setting up a minimal, perhaps uninteresting serverless REST API with AWS lambda and API Gateway. 

**AWS Lambda, API Gateway –** What are these things please?

They're serverless cloud solutions. Remember we stated that all serverless cloud solutions belong to one of two categories: BaaS and FaaS. AWS Lambda is a Function as a Service platform and API Gateway is a Backend as a Service solution.

How is API Gateway a Backend as a Service platform, you might ask?

Well, normally we implement routing in our applications ourselves. With API Gateway, we don't have to do that – instead, we cede the routing task to API Gateway.

**AWS Lambda, API Gateway, Our Application –** How are all these connected?

The connection is simple. AWS Lambda is where we will be deploying our actual application code. But because AWS Lambda is a FaaS platform, we are going to break our application into granular functions, with each function handling a single operation. We'll then deploy each function to AWS Lambda.

Oh okay, but where does API Gateway come in?

AWS Lambda, like all other FaaS platforms, is event-driven. What that means is, when you deploy a function to the platform, that function only does something when some event it's tied to happens. 

An event could be anything from an HTTP request to a file being uploaded to s3.

In our case, we will be deploying a minimal REST API backend. Because we are going serverless and more specifically the FaaS way, we are going to break down our REST backend into independent functions. Each function will be tied to some HTTP request. 

Actually, we will only be writing one function.

_API Gateway is the tool that we will use to tie a request to a function we've deployed._ So when that particular request comes in, the function is invoked.

Think of API Gateway as routing-as-a-service-tool :-). The image below depicts the relationship between the above entities.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Blank-diagram--3-.jpeg)
_API Gateway + AWS Lambda. Source: Author_

Ok, I get the connection. What's next?

### Let's Configure Stuff on AWS xD

The primary task here is to build a minimal paraphrasing tool. We are going to create a REST endpoint that accepts a POST request with some text as the payload. Our endpoint will then return a paraphrased version of that text as the response.

To achieve that, we will code a lambda function that does the actual paraphrasing of text blocks. We will then connect our function to the API gateway, just so whenever there is a POST request, our function will be triggered. 

But first, there are certain things we need to configure. Follow the steps in the following sections to configure all that you'd need to complete the task in this part.

Note: Some of the steps in the subsequent sections were adapted directly from [AWS' tutorial on serverless.](https://aws.amazon.com/getting-started/hands-on/build-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/)

### Step 1: Create an AWS Account

To create an account on AWS, follow the steps in module 1 of [this guide.](https://aws.amazon.com/getting-started/guides/setup-environment/)

### Step 2: Code our Lambda Function on AWS

Remember, we are going to need a function that does the actual text paraphrasing, and this is where we do that. Follow the steps below to create the lambda function:

1. Login to your AWS account using the credentials in step 1. In the search field, input 'lambda', and then select **Lambda** from the list of services displayed.
2. Click the **create function** button on the Lambda page.
3. Keep the default **Author from scratch** card selected.
4. Enter _paraphrase_text_ in the **Name** field.
5. Select **Python 3.9** for the **Runtime**.
6. Leave all the other default settings as they are and click on **create function**.
7. Scroll down to the **Function code** section and replace the exiting code in the **lamda_function.py** code editor with the code below:

```Python
import http.client

def lambda_handler(event, context):
    # TODO implement
    conn = http.client.HTTPSConnection("paraphrasing-tool1.p.rapidapi.com")

    payload = event['body']
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "paraphrasing-tool1.p.rapidapi.com",
        'x-rapidapi-key': "your api key here"
    }

    conn.request("POST", "/api/rewrite", payload, headers)
    res = conn.getresponse()
    data = res.read()

    return {
        'statusCode': 200,
        'body': data
    }
````

We are using [this API](https://rapidapi.com/healthytechguy/api/paraphrasing-tool1/) for the paraphrasing functionality. Head over to that page, subscribe to the basic plan, and grab the API key (it's free).

### Step 3: Test our Lambda Function on AWS

Here, we'll test our lambda function with a sample input to see that it produces the expected behavior: paraphrasing whatever text it is passed. 

To test your just created lambda function, follow the following steps:

1. From the main edit screen for your function, select **Configure test event** from the **Test** dropdown.
2. Keep **Create new test event** selected.
3. Enter _TestRequestEvent_ in the **Event name** field
4. Copy and paste the following test event into the editor:

```Python
{
  "path": "/paraphrase",
  "httpMethod": "POST",
  "headers": {
    "Accept": "*/*",
    "content-type": "application/json; charset=UTF-8"
  },
  "queryStringParameters": null,
  "pathParameters": null,
  "body": "{\r\"sourceText\": \"The bone of contention right now is how to make plenty money. \"\r\r\n    }"
}
```

You can replace the body text with whatever content you want. Once you're done pasting the above code, proceed with the following steps:

1. Click **create.**
2. On the main function edit screen, click **Test** with _TestRequestEvent_ selected in the dropdown.
3. Scroll to the top of the page and expand the **Details** section of the **Execution result** section.
4. Verify that the execution succeeded and that the function result looks like the following:

```Python
Response
{
  "statusCode": 200,
  "body": "{\"newText\":\"The stumbling block right now is how to make big bucks.\"}"
}
```

As seen above, the original text we passed our lambda function has been paraphrased.

### Step 3: Exposing our Lambda Function Via the API Gateway.

Now that we've coded our lambda function and it works, here, we'll expose the function through a REST endpoint that accepts a POST request. Once a request is sent to that endpoint, our lambda function will be called.

Follow the steps below to expose your lambda function via the API Gateway:

#### Create the API

1. In the search field, search and select **API Gateway**
2. On the API Gateway page, there are four cards under the **choose an API type** heading. Go to the **REST API** card and click **build.**
3. Next, provide all the required information as shown in the image below and click **Create API.**

![Image](https://www.freecodecamp.org/news/content/images/2022/02/api-gateway.PNG)
_For endpoint type, select Edge optimized_

#### Create the Resource and Method

**Resource, Method?** In the steps above we created an API. But an API usually has endpoint(s). An endpoint usually specifies a path and the HTTP method it supports. For example GET /get-user. Here, we call the path resource, and the HTTP verb tied to a path a method. Thus, resource + method = REST endpoint.

Here, we are going to create one REST endpoint that will allow users pass a text block to be paraphrased to our lambda function. Follow the steps below to accomplish that:

* First from the **Actions** dropdown select **Create Resource.** Next, fill the input fields and tick the check-box as shown in the image below and click **Create Resource.**

![Image](https://www.freecodecamp.org/news/content/images/2022/02/resource.PNG)
_You could replace resource name and resource path with anything you see fit. Notice how we've also enable CORS._

* With the newly created _/paraphrase_ resource selected, from the **Action** dropdown select **Create Method**. 
* Select _POST_ from the new dropdown that appears, then **click the checkmark**.
* Provide all the other info shown in the image below and click **save.**

![Image](https://www.freecodecamp.org/news/content/images/2022/02/method.PNG)
_lambda function is the name of the function we create in one of the previous steps._

#### Deploy the API

* In the **Actions** drop-down list, select **Deploy API**.
* Select **[New Stage]** in the **Deployment stage** drop-down list.
* Enter _production_ or whatever you wish for the **Stage Name**.
* Choose **Deploy**.
* Note the invoke URL is your API's base URL. It should look something like this: [https://wrl34unbe0.execute-api.eu-central-1.amazonaws.com/](https://wrl34unbe0.execute-api.eu-central-1.amazonaws.com/production){stage name}
* To test your endpoint, you can use postman or curl. Append the path to your endpoint to the end of the invoke URL like so: [https://wrl34unbe0.execute-api.eu-central-1.amazonaws.com/](https://wrl34unbe0.execute-api.eu-central-1.amazonaws.com/production){stage name}/paraphrase. And of course the request method should be POST.
* When testing, also add the expected payload to the request like so:

```Python
{
    "sourceText": "The bone of contention right now is how to make plenty money.   
}
```

## Wrapping Things up

Well that's it. First we learned all about the term serverless and then we went on to set up a light weight serverless REST API with AWS Lambda and API Gateway.

Serverless doesn't imply the total absence of servers, though. It is essentially about having a deployment flow where you don't have to worry about servers. The servers are still present, but they are being taken care of by the cloud provider.

We are going serverless each time if we build a significant components of our application on top of BaaS technologies or whenever we structure our application to be compatible with any FaaS platform (or when we do both).

Thank you for reading to this point. Want to connect? You can find me on [Twitter](https://twitter.com/nyior_clement), [LinkedIn](https://www.linkedin.com/in/nyior/), or [GitHub.](https://github.com/Nyior)

### References

%[https://learning.oreilly.com/library/view/what-is-serverless/9781491984178/]

Cover Image: [hestabit.com](https://www.hestabit.com/blog/serverless-architecture-explained/)

