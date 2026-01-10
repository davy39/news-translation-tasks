---
title: How to implement 3DS2 with Stripe for SCA compliance under PSD2 in Europe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-18T20:27:18.000Z'
originalURL: https://freecodecamp.org/news/implement-3ds2-for-your-saas-using-stripe-billing-and-be-sca-compliant-for-pds2
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/BLOG_002_Implement-3DS2-for-your-SaaS-using-Stripe-Billing-and-be-SCA-compliant-for-PDS2.png
tags:
- name: 3DS2
  slug: 3ds2
- name: psd2
  slug: psd2
- name: 3ds
  slug: 3ds
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: React
  slug: reactjs
- name: SCA
  slug: sca
- name: stripe
  slug: stripe
seo_title: null
seo_desc: 'By Ben Sears

  What are PSD2, SCA, and 3DS?

  PSD2

  The second Payment Services Directive (PSD2) is an EU directive announced in 2015.
  The goal of PSD2 is to protect people when they pay online, promote open banking,
  and make cross-border European payment...'
---

By Ben Sears

# **What are PSD2, SCA, and 3DS?**

## **PSD2**

The second Payment Services Directive (PSD2) is an EU directive announced in 2015. The goal of PSD2 is to protect people when they pay online, promote [open banking](https://en.wikipedia.org/wiki/Open_banking), and make cross-border European payment services safer. It went into effect September of 2019.

## **SCA**

Strong Customer Authentication (SCA) is a [requirement of the PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.069.01.0023.01.ENG&toc=OJ:L:2018:069:TOC) that ensures online payments are performed with multi-factor authentication to increase the security of online payments. Even though PSD2 was enacted in September of 2019, SCA has been delayed by 18 months to allow merchants and banks more time to implement solutions.

## **3DS2**

3-D Secure 2.0 (3DS2) is the second iteration of the 3DS, used to power brand-name systems such as [Visa Secure](https://usa.visa.com/visa-everywhere/security.html), [Mastercard Identity Check](https://www.mastercard.us/en-us/merchants/safety-security/identity-check.html), and [American Express SafeKey](https://network.americanexpress.com/globalnetwork/safekey/us/en/). It was designed to reduce fraud and provide added security to online payments and supported by many major banks.

3DS2 is considered an SCA compliant solution. If your business implements 3DS2, you will no longer be in danger of having your charges declined by banks.

# **Does SCA affect your SaaS business?**

![Image](https://blog.servicebot.io/content/images/2019/10/image-21.png)

SCA is considered in-effect on all e-commerce payments when both:

* The business is in the EU
* The customer's bank is in the EU

If SCA applies to you and you do not authenticate your customer's transactions you risk **having charges declined by banks**. 

There are exemptions for several types of transactions defined in [Articles 12-18 of the PSD2](https://eba.europa.eu/documents/10180/1761863/Final+draft+RTS+on+SCA+and+CSC+under+PSD2+%28EBA-RTS-2017-02%29.pdf). As a SaaS company, the most critical exception to note is **Article 13.** This article states that recurring transactions do not need to be subject to SCA. What this means is that you only need to have an SCA implementation to handle the initial creation of a subscription and not the subsequent recurring charges.

If you are interested in reading a breakdown of the other exemptions and how they may apply to you, [Stripe goes into depth on each here](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication).

# **Should you be SCA-ready even if you aren't in Europe?**

There are benefits to implementing a solution such as 3DS2, even if you aren't affected by PSD2 or SCA. By implementing 3DS2, you will handle customer information in a much more secure manner, as well as shifting liability from you to the card issuer, reducing the risk of chargebacks.

# **How do you become SCA compliant?**

Being SCA compliant as a SaaS means that all online payments are authorized using two of the three elements,

![Image](https://blog.servicebot.io/content/images/2019/10/image-19.png)

As I mentioned before, 3DS2 is an SCA-compliant solution. Drop-in solutions such as [Servicebot](https://servicebot.io), PayPal, and [Stripe Checkout](https://stripe.com/payments/checkout) already use 3DS2 and are therefore SCA-compliant. If you are using a custom-built solution using something like Stripe Billing or Braintree to manage your subscriptions, you will need to develop a 3DS2 implementation.

# **How do you implement 3DS2 using Stripe Billing?**

![Image](https://blog.servicebot.io/content/images/2019/10/image-22.png)

Stripe has created two new objects as part of offering an SCA-compliant solution, PaymentIntent and SetupIntent, to facilitate using 3DS2. A PaymentIntent represents the intent to charge someone and is used as part of a payment authentication flow. SetupIntents are similar to PaymentIntents, but they represent the intent to charge someone's card eventually. You will use SetupIntents if your SaaS has a free trial, or offers a free tier, essentially anywhere a credit card will be charged at a later date.

## **Using PaymentIntents**

If you are using Stripe Billing to create subscriptions, you are already using PaymentIntents by default. They are created and attached to each invoice for every new subscription. If you want to know if a new subscription requires SCA, you can check the status of the `payment_intent` on the `latest_invoice` of the subscription. The object will contain a `status` of `requires_action` - Run the following NodeJS code to see it in action.

## This code creates a subscription that requires SCA
<pre class="runkit-element">
const STRIPE_TEST_SECRET_KEY = "rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE";
let stripe = require("stripe")(STRIPE_TEST_SECRET_KEY);
const sub = await stripe.subscriptions.create({ //creates a SCA-required subscription
    items: [{plan : "plan_FvnU01xoIPrg9l"}], //$300 per month plan without free trial
    customer: "cus_G0juGVZSLskx57",
    default_payment_method: "pm_1FUiR8CISNxwKLmI8uIQDdnv", //This PaymentMethod always requires SCA
    expand: ["latest_invoice.payment_intent"] //we expand the payload to show up the payment intent
});
const paymentIntent = sub.latest_invoice.payment_intent;
console.log(`Subscription Status: ${sub.status}`);
console.log(`PaymentIntent Status: ${paymentIntent.status}`)
console.log(paymentIntent.status === "requires_action" ? "SCA Required" : "No SCA Required");
console.log(sub);
</pre>

Once you know you have a subscription that requires authentication, you can use the PaymentIntent's client_secret on the browser to start a 3DS2 Authentication process using Stripe.js

## **Using Stripe.js handleCardPayment with the PaymentIntent**

Stripe.js has a handy function called [handleCardPayment](https://stripe.com/docs/stripe-js/reference#stripe-handle-card-payment), which takes in a client secret from a payment intent and starts the 3DS2 process to authenticate the payment.

```javascript
await stripe.handleCardPayment('PAYMENTINTENT_SECRET');
```

You can see this in action here

%[https://codepen.io/bsears/pen/PooGOLg?editors=1111]

Once the customer authenticates, the subscription will move from an `incomplete` state to an `active` one, and the customer will be billed successfully.

## **SetupIntents**

As a SaaS business, you will mostly be interacting with SetupIntents if you are either using a Free-tier or give a Free trial. When someone enters a credit card, for one of these subscriptions, you will see a `pending_setup_intent` on the [subscription object](https://stripe.com/docs/api/subscriptions/object#subscription_object-pending_setup_intent). The SetupIntent's `client_secret` should be passed to the front-end so that Stripe.js can start the 3DS2 authentication flow.

## **Using Stripe.js handleCardSetup with the SetupIntent**

This is  basically identical to how we handled the PaymentIntent, except we call handleCardSetup instead

```javascript
await stripe.handleCardSetup('{SETUP_INTENT_CLIENT_SECRET}')
```

You can see a SetupIntent SCA Flow in action below.

%[https://codepen.io/bsears/pen/RwwGyYw?editors=1111]

Once authentication completes, the customer can be moved to a paid plan later or have their card charged after a free trial is over.

# **No-code alternative**

If you are looking for an SCA-compliant solution for Stripe Billing without having to deal with the 3DS2 integration development, check out [Servicebot](https://servicebot.io). We provide a drop-in UI for SaaS companies using Stripe, which is SCA-compliant out-of-the-box! Want to see it in action? Check out [this demo](https://dashboard.servicebot.io/examples/signup-embed/0) and use the test card `4000002760003184` (any Expiration and CVC).

<a href="https://servicebot.io"><img src="https://i.imgur.com/QJkpyHN.png"/></a>

