---
title: 'Webtask Backend-as-a-Service: Quick Serverless Tutorial'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-02T19:04:00.000Z'
originalURL: https://freecodecamp.org/news/webtask-backend-as-a-service-quick-serverless-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca977740569d1a4ca84d3.jpg
tags: []
seo_title: null
seo_desc: 'By Charles Ouellet

  The word serverless is buzzing through dozens of dev circles today.

  It has been for a while now.

  I’ve been meaning to exit my code editor and come talk about the trend here. Especially
  since I discovered Webtask, a few months ago.

  ...'
---

### By Charles Ouellet

The word **serverless** is buzzing through dozens of dev circles today.

It has been for a while now.

I’ve been meaning to exit my code editor and come talk about the trend here. Especially since I discovered [Webtask](https://webtask.io/), a few months ago.

So, in between bug fixes, support & new features, I finally took some time to sit down and write a little.

In this post, I’ll touch on serverless architectures and Backend as a Service tools a bit. But I’ll mostly focus on offering a simple yet meaningful serverless e-commerce tutorial. And I’ll use our own HTML/JS shopping cart platform & Webtask to do so.

## What is a serverless architecture, and why should you care?

Like [the “JAMstack”](https://snipcart.com/blog/jamstack-clients-static-site-cms), **serverless architecture** is a new web development trend subscribing to the “rise of the frontend” paradigm we’re in. In layman’s terms, it’s a way to run server-side code in the cloud without worrying about web servers, routing, etc. It relies heavily on **Backend as a Service (Baas)** third parties such as Webtask, or the most popular kid on the block: [AWS Lambda](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html). With these BaaS services, you just write code and let them take care of all the underlying infrastructure. Scaling-wise, such an approach is quite awesome: the abstraction layer these services offer can handle peaks of traffic on your site wonderfully.

As you may know, we’re big fans of [the JAMstack](http://jamstack.org/) (JavaScript, APIs & Markup) here at Snipcart. It’s another vibrant expression of the “rise of the frontend” paradigm I mentioned. We’ve written whole tutorials on how to run e-commerce with static site generators such as [Jekyll](https://snipcart.com/blog/static-site-e-commerce-part-2-integrating-snipcart-with-jekyll) or [Hugo](https://snipcart.com/blog/hugo-tutorial-static-site-ecommerce), and even with [API-first CMS like Contentful](https://www.contentful.com/blog/2016/02/10/snipcart-middleman-contentful/). From cost to tech stacks shifts, I believe such an approach will deeply impact how businesses handle web development in the next years.

However, I’m aware that it has its limits: a modern static site is **raw content**, which means using dynamic features such as webhooks would be impossible without _some_ server-side code. That’s where Webtask comes in.

## Webtask: Backend-as-as-Service for Targeted Tasks (or FaaS)

Webtask is a neat service crafted by [Auth0](https://auth0.com/), the good folks who made a serious dent in the online authentication world. Acting as a Function as a Service, it basically removes the need to configure a backend for simple mobile or single-page apps. Often [compared to AWS Lambda](http://thenewstack.io/often-choose-webtask-lambda/), it allows developers to write server-side logic & functions executed via HTTP calls. So it’s one of the best Backend as a Service tools out there for developers who’d rather focus on the frontend than configure the backend.

Now let’s see how perfect it is for the use case we’ll explore in this serverless tutorial.

## Serverless e-commerce tutorial: webhooks & custom shipping rates

At Snipcart, I believe one of our most powerful features is [the Webhooks Shipping API](https://docs.snipcart.com/configuration/shipping-providers#webhooks-shipping-api). Simply put, it gives you full control on how your e-commerce site handles shipping.

However, leveraging this feature requires running server-side code. So if you wanted to use a JAMstack set up with a static site generator, you’d be screwed. Thanks to Webtask, however, you’re not! In this serverless tutorial, we’ll use it to host the e-commerce shipping function we need directly via their platform.

## Our simple serverless e-commerce use case

Now, let’s pretend we have a static e-commerce site running with Snipcart.

And let’s say we want to offer three special shipping rates:

* One for customers in our Québec hometown
* One for US customers
* One for all other international customers

## 1. How to create the Webtask function

First of all, let me explain a little how our shipping API works. Snipcart sends all the order details to a URL you can specify in your merchant dashboard. Using this data, you can then write code to return available shipping rates to your end customers.

**Start by creating an account on** [**https://webtask.io/.**](https://webtask.io/) **Once it’s done, follow their steps to install the Webtask CLI via** `**npm**`**.**

We’ll now create a file named `shipping_task.js`. It'll contain all the code needed to parse the order details received from Snipcart and return the available shipping rates.

Let’s start by exporting a module that Webtask will understand.

```javascript
module.exports = function (context, cb) {
    cb(null, context.body);
}
```

The first parameter, context, contains the data Snipcart will send to your application. Webtask takes care of parsing the JSON, and you can access all the event details along with the order via context.body.

With the code above, our task would return the request body that it received; pretty useless. ;)

Now let’s say we want to offer free shipping for customers in Québec.

```javascript
module.exports = function (context, cb) {
    var orderDetails = context.body.content;
    var rates = [];
    
    var address = orderDetails.shippingAddress || order.billingAddress;
    
    if (address.country == "CA" && address.province == "QC") {
      rates.push({
        cost: 0,
        description: "Free shipping for Québec residents!"
      });
    }
    
    cb(null, { rates: rates });
}
```

Ain’t that nice? However, with this code, customers outside Québec won’t have any shipping options. So we’ll make sure to return a standard shipping rate in case the order does not match our conditions:

```javascript
if (rates.length === 0) {
  rates.push({
    cost: 20,
    description: "Standard shipping"
  });  
}
```

You can see below the complete code with some additional conditions:

```javascript
module.exports = function (context, cb) {
    console.log(context.body);

    var orderDetails = context.body.content;

    var rates = [];

    var address = orderDetails.shippingAddress || order.billingAddress;

    if (address.country == "CA" && address.province == "QC") {
      rates.push({
        cost: 0,
        description: "Free shipping for Québec residents!"
      });
    }

    if (address.country == "CA" && address.province != "QC") {
      rates.push({
        cost: 10,
        description: "Shipping to Canada"
      });
    }

    if (address.country == "US") {
      rates.push({
        cost: 15,
        description: "Shipping to US"
      });
    }

    if (rates.length === 0) {
      rates.push({
        cost: 20,
        description: "Standard shipping"
      });
    }

    cb(null, { rates: rates });
}
```

Webtask will then generate a URL; you should see it in your terminal.

Simply use this URL and when configuring the Webhooks Shipping API.

#### 2. Securing the serverless component

With our current set up, anyone could send requests to this API, right? That’s not something we want. So we’ll make sure that the function only handles requests coming from Snipcart. We’ll use our request validation API to do so.

First, we’ll need to send a Snipcart secret API key to the task in order to call the request validation API. We don’t want to expose it directly through the code, so we’re going to use the `secrets` feature that Webtask has. It allows us to pass secret parameters to the task that will be encrypted and accessible via the `context` object.

When creating the task, I added the `--secret` switch:

```javascript
wt create shipping_task.js — secret snipcartApiKey=MY_SECRET_API_KEY
```

You will then be able to access this value using `context.secrets.snipcartApiKey`. We'll also use the `request` module, so we'll need to require it at the beginning of the file:

```javascript
var request = require('request');

```

When we make requests to your Webhooks, we always include a request token in the request headers. The header is named `X-Snipcart-RequestToken`. We'll access it through our `context` object again:

```javascript
var requestToken = context.headers['x-snipcart-requesttoken'];
```

_Please note that all the headers are in lower cases with Webtask._

Here are the options we’ll use to send the request to our API:

```javascript
var requestToken = context.headers['x-snipcart-requesttoken'];
var secretApiKey = context.secrets.snipcartApiKey;

var requestOptions = {
  url: 'https://app.snipcart.com/api/requestvalidation/' + requestToken,
  headers: {
    "Accept": "application/json"
  },
  auth: {
    user: secretApiKey
  }
};
```

We’ll run this request and only execute the code in the callback if it’s successful.

```javascript
request(requestOptions, function(error, response, body) {
  if (response.statusCode === 200) {
      // Return rates
  } else {
    // Return an error when the request does not come from Snipcart.    
    cb("Only Snipcart can call this code!");
  }
});
```

So my whole function now looks like this:

```javascript
var request = require('request');

module.exports = function (context, cb) {
  var requestToken = context.headers['x-snipcart-requesttoken'];
  var secretApiKey = context.secrets.snipcartApiKey;

  var requestOptions = {
    url: 'https://app.snipcart.com/api/requestvalidation/' + requestToken,
    headers: {
      "Accept": "application/json"
    },
    auth: {
      user: secretApiKey
    }
  };

  request(requestOptions, function(error, response, body) {
    if (response.statusCode === 200) {
      var orderDetails = context.body.content;
      var rates = [];

      var address = orderDetails.shippingAddress || order.billingAddress;

      if (address.country == "CA" && address.province == "QC") {
        rates.push({
          cost: 0,
          description: "Free shipping for Québec residents!"
        });
      }

      if (address.country == "CA" && address.province != "QC") {
        rates.push({
          cost: 10,
          description: "Shipping to Canada"
        });
      }

      if (address.country == "US") {
        rates.push({
          cost: 15,
          description: "Shipping to US"
        });
      }

      if (rates.length === 0) {
        rates.push({
          cost: 20,
          description: "Standard shipping"
        });
      }

      cb(null, { rates: rates });
    }
    else {
      cb("Only Snipcart can call this code!");
    }
  });
}
```

#### Closing words on Webtask & the serverless approach

Coming up with this little Webtask function for a static site running Snipcart took me less than two hours. Of course, we could’ve focused on other e-commerce functions: handling webhooks to make the bridge between Snipcart and external accounting systems, automating digital goods delivery, and more.

I really believe there are tons of exciting serverless use cases developers should try to handle with Auth0’s Webtask. Any integration with an API, or delegating more long-running/CPU-consuming jobs would make much sense!

The serverless approach is gearing up to have quite an impact on our work as developers. As we’re now seeing with RESTful APIs, many services will start relying on functions developed or hosted by others. The near future will bring more and more microservices hosted in environments like Webtask & AWS Lambda. Especially coupled with the rise of [frameworks like Vue](https://snipcart.com/blog/vue-js-seo-prerender-example) & the JAMstack.

So I sincerely hope this post inspires developers to leverage the FaaS power of Webtask on different serverless projects, e-commerce or not. And of course, I’d be more than interested to have a look at [such set ups](https://snipcart.com/blog/sell-event-tickets-website). You can shoot us an email at geeks@snipcart.com if you got something similar to share, or if you have questions regarding this approach!

Liked the post? Take a second to ? and [_share it on Twitter_](https://twitter.com/home?status=Using%20%40auth0%27s%20%40webtaskio%20FaaS%20on%20a%20%23serverless%20e-commerce%20tutorial%20http%3A//bit.ly/2e5vm8d%20%23webtask)_!_

_Originally published on the_ [_Snipcart blog_](https://snipcart.com/blog/webtask-baas-serverless-tutorial) _and in_ [_our newsletter_](https://us5.list-manage.com/subscribe?u=c019ca88eb8179b7ffc41b12c&id=3e16e05ea2)_._

