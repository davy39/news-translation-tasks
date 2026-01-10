---
title: How to Become a Serverless Developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-19T20:57:22.000Z'
originalURL: https://freecodecamp.org/news/become-a-serverless-developer
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/sls_talks_3_B.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: serverless
  slug: serverless
- name: serverless framework
  slug: serverless-framework
seo_title: null
seo_desc: 'By Sam Williams

  Serverless Development has been around since the release of AWS Lambda in 2014,
  but in the last few years things have exploded.

  Startups and smart tech companies have started taking advantage of the scalability,
  reliability, and power...'
---

By Sam Williams

Serverless Development has been around since the release of AWS Lambda in 2014, but in the last few years things have exploded.

Startups and smart tech companies have started taking advantage of the scalability, reliability, and power of serverless to rapidly grow – and now they need more serverless developers than ever.

Being a "Serverless Developer" means you build solutions with managed services from the likes of AWS, Google Cloud (GCP), or Azure. You build solutions by piecing together different services and running all of your business logic in AWS Lambda or CGP Cloud Functions instead of on a server.

With your cloud platform dealing with almost all of the operations (security, redundancy, scalability, and networking), you're left to focus on building the best solutions you can. This means features can be built quicker and companies don't need to hire operations specialists.

This article will cover the 5 steps to learning how to become a serverless developer so you can build some kick-butt products.

## In Summary

1. Have solid JavaScript or Python skills. You don't have to be a wizard but being comfortable write an Express or Flask server will make the rest much easier.
    
