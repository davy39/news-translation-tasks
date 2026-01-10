---
title: What is HTTPS? HTTP vs HTTPS Meaning and How it Works
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-16T13:57:44.000Z'
originalURL: https://freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/john-salvino-bqGBbLq_yfc-unsplash.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: http
  slug: http
- name: https
  slug: https
- name: Security
  slug: security
seo_title: null
seo_desc: 'Have you ever noticed the "HTTP" or "HTTPS" at the beginning of a URL in
  your browser? Well, what is HTTP and what is HTTPS? How are they different?

  In order to understand the differences, it helps to demistify to meaning of these
  two terms and under...'
---

Have you ever noticed the "HTTP" or "HTTPS" at the beginning of a URL in your browser? Well, what is HTTP and what is HTTPS? How are they different?

In order to understand the differences, it helps to demistify to meaning of these two terms and understand how they each work.

## What is HTTP?

HTTP stands for **H**yper**T**ext **T**ransfer **P**rotocol and is the foundation of the World Wide Web. Without it the Web wouldn't be what it is today.

An HTTP URL starts with `http://` and  has a number 80 port by default.

The *HyperText* part in the name means that there are documents or files involved. Those can contain text, images, graphics, videos or any other media. 

In addition, they likely contain links to other documents or files for cross referencing, which you can easily access after clicking the link with a mouse or touchpad or after touching it on your phone screen. 

The *Transfer* part in the name means the files can move over the World Wide Web from one networked device to another.

The *Protocol* part means that it consists of a set of computer rules that govern how devices are able to use the Internet. It also tells them how they can use the Internet as a communication medium when connected with many other devices at a distance. 

HTTP is built on top of the TCP/IP network protocol suite and on top of other layers in the protocol stack.

The TCP/IP is a standardized  set of rules for how browsers and servers are allowed to communicate over the Internet. After all, the World Wide Web is all about communication between browsers and servers.

Specifically, HTTP is an application layer protocol and is the primary protocol used for communication and data transfer between a web client and a web server.

In a nutshell, HTTP is a set of rules and standards for how hypertext files and all kinds of information are transfered over the web. It's how browsers and servers communicate.


## A Typical HTTP Request and Response Flow

HTTP is used when browsers want to get connected to websites.

They communicate by sending HTTP requests and receiving HTTP responses. This is known as the *Request - Response Cycle* in a client computer - web server computing model.

![Screenshot-2021-08-11-at-3.17.23-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-11-at-3.17.23-PM.png)

The client, which is typically a web browser like Google Chrome, Mozilla Firefox, or Apple Safari, makes the request. It does this by entering a human-friendly URL (Uniform Resource Locator) like `freecodecamp.org` in the address bar at the top of the browser.

