---
title: The Story of requesting twice - CORS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-13T06:25:10.000Z'
originalURL: https://freecodecamp.org/news/the-story-of-requesting-twice-cors
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/priscilla-du-preez-234144-unsplash.jpg
tags:
- name: api
  slug: api
- name: CORS
  slug: cors
- name: JavaScript
  slug: javascript
- name: REST API
  slug: rest-api
- name: web
  slug: web
- name: Web App Security
  slug: web-app-security
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Lusan Das

  The story of requesting twice, allow me to explain how it all began.

  While working on a feature, I decided to look at the network tab and observed that
  the first request was sent with method OPTIONS, and the following request after
  it wa...'
---

By Lusan Das

The story of requesting twice, allow me to explain how it all began.

While working on a feature, I decided to look at the network tab and observed that the first request was sent with method OPTIONS, and the following request after it was the request with the correct method eg GET, POST etc, which is returning the expected payload. Basically two calls for the same request.

Here take a look at the screen shots below

![Image](https://cdn-media-1.freecodecamp.org/images/1*W7g8e0J9fwocmwX_Ce6VWA.png align="left")

*Request with OPTIONS method*

![Image](https://cdn-media-1.freecodecamp.org/images/1*JgwOpH3t9oTrL8Q_UM01mw.png align="left")

*Request with GET method*

After digging few docs, I realised it was an expected behaviour. It is related to the concept of HTTP access control (CORS).

To understand it better, let me explain a bit about CORS and requests.

### HTTP access control (CORS)

Cross-Origin Resource Sharing ([CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)) is a mechanism that uses additional [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP) headers to let a [user agent](https://developer.mozilla.org/en-US/docs/Glossary/user_agent) gain permission to access selected resources from a server on a different origin (domain) than the site currently in use.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wnTTrWj5tn6VCQJHk9PHKQ.png align="left")

*Cross-Origin Resource Sharing (*[*CORS*](https://developer.mozilla.org/en-US/docs/Glossary/CORS)*)*

Let us understand the above image above to get a better understanding of CORS.

1. **Same Origin Request:** We have opened **domain-a.com**, where we are requesting a **blue image** hosted in web server **domain-a.com.** Since we are performing our requests in the same domain, it is called a Same-origin request.
    
2. **Cross Origin Request:** We have opened **domain-a.com**, where we are requesting a **red image** hosted in web server **domain-b.com.** Since we are performing our requests in different domains, it is called a Cross-origin Request.
    

### **Simple requests**

These are requests that doesn't send it’s first request as method OPTIONS. It is fired only once.

Surely it begs the question, why will the first request have method OPTIONS if we are not sending it, please have patience it will be explained below in preflight section ☺

But before that let us understand what are the points that make request simple.

1. The only allowed methods in simple request are:
    

* [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
    
* [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD)
    
* [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)
    

2. Apart from the headers set automatically by the user agent (for example, connection , [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), or any of the other headers with names defined in the Fetch spec as a “forbidden header name”), the only headers which are allowed to be manually set are [those which the Fetch spec defines as being a “CORS-safelisted request-header”](https://fetch.spec.whatwg.org/#cors-safelisted-request-header), which are:
    

* Accept
    
* Accept-Language
    
* Content-Language
    
* Content-Type
    
* DPR
    
* Downlink
    
* Save-Data
    
* Viewport-Width
    
* Width
    

3. The only allowed values for the Content-Type header are:
    

* application/x-www-form-urlencoded
    
* multipart/form-data
    
* text/plain
    

4. No event listeners are registered on any XMLHttpRequestUpload object used in the request.
    
5. No ReadableStream object is used in the request.
    

### Preflighted requests

Preflighted request is a type of request which sends an HTTP request by the OPTIONS method to the resource on the other domain, in order to determine whether the actual request is safe to send. Cross-site requests are preflighted like this since they may have implications to user data. It is evident from the screenshots above.

For requests like PUT, DELETE, PATCH etc, preflight requests are sent.

Below flowchart summarises really well how it works.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cYI52Rb-fWjSFiQPoCF9pQ.png align="left")

*Image Courtesy html5rocks*

This flowchart opens up a door to a whole new knowledge. Couldn’t help but appreciate how good it is!

> *Strangely enough even GET request was observed to have preflights which for my case was due to presence of custom header Authorization, which can be seen from the screenshot below*

![Image](https://cdn-media-1.freecodecamp.org/images/1*W7g8e0J9fwocmwX_Ce6VWA.png align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/1*JgwOpH3t9oTrL8Q_UM01mw.png align="left")

#### Is Preflight request bad?

It is a small request without a body, but I always felt it as a bother. It is still a request, and each request is a cost, no matter how small that request is, so I definitely recommend to try and avoid having such cases.

#### How do we avoid it?

Well the easiest solution is avoid CORS, try to keep our resources and APIs in the same domain. It is really that simple.

#### Conclusion

It is always good to be armed with knowledge of how requests work. Even if the cost is very low, it still matters. Saving small requests can make our application really fast in the long run. Well I believe in the future, which is fast and furious.

> *Follow me on* [**twitter**](https://twitter.com/daslusan) to get more updates regarding new articles and to stay updated in latest frontend developments. Also **share** this article on twitter to help others know about it. Sharing is caring **^\_^**

### Some helpful resources

Below are some of the links that inspired this article

1. [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
    
2. [https://stackoverflow.com/questions/24704638/options-request-makes-application-2x-slower](https://stackoverflow.com/questions/24704638/options-request-makes-application-2x-slower)
    
3. [https://stackoverflow.com/questions/29954037/why-is-an-options-request-sent-and-can-i-disable-it/29954326](https://stackoverflow.com/questions/29954037/why-is-an-options-request-sent-and-can-i-disable-it/29954326)
    
4. [https://www.html5rocks.com/en/tutorials/cors/](https://www.html5rocks.com/en/tutorials/cors/)
