---
title: Here are three common ways to create your Lambda functions with AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T09:04:40.000Z'
originalURL: https://freecodecamp.org/news/aws-lambda-offering-developers-ultimate-flexibility-d8939ff4220
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JuAJNrCky6mkF4upt0emCg.png
tags:
- name: automation
  slug: automation
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sam Williams

  AWS Lambda functions are incredible! They’re functions that are hosted on Amazon
  Web Services that can be triggered in many different ways.

  One of the best parts is that you only pay for the time the Lambda function is running.
  Got so...'
---

By Sam Williams

AWS Lambda functions are incredible! They’re functions that are hosted on Amazon Web Services that can be triggered in many different ways.

One of the best parts is that you only pay for the time the Lambda function is running. Got something that only runs once an hour and only takes 2 seconds? You’ll only be charged for 48 seconds a day! That’s insane compared to running a 24/7 AWS EC2 instance or your own private server.

Today we’ll create a Lambda function and look at the three best ways to work with the code.

### Creating a Lambda Function

Once you’ve got your AWS account set up, there are a few ways to create a new Lambda function. We’re going to be using the AWS Console.

#### AWS Console

Within the AWS Console, you can find AWS Lambda under Services which takes you to the Lambda console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*23UBDu9eiNn9CasvX9dUqg.png)

This is what you’ll see if this is your first Lambda. Click that **Create a function** button to start setting up your first function.

You’ll end up on the setup page where you configure some aspects of the function (name, runtime, role). You can create a Lambda from Blueprints or Serverless Application Repos but in this example, we’ll Author it from scratch.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmKCKMsIPuMLhgsMxNMBog.png)

Enter the name for your function (this must be unique to your user or sub-account), choose your Runtime (We’ll use Node.js 8.10), and select a role.

You’ll have to create a new role if you don’t already have one. Create one from template and you can leave **Policy templates** blank.

### Writing Your Lambda Function Code

One of the big advantages with Lambdas is that you can choose how you write and edit them. There are three main ways to do so

* Lambda Console
* Cloud9
* On your local machine

I’m going to cover all three and discuss advantages and disadvantages for each of them.

### Method 1: Lambda Console

This is the screen you got sent to when you created the function. You’ll see that there is a lot of stuff going on. The bit that we care about for now is the **Function code** section, about half way down.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VxeSaa8uQgP92Wl4zCPMUg.png)

In here we have a basic editor. I believe it’s based on the Cloud 9 IDE and works pretty damn well for simple Lambda functions. You can see below that the handler is an async function because I chose to use Node 8.10. If you prefer callbacks then Node 6.10 is the runtime for you.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ukr1dY8xL4mT2IIEw0DVZg.png)

#### **The advantages**

* It’s a decent editor.
* You can access it from any computer through your AWS console.

#### **The Disadvantages**

* It doesn’t seem to be 100% stable. Sometimes it doesn’t let you save so you have to copy all of your work to a local file, reload the page, and copy your work back. I hope that this gets fixed soon!
* It doesn’t have a terminal. This means that you can’t install packages using NPM using this method alone.

### Method 2: Cloud9 Editor

Amazon recently acquired Cloud9, an online development platform. It seems to run a very basic version of Ubuntu that is integrated with the rest of the AWS platform.

Search for **Cloud9** in the AWS console, go to the page and select **Create environment**_._ From here you give your environment a name and go to the next step.

Here you get to choose what you want to run this environment on. The great thing is that t2.micro is Free-tier eligible so you can use this method without getting charged anything if you’re on the free tier. I’ve never needed anything more powerful than a t2.micro.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mIMSy6hKCQuer20ZOTjVSQ.png)

Continue on from here and you’ll end up in your new Cloud9 environment!

![Image](https://cdn-media-1.freecodecamp.org/images/1*uaTpBEey0EHYd-_aWa165g.png)

The cool thing about this is that you have access to all of your Lambda functions from inside your Cloud9 environment. Click **AWS Resources** and under **Remote Functions** you’ll find all of your functions. Click on the Lambda function you want to edit and then hit the download icon above to import it into your environment.

Once that’s done, it’ll just be like you’re working on it locally.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P2Y6g3Juw5T7lltbooxhbg.png)

Once you’re finished, just select the function you’ve been working on from the local list and hit the upload button. Within a few seconds it’ll be live with all your changes.

#### **The Advantages**

