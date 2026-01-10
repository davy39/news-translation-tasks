---
title: How to Design Payment Logic on Stripe (and Apply It)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-25T07:24:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-payment-logic-on-stripe-and-apply-it
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/lee-campbell-DtDlVpy-vvQ-unsplash.jpg
tags:
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Vitaly Kuprenko

  Payment logic is central to any product that deals with money. After all, a well-designed
  payment architecture, if properly tested, saves tons of time in the future.

  But it may take too long to master the top level of working with ...'
---

By Vitaly Kuprenko

Payment logic is central to any product that deals with money. After all, a well-designed payment architecture, if properly tested, saves tons of time in the future.

But it may take too long to master the top level of working with popular payment gateways. 

To help you out, I wrote this guide on designing payment logic on Stripe. It includes use cases, project examples, and a bit of theory with code samples. 

This guide is mostly for QA engineers as it helps to understand how to test payment logic based on Stripe. But don't come off, PMs and developers. We have lots of interesting details for you too. 

## How Stripe Works

Let’s start with the basics and review the Stripe payment scheme.

![Image](https://lh4.googleusercontent.com/TbNvvj8SxuZifs9zYb_vDx3WutphLBQmmoLgOCiUUVofnM7ECswMY7FahTHHQEIEbzsseV7pOs6VhZUiV5q5rTjiFbwnmclwKaDpJwd9-xtkdOlKwusmg7EXyfJhXdGA0SE7yIfD)
_Payment scheme for Stripe_

This scheme works for users that buy content on websites or through mobile apps. Visitors don't need to register and add link credit cards to their profiles – Stripe allows paying for the content seamlessly. 

All they need to do is enter credit card details, and the magic happens:

1. Credentials are sent to Stripe.
2. Stripe tokenizes the data and returns a token to the back-end.
3. Back-end creates a charge.
4. The data is sent to Stripe again, and it shares the details with payment systems.
5. Payment systems respond to Stripe and state whether everything alright. Or report about issues.
6. Stripe responds to the server about the state of the transaction.

If everything goes smoothly, the user gets content. If not, an error message.

Besides, there are two necessary conditions to use Stripe: 

* you have a bank account
* you are a resident of one of the 25 supported countries

### Connecting a card to Stripe

Linking your product user with Stripe customer goes on the server-side. And it looks like this:

1. Credit card credentials go to Stripe (from app or website);
2. Stripe returns a token, then it goes to the back-end;
3. Back-end sends it back to Stripe;
4. Stripe checks whether the customer exists (if yes, the card is added, not – it creates a new customer and adds the card).

The first card added is the default payment method. Stripe will use it to make the transaction.

### Connecting with a Stripe account

If you’re building an on-demand app like Uber and want users to get paid in it (like Uber drivers), ask them to create an account first. 

There are three types of Stripe accounts:

* **Standard**. An already existing account with the required credentials. Registered by the user, validated by Stripe and a bank. 
* **Express**. Enables easy on-boarding: you create an account on your own, and the user fills it with details. Works within the US.
* **Custom**. Comes with the highest level of flexibility and allows you to modify multiple parameters. In turn, the platform is responsible for every interaction with users.

## Stripe Core Features

Still on the subject of how Stripe works, I suggest taking a look at its features. 

### Charges

Stripe makes two kinds of charges – **direct** and **destination**. 

**Direct charge**

Let's get back to the Uber model. The platform charges a certain amount from riders, and that money goes directly to the linked accounts, to drivers. Direct charge implies that drivers pay all the fees. Plus, Uber also charges a fixed percentage. 

![Image](https://lh6.googleusercontent.com/tuM5RJt54RMYUyNGiJ-hRwNTDL1LrnR1jIoJXD6Sx_pq2QdHinsZDSu6QXhVNk9zYD9YeSVibie04bZUKYxVjxjXTsu8be8_0PcIVS45uVWzwDlwl0-siZCUc9lu0jbk5I34SdbN)

  
**Destination charge**

In this case, the platform pays all the fees, and you get the net worth. First, the amount goes to the Stripe account of your platform, and then there’s an automatic transfer to the partner (drivers).

### Authorize and capture  


Stripe supports two-step payments that enable users to authorize a charge first and capture it later. Card issuers guarantee that auth payments and the required amount gets frozen on the customer's card. 

If the charge isn't captured for this period, authorization is canceled. 

**Here's how it works in Uber:** a rider sees an approximate cost of the trip while booking the ride. If they agree to it, this amount gets frozen on their cards until they finish their trip. 

When they finish the ride, Uber calculates the final price and charges it from the card. 

That’s the reason product owners choose Stripe for their [P2P payment app development](https://www.cleveroad.com/blog/p2p-payment-app-development). As trust matters the most when it comes to peer-to-peer transactions.

Finally, here come another three Stripe features I’d like to mention. 

**Transfers**. Transfers go from the platform account to suppliers. For instance, Uber drivers link Stripe accounts with their profiles to get the pay. 

**Subscriptions**. This feature is quite flexible and enables users to set intervals, trial periods, and adjust the subscription to their needs. 

**Refunds**. If buyers want to get their money back, Stripe users can easily issue a refund to the customers’ card.

## Handling Stripe Objects

  
Next, we’re moving to the Stripe objects. And here come the code samples I’ve promised.

### Source object

Here's a checklist for the source object. 

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Key</th>
	      <th>Value</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>customer</td>
	      <td>customer’s stripe id</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>stripe_id of added card</td>
	    </tr>
	    <tr>
	      <td>last4</td>
	      <td>last 4 numbers of added card</td>
	    </tr>
          <tr>
	      <td>brand</td>
	      <td>credit card company (Visa, AE)</td>
	    </tr>
          <tr>
	      <td>exp_month, exp_year</td>
	      <td>expiration date of the card</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

The object keeps a payment method that helps to complete the charge. It's also possible to link the source object with users. This allows them to store all the payment methods there. 

When testing, it's crucial to make sure a payment method corresponds with the returned value. Check **last4** and **exp_month/year** for this. 

If the source object is linked with a customer and you want to make sure it belongs to the right person, check the **customer id**.   
Here's a JSON of the object:

```
{
        "id": "card_1CboP4CLud4t5fBlZMiVrzBq",
        "object": "card",
        "address_city": null,
        "address_country": null,
        "address_line1": null,
        "address_line1_check": null,
        "address_line2": null,
        "address_state": null,
        "address_zip": null,
        "address_zip_check": null,
        "brand": "Visa",
        "country": "US",
        "customer": "cus_D1s9PQgvr6U46j",
        "cvc_check": "pass",
        "dynamic_last4": null,
        "exp_month": 4,
        "exp_year": 2024,
        "fingerprint": "soMjdt25OvcMcObY",
        "funding": "credit",
        "last4": "4242",
        "metadata": {},
        "name": null,
        "tokenization_method": null
      }
```

### Customer object

  
Starting with the checklist again.

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Key</th>
	      <th>Value</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>subscriptions</td>
	      <td>the list of Subscriptions</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>customer stripe_id</td>
	    </tr>
	    <tr>
	      <td>default_source</td>
	      <td>stripe_id of the default card</td>
	    </tr>
          <tr>
	      <td>sources</td>
	      <td>list of Sources</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

The customer object stores payment methods including the default one. And contains information about users and their subscriptions. 

It also recalls users' credit cards and the primary payment method set. You can charge users manually based on this data. 

Same with subscriptions – Stripe manages them and withdraws fees automatically.

```
{
  "id": "cus_D1s9PQgvr6U46j",
  "object": "customer",
  "account_balance": 0,
  "created": 1528717303,
  "currency": null,
  "default_source": "card_1CboP4CLud4t5fBlZMiVrzBq",
  "delinquent": false,
  "description": null,
  "discount": null,
  "email": null,
  "invoice_prefix": "4A178DE",
  "livemode": false,
  "metadata": {},
  "shipping": null,
  "sources": {
    "object": "list",
    "data": [
      {
        "id": "card_1CboP4CLud4t5fBlZMiVrzBq",
        "object": "card",
        "address_city": null,
        "address_country": null,
        "address_line1": null,
        "address_line1_check": null,
        "address_line2": null,
        "address_state": null,
        "address_zip": null,
        "address_zip_check": null,
        "brand": "Visa",
        "country": "US",
        "customer": "cus_D1s9PQgvr6U46j",
        "cvc_check": "pass",
        "dynamic_last4": null,
        "exp_month": 4,
        "exp_year": 2024,
        "fingerprint": "soMjdt25OvcMcObY",
        "funding": "credit",
        "last4": "4242",
        "metadata": {},
        "name": null,
        "tokenization_method": null
      },
      {
        "id": "card_1CcC3uCLud4t5fBlW2UMknUW",
        "object": "card",
        "address_city": null,
        "address_country": null,
        "address_line1": null,
        "address_line1_check": null,
        "address_line2": null,
        "address_state": null,
        "address_zip": null,
        "address_zip_check": null,
        "brand": "Visa",
        "country": "US",
        "customer": "cus_D1s9PQgvr6U46j",
        "cvc_check": "pass",
        "dynamic_last4": null,
        "exp_month": 4,
        "exp_year": 2024,
        "fingerprint": "soMjdt25OvcMcObY",
        "funding": "credit",
        "last4": "4242",
        "metadata": {},
        "name": null,
        "tokenization_method": null
      }
    ],
    "has_more": false,
    "total_count": 2,
    "url": "/v1/customers/cus_D1s9PQgvr6U46j/sources"
  },
  "subscriptions": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/customers/cus_D1s9PQgvr6U46j/subscriptions"
  }
}
```

### Charge object  


Checklist for the charge object:

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Key</th>
	      <th>Value</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>destination</td>
	      <td>stripe account of payee</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>charge stripe_id</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>payment amount in cents</td>
	    </tr>
          <tr>
	      <td>amount_refunded</td>
	      <td>refunded amount in cents</td>
	    </tr>
          <tr>
	      <td>customer</td>
	      <td>customer_id of a payer</td>
	    </tr>
          <tr>
	      <td>captured</td>
	      <td>true - payment is made, false - authorized</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

* **amount** – you should always check which amount was charged during the testing process. It may be in cents, euro cents, and so on.
* **amount_refunded** – this field has a value different from zero if the whole amount of transaction (or its part) was refunded.
* **customer** – id of your customer
* **captured** – indicates the status of the transaction. Money can be held on the user's credit card or can be charged.
* **destination** – destination key will store user's Stripe account you've transferred the money to.

```
"fingerprint": "soMjdt25OvcMcObY",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "tokenization_method": null
  },
  "source_transfer": null,
  "statement_descriptor": null,
  "status": "succeeded",
  "transfer_group": null
}
```

**Refund object**

The refund object is embedded in the charge object in case any part of the payment (or the whole payment) gets refunded to the buyer.

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Key</th>
	      <th>Value</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>status</td>
	      <td>success / pending / failed</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>refund stripe_id</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>payment amount in cents</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

```
{
  "id": "re_1CcY10CLud4t5fBlN23KtYq7",
  "object": "refund",
  "amount": 999,
  "balance_transaction": "txn_1CcY10CLud4t5fBlhlmzzJuK",
  "charge": "ch_1CcD7dCLud4t5fBlC1srZNIB",
  "created": 1528892634,
  "currency": "usd",
  "metadata": {},
  "reason": null,
  "receipt_number": null,
  "status": "succeeded"
}
```

**Transfer object**

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Key</th>
	      <th>Value</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>reversals</td>
	      <td>list of reverse transfer objects</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>transfer_id</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>payout amount in cents</td>
	    </tr>
          <tr>
	      <td>destination</td>
	      <td>linked account of a payee</td>
	    </tr>
          <tr>
	      <td>reversed</td>
	      <td>false - money transaction, true - reverse</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

The transfer object keeps information related to the transfer from the platform balance to other accounts. Like payouts to platform's partners – Uber drivers. 

Mind that all the transactions should be loginized in the database. This way, during testing, you'll see the transfer id. Go to Stripe and check the following:

* **amount** – the sum paid to a payee
* **destination** – Stripe account of the user who gets the payment
* **reversed** – if you need to cancel a transaction, the key acts as an indicator. It shows a false value if the transaction succeeded. True – if reversed
* **reversals** – stores a list of objects in case any part of the transfer was reversed

```
{
  "id": "tr_1CcApyCLud4t5fBlZyx5mEPI",
  "object": "transfer",
  "amount": 250,
  "amount_reversed": 0,
  "balance_transaction": "txn_1CcApyCLud4t5fBlfA5cgXBz",
  "created": 1528803538,
  "currency": "usd",
  "description": null,
  "destination": "acct_18bAS3KcT341ksb9",
  "destination_payment": "py_1CcApyKcT341ksb9VawxIJdS",
  "livemode": false,
  "metadata": {},
  "reversals": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/transfers/tr_1CcApyCLud4t5fBlZyx5mEPI/reversals"
  },
  "reversed": false,
  "source_transaction": null,
  "source_type": "card",
  "transfer_group": null
}
```

**Balance Transaction object**

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Key</th>
	      <th>Value</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>type</td>
	      <td>type of transaction (charge, refund, transfer)</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>refund stripe_id</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>payment amount in cents (pay attention to +/- signs)</td>
	    </tr>
          <tr>
	      <td>available_on</td>
	      <td>date when money will be available for a payee</td>
	    </tr>
          <tr>
	      <td>fee</td>
	      <td>amount of Stripe fee</td>
	    </tr>
          <tr>
	      <td>fee_details</td>
	      <td>list of fee objects</td>
	    </tr>
          <tr>
	      <td>net</td>
	      <td>amount of net income/expenditure</td>
	    </tr>
          <tr>
	      <td>status</td>
	      <td>current status of operation</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

The object stores data about any changes to the application balance. You don't actually need to test this object. It’s rather for understanding where the fees come from. 

* **amount** – payment amount in cents
* **available_on** – the money sent to partners will be available for them in time, and this key tells when exactly
* **fee** – amount of the Stripe fee
* **fee_details** – list of fee objects with a description why the fee was charged
* **net** – amount of net income
* **status** – the status of operation success
* **type** – type of the object (charge, refund, transfer)

Code sample of balance transaction for transfer:

```
{
  "id": "txn_1CcApyCLud4t5fBlfA5cgXBz",
  "object": "balance_transaction",
  "amount": -250,
  "available_on": 1528803538,
  "created": 1528803538,
  "currency": "usd",
  "description": null,
  "exchange_rate": null,
  "fee": 0,
  "fee_details": [],
  "net": -250,
  "source": "tr_1CcApyCLud4t5fBlZyx5mEPI",
  "status": "available",
  "type": "transfer"
}
```

Code sample of balance transaction for charge:

```
{
  "id": "txn_1CbrRTCLud4t5fBlhRfMLdq1",
  "object": "balance_transaction",
  "amount": 10000,
  "available_on": 1529280000,
  "created": 1528728983,
  "currency": "usd",
  "description": "Charge user asdf11@example.com for instructor sodom@example.com lesson id: 77",
  "exchange_rate": null,
  "fee": 320,
  "fee_details": [
    {
      "amount": 320,
      "application": null,
      "currency": "usd",
      "description": "Stripe processing fees",
      "type": "stripe_fee"
    }
  ],
  "net": 9680,
  "source": "ch_1CbrP3CLud4t5fBlztHMxVzv",
  "status": "pending",
  "type": "charge"
}
```

**Subscription object**

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Key</th>
	      <th>Value</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>plan</td>
	      <td>rules for subscription: amount, interval, trial days</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>subscription stripe_id</td>
	    </tr>
	    <tr>
	      <td>application_fee_percent</td>
	      <td>% charged for the subscription</td>
	    </tr>
          <tr>
	      <td>billing</td>
	      <td>automatic charge or sending invoice</td>
	    </tr>
          <tr>
	      <td>billing_cycle_anchor</td>
	      <td>time of the next cycle of subscription</td>
	    </tr>
          <tr>
	      <td>current_period_start current_period_end</td>
	      <td>timeframes of current subscription period</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

* **application_fee_percent** – percent of the overall amount the app charges, the rest is paid by the content owner
* **billing** – responsible for how the billing process goes – automatically or manually (through the invoice)
* **billing_cycle_anchor** – contains the due date of the next payment for renewal of the subscription
* **current_period_start & current_period_end** – validity period of customer's subscription
* **plan** – stores the object of a subscription plan, includes a set of rules (amount to pay, interval, number of trial days, and more)

```
{
  "id": "sub_D2JskPBqcW24hu",
  "object": "subscription",
  "application_fee_percent": null,
  "billing": "charge_automatically",
  "billing_cycle_anchor": 1528820423,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "created": 1528820423,
  "current_period_end": 1531412423,
  "current_period_start": 1528820423,
  "customer": "cus_D2Jsi3JgT5zPh1",
  "days_until_due": null,
  "discount": null,
  "ended_at": null,
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_D2Js7N4mYxzAaY",
        "object": "subscription_item",
        "created": 1528820424,
        "metadata": {
        },
        "plan": {
          "id": "ivory-express-917",
          "object": "plan",
          "active": true,
          "aggregate_usage": null,
          "amount": 999,
          "billing_scheme": "per_unit",
          "created": 1528819224,
          "currency": "usd",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {
          },
          "name": "Ivory Express",
          "nickname": null,
          "product": "prod_D2JYysdjdQ2gwT",
          "statement_descriptor": null,
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "quantity": 1,
        "subscription": "sub_D2JskPBqcW24hu"
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_D2JskPBqcW24hu"
  },
  "livemode": false,
  "metadata": {
  },
  "plan": {
    "id": "ivory-express-917",
    "object": "plan",
    "active": true,
    "aggregate_usage": null,
    "amount": 999,
    "billing_scheme": "per_unit",
    "created": 1528819224,
    "currency": "usd",
    "interval": "month",
    "interval_count": 1,
    "livemode": false,
    "metadata": {
    },
    "name": "Ivory Express",
    "nickname": null,
    "product": "prod_D2JYysdjdQ2gwT",
    "statement_descriptor": null,
    "tiers": null,
    "tiers_mode": null,
    "transform_usage": null,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "quantity": 1,
  "start": 1528820423,
  "status": "active",
  "tax_percent": null,
  "trial_end": null,
  "trial_start": null
}
```

## Use Cases

Finally, we move to use cases. So let’s find out how we build the business logic using Stripe.

### Subscriptions 

**Case**: Users pay $5/month for getting access to the content. Its author earns 80% of the overall cost. Customers have five trial days. 

**How to make it work:**  


1. Create the subscription plan in Stripe, specify the cost, % of app fee, and the interval.
2. Integrate webhooks for the server to understand when someone subscribes and when they’re charged.
3. Integrate emails to send users invoices/receipts.
4. When a user buys the subscription, Stripe counts down five days from that moment and then makes the charge.
5. The author gets money, the platform gets its fee. 

**Fee**: 2.9% + 30 cents

### Content purchase

  
**Case**: Users purchase content on a website or mobile application. 

**How to make it work:**

1. The customer tokenizes a card.
2. Backend makes the Charge.
3. If the Charge is successful, the platform's business logic allows the customer to get the content. 

**Fees**: 2.9% from the charge + 30 cents.

### On-demand platform (Uber)

**Case**: The client pays for the ride, the platform charges 20%, the driver gets 80%. 

**Preconditions**: 

* Driver linked an account
* User added a card

In this case, you need to create transfers on your own after the rider completes the payment. 

First, authorize the payment when they book the ride and capture it when the ride's complete. 

Next, create a transfer for the driver – 80% of the total sum. Pay the Stripe fee, and the rest will be the net income. 

**And the fee is**: 2.9% + 30 cents

### On-demand platform #2

Uber-like apps are perfect for showing how Stripe works. So here goes another use case.

**Case**: Customer pays for the service, the platform charges 20%, the driver gets 80%. Plus, the driver can pay $5 for the priority booking right. 

Works if the driver linked their account, and the rider added a credit card. 

* **Variant #1.** You charge $5 from the driver (in case of the priority option), authorize payment for the customer, do the capture when the ride ends, make a transfer for the driver. And keep the rest. In this case, you pay 2.9% fee + 30 cent for each charge. 
* **Variant #2.** You can skip fees by creating the inner monetization on your platform. When you get money from the customer, you calculate the driver's share and transfer those funds to the inner balance.

![Image](https://lh4.googleusercontent.com/PTXyrViF0NXh83Ej8kGdol0jENOP65cgCV3MBcodPJhr6KZ4vsoCOfa9CTQCCRwKdNYG5S9Wh-i3Jdq41SAs6JJxvPAiP-zs16dXNhdbVIsLwZMG6_VaNKt28_2VC_CY73Qku5jo)
_Cashflow_

## In conclusion

  
As you see, the implementation of payment logic and its testing are not as hard as they seem. All you need to do is handle the Stripe objects in the right way. And figure out how to use Stripe on your platform.  
  
I hope this guide will come handy when you get started with designing Stripe-based payment logic and its testing.

