---
title: Here’s how I could’ve ridden for free with Uber
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-26T10:43:53.000Z'
originalURL: https://freecodecamp.org/news/how-anyone-could-have-used-uber-to-ride-for-free-36cdee5ea854
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cK-cejMVQq51oIX9C7M60A.jpeg
tags:
- name: bug bounty
  slug: bug-bounty
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: uber
  slug: uber
- name: Web App Security
  slug: web-app-security
seo_title: null
seo_desc: 'By AppSecure

  Summary

  This post is about a critical bug on Uber which could have been used by hackers
  to get unlimited free Uber rides anywhere in the world. This post also explains
  few best practices while integrating payment gateways.

  Description

  Ub...'
---

By AppSecure

### Summary

This post is about a critical bug on Uber which could have been used by hackers to get unlimited free Uber rides anywhere in the world. This post also explains few best practices while integrating payment gateways.

### Description

Uber Technologies Inc. is an online transportation network company, headquartered in San Francisco, California, with operations in 528 cities worldwide. Users can create their account on Uber.com and book a ride. When the ride is completed a user can either pay cash or charge it to their credit/debit card.

But, by specifying an invalid payment method (for example, abc, xyz, and so on), I was able to ride Uber for free.

To demonstrate the bug, I got permission from the Uber Team and took a free ride in India. I wasn’t charged for any of my rides, using the invalid payment method.

### Vulnerable request:

> POST /api/dial/v2/requests HTTP/1.1 Host: dial.uber.com {“start_latitude”:12.925151699999999,”start_longitude”:77.6657536,  
>  “product_id”:”db6779d6-d8da-479f-8ac7–8068f4dade6f”,”payment_method_id”:”xyz”}

### Steps to reproduce:

1. Replayed the above request with random characters as payment_method_id.
2. Ride was free.

#### Video POC:

Thanks to Uber Security team for fixing this quickly.

### The timeline

Aug 22nd 2016: Vulnerability Report to Uber.

Aug 26th 2016: Uber requested more information about the bug.

Aug 26th 2016: Took a free ride and replied with ride details

Aug 27th 2016: Vulnerability fixed by Uber.

Sep 10th 2016: Rewarded with $5000 bounty by Uber.

### Takeaways

As a developer, you should always take care of the below test cases when integrating payments:

a) Verify if the payment was success or failure by doing a server to server request to payment gateway or verifying checksum to the payment gateway provider.

b) Always validate the amount of the item with the amount which was paid by the user to the payment gateway.

c) Validate currency in the payment API calls. For example, the attacker can pay 50 IDR for a 50 USD item.

d) If you are storing credit cards/debit card information, then always check for authorisation if an identifier is being passed in one of the API requests.

> [**AppSecure**](https://appsecure.in) is a specialised cyber security company with years of skill acquired and meticulous expertise. We are here to safeguard your business and critical data from online and offline threats or vulnerabilities.

> Contact us: **hello@appsecure.in**

