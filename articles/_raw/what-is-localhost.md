---
title: What is Localhost? Local Host IP Address Explained
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-29T16:11:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-localhost
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743780742807/3c1b7eab-e5bb-4b3c-aae9-6183d2cf3f72.jpeg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: Computer Science
  slug: computer-science
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'If you are an experienced web developer, then you’ve likely seen the term
  “localhost” on many occasions.

  And even if you’re a beginner and just getting started in web development, you might
  have seen the number “127.0.0.1:” while using a live server ...'
---

If you are an experienced web developer, then you’ve likely seen the term “localhost” on many occasions.

And even if you’re a beginner and just getting started in web development, you might have seen the number “127.0.0.1:” while using a live server plugin.

You might be using it to test websites and web applications locally without knowing what exactly it is. Well, “127.0.0.1” is localhost and “localhost” is “127.0.0.1”.

In this article, you will learn what localhost is alongside its corresponding IP address, “127.0.0.1”.

## What is Localhost?

In computer networking, host means a “server”. Just like you can put a website on the internet by hosting it on a server, you can make your own computer that server. This connection is called **loopback**. The IP address for that loopback is `127.0.0.1`.

If you’ve put a website on the internet before, then you’ve dealt with hosting companies like Heroku, Hostinger, Netlify, and many others. These are what I refer to as “remote hosts” or virtual servers.

If you’ve served a website on your computer so you can test it without connecting to the internet, what you’re dealing with is a localhost.

So, by definition, **localhost is the computer or hostname currently making a request to itself**. In this case, the computer is also the virtual server.

## What is the IP Address `127.0.0.1`?

If you want to visit a website, you type the website address to your browser’s address bar, for example, `https://freecodecamp.org`.

The Domain Name Server (DNS) matches the address to a numeric IP address corresponding to that name. In the case of freeCodeCamp, this IP address is `104.26.2.33`. This is how it is done for every website you visit.

Localhost is not an exception to this. So, if you type `localhost` to your browser’s address bar, it transforms to the IP address `127.0.0.1`.

This `127.0.0.1` IP address is reserved for local servers on computers, so you will never find another IP address that starts with 127.

### But localhost: what? Or 127.0.0.1: what?

Unlike `HTTP` and `HTTPS` which are protocols, `localhost` is a hostname. Remember that the website domain name is what follows the http or https, for example, `https://www.google.com/` and `https://www.freecodecamp.org/`. So, something has to follow `localhost:` and `127.0.0.1:`. That thing is the port number.

For example, in an Express app, that port number is the port variable you set. Something like this:

```js
const port = 4000;
```

So if you type `localhost:4000` in the browser address bar and hit `ENTER`, the web application you’re currently making will be served to you:

![ss1-5](https://www.freecodecamp.org/news/content/images/2022/06/ss1-5.png align="left")

Also, if you type `127.0.0.1:4000`, you will get the same response:

![ss2-5](https://www.freecodecamp.org/news/content/images/2022/06/ss2-5.png align="left")

If you use the live server extension of VS Code, it uses a port `5500` attached to `127.0.0.1`, followed by the filename:

![ss3-6](https://www.freecodecamp.org/news/content/images/2022/06/ss3-6.png align="left")

## Conclusion

I hope this article has helped you learned more about localhost, what its IP address is, and how it works to serve websites for local testing.

And yes! There’s no place like localhost. Properly put, “there’s no place like `127.0.0.1`” :).

Keep coding…

Thanks to [Bartosz Cytrowski](https://www.cytrowski.com/) for pointing out a key error regarding what localhost is. Your feedback improved the article!
