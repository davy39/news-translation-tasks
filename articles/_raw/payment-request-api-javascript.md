---
title: How to Use the Payment Request API in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-24T22:40:51.000Z'
originalURL: https://freecodecamp.org/news/payment-request-api-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/js-payment-request.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: payments
  slug: payments
seo_title: null
seo_desc: "By  Atta ✨\nThe Payment Request API provides a cross-browser standard that\
  \ lets you collect payments, addresses, and contact information from your customers.\
  \ You can then use this info to process their order. \nIt also facilitates the exchange\
  \ of this ..."
---

By  Atta ✨

The Payment Request API provides a cross-browser standard that lets you collect payments, addresses, and contact information from your customers. You can then use this info to process their order. 

It also facilitates the exchange of this information between the browser and the website. The fundamental idea behind this is to improve the user's online shopping experience by making it easy for users to store payment and contact information in the browser.

## Payment Request API Browser Support

The Payment Request API is still in active development and is only supported by the [last few versions](https://caniuse.com/#feat=payment-request) of modern browsers. 

Before you start making a payment request, you should feature detect to ensure that the API is supported by the browser:

```javascript
if (window.PaymentRequest) {
  // Yes, we can use the API
} else {
  // No, fallback to the checkout page
  window.location.href = '/checkout'
}
```

Note that you can only use the Payment Request API on sites serving over `https`.

Now let's see how this helpful API works.

## How to Create the PaymentRequest Object

A payment request is always started by creating a new object of `PaymentRequest` - using the `PaymentRequest()` constructor. The constructor takes two mandatory parameters and one optional parameter:

* `paymentMethods` defines which forms of payment are accepted. For example, you may only accept Visa and MasterCard credit cards.
* `paymentDetails` contains the total payment amount due, taxes, shipping cost, display items, and so on.
* `options` is an optional argument used to request additional details from the user, such as name, email, phone, and so on.

Next we'll create a new payment request with only the required parameters.

### How to use the `paymentMethods` parameter

```javascript
const paymentMethods = [
  {
    supportedMethods: ['basic-card']
  }
]

const paymentDetails = {
  total: {
    label: 'Total Amount',
    amount: {
      currency: 'USD',
      value: 8.49
    }
  }
}

const paymentRequest = new PaymentRequest(paymentMethods, paymentDetails)
```

Notice the `supportedMethods` parameter in the `paymentMethods` object. When it is set to `basic-card`, both debit and credit cards of all networks will be accepted. 

But you can limit the supported networks and types of cards. For example, with the following only Visa, MasterCard, and Discover credit cards are accepted:

```javascript
const paymentMethods = [
  {
    supportedMethods: ['basic-card'],
    data: {
      supportedNetworks: ['visa', 'mastercard', 'discover'],
      supportedTypes: ['credit']
    }
  }
]
// ...
```

### How to use the `paymentDetails` object

The second parameter passed to the `PaymentRequest` constructor is the payment details object. It contains the total of the order and an optional array of display items. The `total` parameter must include a `label` parameter and an `amount` parameter with `currency` and `value`.

You can also add additional display items to provide a high-level breakdown of the total:

```javascript
const paymentDetails = {
  total: {
    label: 'Total Amount',
    amount: {
      currency: 'USD',
      value: 8.49
    }
  },
  displayItems: [
    {
      label: '15% Discount',
      amount: {
        currency: 'USD',
        value: -1.49
      }
    },
    {
      label: 'Tax',
      amount: {
        currency: 'USD',
        value: 0.79
      }
    }
  ]
}
```

The `displayItems` parameter is not meant to display a long list of items. Since space is limited for the browser's payment UI on mobile devices, you should use this parameter to display only top-level fields such as subtotal, discount, tax, shipping cost, and so on.

Keep in mind that the `PaymentRequest` API does not perform any calculations. So your web application is responsible for providing the pre-calculated `total` amount.

### How to use the `options` argument to request additional details

You can use the third optional parameter to request additional information from the user, such as name, email address, and phone number:

```javascript
// ...
const options = {
  requestPayerName: true,
  requestPayerPhone: true,
  requestPayerEmail: true
}

const paymentRequest = new PaymentRequest(paymentMethods, paymentDetails, options)
```

By default, all of these values are `false`, but adding any of them to the `options` object with a value `true` will result in an extra step in the payment UI. If the user has already stored these details in the browser, they will be pre-populated.

## How to Display the Payment UI

After creating a `PaymentRequest` object, you must call the `show()` method to display the payment request UI to the user. 

The `show()` method returns a [promise](https://www.freecodecamp.org/news/javascript-promises-for-beginners/) that resolves with a `PaymentResponse` object if the user has successfully filled in the details. If there is an error or the user closes the UI, the promise rejects.

```javascript
// ...
const paymentRequest = new PaymentRequest(paymentMethods, paymentDetails, options)

paymentRequest
  .show()
  .then(paymentResponse => {
    // close the payment UI
    paymentResponse.complete().then(() => {
      // TODO: call REST API to process the payment at the backend server
      // with the data from `paymentResponse`.
    })
  })
  .catch(err => {
    // user closed the UI or the API threw an error
    console.log('Error:', err)
  })
```

With the above code, the browser will show the payment UI to the user. Once the user has filled in the details and clicked on the 'Pay' button, you will receive a `PaymentResponse` object in the `show()` promise. 

The payment request UI is closed immediately when you call the `PaymentResponse.complete()` method. This method returns a new promise so that you can call the backend server with the information collected and process the payment.

![Payment Request UI](https://cdn.attacomsian.com/gims/da91575d-9de1-448e-92dc-9c255083f271.jpg)

If you want to call the backend server to process the payment while the payment UI is showing a spinner, you can delay the call to `complete()`. 

Let's create a mock function for payment processing with the backend server. It takes `paymentResponse` as a parameter and returns a promise after 1.5 seconds that resolves to a [JSON object](https://www.freecodecamp.org/news/what-is-json-a-json-file-example/):

```javascript
const processPaymentWithServer = paymentResponse => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ status: true })
    }, 1500)
  })
}

//...
paymentRequest
  .show()
  .then(paymentResponse => {
    processPaymentWithServer(paymentResponse).then(data => {
      if (data.status) {
        paymentResponse.complete('success')
      } else {
        paymentResponse.complete('fail')
      }
    })
  })
  .catch(err => {
    console.log('Error:', err)
  })
```

In the example above, the browser payment UI will show a processing screen until the promise returned by the `processPaymentWithServer()` method is settled. We also used 'success' and 'fail' strings to tell the browser about the transaction outcome. The browser will show an error message to the user if you call `complete('fail')`.

## How to Cancel a Payment Request

If you want to cancel the payment request due to no activity or any other reason, you can use the `PaymentRequest.abort()` method. It immediately closes the payment request UI and rejects the `show()` promise.

```javascript
// ...
setTimeout(() => {
  paymentRequest
    .abort()
    .then(() => {
      // aborted payment request
      console.log('Payment request aborted due to no activity.')
    })
    .catch(err => {
      // error while aborting
      console.log('abort() Error: ', err)
    })
}, 5000)
```

## Conclusion

That's the end of a quick introduction to the JavaScript Payment Request API. It provides a browser-based method to collect customer payment and contact information that can be sent to the backend server to process the payment. 

The aim is to reduce the number of steps in completing an online payment. It makes the whole checkout process smoother by remembering the user's preferred way of paying for goods and services.

If you want to learn more about the Payment Request API, here is a [good resource](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API) that discusses the main concepts and usage of the API.


## Thank you for reading!

If you want to learn more about JavaScript, you may want to check out my [personal blog](https://attacomsian.com/), where I have published over 235 tutorials on JavaScript objects, arrays, strings, Web APIs, and more.

I am also the founder of [AcquireBase](https://acquirebase.com). You can follow me on [Twitter](https://twitter.com/attacomsian) to receive updates when I publish new tutorials or share side projects. 


