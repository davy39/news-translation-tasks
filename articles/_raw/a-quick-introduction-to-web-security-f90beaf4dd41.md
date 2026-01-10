---
title: A quick introduction to web security
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-15T15:22:19.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-web-security-f90beaf4dd41
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xw9gprMTI6h3U3NkKV0vUg.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Austin Tackaberry

  A web developer’s primer on CORS, CSP, HSTS, and all the web security acronyms!

  There are many reasons to learn about web security, such as:


  You’re a concerned user who is worried about your personal data being leaked

  You’re a c...'
---

By Austin Tackaberry

#### A web developer’s primer on CORS, CSP, HSTS, and all the web security acronyms!

There are many reasons to learn about web security, such as:

* You’re a concerned user who is worried about your personal data being leaked
* You’re a concerned web developer who wants to make their web apps more secure
* You’re a web developer applying to jobs, and you want to be ready if your interviewers ask you questions about web security

and so on.

Well this post will explain some common web security acronyms in a way that is easy to understand but still accurate.

Before we do that, let’s make sure we understand a couple of core concepts of security.

### Two Core Concepts of Security

#### **No one is ever 100% safe.**

There is no notion of being 100% protected from being hacked. If anyone ever tells you that, they are wrong.

#### **One layer of protection is not enough.**

You can’t just say…

> Oh, because I have CSP implemented, I am safe. I can cross off cross-site scripting from my vulnerabilities list because that can’t happen now.

Maybe that is a given to some, but it is easy to find yourself thinking in this manner. I think one reason that programmers can easily find themselves thinking this way is because so much of coding is black and white, 0 or 1, true or false. Security is not so simple.

We’ll start off with one that everyone runs into fairly early on in their web development journey. And then you look on StackOverflow and find a bunch of answers telling you how to bypass it.

### Cross-Origin Resource Sharing (CORS)

Have you ever gotten an error that looked something like this?

```
No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'null' is therefore not allowed access.
```

You are certainly not alone. And then you Google it, and someone tells you to get this extension that will make all your problems go away!

> Great, right?

**CORS is there to protect you, not hurt you!**

In order to explain how CORS helps you, let’s first talk about cookies, specifically **authentication cookies**. Authentication cookies are used to tell a server that you are logged in, and they are automatically sent with any request you make to that server.

Let’s say you’re logged in to Facebook, and they use authentication cookies. You click on `bit.ly/r43nugi` which redirects you to `superevilwebsite.rocks`. A script within `superevilwebsite.rocks` makes a client-side request to `facebook.com` which sends your authentication cookie!

In a no-CORS world, they could make changes to your account without you even knowing. Until, of course, they post `bit.ly/r43nugi` on your timeline, and all of your friends click on it, and then they post `bit.ly/r43nugi` on all of your friends’ timelines and then the cycle continues in an evil breadth-first scheme that conquers all of Facebook’s users, and the world is consumed by `superevilwebsite.rocks`. ?

In a CORS world, however, Facebook would only allow requests with an origin of `facebook.com` to edit data on their server. In other words, they would limit cross-origin resource sharing. You might then ask…

> Well can superevilwebsite.rocks just change the origin header on their request, so that it looks like it is coming from facebook.com?

They can try, but it won’t work because the browser will just ignore it and use the real origin.

> Ok, but what if superevilwebsite.rocks made the request server-side?

In this case, they could bypass CORS, but they will not win because they won’t be able to send your authentication cookie along for the ride. The script would need to execute on the client side to get access to your client side cookies.

### Content Security Policy (CSP)

To understand CSP, we first need to talk about one of the most common vulnerabilities on the web: XSS, which stands for cross-site scripting (yay — another acronym).

XSS is when some evil person injects JavaScript into your client-side code. You might think…

> What are they going to do? Change a color from red to blue?

Let’s assume that someone has successfully injected JavaScript into client-side code of a website you are visiting.

What could they do that would be malicious?

* They could make HTTP requests to another site pretending to be you.
* They could add an anchor tag that sends you to a website that looks identical to the one you are on with some slightly different, malicious characteristics.
* They could add a script tag with inline JavaScript.
* They could add a script tag that fetches a remote JavaScript file somewhere.
* They could add an iframe that covers the page and looks like part of the website prompting you to insert your password.

The possibilities are endless.

CSP tries to prevent this from happening by limiting:

* what can be opened in an iframe
* what stylesheets can be loaded
* where requests can be made, etc.

So how does it work?

When you click on a link or type a website URL in the address bar of your browser, your browser makes a GET request. It eventually makes its way to a server which serves up HTML along with some HTTP headers. If you’re curious about what headers you receive, open up the Network tab in your console, and visit some websites.

