---
title: The 5 Stages of a SaaS Subscription
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-09T04:34:53.000Z'
originalURL: https://freecodecamp.org/news/the-5-stages-of-a-saas-subscription-5169307fd0c8
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caeab740569d1a4caa809.jpg
tags:
- name: business
  slug: business
- name: Entrepreneurship
  slug: entrepreneurship
- name: SaaS
  slug: saas
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ben Sears

  This article will go into detail on what you need to automate in order for your
  SaaS company to have a functional subscription billing solution.

  One of the problems SaaS companies face when selling subscriptions is connecting
  their appli...'
---

By Ben Sears

This article will go into detail on what you need to automate in order for your SaaS company to have a functional subscription billing solution.

One of the problems SaaS companies face when selling subscriptions is connecting their application to a billing process.

Some of the things that are need to be considered are:

* How will cancellations be handled
* Free trials
* Granting access to new customers

The challenge in managing these billing processes is handling these events, such as restricting access to an application when a trial expires or if there no longer has a valid funding source attached to an account.

### The SaaS Subscription Lifecycle

![Image](https://cdn-media-1.freecodecamp.org/images/cF991ZGku1qgcPHY5FM8NHUwPlKdt82s6gHW)

The process a customer goes through when doing business with a SaaS company can be broken down into the five events above. Managing these events is the key to integrating a billing system with a SaaS.

#### Subscribe ?

This is the first stage in the journey a user takes with a subscription. In this step, the customer has just signed up for a subscription which needs to trigger an automated process.

The process generally looks something like this:

1. A customer orders a subscription for your application.
2. The customer is granted access to your application.
3. After the trial period is over (if there is a free trial), the customer is charged on a recurring basis.

From a DevOps perspective, these are considered “**Day 1**” operations. These are the steps that a service goes through after being requested in order to be considered “provisioned,” such as installation and configurations of software.

#### Trialing ⏳

In the trialing stage, a customer has subscribed to a service, but is not paying until their trial expires.

![Image](https://cdn-media-1.freecodecamp.org/images/F66cqbVeMQcPsYUx-joezF35PYJQhBlejYVC)

Approximately [75% of SaaS companies](https://www.chargify.com/blog/increase-free-trial-conversions/) offer free trials. Although free trials are almost guaranteed to bring you more paying customers, one of the trickier things about offering them is deciding what happens when a trial expires without a customer adding a funding source.

At this stage of the service lifecycle, a company will need to build logic around trials which will, upon expiration, restrict access to an application and alert the customer that they need to pay.

#### Upgrade ?

![Image](https://cdn-media-1.freecodecamp.org/images/FG7TZ3qnJI9DdlGresF5gspwvM4L8D-V3eNH)
_Netflix offers different tiers_

Many SaaS businesses support multiple tiers of service. If a customer pays a premium, they have access to additional features. This is considered a “**Day 2**” operation, actions which can be taken after a service has been provisioned which affect the end user.

Generally, it follows the pattern below:

1. A customer submits a request to upgrade their subscription.
2. The customer’s subscription rate will be increased.
3. The customer will be granted access to new features within the application.

While this usually takes the form of strict pricing tiers, sometimes customers pay “per user per month” or have “thresholds” which if passed will trigger higher rates.

#### Cancellation ❌

Inevitably, there will be cancellations of subscriptions, also called [churning](http://chaotic-flow.com/saas-metrics-faqs-what-is-churn/). The steps which occur in order to fulfill a cancellation go as follows:

1. A customer requests a cancellation of a SaaS subscription.
2. They will no longer be charged on a recurring basis.
3. Access to the application will terminate at the end of the current billing cycle.

Reaching out to your former customers after they have cancelled will also require some sort of process. It’s recommended that cancellation triggers a process which sends an automated email to the former customer, perhaps with an attempt to recover the customer or a feedback survey to see what reasons they may have had for canceling.

#### Resubscribe ↪️

When a former customer decides to return after canceling, a company can’t just go through the original process to subscribe them as a new customer — they need to reactivate the previously terminated access so that they retain all their former data. This process can be described in three steps:

1. A customer resubscribes by adding a valid funding source to their account.
2. Access to the customer account and data is reactivated.
3. The customer will be charged on a recurring basis once more.

Some complex scenarios might include limited time discount codes for resubscribers, a free trial, or part of another service as part of a combo deal.

### Conclusion

The key to selling software-as-a-service is connecting software to a billing system that can support the lifecycle I just described. Being able to automate this process is a boon to businesses, since manual processes are one of the biggest barriers to scaling.

Trying to manage the challenges of SaaS billing? [Let’s Talk](https://servicebot.io/contact).

We solve challenges SaaS companies face when billing customers by providing easy to integrate hooks which can trigger automated processes.

