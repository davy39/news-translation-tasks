---
title: How to Design Almost Any Backend and Deploy It to AWS with No Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-18T00:59:52.000Z'
originalURL: https://freecodecamp.org/news/design-and-deploy-backend-with-amplify-sandbox
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/How-To-Design-Almost-Any-Backend-and-Deploy-to-AWS-with-No-Code.png
tags:
- name: AWS
  slug: aws
- name: backend
  slug: backend
- name: No Code
  slug: no-code
seo_title: null
seo_desc: 'By swyx

  In this post I''ll show you how to design four different example apps - a SimpleNote
  clone, a Twitter clone, a Slack clone, and an E-commerce store. And we''ll do it
  with the coolest new toy released at AWS re:Invent 2020.

  Introducing the Ampli...'
---

By swyx

In this post I'll show you how to design four different example apps - a SimpleNote clone, a Twitter clone, a Slack clone, and an E-commerce store. And we'll do it with the coolest new toy released at AWS re:Invent 2020.

## Introducing the Amplify Sandbox

[Amplify Admin UI](https://aws.amazon.com/blogs/aws/aws-amplify-admin-ui-helps-you-develop-app-backends-no-cloud-experience-required/) is a new low-code interface for building app backends that doesn't require any AWS expertise. However, what many people may miss is that Amplify Admin also includes [a wonderful new Sandbox](https://sandbox.amplifyapp.com/) which lets you get started without an AWS account. 

This Sandbox is a publicly sharable version of the Amplify Admin UI where you can create and prototype your data models without even logging in to an AWS account! 

Currently only [the Data sandbox](https://sandbox.amplifyapp.com/start#datastore) is built out, but over time the other AWS Amplify categories will be made available as well. 

When you first enter a Sandbox, you are dropped into a visual builder where you can add your [models, enums, and custom types](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html). Mostly, you'll just be creating models. 

You can name models, add fields, and specify types (including whether they are optional or array fields), and even add one-to-one, one-to-many, or many-to-many relationships _between_ models.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-147.png)

Further, it even lets you _share_ the data models you create! This means you don’t have to start from scratch each time you create a project, and **you can share your data schemas like you share code gists**.

## Our Four Sample Sandboxes

  
I thought it would be a great idea to demonstrate how powerful this is by sketching out four example sandboxes that you can use:

* A **notes** app (inspired by the free note-taking app [SimpleNote](https://simplenote.com/))
* A **chat** app (inspired by Slack)
* A **social media** app (inspired by Twitter)
* An **ecommerce** backend (inspired by every shopping experience)

## How to Create Entity Relationship Diagrams

Amplify Admin UI makes it easy to get going, but it is worth doing some planning before we start. 

The time-tested way to do this is to draw [entity relationship diagrams](https://www.youtube.com/watch?v=QpdhBUYk7Kk). We chose to [use Lucidcharts for ours](https://lucid.app/lucidchart/invitations/accept/563dc191-6613-44f5-aef0-24224ad5fbe1), but you can use any diagramming tool to do this.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/empty-relationship-diagrams.png)

## The Notes App

This is a minimal app that I personally use every day, so I like it for its simplicity. We have two models: Notes and Tags, and only one many-to-many relationship between them for easy querying. 

You could extend this by offering collaborative, role based editing, which is available once you deploy this model. You should also make use of the [client-side DataStore libraries](https://docs.amplify.aws/lib/datastore/getting-started/q/platform/js#datastore-with-amplify) to make sure your notes work offline.  
  
You can see the Sandbox here: [https://sandbox.amplifyapp.com/schema-design/1c782f02-1fe7-4785-9a02-22a27cc96d0d/clone](https://sandbox.amplifyapp.com/schema-design/1c782f02-1fe7-4785-9a02-22a27cc96d0d/clone). Note that we use a bidirectional **many to many** relationship here between the models, as notes can have zero or more tags and vice versa.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/simplenote-clone.png)

## The Slack Clone

Many of us use chat apps for work, so we are familiar with this app use case from the user side. 

The new nuances here are that every Message belongs to a Channel and a User, and that each User can both create Channels and join them. So there is an interesting three way relationship between the three primary models.  
  
You can see the Sandbox here: [https://sandbox.amplifyapp.com/schema-design/5f863684-fd1e-41b4-bca1-36c2271e21a1/clone](https://sandbox.amplifyapp.com/schema-design/5f863684-fd1e-41b4-bca1-36c2271e21a1/clone). **Channel** is the most complex model here – notice how we fully utilize all the relationship types available in the Sandbox:

* Channels can have **many** Users, and Users can join **many** Channels
* Channels can only be created by **one** User, and there is no requirement to keep track of what channels any particular user has created
* Channels can have **many** Messages, but each Message can only belong to **one** Channel

![Image](https://www.freecodecamp.org/news/content/images/2024/04/slack-clone.png)

## The Twitter Clone

Social media is often one of the most complex data models to model. We implement the minimum viable social media app – a Tweet and a User model is all we offer. 

However the Tweet itself has a complex set of relationships. It has an author User, and a set of likes, replies, and quotes that need to be modeled. 

Other modifications you can consider for this app: offering other types of tweets, including polls, images, and videos, building in advertisements, and direct messages.  
  
You can see the Sandbox here: [https://sandbox.amplifyapp.com/schema-design/ad5b5b7e-f207-42d1-92b1-0ccef056a26b/clone](https://sandbox.amplifyapp.com/schema-design/ad5b5b7e-f207-42d1-92b1-0ccef056a26b/clone). Note that recursion is implemented here by modeling likes, replies, and quotes as an **array** of the respective User and Tweet ID's.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/twitter-clone.png)

## The Ecommerce Store

The stakes are higher when there is money involved. Keeping track of orders and ensuring a great customer experience is paramount. 

We model a typical ecommerce backend by ensuring that we have separate models for Suppliers, Products, Orders, and Customers. To get into the nuances of a typical ordering experience, we also include the ability to specify product quantities in a single order, as well as to apply coupons. 

Since there are infinitely many variations on the ecommerce experience, we can’t possibly model them all, but I hope that this serves as a good enough starting point. Share your own if you have twists on this concept!  
  
You can see the Sandbox here: [https://sandbox.amplifyapp.com/schema-design/aa0e7a61-aa72-4b27-b6db-ea8e2031f95e/clone](https://sandbox.amplifyapp.com/schema-design/aa0e7a61-aa72-4b27-b6db-ea8e2031f95e/clone). Note the sheer complexity of this model is easily handled by the Sandbox's features. One Order can only have one Customer, but a Customer can have many Orders. 

When you set this up on the Customer model, the Sandbox is smart enough to automatically set up a corresponding customerID field as a "**Relationship Source**" on the Order model. This will be very handy for GraphQL queries down the road.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/ecommerce-store.png)

## How to Deploy the Model to AWS

Once you are done with your model, the Sandbox prompts you to test locally by downloading it with the [Amplify CLI](https://docs.amplify.aws/cli). However, if you just want to get it live on AWS, you can skip that and head straight to the "Deploy to AWS" stage:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-142.png)

Once you hit "Login to deploy to AWS", you're done! Imagine that – you've just created an actual backend data model **without writing any code** and deployed it straight to AWS. 🤯

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-143.png)

From here you can set up further customization, including adding authentication, inviting users and assigning roles, adding authorization rules on each model, creating content with our WYSIWYG editor, and more. 

If you want to learn more, [Ali Spittel did a great blogpost](https://welearncode.com/intro-amplify-admin-ui/) on how powerful the Amplify Admin UI becomes after you deploy it, whereas this article has been about the no-account-needed Sandbox environment _before_ deploying. 

Nader Dabit also wrote about [10 other features you may be keen to try](https://acloudguru.com/blog/engineering/10-exciting-features-of-the-new-amplify-admin-ui).

With the Amplify Sandbox, it is really easy to model and think through any app backend scenario, so hopefully these examples jog your creativity. If you have any requests or submissions, [please let me know](https://twitter.com/swyx)!

