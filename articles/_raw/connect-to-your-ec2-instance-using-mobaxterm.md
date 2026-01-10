---
title: How to Connect to Your EC2 Instance Using MobaXterm with SSH and a Keypair
  (.pem) File
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-10-22T10:54:33.284Z'
originalURL: https://freecodecamp.org/news/connect-to-your-ec2-instance-using-mobaxterm
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729574902773/f80eb07d-524a-4fa2-a8d8-29c6438d37aa.png
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
seo_title: null
seo_desc: In this article, I’ll walk you through the steps of connecting to your EC2
  instance using MobaXterm with a .pem keypair file. Whether you're a beginner dipping
  your toes into the cloud or an experienced user looking for a quicker method, I’ve
  got you...
---

In this article, I’ll walk you through the steps of connecting to your EC2 instance using MobaXterm with a `.pem` keypair file. Whether you're a beginner dipping your toes into the cloud or an experienced user looking for a quicker method, I’ve got you covered. So, let’s dive in!

## **Table of Contents**

* [Why MobaXterm?](#heading-why-mobaxterm)
    
* [Step 1: Install MobaXterm](#heading-step-1-install-mobaxterm)
    
* [Step 2: Get Your EC2 Instance Public IP and Key Pair](#heading-step-2-get-your-ec2-instance-public-ip-and-key-pair)
    
* [Step 3: Open MobaXterm and Start a New SSH Session](#heading-step-3-open-mobaxterm-and-start-a-new-ssh-session)
    
* [Step 4: Enter SSH Session Details](#heading-step-4-enter-ssh-session-details)
    
* [Step 5: Attach Your .pem Key Pair](#heading-step-5-attach-your-pem-key-pair)
    
* [Step 6: Connect to Your EC2 Instance](#heading-step-6-connect-to-your-ec2-instance)
    
* [Step 7: Troubleshooting Common Issues](#heading-step-7-troubleshooting-common-issues)
    
* [Wrapping Up](#heading-wrapping-up)
    

## Why MobaXterm?

You may be wondering why we’re using MobaXterm over other SSH tools. Well, for starters, it’s super beginner-friendly, and it combines a bunch of powerful tools in one. You can use it to transfer files, run scripts, or even open multiple sessions simultaneously.

Plus, it’s like the Swiss Army knife for remote connections. Whether you’re working with AWS, Google Cloud, or even a Raspberry Pi at home, MobaXterm can do it all.

## Step 1: Install MobaXterm

If you’re not already familiar with MobaXterm, it’s basically used for all things remote access. You can download it [here](https://mobaxterm.mobatek.net/download-home-edition.html) for free. Installation is super easy – just download, click, and install.

Once you have it set up, fire up MobaXterm and get ready for the fun part.

## Step 2: Get Your EC2 Instance Public IP and Key Pair

Before we continue, there are two key pieces of information you’ll need:

**Public IP Address**: This is the unique address AWS assigns to your EC2 instance. To find it, go to the **EC2 Dashboard** in AWS, select your running instance, and grab the **Public IPv4 Address** (it looks like `13.123.45.67`).

**Your .pem File**: This is the private key file you downloaded when you created your EC2 instance. If you didn’t save it, you may have to create a new key pair because AWS only lets you download it once. (No pressure – just don’t lose it this time!)

## Step 3: Open MobaXterm and Start a New SSH Session

Time to work some magic with MobaXterm! Open the app, and you’ll see an intuitive interface. Don’t let all the buttons scare you, just focus on the top left where it says **Session**.

![MobaXterm user interface](https://cdn.hashnode.com/res/hashnode/image/upload/v1729567478544/cf69a56b-9d1e-4de3-b6d8-224634b55ae3.png align="center")

Here’s what to do next:

* Click **Session** (you’ll feel powerful just pressing that button).
    
* In the new window, select **SSH** as the session type.
    

![MobaXterm Session setting tab](https://cdn.hashnode.com/res/hashnode/image/upload/v1729567593446/ee8f369d-24be-419d-971f-30e3e4355dd6.png align="center")

## Step 4: Enter SSH Session Details

It’s time to fill in the details that’ll connect MobaXterm to your EC2 instance. Here’s what you need to know:

* **Remote Host**: Enter the **Public IP Address** of your EC2 instance here. Remember, you grabbed that from the EC2 Dashboard earlier.
    
* **Username**: If you’re using Amazon Linux, your default username is `ec2-user`. If you’re on Ubuntu, it’s `ubuntu`.
    

## Step 5: Attach Your .pem Key Pair

MobaXterm makes it super easy to use your `.pem` key file for authentication (no converting to `.ppk` necessary, like you’d have to with other tools).

Here’s how to attach your `.pem` file:

* Head over to the **Advanced SSH Settings** tab.
    
* Check the **Use private key** option.
    
* Click **Browse** and find your `.pem` file on your computer.
    
* Select the file and hit **OK**.
    

It’s like giving MobaXterm the secret key to unlock your EC2 instance.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1729567798203/535c226e-fbd2-43fc-b1af-a48ce171b974.png align="center")

## Step 6: Connect to Your EC2 Instance

Now that you’ve filled in all the details, click **OK** to start your session. If everything’s been set up correctly, you should see a terminal pop up, and MobaXterm will work its magic to connect you to your EC2 instance.

🎉 And just like that, you’re in! You should see a terminal window connected to your instance, and now you can start typing commands like a pro.

## Step 7: Troubleshooting Common Issues

We all know that tech doesn’t always behave. Here are some common problems you might run into—and how to solve them:

* **Connection Timed Out**: This could be due to your instance’s security group settings. Make sure your EC2 security group allows inbound traffic on **port 22** (the SSH port) from your IP address.
    
* **Authentication Failed**: Ensure you’re using the correct username (`ec2-user` for Amazon Linux, `ubuntu` for Ubuntu).
    

## Wrapping Up

And there you have it! Connecting to your EC2 instance using MobaXterm with your `.pem` keypair is as simple as following these steps. It’s not rocket science—but it kind of feels like it, doesn’t it? Now that you’ve got your EC2 instance up and running, the sky’s the limit.

So, go on, take what you've learned here, explore, experiment, and, most importantly, have fun with it! Until next time, happy cloud computing! ☁️

You can follow me on

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
