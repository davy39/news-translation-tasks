---
title: How to Get the Current URL with JavaScript – JS Location Tutorial
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-25T00:34:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-current-url-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--10-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'If you''re a web developer, you''ll work with JavaScript when building
  dynamic and interactive web applications. One common task that you''ll need to perform
  is getting the current URL of a web page.

  In this article, you will learn how to get the curren...'
---

If you're a web developer, you'll work with JavaScript when building dynamic and interactive web applications. One common task that you'll need to perform is getting the current URL of a web page.

In this article, you will learn how to get the current URL using JavaScript's Location object. I'll show you some examples alongside some best practices.

## How to Use the Location Object

The Location object is a built-in JavaScript object that provides information about the current URL of a web page. It contains various properties allowing you to access and modify different parts of a URL.

To access the Location object, you can use the `window.location` property. This returns the Location object for the current web page. This object contains many data, such as the URL, pathname, origin, host, search data, and more.

For example:

```json
{
  "ancestorOrigins": {
    "0": "https://codepen.io"
  },
  "href": "https://cdpn.io/cpe/boomboom/index.html?editors=0012&key=index.html-f1981af8-7dc2-f8b6-669a-8980d4a8d02a",
  "origin": "https://cdpn.io",
  "protocol": "https:",
  "host": "cdpn.io",
  "hostname": "cdpn.io",
  "port": "",
  "pathname": "/cpe/boomboom/index.html",
  "search": "?editors=0012&key=index.html-f1981af8-7dc2-f8b6-669a-8980d4a8d02a",
  "hash": ""
}
```

## How to Access the Current URL With JavaScript

One common use case for the Location object is to get the current URL of a web page. You can do this by accessing the `href` property of the Location object.

The `href` property contains the complete URL of the current web page:

```js
const currentUrl = window.location.href;
console.log(currentUrl);
```

This will log the current URL of the web page to the console.

## How to Parse the Current URL With JavaScript

In addition to getting the current URL, you may need to parse it to extract specific parts. For example, you may want to extract the protocol, host, or path from the URL.

To parse the current URL, you can use the various properties of the Location object. For example, you can use the `protocol` property to get the protocol of the current URL:

```js
const protocol = window.location.protocol;
console.log(protocol);
```

This will log the protocol of the current URL (for example, "http:" or "https:") to the console.

Other properties of the Location object that you can use to extract parts of the current URL include `host`, `hostname`, `port`, `pathname`, `search`, and `hash`.

```js
const host = window.location.host;
const pathname = window.location.pathname;
const search = window.location.search;
const hash = window.location.hash;
```

Using these properties, you can extract various parts of the current URL.

## How to Update the Current URL With JavaScript

In addition to getting and parsing the current URL, you may need to update it. For example, you may need to redirect the user to a different URL or modify the current URL dynamically.

To update the current URL, you can use the various methods of the Location object. For example, you can use the `replace()` method to replace the current URL with a new URL:

```js
const newUrl = "https://example.com/new-page.html";
window.location.replace(newUrl);
```

This will replace the current URL with the new one, redirecting the user to the new page.

## Best Practices When Working With the Location Object

When working with the Location object, there are some best practices that you should follow to avoid potential pitfalls. For example, you should always check if the Location object is available before using it.

```js
if (window.location) {
  // Access or modify the Location object
}
```

You should also be careful when modifying the current URL, as it can affect the user's browsing experience. For example, you should avoid modifying the URL's protocol, host, or port unless absolutely necessary.

## Conclusion

In this article, you have learned how to get the current URL of a web page using JavaScript's Location object. By understanding how to work with the Location object, you can build more dynamic and interactive web applications that provide a better user experience.

Thank you for reading, and I hope you have found this article informative and helpful. You can read this article on [how to refresh a page with JavaScript](https://www.freecodecamp.org/news/javascript-refresh-page-how-to-reload-a-page-in-js/) for more information on working with URLs in JavaScript.

If you would like to learn more about JavaScript and web development, [Browse 200+ expert articles on web development](https://joelolawanle.com/contents) written by me, and also check out [my blog](https://joelolawanle.com/posts) for more captivating content.

Have fun coding!