* Again, this is all remote so you don’t need to worry about forgetting to commit your work or save it to a memory stick if you work on multiple machines.
* Getting your functions and uploading them is super easy. This is by far the best bit about this method.
* You now have an integrated terminal, allowing you to install npm packages and do everything else you want to do using the terminal.

#### **The Disadvantages**

* It still has the same stability issues that the Lambda editor has. I’ve had multiple occasions where I’ve tried to save the function but couldn’t, having to copy to local, refresh, and recopy to Cloud 9. After a few times, I gave up and moved to local editing.

### Method 3: Local Editing

I’m going to do this one a bit differently, I’ll list the advantages and disadvantages then show you how to make it so much better.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XMS7swq0ptF24er7L0fgmg.png)

#### **The Advantages**

* Local editing is how most developers will work. We can use our favourite IDE, extensions, and colour schemes.
* It’s stable (as long as your computer is).

#### **The Disadvantages**

* There’s no fancy button to get and upload your work to AWS.
* Your work is local, so having multiple users or just working on multiple devices is more complex.

#### Local Editing Tricks

Because the advantages for this method are so appealing (or the disadvantages of other methods are so appalling), we’re going to utilise some basic workarounds. It should take about 15 minutes to set up everything we need!

#### AWS CLI

To upload our work to AWS we can use the AWS CLI. This allows us to upload a zip file to our AWS account that populates a given Lambda.

To do this, we first need to setup AWS CLI. You can install it using [this tutorial](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) or by typing `npm install -g aws-cli` into your terminal. Now we need to set up a user for our CLI to log in as.

In IAM Management, click **Add User**_,_ give the user a name and select **Programmatic Access**_._ This will allow us to act as the user remotely.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LkB76XZZwPt6soPHPtWlCQ.png)

In the permissions screen, choose to **Attach existing policies directly** and select **AdministatorAccess**_._ This will let you do whatever you want through your CLI. You can set stricter policies on this user if you want, or if this is for another person to access.

There’s another screen before you end up being shown your access keys. Copy your access keys and open a terminal. Run the command `aws configure` which will ask you for 4 things.

```
AWS Access Key ID [None]: "Your Access Key ID"AWS Secret Access Key [None]: "Your Secret Access Key"Default region name [eu-west-1]:Default output format [json]:
```

The first two are found on the last page of the user creation and the next two can be left as default or changed to whatever you want.

#### Using the AWS CLI

Now that we’ve got the CLI set up, we can use it to make our lives so much easier. If you have a folder with a Lambda function stored in there, we can run a few simple commands to upload it to AWS.

```
cd MyLambdaFunctionrm index.zipzip –X –r ./index.zip *aws lambda update-function-code     --function-name MyLambdaFunction     --zip-file fileb://index.zipcd ..
```

#### AWS CLI Build Script

This is great, but typing this all out every time you want to upload a new Lambda version would become tiresome. So we’re going to use a build script.

For this exact script to work, you need to have a folder structure like this. Each lambda has a folder with the relevant files and a region.txt file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XEed7aP1zbg6CyB3B8maWA.png)

This script not only runs the basic AWS CLI commands, but it also does extra checks, runs `npm install` , and echos out details about the progress.

This may look like a complex script, but it can be easy broken down. The first 32 lines move into the folder of the Lambda function, run `npm install` and check that AWS CLI is installed. Line 38 zips the folder, except for certain files, and line 42 uploads the zip file.

Now all you need to do is to navigate to the main folder wher the Lambdas function resides and run

```
./build.sh example-lambda
```

This script could be modified and expanded to include region-specific uploading, batch uploading multiple Lambda functions or Git integration.

#### Git

Most people reading this will use Git on a daily basis. There’s a reason for that: it makes life simpler.

Having a Git repository for all of your Lambda functions is a great way to work with teams of developers or by yourself on multiple machines.

### Summary

There are three common ways to edit Lambda functions: in the Lambda console, Cloud 9, and locally.

There are advantages and disadvantages of all three methods, but personally I think the best choice is to write the function locally and deploy it using a deployment script.

If you found this article useful then give it some claps and follow me for more AWS tutorials and developer articles!

NEXT → [Say Hello to Your Own Amazon Lex Chat Bot](https://tutorials.botsfloor.com/say-hello-to-your-own-amazon-lex-chat-bot-9f22e7a0f9b0)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-leQk1ik68WjLB__Vc9IXw.gif)

