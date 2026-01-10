---
title: WTF is HTTPS?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-24T12:43:00.000Z'
originalURL: https://freecodecamp.org/news/wtf-is-https
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/dayne-topkin-78982-unsplash.jpg
tags:
- name: https
  slug: https
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Megan Kaczanowski

  Security has a lot of acronyms. What do they mean? Let’s break them down into manageable
  bits.

  First, HTTPS is actually HTTP running with TLS or SSL over it. First, we’ll cover
  HTTP, then TLS and SSL.

  What is HTTP?

  HTTP is what w...'
---

By Megan Kaczanowski

Security has a lot of acronyms. What do they mean? Let’s break them down into manageable bits.

First, HTTPS is actually HTTP running with TLS or SSL over it. First, we’ll cover HTTP, then TLS and SSL.

### What is HTTP?

HTTP is what web browsers use to connect to web pages, images, etc. It is a connectionless text-based protocol. The connectionless part means that every time the web browser needs to load a new element, a new connection needs to be made (instead of keeping the connection open all the time — as most protocols do.) A protocol is just a set of computer rules that govern how devices connect across the internet.

When you type a URL into a browser, the computer will retrieve the IP address (this is DNS). Then, the browser connects to the server and sends an HTTP request to the web page. The web server checks for the page and loads it. Then, the browser receives the page and closes the connection. The browser then looks through the page for other parts it needs to load (such as images, applets, etc.). For each new part it needs to load, the browser will make and close another connection. Finally, the page is completely loaded.

The problem with HTTP is that it transmits information over cleartext — which means that anyone who has the technical skills to watch the traffic can see everything that is being transmitted (including usernames and passwords). HTTPS offers encryption and authentication.

Encryption is designed to hide the contents of a message from anyone other than the intended recipient of the message. The idea is to transform the data so that only a certain person, or group of people, can transform the data back into a recognizable message.

Authentication verifies identity. It is used to verify that the server that is supposed to send the message is actually the server which sent the message.

### What is SSL/TLS?

First, essentially SSL and TLS do the same thing. But TLS is a newer version of the same protocol, with stronger encryption and authentication protocols.

Basically, TLS uses **asymmetric encryption** to set up a link between the two servers using **private/public keys**. Asymmetric encryption is like a lock and key, where one person has the ‘lock’ which encrypts the data, and a second person has the ‘key’ which decrypts the data. Public and private keys are like a lock and key set where one locks up (encrypts) the data, and one unlocks (decrypts) the data.

After the session is initiated, the servers can securely compute a shared secret and begin communicating using symmetric encryption (as it is MUCH faster, and can transmit larger packets of data). Symmetric encryption doesn’t have a lock/key pair. Instead it’s like talking to someone in a secure location (shared secret). If the location is secure (i.e. you are the only two who know where you are/know the shared secret), you don’t have to worry about guarding specific pieces of information with a lock and key. 

### How does SSL/TLS work?

SSL/TLS works via a protocol referred to as the SSL/TLS Handshake. It works like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.22.38-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.22.47-PM.png)

The handshake uses asymmetric encryption to set up the process and agree on a shared secret. Then the handshake switches to the faster symmetric encryption. The ‘accepted ciphers’ part just helps the servers agree on a common protocol to use.

<iframe src="https://giphy.com/embed/cI45LEPRoFQhLVq7AB" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/skittles-yes-winning-heck-cI45LEPRoFQhLVq7AB">via GIPHY</a></p>

HTTPS is important because it protects the integrity of website's traffic. That allows a website to protect their users from intentionally malicious attackers who are interested in installing malware or stealing user data, as well as 3rd parties like ISPs who might be interested in injecting ads or pulling data. 

HTTPS ensures that users have privacy, and it's becoming ubiquitous, in large part due to Google's push for HTTPS. That's why on websites with HTTPS, when you're using a Chrome browser, you'll see a 'lock' symbol (see below).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-18-at-5.31.55-PM-1.png)

Websites which don't have HTTPS will pop up with a bright red 'not secure' warning. In addition, many new features aren't enabled without HTTPS (particularly for progressive web apps). Given how key HTTPS is to the security of the web, it's important for anyone working in security to understand why and how it works. In order to secure systems, you need to understand them.

