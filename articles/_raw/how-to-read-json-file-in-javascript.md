---
title: How to Read a JSON File in JavaScript – Reading JSON in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-02T21:35:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-json-file-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template--5-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: json
  slug: json
seo_title: null
seo_desc: 'When fetching data from external sources or servers, you need to make sure
  that the data returned is in JSON format. Then you can consume the data within your
  application.

  In some situations, when you''re working locally or when you upload the data fi...'
---

When fetching data from external sources or servers, you need to make sure that the data returned is in JSON format. Then you can consume the data within your application.

In some situations, when you're working locally or when you upload the data file to a server, we might want to read these JSON data from a file.

We'll learn how to do that in this tutorial.

## How to Read a JSON File in JavaScript with the Fetch API

One standard method we can use to read a JSON file (either a local file or one uploaded to a server) is with the Fetch API. It uses the same syntax for both. The only difference would be the URL.

For example, suppose we have a local file within our project's folder named `data.json` that contains the following JSON data:

```json
<!--./data.JSON-->

{
    "id": 1,
    "title": "Hello World",
    "completed": false
}
```

We can now read this file in JavaScript using the Fetch API method:

```js
<!--./index.js-->

fetch('./data.json')
    .then((response) => response.json())
    .then((json) => console.log(json));
```

In the above, we have been able to read a local JSON file. But unfortunately, when we run this in a browser, we might get the following CORS error because our file is not on a server:

![](https://paper-attachments.dropbox.com/s_9630F87AB23B79DCD31DCDD0E14D2C6C4A3007934D2E561803A41CF5C1FE0085_1659464623693_image.png align="left")

To fix this, we will make sure our JSON file is on a local or remote server. If we use the Live server on our IDE, we won't get this error. But when we load our file directly, we will get this error.

As I said earlier, suppose we have this JSON file on a remote server and are trying to read this file in JavaScript. The same syntax will work:

```js
<!--./index.js-->

fetch('https://server.com/data.json')
    .then((response) => response.json())
    .then((json) => console.log(json));
```

The fetch API is the preferable method to use when we want to read a JSON file either from an external server or local file into our JavaScript file.

## How to Read a JSON file in JavaScript with the Import Statement

Another method we can use aside from making an HTTP request is the import statement. This method has a few complications, but we will address them all.

Just like in the previous section, suppose we have our JSON file that holds user data, such as `user.json`:

```json
<!--./user.JSON-->

{
    "id": 1,
    "name": "John Doe",
    "age": 12
}
```

We can read this JSON data in JavaScript using the import statement this way:

```js
<!---./index.js-->

import data from './data.json';
console.log(data);
```

Unfortunately, this will throw an error saying we cannot use the import statement outside a module. This is a standard error when we try to use the `import` statement in a regular JavaScript file, especially for developers who are new to JavaScript.

To fix this, we can add the `type="module"` script tag in our HTML file where we referenced the JavaScript file, like this:

```HTML
<html lang="en">
    // ...
    <body>
        <script type="module" src="./index.js"></script>
    </body>
</html>
```

When we do this, we'll still get another error:

![](https://paper-attachments.dropbox.com/s_9630F87AB23B79DCD31DCDD0E14D2C6C4A3007934D2E561803A41CF5C1FE0085_1659465574774_image.png align="left")

To fix this error, we need to add the file type of JSON to the import statement, and then we'll be able to read our JSON file in JavaScript:

```bash
import data from './data.json' assert { type: 'json' };
console.log(data);
```

This works perfectly as long as we run our files on a local or remote server. But suppose we run this locally – then we would get the CORS error.

![](https://paper-attachments.dropbox.com/s_9630F87AB23B79DCD31DCDD0E14D2C6C4A3007934D2E561803A41CF5C1FE0085_1659464623693_image.png align="left")

## Wrapping Up

In this article, we have learned how to read a JSON file in JavaScript and the possible errors we might encounter when using each method.

It's best to use the fetch API method when you want to make an HTTP request. For example, suppose we are fetching data from a mock JSON file which we will eventually pull from an API.

Still, in a situation where we don't need to use an HTTP request, we could use the import statement. We can use the import statement when we use a library like React, Vue, and so on which has to do with modules. This means we won't need to add the type of module, and also, we won't need to add the type of file.

Neither method requires you to install a package or use a library as they are inbuilt. Choosing which method to use is totally up to you.

But a quick tip that differentiates these methods is that the Fetch API reads a JSON file in JavaScript by sending an HTTP request, while the import statement does not require any HTTP request but rather works like every other import we make.

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
