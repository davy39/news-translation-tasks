---
title: Node.js APIs on AWS — the pros and cons of Express versus Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T15:49:44.000Z'
originalURL: https://freecodecamp.org/news/node-js-apis-on-aws-the-pros-and-cons-of-express-versus-serverless-a370ab7eadd7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tgtdC3Ks4buR3XfITJMxsQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By William Woodhead

  Recently I have been playing around with Serverless + AWS lambda and I have to say,
  I have been awestruck.

  Over the past few years I have almost exclusively used Express and AWS EC2 (and
  more recently Docker) to build JavaScript R...'
---

By William Woodhead

Recently I have been playing around with [Serverless](https://serverless.com/) + AWS lambda and I have to say, I have been awestruck.

Over the past few years I have almost exclusively used [Express](http://expressjs.com/) and [AWS EC2](https://aws.amazon.com/ec2/) (and more recently [Docker](https://www.docker.com/)) to build JavaScript REST APIs.

This piece outlines the pros and cons of [Express](http://expressjs.com/) and [Serverless](https://serverless.com/) and explains why it made sense for our team at [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=serverless&utm_campaign=awareness) to switchover. This piece is aimed at tech teams looking to deploy and manage Node.js APIs on AWS (or similar).

![Image](https://cdn-media-1.freecodecamp.org/images/CxXXE330wof5O5qpQa2L0rh7AAzRduCQJbRt)
_Slightly aggressive collage of their logos. Apologies._

#### TL;DR

Switching from [Express](http://expressjs.com/) to [Serverless](https://serverless.com/) has completely transformed our delivery over the past 6 months.

**Pros:** reduced cost | out-of-the-box deployment scalability and monitoring | lightning-fast development.

**Cons**: loss of control | the enigmatic [Lambda](https://aws.amazon.com/lambda/) runtime | young ecosystem | no out-of-the-box zero-downtime deployment

#### What is Express | What is Serverless?

Express is a [Node.js](https://nodejs.org) package which, at its core, is a well-designed abstraction over the native Node.js http(s) module.

Serverless, on the other hand, is a toolkit that interacts with cloud platforms, such as AWS or [GCP](https://cloud.google.com/), to deploy and manage APIs.

From these descriptions, we can see that Express and Serverless are really very different — maybe too different to be compared. However the reason I _am_ comparing them is that both Express and Serverless can be used for writing Node.js APIs. So let’s jump into some comparisons:

#### The index file

In general, I prefer writing code to writing config. It means you can run, test, and debug your work.

With Express, your index file is JavaScript code. It is a really expressive declarative file. With Serverless, it’s yml config, I’m afraid.

Here’s the Express _Hello World_ index.js file:

```
const express = require('express');const handler = require('./handler');
```

```
const app = express();app.get('/hello-world', handler.helloWorld);app.listen(3000, () => console.log('Listening on port 3000'));
```

Here’s the Serverless _Hello World_ index.yml file:

```
service: hello-worldprovider:    name: aws    runtime: nodejs6.10functions:  helloWorld:    handler: handler.helloWorld    events:      - http:        path: hello-world        method: get
```

Pretty similar really, but I personally love the Express middleware-based approach. For me, it’s more readable and easier to test and debug.

#### Learning Curve

This is a tricky topic because it depends on what you are trying to achieve:

* If you are a Node.js hobbyist and you want to learn how to setup a localhost server on your own computer, Express is for you. Its a great package to experiment with, the “get started” documentation on the website is excellent, and you can easily start to play around with the intricacies of the Node.js event-based architecture.
* If you are trying to deploy and manage robust, scalable Node.js APIs, the learning curve is definately easier with Serverless. This is because Serverless deals with many of your complex cloud-based issues out-of-the-box. These include Deployment, Monitoring, and Infrastructure Provisioning to name just a few.

#### Operations — deploying, scaling, logging, monitoring…

![Image](https://cdn-media-1.freecodecamp.org/images/bJdnwDUal7mdHyigzm81e-f0nuD3CC0-usJE)
_Cogs to represent Operations, obviously._

This is where Serverless really comes into its own. Express is not designed to deal with all the complexities of cloud-based architectures by itself. If you use Express, you will need help from other packages:

For Deployment and Scaling you might use [Docker](https://www.docker.com/), [Kubernetes](https://kubernetes.io/), [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) or some other AWS services.

For Logging, Monitoring, and Error Handling, you might use [New Relic](https://newrelic.com/), [Datadog](https://www.datadoghq.com/), [Pingdom](https://www.pingdom.com/), and so on.

You get the idea. Express is a great low-level tool for building APIs, but you need to learn a bunch of other packages for your API to thrive in the modern cloud-based world. This is great if you want to configure your own architectures and have complete control.

With Serverless, you get so much out-of-the-box. Not from the Serverless package itself, but because Serverless can automatically interact with all the services in your Cloud Platform. For instance, just with the _Hello World_ index.yml example we saw above, you would get by default:

* Monitoring from AWS Lambda
* Logging from [AWS Cloudwatch](https://aws.amazon.com/cloudwatch/)
* Autoscaling from AWS Lambda
* Deployment from Serverless & [AWS Cloudformation](https://aws.amazon.com/cloudformation/)

This is absolutely incredible for fast moving tech teams who want to focus on writing application code, not on managing infrastructure.

_Please note: Currently with Serverless, we do not achieve zero-downtime deployment. I think it is possible to achieve with AWS CodeDeploy, but we currently just allow the API to go down for a second or so._

#### Cost

For anyone building robust, highly-available APIs on the cloud, cost is a massive consideration. Serverless has reduced our costs by an unbelieveable amount:

One T2-Medium EC2 Linux Machine on AWS costs you about $33 per month to run. We were using 3 of these machines before switching over to Serverless.

With Serverless + AWS Lambda, you get 1 million requests for free each month.

At Pilcro, we haven’t hit this benchmark yet so we have already saved ourselves over one hundred dollars a month. With Serverless and Lambda, **we can now run our APIs for free**.

#### The AWS Lambda runtime

![Image](https://cdn-media-1.freecodecamp.org/images/NKpXucW4pWZyIhbcklwDRHL8RUzTVVBJxZBz)
_AWS Lambda logo_

One of the downsides of using Serverless is that your API functions are run in the AWS Lambda runtime. This means you are never quite sure what is going on.

You also have to deal with certain oddities of the AWS Lambda function, like the funky _event_ and _context_ objects that are injected into your handlers:

```
function awsLambdaHandler(event, context, callback) {  ...}
```

```
function expressHandler(req, res, next) {  ...}
```

I much prefer the _req, res, next_ middleware pattern of Express. It seems more logical and understandable to me.

Another quirk is that for AWS Lambda to run your handlers, they need to be loaded into an execution context. This can take some time. Functions are cached in the execution context for a while, so often the first request to a Lambda will take more time than subsequent requests. This can be irritating if your API is used infrequently.

_Side note_: One of the great things about the AWS Node.js Lambda runtime is that they have the [ImageMagick](https://www.imagemagick.org) binary installed. So you can do image manipulation in your Lambda functions out of the box!

#### Conclusion

This isn’t really a comparison between Express and Serverless. It’s an acknowledgement that — in the pursuit of robust, scalable cloud APIs — packages like Serverless are offering so much out-of-the-box, that continuing to use Express (alongside other tools) feels like a lot of hard work and learning.

At [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=serverless&utm_campaign=awareness), our APIs are pretty simple and standard. They are comprised of simple REST requests and a few complex image manipulation functions.

Because our APIs are so straightfoward, the decision to use Serverless and Lambda was simple — our main drivers were **cost**, **scalability**, and **development speed.**

**Cost** because … cost.

**Scalability** because we are built on top of G-Suite, so we needed to be able to scale extremely quickly and effectively.

**Development speed** because we needed to deliver Pilcro in 6 months with a small tech team.

Serverless has given us these three benefits, which has completely transformed our delivery over the past 6 months. The ecosystem of Serverless is still young, so there will likely be a lot of development in this space over the next 12 months.

#### Steps to help you decide whether to use Serverless

1. How complex are your APIs? Do you need the low-level configuration and closeness that you get from using Express?
2. How do you currently manage Deployment, Scaling, and Monitoring? Are you happy with your solution? How quickly could a newly hired developer learn all the different parts of your architecture?
3. Could you save any money by switching to Serverless?

_If you liked this story, please ? and please share with others. Also please check out my company p[ilcro.com.](https://www.pilcro.com/?utm_source=medium&utm_medium=serverless&utm_campaign=awareness) Pilcro is brand software for G-Suite — for marketers and brand agencies._

