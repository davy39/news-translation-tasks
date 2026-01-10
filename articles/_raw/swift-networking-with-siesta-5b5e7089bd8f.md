---
title: Let me introduce you to Swift networking with Siesta — my new favorite library.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T20:47:47.000Z'
originalURL: https://freecodecamp.org/news/swift-networking-with-siesta-5b5e7089bd8f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YAavX2qseMIP_llujYfguA.png
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nikolay Derkach

  Today I’d like to tell you about my new favorite iOS networking library called Siesta.
  “What’s so great about it, and why can’t I just use Alamofire?” you might ask. Actually,
  you can use Alamofire with Siesta! Because it’s a netwo...'
---

By Nikolay Derkach

Today I’d like to tell you about my new favorite iOS networking library called [Siesta](https://github.com/bustoutsolutions/siesta). “What’s so great about it, and why can’t I just use Alamofire?” you might ask. Actually, you can use Alamofire with Siesta! Because it’s a networking abstraction layer above HTTP clients.

But unlike libraries like [Moya](https://github.com/Moya/Moya), this one doesn’t hide HTTP from you. This gives you a great middle ground, and that’s exactly how I like to consume my REST APIs.

By adopting a resource-centric approach, rather than a request-centric one, Siesta provides an **app-wide observable model of a RESTful resource’s state**.

What does this mean? It means avoiding unnecessary network requests and redundant response deserialization. It decouples view controllers from network request lifecycles. It provides transparent response parsing out of the box. [And much more.](https://github.com/bustoutsolutions/siesta)

In this tutorial, I’d like to show you how to get started with this awesomeness and make your networking great again, swiftly ?

### Setup

Install it from Cocoapods:

```
pod 'Siesta', '~> 1.0'
```

For the purposes of this tutorial, I built a [simple CRUD app](https://github.com/nderkach/cashman) with a REST API and JWT-based authentication which I [deployed to Heroku](https://jwt-api-siesta.herokuapp.com).

To get started, create a separate class for your API. Let’s call it `AwesomeAPI.swift`

Let’s define a basic API configuration here:

Here we define a global singleton for our API. We configure the service with the URL for our API and `standardTransformers` which are default parsers for text and image responses. We also enable logging in debug mode, which is very useful for debugging requests against your API. Finally, we define our first _resource accessor,_ a public method of our API class returning a resource which we are now going to use in our view controller.

To fetch the data from our newly defined resource we need to create a _resource observer_ in our view controller:

Here we add a _resource observer_ to our `ping` resource, and define a delegate method which is called when the resource’s state is changed. A state could change when an observer is added or when it has some new data, for example.

Because Siesta allows you to decouple request configuration from request initialization, you can request a resource without worrying about nitty-gritty details of how it would be requested.

For example, you don’t need to worry `loadIfNeeded` too often, since Siesta allows you to avoid redundant requests. The default expiration time for a resource is 30 seconds and is configurable.

Now, if you run your app, you should hopefully see something like this:

```
Siesta:network        │ GET https://jwt-api-siesta.herokuapp.com/ping
```

```
Siesta:network        │ Response:  200 ← GET https://jwt-api-siesta.herokuapp.com/ping
```

```
pong
```

### Transformers

Let’s do something more fun. Let’s define some _transformers_ which would automatically decode out raw JSON response into a data model.

In our API we have an endpoint `/status` which returns

```
{  "text": "ok"}
```

To decode JSON on the backend, we are going to use [JSONDecoder](https://developer.apple.com/documentation/foundation/jsondecoder), a recent addition to Swift 4.

First, we are going to add a transformer like this:

`[String: String]` means that we expect a string-to-string mapping dictionary in our JSON response.

Then, we need to update our view controller with resource observer.

As you noticed here, to decode the JSON we are using `typedContent()` when unwrapping the optional. In this case, we need to explicitely provide a data type (`[String: String]`) otherwise the data type cannot be inferred. Likewise, we can rewrite the previous resource observer for `/ping` endpoint like this:

### Authentication

In our API we have a couple of authenticated endpoints: `/incomes` and `/expenses`. To access them, we’d need to obtain a JWT token first. Let’s define a method to authenticate requests. This time, instead of creating a function that returns a _Resource_, we are going to make one returning a `Request.` This would be a way to handle everything besides _GET_ requests on your API.

First, we are going to add a class property, which would store the JWT authentication token:

Every time this property is set, we want to invalidate our service configuration so that the next time a resouce is fetched, request headers would be refreshed. This is necessary because you’ll likely send your authentication token either in a cookie or in _Authorization_ header.

Also consider storing your authentication token in the Keychain, rather than in `NSUserDefaults` or other insecure storage. We are using JWTDecode library here to decode a JWT token and obtain its expiration date.

After that, we also want to automatically refresh the token once it expires. In a more sophisticated implementation of JWT we’d get a _refresh token_ alongside, which we’d later use to refresh our authentication token. In our case, we have a simple JWT implementation, and we are just going to send the login response again.

Here is how you can implement the login request in your _AwesomeAPI_ class to obtain an authentication token:

Here we send a POST to `/login` with user credentials in a JSON payload. We also define two closures: `onSuccess` and `OnFailure` and we store an authentication token on a successful authentication.

Finally, we want to automatically update our authentication token _before_ it expires. We can use a single-shot timer for that:

Yes, the actual login credentials for our test API are _test_ and _test._ You can easily integrate the `AwesomeAPI.login()` call in your login flow by obtaining credentials from a view controller responsible for the login. To successfully decode the response from the login request, you need to define a transformer for it as well:

The API requires us to pass the JWT token in the _Authorization_ header. In order to do that, we can add the following to our service configuration (`init()` ):

Now that we have our request authenticated, let’s try to make some requests to authenticated resources, like `/expenses.` This endpoint returns a list of the following dictionaries:

```
{    "amount": -50.0,    "created_at": "2017-12-07T16:00:52.988245",    "description": "pizza",    "type": "TransactionType.EXPENSE"}
```

Our goal is to create a model to store the response of this format. Let’s create a class called _Expense._ As we are using _JSONDecoder_ here, we just need to inherit our class from _Codable:_

The _CodingKeys_ enum allows us to map field names in our JSON response to the struct’s property names. Note that we are also decoding dates here (`createdAt`). Since our date has a custom format, we need to configure that via _JSONDecoder_’s `dateDecodingStrategy`:

Finally, let’s create a transformer for this class:

We are using `[Expense]` here as we are expecting an array of _Expense_ objects.

After defining an `expenses()` resource accessor the same way as we did previously, we can fetch our authenticated resource like this:

### One last thing…

One last thing I want to show you is what to do when your authentication token expires. What we could do with Siesta, for example, is automatically authenticate and retry a failed request.

First, we need to add the following to our configuration:

Then we chain our request and repeat it with a new token!

If you want to check out the final project, it’s available on [Github](https://github.com/nderkach/AwesomeAPI).

Happy hacking!

