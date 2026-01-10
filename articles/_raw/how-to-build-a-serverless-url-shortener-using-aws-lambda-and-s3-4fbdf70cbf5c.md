---
title: How to build a Serverless URL shortener using AWS Lambda and S3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-01T21:09:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-url-shortener-using-aws-lambda-and-s3-4fbdf70cbf5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9sb5DpSDIGpG1zhzvVAuXQ.png
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Daniel Ireson

  Throughout this post we’ll be building a serverless URL shortener using Amazon Web
  Services (AWS) Lambda and S3. Whilst you don’t require any previous experience with
  AWS, I’m assuming some familiarity with ES6 JavaScript and Node.js...'
---

By Daniel Ireson

Throughout this post we’ll be building a serverless URL shortener using Amazon Web Services (AWS) Lambda and S3. Whilst you don’t require any previous experience with AWS, I’m assuming some familiarity with ES6 JavaScript and Node.js.

Ironically, the URLs that will be generated from our URL shortener will often be longer than the URLs that they redirect to - this is because we’re using the default S3 bucket website address. Towards the end of the post I’ll discuss how you can add a custom domain to get around this limitation.

#### [View the demo](http://serverless-url-shortener.s3-website-eu-west-1.amazonaws.com)

#### [See the code on Github](https://github.com/danielireson/serverless-url-shortener)

