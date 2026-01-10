---
title: Why GraphQL is the key to staying out of technical debt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T15:49:33.000Z'
originalURL: https://freecodecamp.org/news/why-graphql-is-the-key-to-staying-out-of-technical-debt-7915f8f59a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MGM-mwrfaPHWZIr0JiTKfA.png
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Burke Holland

  GraphQL (not to be confused with GraphDB or Open Graph or even an actual graph)
  is a remarkably creative solution to a relatively common problem: How do you enable
  front end developers to access backend data in exactly the way they n...'
---

By Burke Holland

GraphQL (not to be confused with GraphDB or Open Graph or even an _actual_ graph) is a remarkably creative solution to a relatively common problem: **How do you enable front end developers to access backend data in exactly the way they need it?**

Quick example: We want to display a list of products on a web page. So we write a service which returns a list of products. We make it super RESTful because that’s what someone on a podcast said we should do.

```js
{
    "items": [
        {
            "id": 2051,
            "name": "Extension Cord",
            "price": 15,
            "productType": "Electrical",
            "supplierName": "Northwind",
            "shortDescription": "Outlet not where you need it? Extend your power to the right place at the right time",
        },
        {
            "id": 2053,
            "name": "LED Lamp",
            "price": 14,
            "productType": "Hardware",
            "supplierName": "Northwind",
            "shortDescription": "Low power battery operated light",
        }
    ]
}
```

Then we slap said products on the page. Go ahead and imagine a slapping sound. Or feel free to use this one here…

%[https://soundcloud.com/acharus/slap-sound-effect]

![Image](https://cdn-media-1.freecodecamp.org/images/1*DPtCGHJIWOH2gZJi1ZApAw.png)

Now that we have everything done, someone decides we also need to display what quantity of each product we have in stock because of course they do.

Ok. I guess. I mean, you didn’t specify that in the original project document, but why not. Let’s just make the scope whatever **you** want it to be.

The product quantity information is a field in the database, but it’s not being returned by the service. In order to get to it from the front end, we have to modify the code of our service and then redeploy before we can even think about making changes on the front end. For one field.

Likewise, if this same someone (who can’t seem to decide what they really want in life) decides that we no longer need the SKU, we can ignore it on the front end, but it’s part of the API response so it ends up being junk data in the payload, and pointless bits that our users don’t need.

**Every project** is just this back and forth of unforeseen changes. That’s literally the definition of “Software Development”. I mean it’s not, but my point sounds better if I reference a dictionary.

The point is that we end up making a lot of trade-offs on both the front and back ends just to make things work and keep up with the pace of change. And trade-offs equal technical debt.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LQSVhGCpmMOzBdSq.)

This is the very essence of the problem that GraphQL is trying to solve.

I only recently put all the GraphQL pieces together in my own head. It wasn’t until my colleague [Simona Cotin](https://twitter.com/simona_cotin) volunteered to teach me GraphQL that I had the epiphany that it is, perhaps, the answer to a problem that I’ve been trying to work around the bulk of my professional career.

#### Learn GraphQL With Us

Simona and I did three teaching sessions together and we recorded each one. In these three videos, you can learn with me as I go from zero knowledge about GraphQL, to implementing a GraphQL interface and then consuming it from a React application.

Each video comes with a Github repo that you can clone to get the fully working solution in case you get lost along the way.

We use Azure Functions a lot in this video series because it’s so much easier to build a Serverless API than it is to start from scratch. Grab a free Azure account if you don’t already have one.

[**Create your Azure free account today | Microsoft Azure**](https://azure.microsoft.com/free/?WT.mc_id=video-youtube-sicotin)  
[_Get started with 12 months of free services and $200 USD in credit. Create your free account today with Microsoft…_azure.microsoft.com](https://azure.microsoft.com/free/?WT.mc_id=video-youtube-sicotin)

### Part 1: Introducing GraphQL

In the first video, Simona introduces me to the concepts of GraphQL and the quirky syntax that it uses. We also create the GraphQL API in this video and deploy it.

%[https://youtu.be/x-imn__380s]

[**simonaco/serverless-graphql-apis-part1**](https://github.com/simonaco/serverless-graphql-apis-part1)  
[_Contribute to simonaco/serverless-graphql-apis-part1 development by creating an account on GitHub._github.com](https://github.com/simonaco/serverless-graphql-apis-part1)

### Part 2: Installing Graphiql locally and deploying

In part 2, I get the [Graphiql](https://github.com/graphql/graphiql) visual GraphQL testing tool running locally on my own machine and then deploy it to [Azure Storage](https://code.visualstudio.com/tutorials/static-website/getting-started?WT.mc_id=freecodecamp-blog-sicotin) so I can easily test my GraphQL API without needing to wire up an application.

%[https://youtu.be/X2846rUj_P8]

[**simonaco/serverless-graphql-apis-part2**](https://github.com/simonaco/serverless-graphql-apis-part2)  
[_Contribute to simonaco/serverless-graphql-apis-part2 development by creating an account on GitHub._github.com](https://github.com/simonaco/serverless-graphql-apis-part2)

### Part 3: Using the API in a React App

We round out this series by looking at how to actually call this API from an application. That’s kind of an important detail.

%[https://youtu.be/c2r_nUDUYe0]

[**simonaco/serverless-graphql-apis-part3**](https://github.com/simonaco/serverless-graphql-apis-part3)  
[_Contribute to simonaco/serverless-graphql-apis-part3 development by creating an account on GitHub._github.com](https://github.com/simonaco/serverless-graphql-apis-part3)

#### Learn more about GraphQL

Once you understand the problem that GraphQL solves, you’ll start to see opportunities for it everywhere. And the best part is that you don’t have to start fresh to use it. In fact, it’s _recommended_ that you use it on top of a typical REST API, so you’re likely in the perfect spot to use GraphQL today.

If you want to go further with GraphQL and React, check out [Wes Bos’s](https://twitter.com/wesbos) course. It’s paid, but it’s worth every penny. This is an investment you will be glad you made. Wes doesn’t pay me anything to say that. But maybe he should.

[**Advanced React & GraphQL**](https://advancedreact.com/)  
[_Build Full Stack Applications with React and GraphQL_advancedreact.com](https://advancedreact.com/)

