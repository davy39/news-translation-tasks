---
title: How we serve 25M API calls from 10 scalable global endpoints for $150 a month
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T13:31:19.000Z'
originalURL: https://freecodecamp.org/news/how-we-serve-25m-api-calls-from-10-scalable-global-endpoints-for-150-a-month-911002703280
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I-GPwGqtRcyciHkXjIsMLw.jpeg
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: software
  slug: software
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By Jonathan Kosgei

  I woke up on Black Friday last year to a barrage of emails from users reporting
  503 errors from the ipdata API.

  Our users typically call our API on each page request on their websites to geolocate
  their users and localize their con...'
---

By Jonathan Kosgei

I woke up on Black Friday last year to a barrage of emails from users reporting 503 errors from the [ipdata](https://ipdata.co/?utm_campaign=how-we-serve-25M-calls&utm_medium=freecodecamp-post&utm_source=medium) API.

Our users typically call our API on each page request on their websites to geolocate their users and localize their content. So this particular failure was directly impacting our users’ websites on the biggest sales day of the year.

I only lost one user that day but I came close to losing many more.

This sequence of events and their inexplicable nature - CPU, memory and I/O were nowhere near capacity. As well as concerns on how well (if at all) we would scale, given our outage, were a big wake up call to rethink our existing infrastructure.

## Our Tech Stack At The Time

![Image](https://cdn-media-1.freecodecamp.org/images/rqzWDcdQF8izmRhxYtIyeJF0PATKA2yddmv5)

* Japronto Python Framework
* Redis
* AWS EC2 nodes
* AWS Elastic Loadbalancers
* Route53 Latency Based Routing

I had run tests on several new, promising Python micro-frameworks.

Choosing between aiohttp, sanic and japronto I settled on [Japronto](https://medium.freecodecamp.org/million-requests-per-second-with-python-95c137af319) after benchmarking the 3 using [https://github.com/samuelcolvin/aiohttp-vs-sanic-vs-japronto](https://github.com/samuelcolvin/aiohttp-vs-sanic-vs-japronto) and finding it to have the highest throughput.

The API ran on 3 EC2 nodes in 3 regions behind ELB loadbalancers with Route53 latency based routing to route requests to the region closest to the user to ensure low latency.

## Choosing A New Tech Stack

![Image](https://cdn-media-1.freecodecamp.org/images/diPMaejoDxpsKkQxbBsp8J5orTLZn6CIsawU)
_An Example Weather API using our current stack_

Around this time I started to seriously look into using API Gateway with AWS Lambda given their:

1. Favorable pricing - about $3.50 per million on API Gateway and $0.20 per million for AWS Lambda.
2. Infinite scale and high throughput - the account limit on API Gateway is 10,000 requests per second or about 864M calls daily. A limit that is possible to lift by opening a support request.

This also made it economically viable to have endpoints in numerous AWS regions to provide low latencies to all our users all over the globe.

## Designing A Multi-Regional API Gateway Based API

There were a number of architectural challenges that had be solved to make this viable.

1. Each Lambda function in each region needed to be able to lookup usage data in a database in the same region to minimize latency
2. I needed to figure out a way to determine the number of API calls made by each IP Address, Referer and API Key.
3. A means to sync the usage data in all regions. For example, if Route53 sent 10,000 requests to our Sydney endpoint then decided to send the next 50,000 to our Seoul endpoint (depending on which endpoint had the least network latency at that point in time). Each lambda function would need to know that the user had made 60,000 requests in total to properly handle rate limiting.
4. Authorization - API Gateway provides usage plans and API key generation and allows you to link an API key to a usage plan. With the added advantage that you don’t get charged for requests users make beyond their quotas. However I couldn’t use this because it was important to me to provide a no sign-up, no credit card free tier.

With quite a bit of work, I was able to solve these problems in creative ways.

## Accessing The Usage Data Locally (For Each Lambda Function)

The obvious solution for this was to use DynamoDB, it was cost effective at scale, fast and the first 200M requests per month were free.

DynamoDB also provided consistently low read latencies of 1 - 2 ms.

![Image](https://cdn-media-1.freecodecamp.org/images/dwE0L8p8fjQekAXNod7CLuJ9bnFSOhnNmy7I)

And this can be sped up into the microsecond range with [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/) (DAX).

> DAX takes performance to the next level with response times in microseconds and provides millions of requests per second for read-heavy workloads.

## Collecting Usage Data For All Identifiers

The next challenge was how to count in real time the number of requests made per IP address, Referer or API key.

The simplest most direct way to do this would be to update a count in a DynamoDB table on each call.

However this would introduce database writes on each call to our API, potentially introducing significant latency.

I was able to find a simple and elegant solution to this:

1. First, print a log (a JSON object) with all the request identifiers on each request. That is the IP address, Referer and API key if present. Really just;

```
print(event)
```

1. Add a [Cloudwatch Subscription Filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html) to the Cloudwatch Log Stream of each Lambda function in each region and push all the logs into a Kinesis stream. This would allow me to process log events from every region in a central place. I chose Kinesis over SQS (Amazon’s Simple Queue Service) because of the ability to play back events. SQS deletes the event as soon as a consumer reads it. And I wanted the ability to be able to recover from node failures and data loss.
2. Read from the Kinesis stream and update a [Local DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) instance with the usage data
3. Use the [DynamoDB Cross Regional Replication Library](https://github.com/awslabs/dynamodb-cross-region-library) to stream all changes from my local DynamoDB instance to all the tables in all regions in real time.

## Authenticating Requests

I handle this by replicating keys to every region on signup, so that no matter what endpoint a user hits, the Lambda function they hit can verify their key by checking the local DynamoDB table within the same region within a millisecond. This also stores the user’s plan quota and can in a single read verify the key and if it exists get the plan quota to compare usage against and determine whether to accept or reject the request.

## How This Has Fared

Today we serve 25M API calls monthly, about 1M calls daily.

Majority of them in under 30ms, providing the fastest IP Geolocation Lookup over SSL in the industry.

#### [Hyperping.io](https://hyperping.io/)

![Image](https://cdn-media-1.freecodecamp.org/images/D4hfVJDYxsX8O2rz5B-67wN3QE-w-ExvS2eh)

### [Our Status Page](https://status.ipdata.co)

![Image](https://cdn-media-1.freecodecamp.org/images/OqGMUdPHAQIKxH7SlYTFMu3g9yGCoTBrQ5yg)

Latency is pretty much the biggest reason developers shy from using third party APIs for GeoIP lookups.

However our low latencies and redundant global infrastructure are slowly drawing large businesses to our service.

## Costs

![Image](https://cdn-media-1.freecodecamp.org/images/yqRZHcP929fjBeROjup4i1SIQbStNx3GQBNd)
_A breakdown of our costs_

## Lessons

1. CloudWatch can be surprisingly costly - and not log storage. We only store CloudWatch logs for 24hrs. Alarms, metrics and CloudWatch requests can really add up.
2. On API Gateway the more requests you get the lower your latencies will be due to fewer cold starts, because of this I’ve seen latencies as low as 17ms in our busiest region (Frankfurt) to 40ms in our less busy regions such as Sydney.
3. DynamoDB is fast and will cost you less than you think (or maybe not). Have a look at [https://segment.com/blog/the-million-dollar-eng-problem/](https://segment.com/blog/the-million-dollar-eng-problem/). I initially thought I’d get charged per the number of read capacity units (RCUs) and write capacity units (WCUs) I’d provision. However billing seems to be only per usage, so if you provision 1000 RCUs and 1000 WCUs but only use 5 RCUs and WCUs you’ll only get charged for your usage. This aspect of DynamoDB pricing was a bit tough to wrap my head around at the beginning.
4. Increasing your Lambda RAM can halve your execution time and make response times more consistent (as well as double your costs!)
5. Kinesis has proven to be very reliable under high throughput. Relaying all our log events for processing in near real time.
6. Local DynamoDB is only limited by your system resources, which makes it great for running table scans or queries (for example when generating reports) that would otherwise be expensive to do on AWS’s DynamoDB. Keep in mind that Local DynamoDB is really just Dynamo wrappings around SQLite. ? It’s useful and convenient for our use case but might not be so for you.

## Notes

* AWS announced DynamoDB Global tables at Re:invent last year which syncs all writes in all tables - across regions - to each other. We’re currently not moving to this as it’s only available in 5 regions.
* Amazon also introduced Custom Authorizers of the `REQUEST` type in Amazon API Gateway. This would potentially allow you to rate limit by IP Address as well as any header, query or path parameter.

Read about more real life architectures on the [highscalability.com](http://highscalability.com) blog.

#### **Update:**

Checkout our detailed analysis of 8 of [the best IP Geolocation APIs](https://medium.com/@ipdata_co/what-is-the-best-commercial-ip-geolocation-api-d8195cda7027).

