---
title: How to Validate URLs in JavaScript
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2022-11-22T04:12:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-urls-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/jase-bloor-oCZHIa1D4EU-unsplash--1-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: Regex
  slug: regex
- name: url
  slug: url
seo_title: null
seo_desc: 'A Uniform Resource Locator (URL) is what leads you to a page or file on
  the internet. URLs serve as the addresses of things on the internet.

  All valid URLs follow certain patterns. So if you know those patterns, you can determine
  whether a URL is val...'
---

A Uniform Resource Locator (URL) is what leads you to a page or file on the internet. URLs serve as the addresses of things on the internet.

All valid URLs follow certain patterns. So if you know those patterns, you can determine whether a URL is valid or not in your program and give feedback, throw an error, and so on.

In this tutorial, you will learn three methods to check if a string in JavaScript is a valid URL:

* [How to Use the `URL` Constructor to Validate URLs](#heading-how-to-use-the-url-constructor-to-validate-urls)
    
* [How to Use npm Packages to Validate URLs](#heading-how-to-use-npm-packages-to-validate-urls)
    
* [How to Use Regex to Validate URLs](#heading-how-to-use-regex-to-validate-urls)
    

## How to Use the `URL` Constructor to Validate URLs

When you pass a string to the `URL` constructor, it returns a new `URL` object if a string is a valid URL. Otherwise, it returns an error:

```javascript
const fccUrl = new URL("https://www.freecodecamp.org/");
console.log(fccUrl);
```

The following is what you get when you log `fccUrl` to the console:

![A URL object in JavaScript](https://www.freecodecamp.org/news/content/images/2022/11/validURL.PNG align="left")

*A* `URL` object in JavaScript

This object means that the string you passed to the `URL` constructor was a valid URL.

Now let's see what you get when you pass an invalid URL string:

```javascript
const fccUrl = new URL('freecodecamp');
console.log(fccUrl);
```

The string `'freecodecamp'` is not a valid URL. Thus, you get the following `TypeError`:

![A TypeError after passing an invalid URL to the URL constructor](https://www.freecodecamp.org/news/content/images/2022/11/invalidURL.PNG align="left")

*Invalid URL*

To recap:

1. When you pass a valid URL string to the `URL` constructor, it returns a new `URL` object.
    
2. When you pass an invalid URL string to the `URL` constructor, it returns a `TypeError`.
    

With this knowledge, you can create a custom function to check the validity of a given URL string.

### How to Create a URL Validator Function with the `URL` Constructor

By using the `URL` constructor and a `try...catch` statement, you can create a custom `isValidUrl` function:

```javascript
function isValidUrl(string) {
  try {
    new URL(string);
    return true;
  } catch (err) {
    return false;
  }
}
```

The `isValidUrl` function returns `true` when the string you pass as an argument is a valid URL. Otherwise, it returns `false`:

```javascript
console.log(isValidUrl('https://www.freecodecamp.org/')); // true
console.log(isValidUrl('mailto://mail@freecodecamp.org')); // true
console.log(isValidUrl('freecodecamp')); // false
```

### How to Validate Only HTTP URLs with the `URL` Constructor

Sometimes, you may want to check if the string is a valid HTTP URL, and reject other valid URLs like `'mailto://mail@freecodecamp.org'`.

If you look closely at the `URL` object, one of its properties is `protocol`:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/protocol.png align="left")

*The* `URL` object has a protocol property.

In the example above, the value of the protocol property is `'https:'`.

To check if a string is a valid HTTP URL, you can use the protocol property of the URL object:

```javascript
function isValidHttpUrl(string) {
  try {
    const newUrl = new URL(string);
    return newUrl.protocol === 'http:' || newUrl.protocol === 'https:';
  } catch (err) {
    return false;
  }
}

console.log(isValidHttpUrl('https://www.freecodecamp.org/')); // true
console.log(isValidHttpUrl('mailto://mail@freecodecamp.org')); // false
console.log(isValidHttpUrl('freecodecamp')); // false
```

The difference here is that you're not returning `true` after the new `URL` object is created. Instead, you're checking if the `protocol` property has a value equal to `'http:'` or `'https:'` and returning `true` if it is and `false` if not.

## How to Use npm Packages to Validate URLs

There are two NPM packages you can use: `is-url` and `is-url-http`.

These packages are the simplest way to check if a string is a valid URL. All you need to do is pass in a string as a parameter, and they will return `true` or `false`.

Let's see how both of these packages work.

### How to Validate URLs with the `is-url` Package

You can use the `is-url` package to check if a string is a valid URL. This package does not check the protocol of the URL passed to it.

To use `is-url`, first install it using the command below:

```javascript
npm install is-url
```

Then import it and pass your URL string to it as an argument:

```javascript
import isUrl from 'is-url';

const firstCheck = isUrl('https://www.freecodecamp.org/');
const secondCheck = isUrl('mailto://mail@freecodecamp.org');
const thirdCheck = isUrl('freeCodeCamp');

console.log(firstCheck); // true
console.log(secondCheck); // true
console.log(thirdCheck); // false
```

The `is-url` package returns `true` for strings that have valid URL formats and `false` for strings that have invalid URL formats.

In the example, both `firstCheck` (with the `https:` protocol) and `secondCheck` (with the `mailto:` protocol) return `true`.

### How to Validate HTTP URLs with the `is-http-url` Package

You can use the `is-url-http` package to check if a string is a valid HTTP URL.

Install the package with the following command:

```javascript
npm install is-url-http
```

Then import it and pass the URL string to it like so:

```javascript
import isUrlHttp from 'is-url-http';

const firstCheck = isUrlHttp('https://www.freecodecamp.org/');
const secondCheck = isUrlHttp('mailto://freecodecamp@mail.org');
const thirdCheck = isUrlHttp('freeCodeCamp');

console.log(firstCheck); // true
console.log(secondCheck); // false
console.log(thirdCheck); // false
```

In this example, only `firstCheck` returns `true`. The `is-url-http` package is not only checks that the string is a valid URL, it also checks if it's a valid HTTP URL. That is why it returns `false` for `secondCheck`, which is not a valid HTTP URL.

## How to Use Regex to Validate URLs

You can also use regex, or a regular expression, to check if a string is a valid URL or not.

All valid URLs follow a particular pattern. They have three main parts, which are:

* Protocol
    
* Domain name (or IP address)
    
* Port and path
    

Sometimes a query string or fragment locator follows the path.

You can learn more about URL patterns from this [freeCodeCamp article on the structure of URLs](https://www.freecodecamp.org/news/what-happens-when-you-hit-url-in-your-browser/).

Knowing the pattern URLs are made of, you can use regex to check for the existence of such patterns in a string. If the patterns exist, then the string passes the regex test. Otherwise, it fails.

Also, using regex, you can check for all valid URLs, or only check for valid HTTP URLs.

### How to Validate URLs with Regex

```javascript
function isValidUrl(str) {
  const pattern = new RegExp(
    '^([a-zA-Z]+:\\/\\/)?' + // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR IP (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
      '(\\#[-a-z\\d_]*)?$', // fragment locator
    'i'
  );
  return pattern.test(str);
}

console.log(isValidUrl('https://www.freecodecamp.org/')); // true
console.log(isValidUrl('mailto://freecodecamp.org')); // true
console.log(isValidUrl('freeCodeCamp')); // false
```

The regex in the `isValidUrl` function above checks if a string is a valid URL. The protocol check `^([a-zA-Z]+:\\/\\/)?` is not limited to just `https:`.

This is why the second example with the `mailto:` protocol returns `true`.

### How to Validate HTTP URLs with Regex

To use regex to check if a string is a valid HTTP URL, you need to edit the protocol check.

Instead of `^([a-zA-Z]+:\\/\\/)?`, you should use `'^(https?:\\/\\/)?'`:

```javascript
function isValidHttpUrl(str) {
  const pattern = new RegExp(
    '^(https?:\\/\\/)?' + // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
      '(\\#[-a-z\\d_]*)?$', // fragment locator
    'i'
  );
  return pattern.test(str);
}

console.log(isValidHttpUrl('https://www.freecodecamp.org/')); // true
console.log(isValidHttpUrl('mailto://freecodecamp.org')); // false
console.log(isValidHttpUrl('freeCodeCamp')); // false
```

Now only the first example which has a valid `https:` protocol returns `true`. Note that URL strings with `http:` work, too.

## Wrapping up!

In this article, you learned how to check the validity of URLs in JavaScript. You now know the following three methods for doing so.

* How to Use the `URL` Constructor to Validate URLs
    
* How to Use npm Packages to Validate URLs (`is-url` and `is-http-url`)
    
* How to Use Regex to Validate URLs
    

It's up to you to choose which method you're comfortable working with.

Thanks for reading. And happy coding!
