---
title: The Access-Control-Allow-Origin Header Explained – With a CORS Example
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-07-17T07:18:00.000Z'
originalURL: https://freecodecamp.org/news/access-control-allow-origin-header-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99aa740569d1a4ca210e.jpg
tags:
- name: CORS
  slug: cors
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Often times when calling an API, you may see an error in your console that
  looks like this:


  Access to fetch at ''http://somesite.com'' from origin ''http://yoursite.com'' has
  been blocked by CORS policy: The ''Access-Control-Allow-Origin'' header has a va...'
---

Often times when calling an API, you may see an error in your console that looks like this:
```

Access to fetch at 'http://somesite.com' from origin 'http://yoursite.com' has been blocked by CORS policy: The 'Access-Control-Allow-Origin' header has a value that is not equal to the supplied origin

```

In this post, we are going to learn why this error happens and how you can fix it. 


## What is the `Access-Control-Allow-Origin` header?
`Access-Control-Allow-Origin` is a CORS header. CORS, or Cross Origin Resource Sharing, is a mechanism for browsers to let a site running at origin A to request resources from origin B. 

Origin is not just the hostname, but a combination of port, hostname and scheme, such as - `http://mysite.example.com:8080/`


Here's an example of where this comes into action - 
1. I have an origin A: `http://mysite.com` and I want to get resources from origin B: `http://yoursite.com`. 
2. To protect your security, the browser will not let me access resources from yoursite.com and will block my request. 
3. In order to allow origin A to access your resources, your origin B will need to let the browser know that it is okay for me to get resources from your origin.


Here is an example from Mozilla Developer Network that explains this really well:


![Image](https://www.freecodecamp.org/news/content/images/2020/07/CORS_principle.png)

With the help of CORS, browsers allow origins to share resources amongst each other. 

There are a [few headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#The_HTTP_response_headers) that allow sharing of resources across origins, but the main one is  `Access-Control-Allow-Origin`. This tells the browser what origins are allowed to receive requests from this server. 


## Who needs to set `Access-Control-Allow-Origin`?

To understand who needs to set this header, consider this scenario: You are browsing a website that is used to view and listen to songs. The website attempts to make a connection to your bank in the background maliciously. 

So who has the ultimate ability to prevent this malicious website from stealing your data from the bank? The bank! So, the bank will need to protect its resources by setting the `Access-Control-Allow-Origin` header as part of the response.

Just remember: the origin responsible for serving resources will need to set this header.


## How to use and when to pass this header 
Here's an example of values you can set: 

1. `Access-Control-Allow-Origin : *` : Allows any origin.
2. `Access-Control-Allow-Origin : http://mysite.com` : Allow requests only from mysite.com.


## See it in action

Let's look at an example. You can check out this code [on my GitHub repo](https://github.com/shrutikapoor08/blogs/tree/master/code-examples/CORS). 

We are going to build a server on origin A `http://localhost:8000` which will send a string of `Hello`s to an `api` endpoint. We are going to call with this endpoint by creating a client on origin B `http://localhost:3000` and then use fetch to request the resource. We expect to see the string `Hello` passed by origin A in the browser console of origin B. 


Let's say we have an origin up on `http://localhost:8000` that serves up this resource on `/api` endpoint. The server sends a response with the header `Access-Control-Allow-Origin`.

```
const express = require("express");

const app = express();
const port = process.env.SERVER_PORT || 8000;

// Add Access Control Allow Origin headers
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "https://yoursite.com");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.get("/api", (req, res) => {
  res.json("Hello");
});

app.listen(port, () => console.log(`Listening on port ${port}`));

```

On the client side, you can call this endpoint by calling `fetch` like this: 

```
fetch('http://localhost:8000/api')
.then(res => res.json())
.then(res => console.log(res));

```
Now open your browser's console to see the result. 
Since the header is currently set to allow access only from `https://yoursite.com`, the browser will block access to the resource and you will see an error in your console.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CORS-access-denied.png)

Now, to fix this, change the headers to this:

```
 res.setHeader("Access-Control-Allow-Origin", "*");

```

Check your browser's console and now you will be able to see the string `Hello`.

### Interested in more tutorials and JSBytes from me? Sign up for my newsletter.

