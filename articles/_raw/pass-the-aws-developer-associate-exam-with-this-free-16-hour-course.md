---
title: Pass the AWS Developer Associate Exam With This Free 16-Hour Course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-06T06:40:38.000Z'
originalURL: https://freecodecamp.org/news/pass-the-aws-developer-associate-exam-with-this-free-16-hour-course
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/RrKRN9zRBWshd.jpg
tags:
- name: AWS
  slug: aws
- name: 'AWSCertified  '
  slug: awscertified
- name: Certification
  slug: certification
seo_title: null
seo_desc: 'By Andrew Brown

  As promised, here is the 3rd free ExamPro AWS Certification course. This course
  prepares you to earn the coveted AWS Developer Associate Certification.

  And yes – you read all that correctly. This is a full 16-hour video course – avail...'
---

By Andrew Brown

As promised, here is the 3rd free ExamPro AWS Certification course. This course prepares you to earn the coveted AWS Developer Associate Certification.

And yes – you read all that correctly. This is a full 16-hour video course – available for free on freeCodeCamp's YouTube channel.

We now have free courses for **3 out of the 12** AWS Certifications:

1. ? [AWS Certified Cloud Practitioner](https://www.freecodecamp.org/news/aws-certified-cloud-practitioner-training-2019-free-video-course/)
2. ? [AWS Solutions Architect Associate](https://www.freecodecamp.org/news/pass-the-aws-certified-solutions-architect-exam-with-this-free-10-hour-course/)
3. ? AWS Developer Associate (the full course link is at the bottom of this article – but I hope you'll read this article first ?)
4. AWS SysOps Administrator Associate (coming soon)
5. AWS Solutions Architect Professional (coming soon)
6. AWS DevOps Engineer Professional (coming soon)
7. AWS Machine Learning Speciality (coming soon)
8. AWS Security Speciality (coming soon)
9. AWS Advanced Networking Speciality (coming soon)
10. AWS Alexa Skill Builder Specialty (coming soon)
11. AWS Data Analytics Specialty (coming soon)
12. AWS Databases Specialty (coming soon)

## What Is The AWS Developer Associate Certification?

Amazon Web Services (AWS) has 3 Associate Certifications:

1. Solutions Architect (most popular)
2. SysOps Administrator (most technical)
3. Developer (most practical)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS_Certification_-_Validate_AWS_Cloud_Skills_-_Get_AWS_Certified-1.jpg)
_A chart of 11 of the AWS certifications, showing which ones we're currently working on courses for._

The AWS Developer Associate is widely considered the most difficult associate certification. This is because the exam questions are based on practical knowledge of implementing, deploying, and securing web applications.

Along the way, you’ll gain practical developer knowledge for the 3 most common cloud architectures:

* Traditional (Virtual Machines)
* Containers / Microservices (Docker)
* Serverless (AWS Lambda)

I always say: if you don’t know which AWS Certification to take, you should go for the AWS Solutions Architect Associate. It's so broad in scope that it offers the largest amount of cloud roles available to you.

But if you want the highest chance of getting a job, the AWS Developer Associate is the objectively best certification. It proves you have hands-on knowledge, which helps reassure employers you're ready to work on the cloud.

## Who Is The AWS Developer Associate For?

The AWS Developer Associate is for you if:

* you want to prove that you have practical knowledge of AWS.
* you’re already a Web Developer and want to show you have Cloud Computing knowledge.
* you enjoy writing code and building applications.
* you want to master how to deploy web applications to production.
* you want the highest chance of getting a job as a junior developer.

## What is a Cloud Engineer?

A Cloud Engineer is a Full Stack Web Developer who knows how to use the cloud. Cloud Engineers are Web Developers, but not all Web Developers are Cloud Engineers.

Let's contrast these two roles to see how responsibilities change when using the Cloud:

### Web Developer

* Setting up a production environment requires deep knowledge of Linux and configuring OS packages. (Some developers avoid needing deployment knowledge altogether by using Platforms as a Service like Heroku.)
* It's not easy for Web Developers to leverage Machine Learning, Cloud Storage, Analytics, or Virtual Reality, because their tools are often directly integrated into the application on a single server.
* As the complexity of a single web application grows, it becomes harder to add more Web Developers because the app becomes more difficult to learn, configure, and maintain.

### Cloud Engineer

* A Cloud Engineer has many deployment options available based on the architecture they use. Many cloud services manage the complexity for you. Then – once you've learned the cloud tools – you can directly manage deployment yourself.
* Cloud Engineers have multiple architectures to choose from such as Microservices, Serverless, or traditional.
* Cloud Engineers are better equipped to make their applications highly available, durable, and scalable.
* Cloud Engineers can leverage cloud services to bolt-on Machine Learning, Cloud Storage, Analytics, VR, Realtime, and more.
* It is easier to grow a team of Cloud Engineers, since using Cloud services encourage isolation of applications and keep apps small and easy to maintain.

## Which AWS Services You Should Give Special Attention To

Most AWS Certifications emphasize specific AWS services. It's important for you to give these AWS services special attention in your studies. I wanted to highlight the top 8 AWS services for the AWS Developer Associate and explain why they are important.

### 1. DynamoDB

DynamoDB is a NoSQL database that allows you to scale to any size. All you need to do is tell it how many reads and writes per second, and you have a guarantee of performance. DynamoDB is serverless, meaning it just scales, and you can choose to pay on demand.

The most immediate use-case I find in my day-to-day is when I need to create a small application backed by a database.

If you have to use a relational database such as MySQL or Postgres, you could use RDS. However, the starting cost would be $15 per month for a t2.db.micro. You could set up your own Postgres server on a t2.nano which would be around ~5 per month, but you’d have to configure, backup, and manage that server.

Maybe you think you could use Aurora Serverless, but in my experience, it was not as cost-effective as DynamoDB, where it was the difference between paying dollars vs paying pennies.

As a Cloud Engineer, you want to create isolated applications instead of big apps that do everything on a single server. The latter is what is known as building a monolith.

The future of application architecture is moving to micro-services. To fully decouple your services, they need to have ownership of their own database. With DynamoDB you can do that.

So in the free AWS Developer Associate course, we have put considerable effort to ensure you understand DynamoDB inside and out. The Cheatsheet is 7 pages long! [In fact, we published it for free on freeCodeCamp so you can print it out on the day of the exam](https://www.freecodecamp.org/news/ultimate-dynamodb-2020-cheatsheet/).

### 2. Elastic Beanstalk

Elastic Beanstalk (EB) is the fastest way to deploy traditional architecture to AWS. Traditional architecture is when you use Virtual Machines configured for a web framework. If you are using traditional web-frameworks such as Ruby on Rails, Laravel, ExpressJS, Django, or Spring, then you are using traditional architecture.

When you use micro-services or serverless architecture your code is broken up into smaller chunks.  Much of the responsibilities of your traditional web-framework are pushed to application integration AWS services.

However, the majority of tech companies use traditional architecture because it's what they know, and it is taking time for companies to adopt microservices and serverless.

When you want to deploy a traditional web-application you have to:

* Configure a virtual machine image by installing the correct libraries and applications
* You need to set up a load balancer and auto-scaling groups
* You need to set up a relational database and configure a secure connection
* You need to configure your Cloud Networking such as Security groups
* You’ll need to set up a deployment pipeline.

Elastic Beanstalk will set up all the above for you. All you need to do is choose what environment you want and upload your code. 

Elastic Beanstalk manages the infrastructure but does not abstract it away, so you can explore all the services it setups for you. Eventually, when you get familiar with all underlying infrastructure, you can directly manage these resources.

I like to think of Elastic Beanstalk as training wheels for deployment. It’s the best way to get started on AWS if you’re a developer, and we show you how to deploy a variety of different ways with EB.

### 3. AWS CLI and SDK, 4. CloudFormation

Nearly all AWS Services can be accessed programmatically via the AWS API. This allows you to write code to automate the creation, deletion, and configuration of any AWS services and resources within your account.

AWS CloudFormation (CFN) is also used to automate the creation and configuration of infrastructure. While it's important for developers to know CFN, the AWS CLI and SDK is more important for the Developer Associate as it allows greater fine-tune control over services programmatically. When you run into a situation where something cannot be done with CFN, you can be sure you can do that with the  CLI or SDK.

To access the AWS API you either use the AWS Command Line Interface (AWS CLI) or the AWS Software Development Kit (SDK).

The AWS CLI saves developers time from logging into the AWS console and navigating around the Graphical User Interface.

The AWS SDK is the primary way you integrate AWS Services into your web-applications. The SDK is also available in most common programming languages.

In this free AWS Developer Associate course, we take every opportunity to use the CLI and SDK, and added additional slides showing the CLI commands for various services. You'll need to know CLI commands for the exam, and they're all important to know as a Cloud Engineer.

### 5 / 6. ECS and Fargate

Elastic Container Service (ECS) and ECS Fargate make it easy to run single or multi-container applications. Running your web-applications is becoming more popular because it allows you to package your server configuration with your code, giving you greater portability of applications.

### 7. X-Ray

With microservice architecture, you have many isolated services working together. It can be difficult to monitor the performance or pinpoint failure, so X-Ray is a service that allows you to trace the path of HTTPS requests through various services.

### 8. Step Functions

Lambdas allow you to pay per 100ms for compute time – you just upload your code and AWS is responsible for the rest. The challenge is how to organize all these Lambda functions into actual serverless applications.  

Step Functions is a state machine that allows you to define something that looks like a flow chart so you can build serverless applications.

### 9. CodeCommit 10. CodeBuild 11. CodeDeploy and 12. CodePipeline

Elastic Beanstalk (EB) comes with a simple deployment pipeline. When you graduate from EB you'll have to build your own deployment pipeline. So we need to know how to use all the CI/CD AWS services.

## Overlapping Content From The Solutions Architect Associate

When you are studying for more than one AWS Associate certification, you will notice overlapping content.

40% of the AWS Solutions Architect content is necessary to pass the Developer Associate. So what we have done is carried over that 40% into this free Developer Associate exam.

So there are 6 hours of content from the free AWS Solutions Architect Associate with some minor corrections, and there are 10 hours of new content specific to the Developer Associate.

We have marked in the table of content with ? to indicate this is repeated content. So if you’ve already watched our free AWS Solutions Architect Associate course you can skip these videos.

## The #AWSCertified Challenge

To maximize your study experience, I recommend you [join the #AWSCertified Challenge](https://www.freecodecamp.org/news/awscertified-challenge-free-path-aws-cloud-certifications/) so you don’t have to study alone.

Thanks to [Jose Talancha]( https://twitter.com/jcloudofthrones) for moderating the #AWSCertifiedChallenge Discord and volunteering their time to support other people studying. 

## Recommended Additional Free Resources

There are additional free learning resources I want to recommend to you because:

* we didn’t have time to include them in this free course
* they are core to being a Cloud Engineer but are not part of the exam right now
* they explain certain difficult concepts in an alternative way.

### What The Cloud?

* [Alejandra Quetzalli](https://twitter.com/QuetzalliAle) ??? — AWS Developer Advocate @ AWS
* [Jonathan Dion](https://www.freecodecamp.org/news/p/53f649ac-89c9-4851-b2ac-8b78f6fe292a/linkedin.com/in/jotdion) ??? — AWS Developer Advocate @ AWS

What The Cloud? is the personal project of Ale and Jon to make cloud knowledge accessible to anyone. They achieve accessibility by multiple means such as:

* Translating their videos into French and Spanish
* All their videos have Closed Captioning
* They take the time to thoroughly explain cloud concepts with illustrations

Their content is for everyone. For example, in my free AWS courses I cover AWS Global Infrastructure, but I never covered Points of Presence (PoPs) because I honestly didn’t know what they were. They're mentioned, but never explained in the AWS documentation. So when I watched What the Cloud? I was surprised to learn I missed such fundamental knowledge.

Ale and Jon leave no stone and unturned, and I recommend their videos to fill any gaps in knowledge you may have been too embarrassed to ask about.

%[https://www.youtube.com/watch?v=5MO_TSLyZU4&t=70s]

### AWS Identity & Access Management

* [Bart Castle](https://twitter.com/cloudbart) ??— Cloud Technical Trainer @ CBT Nuggets

AWS IAM is required knowledge for all AWS Certifications. What appears to be a simple service gets very complicated quickly. Everything that IAM does is not in the AWS console, and its important for you to understand the underlying functionality.

I strongly recommend watching Bart’s IAM playlist so you have alternative explanations to ensure thorough knowledge of this tricky AWS service.

%[https://www.youtube.com/watch?v=j9KZeI_304g&list=PL3GN5xkPjwo23bCqxjxh0uXVW9tgIfhOi]

### AWS Amplify

[Nader Dabit](https://twitter.com/dabit3) ?️?— Senior Developer Advocate @ AWS

I really wanted to include AWS Amplify in this free AWS Developer Certification course, but we ran out of time. AWS Amplify does not currently appear in the exam, but you will see it in future exams.

The reason I want to get you hands-on exposure to AWS Amplify is because its the most powerful service for Cloud Engineers to learn. 

AWS Amplify is a modern serverless framework for building web or mobile applications. It has plugins to various AWS services so you can quickly bolt on Analytics, Machine Learning, AR, VR, Decentralized Authentication, Notifications, Chatbots, and more!

By learning AWS Amplify you are gaining a competitive advantage because, if you master this framework, you can rapidly develop applications which will absolutely impress employers. 

So I recommend you check out Nader’s Youtube channel which is packed with AWS Amplify tutorials.

%[https://www.youtube.com/playlist?list=PLSMvK3DkHvw8pV6icyH_WhgZJWAdG6InV]

## Amazon EventBridge

* [James Beswick](https://twitter.com/jbesw) ☕? — Senior Developer Advocate @ AWS 

We only briefly cover EventBridge in the free AWS Developer Associate course because currently it does not appear much on the exam. EventBridge is a service I want you to know because it fundamentally changes the way to architect serverless applications.

EventBridge was previously called CloudWatch Events, but AWS added some additional functionality to create multiple event busses and the ability to connect third-party services and multi-account services.

It’s hard to describe, so I generally say to people it’s like Zapier. But its really more like IFTTT. 

To get a good handle on EventBridge and stay current with modern serverless architecture, I recommend looking at James Beswick’s content:

* ?[Introduction to EventBridge](https://www.facebook.com/watch/?v=205256927498747)
* ?[Amazon EventBridge: Integrating with Zendesk](https://www.youtube.com/watch?v=NakNmzsN6LI)
* ?[Setting Up A Custom Event Bus](https://twitter.com/awscloud/status/1235246274032611329)
* ?[How Amazon EventBridge transforms serverless development](https://www.youtube.com/watch?v=ZF79T79RYRg)

## Some Parting Words

The world ? needs Cloud Engineers (Web Developers + Cloud Skills) right now more than ever.

The pandemic of 2020 has forced everyone to be open to remote opportunities and created a demand for cloud talent. So this is your best opportunity to enter the cloud and web development industry. 

I did my part by making this course free for you – it's up to you to complete the journey.

## ? You can [watch the course here](https://www.youtube.com/watch?v=RrKRN9zRBWs).



Note that YouTube wouldn't let us upload all 16 hours as a single video, so the first video is 12 hours. The final 4 hours of the course are in a second video, linked from the video description.

Best of luck preparing for the exam.

