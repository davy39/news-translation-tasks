---
title: 'How to Build an Excellent Stripe Integration with Node.js: 4 Best Practices
  and Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-28T17:23:26.000Z'
originalURL: https://freecodecamp.org/news/stripe-and-node-js-4-best-practices-and-examples
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/BLOG_003_Stripe-and-Node.js_-4-Best-Practices-and-Examples.jpg
tags:
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: stripe
  slug: stripe
seo_title: null
seo_desc: 'By Ben Sears

  Have you ever woken up in the middle of the night, worried that you are not using
  the Stripe npm module properly? Probably not, but this article will help put your
  troubled soul at ease anyway with some interactive Node.js examples that ...'
---

By Ben Sears

Have you ever woken up in the middle of the night, worried that you are not using the Stripe npm module properly? Probably not, but this article will help put your troubled soul at ease anyway with some interactive Node.js examples that explain how to build an excellent Stripe integration.

## 1. Use auto-pagination to avoid bloated code

Pagination is a necessary evil that saves us from loading too much data, but dealing with it in code can be a pain. Before `v6.11.0`, your Stripe code would look something like this to deal with pagination:

#### This example shows the old way of handling pagination in Stripe
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_72wdhn7pifTOWbrtrSNFxhsQ00NrdzPvaC")

//get first 100 invoices
let invoices = await stripe.invoices.list({limit: 100});
let numberProcessed = 0;

//loop through these invoices
for(let invoice of invoices.data){
    numberProcessed++;
}

//has_more indicates if we need to deal with pagination
while(invoices.has_more){

    //starting_after will be the the id of the last result
    invoices = await stripe.invoices.list({limit: 100, starting_after: invoices.data[invoices.data.length -1].id});
    
    //loop through the next 100
    for(let invoice of invoices.data){
        numberProcessed++;
    }
    console.log("Number processed so far: " + numberProcessed);
}
console.log("Total Number Processed: " + numberProcessed);
</pre>

With the introduction of  auto-pagination in `v6.11.0`, we are now able to have a much more efficient way of paginating: 

#### This example shows how to auto-paginate in Stripe
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_72wdhn7pifTOWbrtrSNFxhsQ00NrdzPvaC")

//get all invoices
const allInvoices = await stripe.invoices.list({limit: 100}).autoPagingToArray({limit: 10000});
console.log("Invoices - " + allInvoices.length);
</pre>

> Note: You need to be running Node.js v10 or above for this. 

## 2. Use expand to reduce the number of API calls

In Stripe, there are a lot of different objects. A lot of times, when dealing with one type of object, say a subscription; you want to get the product that subscription belongs. To get the product, you need to make an extra call to Stripe as shown here:

#### This example shows how to get the product from a subscription in Stripe without using expand
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE")

const subscription = await stripe.subscriptions.retrieve("sub_G0zK9485afDl6O");
const product = await stripe.products.retrieve(subscription.plan.product);
console.log(product.name);
</pre>

We can effectively avoid this by using the ["expand" attribute in Stripe's API](https://stripe.com/docs/api/expanding_objects):

#### This example shows getting the product by using expand
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE")

//expand the product inside the plan
const subscription = await stripe.subscriptions.retrieve("sub_G0zK9485afDl6O", {expand: "plan.product"});
console.log(subscription.plan.product.name);
</pre>

Cutting down on API calls will improve your app's performance and reduce the risk of hitting Stripe's API limits.

## 3. Configure your Stripe connection for a more stable experience

Most people with a simple Stripe integration will define a new Stripe connection on the fly without configuring it first like so:

`const stripe = require("stripe")("STRIPE_SECRET_KEY");`

When scaling your billing system, consider doing the following to improve your integration quality:

* **Lock your API version to avoid being affected by API changes**
* **Set to Retry Automatically in case of network failure**
* **Define your app information to help the Stripe team**

#### Here's an example function that returns a configured Stripe connection
<pre class="runkit-element">
function createStripeConnection(stripe_api_key){
    const Stripe = require("stripe");
    const stripe = Stripe(stripe_api_key);
    stripe.setApiVersion('2019-03-14');//lock API version down to avoid code breaking
    stripe.setAppInfo({
        name: 'Servicebot',
        version: "1.1.3", //Optional
        url: 'https://servicebot.io' // Optional
    });
    stripe.setMaxNetworkRetries(3); //retry on network failure
    return stripe;
}

const stripe = createStripeConnection("rk_test_72wdhn7pifTOWbrtrSNFxhsQ00NrdzPvaC");
console.log(await stripe.invoices.list());
</pre>


## 4. Use Webhooks to process events that occur in Stripe

Webhooks play an essential role in most Stripe integrations. There are [a lot of different](https://stripe.com/docs/api/events/types) events that happen, so which ones should you care about?

The most important webhook as a SaaS app to pay attention to is the [customer.subscription.deleted](https://stripe.com/docs/api/events/types#event_types-customer.subscription.deleted) - when a subscription goes into state cancelled. You listen for this event in order to decide what to do with someone's account when they cancel, trial runs out, or their card fails. 

Once you start listening to Stripe events, it is a good idea to secure your webhook receiver as not to be fed phony webhooks by a bad-actor. You do this by  utilizing Stripe's webhook si	gning functionality: 

### This example shows how to validate a webhook has come from Stripe

```javascript
// Set your secret key: remember to change this to your live secret key in production
// See your keys here: https://dashboard.stripe.com/account/apikeys
const stripe = require('stripe')('sk_test_bkoS59kZFWBR3XZgkiHwozoX00lD4ttSs1');

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = 'whsec_...';

// This example uses Express to receive webhooks
const app = require('express')();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

// Match the raw body to content type application/json
app.post('/webhook', bodyParser.raw({type: 'application/json'}), (request, response) => {
  const sig = request.headers['stripe-signature'];

  let event;

  try {
    event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
  }
  catch (err) {
    response.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle the event
  switch (event.type) {
    case 'payment_intent.succeeded':
      const paymentIntent = event.data.object;
      handlePaymentIntentSucceeded(paymentIntent);
      break;
    case 'payment_method.attached':
      const paymentMethod = event.data.object;
      handlePaymentMethodAttached(paymentMethod);
      break;
    // ... handle other event types
    default:
      // Unexpected event type
      return response.status(400).end();
  }

  // Return a response to acknowledge receipt of the event
  response.json({received: true});
});

app.listen(8000, () => console.log('Running on port 8000'));

```



---

## Avoid the effort of building and maintaining a complex Stripe Integration

Your billing code can get pretty complicated when it comes to having a fully-featured solution that includes coupons, free trials, metered billing, and more.

Building a user interface for your Stripe integration could take months to develop. [Servicebot](https://servicebot.io) provides a drop-in UI for Stripe Billing. It takes less than an hour to set up and doesn’t require any development effort.

<a href="https://servicebot.io"><img src="https://i.imgur.com/QJkpyHN.png"/></a>


