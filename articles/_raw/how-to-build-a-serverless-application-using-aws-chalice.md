---
title: How to Build a Serverless Application Using AWS Chalice
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-14T21:50:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-chalice
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cloud-computing--1--1.png
tags:
- name: AWS
  slug: aws
- name: Python
  slug: python
- name: serverless
  slug: serverless
seo_title: null
seo_desc: "By Siben Nayak\nI recently came across AWS Chalice and was fascinated by\
  \ the simplicity and usability it offers. \nAWS Chalice is a serverless framework\
  \ that allows you to build serverless applications using Python, and deploy them\
  \ on AWS using Amazon ..."
---

By Siben Nayak

I recently came across AWS Chalice and was fascinated by the simplicity and usability it offers. 

AWS Chalice is a serverless framework that allows you to build serverless applications using Python, and deploy them on AWS using Amazon API Gateway and AWS Lambda.

I decided to play around with it and was actually able to create and deploy a sample REST API on AWS within a few minutes. 

In this article, I will walk you through the steps required to build and deploy a serverless application that gets the latest news from Google News using Chalice.

## Prerequisites

This tutorial requires an AWS account. If you don’t have one already, go ahead and [create one](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). Our application is going to use only the free-tier resources, so cost shouldn’t be an issue. 

You also need to configure security and create users and roles for your access.

## How to Configure AWS Credentials

Chalice uses the AWS Command Line Interface (CLI) behind the scenes to deploy the project. If you haven’t used AWS's CLI before to work with AWS resources, you can install it by following the guidelines [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

Once installed, you need to [configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) your AWS CLI to use the credentials from your AWS account. 

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-31.png)

## How to Install Chalice

Next, you need to install Chalice. We will be using Python 3 in this tutorial, but you can use any version of Python supported by AWS Lambda.

### Verify Python Installation

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-32.png)

### Install Chalice

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-33.png)

### Verify Chalice Installation

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-34.png)

## How to Create a Project

Next, run the `chalice new-project` command to create a new project.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-35.png)

This will create a `daily-news` folder in your current directory. You can see that Chalice has created several files in this folder. We'll be working with the `app.py` and `requirements.txt` files only in this article.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-37.png)

Let’s take a look at the contents of `app.py` file:

<script src="https://gist.github.com/theawesomenayak/20986881b7ca3c6e9b48a1ec7ce66d2c.js"></script>

The `new-project` command created a sample app `daily-news`. It defines a single view `/`, that returns the JSON body `{"hello": "world"}` when called. You can now modify this template and add more code to read news from Google.

We will be using Google’s RSS feed to get our news. Since RSS feeds consist of data in XML format, we will need a Python library called Beautiful Soup for parsing the XML data. 

You can install Beautiful Soup and its XML parsing library using `pip`, like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-36.png)

Next add the following imports to `app.py`. This essentially adds imports from `urllib` to make HTTP calls and `bs4` to parse XML.

<script src="https://gist.github.com/theawesomenayak/1370454bb17aa7c052af901f73010813.js"></script>

Next, you need to add a method to fetch the RSS feed from Google. We will use `urllib` to make an HTTP call to Google's RSS endpoint and get the response. You can then parse the response to extract the news title and publication date, and create a list of news items. 

To do this, add the following code to your `app.py`:

<script src="https://gist.github.com/theawesomenayak/a9a5c9c3b812c3a7f96651dd67b240c8.js"></script>

Update the index method in `app.py` to invoke this method and return the list of news items as a result.

<script src="https://gist.github.com/theawesomenayak/195fff0f32991521ef0c7e34a23a4b47.js"></script>

Note that you installed a few dependencies to make the code work. These dependencies were installed locally, and will not be available to the AWS Lambda container at runtime. 

To make them available to AWS Lambda, you will need to package them along with your code. 

To do that, add the following to the `requirements.txt` file. Chalice packs these dependencies as part of your code during build and uploads them as part of the Lambda function.

<script src="https://gist.github.com/theawesomenayak/570c0eca944ef5eb23c5b4d40b7a80ca.js"></script>

## How to Deploy the Project

Let’s deploy this app. From the `daily-news` folder, run the `chalice deploy` command.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-38.png)

This deploys your API on Amazon API Gateway and creates a new function on AWS Lambda.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-11-at-12.51.29-PM.png)
_daily-news API_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-11-at-12.59.13-PM.png)
_daily-news-dev Lambda Function_

Let's try accessing the API now. You can use `curl` to invoke the API Gateway URL that you received during `chalice deploy`. The response of the API call would return a list of news items as shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-41.png)

## How to Clean Up Resources

You can also use the `chalice delete` command to delete all the resources created when you ran the `chalice deploy` command.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-42.png)

## Conclusion

Congratulations! You just deployed a serverless application on AWS using Chalice. It wasn’t too hard, was it?

You can now go ahead and make any modifications to your `app.py` file and rerun `chalice deploy` to redeploy your changes.

You can also use Chalice to integrate your serverless app with Amazon S3, Amazon SNS, Amazon SQS, and other AWS services. Take a look at the [tutorials](https://aws.github.io/chalice/tutorials/index.html) and keep exploring. The full source code for this tutorial can be found [here](https://github.com/theawesomenayak/daily-news).

Thank you for staying with me so far. Hope you liked the article. You can connect with me on [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) where I regularly discuss technology and life. Also take a look at some of my other articles on [Medium](https://medium.com/@theawesomenayak). Happy reading ? 

