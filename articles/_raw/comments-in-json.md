---
title: Comments Inside JSON – Commenting in a JSON File
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-31T15:10:51.000Z'
originalURL: https://freecodecamp.org/news/comments-in-json
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--1-.png
tags:
- name: json
  slug: json
seo_title: null
seo_desc: 'JSON (JavaScript Object Notation) is a popular data interchange format
  used in web development and mobile applications due to its simplicity and flexibility.

  But JSON files do not officially support comments. This makes providing additional
  context o...'
---

JSON (JavaScript Object Notation) is a popular data interchange format used in web development and mobile applications due to its simplicity and flexibility.

But JSON files do not officially support comments. This makes providing additional context or explanation for the data challenging.

This article will show you how to include comments in JSON files and why JSON does not natively support comments.

## Why JSON Does Not Support Comments?

According to the JSON specification, a JSON document should only contain data structures like arrays and objects and not include comments. This is because JSON is intended to be a simple, easily parsable data format that can be quickly and efficiently processed.

Comments, while useful for providing additional context or explanation for human readers, can add complexity to the parsing process. This slows down performance and increases the risk of errors.

The primary reason why JSON does not support comments is that its creator, [Douglas Crockford](https://en.wikipedia.org/wiki/Douglas_Crockford), deliberately removed them from the format to prevent misuse and keep it as a pure data-only format.

Crockford observed that some people were using comments to store parsing directives, which could break compatibility between different systems. Hence, the decision to remove comments to maintain the simplicity and consistency of the format across various programming languages and environments.

As a result, the only option for adding comments to a JSON file is to use a workaround, such as using custom elements to store comments.

## How to Add Comments Inside JSON

When you add comments in the form `//`, `#`, or `/* */`, which are used in popular programming languages, you will notice the error “Comments are not permitted in JSON”.

![](https://paper-attachments.dropboxusercontent.com/s_7788E690364D593F2C3E31F8D1CF26EB90DAC0141414EE29BD5F57C061BD4347_1680020901125_image.png align="left")

Then, how can you add comments to a JSON file?

The only way this can be done is to include comments as data pairs in a JSON file. It is not a commonly used or recommended practice, but technically it’s the best way to add comments to your JSON file.

Create a custom element within your JSON object, such as "\_comment", to distinguish them from the rest of the data.

```json
{
    "_comment": "Put your JSON comment here"
    "name": "John Doe",
    "age": 35,
    "city": "New York City",
    "isMarried": true,
    "occupation": "Software Engineer",
}
```

**Note:** It's not compulsory that you use underscores. You can decide to use two slash such as “//comment” or any other allowed character. **The goal is to make it clear that it’s a comment**.

It's important to note that this approach may make the JSON file more complex and harder to parse. But if comments are added as custom elements, they will be received and processed like any other data in JSON on the server-side.

You now know how to add comments to your JSON file technically. But how can you add multiple comments? This is possible, but you should remember that JSON does not allow duplicate object keys. You must include unique letters or numbers in the comment element, ensuring it is valid and distinguishable from other elements in the JSON file.

```json
{
    "_comment1": "This is the basic data",
    "name": "John Doe",
    "age": 35,
    "city": "New York City",
    "_comment2": "Marital information",
    "isMarried": true,
    "wifeName": "Jane Doe"
}
```

When you have nested JSON objects, you can use similar object keys:

```json
{
    "_comment": "This is the basic data",
    "name": "John Doe",
    "age": 35,
    "city": "New York City",
    "maritalInfo": {
        "_comment": "Marital information",
        "isMarried": true,
        "wifeName": "Jane Doe"
    }
}
```

## Conclusion

You now know how to add comments to your JSON file. But because these comments are also processed and can be accessed, you need to be careful when adding comments to JSON files using custom elements.

Thanks for reading. Have fun coding!
