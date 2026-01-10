---
title: How to Use Metrics to Monitor Your Microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-30T16:49:38.000Z'
originalURL: https://freecodecamp.org/news/microservice-observability-metrics
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/Microservice-Observability---Metrics.png
tags:
- name: error handling
  slug: error-handling
- name: logging
  slug: logging
- name: metrics
  slug: metrics
- name: Microservices
  slug: microservices
seo_title: null
seo_desc: "By Siben Nayak\nIn my previous article, I talked about the importance of\
  \ logs and the differences between structured and unstructured logging. \nLogs are\
  \ easy to integrate into your application, and they give you the ability to represent\
  \ any type of da..."
---

By Siben Nayak

In my previous [article](https://www.freecodecamp.org/news/how-to-handle-logs-in-microservices/), I talked about the importance of logs and the differences between structured and unstructured logging. 

Logs are easy to integrate into your application, and they give you the ability to represent any type of data in the form of strings.

Metrics, on the other hand, are numerical representations of data. These are often used to count or measure a value and are aggregated over a period of time. 

Metrics give us insights into the historical and current state of a system. Since they are just numbers, we can also use them to perform statistical analysis and predictions about the system’s future behaviour. 

You can also use metrics to trigger alerts and notify you about issues in the system’s behaviour.

# Logs vs. Metrics

## How Logs and Metrics are Formatted

Logs are represented as strings. They can be simple text, JSON payloads, or key-value pairs (like we discussed in structured logging).

A typical log entry looks like this:

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in fetching product information - Product Not Available
```

Metrics are represented as numbers. They measure something (like CPU usage, number of errors, and so on) and are numeric in nature.

A typical metric looks like this:

```
{class=InventoryValidator, exception=Product Not Available, timestamp=1609306200}
```

## The Resolution of Logs and Metrics

Logs contain high-resolution data. This includes complete information about an event and can be used to correlate the flow (or path) that the event took through the system. 

In case of errors, logs contain the entire stack trace of the exception, which allows us to view and debug issues originating from downstream systems as well. 

![Image](https://www.freecodecamp.org/news/content/images/2020/12/android-stack-trace-error-2.png)
_A log entry showing the stacktrace of an error_

In short, logs can tell you _what happened_ in the system at a certain time.

Metrics contain low-resolution data. This may include a count of parameters (such as requests, errors, and so on) and measures of resources (such as CPU and memory utilization). 

![Image](https://www.freecodecamp.org/news/content/images/2020/12/tracing_aggregated_red_metrics.png)
_A Metric showing number of hits to a service_

In short, metrics can give you _a count of something that happened_ in the system at a certain time.

## The Cost of Logs and Metrics

Logs are expensive to store. The storage overhead of logs also increases over time and is directly proportional to the increase in traffic.

Metrics have a constant storage overhead. The cost of storage and retrieval of metrics does not increase too much with the increase in traffic. It is, however, dependent on the number of variables we emit with each metric.

# Cardinality of Metrics

Metrics are identified by two key pieces of information:

* A metric name
* A set of key-value pairs called tags or labels

A permutation of these values provides the metric its cardinality. For example, if we are measuring the CPU utilization of a system with three hosts, the metric has a cardinality value of 3 and can have the following three values:

```
(name=pod.cpu.utilization, host=A)
(name=pod.cpu.utilization, host=B)
(name=pod.cpu.utilization, host=C)
```

Similarly, if we introduced another tag in the metric that determined the AWS region of the hosts (say, `us-west-1` and `us-west-2`), we would now have a metric with a cardinality value of 6.

# Types of Metrics

## Golden signals

Golden signals are an effective way of monitoring the overall state of the system and identifying problems.

* **Availability:** State of your system measured from the perspective of clients (for example, the percentage of errors on total requests).
* **Health:** State of your system measured using periodic pings.
* **Request Rate:** Rate of incoming requests to the system.
* **Saturation:** How free or loaded the system is (foe example, the queue depth or available memory).
* **Utilization:** How busy the system is (for example, CPU load or memory usage). This is represented as a percentage.
* **Error Rate:** Rate of errors being produced in the system.
* **Latency:** Response time of the system, usually measured in the 95th or 99th percentile.

## Resource metrics

Resource metrics are almost always made available by default from the infrastructure provider (AWS CloudWatch or Kubernetes metrics) and are used to monitor infrastructure health.

* **CPU/Memory Utilization:** Usage of the system’s core resources.
* **Host Count:** Number of hosts/pods that are running your system (used to detect availability issues due to pod crashes).
* **Live Threads:** Threads spawned in your service (used to detect issues in multi-threading).
* **Heap Usage:** Heap memory usage statistics (can help debug memory leaks).

## Business metrics

Business metrics can be used to monitor granular interaction with core APIs or functionality in your services.

* **Request Rate:** Rate of requests to the APIs.
* **Error Rate:** Rate of errors being thrown by the APIs.
* **Latency:** Time taken to process requests by the APIs.

# Dashboards and Alerts for Metrics

Since metrics are stored in a time-series database, it’s more efficient and reliable to run queries against them for measuring the state of the system.

You can use these queries to build dashboards for representing the historical state of the system.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-03-at-3.20.16-PM.png)
_A Wavefront dashboard with some important metrics_

They can also be used to trigger alerts when there is an issue with the system (like an increase in the number of errors observed or a sudden spike in CPU utilization).

Due to their numeric nature, we can also create complex mathematical queries (such as X% of errors in last Y minutes) to monitor system health.

The biggest challenge, however, in handling metrics is deciding the right amount of cardinality that makes the metric useful while also keeping its costs under control. 

Emitting too many metrics, or metrics with too many dimensions, can lead to an increase in storage and processing costs. You need to choose the minimum cardinality that is just enough to give a high level picture about the system.

# How to Use Logs and Metrics 

Both logs and metrics have their own pros and cons. However, in any production system, we need to use both logs and metrics together to effectively monitor the system and debug any issues.

Metrics are often the first line of sight into the health of a system. Let's take the example of an e-commerce application like Amazon. The most important metric for such a use-case is the total number of successful and failed orders. 

On a normal day, the metric for number of failed orders would remain at zero or some very small number. If there is an issue in the system that causes orders to suddenly start failing, this metric will show an increase in count.

You can create an _alert_ on a combination of two metrics - total orders and failed orders. This will allow you to send a notification when the percentage of failed orders increases beyond a certain threshold (say 5%).

Once you are notified about the failing orders, you can then refer to the logs to find the cause of the failures. The logs would contain the error messages leading to the failure, as well as the detailed stacktrace that can identify the root cause of the failure.

# Conclusion

In this article, we saw the differences between metrics and logs, and how metrics can help us monitor the health of our system more efficiently. Metrics can also be used to create dashboards and alerts using monitoring software like Wavefront and Grafana.

It is also necessary to use both metrics and logs in coordination to accurately detect and debug issues.

Thank you for staying with me so far. Hope you liked the article. You can connect with me on [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) where I regularly discuss technology and life. Also take a look at some of my other articles on [Medium](https://medium.com/@theawesomenayak). Happy reading 🙂

