---
title: How to Set Up Application Performance Monitoring for Node.js Applications Using
  Elastic
subtitle: ''
author: Tamerlan Gudabayev
co_authors: []
series: null
date: '2023-08-07T20:57:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-monitoring-for-nodejs-applications-using-elastic
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/pexels-taras-makarenko-593172.jpg
tags:
- name: node js
  slug: node-js
- name: performance
  slug: performance
seo_title: null
seo_desc: "Building features is half the equation of creating a successful product.\
  \ \nThe other half is making something scalable and maintainable. One aspect of\
  \ that is the ability to monitor your services. \nThis is what we will learn today\
  \ using the help of so..."
---

Building features is half the equation of creating a successful product. 

The other half is making something scalable and maintainable. One aspect of that is the ability to monitor your services. 

This is what we will learn today using the help of software provided by Elastic. This is the company that originally made [ElasticSearch](https://www.elastic.co/), but which now provides a suite of different tools for search, observability, logging and much more. 

For this article, we will specifically use the [Elastic Application Performance Monitoring](https://www.elastic.co/observability/application-performance-monitoring) (APM) tool. 

## Table of Contents

* [Prerequisites](#heading-prerequisites)
* [Why Should you Monitor Your Services?](#heading-why-should-you-monitor-your-services)
* [What is Elastic Application Performance Monitoring?](#heading-what-is-elastic-application-performance-monitoring)
* [How to set up APM](#heading-how-to-set-up-apm)
* [Conclusion](#heading-conclusion)

## Prerequisites

This article is strictly about Elastic APM. So, I assume you just want to connect it to your Node.js application. 

I also assume you have Docker and Docker Compose installed locally and know how to use them. 

You can find the code for this article [here](https://github.com/TamerlanG/node-elastic-demo). 

## Why Should you Monitor Your Services?

If your software is successful (meaning you have users), then you may want to monitor your services for a few reasons.

Let's go over them in the following sections.

### You want to know the status of your services 

If your services are down, you want to know about it first. You don't want your users to be the ones to notify you. 

To help with that, you can add alerts based on some criteria, such as:

* If there are more than 10 status code 500 errors in the last 5 minutes. 
* If the latency of your services goes above some threshold (such as 1 second). 

### You can't improve something you don't measure. 

If you want to optimize something, then you first have to measure it. 

Find the hotspots and fix them. But to be able to find these, you must first monitor your services. 

This will benefit you in two ways:

The first way is that you can define your SLOs (Service Level Objectives), which are goals that you would want to have for your services. 

For example:

* **Uptime Objectives** – I want my services to be up 99.9% of the time. 
* **Latency Objectives** – I want the P99 (99th percentile) of my requests to be completed in less than 1 second. 

SLOs then help you define your SLAs (Service Level Agreements) which are promises you make to your customer. These promises increase the value that you provide to them. 

Examples of SLAs include:

* **Uptime Guarantee** – Our services will be up 99.9% of the time. If not, then we would refund you (Every company has their own refunding model – for example, AWS will give credits back for all the time affected, while other companies will simply reimburse you).
* **Latency Guarantee** – Our P99 is lower than 200ms. If not, then there will be repercussions. 

On to our final point. 

### Metrics don't always have to be technical 

We can measure user behavior. 

Things such as how long they stay on a specific page or some domain level things which are special for the business. 

These metrics allows us to make data driven decisions. 

For example, if you see your users not completing some sort of form, then you would decide that there is something wrong with it and fix it. 

Another example would be that if your landing page isn't making a lot of sales then you would decide to do something about it. 

## What is Elastic Application Performance Monitoring?

Elastic Application Performance Monitoring  (APM) is a tool that is used to monitor your application built on top of the Elastic Stack. 

Here are some of its features:

* **Real Time Monitoring** – APM collects metrics on the fly, so you can see the status of your services in real-time. 
* **Detailed Monitoring** – APM collects detailed information about requests such as response time, database queries, calls to caches, external HTTP requests, and more. 
* **System Metrics** – APM automatically picks up basic host level metrics and agent specific metrics, like .NET metrics from the .NET agent. It also collects metrics such as CPU usage and more. 
* **Collects Errors** – APM automatically collects unhandled errors and exceptions. They are grouped based on the stack trace, so you can identify new errors as they appear. 
* **Tracing** – APM allows you to trace requests across microservices that have APM set up. 
* **Support** – APM supports almost all popular programming languages and frameworks. 

## How to Set Up APM 

Now that we know what APM is and how it works, let's set it up with a Node agent locally. For this we need to go through two steps.

### Step 1: Set Up ELK Locally

Setting up the Elastic Stack (ELK) locally can be a pain. There are so many different services and you have to configure them all to work together. 

Thankfully, other people have noticed this problem and created pre-configured Docker setup for ELK. 

For the most up to date information, follow the guide [here](https://github.com/sherifabdlnaby/elastdocker). 

Here's a TLDR version:

1. `git clone https://github.com/sherifabdlnaby/elastdocker.git`
2. `cd elastdocker`
3. `make setup`
4. `make all`

At this point, you should have all the required services up and running. Most notably the three most important ones are:

* ElasticSearch which is the heart of all of this is running at port 9200. 
* Kibana which is our dashboard running at port 5601. 
* APM server which picks up the metrics running at port 8200. 

If you want to login to Kibana, here are the credentials:

* Username: `elastic`
* Password: `changeme`

### Step 2: Set Up Node Agent 

Okay, now that we have ELK set up, let's set things up from the client side. 

The first step is to add the APM node agent package. Install that using the following command:

`npm install elastic-apm-node --save`

Here's an important note. **The agent must be started before all your other modules.** 

So, most likely you would have to start it in your application main file (usually `index.js`, `server.js` or `app.js`) at the top. 

Here's an example for an Express application: 

```javascript
const apm = require('elastic-apm-node').start({
  serviceName: 'node-application',
  secretToken: 'secrettokengoeshere',
  verifyServerCert: false,
  serverUrl: 'https://127.0.0.1:8200',
})

const app = require('express')()

app.get('/', function (req, res) {
  res.send('Hello World!')
})

app.listen(3000)
```

Let's break down the configuration:

* `serviceName`: name of your application.
* `secretToken`: token required to authenticate the application to APM server. (The default token that is preconfigured from our docker-compose files is `secrettokengoeshere`)
* `verifyServerCert`: as we are running this locally, we don't want to verify certificates. 
* `serverUrl`: URL of our APM server. 

All that's left now is to run your application and play around with it a little for it to send some metrics. 

Then go to Kibana at [https://localhost:5601/](https://localhost:5601/). 

Under Observability, click on APM. 

You will find your application and it will look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-8.png)
_Elastic APM Dashboard_

## Conclusion

In summary: creating features is half the battle – the other half is monitoring and maintaining them. 

You can use Elastic's out the box solution Application Performance Monitoring tool to monitor your application. 

I hope you learned something today and if you have any questions feel free to ask me on Twitter (or X) [@tamerlan_dev](https://twitter.com/tamerlan_dev). 

Thanks for reading. 