![Image](https://cdn-media-1.freecodecamp.org/images/tEVMAYbvGlK1NVTUsULy984Ee322WWoMTtax)

It’s relatively easy to get started with AWS and yet there’s definitely a perceived complexity. The number of available services can be daunting to pick from as many of them overlap in functionality. The slow and unintuitive AWS Management Console doesn’t help, nor does the text-heavy online documentation. But throughout this post, I hope to demonstrate that the best way to adopt AWS services is to use an incremental approach and you can get started by using only a handful of services.

We’ll be using the [Serverless Framework](https://serverless.com) to interact with AWS and so there’ll be no need to login to the AWS Management Console. The Serverless Framework provides an abstraction over AWS and helps provide project structure and sensible configuration defaults. If you want to learn more before we get started you should have a read of their [docs](https://serverless.com/framework/docs/).

### Architecture

Before jumping into any development let’s first look at the AWS services we’ll be using to build our URL shortener.

To host our website we’ll use the Amazon S3 file storage service. We’ll configure our S3 bucket, which can be thought of as a top-level folder, to serve a static website. The website will consist of static content and client-side scripts. There’s no capability to execute server-side code (like PHP, Ruby or Java for example), but that’s fine for our use case.

We’ll also be using a [little known feature](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html) of S3 that allows you to setup forwarding for objects inside S3 buckets simply by adding a `Website-Redirect-Location` value to the metadata of the object. Setting this to a URL will have browsers redirected through a HTTP 301 response and the `location` header.

The URL of an S3 object is composed of the S3 bucket address followed by the object’s name.

```
http://[bucket-name].s3-website-eu-west-1.amazonaws.com/[object-name]
```

The following is an example of the format of an S3 bucket object for the `eu-west-1` region.

```
http://serverless-url-shortener.s3-website-eu-west-1.amazonaws.com/6GpLcdl
```

This object name “6GpLcdl” at the end of the URL in the example above becomes the shortcode for our shortened URLs. Using this functionality we get native URL redirection as well as storage capabilities. We don’t require a database to store the details of which shortcode points to which URL as this information will instead be stored with the object itself.

We’ll create a Lambda function for saving these S3 objects with the appropriate metadata to our S3 bucket.

You could alternatively use the AWS SDK client-side in the browser to save the objects. But it’s better to extract this functionality into a separate service. It provides the advantage of not having to worry about exposing security credentials and is more extendable in the future. We’ll map the Lambda function to an endpoint on API Gateway so it’s accessible through an API call.

### Getting started

Head on over to the [Serverless Framework docs](https://serverless.com/framework/docs/providers/aws/guide/quick-start/) and run through their quick-start guide. As part of the setup process, you’ll have to install the [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) and configure your AWS credentials.

Start by creating a `package.json` file at the root of the project.

```
{  "name": "serverless-url-shortener",  "scripts": {},  "dependencies": {}}
```

We know we’ll need to use the [AWS SDK](https://aws.amazon.com/sdk-for-node-js/), so go ahead and install it from NPM now by entering the following command.

`npm install aws-sdk --save`

Now create a `config.json` file also at the project root. We’ll use this to store customisable user options in JSON format.

Add the following keys with values appropriate to your setup.

* **BUCKET** - the name you want to use for your S3 bucket. This will become part of the short URL if you choose not to add a custom domain. It has to be unique to the region you’re deploying to so don’t pick something too generic. But don’t worry, if your chosen bucket name is already in use you’ll be warned through the Serverless CLI at deployment.
* **REGION** - the [AWS region](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) you wish to deploy to. It’s best to pick the region closest to your users for performance reasons. If you’re just following along with the tutorial I’ll be using `eu-west-1`.
* **STAGE** - the stage to deploy to. Typically you’d have a staging environment that replicates the same configuration as your production environment. This allows you to test software releases in a non-destructive manner. As this is a tutorial, I’ll be deploying to the `dev` stage.

Your `config.json` file should look similar to the following once complete.

```
{  "BUCKET": "your-bucket-name",  "REGION": "eu-west-1",  "STAGE": "dev",}
```

Next, create another file at the project root, `serverless.yml`. This will hold our Serverless Framework configuration formatted in the YAML markup language.

Inside this file we’ll start by defining our environment. Notice how we can reference variables stored earlier in `config.json`.

```
service: serverless-url-shortenerprovider:  name: aws  runtime: nodejs6.10  stage: ${file(config.json):STAGE}  region: ${file(config.json):REGION}  iamRoleStatements:    - Effect: Allow      Action:        - s3:PutObject      Resource: "arn:aws:s3:::${file(config.json):BUCKET}/*"
```

The `iamRoleStatements` section refers to [Identity and Access Management](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) which is used to set up Lambda permissions. Here we give the Lambda write-access to our S3 bucket.

To save objects we need permission to execute the `s3:PutObject` action. Other permissions can be added here if they are required by your project. Refer to the [S3 docs](http://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-objects) for other available actions.

The `Resource` value is set to the S3 bucket’s [Amazon Resource Name](http://Amazon Resource Name), which is used to uniquely identify a particular AWS resource. The format of this identifier depends upon the AWS service that is being referred to, but generally they have the following format.

```
arn:partition:service:region:account-id:resource
```

Underneath `provider` append our `functions` configuration.

```
functions:  store:    handler: api.handle    events:      - http:          path: /          method: post          cors: true
```

Here we define the API configuration and map our Lambda to an HTTP POST event at the API’s base URL. A `handler` with the value `api.handle` refers to a function named `handle` that is exported from `api.js` (we don’t need the _js_ file extension because earlier in `serverless.yml` we set the runtime to `nodejs6.10`).

Lambda is event based and so functions only get executed based on predefined triggers. Here we’ve defined a HTTP event but this could have also have been an event trigged by a DynamoDB table or an SQS queue.

Next in `serverless.yml` we define the AWS resources to be instantiated for us on deployment using [CloudFormation](https://aws.amazon.com/cloudformation). It’s worth mentioning that you don’t necessarily have to setup resources this way, you could also create them using the AWS Management Console. Providing the correct access permissions are in place it doesn’t matter how the resources are created. But in defining the required services in `serverless.yml` you’re defining your ‘infrastructure as code’ and obtain a number of benefits in doing so.

> “Infrastructure as code is the approach to defining computing and network infrastructure through source code that can then be treated just like any software system. Such code can be kept in source control to allow auditability and ReproducibleBuilds, subject to testing practices, and the full discipline of ContinuousDelivery.”

> - Martin Fowler

Go ahead and add the `resources` configuration.

```
resources:  Resources:    ServerlessRedirectS3Bucket:      Type: AWS::S3::Bucket      Properties:        BucketName: ${file(config.json):BUCKET}        AccessControl: PublicRead        WebsiteConfiguration:          IndexDocument: index.html    ServerlessRedirectS3BucketPolicy:      Type: AWS::S3::BucketPolicy      Properties:        Bucket: ${file(config.json):BUCKET}        PolicyDocument:          Statement:          - Action:            - s3:GetObject            Effect: Allow            Resource:            - arn:aws:s3:::${file(config.json):BUCKET}/*            Principal: "*"
```

We ask for an S3 bucket resource configured to use static site hosting with `index.html` as the root document. S3 buckets for good reason are private by default and so we need to create an S3 bucket policy which allows public access to it. Without this policy website visitors would instead by shown an unauthenticated error message.

### Building the API

Our Lambda function is responsible for four tasks.

1. Grabbing the URL to shorten from the user’s form submission.
2. Generating a unique shortcode for the URL.
3. Saving the appropriate redirect object to S3.
4. Returning the object’s path to the client.

#### Create the handler

Create a new file called `api.js` and export an arrow function named `handle` which takes three arguments: `event`_,_ `context` and `callback`_._ These will be provided by AWS when the handler is invoked. This file is a Node.js script and in order to export the arrow function you need to append it to `module.exports`.

```
module.exports.handle = (event, context, callback) => {
```

```
}
```

This handler will get invoked when a HTTP POST request is made to our endpoint. To return an API response we need to use the supplied callback function provided as the third arrow function argument. It’s an [error-first callback](http://fredkschott.com/post/2014/03/understanding-error-first-callbacks-in-node-js/) which takes two arguments. If the request completed successfully `null` should be passed in as the first argument. The response object passed in as the second argument determines the type of response to be returned to the user. Generating a response is as simple as providing a `statusCode` and `body` as is shown in the example below.

```
const response = {  statusCode: 201,  body: JSON.stringify({ "shortUrl": "http://example.com" })}
```

```
callback(null, response)
```

The `context` object passed in as the second argument to the handler contains run-time information which for this tutorial we don’t need access to. We do however need to make use of the `event` passed in as the first argument as this contains the form submission with the URL to shorten.

#### Parse the request

Below is an example of an API Gateway event that will be passed to our handler when a user makes a form submission. As we’re building our URL shortener as a single page application we’ll be submitting the form using JavaScript and hence the content type will be `application/json` rather than `application/x-www-form-urlencoded`.

```
{     resource:'/',   path:'/',   httpMethod:'POST',   headers: {      Accept:'*/*',      'Accept-Encoding':'gzip, deflate',      'cache-control':'no-cache',      'CloudFront-Forwarded-Proto':'https',      'CloudFront-Is-Desktop-Viewer':'true',      'CloudFront-Is-Mobile-Viewer':'false',      'CloudFront-Is-SmartTV-Viewer':'false',      'CloudFront-Is-Tablet-Viewer':'false',      'CloudFront-Viewer-Country':'GB',      'content-type':'application/json',      Host:'',      'User-Agent':'',      'X-Amz-Cf-Id':'',      'X-Amzn-Trace-Id':'',      'X-Forwarded-For':'',      'X-Forwarded-Port':'443',      'X-Forwarded-Proto':'https'   },   queryStringParameters:null,   pathParameters:{},   stageVariables:null,   requestContext: {        path:'/dev',      accountId:'',      resourceId:'',      stage:'dev',      requestId:'',      identity:{           cognitoIdentityPoolId:null,         accountId:null,         cognitoIdentityId:null,         caller:null,         apiKey:'',         sourceIp:'',         accessKey:null,         cognitoAuthenticationType:null,         cognitoAuthenticationProvider:null,         userArn:null,         userAgent:'',         user:null      },      resourcePath:'/',      httpMethod:'POST',      apiId:''   },   body:'{"url":"http://example.com"}',   isBase64Encoded:false}
```

We only need the form submission from the event, which we can get by looking at the request `body`. The request body is stored as a stringified JavaScript object which we can grab inside of our handler using `JSON.parse()`. Taking advantage of [JavaScript short-circuit evaluation](http://www.jstips.co/en/javascript/short-circuit-evaluation-in-js/) we can set a default value of an empty string for cases where a URL hasn’t been sent as part of the form submission. This allows us to treat instances where the URL is missing and where the URL is an empty string equally.

```
module.exports.handle = (event, context, callback) => {  let longUrl = JSON.parse(event.body).url || ''}
```

#### Validate the URL

Let’s add some basic validation to check that the provided URL looks legitimate. There are multiple approaches that could be taken to achieve this. But for the purpose of this tutorial we’ll keep it simple and use the built-in [Node.js URL](https://nodejs.org/api/url.html) module. We’ll build our validation to return a resolved promise on a valid URL and return a rejected promise on an invalid URL. Promises in JavaScript can be sequentially chained so that the resolution of one promise gets passed to the success handler of the next. We’ll be using this attribute of promises to structure our handler. Let’s write the validate function using promises.

```
const url = require('url')
```

```
function validate (longUrl) {  if (longUrl === '') {    return Promise.reject({      statusCode: 400,      message: 'URL is required'    })  }
```

```
let parsedUrl = url.parse(longUrl)  if (parsedUrl.protocol === null || parsedUrl.host === null) {    return Promise.reject({      statusCode: 400,      message: 'URL is invalid'    })  }
```

```
return Promise.resolve(longUrl)}
```

In our `validate` function we first check that the URL isn’t set to an empty string. If it is we return a rejected promise. Notice how the rejected value is an object containing a status code and message. We’ll use this later to build an appropriate API response. Calling `parse` on the Node.js `url` module returns a URL object with information that could be extracted from the URL that was passed in as a string argument. As part of our basic URL validation we simply check to see whether a protocol (For example, ‘http’) and a host (like ‘example.com’) could be extracted. If either of these values is `null` on the returned URL object, we assume that the URL is invalid. If the URL is valid we return it as part of a resolved promise.

#### Returning a response

After grabbing the URL from the request we call `validate` and for each additional handler step that’s required we’ll return a new promise in the previous promise’s success handler. The final success handler is responsible for returning an API response through the handle’s callback argument. It will be invoked for both error API responses generated from rejected promises as well as successful API responses.

```
module.exports.handle = (event, context, callback) => {  let longUrl = JSON.parse(event.body).url || ''  validate(longUrl)    .then(function(path) {      let response = buildResponse(200, 'success', path)      return Promise.resolve(response)    })    .catch(function(err) {      let response = buildResponse(err.statusCode, err.message)      return Promise.resolve(response)    })    .then(function(response) {      callback(null, response)    })}
```

```
function buildResponse (statusCode, message, path = false) {  let body = { message }  if (path) body['path'] = path    return {    headers: {      'Access-Control-Allow-Origin': '*'    },    statusCode: statusCode,    body: JSON.stringify(body)  }}
```

#### Generate a URL shortcode

The API needs to be able to generate unique URL shortcodes, which are represented as filenames in the S3 bucket. As a shortcode is just a filename there’s a great degree of flexibility in how it’s composed. For our shortcode we’ll use a 7 digit alphanumeric string consisting of both uppercase and lowercase characters, this translates to 62 possible combinations for each character. We’ll use recursion to build up the shortcode by selecting one character at a time until seven have been selected.

```
function generatePath (path = '') {  let characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  let position = Math.floor(Math.random() * characters.length)  let character = characters.charAt(position)
```

```
if (path.length === 7) {  return path}
```

```
return generatePath(path + character)}
```

Whilst the chance of randomly generating the same shortcode is slim (there’s actually a 0.0000000000000000000000008063365516 chance that two shortcodes will be the same), we need to check whether the generated shortcode is already in use, which we can do using the AWS SDK. There’s a `headObject` method on the S3 service which loads an object’s metadata. We can use this to test whether an object with the same name already exists as when an object isn’t found a promise with the code _NotFound_ is rejected. This rejected promise indicates that the shortcode is free and can be used. Calling `headObject` is more performant than testing whether the object exists through `getObject`, which loads the entire object.

```
const AWS = require('aws-sdk')const S3 = new AWS.S3()
```

```
function isPathFree (path) {  return S3.headObject(buildRedirect(path)).promise()    .then(() => Promise.resolve(false))    .catch(function (err) {      if (err.code == 'NotFound') {        return Promise.resolve(true)      } else {        return Promise.reject(err)      }    })}
```

```
function buildRedirect (path, longUrl = false) {  let redirect = {    'Bucket': config.BUCKET,    'Key': path  }
```

```
if (longUrl) {    redirect['WebsiteRedirectLocation'] = longUrl  }
```

```
return redirect}
```

We can use `isPathFree` to recursively find a unique object path.

```
function getPath () {  return new Promise(function (resolve, reject) {    let path = generatePath()    isPathFree(path)      .then(function (isFree) {        return isFree ? resolve(path) : resolve(getPath())      })  })}
```

Taking advantage of the ability to chain promises we return a new invocation of `getPath` if `isPathFree` returns false.

To save an object after a unique shortcode has been found we just need to call the `putObject` method on the AWS SDK S3 service. Let’s wrap this up in a function that resolves the shortcode if the `putObject` method call was successful and returns an error object to build an API response if it didn’t.

```
function saveRedirect (redirect) {  return S3.putObject(redirect).promise()    .then(() => Promise.resolve(redirect['Key']))    .catch(() => Promise.reject({      statusCode: 500,      message: 'Error saving redirect'  })}
```

Utilizing the above functions we can add two new promise success handlers to finalise our API endpoint. We need to return `getPath` from the first promise success handler which will resolve a unique URL shortcode. Returning `saveRedirect` with a redirect object built using this unique shortcode in the second success handler will save the object to the S3 bucket. This object’s path can then be returned to the client as part of an API response. Our handler should now be complete.

```
module.exports.handle = (event, context, callback) => {  let longUrl = JSON.parse(event.body).url || ''  validate(longUrl)    .then(function () {      return getPath()    })    .then(function (path) {      let redirect = buildRedirect(path, longUrl)      return saveRedirect(redirect)    })    .then(function (path) {      let response = buildResponse(200, 'success', path)      return Promise.resolve(response)    })    .catch(function (err) {      let response = buildResponse(err.statusCode, err.message)      return Promise.resolve(response)    })    .then(function (response) {      callback(null, response)    })}
```

#### Deploy the API

Run `serverless deploy` in your terminal to deploy the API to AWS. This will setup our S3 bucket and return the URL of the endpoint. Keep the URL of the endpoint handy as we’ll need it later on.

```
Serverless: Packaging service...Serverless: Excluding development dependencies...Serverless: Uploading CloudFormation file to S3...Serverless: Uploading artifacts...Serverless: Uploading service .zip file to S3 (5.44 MB)...Serverless: Validating template...Serverless: Updating Stack...Serverless: Checking Stack update progress.................Serverless: Stack update finished...Service Informationservice: serverless-url-shortenerstage: devregion: eu-west-1stack: serverless-url-shortener-devapi keys:  Noneendpoints:  POST - https://t2fgbcl26h.execute-api.eu-west-1.amazonaws.com/dev/functions:  store: serverless-url-shortener-dev-storeServerless: Removing old service versions...
```

### Creating the frontend

To assist with frontend design we’ll be utilizing the [PaperCSS](https://github.com/papercss/papercss) framework. We’ll also be grabbing [jQuery](https://jquery.com/) to simplify working with the DOM and making AJAX queries. It’s worth noting that for a production environment you’d probably want to pull in two lighter dependencies, but as this is just a tutorial I feel it’s acceptable.

Create a `static` folder so we have somewhere to store our frontend code.

#### Download the dependencies

Save a copy of [paper.min.css](https://github.com/papercss/papercss/releases/download/v1.3.1/paper.min.css) and [jquery-3.2.1.min.js](https://code.jquery.com/jquery-3.2.1.min.js) to our newly created `static` folder, these are minified versions of the PaperCSS framework and jQuery library respectively.

#### Add the HTML

Create a new file called `index.html` inside the `static` folder and add the required HTML. We need a form with a URL input and a button to submit the form. We also need somewhere to put the result of any API calls, which for a successful API call would be the shortened URL and for an unsuccessful API call this would be the error message.

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <meta name=viewport content="width=device-width,initial-scale=1">  <title>Serverless url shortener</title>  <link href="paper.min.css" rel="stylesheet"></head><style>  * {    text-align: center;  }
```

```
  #message {    display: none;  }</style><body>  <div class="row flex-center">    <div class="col-8 col">      <h2>Serverless url shortener</h2>      <form action="">        <div class="form-group">          <label for="url">Enter URL to shorten</label>          <input             class="input-block"             name="url"             type="url"             id="url"              autocomplete="off"             required>        </div>        <div id="message" class="alert alert-primary"></div>        <input           class="paper-btn"           type="submit"           value="Shorten link">      </form>      <p class="padding-top">        <a href="https://git.io/vbS8I">          View this project on Github        </a>      </p>    </div>  </div></body></html>
```

Although not shown in the code block above for brevity, be sure you set the form action to the API endpoint that was displayed when you ran `serverless deploy`. If you’ve no longer got access to your terminal output from that deployment, you can find out the endpoint URL through the `serverless info` command.

#### Make API requests

Before writing the JavaScript to make requests to our API, let’s first load jQuery by appending a script tag just before `</bo`dy> and referencing the minified file we downloaded previously.

```
<script src="jquery-3.2.1.min.js"></script>
```

Now add another pair of script tags underneath and inside let’s create a function that can be used to display a message to the user using the message `div` in our template that is set to `display:none` by default on page load. To show a message we can simply set the text inside of this `div` using `text()` and toggle the display using `show()`.

```
<script>  function addMessage (text) {    $('#message').text(text).show()  }</script>
```

Let’s write another function to go inside the same set of script tags that will use jQuery to make requests to our API.

```
function shortenLink (apiUrl, longUrl) {  $.ajax(apiUrl, {    type : 'POST',     data: JSON.stringify({url: longUrl})})    .done(function (responseJSON) {      var protocol = window.location.protocol + '//'      var host = window.location.host + '/'      var shortUrl = protocol + host + responseJSON.path      addMessage(shortUrl)    })    .fail(function (data) {      if (data.status === 400) {        addMessage(data.responseJSON.message)      } else {        addMessage('an unexpected error occurred')      }    })}
```

This function creates a POST request and sets the request body to a JSON object containing the URL to shorten. If the request completed successfully and a HTTP 2XX status code was returned, it grabs the shortcode from the `path` key on the response and builds up a fully qualified short URL to present to the user using the `addMessage` function created previously. If the request was unsuccessful then an error message is displayed.

Finally we can hook this up to our form by adding an on submit handler. We get the API endpoint URL from the form action attribute and get the URL to shorten from the `url` form input.

```
$('form').submit(function (event) {  event.preventDefault()  addMessage('...')  shortenLink(event.target.action, event.target.url.value)})
```

#### Deploy the website

For website deployment we’ll use the AWS CLI `sync` command to upload the contents of the static folder to our S3 bucket. Run `aws s3 sync static s3://[bucket]` in your terminal, replacing `[bucket]` with your bucket name chosen in `config.json`. After this completes you should be able to head to your S3 bucket address in a browser to see the URL shortener in action. Public URLs for S3 buckets take the following form.

```
http://[bucket].s3-website-[region].amazonaws.com
```

So after adding your bucket name and region your URL shortener address should look similar to the below.

```
http://serverless-url-shortener.s3-website-eu-west-1.amazonaws.com
```

To add a custom domain to your bucket you should follow one of the instructions in [this AWS support article](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html). For the easiest option you should set the bucket name to your domain’s `www` subdomain (for example www.example.com). If you then add a CNAME record in your DNS configuration for the `www` subdomain and set it to your S3 bucket address, the website should be accessible via your domain. Be sure to also remove any existing `A` records and bear in mind that this won’t set up a redirection from your root domain to the `www` subomain. There’s a couple of ways this could be solved which are described in the AWS article.

### Wrap up

I hope you found this tutorial useful. The reality is that AWS is incredibly flexible and in this article we went through just one way you can create a URL shortener using Lambda and S3. But there are a variety of other ways the same process could also have been accomplished.

If you found this interesting you might enjoy [one of my previous articles](https://hackernoon.com/creating-a-form-forwarding-service-for-aws-lambda-aec07af9f951) where I created a form forwarding service using AWS Lambda.

[**Introducing Formplug v1, a form forwarding service for AWS Lambda**](https://hackernoon.com/introducing-formplug-v1-a-form-forwarding-service-for-aws-lambda-2c125dfe608e)  
[_It’s estimated that approximately 269 billion emails are sent in a single day. Over 10 million were sent as you read…_hackernoon.com](https://hackernoon.com/introducing-formplug-v1-a-form-forwarding-service-for-aws-lambda-2c125dfe608e)

