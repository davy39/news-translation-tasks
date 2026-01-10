---
title: Serverless has its pitfalls. Here’s how you can avoid them.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-27T06:24:41.000Z'
originalURL: https://freecodecamp.org/news/the-serverless-series-mistakes-you-should-avoid-9ec1ca6b9dff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hyAp4Q0OPmp-wOaeSqA7nA.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nicolas Dao

  In this post, I will share the lessons I learned over the past year while using
  Serverless to build mobile and web apps for a tech consultancy in Sydney. For each
  drawback, I will also recommend one or multiple solutions.

  1. FaaS - Con...'
---

By Nicolas Dao

In this post, I will share the lessons I learned over the past year while using Serverless to [build mobile and web apps for a tech consultancy in Sydney](https://neap.co/). For each drawback, I will also recommend one or multiple solutions.

#### 1. FaaS - Connection Pooling Limitation

FaaS conversations do not mention this limitation very often. Cloud providers market FaaS as a solution that could infinitely scale. While this may apply to the function itself, most of the resources that your function depends upon won’t be infinitely scalable.

The number of concurrent connections that your relational database supports is one of those limited resources. The unfriendliness of FaaS towards [connection pooling](https://en.wikipedia.org/wiki/Connection_pool) is what makes this problem such a big deal.

Indeed, as I mentioned before, each instance of your function lives in its isolated stateless environment. That means that when it connects to a relational database (for example PostgreSQL, MySQL, Oracle), it should most probably use a connection pool to avoid reconnecting back and forth with your DB.

Your relational database can only manage a certain amount of concurrent connections (usually the default is 20). Spawning more than 20 instances of your function will quickly exhaust your database connections, preventing other systems from accessing it.

For that reason, I recommend avoiding any FaaS if your function needs to communicate with a relational DB using a connection pool. If you need to use a connection pool, then a few options are available:

* Use a BaaS instead.
* Some relational database like PostgreSQL offers plugins that can solve this problem by [multiplexing the number of available concurrent connections](https://blog.zappa.io/posts/multiplex-rds-connections).

#### 2. FaaS - No Support For WebSockets

This one is kind of obvious. But for those who think they can have the cake and eat it too, you can’t hope to maintain a WebSocket on a system that is by design ephemeral. If you’re looking for a Serverless WebSocket, then you’d need to use a BaaS like Zeit Now instead.

Alternatively, if you’re attempting to create a Serverless GraphQL API, then it is possible to use Subscriptions (which relies on WebSockets) by using [AWS AppSync](https://aws.amazon.com/appsync/). A great article that explains this use case in greater detail is [Running a scalable & reliable GraphQL endpoint with Serverless](https://hackernoon.com/running-a-scalable-reliable-graphql-endpoint-with-serverless-db16e42dc266).

#### 3. FaaS — Cold Start

FaaS solutions like [AWS Lambda](https://aws.amazon.com/lambda) have demonstrated huge gains when solving Map-Reduce challenges (for example, [Leveraging AWS Lambda for Image Compression at Scale](https://medium.com/squad-engineering/leveraging-aws-lambda-for-image-compression-at-scale-a01afd756a12)). However, if you’re trying to provide a fast response to events like HTTP requests, you’ll need to take into account the time required by the function to warm up.

Your function lives inside a virtual environment that needs to be spawned to scale up based on the traffic it receives (something you naturally do not control). This spawning process takes a few seconds, and after your function idles due to low traffic, it will need to be spawned again.

I learned that at my expense when deploying a relatively complex reporting REST API on Google Cloud Functions. That API was part of a microservice refactoring effort to break down our big monolithic web API. I started with a low-traffic endpoint, which meant that function was often in an idle state. The reports that were powered by that microservice became slow the first time they were accessed.

To fix that issue, I moved our microservice from Google Cloud Function (FaaS) to Zeit Now (BaaS). That migration allowed me to keep at least one instance up all the time (more about Zeit Now in my next post: Why We Love Zeit Now & When To Use It Over FaaS).

#### 4. FaaS - Long-Lived Processes, Don’t Bother!

AWS Lambda and Google Cloud Functions can run no longer than 5 and 9 minutes, respectively. If your business logic is a long-running task, you will have to move to a BaaS like Zeit Now instead.

For more details on FaaS limitations, please refer to [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) and [Google Cloud Functions quotas](https://cloud.google.com/functions/quotas).

#### 5. BaaS & FaaS - Loosing Infrastructure Control

If your product requirements necessitate some degree of control over your infrastructure, then Serverless will most likely leave you up the creek. Example of such problems could be:

* Microservices deployment orchestration. Ending up with a myriad of Serverless microservices will quickly become a deployment nightmare, especially if they need to be versioned altogether or by domain.
* Controlling the lifecycle of each server to save on costs.
* Having long-running tasks on multiple servers.
* Controlling the exact version of the underlying server OS, or installing specific libraries required by your app.
* Controlling exact geo-replication of your app or data to ensure consistent and fast performances globally (there are ways to overcome this in some scenarios. Check out [Build a serverless multi-region, active-active backend solution in an hour](https://read.acloud.guru/building-a-serverless-multi-region-active-active-backend-36f28bed4ecf)).

Serverless may fall short in all the above use cases. However, as I’ve discussed before, Serverless is just an extension of PaaS. To keep as much focus as possible on writing code rather than worrying too much about the underlying infrastructure scalability and reliability, leveraging the latest PaaS containerization strategies such as [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) can get you very close to what Serverless has to offer.

#### 6. BaaS & FaaS - Compliance & Security

Serverless shares all the usual complaints related to the cloud. You are giving up control of your infrastructure to one or multiple third parties. Depending on the vendor, Serverless may or may not provide the right SLA and security levels for your business case.

Whether Serverless a go or no-go from a compliance and security point of view really depends on your particular case. Many articles discuss this topic in great details (like [The state of serverless security](https://read.acloud.guru/the-state-of-serverless-security-fall-2017-fb2b8936044f)).

### Conclusion

Serverless is not a silver bullet. The gains you can obtain from it depend on your knowledge of it. The good part is that the barrier to entry is so low that you should be proficient in no time.

### COMING NEXT…

Of course, Serverless has limitations. All technical solutions have them. The question now is how we overcome them. In my next post, I’ll write about suggestions my team and I developed to deal with those limitations: “Why We Love Zeit Now & When To Use It Over FaaS”.

Follow me on Medium - [Nicolas Dao](https://www.freecodecamp.org/news/the-serverless-series-mistakes-you-should-avoid-9ec1ca6b9dff/undefined) - if you’re interested in what’s coming next:

Current posts in this serverless series:

* [Do You Really Know What Serverless Is?](https://hackernoon.com/the-serverless-series-what-is-serverless-d651fbacf3f4)
* [The Impact of Serverless On Tech Leadership](https://hackernoon.com/the-serverless-series-automating-it-engineers-reshaping-tech-leadership-788cf9b625d5)
* [How Serverless Is Automating IT Engineers](https://hackernoon.com/the-serverless-series-automating-it-engineers-reshaping-tech-leadership-788cf9b625d5)

Future posts in the series:

* Why We Love [Zeit Now](https://zeit.co/now) & When To Use It Over FaaS
* Serverless Event-Driven Architecture: The Natural Fit
* How To Manage Back-Pressure With Serverless?
* GraphQL on Serverless In Less Than 2 Minutes

