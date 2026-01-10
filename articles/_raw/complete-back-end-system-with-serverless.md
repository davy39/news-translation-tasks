---
title: How to Build a Complete Back End System with Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-27T09:33:44.000Z'
originalURL: https://freecodecamp.org/news/complete-back-end-system-with-serverless
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/thumbnail.png
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: Backend Development
  slug: backend-development
- name: serverless
  slug: serverless
- name: serverless framework
  slug: serverless-framework
seo_title: null
seo_desc: 'By Sam Williams

  This article will teach you how to build and deploy everything you need to be able
  to build a back-end for your application. We''ll be using AWS to host all of this
  and deploying it all using the Serverless Framework.

  By the end of thi...'
---

By Sam Williams

This article will teach you how to build and deploy everything you need to be able to build a back-end for your application. We'll be using AWS to host all of this and deploying it all using the Serverless Framework.

By the end of this article you'll know how to:

* [Set up your AWS account to work with the Serverless Framework](#)
* [Set up a Serverless Project and deploy a Lambda](#)
* [Create private cloud storage with S3 bucket and upload files from your computer](#)
* [Deploy an API using API Gateway and AWS Lambda](#)
* [Create a serverless database table with AWS DynamoDB](#)
* [Create an API to get data from your DynamoDB table](#)
* [Create an API to add data to your DynamoDB table](#)
* [Create APIs to store files and get files from your S3 bucket](#)
* [Secure all of your API endpoints with API keys](#)

Being able to do all these things gives you the ability to create all the functionality needed from most application back ends.

<a class="anchor" id="setup"></a>

# **Serverless Setup with AWS**

The Serverless Framework is a tool that we can use as developers to configure and deploy services from our computers. There's a bit of setup to allow all of this to work together and this section will show you how to do that.

[Embedded content](https://www.youtube.com/embed/videoseries?list=PLmexTtcbIn_gP8bpsUsHfv-58KsKPsGEo)

To allow Serverless to do work on your account, you need to set up a user for it. To do this, navigate into AWS and search for "IAM" (Identity and Access Management).

Once on the IAM Page, click on _Users_ in the list on the left hand side. This will open the list of users on your account. From here we'll be clicking _Add user._

We need to create a user which has _Programmatic access_ and I've called my user _ServerlessAccount_, but the name doesn't matter too much.

![Image](https://completecoding.io/content/images/2019/08/createUser-1.png)

Next, we need to give the user some permissions. When on the permissions screen, select _Attach existing policies directly_ and then select _AdministratorAccess_. This will give the Serverless Framework permission to create all the resources it needs to.

We don't need to add any tags, so we can move straight onto _Review_.

![Image](https://completecoding.io/content/images/2019/08/credential.png)

On the review window, you'll see the user has been given an _Access key ID_ and a _Secret access key_. We'll be needing those in the next part so keep this page open.

### **Serverless Install and Configuration**

Now that we've created our user, we need to install the Serverless Framework on our machine.

Open up a terminal and run this command to install Serverless globally on your computer. If you haven't got NodeJS installed check out [this page.](https://nodejs.org/en/download/)

```
npm install -g serverless
```

Now that we've got Serverless installed, we need to set up the credentials for Serverless to use. Run this command, putting your _access key ID_ and _Secret access key_ in the correct places:

```js
serverless config credentials --provider aws --key ${Your access key ID} --secret ${Your secret access key} --profile serverlessUser
```

Once this has been run, you're all set up with Serverless.

<a class="anchor" id="firstlambda"></a>

# **Deploying Your First AWS Lambda**

With out serverlessUser set up, we want to deploy something using the Serverless Framework. We can use Serverless templates to setup a basic project that we can deploy. This will be the base for the whole of this Serverless project.

[Embedded content](https://www.youtube.com/embed/sku9Rrci-tE?feature=oembed)

In your terminal we can create a Serverless project from a template. This command will create a NodeJS Serverless project in the `myServerlessProject` folder:

```
serverless create --template aws-nodejs --path myServerlessProject

```

If you now open the folder up in your code editor we can look at what we've created.

![Image](https://completecoding.io/content/images/2019/12/folderStruct.png)

We've got two file worth talking about: `handler.js` and `serverless.yml`

### **handler.js**

This file is a function that will be uploaded as a Lambda function to your AWS account. Lambda functions are great and we'll use a lot more of them later on in the series.

### **serverless.yml**

This is a very important file for us. This is where all the configuration for our deployment goes. It tells Serverless what runtime to use, which account to deploy to, and what to deploy.

We need to make a change to this file so that our deployment works properly. In the `provider` object we need to add a new line of `profile: serverlessUser`. This tells Serverless to use the AWS credentials we created in the last section.

We can scroll down to `functions` and see that we have one function which is called `hello` and points to the function within the `handler.js` file. This means we will be deploying this Lambda function as part of this project.

We'll learn a lot more about this `serverless.yml` file later on in this article.

## **Deploying Our Project**

Now that we've looked at the files it's time to do our first deployment. Open up a terminal and navigate to our project folder. Deploying is as simple as typing:

```
serverless deploy

```

This takes a while, but when it's done we can check that everything has deployed successfully.

Open up your browser and navigate to your AWS account. Search for `Lambda` and you'll see a list of all your Lambda functions. (If you don't see any then check that your region is set to `N. Virginia`). You should see the `myserverlessproject-dev-hello` Lambda which contains the exact code that is in the `handler.js` file in your project folder.

<a class="anchor" id="s3"></a>

# **Deploying an S3 Bucket and Uploading Files**

In this section we're going to learn how we can deploy an Amazon S3 bucket and then sync up files from our computer. This is how we can start using S3 as cloud storage for our files.

[Embedded content](https://www.youtube.com/embed/8dc72i41r1A?feature=oembed)

Open up the `serverless.yml` file and remove all the commented out lines. Scroll to the bottom of the file and add the following code to include our S3 resources:

```
resources:
    Resources:
        DemoBucketUpload:
            Type: AWS::S3::Bucket
            Properties:
                BucketName: EnterAUniqueBucketNameHere

```

Change the name of the bucket and we're ready to deploy again. Open up your terminal again and run `serverless deploy`. You may get an error saying that the bucket name is not unique, in which case you'll need to change the bucket name, save the file and rerun the command.

If it is successful we can then go and see our new S3 bucket in our AWS Console through our browser. Search for `S3` and then you should see your newly created bucket.

## **Syncing up your files**

Having a bucket is great, but now we need to put files in the bucket. We're going to be using a Serverless plugin called S3 Sync to do this for us. To add this plugin to our project we need to define the plugins. After your provider object, add this code:

```
plugins:
    - serverless-s3-sync
```

This plugin also needs some custom configuration, so we add another field to our `serverless.yml` file, changing out the bucket name for yours:

```
custom:
    s3Sync:
        - bucketName: YourUniqueBucketName
          localDir: UploadData

```

This section of code is telling the S3 Sync plugin to upload the contents of the `UploadData` folder to our bucket. We don't currently have that folder so we need to create it and add some files. You can add a text file, an image, or whatever you want to be uploaded, just make sure there is at least 1 file in the folder.

The last thing we need to do is to install the plugin. Luckily, all Serverless plugins are also npm packages, so we can install it by running `npm install --save-dev serverless-s3-sync` in our terminal.

As we've done before, we can now run `serverless deploy` and wait for the deployment to complete. Once it is complete we can go back into our browser and into our bucket and we should see all the files that we put in the `UploadData` folder in our project.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.12.07.png)

<a class="anchor" id="api"></a>

# **Creating an API with Lambda and API Gateway**

In this section we'll learn to do one of the most useful things with Serverless: create an API. Creating an API allows you to do so many things, from getting data from databases, S3 storage, hitting other APIs, and much more!

[Embedded content](https://www.youtube.com/embed/Jruqo0KVOWk?feature=oembed)

To create the API we first need to create a new Lambda function to handle the request. We're going to make a few Lambdas, so we're going to create a `lambdas` folder in our project with two subfolders, `common` and `endpoints`.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.47.27.png)

Inside the endpoints folder we can add a new file called `getUser.js`. This API is going to allow someone to make a request and get back data based on the ID of a user. This is the code for the API:

```js
const Responses = require('../common/API_Responses');

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.ID) {
        // failed without an ID
        return Responses._400({ message: 'missing the ID from the path' });
    }

    let ID = event.pathParameters.ID;

    if (data[ID]) {
        // return the data
        return Responses._200(data[ID]);
    }

    //failed as ID not in the data
    return Responses._400({ message: 'no ID in data' });
};

const data = {
    1234: { name: 'Anna Jones', age: 25, job: 'journalist' },
    7893: { name: 'Chris Smith', age: 52, job: 'teacher' },
    5132: { name: 'Tom Hague', age: 23, job: 'plasterer' },
};

```

If the request doesn't contain an ID then we return a failed response. If there is data for that ID then we return that data. If there isn't data for that user ID then we also return a failure response.

As you may have noticed we are requiring in the `Responses` object from `API_Responses`. These responses are going to be common to every API that we make, so making this code importable is a smart move. Create a new file called `API_Responses.js` in the `common` folder and add this code:

```js
const Responses = {
    _200(data = {}) {
        return {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            },
            statusCode: 200,
            body: JSON.stringify(data),
        };
    },

    _400(data = {}) {
        return {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            },
            statusCode: 400,
            body: JSON.stringify(data),
        };
    },
};

module.exports = Responses;

```

This set of functions are used to simplify the creation of the correct response needed when using a Lambda with API Gateway (which we'll do in a sec). The methods add headers, a status code, and stringify any data that needs to be returned.

Now that we have the code for our API, we need to set it up in our `serverless.yml` file. Scroll to the `functions` section of the `serverless.yml` file. In the last part of this guide we deployed the `hello` function, but we no longer need that. Delete the functions object and replace it with this:

```yml
functions:
    getUser:
        handler: lambdas/endpoints/getUser.handler
        events:
            - http:
                  path: get-user/{ID}
                  method: GET
                  cors: true

```

This code is creating a new Lambda function called `getUser` which is in the file of `lambdas/getUser` on the method of `handler`. We then define the events that can trigger this lambda function to run.

To make a Lambda into an API we can add a `http` event. This tells Serverless to add an API Gateway to this account and then we can define the API endpoint using `path`. In this case `get-user/{ID}` means the URL will be `https://${something-provided-by-API-Gateway}/get-user/{ID}`, where the ID is passed into the Lambda as a path parameter. We also set the method to `GET` and enable CORS so that we could access this endpoint from a front end application if we wanted.

We can now deploy again, and this time we can use the shorthand command `sls deploy`. This only saves a few characters, but helps avoid a lot of typos. When this is completed we'll get an output that also includes a list of endpoints. We can copy our endpoint and head over to a browser to test it out.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.19.00.png)

If we paste our API URL into our browser and then add an ID to the end of 5132 we should get back a response of `{ name: 'Tom Hague', age: 23, job: 'plasterer' }`. If we enter a different ID such as 1234 we'll get different data, but entering an ID of 7890 or not entering an ID will return an error.

If we want to add more data to our API, we can simply add a new row to the data object in the `getUser.js` file. We can then run a special command which only deploys one function, `sls deploy -f ${functionName}`. So for us that is:

```
sls deploy -f getUser

```

If you now make a request using the ID of the new data, the API will return that new data instead of an error.

<a class="anchor" id="dynamo"></a>

# **Creating a Database on AWS**

DynamoDB is a fully hosted, non-relational database on AWS. This is the perfect solution for storing data that you need to access and update regularly. In this section we're going to learn how we can create a DynamoDB table with Serverless.

[Embedded content](https://www.youtube.com/embed/1de8NkTseqM?feature=oembed)

In our `serverless.yml` file we're going to add some configuration to the `Resources` section:

```
resources:
    Resources:
        DemoBucketUpload:
            Type: AWS::S3::Bucket
            Properties:
                BucketName: ${self:custom.bucketName}
        # New Code
        MyDynamoDbTable:
            Type: AWS::DynamoDB::Table
            Properties:
                TableName: ${self:custom.tableName}
                AttributeDefinitions:
                    - AttributeName: ID
                      AttributeType: S
                KeySchema:
                    - AttributeName: ID
                      KeyType: HASH
                BillingMode: PAY_PER_REQUEST

```

In this code we can see that we are creating a new DynamoDB table with a `TableName` of `${self:custom.tableName}`, defining an attribute of `ID` and setting the billing mode to pay per request.

This is our first look at the use of variables in our `serverless.yml` file. We can use variables for a few reasons and they can make our jobs much easier. In this case, we're referencing the variable `custom.tableName`. We can then reference this variable from multiple locations without having to copy and paste the table name. To get this to work we also need to add `tableName` to the custom section. In our case we're going to add the line `tableName: player-points` to create a table to store the points a player has. This table name only needs to be unique to your account.

When defining a table you need to define at least one of the fields which will be your unique identifying field. Because DynamoDB is a non-relational database, you don't need to define the full schema. In our case we've defined the `ID`, stating that it has an attribute type of string and a key type of `HASH`.

The last part of the definition is the billing mode. There are two ways to pay for DynamoDB:

* pay per request
* provisioned resources.

Provisioned resources lets you define how much data you're going to be reading and writing to the table. The issues with this are that if you start using more your requests get throttled, and that you pay for the resource even if no one is using it.

Pay Per Request it's much simpler as you just pay per request. This means if you have no one using it then you pay nothing and if your have hundreds of people using it at once, all the requests work. For this added flexibility you pay slightly more for Pay Per Request, but in the long run it usually works out to be cheaper.

Once we've run `sls deploy` again we can open up our AWS console and search for DynamoDB. We should be able to see our new table and we can see that there is nothing in there.

To add data to the table, click `Create item`, give it a unique ID, click the plus button and `append` to a new field and select the type of string. We need to give it a field of `name` and a value of `Jess`. Add a number field of `score` set to `12`. Click save and you now have data in your dynamo table.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.57.54.png)

<a class="anchor" id="dynamoGet"></a>

# **Getting Data from your DynamoDB Table**

Now that we have our Dynamo table created, we want to be able to get and add data to the table. We're going to start with getting data from the table with a get endpoint.

[Embedded content](https://www.youtube.com/embed/CpDFfSXRG04?feature=oembed)

We're going to create a new file in our `endpoints` folder called `getPlayerScore.js`. This Lambda endpoint is going to handle the requests for a user and get that data from the Dynamo table.

```js
const Responses = require('../common/API_Responses');
const Dynamo = require('../common/Dynamo');

const tableName = process.env.tableName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.ID) {
        // failed without an ID
        return Responses._400({ message: 'missing the ID from the path' });
    }

    let ID = event.pathParameters.ID;

    const user = await Dynamo.get(ID, tableName).catch(err => {
        console.log('error in Dynamo Get', err);
        return null;
    });

    if (!user) {
        return Responses._400({ message: 'Failed to get user by ID' });
    }

    return Responses._200({ user });
};

```

The code used here is very similar to the code inside the `getUser.js` file. We are checking that a path parameter of ID exists, getting the user data, and then returning the user. The main difference is how we are getting the user.

We have imported the `Dynamo` function object and are calling `Dynamo.get`. We're passing in the ID and the table name and then catching any errors. We now need to create that `Dynamo` function object in a new file called `Dynamo.js` in the common folder.

```js
const AWS = require('aws-sdk');

const documentClient = new AWS.DynamoDB.DocumentClient();

const Dynamo = {
    async get(ID, TableName) {
        const params = {
            TableName,
            Key: {
                ID,
            },
        };

        const data = await documentClient.get(params).promise();

        if (!data || !data.Item) {
            throw Error(`There was an error fetching the data for ID of ${ID} from ${TableName}`);
        }
        console.log(data);

        return data.Item;
    },
};
module.exports = Dynamo;

```

Reading and writing to Dynamo requires a reasonable amount of code. We could write that code every time we want to use Dynamo but it is much cleaner to have functions to simplify the process for us.

The file first imports AWS and then creates an instance of the DynamoDB Document Client. The document client is the easiest way for us to work with Dynamo from our Lambdas. We create a `Dynamo` object with an async get function. The only things we need to make a request are an ID and a table name. We format those into the correct parameter format for the DocumentClient, await a `documentClient.get` request, and make sure that we add `.promise()` to the end. This turns the request from a callback to a promise which is much easier to work with. We check that we managed to get an item from Dynamo and then we return that item.

We now have the all the code that we need, we have to update our `serverless.yml` file too. The first thing to do is to add our new API endpoint by adding it to our list of functions.

```
    getPlayerScore:
        handler: lambdas/endpoints/getPlayerScore.handler
        events:
            - http:
                  path: get-player-score/{ID}
                  method: GET
                  cors: true

```

There are two more changes that we need to make to get our endpoint working:

* environment variables
* permissions

You may have noticed in the `getPlayerScore.js` file we had a line of code like this:

```js
const tableName = process.env.tableName;

```

This is where we are getting the table name from the environment variables of the Lambda. To create our Lambda with the correct environment variables, we need to set a new object in the provider called `environment` with a field of `tableName` and a value of `${self:custom.tableName}`. This will ensure that we are making the request to correct table.

We also need to give our Lambdas permissions to access Dynamo. We have to add another field to the provider called `iamRoleStatements`. This has an array of policies which can allow or disallow access to certain services or resources:

```
provider:
    name: aws
    runtime: nodejs10.x
    profile: serverlessUser
    region: eu-west-1
    environment:
        tableName: ${self:custom.tableName}
    iamRoleStatements:
        - Effect: Allow
          Action:
              - dynamodb:*
          Resource: '*'

```

As all this has been added to the provider object, it will be applied to all Lambdas.

We can now run `sls deploy` again to deploy our new endpoint. When that is done we should get an output with a new endpoint of `https://${something-provided-by-API-Gateway}/get-player-score/{ID}`. If we copy that URL into a browser tab and add the ID of the player that we created in the last section, we should get a response.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.59.02.png)

<a class="anchor" id="dynamoPut"></a>

# **Adding New Data to DynamoDB**

Being able to get data from Dynamo is cool, but it's quite useless if we can't also add new data to the table as well. We're going to be creating a POST endpoint to create new data in our Dynamo table.

[Embedded content](https://www.youtube.com/embed/AguTaMQGACE?feature=oembed)

Start by creating a new file in our endpoints folder called `createPlayerScore.js` and adding this code:

```js
const Responses = require('../common/API_Responses');
const Dynamo = require('../common/Dynamo');

const tableName = process.env.tableName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.ID) {
        // failed without an ID
        return Responses._400({ message: 'missing the ID from the path' });
    }

    let ID = event.pathParameters.ID;
    const user = JSON.parse(event.body);
    user.ID = ID;

    const newUser = await Dynamo.write(user, tableName).catch(err => {
        console.log('error in dynamo write', err);
        return null;
    });

    if (!newUser) {
        return Responses._400({ message: 'Failed to write user by ID' });
    }

    return Responses._200({ newUser });
};

```

This code is very similar to the `getPlayerScore` code with a few changes. We are getting the user from the body of the request, adding the ID to the user, and then passing that to a `Dynamo.write` function. We need to parse the event body as API Gateway stringifies it before passing it to the Lambda.

We now need to modify the common `Dynamo.js` file to add the `.write` method. This performs very similar steps to the `.get` function and returns the newly created data:

```js
    async write(data, TableName) {
        if (!data.ID) {
            throw Error('no ID on the data');
        }

        const params = {
            TableName,
            Item: data,
        };

        const res = await documentClient.put(params).promise();

        if (!res) {
            throw Error(`There was an error inserting ID of ${data.ID} in table ${TableName}`);
        }

        return data;
    }

```

We've created the endpoint and common code, so the last thing we need to do is modify the `serverless.yml` file. As we added the environment variable and permissions in the last section, we just need to add the function and API configuration. This endpoint is different from the previous two because the method is `POST` instead of `GET`:

```
    createPlayerScore:
        handler: lambdas/endpoints/createPlayerScore.handler
        events:
            - http:
                  path: create-player-score/{ID}
                  method: POST
                  cors: true

```

Deploying this with `sls deploy` will now create three endpoints, including our `create-player-score` endpoint. Testing a `POST` endpoint is more complex than a `GET` request, but luckily there are tools to help us out. I use [Postman](https://www.getpostman.com/) to test all my endpoints as it makes it quick and easy.

Create a new request and paste in your `create-player-score` URL. You need to change the request type to `POST` and set the ID at the end of the URL. Because we're doing a POST request we can send up data within the body of the request. Click `body` then `raw` and select `JSON` as the body type. You can then add the data that you want to put into your table. When you click `Send`, you should get a successful response:

![Image](https://completecoding.io/content/images/2019/12/postman.png)

To validate that your data has been added to the table, you can make a get-player-score request with the ID of the new data you just created. You can also go into the Dynamo console and look at all the items in the table.

<a class="anchor" id="s3API"></a>

# **Creating S3 GET and POST Endpoints**

Dynamo is a brilliant database storage solution, but sometimes it isn't the best storage solution. If you've got data that isn't going to change and you want to save some money, or if you want to store files other than JSON, then you might want to consider Amazon S3.

[Embedded content](https://www.youtube.com/embed/MlKpK0WqTSs?feature=oembed)

Creating endpoints to get and create files in S3 is very similar to DynamoDB. We need to create two endpoint files, a common S3 file, and modify the `serverless.yml` file.

We're going to start with adding a file to S3. Create a `createFile.js` file in the endpoints folder and add this code:

```js
const Responses = require('../common/API_Responses');
const S3 = require('../common/S3');

const bucket = process.env.bucketName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.fileName) {
        // failed without an fileName
        return Responses._400({ message: 'missing the fileName from the path' });
    }

    let fileName = event.pathParameters.fileName;
    const data = JSON.parse(event.body);

    const newData = await S3.write(data, fileName, bucket).catch(err => {
        console.log('error in S3 write', err);
        return null;
    });

    if (!newData) {
        return Responses._400({ message: 'Failed to write data by filename' });
    }

    return Responses._200({ newData });
};

```

This code is almost identical to the `createPlayerScore.js` code, but uses a `filename` instead of an `ID` and `S3.write` instead of `Dynamo.write`.

Now we need to create our `S3` common code to simplify requests made to S3:

```js
const AWS = require('aws-sdk');
const s3Client = new AWS.S3();

const S3 = {
    async write(data, fileName, bucket) {
        const params = {
            Bucket: bucket,
            Body: JSON.stringify(data),
            Key: fileName,
        };
        const newData = await s3Client.putObject(params).promise();
        if (!newData) {
            throw Error('there was an error writing the file');
        }
        return newData;
    },
};
module.exports = S3;

```

Again, the code in this file is very similar to the code in `Dynamo.js`, with a few differences around the parameters for the request.

The last thing we need to do for writing to S3 is change the `severless.yml` file. We need to do four things: add environment variables, add permissions, add the function, and add an S3 bucket.

In the provider we can add a new environment variable of `bucketName: ${self:custom.s3UploadBucket}`.

To add permission to read and write to S3 we can add a new permission to the existing policy. Straight after `- dynamodb:*` we can add the line `- s3:*`.

Adding the function is the same as we've been doing with all our other functions. Make sure that the path has a parameter of `fileName` as that is what you are checking for in your endpoint code:

```
    createFile:
        handler: lambdas/endpoints/createFile.handler
        events:
            - http:
                  path: create-file/{fileName}
                  method: POST
                  cors: true

```

Lastly we need to create a new bucket to upload these files into. In the `custom` section we need to add a new field `s3UploadBucket` and set it to a unique bucket name. We also need to configure the resource. After the Dynamo table config, we can add this to create a new bucket for our file uploads:

```
        s3UploadBucket:
            Type: AWS::S3::Bucket
            Properties:
                BucketName: ${self:custom.s3UploadBucket}

```

With this set up it is time to deploy again. Running `sls deploy` again will deploy the new upload bucket as well as the S3 write endpoint. To test the write endpoint, we'll need to head back over to Postman.

Copy in the `create-file` URL that you get when Serverless has completed the deployment and paste it into Postman and change the request type to `POST`. Next, what we need to do is to add the filename that we are uploading. In our case we're going to be uploading `car.json`. The last thing we need to do is add the data to the request. Select `Body` then `raw` with a type of `JSON`. You can add whatever JSON data you would like but here's some example data:

```
{
	"model": "Ford Focus",
	"year": 2018,
	"colour": "red"
}
```

When you post this data up, you should get a `200` response with an `ETag` reference to the file. Going into the console and your new S3 bucket you should be able to see `car.json`.

## **Getting Data from S3**

Now that we can upload data to S3, we want to be able to get it back too. We start by creating a `getFile.js` file inside the endpoints folder:

```js
const Responses = require('../common/API_Responses');
const S3 = require('../common/S3');

const bucket = process.env.bucketName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.fileName) {
        // failed without an fileName
        return Responses._400({ message: 'missing the fileName from the path' });
    }

    const fileName = event.pathParameters.fileName;

    const file = await S3.get(fileName, bucket).catch(err => {
        console.log('error in S3 get', err);
        return null;
    });

    if (!file) {
        return Responses._400({ message: 'Failed to read data by filename' });
    }

    return Responses._200({ file });
};
```

This should look pretty similar to previous `GET` endpoints we've created before. Differences are the use of the `fileName` path parameter, `S3.get`, and returning the file.

Inside the common `s3.js` file we need to add the `get` function. The main difference between this and getting from Dynamo is that when we get from S3, the result is not a JSON response, but a `Buffer`. This means that if we upload a JSON file, it won't come back down in JSON format, so we check if we're getting a JSON file and then transform it back to JSON:

```js
    async get(fileName, bucket) {
        const params = {
            Bucket: bucket,
            Key: fileName,
        };
        let data = await s3Client.getObject(params).promise();
        if (!data) {
            throw Error(`Failed to get file ${fileName}, from ${bucket}`);
        }
        if (fileName.slice(fileName.length - 4, fileName.length) == 'json') {
            data = data.Body.toString();
        }
        return data;
    }

```

Back in our `serverless.yml` file, we can add a new function and endpoint for getting files. We've already configured the permissions and environment variables:

```
    getFile:
        handler: lambdas/endpoints/getFile.handler
        events:
            - http:
                  path: get-file/{fileName}
                  method: GET
                  cors: true
```

As we're creating a new endpoint we need to do a full deployment again with `sls deploy`. We can then take the new `get-file` endpoint and paste it into a browser or Postman. If we add `car.json` to the end of the request we'll receive the JSON data that we uploaded earlier in this section.

<a class="anchor" id="l9apikey"></a>

# **Securing Your Endpoints with API Keys**

Being able to create API endpoints quickly and easily with Serverless is great for starting a project and creating a proof of concept. When it comes to creating a production version of your application, you need to start being more careful about who can access your endpoints. You don't want anybody being able to hit your APIs.

[Embedded content](https://www.youtube.com/embed/n5aSq1L5nIw?feature=oembed)

To secure your APIs there are loads of methods, and in this section we're going to be implementing API keys. If you don't pass the API key with the request then it fails with an unauthorised message. You can then control who you give the API keys to, and therefore who has access to your APIs.

You can also add usage policies to your API keys so that you can control how much each person uses your API. This allows you to created tiered usage plans for your service.

To start we're going to be creating a simple API Key. To do this we need to go into our `serverless.yml` file and add some configuration to the provider.

```js
	apiKeys:
		myFirstAPIKey
```

This will create a new API key. Now we need to tell Serverless which API endpoints to protect with the API key. This has been done so that we can have some of the APIs protected, whilst some of them stay public. We specify that an endpoint needs to be protected by adding the option `private: true`:

```js
    getUser:
        handler: lambdas/endpoints/getUser.handler
        events:
            - http:
                  path: get-user/{ID}
                  method: GET
                  cors: true
                  private: true
```

You can then add this field to as many of your APIs as you would like. To deploy this we can run `sls deploy` again. When this completes, you will get back an API key in the return values. This is very important and we'll use it very soon. If you try and make a request to your `get-user` API you should get a 401 Unauthorised error.

To get the request to succeed, you now need to pass up an API key in the headers of the request. To do this we need to use Postman or another API request tool and add header to our get request. We do this by selecting `Authorisation` using the `API type`. The key needs to be `X-API-KEY` and the value is the key that you got as an output from your Serverless deploy:

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-20-at-20.05.53.png)

Now when we make the request we get a successful response. This means that the only people who can access your API are people who you have given your API key to.

This is great, but we can do more. We can add a usage policy to this API key. This is where we can limit the number of requests a month as well as the rate at which requests can be made. This is great for running a SAAS product as you can provide an API key that gives users a set amount of API calls.

To create a usage plan we need to add a new object in the provider. The `quota` section defines how many requests can be made using that API key. You can change the period to either `DAY` or `WEEK` if that would suit your application better.

The `throttle` section allows you to control how frequently your API endpoints can be hit. Adding a throttle `rate limit` sets a maximum number of requests per second. This is very useful as it stops people from setting up a denial of service attack. The `burstLimit` allows the API to be hit more often than your `rateLimit` but only for a short period of time, normally a few seconds:

```
    usagePlan:
        quota:
            limit: 10
            period: MONTH
        throttle:
            burstLimit: 2
            rateLimit: 1
```

If we were to deploy this again, the deployment would fail as we would be trying to deploy the same API key. API keys need to be unique so we have to change the name of the API key. When we deploy this and copy our new API key into Postman, we'll be able to make requests as we normally would. If we try and make too many requests per second or reach the maximum number of requests then we'll get a 429 error of

```
{
    "message": "Limit Exceeded"
}
```

This means that you can't use this API key again until next month.

Whilst creating a usage plan is great, you often want to give different people different levels of access to your services. You might give free users 100 requests per month and paying users get 1000. You might want different payment plans which give different number of requests. You would also probably want a master API key for yourself which has unlimited requests!

To do this we can set up multiple groups of API keys that each have their own usage policy. We need to change the `apiKeys` and `usagePlan` sections:

```
	apiKeys:
        - free:
              - MyAPIKey3
        - paid:
              - MyPaidKey3
    usagePlan:
        - free:
              quota:
                  limit: 10
                  period: MONTH
              throttle:
                  burstLimit: 2
                  rateLimit: 1
        - paid:
              quota:
                  period: MONTH
                  limit: 1000
              throttle:
                  burstLimit: 20
                  rateLimit: 10
```

Once you've saved and deployed this you'll get two new API keys, each with a different level of access to your API endpoints.

<style> a.anchor {
    display: block;
    position: relative;
    top: -40px;
    visibility: hidden;
}
</style>

Thanks for reading this guide! If you've found it useful, please subscribe to my [Youtube channel](https://www.youtube.com/channel/UC8uBP0Un18DJAnWjm1CPqBg) where I release weekly videos on Serverless and software development.

  

