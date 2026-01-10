---
title: Slow Loris attack using JavaScript on a PHP Server [and its prevention!]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-02T00:58:30.000Z'
originalURL: https://freecodecamp.org/news/slow-loris-attack-using-javascript-on-php-server
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/websec.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'By Mehul Mohan

  Forget the post for a minute, let''s begin with what this title is about! This is
  a web security-based article which will get into the basics about how HTTP works.
  We''ll also look at a simple attack which exploits the way the HTTP proto...'
---

By Mehul Mohan

Forget the post for a minute, let's begin with what this title is about! This is a web security-based article which will get into the basics about how HTTP works. We'll also look at a simple attack which exploits the way the HTTP protocol works.

## What is HTTP?

**HTTP,** HyperText Transfer Protocol, is the protocol used by the web for communication. Your device, when you use a browser, uses this particular protocol to send requests to remote servers to request data from them. 

It's basically like you saying to your mom, "Hey mom, I need to eat the item in the fridge present at shelf 2, could you give it to me?"

And your mom says, "Sure, here you go", and sends you that item. Now, HTTP is the way you were able to communicate this information to your mom, more like the language you used for communication.

## How HTTP Works

Here's a TL;DR video if you're a video person. Otherwise, proceed with the article:

%[https://www.youtube.com/watch?v=aE75gHVK16A]

HTTP (Layer 7) is built on the top of TCP protocol (Layer 4). We can use `nc` (netcat) utility to open a raw TCP socket to any website running on HTTP (usually port 80). See the following example on how we connect to HTTP port 80 for google.com using netcat:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.09.39-am.png)

See the data we sent:

```shell
GET / HTTP/1.1
Host: google.com
X-header-1: somemoredata
X-header-2: somemoredata
<empty line>
```

Ignore the extra `X-header-*` headers, they're just random headers you can send with your request. The important header to include in HTTP/1.1 spec is the `Host` header.

And the response we got:

```shell
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Tue, 01 Oct 2019 23:24:13 GMT
Expires: Thu, 31 Oct 2019 23:24:13 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Accept-Ranges: none
Via: HTTP/1.1 forward.http.proxy:3128
Connection: keep-alive

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

Thus, HTTP is a plaintext protocol consisting of the request information sent by the client and the response as shown above.

## Slow Loris Attack

A Slow Loris attack exploits the fact that I could make an HTTP request very very slowly. In other words, I can initiate an HTTP request to the server and keep sending data to the server very slowly in order to keep that connection alive. And at the same time, it never ends that connection and opens multiple such connections to exhaust the connection pool of the server.

**Disclaimer** - Penetration testing any online/offline service not owned by you without prior written permission is **illegal** and I'm not responsible for any damage caused. **Use this content for educational purposes only.**

## Slow Loris Demonstration:

%[https://www.youtube.com/watch?v=KUxd7FFDwTM]

This means, I could keep on sending additional data to the server in the form of headers. Now, I'll start a simple PHP development server on my machine:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.16.34-am.png)

And I use a simple Node script to perform what we discussed above on my local server:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.17.40-am.png)

You can find the Node script used [here](https://gist.github.com/mehulmpt/49eee6cc0e84d6770b904336d0ad7f3e).

After some time, you'll see that our PHP server actually crashes!

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.17.52-am.png)

This is because there are way too many open connections and PHP cannot handle any more open connections (due to memory/hardware limits).

Now, of course this works flawlessly on a local development server. But if you're able to find a server which does not implement protections against slow loris attacks, it is a big problem for them.

## Protections against a Slow Loris attack



* Use solutions like Cloudflare in front of your servers to prevent DoS/DDoS  
Quoting from Cloudflare's site:

> Cloudflare **buffers incoming requests** before starting to send anything to the origin server. As a result, “low and slow” attack traffic like Slowloris attacks never reach the intended target. Learn more about how Cloudflare's DDoS protection stops slowloris attacks.

* Rate limit number of simultaneous connections open by a particular IP address to a small number. This could be achieved using simple frontend reverse proxy servers like nginx using their leaky bucket algorithm implementation. How that works, is something for another day!
* Increasing the server capacity - Now this might mitigate small attacks, but honestly attacker can and would scale/amplify the original attack quite easily due to the less bandwidth required to carry out such an attack.

## Conclusion

A lot of servers (nginx/apache2 new versions) come with slow loris attack protections by default. But for a lot of internal services, servers might be vulnerable to this simple attack. 

You might want to check your services and implement the fixes. Web security is an exciting area, and I plan to do a web series on it on [codedamn](https://www.youtube.com/codedamn). You can connect with me on [twitter](https://twitter.com/mehulmpt) for updates too. Till then, be safe!

