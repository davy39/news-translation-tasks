---
title: HTTP Error 504 – 504 Gateway Timeout Status Code Explained
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-12T20:21:09.000Z'
originalURL: https://freecodecamp.org/news/http-error-504-gateway-timeout-status-code-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/error.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: null
seo_desc: "While surfing the internet, we are able to interact with web servers through\
  \ HyperText Transfer Protocol (HTTP) requests. These requests are sent from the\
  \ client (our browsers) to the server before we get a response. \nHTTP status codes\
  \ allows us know..."
---

While surfing the internet, we are able to interact with web servers through HyperText Transfer Protocol (HTTP) requests. These requests are sent from the client (our browsers) to the server before we get a response. 

HTTP status codes allows us know if our request to the server was successful or not. Here are the status codes and what each type means:

* 100 - 199 (Informational).
* 200 - 299 (Successful).
* 300 - 399 (Redirection).
* 400 - 499 (Client error).
* 500 - 599 (Server error).

In this article, we'll be talking about the 504 error which falls under the server error category. We'll see some of the reasons why you might encounter this error and the possible ways of fixing it.

## What Is the HTTP 504 Error?

From the status codes listed before this section, we can see that the 504 error is a server error. This means that it is not a problem from our end as the client. Our request was sent successfully to the server but something went wrong while we were awaiting a response. 

You'll usually get a response saying "Gateway Timeout Error" or something similar if it is a 504 error.

This error occurs when our server doesn't receive a response fast enough from the server where our request was sent. As a result of the delay, our server times out and returns an error instead.

The reasons for this error can vary. The server where the request was sent to could be down for maintenance or overloaded, amongst other reasons.

## How to Fix the HTTP 504 Error

In this section, we'll talk about some of the ways in which you can fix the 504 error. 

The following solutions are for users visiting websites:

### Refresh Your Browser

The first thing you should try when you encounter this error is to refresh your browser. Each browser usually has a shortcut for refreshing, but you can always use the refresh button.

### Disconnect and Reconnect Your Network Devices

If refreshing your browser doesn't fix the problem then you should try disconnecting from and reconnecting to your network devices. This could be a modem, a router, a Wi-Fi hotspot, and so on. 

### Clear Browser Data and Cookies

Each browser has a way of clearing data and cookies but this is usually in the browser settings. 

While this may fix the problem, you should know that in most cases, it doesn't – so be sure you are willing to get rid of the data and cookies before proceeding.

### Find Out If Other Users Are Experiencing the Same Problem

If you are on any community platform or know other users who make use of the website then you should probably try and find out from them to see if it is a general problem.

If this is a general problem then you can sit back and relax. The website owners might be up to something on the backend.

Note that trying these fixes above may not work all the time. In situations like this, the best thing to do is to wait and try later because it is usually not a problem from your end as the client. 

The following solutions are for you if you own a website:

### Contact Your Hosting Provider

In cases where the website belongs to you and users cannot access it, you should try contacting your hosting provider to be sure everything is in check. 

It could be as a result of your hosting plan requiring an upgrade because you may have reached the limits of your current plan.

### Check for DNS Changes

When you change servers for your website, the DNS information changes will usually take some time before updating. So you can inform your users of changes like this before or after they happen.

DNS stands for Domain Name System. They change domain names to IP addresses which browsers can easily recognize before loading websites.

## Conclusion

In this article, we talked about the HTTP 504 error. We talked about HTTP status codes and found out what category the 504 error belonged to.

We then talked about why this error might happen and some of the possible ways of fixing it.

Thank you for reading!


