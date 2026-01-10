---
title: A quick introduction to Azure function proxies
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-28T07:36:53.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-azure-function-proxies
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/Azure-Functions-Proxies.jpg
tags:
- name: Azure
  slug: azure
- name: Azure Functions
  slug: azure-functions
seo_title: null
seo_desc: "By Nadeem Ahamed\nIn this article, we'll discuss Azure Function Proxies.\
  \ They provide “Reverse Proxy Functionality” for Azure Functions. Azure Function\
  \ Proxies are quite similar to Azure API management.  \nThis post is largely inspired\
  \ by Matthew Hende..."
---

By Nadeem Ahamed

In this article, we'll discuss Azure Function Proxies. They provide “Reverse Proxy Functionality” for Azure Functions. Azure Function Proxies are quite similar to Azure API management.  

This post is largely inspired by Matthew Henderson the of Microsoft Azure Function Team. In his blog post, [Azure Functions Proxies public preview](https://blogs.msdn.microsoft.com/appserviceteam/2017/02/22/azure-functions-proxies-public-preview/), Matthew explains the reason behind why Microsoft came up with the ideology for Azure Function Proxies.

## **What are Azure Function Proxies?**

The basic idea behind Azure Function Proxies is that they allow us to define a single API surface for multiple function apps. Now any function app can define an endpoint that serves as a Reverse Proxy for another API. The endpoint can be a function app or it can be anything else. 

Are you looking out for an off the shelf tool to manage and monitor your Azure Functions? [Try this one out here for free](http://bit.ly/2L6eEmM).

## **Reason for implementing Azure Function Proxies**

For some users, it's difficult to manage large solutions with a single function app. There are a bunch of organizations using Azure Function in their micro service architecture with deployment between individual components. In this case, each function app has its own hosting, so there are many different function apps to keep track of. 

We could also have some function app combined with another API but they could be in various different regions. So we end up passing a lot of that complexity on down to our client or consuming system.

Azure Function Proxies come to the rescue by providing a unified URI (Uniform Resource Identifier) which the client can actually consume. In the meantime, we can abstract all of the different function apps or other APIs and it would also enable us to build our API at a faster rate.

## **Explanation**

![Azure Function Proxies](https://www.serverless360.com/wp-content/uploads/2018/07/Solution-Architecture-Diagram.png)

In the Solution Architecture Diagram above, we have an Azure Function Proxy followed by an Azure Function and Service Bus Queue on the back-end to store information. At the other end of the diagram, we have Data Publishers. For the purposes of this discussion, let's say that the Power Equipment generates the tag event and forwards it to Azure Functions through Proxy.

Initially, we create a function app by selecting the function option from the Azure portal. Here let's say we create an HTTP trigger for C# where the function of the HTTP trigger is to invoke a function with an HTTP request. 

Now we create two functions: one is the PostTag which represents our post if we want to create a tag. The Code for the PostTag function is the following:

![Post Tag](https://www.serverless360.com/wp-content/uploads/2018/07/Post-Tag.png)

Then, we create another function called GetTag with the code specified as follows:

![Get Tag](https://www.serverless360.com/wp-content/uploads/2018/07/Get-Tag.png)

We use GetTag to pull the message from the queue, and the last tag value returns to the client.

We can select the link specified below to fetch the URL of both the functions. This link will provide us with a Security Token for authorization.

![To Get Function URL](https://www.serverless360.com/wp-content/uploads/2018/07/To-Get-Function-URL.png)

At this point, we move over to Function App Settings and enable the Azure Function Proxies that have the latest proxy runtime version of 0.2. Consequently, we select the “New Proxy” option from Function App Development which enables us to create two proxies. They are Proxy GetTag and Proxy PostTag. The available options in proxy are:

* Proxy URL
* Route Template
* Backend URL

The URL specified in Proxy URL and the Route Template are the same regarding both the GetTag and PostTag event. The Backend URL of the Proxy GetTag will be related to the GetTag event - but for the Proxy PostTag it will be related to the PostTag event.

## Wrap-up

Azure Function Proxies are a great way to mock and test your Azure Functions endpoint even before the actual back-end development begins. Also, they can even be used in production when you need to route one URI to another.

I would like to conclude that Azure Function Proxies are one of the most engaging and go to market features that the Azure Functions team has provided.

This blog was originally published in [Serverless360](http://bit.ly/2ZkPmLZ).

