---
title: How to Extract an Error Object from a Blob API Response in JavaScript
subtitle: ''
author: Olabisi Olaoye
co_authors: []
series: null
date: '2024-03-29T00:34:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-extract-an-error-object-from-a-blob
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/React-form-validation--1-.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "I encountered an issue when I made a GET request in my React project which\
  \ was supposed to return a file I could download. For the file to download properly,\
  \ I had to make the response type a blob. \nBut if an error occurred when the server\
  \ returns a ..."
---

I encountered an issue when I made a GET request in my React project which was supposed to return a file I could download. For the file to download properly, I had to make the response type a [blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob). 

But if an error occurred when the server returns a JSON object, I'd be unable to get that object because I had already defined the response type as a blob. And if I remove the blob definition, the file would just return as regular JSON and might not download properly. 

So how do I get the blob to download it and retrieve the error object in case something didn't go well from the server? Thankfully, there's a way to achieve this. 

This guide will show you how to retain a JSON object for error handling purposes, while being able to download a file from a server. We'll be using [Axios](https://axios-http.com/), a JavaScript library used for making HTTP requests, to make our API call.

## Step 1: Define the Response Type in the API Call

First, define a function that makes the HTTP request to the server. In this case, we're expecting a file, so the conventional HTTP verb would be GET. 

The response type for Axios requests is JSON by default, but we want to change that to a blob like this:

```javascript
import axios from "axios";

const getFileFromServer = () => {
    const res = await axios.get('https://api.some-server.com', {responseType: 'blob'})?.data;
    return res;
}
```

## Step 2: Convert Blob To Text

In the previous step, we were able to get our file as a blob easily. But when it comes to showing the error, we need it to show as JSON. 

First, we need to wrap the request in a [try/catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) statement to specify what should happen if an error is thrown while the request is being made.

```javascript
import axios from "axios";

const getFileFromServer = async () => {
    try {
        const res = await axios.get('https://api.some-server.com', {responseType: 'blob'}).data;
    return res;
    }
    catch (error) {
        let errorResponse = await error.response.data.text();
        const errorObj = JSON.parse(response);
        console.log(errorObj) // log error to console
    }
}
```

The type conversion was done inside the `catch` block. First, we converted the response data to a JSON string using the `text()` method from JavaScript's [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

Finally, we used the `JSON.parse()` method to convert that string to actual JSON. That way, we can access the object in its intended format while being able to retrieve the file from the server if there is no error.

Logging the error object to the console will result in something like this:

```json
{
  "statusCode": 400,
  "message": "Some error occured"
}
```

## Conclusion

This is one of the problems I faced in real life, so I thought I'd share it in case someone else encounters it. 

Let me know your thoughts about the article, and feel free to make any suggestions you think could improve my solution.

Thanks for reading!

