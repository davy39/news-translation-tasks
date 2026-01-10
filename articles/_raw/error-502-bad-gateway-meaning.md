---
title: Error 502 Bad Gateway Meaning
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-08T20:21:52.000Z'
originalURL: https://freecodecamp.org/news/error-502-bad-gateway-meaning
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/502b.png
tags:
- name: error
  slug: error
- name: http
  slug: http
seo_title: null
seo_desc: "When you visit a website and you get a “502 Bad Gateway” error, it means\
  \ there’s an issue with the servers powering the website.  \nOn many occasions,\
  \ this error is an issue with the website itself, so on your end, there’s nothing\
  \ you can do to solve ..."
---

When you visit a website and you get a “502 Bad Gateway” error, it means there’s an issue with the servers powering the website.  

On many occasions, this error is an issue with the website itself, so on your end, there’s nothing you can do to solve it. 

But the error can also occur if your network adapters or network settings of your computer are badly configured. 

The “502” in the error is an HTTP status code that indicates one server received an invalid response from another server.

Google shows the error this way:
![502-error](https://www.freecodecamp.org/news/content/images/2022/06/502-error.png)

Sometimes, a popular forum in my country shows it this way:
![cloudflare-502-bad-gateway-error](https://www.freecodecamp.org/news/content/images/2022/06/cloudflare-502-bad-gateway-error.png)

It looks like websites powered by Cloudflare show the error that way.

Some other websites show it in their own customized way.

## What Exactly Does 502 Bad Gateway Mean?

The international engineering task force (IETF) defines the 502 Bad Gateway Error in a more extensive way:

> The 502 (Bad Gateway) status code indicates that the server while acting as a gateway or proxy, received an invalid response from an inbound server it accessed while attempting to fulfill the request.

The “proxy server” is a system or router that acts as a gateway between your computer and the internet. 

The inbound server, on the other hand, is the one conveying an incoming connection onto your computer. That is, a web server.

## What Causes a Bad Gateway Error?

As earlier pointed out, 502 Bad Gateway is a server error just like other HTTP status code errors in the 500 range such as 501 (Not Implemented), 503 (Service Unavailable), 504 (Gateway Timeout), and 505 (HTTP Version not supported).

This particular server error could be an overloaded server, programming, and backend configuration error, or even a yet-to-be-propagated domain name.

But sometimes, the browser could throw this error due to past-due updates, ad-blockers, browser extensions, or computer DNS server problems.


## Final Thoughts 

I hope this article helps you understand what the 502 Bad Gateway error means.

If you’re a web administrator and your users are complaining of this error, you should try to fix it as soon as possible as it could have a negative effect on your website's SEO.

If you’re facing this error as a user, there’s a high chance it’s from the website you’re trying to visit. Some other times, it could be due to a badly configured router and settings.

You can try refreshing the web page, clearing your browser cache, and switching to another browser.

To see how you can solve the error as a user, I wrote [a detailed article that can help you out.](https://www.freecodecamp.org/news/502-bad-gateway-error-solved/)

Thank you for reading.


