---
title: How to quickly create a serverless RESTful API with Node.js and AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T01:30:16.000Z'
originalURL: https://freecodecamp.org/news/quickly-create-a-serverless-restful-api-with-nodejs-and-aws-lambda-api-gateway-and-a6be891cc16a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YofxX8XmRkh_uB4XMyq34g.png
tags:
- name: AWS
  slug: aws
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Mark Hopson

  In this beginner’s guide, we’ll briefly describe the “Serverless” software architecture,
  and then create a RESTful API using AWS, Node.js, and Swagger in a few short minutes.

  So what’s Serverless?

  The term Serverless (a.k.a. Functions-...'
---

By Mark Hopson

In this beginner’s guide, we’ll briefly describe the “Serverless” software architecture, and then create a RESTful API using AWS, Node.js, and Swagger in a few short minutes.

### So what’s Serverless?

The term Serverless (a.k.a. Functions-as-a-Service) describes a type of architecture that allows code to be deployed to, and run on, ephemeral and stateless containers from third-party vendors (like Azure or AWS).

#### Serverless Benefits

* **Reduced operational management.** Serverless architectures allows developers to focus on writing code, and not worry about configuring and managing the infrastructure that their code runs on.
* **Easy, flexible scaling.** Since Serverless “functions” (your Serverless applications) are stateless and always invoked by an event (like an HTTP request), you can run as many, or as few, functions as you need. More invocations mean more containers. Depending on the scale and shape of your traffic, this can be very cost efficient, since Serverless functions are typically billed per invocation.

#### Serverless Drawbacks

* **Latency for initial requests (known as “cold starts”).** If the Serverless function is inactive (has not been run in a while), then handling the first invocation can require extra time to complete because the container will have to initialize (that is, allocate host, load code, and so on).
* **Lack of system control**. Since your code is running in an environment managed by a vendor, you won’t be able to control system upgrades, or dependencies outside of your code base.

### And what’s CloudFormation?

CloudFormation is a service from Amazon that allows you to build AWS resources using templates. A template is a configuration file (YML or JSON) for provisioning all your AWS resources such as EC2 instances, DynamoDB tables, IAM roles and permissions, or anything else.

### Let’s Start Coding!

In this tutorial, we are going to make a simple RESTful API with the following two endpoints:

#### POST /users/${userId}/hello

The request body will be saved in a DynamoDB table. In this tutorial, the request body must have this structure: `{ "email": "any@email.com" }`

#### GET /users/${userId}/hello

The response will contain the value for `"email"` set in the POST request.

![Image](https://cdn-media-1.freecodecamp.org/images/P04BLr7QnCkdrzhpX6KANzaOxxwfzzUTzUGx)
_A simplified system architecture for what we’re going to build._

#### Step 1: Clone the repo

There are two files that you need for this tutorial: `index.js` (the NodeJS code for our Lambda function) and `stack.yml` (the CloudFormation stack template). To get these files, visit [this](https://github.com/markhopson/cloudformation-serverless-api) Github link.

#### Step 2: Examine the stack.yml file

Pay attention to the `stack.yml` in the repo, as it is the config file that will be used by CloudFormation to create everything our application will require.

Below is a detailed diagram of all the AWS resources our `stack.yml` will need to create. The names that are used in the YML are in the red boxes.

![Image](https://cdn-media-1.freecodecamp.org/images/B5oGAguxI6ZzZESx99yV0XWDk4nrQ1fnd1Pj)
_All the AWS resources (grey boxes) that will be provisioned by our `stack.yml` CloudFormation file._

#### Step 3: Upload your CloudFormation Template

After you check out the YML, head over to [this link](https://console.aws.amazon.com/cloudformation) and click the **Create Stack** button. Choose **Upload a template to Amazon S3** and upload the `stack.yml` file.

![Image](https://cdn-media-1.freecodecamp.org/images/vrSzSMhfzIEL6jbjhsoRqSlGLTTkZrqYNmAI)
_Create your CloudFormation stack by first uploading our `stack.yml` template._

On the next screen, you will be ask to pick a **Stack name** (can be anything). After this, click Next and select **I acknowledge that AWS CloudFormation might create IAM resources**, and click Next again**.**

At this point, your stack is being created. Wait a minute on the Stacks page until your stack’s status becomes **CREATE_COMPLETE**.

![Image](https://cdn-media-1.freecodecamp.org/images/C0drkb4xxGIHAJOwSzjYriMn4vDqn9-2xRCP)
_The CloudFormation Stacks listing page with status._

#### Step 4: Find your Lambda created by CloudFormation

Once your stack is complete, go and find your stack’s new Lambda [here](https://console.aws.amazon.com/lambda). Your Lambda’s Function name should resemble **${StackName}-HelloLambda-XXXX**.

![Image](https://cdn-media-1.freecodecamp.org/images/mjmf5CxbNznAvYisJXr2C7OAPevVVtyBMAYi)
_Lambda listing page_

#### Step 5: Deploy (copy and paste) your code to your Lambda

Once you’ve found your Lambda, click on it for more details. Then scroll to the **Function Code** section, change the **Code entry type** to **Edit code inline**, then open and copy `index.js` (from the repo) into the code editor. Click **Save**.

![Image](https://cdn-media-1.freecodecamp.org/images/Rm2WnYjfErwGdcI078HzvlMh8OSbFjwkuXJw)
_My Lambda details page with in-line code editor_

At this point, your code has been “deployed” to the Lambda, and all that’s left is to deploy our API Gateway so we can send HTTP requests to it.

#### Step 6: Find your API Gateway that was created by CloudFormation

Find your API Gateway created by your CloudFormation template [here](https://console.aws.amazon.com/apigateway). Your API Gateway’s name should resemble **${StackName}-MyApiGateway**.

![Image](https://cdn-media-1.freecodecamp.org/images/yfx9e9OPI6QdU577QQLufZ5TkBKHORDyTQik)
_The details page for the /hello POST endpoint_

#### Step 7: Test if your API Gateway is hooked up to Lambda

After you found your API Gateway, we can test to see if everything is hooked up by selecting the **POST** option under **/users** and then clicking **TEST .**

![Image](https://cdn-media-1.freecodecamp.org/images/uzYspS9a9seVUYWaxzT8avKmIVKFxPhfTXNx)
_The Test page for the /hello POST endpoint after a successful test request._

On the Test page, set **userId** to 123, and set the **Request Body** to the following and click **Test**. If everything worked, the **Status** should be **200** with no data.

![Image](https://cdn-media-1.freecodecamp.org/images/N8VquMDYIYnp792ZjcuXeM4BBhtQ6zJw5shU)
_The Test page for the /hello GET endpoint after a successful test request._

After testing the POST endpoint, you can check to see if your data was saved by going to the /hello GET Test page and trying a request (remember to set **userId** to 123). The response body should contain the Request Body from the POST test (see above).

Now that you’ve verified that your API Gateway, Lambda, and DynamoDB are hooked up, you can deploy your API Gateway so you can reach it from the internet.

#### Step 8: Deploy your API Gateway

To deploy your API, click the Actions menu and select Deploy API. Once the confirmation pop-up appears, set **Deployment stage** to **prod** and then click **Deploy**.

![Image](https://cdn-media-1.freecodecamp.org/images/61EyYYsUGVS1d8FBv2hwQFDCm2lksXbIUOnT)
_The Deploy API option un the Actions dropdown._

Once you’ve deployed your API, you will be forwarded to the **Stages** page for **prod**. Here you will find the domain for your API Gateway in the blue highlighted area beside **Invoke URL**.

![Image](https://cdn-media-1.freecodecamp.org/images/quo2GSkRBopc1s-bWDVZVgP1PWPu7iod1d8y)
_Find the public URL (Invoke URL) for your API Gateway in the big blue box._

Using the URL from the screenshot above, I should be able to send a **GET /users/123/hello** request in my web browser like below.

![Image](https://cdn-media-1.freecodecamp.org/images/1Z-JHxCJCE7QtuPvGVvYUtfO83EvqOMg9qap)
_A successful request to my Serverless API from the outside world_

And that’s it! You now have a Serverless RESTful API that is scalable, reliable, doesn’t require patching or provisioning, and doesn’t cost money when idle. I hope you’ve enjoyed this tutorial, and if you have any feedback, please leave it in the comments below. Thanks!

### Other Notes and Callouts

* The route configuration for API Gateway is embedded inside the API Gateway (MyApiGateway) configuration inside `stack.yml`, which makes the YML more of a monstrosity than it already is.
* Environment variables inside the HelloLambda Lambda configuration page contain the info needed to connect to the HelloTable DynamoDB table.
* The AWS-SDK comes bundled with every Lambda function so we can use `require('aws-sdk')` without a `package.json`. Very handy!
* Instead of copying and pasting the NodeJS code into the embedded editor inside the Lambda Details page, you can deploy your code through the AWS CLI. We copy and paste for simplicity.
* Be warned, the CloudFormation Stack Template is overwhelmingly verbose by nature. I promise it’s not just me and my`stack.yml`.
* HelloTable DynamoDB table’s primary partition key is **userId**
* From u/[**SalamiJack**](https://www.reddit.com/user/SalamiJack)**: “**it’s worth calling out that API Gateway + Lambda performance, even for a warmed up, simple Lambda, is quite bad. Expect in the realm of 80–150ms response times at all times.”

_Originally published at [medium.com](https://medium.com/@markhopson/how-to-create-a-serverless-restful-api-with-nodejs-and-aws-9aab63c636db) on March 26, 2018._