That domain name, `freecodecamp.org`, is mapped to an IP address [with the help of the Domain Name System (DNS)](https://www.freecodecamp.org/news/what-is-dns/).

The web browser then gets connected to the server and makes an HTTP *Request*, asking for the information it needs to receive in order to load a web page.

An HTTP request can look something like this:

```
GET / HTTP/1.1
Host: www.freecodecamp.org
```

It consists of:

- An HTTP method, often referred to as an HTTP verb, like `GET`. This specific verb is used to *get* information back. Another common verb is `POST`, which is used when the client submits data in a form. Verbs specify the action browsers are expecting from the server.
- The path, which in our example is `/`, the *root* path. The server stores all the files that make up a website, so a request needs to specify which part the browser is requesting to load.
- The HTTP type and its version.
- The domain name of the URL.

The web server then receives the request and processes it by looking for the requested data.

A server is a computer different from the ones we use on a day-to-day basis. Its sole purpose is to store data and files and retrieve them and distribute them when requested.

The server returns a message, or HTTP *Response*, back to the browser.

An example of a response is: `HTTP/1.1 200 OK`

- It first starts with the protocol and version `HTTP/1.1`
- Next is the HTTP *status code*, a 3-digit number, which in this case is `200`. It indicates wether the HTTP request was completed or not. Status codes starting with a `2` indicate success and that the request was successfully completed. Status codes starting with a `4`, like `404`, indicate a client side error (for example making a typo in the URL) so the page is not displayed in the browser. A status code starting with `5` means a server side error and again the page is not displayed in the browser.
- Next is the *status text*, human readable text, that summarizes the meaning of the status code. In this case it's "OK", meaning a successful retrieval of the requested document.

A HTTP response also includes headers that can look something like this:

```
date: Thu, 12 Aug 2021 12:07:16 GMT
server: cloudflare
content-type: text/html; charset=utf-8
```

Headers include important information about the content type sent back, such as the language, format, and when the response was sent.

Lastly, a response to a 'GET' request includes the optional *HTTP body*. This contains the requested information, like the HTML/CSS/JavaScript files that make up the website.

Then the browser receives the response, renders the page, and closes the connection. 

Each time it needs to load a new element on a page (like different styles or images or videos) it will start a new connection and the whole process repeats again.

## Limitations of HTTP

HTTP is fast because of its simplicity, but it does not provide security when data is exchanged. This is because all the data is transmitted in  **plain text** and nothing is encrypted at all.

During the transfer, the hypertext data is broken down into 'packets', and anyone with the right tools, skills, and knowledge between the browser and server can easily view and steal the information being transmitted. 

This means that usernames, passwords, and sensitive information are at risk of being accessible to attackers, while at the same time the risk of injecting viruses is high. 

This means that HTTP is not a secure or private medium, resulting in users feeling unsafe.

HTTP is safe for certain sites, like blogs, but you should not submit any credit card or other personal information over an HTTP connection.


## What is HTTPS?

HTTPS stands for **H**yper**T**ext **T**ransfer **P**rotocol **S**ecure.

A HTTPS URL starts with `https://` and uses a port number 443 by default.

It's not a separate protocol from HTTP, but it's the more *secure* and confidential version of it. It's the safest way to transfer data between a browser and a server.

Most websites nowadays use HTTPS over HTTP. So before submitting any sensitive information like logging into your bank account and making financial transactions, always make sure the site uses HTTPS.

You can tell if a site is secure and has an HTTPS connection by the lock icon on the left hand side of the address bar:

![Screenshot-2021-08-11-at-6.41.08-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-11-at-6.41.08-PM.png)

![Screenshot-2021-08-12-at-7.38.33-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-12-at-7.38.33-PM.png)

Unlike HTTP which works on the Application Layer, HTTPS works on the Transport Layer.

## How Does HTTPS Work?

Each data packet sent over an HTTPS connection is *encrypted* and secure, using cryptographic protocols such as TLS or SSL, on top of HTTP.

Transport Layer Security (TLS), formely known as Secure Sockets Layer (SSL), is the protocol used to encrypt communications. It is the newer and more secure version of SSL. 

TLS provides security against attacks, and its three main goals are authentication, privacy, and overall security.

TLS secures communications by using an asymmetric key algorithm, Public Key Infrastructure (PKI). This system uses two uniquely related keys to encrypt and decrypt sensitive information, enabling safe communication over the Internet.

Both keys are used in conjunction, and in this way TLS creates a link between sender and receiver. It makes sure both parties are identified and are really who they say they are.

First, you have the **public** key. It is available to view publicly and  can be shared with everyone and anyone who wants to interact with the site.

This key is used to turn plain text into cipher text, to encrypt data, and acts as a lock to encrypt the data. It also confirms the owner of a private key. Distribution of public keys to browsers is done with Certificates.

Then, each public key has a unique **private** key and they work as a pair. You use this key to decrypt information. Data encrypted with a public key can only be decrypted by the corresponding unique private key. 

It is this unique private key that unlocks the lock and decrypts the data. A private key also confirms that the information is yours. This key is kept private, stored and available only to its owner.

A secure connection is set up and certificates are exchanged before any actual data is transfered.

The client types in the URL of the webpage they want to access. The webpage's server sends over the TLS or SSL certificate that contains the public key to start the connection. The client and server go through a lot of back and forth (called a TLS/SSL handshake) until they establish a secure session.


## Conclusion

In this article we learned what HTTPS is, how it works, and how it is different (and more secure) than HTTP.

To recap, HTTPS is the secure version of HTTP, the basic network protocol for sending hypertext over the web.

In HTTPS there are additional steps for security, such as TLS/SSL certificates and the TLS/SSL handshake.

It provides authentication for users and data, making sure transactions are kept private (with data integrity being a priority) without fearing a data breach during the client-server communication.

The contents of messages and transactions can only be viewed by the sender and intended recipient.

Thanks for reading!



