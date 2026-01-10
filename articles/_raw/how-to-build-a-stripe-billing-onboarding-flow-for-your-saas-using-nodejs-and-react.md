---
title: How to build a Stripe Billing onboarding flow for your SaaS using NodeJS and
  React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-16T14:59:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-stripe-billing-onboarding-flow-for-your-saas-using-nodejs-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/BLOG_001_How-to-build-a-Stripe-Billing-onboarding-flow-for-your-SaaS-using-NodeJS-and-React.jpg
tags:
- name: Node.js
  slug: nodejs
- name: React
  slug: react
seo_title: null
seo_desc: 'By Ben Sears

  What will you learn?

  In this article we will be going over the steps needed to integrate Stripe Billing
  with an onboarding flow using NodeJS and React. In the guide we will be:


  Configuring a Stripe account with a pricing strategy we wil...'
---

By Ben Sears

# What will you learn?

In this article we will be going over the steps needed to integrate Stripe Billing with an onboarding flow using NodeJS and React. In the guide we will be:

* Configuring a Stripe account with a pricing strategy we will be using in this example
* Setting up a Route in ExpressJS which will expose the pricing strategy to the front-end
* Setting up a React front-end which will handle the onboarding flow, utilizing [Stripe Elements](https://stripe.com/payments/elements) for checkout

In this article we assume you already have a working knowledge of Node and ExpressJS as well as the steps needed to create a React app. For some good resources on how to learn these check out:

* [ExpressJS on FreeCodeCamp](https://guide.freecodecamp.org/nodejs/express/)
* [React on FreeCodeCamp](https://learn.freecodecamp.org/front-end-libraries/react/)

# Define your Products and Plans in Stripe

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-64.png)

The first step is to create some products and plans in your Stripe account. If you haven't registered for Stripe you can do so [here](https://dashboard.stripe.com/register). 

For this example we are going to create a two tiered pricing strategy, with a Basic $50/month tier and a Premium at $300/month tier defined as separate Products in Stripe.

![Image](https://blog.servicebot.io/content/images/2019/10/image-10.png)
_The Products we create with plans attached_

If you want this automated for your specific Stripe account, feel free to edit the secret key in this RunKit to your Stripe test key.

### This code will create products and plans in Stripe
<pre class="runkit-element">
const STRIPE_TEST_SECRET_KEY = "sk_test_6pewDqcB8xcSPKbV1NJxsew800veCmG5zJ"//your Stripe key here
const stripe = require('stripe')(STRIPE_TEST_SECRET_KEY);

const basicPlan = await stripe.plans.create({
    amount: 5000, 
    interval: "month", 
    product: {
        name : "AcmeBot Basic"
    },
    currency: "USD"
})
const premiumPlan = await stripe.plans.create({
    amount: 30000, 
    interval: "month", 
    product: {
        name : "AcmeBot Premium"
    },
    currency: "USD"
})
console.log(`Stripe Plans that were Created:`);
console.log(`AcmeBot Basic, Plan ID: ${basicPlan.id}, Amount: $${basicPlan.amount/100}/${basicPlan.interval}, Product ID: ${basicPlan.product}`)
console.log(`AcmeBot Premium, Plan ID: ${premiumPlan.id}, Amount: $${premiumPlan.amount/100}/${premiumPlan.interval}, Product ID: ${premiumPlan.product}`)
</pre>

# Create a REST endpoint for getting Plans

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-62.png)

After you have your Stripe configured, we can define a new REST endpoint in Express that our React can consume in order to render an onboarding flow using live Stripe data. 

In order to render a pricing page, the front-end will need to know the plans in your Stripe account, so our code will be making an API call to Stripe using the `stripe` module. Here is what an example ExpressJS middleware could look like which does this.

### ExpressJS middleware for getting all Stripe plans          
<pre class="runkit-element">
const STRIPE_TEST_SECRET_KEY = "rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE"; //your Stripe key here
const stripe = require('stripe')(STRIPE_TEST_SECRET_KEY);


//express middleware
async function getAllPlans(req, res, next){

    //get all plans, expand keyword will also return the contents of the product this plan is attached to
    const plans = await stripe.plans.list({expand: ["data.product"]});
    res.json(plans);
}


//see it in action
const req = {}; // req not used
const res = {
    json : function(payload){
        console.log("All Stripe Plans:")
        for(let plan of payload.data){
            console.log(`Plan ${plan.id}, Name: ${plan.product.name}, Amount: ${plan.amount/100}/${plan.interval}`)
        }
        console.log("payload:", payload);
}
};
const next = function(){};
await getAllPlans(req, res, next)
</pre>

After this step is done, we can do our front-end in React in order to display a pricing page and a checkout flow

# Create a Component to display pricing

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-63.png)

In order to create a pricing page, we'll need to define a component which renders the plan data that is gotten from the REST API we defined above.

The component will look something like this. It'll loop through all the plans and render the relevant information such as price, name, and interval. It will also display a checkout page (which we will define in the next step) when the user presses "Get Started".

```javascript
function Pricing({pricingPlans, onPlanSelect}){
  return <div>{pricingPlans.data.map(({id, interval, amount, product: {name}})=>{
      return <div>
        <h1>{name}</h1>
        <h4>${amount/100}/{interval}</h4>
        <button onClick={onPlanSelect(id)}>Get Started</button>
      </div>
    })}</div>
}
```

You see this code in action below in the CodePen. Note, for this CodePen we don't make an API call and just statically define the payload. In your own implementation you should be pulling the payload directly from your API.

%[https://codepen.io/bsears/pen/jOOEaap]

# Create a Checkout Flow



For the last step, we will be creating a checkout process using [Stripe Elements](https://stripe.com/payments/elements) and tying it back to the pricing page we just set up. 

In the previous example we created a callback function which would be triggered when someone picks a plan. We now need to tie that to Stripe so when they pick a plan, they are prompted with a checkout page. We do that using [React Stripe Elements](https://github.com/stripe/react-stripe-elements), the React wrapper around the Stripe Elements library.

You can see this in action below:

%[https://codepen.io/bsears/pen/BaayXME]

Now that we have a basic checkout flow, we will need to [process the token](https://stripe.com/docs/sources/cards) generated by the form and [create a subscription](https://stripe.com/docs/api/subscriptions/create) for the new customer, giving us a new subscription. Alternatively, you could, instead of using Stripe Elements, use [Stripe Checkout](https://stripe.com/payments/checkout) which automatically creates subscriptions (but is not as flexible).

This wraps up the tutorial on creating a checkout flow with Stripe, React, and Node

## What comes next?

Thanks for reading! This will get you started with billing, but we've only touched the tip of the iceberg of building a billing system with Stripe with this post. More advanced topics such as coupons, advanced pricing strategies, and different pricing intervals (monthly/annual for example) requires much more development to support.

If you are looking to get great looking & mobile friendly pricing pages, checkout forms, and more without having to build it all yourself, check out [Servicebot](https://servicebot.io) - A drop-in UI toolkit built on top of Stripe, you just paste a code snippet and get a fully featured front-end powered by Stripe.

<a href="https://servicebot.io"><img src="https://i.imgur.com/QJkpyHN.png"/></a>


