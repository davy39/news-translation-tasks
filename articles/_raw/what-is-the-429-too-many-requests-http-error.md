---
title: 429 Error – Too Many Requests HTTP Code Explained
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-28T15:45:26.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-429-too-many-requests-http-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/429.png
tags:
- name: beginner
  slug: beginner
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: null
seo_desc: 'Whether you are a web developer or you are a regular internet user, you
  might have encountered a 429 error. It means that the website can''t handle the
  number of requests being sent to it.

  For a developer, this error can be hard to resolve because, on...'
---

Whether you are a web developer or you are a regular internet user, you might have encountered a 429 error. It means that the website can't handle the number of requests being sent to it.

For a developer, this error can be hard to resolve because, on many occasions, it doesn’t show what you need to do to fix it.
![deve-429](https://www.freecodecamp.org/news/content/images/2022/06/deve-429.png)

But if you’re surfing the net as a user and you encounter the error, there could be a hint showing what to do.
![429-clinet](https://www.freecodecamp.org/news/content/images/2022/06/429-clinet.png)

In this case, you should wait a bit to make another request. For security reasons, the period of time to wait might not be specified. But if the website proritzes user experience, they'll show you how much time to wait before making another request.

In this article, I will explain what the 429 error means and how a developer might have implemented it. I will also show what you can do to resolve it as an internet user.

## What is the 429 Error?

The 429 error is an HTTP status code. It tells you when the use of an internet resource has surpassed the number of requests it can send within a given period of time.

This error might be shown to you in another form like:
- Error 429 
- 429 Too many requests
- 429 (Too many requests)

It all depends on how the administrator in charge of the internet resource customizes it.

In the small app I built to show you how rate limiting is implemented in an Express app, this is how I customized the error:
![custom429](https://www.freecodecamp.org/news/content/images/2022/06/custom429.png)

With this error, the administrators in charge of a website or internet resource are telling you they don’t have enough resources to handle the number of requests you are sending over. This is called “rate limiting”.


## What Causes the 429 Error?

The most common cause of the 429 error is not having enough resources to handle so many concurrent requests. 

For example, if this error is shown on a hosting server, it could mean that the package you’re using has a limit for the number of requests you can send. 

And if the error comes up while making an API request, it means you’ve exceeded the number of requests you can make for a certain period of time.

Also, if a user tries to access a page on a website too often, the server of that website could trigger a rate-limiting feature implemented in it. So, this is a good security measure to put in place in order to prevent attacks from hackers.

For example, this is how you can implement rate limiting in an Express app using the [express-rate-limit package](https://www.npmjs.com/package/express-rate-limit):

```js
// Import deps
const express = require("express");
const rateLimit = require("express-rate-limit");

const app = express();

// Port
const port = 4000;

const limiter = rateLimit({
  windowMs: 5 * 60 * 1000,
  max: 5, // Limits each IP to 5 per 15 minutes
  message:
    `<h1 style='display:flex; align-items:center; justify-content:center; height:100vh'>
     429 - Too many Requests <br> Try again later!
    </h1>`,
});

// Apply to all requests
app.use(limiter);

app.get("/", limiter, (req, res) => res.send("Hello World!"));

app.listen(port, () => console.log(`App listening on port ${port}!`));

```

And when the limit is surpassed for the number of seconds specified, this message gets shown to the user:
![custom429](https://www.freecodecamp.org/news/content/images/2022/06/custom429.png)

## What you can do to Resolve the 429 Error

As an internet user, you should wait a bit before making another request. But if the error persists, you should contact the website administrator.

If you’re a web administrator, you should reduce the number of requests you make within the specified time (if any). If you are in control of the limit yourself, you should increase it for a particular period of time.

If the website you’re handling is a WordPress website, one of your plugins or themes might be causing the 429 error. You should disable your site plugins and themes one by one to see which one of them is the cause.

If the error is related to hosting, you should contact the customer care service of your hosting provider.


## Conclusion

No website admin wants their server to get clunked up or crash. So, from a technical perspective, the 429 error is not an error. It’s the server’s way of telling you it doesn’t have enough resources to handle the high number of requests you’re making.

Thank you for reading.


