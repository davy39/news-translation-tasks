---
title: What is session hijacking and how you can stop it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T14:30:46.000Z'
originalURL: https://freecodecamp.org/news/session-hijacking-and-how-to-stop-it-711e3683d1ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IpyNijir6izjsjs2kW6ADA.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ramesh Lingappa


  This story is for beginners and anyone who has a basic understanding about cookies
  (sessions cookies), but who’s not sure how to secure them properly. You don’t have
  to be a security expert to do that. You just have to understand ...'
---

By Ramesh Lingappa

> _This story is for beginners and anyone who has a basic understanding about cookies (sessions cookies), but who’s not sure how to secure them properly. You don’t have to be a security expert to do that. You just have to understand the process and then you will know._

If you don’t have any idea about cookies or how they work, then please read this article about [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

Let's get to it! You have an amazing web application offering a great service for customers. That means you will have an **Authentication** mechanism to get the user to your application. You know how important security is. You implemented all sorts of security measures during authentication. **Great!**

Upon successful authentication, you must create a **Session** for that user. This means that you are actually creating a **cookie** and sending it back to the browser. For example, in a Java web app, by default, it’s called **JSESSIONID.** It looks something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*C7TCffrIAgtzkEnnS2fW3Q.png)
_Cookie information from Chrome Dev Console -&gt; Applications -&gt; Cookies_

By using this cookie, only your web server is able to identify who the user is and it will provide content accordingly. And this cookie looks great. No sensitive information in the cookie, just the random ID (non-guessable). So the user is **Safe!** …right?

Well not exactly, let’s take a closer look.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0z9yq3Ti01YFUiZmN3bRdg.png)

There are two properties in this cookie: **HttpOnly (HTTP)** and **Secure.** Their values are blank, meaning **not enabled for this cookie_._** That’s where it gets to the point that it’s no longer safe.

This is where Session Hijacking comes into play.

> **Session hijacking**, sometimes also known as cookie **hijacking** is the exploitation of a valid computer **session** — sometimes also called a **session** key — to gain unauthorized access to information or services in a computer system. — [Wikipedia](https://en.wikipedia.org/wiki/Session_hijacking)

So it’s the act of stealing a customer’s session ID, by which they can access your web application as if they’re that customer.

**Is this possible? How do they get that session ID which is in the user’s browser?**

Yes it’s possible. The two cookie properties (or flags) which we saw earlier (**HttpOnly** and **Secure**) are the reason for this.

### **HttpOnly Flag**

> `**HttpOnly**` cookies are inaccessible to JavaScript's `[**Document.cookie**](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)` API; they are only sent to the server. For example, cookies that persist server-side sessions don't need to be available to JavaScript, and the `HttpOnly` flag should be set.

So in simple terms, if you don’t set the httpOnly flag, then your cookie is readable from the front end JavaScript code.

Open any web page whose cookie doesn’t have the httpOnly flag set. Then open **Chrome Dev Console** and then tap **Console Tab** (Cmd + Shift+ J or Ctrl + Shift+ J). Type `_document.cookie_` and Enter, and you will see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5Y26jhjlgFFrvi0XFnJa6g.png)
_document.cookie usage_

As you can see, you get all the cookie info. A JavaScript attacker can simply post this to their own server for later use.

You might wonder how they can write this code in your Application. It’s possible in several ways.

One way is to inject some **untrusted third-party JS library** like logging, helper utilities, etc. Read this article [**I’m harvesting credit card numbers and passwords from your site. Here’s how**](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5)**.**

Another way is by using a [**Cross Site Scripting Attack**](https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29)**.** We are not going to get into the details of it, but remember it can be done.

#### **So how do we fix it?**

The session cookie doesn’t even need to be accessible by the JavaScript client. It’s only needed for the server. We should make it only accessible for the server. It can be done by adding one word (**httpOnly**) in your **_set_cookie_** http response header. Like this:

```
Set-Cookie: JSESSIONID=T8zK7hcII6iNgA; Expires=Wed, 21 May 2018 07:28:00 GMT; HttpOnly
```

By adding the **httpOnly** flag, you are instructing the browser that this cookie should not be read by the JavaScript code. The browser will take care of the rest. This is how it looks after adding the httpOnly flag:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qjk5J3R-k88qpkMq5wkYJg.png)
_cookie set with httpOnly flag_

Notice the tick mark in the HTTP property. That indicates that **httpOnly** is enabled.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qD_G_6aUnj8LaDbPdHY9mA.png)

Here you can see that **_document.cookie_** doesn’t return our session cookie. Meaning no JS can read it, including any external scripts.

That’s it — one down one to go!

### Secure Flag

The **secure** flag instructs the browser that the cookie should only be returned to the application over encrypted connections, that is, an HTTPS connection.

So, when a cookie is sent to the browser with the flag **secure,** and when you make a request to the application using HTTP, the browser won’t attach this cookie in the request. It will attach it only in an HTTPS request. The HTTPS request will be encrypted so cookies will be safely sent across the network to your application.

**How can someone read the cookie in the HTTP request?**

This can be achieved when someone (called a **“Man in the Middle”** attack) is monitoring all the traffic in the network of customers. They are able to see the clear text data if the request is in _HTTP._

When it’s sent over _HTTPS_, all data will be encrypted from the browser and sent to the network. The attacker won’t be able to get the raw data you were sending. Nor will the attacker be able to decrypt the content. This is why sending Data over SSL is secure.

#### So how do we fix it?

Just like the httpOnly flag, you just need to add the **secure** flag in your **_set_cookie_** HTTP response header. Like this:

```
Set-Cookie: JSESSIONID=T8zK7hcII6iNgA; Expires=Wed, 21 May 2018 07:28:00 GMT; HttpOnly; Secure
```

In Java it can be done in several ways. If you are using Servlet 3.0 or above, then you can configure these settings in **_web.xml_** like this:

```
<session-config>    <cookie-config>        <http-only>true</http-only>        <secure>true</secure>    </cookie-config> </session-config>
```

If your environment doesn’t support it, then you can add it manually. For example using Servlets you can do this:

Finally, this is how it looks when both flags are set,

![Image](https://cdn-media-1.freecodecamp.org/images/1*zhc23uSW0I1enxdqSUWN3Q.png)

### Conclusion

So when you are dealing with session cookies or any other important cookies, make sure you add these two flags.

Thanks for reading, **Happy Securing!**

