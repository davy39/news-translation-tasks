---
title: How to Set Up AWS Cognito Authentication with Serverless and NodeJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-05T20:15:00.000Z'
originalURL: https://freecodecamp.org/news/aws-cognito-authentication-with-serverless-and-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/feature-psd-1.png
tags:
- name: AWS
  slug: aws
- name: node js
  slug: node-js
- name: serverless
  slug: serverless
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Shivang\nIn this post, we are going to see how we can create a REST\
  \ API application for authentication using AWS Cognito, AWS Serverless, and NodeJS.\
  \ \nWe are going to use Lambda functions, API Gateway, and the Serverless framework\
  \ to achieve this.\n..."
---

By Shivang

In this post, we are going to see how we can create a REST API application for authentication using AWS Cognito, AWS Serverless, and NodeJS. 

We are going to use Lambda functions, API Gateway, and the Serverless framework to achieve this.

Let’s start by setting up the project.

## **Project setup**

Our project structure will look like this:

![aws cognito project folder structure](https://devswisdom.com/wp-content/uploads/2021/12/folder-structure.png)

As you can see, we are storing all our lambda function files in a folder named _user_ and all our utility functions in a separate folder called _functions_. Other than that there is a _serverless.yml_ file which is a core file for any serverless-based project.

If you want to know more about this file, check out [this](https://devswisdom.com/use-websockets-with-aws-serverless/) post.

## **Serverless.yml file**

Let’s start coding our _serverless.yml_ file where we will be defining all our lambda functions. It will hold our logic for Sign up, Sign in, and so on. 

We will also define our AWS Cognito user pool and user pool client with different settings and permissions.

Let’s break this file into different parts so we can understand each part separately.

### **How to define **AWS IAM permissions and settings****

We will start by defining things like environment variables, serverless project configuration, settings, and AWS IAM permissions.

```yaml
service: serverless-cognito-auth

provider:
  name: aws
  runtime: nodejs14.x
  environment:
    user_pool_id: { Ref: UserPool }
    client_id: { Ref: UserClient }
  iamRoleStatements:
    - Effect: Allow
      Action:
        - cognito-idp:AdminInitiateAuth
        - cognito-idp:AdminCreateUser
        - cognito-idp:AdminSetUserPassword
      Resource: "*"
```

Under the `provider` block we are defining multiple configurations and settings. Let’s discuss each part in brief.

#### `environment`

In this block, we define all our environment variables which we want to use in our project, like in our lambda functions and so on. 

We set the user pool id and client id of our AWS Cognito user pool and client. 

And we are also referencing the resources which we are going to define later on in this file, so don’t worry about that. Just understand that these references are going to give us the id for the created user pool and client.

#### `iamRoleStatements`

In this block, we define all the AWS IAM permissions which we want to give to our resources, in our case these permissions are required by our lambda functions which are going to use the AWS Cognito API.

To read more about AWS IAM, check out the official [documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

### **How to define the **lambda functions****

Next, we will define our lambda functions. We are going to need three of them – one for user registration, one for user login, and the last one to test a private route.

```yaml
functions:
  loginUser:
    handler: user/login.handler
    events:
      - http:
          path: user/login
          method: post
          cors: true

  signupUser:
    handler: user/signup.handler
    events:
      - http:
          path: user/signup
          method: post
          cors: true

  privateAPI:
    handler: user/private.handler
    events:
      - http:
          path: user/private
          method: post
          cors: true
          authorizer:
            name: PrivateAuthorizer
            type: COGNITO_USER_POOLS
            arn:
              Fn::GetAtt:
                - UserPool
                - Arn
            claims:
              - email
```

In the `**events**` block, we define the event on which our lambda function will get invoked. So in our case, we are adding HTTP event here, which will be our AWS API Gateway call.

**`authorizer`** – Here we define our authorizer which will get called before our main lambda function gets invoked. So here we are using AWS Cognito authorizer for our API Gateway which checks on each request if the valid access token is being passed with it. And only then it allows our main lambda function to be invoked.

We need to pass ARN of our AWS Cognito user pool, so we are referencing that resource and getting the ARN from it by using the `:GetAtt` function. 

We are also using the `claims` block which to have the specific fields available from the decoded access token object in our main lambda function in the event object.

### **How to define the **resources****

Finally, we are going to define all the resources which we need in our _serverless.yml_ file.

```yaml
resources:
  Resources:
    UserPool:
      Type: AWS::Cognito::UserPool
      Properties:
        UserPoolName: serverless-auth-pool
        Schema:
          - Name: email
            Required: true
            Mutable: true
        Policies:
          PasswordPolicy:
            MinimumLength: 6
        AutoVerifiedAttributes: ["email"]

    UserClient:
      Type: AWS::Cognito::UserPoolClient
      Properties:
        ClientName: user-pool-ui
        GenerateSecret: false
        UserPoolId: { Ref: UserPool }
        AccessTokenValidity: 5
        IdTokenValidity: 5
        ExplicitAuthFlows:
          - "ADMIN_NO_SRP_AUTH"
```

Here we are creating our AWS Cognito user pool and client. Let’s go through some of the options now. If you want to see all the options which you can use, check out this official [documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html) and [this one](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html) as well for user pool client.

**`Schema`** – Here we define the schema of the user data which will be created in our user pool. We can define different attributes like email, age, gender, and so on.

**`Policies`** – In this block, we define our password validation policy – so basically all the settings of how the password should be before it can get saved in our user pool.

**`AutoVerifiedAttributes`** – Here we can set the fields which we want to be automatically verified like email and phone number. Generally when a new user gets created in the AWS Cognito user pool, that user has to go through a verification process to verify their email or phone number. But setting that field here is going to skip that verification process for the created user.

**`AccessTokenValidity`** – This defines the number of hours the access token will be valid.

**`ExplicitAuthFlows`** – This defines all the authentication flows which will be allowed by the user pool client. We are going to use `ADMIN_NO_SRP_AUTH` which can be used to authorize users with username and password – that’s why we are passing it here as the value.

I encourage you to also check out the official [documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) of AWS Cognito.

## **How to code **the lambda functions****

It’s now time to start coding our REST API logic by creating lambda functions for user registration, user login, and our private route to test everything out.

### **User registration**

First, we are going to create a new file inside th_e user_ folder and name it _signup.js_. This file will hold all the logic related to user registration. Let’s see how the code will look in this file by breaking it into parts.

#### **Imports**

```javascript
const AWS = require('aws-sdk')
const { sendResponse, validateInput } = require("../functions");

const cognito = new AWS.CognitoIdentityServiceProvider()
```

We are going to use `aws-sdk` NPM to interact with AWS Cognito API. We are also importing two utility functions (check out the code): `sendResponse` for sending the response of the HTTP request, and `validateInput` for validating the request body data. 

We are also getting the instance of the Cognito identity provider to interact with the user pool API.

#### **How to validate the **request body data****

```javascript
const isValid = validateInput(event.body)
if (!isValid)
return sendResponse(400, { message: 'Invalid input' })
```

Here we are validating the request body data and checking if the data is valid or not. If it is not valid, we are returning the response and sending an appropriate message.

#### **How to create **a user in** the **AWS Cognito user pool****

```javascript
const {
 email,
 password
 } = JSON.parse(event.body)
const {
 user_pool_id
 } = process.env

const params = {
  UserPoolId: user_pool_id,
  Username: email,
  UserAttributes: [{
      Name: 'email',
      Value: email
    },
    {
      Name: 'email_verified',
      Value: 'true'
    }
  ],
  MessageAction: 'SUPPRESS'
}
const response = await cognito.adminCreateUser(params).promise();
```

Here we get the email and password from the request body and also the user pool id from the environment variables object. 

After that, we create a parameter object for the `adminCreateUser` API. `MessageAction` is set as ‘SUPPRESS’ because we don’t want to send the default email sent by AWS Cognito when a new user gets created in the user pool.

#### **How to set **the password** for **the created user****

```javascript
if (response.User) {
  const paramsForSetPass = {
    Password: password,
    UserPoolId: user_pool_id,
    Username: email,
    Permanent: true
  };
  await cognito.adminSetUserPassword(paramsForSetPass).promise()
}
return sendResponse(200, {
  message: 'User registration successful'
})
```

When our user gets created in the user pool, we need to set the password for that user. We do this because we don’t want users to create a password when they login as they are already sending their password in the HTTP request. 

This will also change the user status to CONFIRMED in the Cognito user pool.

We also need to pass `Permanent` as `true` because otherwise a temporary password will be generated for the user.

### **User login**

Now we will start with the user login by creating a file inside the _user_ folder named _login.js_. This login API will start the authentication process and send the identity token to the user which they can use to access the authorized routes.

_login.js_ will look very similar to _signup.js_. The only difference will be the parameters and the API call.

#### **How to start **the authentication process****

```javascript
const {
  email,
  password
} = JSON.parse(event.body)
const {
  user_pool_id,
  client_id
} = process.env

const params = {
  AuthFlow: "ADMIN_NO_SRP_AUTH",
  UserPoolId: user_pool_id,
  ClientId: client_id,
  AuthParameters: {
    USERNAME: email,
    PASSWORD: password
  }
}
const response = await cognito.adminInitiateAuth(params).promise();
return sendResponse(200, {
  message: 'Success',
  token: response.AuthenticationResult.IdToken
})
```

The main thing to understand in this code is that we are using `AuthFlow` as ADMIN_NO_SRP_AUTH which is used for authenticating the user based on username and password. After that we are just calling the `adminInitiateAuth` API and sending the identity token to the user.

### **Private route**

We will add one more lambda function which will act as a private route. To access this API endpoint we will need to send a valid identity token in the request header with the key ‘Authorization’.

Start by creating a new file inside the _user_ folder and name it _private.js._

```javascript
module.exports.handler = async (event) => {
  return sendResponse(200, {
    message: `Email ${event.requestContext.authorizer.claims.email} has been authorized`
  })
}
```

Here we are just getting the email from the request and sending a simple response. This lambda function will only get invoked if the request passes the authorizer layer added in the API Gateway configuration.

To check out all the APIs offered by Nodejs SDK check [these docs](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityServiceProvider.html) out.

Also check out how [AWS Cognito Pricing](https://devswisdom.com/aws-cognito-pricing-and-features-2021/) gets calculated by AWS so you only spend what you wish to.

## **Conclusion**

Now you have the REST API for authentication using AWS Cognito, AWS Serverless, and Nodejs. Congrats!

Make sure to check out the GitHub code given at the end of this post. There are many things you can add or improve in the current code – the data validation can be increased, forget password can be added, and so on. I leave that up to you. 

We can also do this with DynamoDB, check out [AWS DynamoDB Pricing](https://devswisdom.com/aws-dynamodb-pricing-and-features/) to know more.

## **Get the code**

You can find the [source code on Github](https://github.com/shivangchauhan7/serverless-auth).

_You can [check out more articles like this](https://devswisdom.com/) on my site._ 

