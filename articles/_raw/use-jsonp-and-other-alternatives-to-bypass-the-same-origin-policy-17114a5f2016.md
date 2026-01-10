---
title: How to use JSON padding (and other options) to bypass the Same Origin Policy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T00:00:51.000Z'
originalURL: https://freecodecamp.org/news/use-jsonp-and-other-alternatives-to-bypass-the-same-origin-policy-17114a5f2016
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zbemC10taSnmtxa1n2Tw0w.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anthony Ng

  In this article, we will be looking at what JSONP is, its drawbacks, and some alternatives
  to JSONP.

  You may have run into situations where you make an API call from one origin to another.
  For example, we have a page served from localho...'
---

By Anthony Ng

In this article, we will be looking at what JSONP is, its drawbacks, and some alternatives to JSONP.

You may have run into situations where you make an API call from one origin to another. For example, we have a page served from localhost:3000 that is calling an API from localhost:8000.

**Note**: We will refer to localhost:3000 as our client server. We will refer to localhost:8000 as our API server.

But we see this intimidating error.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hr7T_kBgvnZwzSDdGF3E9w.png)
_Error when trying to make fetch call from client server to api server_

This is the Same-Origin Policy protecting us. This policy restricts how resources from one origin interact with resources from another origin. It is a critical security mechanism in the browser. But there are instances where we want to make cross-origin requests to trusted resources.

JSONP (JSON with Padding) provides a work-around for this Same-Origin Policy problem. Let’s look at how JSONP came to be.

### Technical dive

We can run JavaScript code inside our HTML file with `<scri`pt> tags.

We can move our JavaScript code into a separate JavaScript file and reference it with our script tag. Our webpage now makes an external network call for the JavaScript file. But functionally, everything works the same.

The Javascript file doesn’t have to have a `js` extension. The browser will interpret content as JavaScript if the Response’s Content-Type is JavaScript. (`text/javascript`, `application/javascript`).  
Most servers allow you to set the content type. In [Express](https://expressjs.com), you would do:

![Image](https://cdn-media-1.freecodecamp.org/images/1*llfbidT6kG5hfSNdfc2nlw.png)
_Setting Content-Type header for Response_

Your `<scri`pt> tag can reference a URL that doesn’t h`av`e a js extension.

Script tags are not limited by the Same-Origin Policy. There are other tags, such as `<i`mg>`; and &`lt;video> tags, that are not limited by the Same-Origin Policy. So our JavaScript can live on a different origin.

The code inside the JavaScript file has access to everything that is in scope. You can use functions defined earlier in your HTML file.

You can pass arguments as you would for a normal function call.

In the above example, we passed a hard-coded string. But we could also pass in data coming from a database. Our API server can construct the JavaScript file with this dynamic information.

This is what JSONP is. Instead of using `[fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)` or `[XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)` to make an API call to retrieve data, we used a `<scri`pt> tag. Because we u`sed a &l`t;script> tag, we were able to bypass the Same-Origin Policy.

As I mentioned above, JSONP means JSON with Padding. What does the padding mean? Normal API responses return JSON. In JSONP responses, we return the JSON response surrounded (or padded) with a JavaScript function.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zbemC10taSnmtxa1n2Tw0w.png)
_Artist rendition of JSON with Padding_

Most servers allow you to specify the name of your padding function.

The server takes your padding function name as a query. It invokes your padding function with the JSON data as an argument.

You are not limited to passing function names as your callback. You can pass inline JavaScript in your query.

I have not thought of a reason to do this.

### Alternatives to using JSONP

There is no official spec for JSONP. I think of JSONP as more of a hack.

`<scri`pt> tags can only make GET requests. So JSONP can only make GET requests.

[Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) has an official specification, and is the preferred way of getting around the Same-Origin Policy.

You can enable Cross-Origin Resource Sharing by adding a header to our Response.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CdIror6QvF0F1e82W1WbPA.png)

This means all origins can use this resource without fear of the Same-Origin Policy.

Sometimes, you don’t have control over the server-code though. You would not be able to include the `Access-Control-Allow-Origin` header. An alternate solution is to make your own proxy server make the cross-origin request for you. The Same-Origin policy only applies to the browser. Servers are free to make cross-origin requests.

Questions? Comments? Please leave a message below.

### Resources

* [Same Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
* [Github Repository with JSONP and CORS examples](https://github.com/newyork-anthonyng/jsonp-example.)
* [Detailed explanation of JSONP](https://web.archive.org/web/20160304044218/http://www.json-p.org/)

