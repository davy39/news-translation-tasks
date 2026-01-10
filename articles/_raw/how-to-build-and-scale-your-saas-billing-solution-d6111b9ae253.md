---
title: How To Build and Scale Your SaaS Billing Solution
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-26T21:12:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-scale-your-saas-billing-solution-d6111b9ae253
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tnIp6GZjyfJRU2sCnea_tA.png
tags:
- name: business
  slug: business
- name: Entrepreneurship
  slug: entrepreneurship
- name: SaaS
  slug: saas
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ben Sears

  What you need for a Minimum Viable Product

  When you are building your Software as a Service (Saas) Minimum Viable Product (MVP),
  there is a lot of work that needs to be done. It can be difficult to balance this
  workload.

  Oftentimes you a...'
---

By Ben Sears

### What you need for a Minimum Viable Product

When you are building your Software as a Service (Saas) Minimum Viable Product (MVP), there is **a lot** of work that needs to be done. It can be difficult to balance this workload.

Oftentimes you are so focused on developing the product that you forget that you still need to sell it to people. This guide is meant to help you get your billing system off the ground to start making revenue, and show what you should be doing when you are ready to scale up.

![Image](https://cdn-media-1.freecodecamp.org/images/OFXjFRN0BrbdrfRc2F6keUgGrbDU9MKfOMVM)
_Like the functionality of your product, your billing system should scale as you grow_

#### Subscriptions

Subscriptions are key to an effective billing strategy. The ability to charge a credit card on a recurring basis makes payment more efficient for both you and the customer.

To start selling subscriptions to your clients, you need:

* A form users can fill out to enter their credit card
* A backend process that can be called after the payment is successful

If you don’t have the development cycles to do this, you will be stuck with a painful process of sending invoices manually, giving customers access manually, and adding friction to the on-boarding process.

#### Free Trials

> For many SaaS companies, 100% of their customers come in through their Free trial system. — [Lincoln Murphy](https://sixteenventures.com/saas-free-trial-benchmarks)

Offering free trials is considered by many to be one of the best ways to find early adopters of your SaaS.

When someone is given the opportunity to try your product before committing to a subscription, they are far more likely to become a regular customer.

It is good practice to treat your trial users with the same level of support and respect as you would your paying customers. Not only are they experiencing your product, they are also experiencing the quality of your service.

#### What to integrate with

At the end of the day, you will end up integrating with an external system to handle these use cases. I highly recommend looking at [**Stripe**](https://stripe.com) because they have an excellent API to integrate with and a wide range of functionalities.

If you don’t want to develop the integration with Stripe yourself, take a look at **[Servicebot](https://servicebot.io)** — It comes fully integrated with Stripe and has great Customer Relationship Management (CRM) functionality so you can better manage your customers and subscriptions from a dashboard.

![Image](https://cdn-media-1.freecodecamp.org/images/Wq9ipq8Diz4bqjrCd8VljZ3iAdgMSTQmHMId)
_Designing a service in [https://servicebot.io](https://servicebot.io" rel="noopener" target="_blank" title=")_

### Automation is the key to scaling

During your early stages, [Y Combinator](http://www.ycombinator.com/) founder Paul Graham says, “[Do things that don’t scale.](http://paulgraham.com/ds.html)” Although this may sound counter-intuitive, this is the best way to grow your customer base before you begin to even think about scaling.

What scaling boils down to is automating the manual processes you’ve found to be effective at growing your startup.

When you’re ready to scale your billing solution, here are a few things to consider:

#### Billing Process Automation

Automating the processes involved with billing — such as what happens when a user requests a trial, adds a funding source, or requests a cancellation — is one of the most important parts of scaling your billing solution.

You should first take a look at how you are currently doing your billing. Identify all the manual processes that currently are a part of your system, like restricting access if trials expire or reactivating accounts after they’ve been cancelled. Once you make that list you can start figuring out how much time is spent performing these and start iterating to reduce the most painful parts.

Another big part of automating your process is automating customer outreach based on their status in the billing system.

#### Automatic customer outreach

![Image](https://cdn-media-1.freecodecamp.org/images/8e3TpVvgV9F70y1sEj06dMedSupxvIJajLF2)

Customer outreach is key to converting customers from free trials to paid. When starting out, this process is mostly manual. Email people when they sign up, remind them when their trial is ending soon, or ask if they need help getting started.

This is not scalable — you need to eventually automate this process, and the best place to focus on is the billing side because so many steps are processed there

* **On-boarding** — When a new user signs up, your system should automatically send an email explaining how to get started.   
More advanced systems follow the customer’s journey and send specific help articles for things they haven’t done yet.
* **Trial Conversion** — When a trial is created, there are a few things that should be sent to the user to convince them to convert. Things like a “3 days left” reminder or a message asking for a 1-on-1 call can really make the difference.   
Automating these messages is important to insure scalability.
* **Lead recovery** — When a trial expires or a user cancels, all is not lost. Sending emails a specific duration after they leave explaining new features, asking for feedback of what you can do better, and articles about your product may be enough to bring them back around to give you another chance.

To ensure seamless communication between your system and the customer, it is important for your system to be tightly integrated with your billing.

### Integrating with other systems

![Image](https://cdn-media-1.freecodecamp.org/images/DwWFv5oAvnOSQoHJKYLVDlFhHOOFVgnrMH4-)

One of the best ways to automate your businesses with minimum development effort is to integrate with third-parties who have already solved the problems you are facing.

Here are my favorites which I’m using for my own SaaS startup:

#### Stripe — Payment processing

Stripe has become the staple of SaaS payment providers. With a developer-friendly API and constant new features, I (and countless others) feel it’s an obvious integration point.

Some of the features you can integrate with to automate more of your billing are:

* Webhooks to alert your system of failed payments
* No credit card free trials
* Add charges to existing subscriptions

There is much more you can do with Stripe, it should be up to you and your startup’s needs to determine how deep of an integration you need.

#### Intercom — Communication automation

The staple of [Intercom](https://www.intercom.com/) is the live chat widget that you embed on your site to enable communication with your customers. What many people don’t realize is that Intercom also provides an automation platform. If you integrate with Intercom, you can send customized messages to your customer based on what they do with your product.

This allows you to automate the communication with your customer so you don’t have to manually email anymore.

![Image](https://cdn-media-1.freecodecamp.org/images/XtG6G3gMrwU9kMTkLQiaPDXL7-n3GkvPXjYQ)
_Example of intercom outreach automation_

#### Servicebot — Subscription Management

[Servicebot](https://servicebot.io/#1) comes out-of-the-box with a Stripe and Intercom integration. When a customer requests a free trial, Servicebot creates a new trialing subscription and customer in Stripe and a new user in Intercom, and directs them to a newly-created instance to use.

Intercom will send automated messages with the goal of converting to a paying user while Stripe will manage the subscription automatically.

A good first step to begin scaling is with automating your billing process. When it all comes together, you can connect parts of your business to a centralized location, as well as integrate it with third parties. The result of all this will be massive gains in productivity and efficiency that make the effort well worth it.

If you are interested in automating parts of your SaaS billing solution to do things like automate customer on-boarding and connecting business processes to your billing system.

