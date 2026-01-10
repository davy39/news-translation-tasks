---
title: HTTP 401 Error vs HTTP 403 Error – Status Code Responses Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-24T05:00:00.000Z'
originalURL: https://freecodecamp.org/news/http-401-error-vs-http-403-error-status-code-responses-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a15740569d1a4ca2366.jpg
tags:
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: null
seo_desc: "By Jackson Bates\nWe've covered the 403 (Forbidden) HTTP Error code in\
  \ some detail before, but it also has a near identical sibling. \nSo what exactly\
  \ is the difference between the 401 (Unauthorized) and 403 (Forbidden) status codes?\
  \ Surely they mean t..."
---

By Jackson Bates

We've covered the [403 (Forbidden) HTTP Error](https://www.freecodecamp.org/news/http-error-403-forbidden-what-it-means-and-how-to-fix-it/) code in some detail before, but it also has a near identical sibling. 

So what exactly is the difference between the 401 (Unauthorized) and 403 (Forbidden) status codes? Surely they mean the same thing? Let's take a closer look!

## RFC Standards

The most up to date RFC Standard defining 401 (Unauthorized) is [RFC 7235](https://tools.ietf.org/html/rfc7235#section-3.1)

> The 401 (Unauthorized) status code indicates that the request has not been applied because it lacks valid authentication credentials for the target resource...The user agent MAY repeat the request with a new or replaced Authorization header field.

Whereas 403 (Forbidden) is most recently defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3)

> The 403 (Forbidden) status code indicates that the server understood the request but refuses to authorize it...If authentication credentials were provided in the request, the server considers them insufficient to  grant access.

## Common Causes

As mentioned in the previous article, the 403 error can result when a user has logged in but they don't have sufficient privileges to access the requested resource. For example, a generic user may be attempting to load an 'admin' route.

The most obvious time you'd encounter a 401 error, on the other hand, is when you have not logged in at all, or have provided the incorrect password.

These are the two most common causes for this pair of errors.

## Less Common Causes

There are some instances where it's not quite as straightforward as that, though.

403 errors can occur because of restrictions not entirely dependent on the logged in user's credentials. 

For example, a server may have locked down particular resources to only allow access from a predefined range of IP addresses, or may utilize geo-blocking. The latter can be potentially circumvented with a VPN.

401 errors can occur even if the user enters the correct credentials. This is rare, and might be something you only really encounter while developing your own authenticated back ends. But if the authorization header is malformed it will return a 401. 

For example, you might have a JWT (JSON Web Token) you want to include in the request header, which expects the format `Authorization: Bearer eyJhbGci......yJV_adQssw5c`. If you were to forget the word 'Bearer' before the JWT, you would encounter the 401 error. 

I have run in to this problem myself when testing APIs under development with Postman and forgetting the correct syntax for auth headers! 

## That's it

I hope this clears up any confusion surrounding these very similar errors.

If you found this helpful, or wish to challenge or extend anything raised here, feel free to contact me on Twitter [@JacksonBates.](https://twitter.com/JacksonBates)

