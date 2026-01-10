---
title: Azure Logic Apps Use Case – Black Friday
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-04T04:25:56.000Z'
originalURL: https://freecodecamp.org/news/azure-logic-apps-use-case-black-friday
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/black-friday-Banner-image.png
tags:
- name: Azure
  slug: azure
- name: Logic Apps
  slug: logic-apps
- name: Middleware
  slug: middleware
- name: use-cases
  slug: use-cases
seo_title: null
seo_desc: 'By Nadeem Ahamed

  This blog gives an overview of how Azure Serverless technologies came to rescue
  when the custom-built integration system went down. Also, it shows the high-level
  architecture solution built using Azure Serverless services like Logic ...'
---

By Nadeem Ahamed

This blog gives an overview of how Azure Serverless technologies came to rescue when the custom-built integration system went down. Also, it shows the high-level architecture solution built using Azure Serverless services like Logic Apps, Service Bus Queue and Topics, etc to replace the legacy system.

This article was originally published at [Serverless360.com](https://www.serverless360.com)

## How it all Started?

![Legacy system](https://www.serverless360.com/wp-content/uploads/2019/06/1-Legacy-system.png)

About three years ago, Northwind, a company who runs their business in B2B space wanted to extend its business to B2C. So, the company wanted to open a Web Shop (SaaS). Since it was a B2B specialized company there were no warehouse and transport service to serve the customers effectively. The company chose to go ahead with LSP (Logistics Service Provider) instead. The legacy system was built using a middleware to connect the Web Shop and the LSP. Later, the legacy system was integrated with the email system. The complexity of the system increased as several branches (Web shops) opened across the globe.

One day, the whole system went down, and the company started losing hundreds of orders. Then, the company approached an expert team to fix their middleware.

### **Requirements to be considered**

* Stability – the system needs to be stable enough to handle a lot of orders.
* Monitoring – the system should be monitored to alert the operation personnel when something goes wrong.
* To handle 10,000 orders per hour.
* New SaaS webshop

## The Solution

![Serverless middleware](https://www.serverless360.com/wp-content/uploads/2019/06/2-serverless-middleware.png)

The expert team replaced the middleware using Azure serverless technologies. Predominantly, Logic Apps and other Serverless entities like Azure Functions, Service Bus Queues and Topics were used. The stateful middleware was changed to stateless using event-based approach.

## What is Serverless?

![what is serverless](https://www.serverless360.com/wp-content/uploads/2019/06/3-what-is-serverless.png)

**The abstraction of server, platform, and runtime** – There is no need to provision or maintain any servers. There is no software or runtime to install, maintain, or administer.

**Event-driven scaling** – This is one of the important characteristics of Serverless, you shouldn’t worry about scaling your solution if demand arises.

**Micro-billing** – When your code is executed you pay per execution. Typically, the vendors calculate this based on memory consumption and the time it takes for the execution.

### Advantages

**Manage apps not servers** – The significant advantage of serverless is that the user does not manage the servers, but the cloud service providers do.

**Reduced DevOps** – It reduces the DevOps cost as the infrastructure is maintained by CSP.

**Faster time to Market** – It reduces the time to market as serverless technology screens the ground works and lets the developer focus on the logic.

## Azure Logic Apps

> _You can run a business workflow in Azure using the Logic App service._

The Logic App is a logical container for one workflow you can define using triggers and actions. A trigger can instantiate a workflow, which can consist of one or many activities (actions). For instance, you can trigger a workflow by sending an HTTP request or schedule a workflow every hour to retrieve data from a public website. There are 200+ out-of-the-box connectors available for enterprise integration.

### Benefits

* Out-of-the-box connector reduces the integration challenges
* Connect and Integrate data from the cloud to on-premises
* B2B and enterprise messaging in the cloud
* A powerful web-based workflow designer

## Pricing of Azure Logic Apps

![Azure logic Apps pricing](https://www.serverless360.com/wp-content/uploads/2019/06/4-logic-Apps-pricing.png)

The pricing is very simple. It works on the pay-as-you-go model, it would cost you only a few nickels. For instance, if you process 1000 service bus messages a day, with a workflow of five actions it would cost you EUR 4.62 approx. To execute a normal action, it would cost $ 0.000025 and for a Standard connector, it would cost you $0.000125. Even, the Enterprise connector would cost you only $0.001. For more information see the pricing page [here](https://azure.microsoft.com/en-in/pricing/details/logic-apps/).

## Basic Architecture Solution

![Basic architecture solution](https://www.serverless360.com/wp-content/uploads/2019/06/5-Basic-architecture-solution.png)

Initially, there is a webshop connected to Webshop publisher Logic App through Webhook. The Webshop publisher Logic Apps act as the orchestrator for the workflow. The data from the Webshop is converted into Canonical entity and passed to the Canonical Order Mapper Logic App. Subsequently, the control flows to the CE publisher where the translation of the object happens. Then, the translated object is sent to Service Bus Topic. Topic Subscriptions provide a one-to-many form of communication, in a publish/subscribe pattern. Get to know about Topic Subscription rules [here](https://www.serverless360.com/blog/manage-azure-topic-subscription-rules).  Based on the filter, the orders are sent to LSP Subscriber and MS (Marketing System) Subscriber.

## Impressive Scalability of Azure Logic Apps

![impressive scalability](https://www.serverless360.com/wp-content/uploads/2019/06/6-impressive-scalability.png)

On running the above workflow, it could process 73,120 orders in 20 min. Every order would get processed in less than 3 seconds and the success rate was above 98 percent. The above log shows that there were 73,120 runs completed and out of which 72,972 runs were accomplished and 148 runs were failed.

## View of Entities in a Resource Group

![view of entities](https://www.serverless360.com/wp-content/uploads/2019/06/7-view-of-entities.png)

The above picture represents how the entities will be listed in a Resource Group. For better management of the entities use the Display Name tag. It helps the user to debug the workflow in case of failure.

## Webshop Publisher Logic App

![webshop publisher logic app](https://www.serverless360.com/wp-content/uploads/2019/06/8-webshop-publisher-logic-app.png)

Out-of-the-box, there is an HTTP trigger which initiates the Logic App and sends 201 response directly for the received message. 201 response represents that request has been fulfilled and has resulted in one or more new resources being created. Subsequently, sends the order message to the other Logic App (Map order to Canonical order) and to Publish canonical order.

### Tracked properties

In “Response 201 directly” action, the following properties are tracked

* Customer Email
* Flow
* Order ID
* Shop ID

## Canonical Order Mapper

![canonical order mapper](https://www.serverless360.com/wp-content/uploads/2019/06/9canonical-order-mapper.png)

The Logic App gets triggered by receiving the HTTP request. Then, the message would be passed to Data Operation actions to compose canonical order items and create shop reference data.  Subsequently, composes the canonical order using Data Operation action and sends back the response.

## Service Bus Explorer

For easy management of the entities use Service Bus Explorer. It provides filter option for Service Bus Topic using which the message can be sent to the defined subscriptions (LSP). The message will be filtered based on the properties defined in the Service Bus Topic. [Here is how Serverless360 makes a better option for Service Bus Explorer.](https://www.serverless360.com/compare-service-bus-explorer)

## Monitoring

![Log Analytics](https://www.serverless360.com/wp-content/uploads/2019/06/10-Log-Analytics.png)

The above picture shows the Log Analytics dashboard. It provides a graphical representation and monitoring capability for the entities associated with the Log analytics. Inside the Log Analytics, the user can run powerful quires and inspect the database if something goes wrong.

## Demo – order paid

To test the new solution architecture, send the test order, use the Postman tool to send a POST message to the Logic App. On sending the successful order, you can see the 201 response at the bottom left corner of the Postman tool. On receiving the order, the Logic Apps gets triggered and finally, the order message would reach any one of the respective LSP.

## CI/CD pipeline

![CICD pipeline](https://www.serverless360.com/wp-content/uploads/2019/06/10-CICD-pipeline.png)

The above picture represents the CI/CD pipeline architecture. There are three blocks namely Developer context, Azure DevOps and Azure subscription. The Developer context contains PowerShell, IDE’s, etc. Once the developer checks in the code, it commits to the repository. On switching the Build option, build pipeline deploys the code to the Blob storage. Once Build pipeline is done with the work, Release pipeline kicks off and tells the ARM to reflect the changes in Development, Testing, and Production environment.

### Benefits

* No manual steps required to deploy the code.
* Quality control can be done
* The organization can have a bigger development team

### **Challenges**

* A lot of housekeeping is required around ARM templates.
* Things get complex if any ARM template goes down. Because the failure can be spotted only during release.
* The rhythm of the service changes rapidly

## Key Takeaways from the Above Solution

* Faster time to market: There were only three developers and they could get the project done within 3 months.
* Resilient and scalable: As we saw above the application was highly scalable. It could handle about 73 thousand orders in 20 minutes.
* It is best suitable for business-critical systems

This blog is an extraction of the session “Black Friday? Logic Apps to the rescue” presented by [Aarjan Meirink](https://twitter.com/aarjanmeirink) at MSBuild 2019.

