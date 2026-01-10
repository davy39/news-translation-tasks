---
title: How to Handle Logs in Microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-12T16:31:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-logs-in-microservices
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Microservice-Observability---Logs.png
tags:
- name: logging
  slug: logging
- name: Microservices
  slug: microservices
seo_title: null
seo_desc: 'By Siben Nayak

  Logging is one of the most important parts of software systems. Whether you have
  just started working on a new piece of software, or your system is running in a
  large scale production environment, you’ll always find yourself seeking he...'
---

By Siben Nayak

Logging is one of the most important parts of software systems. Whether you have just started working on a new piece of software, or your system is running in a large scale production environment, you’ll always find yourself seeking help from log files. 

Because of this, logs are the first thing developers look for when something goes wrong, or something doesn’t work as expected.

Logging the right information in the right way makes a developer's life so much easier. And in order to get better at logging, you need to know what and how to log. 

In this article, we’ll take a look at the some basic logging etiquette that can help you get the most out of your logs.

# What to Log and How Logging Works

Let’s start with an example of an e-commerce system and take a look at logging in its Order Management Service (OMS).

Suppose a customer order fails due to an error from Inventory Management Service (IMS), a downstream service that OMS uses to verify the available inventory.

Let’s assume that OMS has already accepted an order. But during the final verification step, IMS returns the following error because the product is no longer available in the inventory.

`404 Product Not Available`

## What to Log

Normally, you would log the error in this way:

```java
log.error(“Exception in fetching product information - {}”, ex.getResponseBodyAsString())
```

This will output a log in the following format:

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in fetching product information - Product Not Available
```

Well, there isn’t much information available in this log statement, is there? A log like this doesn’t serve much purpose because it lacks any contextual information about the error.

Can we add more information to this log to make it more relevant for debugging? How about adding the Order Id and Product Id?

```java
log.error("Exception in processing Order #{} for Product #{} due to exception - {}", orderId, productId, ex.getResponseBodyAsString())
```

This will output a log in the following format:

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #182726 for Product #21 due to exception - Product Not Available
```

Now this makes a lot of sense! Looking at the logs, we can understand that an error occurred while processing Order #182726 because Product #21 was not available.

## How to Log

While the above log makes perfect sense for us humans, it may not be the the best format for machines. Let’s look at an example to understand why.

Suppose there is some issue in the availability of a certain product (say Product #21) due to which all orders containing that product are failing. You have been assigned the task to find all the failed orders for this product.

You happily do a `grep` for Product #21 in your logs and excitedly wait for the results. When the search completes, you get something like this

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #182726 for Product #21 due to exception - Product Not Available

[2020-09-27T18:53:29,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #972526 for Product #217 due to exception - Product Not Available

[2020-09-27T18:52:34,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #46675754 for Product #21 due to exception - Product Not Available

[2020-09-27T18:52:13,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #332254 for Product #2109 due to exception - Product Not Available
```

Not quite what you were expecting right? So how can you improve this? Structured logging to the rescue.

# What is Structured Logging?

Structured logging solves these common problems and allows log analysis tools to provide additional capabilities. Logs written in a structured format are more machine-friendly, meaning they can be easily parsed by a machine. 

This can be helpful in the following scenarios:

* Developers can search logs and correlate events, which is invaluable both during development as well as for troubleshooting production issues.
* Business teams can parse these logs and perform analysis over certain fields (for example, unique product count per day) by extracting and summarising these fields.
* You can build dashboards (both business and technical) by parsing the logs and performing aggregates over relevant fields.

Let’s use our earlier log statement and make a small change to make it structured.

```java
log.error("Exception in processing OrderId={} for ProductId={} due to Error={}", orderId, productId, ex.getResponseBodyAsString())
```

This will output a log in the following format:

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing OrderId=182726 for ProductId=21 due to Error=Product Not Available
```

Now this log message can be easily parsed by the machine by using “=” as a delimiter to extract the `OrderId`, `ProductId` and `Error` fields. We can now do an exact search over `ProductId=21` to accomplish our task.

This also allows us to perform more advanced analytics on the logs, such as preparing a report of all the orders that failed with such errors.

If you use a log management system like Splunk, the query `Error=”Product Not Available” | stats count by ProductId` can now produce the following result:

```
+-----------+-------+
| ProductId | count |
+-----------+-------+
| 21        | 5     |
| 27        | 12    |
+-----------+-------+
```

We could also use a JSON layout to print our logs in the JSON format:

```json
{  
    "timestamp":"2020-09-27T18:54:41,500+0530"  
    "level":"ERROR"  
    "class":"InventoryValidator"  
    "line":"13"  
    "OrderId":"182726"  
    "ProductId":"21"  
    "Error":"Product Not Available"
}
```

It’s important to understand the approach behind structured logging. There is no fixed standard and it can be done in many different ways.

# Conclusion

In this article, we saw the pitfalls of unstructured logging and the benefits and advantages offered by structured logging. 

Log management systems such as Splunk are hugely benefited by a well structured log message and can offer easy search and analytics on log events.

The biggest challenge however, when it comes to structured logging, is establishing a standard set of fields for your software. This can be achieved by following a custom logging model or centralised logging which ensures that all developers use the same fields in their log messages.

Thank you for staying with me so far. Hope you liked the article. You can connect with me on [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) where I regularly discuss technology and life. Also take a look at some of [my other articles](https://www.freecodecamp.org/news/author/theawesomenayak/). Happy reading. 🙂