You might see a response header that looks like this:

```
content-security-policy: default-src * data: blob:;script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.virtualearth.net *.google.com 127.0.0.1:* *.spotilocal.com:* 'unsafe-inline' 'unsafe-eval' *.atlassolutions.com blob: data: 'self';style-src data: blob: 'unsafe-inline' *;connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net *.spotilocal.com:* wss://*.facebook.com:* https://fb.scanandcleanlocal.com:* *.atlassolutions.com attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' chrome-extension://boadgeojelhgndaghljhdicfkmllpafd chrome-extension://dliochdbjfkdbacpmhlcpmleaejidimm;
```

That is the content security policy of `facebook.com`. Let’s reformat it to make it easier to read:

```
content-security-policy:
default-src * data: blob:;

script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.virtualearth.net *.google.com 127.0.0.1:* *.spotilocal.com:* 'unsafe-inline' 'unsafe-eval' *.atlassolutions.com blob: data: 'self';

style-src data: blob: 'unsafe-inline' *;

connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net *.spotilocal.com:* wss://*.facebook.com:* https://fb.scanandcleanlocal.com:* *.atlassolutions.com attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' chrome-extension://boadgeojelhgndaghljhdicfkmllpafd chrome-extension://dliochdbjfkdbacpmhlcpmleaejidimm;
```

Now, let’s break down the directives.

* `**default-src**` restricts all other CSP directives that are not explicitly listed.
* `**script-src**` restricts the scripts that can be loaded.
* `**style-src**` restricts the stylesheets that can be loaded.
* `**connect-src**` restricts the URLs which can be loaded using script interfaces, so fetch, XHR, ajax, etc.

Note that there are many more CSP directives than just these four shown above. The browser will read the CSP header and apply those directives to everything within the HTML file that was served. If the directives are set appropriately, they allow only what is necessary.

If no CSP header is present, then everything goes, and nothing is restricted. Everywhere you see `*` , that is a wildcard. You can imagine replacing `*` with anything and it will be allowed.

### HTTPS or HTTP Secure

Certainly you have heard about HTTPS. Maybe you have heard some people say…

> Why do I care about using HTTPS if I am just on a website playing a game.

Or maybe you have heard the other side…

> You are crazy if your site doesn’t have HTTPS. It’s 2018! Don’t trust anyone that says otherwise.

Maybe you heard that Chrome will now mark your site as insecure if it is not HTTPS.

At its core, HTTPS is fairly straightforward. HTTPS is encrypted and HTTP is not.

So why does this matter if you are not sending sensitive data?

Get ready for another acronym…MITM, which stands for Man in the Middle.

If you are using public Wi-Fi with no password at a coffee shop, it’s pretty easy for someone to act like your router, so that all requests and responses go through them. If your data is not encrypted, then they can do whatever they want with it. They can edit the HTML, CSS, or JavaScript before it even gets to your browser. Given what we know about XSS, you can imagine how bad this could be.

> Ok, but how is it that my computer and the server know how to encrypt/decrypt but this MITM does not?

That’s where SSL (Secure Sockets Layer) and more recently, TLS (Transport Layer Security) come in. TLS took over for SSL in 1999 as the encryption technology used within HTTPS. Exactly how TLS works is outside of the scope of this post.

### HTTP Strict-Transport-Security (HSTS)

This one is pretty straightforward. Let’s use Facebook’s header as an example again:

```
strict-transport-security: max-age=15552000; preload
```

* `max-age` specifies how long a browser should remember to force the user to access a website using HTTPS.
* `preload` is not important for our purposes. It is a service hosted by Google and not part of the HSTS specification.

This header only applies if you accessed the site using HTTPS. If you accessed the site via HTTP, the header is ignored. The reason is that, quite simply, HTTP is so insecure that it can’t be trusted.

Let’s use the Facebook example to further illustrate how this is helpful in practice. You are accessing `facebook.com` for the first time, and you know HTTPS is safer than HTTP, so you access it over HTTPS, `https://facebook.com`. When your browser receives the HTML, it receives the header above which tells your browser to force-redirect you to HTTPS for future requests. One month later, someone sends you a link to Facebook using HTTP, `http://facebook.com`, and you click on it. Since one month is less than the 15552000 seconds specified by the `max-age` directive, your browser will send the request as HTTPS, preventing a potential MITM attack.

### Closing Thoughts

Web security is important no matter where you are in your web development journey. The more you expose yourself to it, the better off you will be. Security is something that should be important to everyone, not just the people who have it explicitly named in their job title! ?

