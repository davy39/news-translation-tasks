---
title: How to use Azure functions to process high throughput messages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T10:53:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-azure-functions-to-process-high-throughput-messages-996d05d4ab23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c37536mEXRF32zB3duPzTA.png
tags:
- name: Azure
  slug: azure
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Nadeem Ahamed

  Authored with Steef-Jan Wiggers, Azure MVP.

  With Microsoft Azure, customers will push all types of workloads to its services.
  Workloads are ranging from datasets for Machine Learning purposes to a large number
  of messages for the Ser...'
---

By Nadeem Ahamed

Authored with [Steef-Jan Wiggers, Azure MVP](https://www.serverless360.com/blog/author/steef?utm_source=medium-freecodecamp&utm_medium=author-name&utm_campaign=blog-resurfacing).

With Microsoft Azure, customers will push all types of workloads to its services. Workloads are ranging from datasets for Machine Learning purposes to a large number of messages for the Service Bus. In any case, Azure like any cloud provider is elastic enough to deal with any size of workload. Scalability and availability are common phrases for cloud-computing. Moreover, you leverage the cloud for it and pay for using it.

### Messaging scenario

In this blog post, we will look at a specific messaging scenario. Suppose we have a large number of messages pushed to a service bus topic from a LOB application. Furthermore, multiple listeners are attached to subscriptions on a topic. The number of messages per subscription is 50 to a hundred per second — for the service bus, it is easy to handle. The challenge in this scenario is how to scale an Azure service consuming these messages at the same rate. Would you use functions, a web job or perhaps Service Fabric?

For this blog post, we choose a client application generating ~100,000 messages per minute or around 1,666 messages per second. Each message is sent to a topic in Azure with five subscriptions. Each subscription has a corresponding Azure Function consuming the message (service bus topic trigger) and inserting it into a Cosmos DB document collection.

![Image](https://cdn-media-1.freecodecamp.org/images/YRIPBCqQLxLvkEJvrSdu-a66VLIuxrHryPtX)

### Azure Functions

Azure Functions are part of the Azure Web + Mobile suite of App Services. They are designed to enable the creation of small pieces of meaningful, reusable methods. These methods are easily shared across services. These serverless, event-driven methods are often referred to as _“nano-services”_ due to their small size. Although an Azure Function can contain quite a bit of code, they are typically designed to serve a single purpose and respond to events in connected services.

In our scenario, the functions can respond to messages in a service bus queue or topic (subscription). The challenge for throughput lies with hosting the functions. Functions can run on a consumption plan or app service plan. The latter allows for upscale dimensioning. When running on consumption, you pay for the underlying infrastructure supporting your function in a Function App.

We choose to develop a simple function using the topic trigger binding and Cosmos DB binding for output. The function code looks as follows:

```java
using System;
using System.Threading.Tasks;
public static void Run(string mySbMsg, ILogger log, out object outputDocument)
{
log.LogInformation($"C# ServiceBus topic trigger function processed message: {mySbMsg}");
outputDocument = new
{
mySbMsg
};
}
```

The incoming message is sent as output (document) to a collection in CosmosDB. The potential limiting factor on the Cosmos DB side is the specified number of [Request Units per second (RU/s)](https://docs.microsoft.com/en-us/azure/cosmos-db/request-units). When this setting is set too low, throttling will occur, and you would see HTTP 429 messages appear.

Furthermore, the reserved performance is specified regarding Request Units (RU) per second. Hence, each operation in Azure Cosmos DB, including writes, updates, reads, and queries, and updating a document, consumes CPU, memory, and IOPs. By specifying Request Units, you are provided with guaranteed performance and elasticity at any scale. For our setup, we choose 10000 RU/s.

### Testing the setup with Azure Functions

Once we run the test, we notice it takes up to 90 seconds for our message generator to send 100000 messages to a service bus topic in Azure (West-Europe). Hence, we have an outbound stream of over 1000 messages per second. Subsequently, it takes about an additional 180 seconds for five functions to read the corresponding subscriptions and write to the Cosmos DB collection. The documents are about ~ 1Kb in size each.

Once we start the test, we see the number of in- and outgoing requests increase to 100 per second and growing during the trial to 500 per second.

During the trial, we see the subscriptions fill up with messages and subsequently decrease over time to zero. In the end, about 180 seconds after the application sending the messages finishes. This behavior can be observed when running the test for the first time.

![Image](https://cdn-media-1.freecodecamp.org/images/6C8hHxeTYI00zdL7vcXs4Ge6c6rCx4UTomWG)

After all the subscriptions are read, and the functions finish processing the in- and outgoing request in the live metrics of the Application Insights drop to zero.

![Image](https://cdn-media-1.freecodecamp.org/images/xOuhKPd3c3ALsjaEWSVjpftD9jDNsSE0D6OQ)

### After several tests the outcome is as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/S7FcJSV6VoGYRj6ac9cTlC8S7Vpt2-rclvx8)

Message sender sends within 90 seconds 100000 messages to a Service Bus Topic: > 1100 messages/second.

The five functions consume and process the 100000 messages in 270 seconds: > 350 messages/second. After one test the functions are warmed up. Any test following the first results in a throughput of over 1000 messages/second. This corresponds with the latency Cosmos DB promises when writing messages of around 1 Kb.

Note that when running functions on a consumption plan your app can go to sleep leading to cold start issues. According to a post from fellow MVP Chris ‘O Brien:

![Image](https://cdn-media-1.freecodecamp.org/images/D-UL-NiGG6RejKC1OLKmgj5OtJBPTjjutPop)

> _Currently, the timeout period for Azure Functions is 20 minutes — so if there are periods where your function won’t run, you’ll suffer from this issue._

This behavior shows when testing the scenario, the first time. After the functions are warm, the throughput triples from ~ 350 to ~ 1150 msg/sec.

We re-run the tests with a function in a function app using an app service plan B3 (Standard) and the number of instances set to three. Also, the number of functions and subscriptions were limited to three.

The test with an App Service Plan using a B3 led to a throughput of ~ 1150 messages/sec each time without any warm-up issues.

![Image](https://cdn-media-1.freecodecamp.org/images/AgyczAhS40Xt82W19bxbSZNU0f4M5EO0vxhM)

The graphs above show the number of in- and outgoing requests are around the measured throughput.

![Image](https://cdn-media-1.freecodecamp.org/images/-X1FHjnYrlqR-7wy9qFWKtCvHWkBO38h8Fe0)

You could further experiment using a premium or isolated App Service Plan with more resources.

### Azure WebJobs

A useful means to automate tasks in the cloud is by leveraging Azure WebJobs hosted on Azure App Service. With the App Service, you can continuously read messages from a service bus topic (subscription) or queue without running into warm-up issues. For our scenario, Azure Function on a consumption plan is enough, regardless of the warm-up problems.

### Service Fabric

With Service Fabric you build distributed applications at scale leveraging the Azure infrastructure. The service is an open source project and powers core Azure services such as Azure Event Hubs, Cosmos DB, and Dynamics 365. You can use Service Fabric to develop services that auto-scale based on needs and thus any required throughput. Therefore, when you expect a performance unable to be achieved with Web Jobs or Azure Functions you can opt to go for a Service Fabric implementation. For our scenario, Azure Functions is sufficient to meet the 50 to 100 messages per second throughput.

### Wrap up

In this blog post, we looked at a scenario of achieving a given throughput of messages from a topic to Cosmos DB. With a function, leveraging the Service bus and Cosmos DB binding, we can easily consume over 300 messages per second and insert the messages into a Cosmos DB collection. In case we exclude the warm-up issues, the functions can efficiently process over 1000 messages per second.

> _Hence, we can conclude Azure Functions are a good option for handling around 1000 messages per second with the appropriate service plan in place._

Note that this blog describes a small experiment and more options are available to process a high volume of messages in Azure.

### Management and Monitoring

One may need a deeper insight into the Azure Serverless entities to leverage it. With the third party tool [Serverless360](https://www.serverless360.com/?utm_source=Freecodecamp-blog&utm_medium=&utm_campaign=), you can manage your composite cloud-native solution at one place. The tool monitors your Azure integration services like Logic Apps, Functions, Event Hubs, Service Bus, and API endpoints. Furthermore, you can:

* In your service bus queues or topics, access active messages to know more details, process the dead letter messages to repair, resubmit or merely purge them.
* Detect and be alerted about violations occurring in your composite integration solutions.
* Integrate your Azure serverless monitoring with essential notification tools like PagerDuty, Microsoft Teams, ServiceNow, Slack, SMTP, and OMS.
* Have full control over what your colleagues or consultants can see and do with the Azure resources in your environment.
* Governance and audit report provide detailed information on the four W’s — WHO accessed WHAT, WHEN, and WHY. Serverless360 collects, consolidates, and enables search filters on your account logs.

![Image](https://cdn-media-1.freecodecamp.org/images/ZaCZPn44t2r0OqM042dfC9jqf69Dcjix3y0U)
_Serverless360 Composite Application_

> _Originally published at [www.serverless360.com](https://www.serverless360.com/blog/azure-functions-to-process-high-throughput-messages?utm_source=medium-freecodecamp&utm_medium=link&utm_campaign=blog-resurfacing) on November 27, 2018._

