---
title: What are Cookies on the Web and How Do You Use Them?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-cookies-on-the-web-and-how-do-you-use-them
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce9740569d1a4ca34d9.jpg
tags:
- name: Productivity
  slug: productivity
- name: toothbrush
  slug: toothbrush
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'Manipulating Cookies

  Getting or setting cookies is a straightforward operation that can be achieved by
  accessing the cookie property on the browser’s document object.

  Let''s say you find an amazing and informative recipe website to cook a fun meal
  for...'
---

## **Manipulating Cookies**

Getting or setting cookies is a straightforward operation that can be achieved by accessing the cookie property on the browser’s document object.

Let's say you find an amazing and informative recipe website to cook a fun meal for your guests but it’s in foreign language. Luckily you are able to change the language on the website using a dropdown. 

A couple of days later you visit the same site again to make a dish for your mother, but now you see the website in your native language by default.

How'd that happen? The website remembers the language you selected on your last visit and stores it in the form of a **cookie**. Now it automatically selects your preferred language by reading that cookie.

`userLanguage:french`

Cookies are used to store data in the form of `name:value` pairs on the client side. They let a website store user specific information on the browser for later use. The stored information could be `sessionID`, `userCountry`, `visitorLanguage` and so on.

Another way to store the data on the client side is `localstorage`.

### **Set Cookie**

A cookie can be set using the syntax below. But a library, like the one mentioned at the end, is highly recommended to make development easier for everyone. 

While setting the cookie, you can set the expiration date for it as well. If you skip this, the cookies are erased when the browser is closed.

**Keep in mind** that a **cookie set by a particular domain can only be read by that domain & its subdomains only.**

```javascript
// Using vanilla javascript
document.cookie = 'userLanguage=french; expires=Sun, 2 Dec 2017 23:56:11 UTC; path=/';

//Using JS cookie library
Cookies.set('userLanguage', 'french', { expires: 7, path: '/' });
```

_The above cookie expires in 7 days._

### **Get Cookie**

```javascript
// Using vanilla javascript
console.log(document.cookie)

// => "_ga=GA1.2.1266762736.1473341790; userLanguage=french"

// Using JS cookie library
Cookies.get('userLanguage');

// => "french"
```

### **Delete Cookie**

In order to delete a cookie set the expiration date to something in the past.

```javascript
// Using vanilla javascript
document.cookie = 'userLanguage; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/';

//Using JS cookie library
Cookies.remove('userLanguage');
```

_If you find yourself playing with cookies a lot in your project, please use a library like this [JS Cookie](https://github.com/js-cookie/js-cookie) and save yourself a ton of time._

