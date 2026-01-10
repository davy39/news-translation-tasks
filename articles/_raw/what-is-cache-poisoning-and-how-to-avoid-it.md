---
title: What is Cache Poisoning? How Hackers Manipulate Web Caches and How to Avoid
  It
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-09-05T15:00:53.243Z'
originalURL: https://freecodecamp.org/news/what-is-cache-poisoning-and-how-to-avoid-it
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725456042044/d3744ebe-ad28-42c4-99a2-25d6bd250aee.webp
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: null
seo_desc: 'Web caches play an important role in speeding up our browsing experience.
  They save copies of web pages and other resources so that users can access them
  faster.

  But what happens when these caches become a tool for hackers?

  Let’s look at cache poison...'
---

Web caches play an important role in speeding up our browsing experience. They save copies of web pages and other resources so that users can access them faster.

But what happens when these caches become a tool for hackers?

Let’s look at cache poisoning, how it works, and how to protect against it.

## What is a Web Cache?

Caching means storing a copy of a piece of content. A web cache stores copies of web pages or parts of web content temporarily.

When you visit a website, your browser may cache some elements, like images and scripts. So the next time you visit the same site, the browser can load it faster.

Caching speeds up websites. It reduces the amount of data that must be transferred over the network. This makes browsing more efficient and provides a smoother experience for users.

A cache can be in several places. These include:

**Browser Cache :** Your browser keeps a copy of recently visited web pages, images, and other content.

**CDN Cache** : CDNs store copies of web resources in multiple, worldwide locations. This ensures that users access a nearby server, reducing load times.

**Reverse Proxy Cache :** A reverse proxy server sits between users and the web server. It caches content to reduce server load and improve response times.

Web caching works on a few basic principles.

**Expiration :** Cached content has a time-to-live (TTL) value. After this TTL, the cache will be cleared.

**Validation :** The cache checks with the server to see if the stored content is still valid or needs refreshing.

**Invalidation** : If a website’s content updates, it will remove the cache and fetch the latest version from the server.

## How Does Cache Poisoning Work?

Cache poisoning is a cyber-attack where a hacker manipulates the stored data in a web cache. The cache stores a harmful or altered version, not a real page.

When a user requests this cached content, they receive the manipulated data instead. This attack can lead to dangerous scripts running on the user’s browsers.

![DNS cache poisoning](https://cdn.hashnode.com/res/hashnode/image/upload/v1725563209590/ec36e4dd-94cf-47f5-9b9d-5c335fe26327.png align="center")

In a cache poisoning attack, a hacker exploits how caching systems store content. Here’s a simplified explanation of how this attack works.

The attacker first identifies which resources on a website are cached. They look for pages or resources that the cache might store based on the URL or request headers.

The attacker then crafts a request that includes harmful content. This request will look like a legitimate request so that the cache stores the response.

The server processes the request and returns a response that gets cached. If the cache server doesn’t check the request, it will store the malicious content.

Now, when a user requests the cached resource, the cache serves the malicious version instead of the legitimate one.

### Common Techniques Used in Cache Poisoning

Cache poisoning exploits different vulnerabilities in web caching mechanisms. Some of the most common techniques include:

**Host Header Attacks**

The “Host” header specifies which domain a request is for. Attackers can change this header. They can trick the server into caching a malicious response. For example

Normal request

```plaintext
GET /resource HTTP/1.1
Host: www.example.com
```

Malicious request

```plaintext
GET /resource HTTP/1.1
Host: attacker.com
```

If the cache stores the response based on the manipulated host, all users of “www.example.com” may get malicious content.

**HTTP Parameter Pollution**

Attackers can inject unexpected parameters into URLs. This changes server behavior and poisons the cache. For example:

**Normal URL**: [`https://www.example.com/page?id=123`](https://www.example.com/page?id=123%60)

**Malicious URL**: [`https://www.example.com/page?id=123&malicious_flag=101`](https://www.example.com/page?id=123&evil=1%60)

If the server does not sanitize these parameters, it may cache different content. The next user who visits the normal URL might receive the poisoned content.

**Vary Header Manipulation**

The Vary header is an HTTP response header. It tells caches how to store different versions of a web resource based on certain request headers.

For example, if a server sends a **“Vary: User-Agent”** header, it means that the response may vary based on the client’s user agent. So caches will store separate versions of the resource for different user agents. For example, one for desktop browsers and another for mobile browsers.

If the “Vary” header is not checked properly, attackers can manipulate request headers to poison the cache.

For example, an attacker can craft a request with a manipulated “User-Agent” header. This can result in malicious content being cached for the next user.

## How to Protect Against Cache Poisoning

Now that we understand how cache poisoning works, let’s see how to protect against it:

### **Proper Input Validation**

Always sanitize and check input from users. Especially when it comes to request headers and URL parameters. This stops attackers from injecting harmful content into cached requests.

### Use Secure Caching Headers

Set caching headers like “Cache-Control” and “Expires” correctly to avoid caching sensitive data. Use headers such as “no-cache,” “no-store,” and “must-revalidate” for dynamic or sensitive content.

### Control Cache Key Settings

Set the cache keys properly to avoid caching responses with user-specific parameters. Don’t use request headers or query parameters that attackers can easily manipulate.

### Implement HTTPS

Using HTTPS helps prevent attackers from intercepting and modifying requests and responses. HTTPS also reduces the risk of cache poisoning attacks, as it ensures data integrity.

## Conclusion

Cache poisoning poses a significant risk to web applications and users. Hackers can manipulate cached content to serve malicious data or steal sensitive information.

You can protect your web apps from cache poisoning by learning how it works and by using proper precautions. With the right approach, you can ensure a safer browsing experience for your users.

**Check out the** [***Stealth Security***](https://www.stealthsecurity.sh/) **newsletter for more articles on offensive and defensive cybersecurity.**
