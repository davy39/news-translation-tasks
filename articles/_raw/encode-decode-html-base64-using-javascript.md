---
title: How to Encode and Decode HTML Base64 using JavaScript – JS Encoding Example
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-08T19:20:23.000Z'
originalURL: https://freecodecamp.org/news/encode-decode-html-base64-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template-1.png
tags:
- name: encoding
  slug: encoding
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When building an application or writing a program, you may need to encode
  or decode with HTML Base64 in JavaScript.

  This is possible thanks to two Base64 helper functions that are part of the HTML
  specification and are supported by all modern browser...'
---

When building an application or writing a program, you may need to encode or decode with HTML Base64 in JavaScript.

This is possible thanks to two Base64 helper functions that are part of the HTML specification and are supported by all modern browsers.

In this article, you will learn about Base64 and how it works to convert binary data, regular [strings](https://www.freecodecamp.org/news/what-is-a-string-in-javascript/), and lots more into ASCII text.

## What is Base64?

[Base64](https://en.wikipedia.org/wiki/Base64) is a group of binary-to-text encoding schemes representing binary data in ASCII string format. It is commonly used to encode data that needs to be stored or transmitted in a way that cannot be directly represented as text.

Base64 encoding works by mapping binary data to 64 characters from the ASCII character set. The 64 characters used in Base64 encoding are: `A-Z`, `a-z`, `0-9`, `+`, and `/`.

The encoding process takes 3 bytes of binary data and maps it to 4 characters from the above set, such that a single character represents every 6 bits of binary data. The result is a string of ASCII characters that can be transmitted or stored as text.

Base64 decoding is the reverse process of encoding. It takes a Base64 encoded string and maps each character back to its 6-bit binary representation. The resulting binary data is a reconstruction of the original binary data encoded to Base64.

## How to Encode and Decode HTML Base64 using JavaScript

To encode and decode in JavaScript, you will use the `btoa()` and `atob()` JavaScript functions that are available and supported by modern web browsers.

These JavaScript helper functions are named after old Unix commands for converting binary to ASCII (btoa) and ASCII to binary (atob).

You can encode a string to base64 in JavaScript using the `btoa()` function and decode a base64 string using `atob()` function. For example, if you have a string stored in a variable, as seen below, you can first encode it to Base64:

```js
let myString = "Welcome to freeCodeCamp!";
let encodedValue = btoa(myString);
console.log(encodedValue); // V2VsY29tZSB0byBmcmVlQ29kZUNhbXAh
```

You can also decode the `encodedValue` back to its original form using the `atob()` function. This function takes the encoded value and decodes it from Base64:

```js
let myString = "Welcome to freeCodeCamp!";
let encodedValue = btoa(myString);
let decodedValue = atob(encodedValue);
console.log(decodedValue); // Welcome to freeCodeCamp!
```

You now know how to encode and decode Base64 in JavaScript.

## More JavaScript Encoding Examples

You can also encode binary data to Base64 encoded ASCII text in JavaScript using the `btoa()` function:

```js
let binaryData = new Uint8Array([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]);
let stringValue = String.fromCharCode.apply(null, binaryData);
console.log(stringValue); // "Hello World"

let encodedValue = btoa(stringValue);
console.log(encodedValue); // SGVsbG8gV29ybGQ=
```

In the above, you first converted Unicode values to characters and then encoded the string.

You can also decode the Base64 encoded ASCII text to binary data in JavaScript using the `atob()` function:

```js
let encodedValue = "SGVsbG8gV29ybGQ=";
let binaryData = new Uint8Array(atob(encodedValue).split("").map(function (c) {
    return c.charCodeAt(0);
}));
console.log(binaryData); // Uint8Array [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
```

## Wrapping Up!

In this article, you have learned what Base64 means, how it works, and when to encode and decode in JavaScript.

Base64 is not intended to be a secure encryption method, nor is it intended to be a compression method, because encoding a string to Base64 typically results in a 33% longer output.

Base64 encoding is commonly used in JavaScript for situations like:

* Storing and transmitting binary data as text.
    
* Encrypting data where the encoded data is sent over an insecure channel and decoded on the other end. However, it should not be considered a secure encryption method, as it can easily be decoded.
    
* Data transfer between systems with different character sets.
    
* Storing binary data in a database.
    

Thanks for reading and have fun coding!

You can access over 185 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.
