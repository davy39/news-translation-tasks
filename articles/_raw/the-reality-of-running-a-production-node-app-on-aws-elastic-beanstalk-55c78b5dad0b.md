---
title: The reality of running a production Node app on AWS Elastic Beanstalk
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-21T16:08:21.000Z'
originalURL: https://freecodecamp.org/news/the-reality-of-running-a-production-node-app-on-aws-elastic-beanstalk-55c78b5dad0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sUif8A5X81bOpkLssOTbcg.jpeg
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Jared Nutt

  Lessons learned from 2 years of running a production Node app on AWS’ ELB platform


  _Photo by [Unsplash](https://unsplash.com/photos/1ZZ96uESRJQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="...'
---

By Jared Nutt

#### Lessons learned from 2 years of running a production Node app on AWS’ ELB platform

![Image](https://cdn-media-1.freecodecamp.org/images/6DRA1yuoVD7jj2JoXxmeLHLuf2atDKrotLtz)
_Photo by [Unsplash](https://unsplash.com/photos/1ZZ96uESRJQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Shane Rounce</a> on <a href="https://unsplash.com/search/photos/technology?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Front-Matter

Let’s be honest, the [AWS pricing calculator](https://calculator.s3.amazonaws.com/index.html) is confusing. Part of that is because of the _a la carte_ method of payments AWS offers. This makes trying to give a good quote to a client difficult. Hopefully this article can provide some light on how much it costs to run an app, as well as some ways to reduce cost.

### The Real Cost of Running an App

I’ve been managing a node web-app on ELB for about two years now. The first year was great, they gave you everything for free (mostly)! After that, you have to start paying for stuff, like EC2 instances.

This article will focus on my specific app requirements, which is a node based express app that is hosted on Elastic Beanstalk.

For full details about the build, see my previous article [here](https://medium.freecodecamp.org/how-to-deploy-a-node-js-app-to-the-aws-elastic-beanstalk-f150899ed977).

#### Breakdown

This is what I’m currently running on AWS:

Single EBS Environment (U.S. West Region):

* 1 Classic Load Balancer
* 1 t2.micro EC2 instance
* S3 Bucket that holds images (7 GB at time of writing)
* 1 Route 53 Hosted Zone

**$18** (Load Balancer) + **$5** (EC2 with an RI) + **$0.50** (Route 53) + **$0.17** (S3) + **$0.21** (Data Transfer) = Roughly **$25** a month.

Additionally, I host a MongoDB elsewhere, so if you plan on hosting a DB on AWS, that will incur additional costs. Let’s break down the various costs.

#### Load Balancer

This is the most expensive part of the stack. It costs:

* $0.025 per Classic Load Balancer-hour (or partial hour)
* $0.008 per GB of data processed by a Classic Load Balancer

That means, if you run your app 24 hours a day, it will cost roughly $18 + data charges, every month.

#### EC2 Instance

On-Demand EC2 instances are more expensive than they should be. To save some money here, refer to the section below about Reserved EC2 Instances. In case you were wondering, it would cost $8.40 to run the same type of EC2 instance as mentioned above, on-demand.

#### S3

I have a couple S3 buckets. One for my static home page, one for holding images and one for holding the application version. As far as I know, ELB automatically creates the one for managing the application versions.

The S3 is pretty cheap, so I’m not too worried about trying to nickel and dime it, but there are ways to save money via their [Glacier](https://aws.amazon.com/glacier/) system.

#### Database

I host my MongoDB DB at mLab, which is going away soon. So I’ll update this when I sort out how much that is actually gonna cost once I’m forced to move over to Mongo’s Atlas.

### Reserved EC2 Instances

Let’s talk about Reserved Instances (RI). Amazon’s convoluted billing system is the most confusing part about managing anything on AWS. Reserved Instances can alleviate some of the cost, but are way too confusing.

After a lot of reading and talking with the AWS customer service, this is what I sorta figured out.

First, there are two different ways you can reserve where the RI is: Regional and Availability Zone. Regional means, it is specific to one of the main regions, eg. us-west-2 (Oregon). The availability zone (AZ) is specific to a zone within that region, e.g. us-west-2**a** (Oregon).

I bought an RI within us-west-2 and it was automatically applied to my instance running in that area. If you buy one within the AZ, it will only apply to the specific AZ, e.g. us-west-2a, so if ELB spins up an EC2 instance in us-west2b, you’re out of luck.

Additionally, there are “standard” and “convertible” types of RIs. I’m not 100% on what that means, but from what I understand convertible is more flexible on what you can swap it to, but more expensive.

Finally, there are three types of payment types: No Up-front, partial Up-front, All Up-Front. This is pretty straightforward, you either pay nothing, some or all when you reserve the instance. There is no cost benefit, that I can see. However, as a new account, you most likely can’t do no up-front.

Per AWS Support:

> No Upfront Reserved Instances (RIs) can pose a significant billing risk to new accounts, as they’re a contractual obligation to pay monthly for the entire term of the RI. For this reason, new accounts and lightly used accounts are unable to sign up for No Upfront RIs until a successful billing history is built with us.

You may run into this error if you try and buy a no up-front.

> Error : Your current quota does not allow you to purchase the required number of reserved instances (Service: AmazonEC2; Status Code: 400; Error Code: ReservedInstancesLimitExceeded;)

Caveat: For whatever reason, it takes a bit for the the reserved instance to “kick-in” which means the first day of the month always costs more. I’m not sure why this is, but if I figure it out, I’ll update this. See graph below:

![Image](https://cdn-media-1.freecodecamp.org/images/JNI-ha2AnV7fhXmn8AbusMNAY33UW6mug6lW)

### Pain Points

These are just some minor complaints about the overall EBS, which I figured I’d include as an addendum to my original article, in case you’re curious.

#### Automatic updates aren’t really that automatic

Node versions don’t line up from version to version.

Refer to the step below on how I manage changing Linux versions when Node doesn’t work.

#### Running more than one environment

Having a development environment and a production running at the same time is easy, but it’s expensive. It doubles it, in fact. Therefore, I usually destroy the dev environment as soon as I’m done with it.

#### Documentation is horrendous

AWS is too big for its own good. That is part of why I’m writing this. It was really hard to find answers to my specific needs.

### How I manage Updates

I have two separate instances of my Git repo installed on my laptop. I have one for dev, and one for production.

I use the dev environment to, well, develop! Pretty straightforward. I use the production folder solely for the purpose of pulling updates from Git master branch, running my webpack configuration and deploying to the production server.

The reason they are separate is because I can maintain separate elastic beanstalk configurations and not have to worry about deploying to the wrong place.

#### Updates not requiring a Linux Environment change

For updates not requiring any changes to the linux environment, it’s as simple as running `eb deploy` in the terminal. It’s amazing and takes about 10 minutes to propagate.

#### Updates requiring a Linux Environment change

Occasionally, you will want to update the Linux environment but will be unable too because AWS is freaking dumb (I’m sure there’s a reason) and only allows certain versions of Node on each Linux build. For this, it’s a bit more complicated, but manageable.

1. Push to production config under new env. The last time I did this, I just created a new instance via `eb create prod-1` . It’ll do what it needs to and deploy your app to a new environment.
2. Make sure all your updates work. Seems pretty obvious, but this is a good time to make sure there weren’t any hiccups with the new build.
3. Make sure your env vars are setup correctly. This is sorta part of the previous version, but make sure you’re pulling from the right DB, or whatever.
4. Make sure your load balancer has the same SSL cert (if applicable). Fun fact, if you try to access an ELB instance in https without a certificate, it will fail!
5. Swap the instances. Finally, after everything looks good to go, there’s a button in the console to swap the instance urls. EASY PEASY. You don’t have to change anything in the Route 53, it does it all for you.

So, there you have it. How to manage your updates. Pretty easy.

### Final Thoughts

If you have any suggestions to make it cheaper/easier, I would love to hear them. I like the discussion about tools and options just as much as the next developer!

With that, I’ll leave with this: Happy coding!

