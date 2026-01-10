---
title: How to schedule ad-hoc tasks with DynamoDB TTL and Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T00:43:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-schedule-ad-hoc-tasks-with-dynamodb-ttl-and-lambda-421fa5778993
coverImage: https://cdn-media-1.freecodecamp.org/images/0*C_kNu0DfEkRCWkxf.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Yan Cui

  CloudWatch Events let you easily create cron jobs with Lambda. However, it’s not
  designed for running lots of ad-hoc tasks, each to be executed once, at a specific
  time. The default limit on CloudWatch Events is a lowly 100 rules per regio...'
---

By Yan Cui

[CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) let you easily create cron jobs with Lambda. However, it’s not designed for running lots of ad-hoc tasks, each to be executed once, at a specific time. The default limit on CloudWatch Events is a lowly [100 rules per region per account](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/cloudwatch_limits_cwe.html). It’s a soft limit, so it’s possible to request a limit increase. But the low initial limit suggests it’s not designed for use cases where you need to schedule **millions of ad-hoc tasks**.

**CloudWatch Events is designed for executing recurring tasks.**

![Image](https://cdn-media-1.freecodecamp.org/images/lqXGe3MgGpO8atm0UG35G8t3X6-nO0-IwKVU)
_[https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/cloudwatch_limits_cwe.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/cloudwatch_limits_cwe.html" rel="noopener" target="_blank" title=")_

### The Problem

It’s possible to do this in just about every programming language. For example, .Net has the `[Timer](https://docs.microsoft.com/en-us/dotnet/api/system.timers.timer?view=netframework-4.7.2)` class and JavaScript has the `[setInterval](https://www.w3schools.com/jsref/met_win_setinterval.asp)` function. But I often find myself wanting a service abstraction to work with. There are many use cases for such a service, for example:

* A tournament system for games would need to execute business logic when the tournament starts and finishes.
* An event system (think [eventbrite.com](https://www.eventbrite.com/) or [meetup.com](https://meetup.com/)) would need a mechanism to send out timely reminders to attendees.
* A to-do tracker (think [wunderlist](https://www.wunderlist.com/)) would need a mechanism to send out reminders when a to-do task is due.

However, AWS does not offer a service for this type of workloads. CloudWatch Events is the closest thing, but as discussed above it’s not intended for the use cases above. You can, however, implement them using cron jobs. But such implementations have other challenges.

I have implemented such service abstraction a few times in my career already. I experimented with a number of different approaches:

* cron job (with CloudWatch Events)
* wrapping the .Net `Timer` class as an HTTP endpoint
* using SQS Visibility Timeout to hide tasks until they’re due

And lately, I have seen a number of folks use [DynamoDB Time-To-Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html) (TTL) to implement these ad-hoc tasks. In this post, we will take a look at this approach and see where it might be applicable for you.

### How do we measure the approach?

For this type of ad-hoc task, we normally care about:

* **Precision**: how close to my scheduled time is the task executed? The closer the better.
* **Scale (number of open tasks)**: can the solution scale to support many open tasks, i.e. tasks that are scheduled but not yet executed?
* **Scale (hotspots):** can the solution scale to execute many tasks around the same time? E.g. millions of people set a timer to remind themselves to watch the Superbowl, so all the timers fire within close proximity to kickoff time.

### DynamoDB TTL as a scheduling mechanism

From a high level, this approach looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/4P77Vvmy5ZDOynG2ImgXBdbaEfRKfOmy1fpE)

* A `scheduled_items` DynamoDB table which holds all the tasks that are scheduled for execution.
* A `scheduler` function that writes the scheduled task into the `scheduled_items` table, with the TTL set to the scheduled execution time.
* An `execute-on-schedule` function that subscribes to the DynamoDB Stream for `scheduled_items` and reacts to `REMOVE` events. These events correspond to when items have been deleted from the table.

#### Scalability (number of open tasks)

Since the number of open tasks just translates to the number of items in the `scheduled_items` table, this approach can scale to millions of open tasks.

DynamoDB can handle large throughputs (thousands of TPS) too. So this approach can also be applied to scenarios where thousands of items are scheduled per second.

#### Scalability (hotspots)

When many items are deleted at the same time, they are simply queued in the DynamoDB Stream. AWS also auto scales the number of shards in the stream, so as throughput increases the number of shards would go up accordingly.

But, events are processed in sequence. So it can take some time for your function to process the event depending on:

* its position in the stream, and
* how long it takes to process each event.

So, while this approach can scale to support many tasks all expiring at the same time, it cannot guarantee that tasks are executed on time.

#### Precision

This is a big question about this approach. According to the official [documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html), expired items are deleted **within 48 hours**. That is a huge margin of error!

![Image](https://cdn-media-1.freecodecamp.org/images/uubpqNjDRYU8sQFNzf3l6sYT9bUvnVqHWmvx)

As an experiment, I set up a Step Functions state machine to:

1. add a configurable number of items to the `scheduled_items` table, with TTL expiring between 1 and 10 mins
2. track the time the task is scheduled for and when it’s actually picked up by the `execute-on-schedule` function
3. wait for all the items to be deleted

The state machine looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/DZ7zKEkjn26InqsMwDg8qkDXTlcE75FasIcr)

I performed several runs of tests. The results are consistent regardless of the number of items in the table. A quick glimpse at the table tells you that, on average, a task is executed over **11 mins** AFTER its scheduled time.

![Image](https://cdn-media-1.freecodecamp.org/images/maU40YnAni5P0wmpbSHHucooNaZLzI17Txxx)
_US-EAST-1_

I repeated the experiments in several other AWS regions:

![Image](https://cdn-media-1.freecodecamp.org/images/DLYm48ZBEoFPqNuTmfF6CgSs8uWbf5DnFU76)

I don’t know why there is such a marked difference between US-EAST-1 and the other regions. One explanation is that the TTL process requires a bit of time to kick in after a table is created. Since I was developing against the US-EAST-1 region initially, its TTL process has been “warmed” compared to the other regions.

### Conclusions

Based on the result of my experiment, it will appear that using DynamoDB TTL as a scheduling mechanism cannot guarantee a reasonable precision.

On the one hand, the approach scales very well. But on the other, the scheduled tasks are executed at least several minutes behind, which renders it unsuitable for many use cases.

