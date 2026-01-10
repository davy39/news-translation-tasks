---
title: What is HTTPS? A Guide to Secure Web Browsing and Browser Encryption
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-13T18:05:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-https-a-guide-to-secure-web-browsing-and-browser-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/HTTPS-image.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: https
  slug: https
seo_title: null
seo_desc: 'You may have noticed the "https" at the beginning of a URL. Or you may
  have noticed a lock in the URL bar of your browser.

  What does "https" mean? What does the lock icon in your browser mean? These things
  are key to secure web browsing. In this arti...'
---

You may have noticed the "https" at the beginning of a URL. Or you may have noticed a lock in the URL bar of your browser.

What does "https" mean? What does the lock icon in your browser mean? These things are key to secure web browsing. In this article, you will learn all about secure web browsing and browser encryption. 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-6.png)

The "S" in "HTTPS" stands for **Secure**. Let's first learn what HTTP" is.

## What is HTTP?

HTTP (which stands for HyperText Transfer Protocol) is a network protocol. It tells web browsers how to connect to web pages and other documents across the internet. It is connectionless, which means that a new connection is made every time a browser has to load a new file or element.

If you type a website URL into your browser, the browser will send an HTTP request to the server hosting the website. The server will then send back the requested web page, sending each part (i.e. images, text, styles) separately.

There is a major problem with HTTP, however. The information transmitted using the HTTP is not encrypted at all. Anyone that knows how can watch the traffic and see all the data transmitted. That includes usernames and passwords!

HTTPS secures and encrypts the entire process.

## What is HTTPS?

HTTPS (HypterText Transfer Protocal Secure) ensures secure communication between a browser and web server. It encrypts every data packet sent using either SSL or TLS encryption. Without this additional security, any information you enter into a site will be sent in plaintext and could potentially be seen by someone trying to hack your data.

TLS is newer and more secure than SSL, and is what most HTTPS sites use. TLS will make sure both parties are who they say they are. It also makes sure the data sent has not been tampered with.

TLS uses asymmetric encryption to create a link between the user and the server using private/public keys. These key are like a lock and key set. One encrypts the data with a lock and the person decrypts the data with a key.

The servers switch to symmetric encryption after the session begins because it is faster and can transmit larger amounts of data. Instead of using a public/private key, symmetric encryption uses a shared secret. It is like talking to someone in a room that no one else knows about. Since the room is secret, you don't have to worry that other people will be in the room and hear what you are talking about.

Most sites today use HTTPS instead of HTTP since there are major advantages and few disadvantages.

Before submitting any confidential information such as passwords, you should always make sure the site is using HTTPS. 

Most web browsers will show a lock icon to the left of the URL to indicate the site is secure. Also, most browsers will also warn users with a 'not secure' warning in the site is not using HTTPS. 

## Virtual Private Networks

Even with HTTPS enabled, ISPs will still know what websites you’re visiting, even if they don’t know what you’re doing there.

And just knowing where you’re going — the “metadata” of your web activity — gives ISPs a lot of information they can sell.

So if you want to take security to the next level, consider using a Virtual Private Network (VPN).  VPNs will encrypt everything, including what websites you visit. For more info on VPNs and how to set one up, check out [this article by Quincy Larson](https://www.freecodecamp.org/news/how-to-set-up-a-vpn-in-5-minutes-for-free-and-why-you-urgently-need-one-d5cdba361907/).