2. Pick your framework – choose either [The Serverless Framework](https://www.serverless.com/) or [AWS CDK.](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
    
3. Follow a tutorial to start learning to build with your framework. Start with building an API with API Gateway and Lambda.
    
4. Learn more about the services you're using. What are the benefits, limitations, good use cases and bad ones?
    
5. Build what you've learnt in the tutorials into your own project.
    

Now you've learnt to build an API, add some more services, repeating steps 3-5 each time. A good order could be:

* DynamoDB – getting and writing data
    
* S3 – reading and writing files
    
* DynamoDB – with secondary indexes and queries
    
* Cognito – Authorisation for your API
    
* AppSync – GraphQL API
    

%[https://youtu.be/u-UaP8XONgg] 

## 1\. Solid JavaScript or Python Skills

Before trying to build serverless systems, you really need to have a good grasp on the fundamentals of one of the common programming languages. You don't need to be a wizard, but being comfortable using your chosen language is key.

The reason you need to be comfortable writing good code is that it has a massive effect on the software you build. Serverless is like building blocks and the Lambda code is like the glue. In that code, you write the logic for connecting each part.

> You could have the perfect architecture but if your Lambda code is buggy, your solution will be, too.

I recommend either JavaScript (TypeScript) or Python. The reason I recommend these two languages is that most of the companies that will be using Serverless Architecture will be using one of these two languages. Luckily they're also the two languages taught here on FreeCodeCamp 🎉 .

Being the most widely used they also have more tutorials and a bigger community to help when you get stuck.

Another reason that I recommend these languages is that you can write the framework code with the same language you write the Lambda code with. You'll be constantly jumping between lambda code and frameworks config. Not having to switch between languages will save a LOT of you brain juice 🧠

## 2\. Pick your Framework

With a solid grasp of your language, you need a tool to help you create the serverless components in AWS.

There are LOT out there, but I would say you should pick either the Serverless Framework or AWS CDK. I have a bias towards the Serverless Framework as I have a [**Youtube channel**](https://www.youtube.com/CompleteCoding) with over 50 videos on building with it. If you're a Python developer then maybe the AWS CDK might be better suited for you.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/slsVsCdk.png align="left")

### Why use a framework?

When building a solution it is possible to do it all in the AWS Console. That's how I started my AWS journey.

The issue is that it is not controllable, manageable or scalable. If you want to copy this setup to another account (separate dev and prod accounts) you have to remember all the steps you've done. Working with multiple team members can get messy.

That is why it's helpful to use a framework to allow us to write Infrastructure-as-Code (IaC). This allows us to use Git for version control. This makes working as a team much easier, enables multi-environment deployments, even continuous integration and deployment. All things that are required when running production workloads

### The Serverless Framework

* Proven in large, production workloads
    
* Easy to get started
    
* Large community
    
* Lots of tutorials
    
* Lots of plugins to make many jobs easier
    

* Not as easy when doing things that aren't serverless
    
* If you're using Python, you'll have to configure it with YAML
    

### AWS CDK

* From AWS and is actively developed by them
    
* Good support for almost anything in AWS
    
* Some cool ways to create re-usable constructs
    
* Growing community and pool of tutorials
    
* Can define the config using Python
    

* Not the same 'Plugins' ecosystem as the Serverless Framework
    

### Other Frameworks

Some of you may say "What about all of the other frameworks?" and I'll address those.

#### AWS SAM & AWS Amplify

![Image](https://www.freecodecamp.org/news/content/images/2022/01/SAM-AMPLIFY.png align="left")

These frameworks are designed to be very easy to do simple things. If you're reading this then you could probably use these to create an API and website quickly and easily.

This is great if that is all you want to do. But if you want more control over **how** they are deployed or want to deploy **more complex systems** then you're going to struggle.

#### Terraform & Ansible

These frameworks have been around for a long time and are used in enterprise as their Infrastructure as Code (IaC) tool.

The reasons I wouldn't learn these as my first framework are:

1. You have to learn a new language. Terraform uses HCL (Hashcorp Language) and Ansible uses YAML. Leaning a new language whilst trying to learn about Serverless architecture isn't ideal. Also switching into that language when you need to create infrastructure is brain zapping.
    
2. They are opinionated and strict. Getting a small thing not configured perfectly will just not work, often with a hard to understand error.
    
3. They're not as flexible or powerful as CDK or Serverless Framework.
    

#### Webiny & Serverless Cloud

These are very new frameworks that are trying to make IaC as simple but as powerful as possible.

The reason that I would avoid these for now is that they're just too new. This has two drawbacks:

1. The community isn't as big. This means fewer tutorials and fewer people to ask if you get stuck
    
2. Things change quickly. Best practices and common structure, but sometimes APIs, methods and parameters too. When learning a framework you don't want to have to deal with this stuff.
    

If there is a feature you absolutely need to use and you have someone who is very experienced with that specific framework, then it could work. I would still recommend one of the main two.

## 3\. Follow a tutorial

With your framework chosen, you can now start building things with it.

The first thing you should build is an API using just Lambda and API Gateway. This is very simple but will get you practice with the core fundamentals of the framework. Understanding the fundamentals will make learning more advanced things much easier.

### Why Follow a Tutorial

When learning a new service, it may be tempting to try and learn it by adding it straight into an existing project. I would recommend always trying to follow a tutorial the first time you work with any new service or tool.

When you follow a tutorial it should work without any issues. This means you can focus on learning about the service and how it fits in with everything else.

Adding it into your own project means if something doesn't work you've got to debug it on your own. You might not know whether you've used the service wrong or if there is a bug connecting it to your existing system.

## 4\. Learn more about the services you're using

Now that you've used the new service, it's a good idea to learn a bit more about it. The key things I would want to know about a service I use are:

1. What are its strengths, weaknesses, and limitations?
    
2. What are some ideal use cases for using the service?
    
3. What are some use cases where you should avoid using this service?
    

Knowing these three things, you will be much better able to decide whether a service will be a good fit for the solution you are currently building.

You can learn from a range of places: tutorials, articles, and even the AWS Docs.

For example, AWS Lambda is great for most APIs, but can't run for more than 15 minutes. If I need to build an API that does some batch processing that takes 10-20 minutes then it would time out half of the time. Therefore I need to find another solution.

Again you don't need to understand every little detail about every service, just enough to know when it is a good idea to use and when not to.

## 5\. Build your own projects

Now you know how to build with the new service (from the tutorials) and have a good understanding of when to use the service.

From here it is time to use these services in your own projects.

I would recommend starting with a personal project that you use just for practicing using new services in. That way you don't have to worry about breaking things and you can focus on how the service is working.

You can now start using it in production apps and this is where you'll learn a lot about the details of a service. You learn how to make it meet the business requirements and how it works with other services. If you can do this as part of your job, even better. Else have a deployed app that you treat with the same care.

## Repeat steps 3-5

Congratulations! You've learnt how to build an API using a framework.

That isn't the end, as there's always more to learn and a way to become a better serverless developer. Pick a new topic, service, or design pattern and repeat steps 3-5.

If you've just made your first serverless API, then here are the next topics and services I would learn to continue your journey.

* DynamoDB – creating a simple table, getting and writing data
    
* S3 – creating an S3 bucket, reading and writing files
    
* DynamoDB – with secondary indexes and queries
    
* Cognito – Authorisation for your API
    
* AppSync – GraphQL API
    

After that, focus on creating features for your solutions and use that to guide what to learn next.

If you're a JavaScript developer wanting to use the Serverless Framework, then a great place to start is my [Youtube channel](https://www.youtube.com/CompleteCoding) where we create tutorials on becoming the best Serverless Developer that you can be.
