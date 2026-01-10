---
title: How to Set Up AWS Simple Email Service
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2023-03-27T15:44:03.000Z'
originalURL: https://freecodecamp.org/news/set-up-aws-simple-email-service
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Blog-Banner---Template--3-.png
tags:
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: email
  slug: email
seo_title: null
seo_desc: "If you're looking for a reliable and cost-effective way to send emails,\
  \ AWS Simple Email Service (SES) is a great option. It's a cloud-based email platform\
  \ that helps you send and receive emails quickly and easily. \nWith SES, you don't\
  \ have to worry ..."
---

If you're looking for a reliable and cost-effective way to send emails, AWS Simple Email Service (SES) is a great option. It's a cloud-based email platform that helps you send and receive emails quickly and easily. 

With SES, you don't have to worry about managing your mail server, and you can benefit from the scalability and reliability of Amazon's cloud infrastructure. 

There are a few steps to setting up SES, such as verifying your domain, verifying your email address, and setting up MX records. This short guide will walk you through each step to get your SES up and running in no time.  
  
**Prerequisites:** This tutorial will be a hands-on demonstration. To follow along, be sure you have an active [AWS account](https://aws.amazon.com/free/).

## How to Configure AWS SES

### Step 1 – Verify Identities

First, login into your AWS Management Console account and search for Simple Email Service. Select the **Amazon Simple Email Service.**

![Image](https://i.imgur.com/8ZjaAKn.png)
_Searching for AWS SES_

This will lead you to an SES Console.

To start sending emails, you'll need to create an identity. This involves verifying the email address you would use to send emails. If you do not verify the email address, you can't use the email to perform any action on SES. 

Note you can add a domain as an identity, but we'll use an email address for this guide. Click **Create identity** to verify an email address.

![Image](https://i.imgur.com/8xrgwvL.png)
_Creating an Identity_

Next, select the **Email address** option and enter the email address you wish to use.

In Amazon SES, you can use a domain, subdomain, or email address as a _verified_ identity. You may use whatever suits you best.

![Image](https://i.imgur.com/apfMPNY.png)
_Verifying an Identity_

We use tags to manage identities on Amazon SES. We'll skip this here, but if you wish, you can define a tag. Once you're done, click **Create identity** to create an identity for your SES account.

![Image](https://i.imgur.com/8e6swKE.png)
_Creating an Identity for Amazon SES_

Now, an email will be sent to the email address you used to create the identity. Click the link in the email to verify your email.

![Image](https://paper-attachments.dropboxusercontent.com/s_8C16BB81FDF5129198CC129A07A220ADD326C1D4AD8E16A42ED5864426B31F5B_1670344969240_6DeFvpt.png)
_Verifying your email address_

Once you've done that, you will see your email address on your SES account's list of verified identities.

![Image](https://i.imgur.com/22Q4jrr.png)
_List of verified identities_

## How to Create SMTP Credentials

A Simple Mail Transfer Protocol (SMTP) sends and receives messages through a mail server. In this section, you will learn how to create credentials that grant you access to the SES mail server to send and receive mail. 

First, log in to your [Amazon SES dashboard](https://us-east-1.console.aws.amazon.com/ses/home?region=us-east-1#/account). Click on **SMTP settings.**

![Image](https://i.imgur.com/1LsYmUe.png)
_Amazon SES Dashboard_

Then click on **Create SMTP** **credentials** to create login details to your SMTP account under Amazon SES.

![Image](https://i.imgur.com/M4e6D2p.png)
_Creating SMTP Credentials_

You can choose to define an IAM username or use the default. Once you've done that, click **Create**.

![Image](https://i.imgur.com/pI1OI2R.png)
_Creating IAM user for SMTP_

Once you create an IAM user, your SMTP details will be displayed alongside your IAM username.

A notification telling you your user has been created will be displayed at the top. Make sure you download the credentials since it is a One-Time display detail. You can download them by clicking on **Download Credentials**.

![Image](https://i.imgur.com/uc8Pxta.png)
_Created SMTP Credentials_

  
Great! You have access to AWS Simple Email Service SMTP credentials. You can use the credentials to connect your backend to the Amazon SES server to send emails. 

# Conclusion

Amazon Simple Email Service (SES) is a powerful and reliable tool for quickly sending marketing, notification, and transactional emails. Setting up Amazon SES is straightforward and you can do it in just a few simple steps. 

After signing up for an AWS account and accessing the Amazon SES console, you can verify and set a default email address and start sending emails using the service. 

With Amazon SES, you can enjoy the benefits of cloud-based email sending, including improved deliverability, scalability, and security.

