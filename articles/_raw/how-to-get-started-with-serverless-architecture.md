---
title: How to Get Started With Serverless Architecture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-18T01:09:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-serverless-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/serverless-cover-1.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Anirban Das

  Traditionally, when you wanted to build a web app or API, you’d usually have to
  spend significant time and effort managing servers and ensuring your app scales
  up to handle large request volumes. Serverless is a cloud computing model w...'
---

By Anirban Das

Traditionally, when you wanted to build a web app or API, you’d usually have to spend significant time and effort managing servers and ensuring your app scales up to handle large request volumes. Serverless is a cloud computing model which lets you run applications without having to worry about managing and scaling servers.

All you need to do is to upload your code to a cloud provider’s service, and they automatically provision an ephemeral environment. Unlike traditional architectures, it can scale up to handle thousands of requests in an instant, and you only pay for the duration during which your code executes.

In this article, we’ll build a simple contact form powered by AWS’s (Amazon Web Services) serverless offering, Lambda. However, serverless is suitable for applications of any complexity or size. As an example, we built [myCompiler](https://www.mycompiler.io/) — a programming playground that supports 20 languages — and it is largely powered by serverless.

Before we get started, we’ll take a closer look at how serverless and Lambda work, and the architecture that we’re going to set up for our contact form. Also, towards the end of this article, we’ll look at some tools which are meant to help with building and deploying large serverless applications.

You’ll need an AWS account to follow along this guide, and [you can register here](https://portal.aws.amazon.com/billing/signup). Our AWS usage for this guide will be entirely covered by the free tier.

## How does AWS Lambda work?

In this section, we'll understand the workflow with Lambda and a brief understanding of how it works. However, these concepts apply to most other cloud providers’ serverless offerings as well.

With Lambda, you upload your code to AWS, which is usually a script written in Python, Node.js or Ruby. In the case of a language such as Go, Java or C#, it is a Linux executable or a package in the language’s format (such as jar files for Java).

After uploading your code, you can then"invoke" it manually or use another AWS service for this purpose (we'll look at this in detail in a moment). When you invoke your code, Lambda creates a secure, ephemeral Linux environment called a"container" on one of their servers, and any data that you passed as part of the invocation is fed to your function.

Once the function completes execution, the Lambda service returns the results of the code to its caller. The container can then be reused to serve another execution, or if the function hasn't been invoked for a long time, the container is destroyed.

When you make parallel invocations, Lambda creates a container to serve each invocation. Because each invocation is dedicated to a single container, each invocation gets ample resources for execution. You can assign anywhere from 128 MB to 3 GB of memory to each invocation, along with CPUs that increase with memory. Combine this with the fact that it can serve up to a 1000 parallel invocations (this can be increased by contacting AWS), you can handle heavy workloads without having to worry about scaling.

So, with scaling concerns out of the way, what does AWS Lambda cost us to run? Lambda usage is measured using the following parameters: the number of requests, the memory allocated to it, and the number of milliseconds your functions take to run.

If you choose the smallest memory size (128 MB), and your functions take 1 second to run when you invoke it, you can invoke your function up to a million times for free. After that, every 1 million invocations can cost up to $2.30. A memory size of 128 MB might seem tiny, but it is certainly enough to handle many kinds of workloads.

## API gateway — Serving HTTP requests with Lambda

As we mentioned previously, once you upload your code, you have to invoke it manually. To build a web app, you'd need to have a server that listens for HTTP requests, invokes your function with the details of the request, and translates the data returned from your function as a HTTP response. 

AWS has another service which allows you to do just that — API gateway. Just like Lambda, it is another AWS managed service which can automatically scale up to handle extremely high request volumes.

Once you create an API gateway, you'll get a base URL which looks something like this:  
`https://abcdefgh.execute-api.us-east-1.amazonaws.com/`

Under this base URL, you can map paths and request methods (such as GET or POST) to your functions. You also have the option of creating your custom domain if you’d like to use something else other than the default, but we won’t go through that in this guide.

Also, just like Lambda, API gateway’s pricing is great too — you can serve up to a million requests for free, and after that every 1 million requests costs you $1.

## Building a contact form

We’ll build a simple contact form that sends us an email containing the details that our user fills in. This is how we’ll build out the various parts of the contact form:

1. First, we’ll set up SES (Simple Email Service), AWS’s email offering. This is to help us send emails for the contact form.
2. Next, we’ll set up a “role” for Lambda, and then create a Lambda function that receives the HTTP request and sends us an email.
3. We’ll set up API gateway and map it to the function that we created in step 2.
4. We’ll then set up a web page that interacts with the API gateway endpoint and submits details filled in by the user.

At the end of this guide, you’ll set up something that works like this:

![Serverless app](https://www.freecodecamp.org/news/content/images/2020/03/serverless-app.png)

To get started, visit the [AWS management console](http://console.aws.amazon.com/) (or simply, the“console”) and log in with the details that you used to sign up. Once you’ve logged in, you can use the “Services” dropdown in the navigation bar to switch between various services that we’re going to use.

![AWS management console](https://www.freecodecamp.org/news/content/images/2020/03/AWS-management-console.png)

## Setting up SES for sending emails

Begin by visiting the SES (Simple Email Service) section of the console through the “Services” dropdown, or by using this [direct link](https://console.aws.amazon.com/ses/home). Then, click on the “Email Addresses” section on the left. You’ll be greeted with this page:

![AWS SES](https://www.freecodecamp.org/news/content/images/2020/03/AWS-SES.png)

Click on the “Verify a New Email Address” button and then enter your email address, and click “Verify This Email Address”. You’ll receive an email with a verification link. Open it to verify the address, and then refresh the SES console page. You’ll see that the email address has been verified:

![AWS SES verify email address](https://www.freecodecamp.org/news/content/images/2020/03/AWS-SES-verify-email-address.png)

At this point, you’ll be able to send emails for your email address using SES.

## Setting up a role for the Lambda function

In AWS, most things start out with no permissions at all to interact with other resources or services in your AWS account, unless you give it explicit permissions to do so.

This means that our Lambda function won’t be able to talk to services such as SES to send emails. Lambda uses something called a “role” to define the level of access it has to other services. So, in this section, we’ll set up a role for our function with access to SES and [CloudWatch](https://aws.amazon.com/cloudwatch/). CloudWatch is a service that stores logs and metrics, and Lambda uses it to store errors and execution logs for your functions.

To set up the role, go to the IAM (Identity and Access Management) section of the console, or use this [direct link](https://console.aws.amazon.com/iam/home), and click on“Roles” from the left. You’ll see a page like the one below:

![AWS IAM](https://www.freecodecamp.org/news/content/images/2020/03/AWS-IAM.png)

We’ll need to create a new role, so click on “Create role”. You’ll see a page with a list of AWS services. Since we’re setting this up for Lambda, select “Lambda” and click on the “Next: Permissions” button.

![AWS role trusted entity](https://www.freecodecamp.org/news/content/images/2020/03/AWS-role-trusted-entity.png)

Now, on the Permissions page, you’ll get an option to attach policies. First, we’ll grant “SES” permissions — and you can do this by searching for “SES” and selecting the “AmazonSESFullAccess” policy.

![AWS permission policies](https://www.freecodecamp.org/news/content/images/2020/03/AWS-permission-policies.png)

Similarly, you can grant CloudWatch access by searching for “CloudWatchFullAccess” and then selecting the policy that comes up:

![cloudwatch policy](https://www.freecodecamp.org/news/content/images/2020/03/cloudwatch-policy.png)

After selecting these policies, click on “Next: Tags” and then the “Next: Review” button. In the “Role name” text box, enter a role name of your choice, such as “ContactFormRole”. Then, click the “Create Role” button.

![AWS role](https://www.freecodecamp.org/news/content/images/2020/03/AWS-role.png)

Now, we have a role ready to use with our Lambda function.

## Creating the Lambda function

At this point, we can create the Lambda function that receives the details from API gateway, and sends us an email.

To create the function over to the Lambda section of the console, or use this [direct link](https://console.aws.amazon.com/lambda/home). Click on “Functions” from the left side. On this page, click the “Create function” button.

![create lambda function](https://www.freecodecamp.org/news/content/images/2020/03/create-lambda-function.png)

On the create function page, you’ll be asked for the function’s name and the language that you want to use. We’ll name our function “ContactFormFunction”, and we’ll use Python 3.8 as the language.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-1.png)

Next, we’ll attach the role that we created in the previous section. Click on the “Choose or create an execution role” below the “Permissions" section, and select “Use an existing role” and then select the role that we created earlier, “ContactFormRole”. Once you’ve entered the details, click on the “Create function” button.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-2.png)

This will take you to a page showing details about your function. Scroll down a bit so that you can see the code editor, which looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-3.png)

In the right pane, paste the following code and change `your_email_address_here` with your email address.

```python
import boto3
from base64 import b64decode
from urllib.parse import parse_qs

# Replace your email address here
send_to = 'your_email_address_here'

def lambda_handler(event, context):
    # We receive our data through POST requests. API gateway
    # sends the POST data as a Base64 encoded string in
    # event['body'], so we must decode it.
    data = parse_qs(b64decode(event['body']).decode())

    subject = 'You got a message from %s' % data['email'][0]
    text = '\n'.join([
        'Name: %s' % data['name'][0],
        'Email: %s' % data['email'][0],
        'Message %s' % data['message'][0]
    ])

    # Send an email through SES with the SendEmail API
    client = boto3.client('ses', region_name='us-east-1')
    client.send_email(
        Source=send_to,
        Destination={'ToAddresses': [send_to]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': text}}
        },
        ReplyToAddresses=[data['email'][0]]
    )

    # This is the response that'll be sent out through the
    # API gateway to the browser.
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': '"Success"' # jquery expects a JSON response
    }
```

Then, click on the “Save” button on the top right to save your code. With that out of the way, we’ll create an API gateway and map it with the Lambda function.

## Handling HTTP requests with API gateway

To add an API gateway and map it to your function, scroll up in the Lambda function page till you see the “Designer” section, and click on the “Add Trigger” button as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-4.png)

This will open the “Trigger” configuration page. Triggers are something that can invoke your Lambda function, and since we need an API gateway, choose it from the dropdown:

![lambda trigger](https://www.freecodecamp.org/news/content/images/2020/03/lambda-trigger.png)

This will bring up various options for setting up the API gateway. Ensure that you’ve set up “API” to “Create a new API” and “Choose a template” to “HTTP API”:

![API Gateway create API](https://www.freecodecamp.org/news/content/images/2020/03/api-gateway-create-api.png)

Scroll down below and click the “Add” function to set up the API gateway. This takes a few seconds to complete, and once it’s done, you’ll be taken to the designer view. Click on the “API gateway” button on the left to see the URL through which you can trigger the Lambda function:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-5.png)

Now, before we build the contact form page, we’ll test that our setup so far works correctly. If you’re on MacOS, Linux, or a recent version of Windows 10, you can copy the API gateway URL shown above and run the following command in your terminal. Make sure to replace `your_api_gateway_url` with the actual URL!

```
curl -i your_api_gateway_url --data-urlencode "name=John" --data-urlencode "email=john@example.com" --data-urlencode "message=hi there"
```

If all went well, you can see a 200 OK response with a “Success” message, like so:

![curl request](https://www.freecodecamp.org/news/content/images/2020/03/curl-request.png)

You should also receive an email in your inbox titled “You got a message from john@example.com” with the details that were entered in the form.

However, this can sometimes be finicky. The email might get delivered in your spam folder, or sometimes even get rejected without you ever seeing that email. This is because providers such as Gmail and Yahoo block third parties (such as SES) from sending emails using their domain name.

If you have your own domain name, you can work around this by setting up a [SPF record](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-authentication-spf.html). However, we won’t discuss that in this guide, as we want you to be able to follow even without a domain.

Next, we’ll complete this guide by building the contact form page.

## Building the contact form

Open your favorite text editor and save the following code as a HTML file. Remember to replace `your_api_gateway_url`  with the full URL that you obtained previously.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Contact form</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <style>
    body {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Contact form</h2>
    <hr>
    <form id="form">
      <div class="form-group">
        <label for="name">Your name</label>
        <input type="text" class="form-control" id="name" placeholder="Your name">
      </div>
      <div class="form-group">
        <label for="email">Your email address</label>
        <input type="email" class="form-control" id="email" placeholder="Your email address">
      </div>
      <div class="form-group">
        <label for="message">Your message</label>
        <textarea class="form-control" id="message" rows="3"></textarea>
      </div>
      <div id="alert" class="alert d-none">
      </div>
      <button type="submit" class="btn btn-primary">
        Submit
      </button>
    </form>
  </div>
  <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
  <script>
    function showMessage(msg, type) {
      $('#alert').attr('class', `alert alert-${type}`).text(msg)
    }

    function hideMessage(msg) {
      $('#alert').attr('class', 'd-none')
    }

    $('#form').submit(event => {
      event.preventDefault()
      hideMessage()

      let name = $('#name').val().trim()
      let email = $('#email').val().trim()
      let message = $('#message').val().trim()

      if (!(name && email && message)) {
        showMessage('You must fill in all the fields before submitting the form', 'danger')
        return
      }

      $.post('your_api_gateway_url', {name, email, message}).done(_ => {
        showMessage("Thanks for contacting us. We'll be in touch shortly.", 'success')
      }).fail(_ => {
        showMessage('Something went wrong when submiting the message', 'danger')
      })
    })
  </script>
</body>
</html>
```

Once you’ve saved the file, open it in your browser, fill in the details and click “Submit”. You’ll be able to see a success message, like so:

![contact form](https://www.freecodecamp.org/news/content/images/2020/03/contact-form.png)

Clicking the button submits the details as a POST request to the API gateway, which then triggers the Lambda function, which in turn sends us an email over SES. However, as we discussed in the previous section (“Handling HTTP requests with API gateway”), you might not end up receiving an email in certain circumstances.

Now that we have a contact form that moves most of its logic over to serverless, you have this static web page that you need to host somewhere. 

So, do you need a server to host this page? Not at all! AWS offers a storage service named S3 (Simple Storage Service), and you can use it to host static websites. This does require a domain name, so if you own one, you can use [this article](https://medium.com/@kyle.galbraith/how-to-host-a-website-on-s3-without-getting-lost-in-the-sea-e2b82aa6cd38) to host the web page.

## Where to go next?

Now that we’ve built a simple contact form using serverless, how do you build large applications? Clicking around various options in the console is a good way to learn AWS and serverless, but it’s not an option when you’re trying to build something big with lots of moving parts.

Fortunately, there are various tools that can help you build and deploy serverless apps on AWS, such as the [Serverless framework](https://serverless.com/) or [AWS Chalice](https://chalice.readthedocs.io/en/latest/). [CloudFormation](https://aws.amazon.com/cloudformation/), a free AWS service, can also help you build apps by automating the deployment process through templates written in JSON or YAML, though it’s a bit difficult to use than the other options.

