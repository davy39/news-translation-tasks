---
title: How to Upload Files with JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-06T20:27:40.000Z'
originalURL: https://freecodecamp.org/news/upload-files-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/JavaScript-Blog-Cover.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Austin Gil

  I recently published a tutorial showing how to upload files with HTML. That''s great,
  but it''s a bit limited to using the native browser form behavior, which causes
  the page to refresh.

  In this tutorial, I want to show you how to do the ...'
---

By Austin Gil

I recently published [a tutorial showing how to upload files with HTML](https://austingil.com/uploading-files-with-html/). That's great, but it's a bit limited to using the native browser form behavior, which causes the page to refresh.

In this tutorial, I want to show you how to do the same thing with [JavaScript](https://austingil.com/category/javascript/) to avoid the page refresh. That way, you can have the same functionality, but with better user experience.

%[https://www.youtube.com/watch?v=Zyjgc2bySZo]

## How to Set Up an Event Handler

Let's say you have an [HTML](https://austingil.com/category/html/) form that looks like this:

```html
<form action="/api" method="post" enctype="multipart/form-data">
  <label for="file">File</label>
  <input id="file" name="file" type="file" />
  <button>Upload</button>
</form>
```

With HTML, to access a file on the user’s device, we have to use an [`<input>` with the “file” `type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file). And in order to create the [HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP) to upload the file, we have to use a `[<form>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)` element.

When dealing with JavaScript, the first part is still true. We still need the file input to access the files on the device. But browsers have a [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) that we can use to make HTTP requests without forms.

I still like to include a form because:

1. [Progressive enhancement](https://austingil.com/resilient-applications-progressive-enhancement/): If JavaScript fails for whatever reason, the HTML form will still work.
2. I’m lazy: The form will actually make my work easier later on, as we’ll see.

With that in mind, for JavaScript to submit this form, I’ll set up a “submit” [event handler](https://developer.mozilla.org/en-US/docs/Web/Events/Event_handlers).

```js
const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);

/** @param {Event} event */
function handleSubmit(event) {
  // The rest of the logic will go here.
}
```

Throughout the rest of this article, we’ll only be looking at the logic within the event handler function, `handleSubmit`.

## How to Prepare the HTTP Request

The first thing I need to do in this submit handler is call the event’s `[preventDefault](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)` method to stop the browser from reloading the page to submit the form. I like to put this at the end of the event handler so that if there is an [exception](https://developer.mozilla.org/en-US/docs/Glossary/Exception) thrown within the body of this function, `preventDefault` will **not** be called, and the browser will fall back to the default behavior.

```js
/** @param {Event} event */
function handleSubmit(event) {
  // Any JS that could fail goes here
  event.preventDefault();
}
```

Next, we’ll want to construct the HTTP request using the Fetch API. The Fetch API expects the [first argument to be a URL](https://developer.mozilla.org/en-US/docs/Web/API/fetch#resource), and a second, [optional argument as an Object](https://developer.mozilla.org/en-US/docs/Web/API/fetch#options).

We can get the URL from the form’s `[action](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/action)` property. It’s available on any [form DOM node](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement) which we can access using the event’s `[currentTarget](https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget)` property. If the `action` is not defined in the HTML, it will default to the browser’s current URL.

```js
/** @param {Event} event */
function handleSubmit(event) {
  const form = event.currentTarget;
  const url = new URL(form.action);

  fetch(url);

  event.preventDefault();
}
```

Relying on the HTML to define the URL makes it more declarative, keeps our event handler reusable, and our JavaScript bundles smaller. It also maintains functionality if the JavaScript fails.

By default, Fetch sends HTTP requests using the `[GET](https://www.freecodecamp.org/news/javascript-get-request-tutorial/)` method, but to upload a file, we need to use a `[POST](https://www.freecodecamp.org/news/javascript-post-request-how-to-send-an-http-post-request-in-js/)` method. We can change the method using `fetch`‘s optional second argument. I’ll create a variable for that object and assign the `method` property, but once again, I’ll grab the value from the form’s `[method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/method)` attribute in the HTML.

```js
const url = new URL(form.action);

/** @type {Parameters<fetch>[1]} */
const fetchOptions = {
  method: form.method,
};

fetch(url, fetchOptions);
```

Now the only missing piece is actually including the payload in the body of the request.

## How to Add the Request Body

If you’ve ever created a Fetch request in the past, you may have included the body as a [JSON string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) or a `[URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)` object. Unfortunately, neither of those will work to send a file, as they don’t have access to the binary file contents.

Fortunately, there is the `[FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)` browser API. We can use it to construct the request body from the form DOM node. And conveniently, when we do so, it even sets the request’s `[Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)` header to `multipart/form-data` – also a necessary step to transmit the binary data.

```js
const url = new URL(form.action);
const formData = new FormData(form);

/** @type {Parameters<fetch>[1]} */
const fetchOptions = {
  method: form.method,
  body: formData,
};

fetch(url, fetchOptions);
```

That’s really the bare minimum needed to upload files with JavaScript. Let’s do a little recap:

1. Access to the file system using a file type input.
2. Construct an HTTP request using the Fetch (or [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)) API.
3. Set the request method to `POST`.
4. Include the file in the request body.
5. Set the HTTP `Content-Type` header to `multipart/form-data`.

Today we looked at a convenient way of doing that, using an HTML form element with a submit event handler, and using a `FormData` object in the body of the request. The current `handleSumit` function should look like this:

```js
/** @param {Event} event */
function handleSubmit(event) {
  const url = new URL(form.action);
  const formData = new FormData(form);

  /** @type {Parameters<fetch>[1]} */
  const fetchOptions = {
    method: form.method,
    body: formData,
  };

  fetch(url, fetchOptions);

  event.preventDefault();
}
```

Unfortunately, the current submit handler is not very reusable. Every request will include a body set to a `FormData` object and a “`Content-Type`” header set to `multipart/form-data`. This is too brittle. Bodies are not allowed in `GET` requests, and we may want to support different content types in other POST requests.

## How to Make it Reusable

We can make our code more robust to handle `GET` and `POST` requests, and send the appropriate `Content-Type` header. We’ll do so by creating a `[URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)` object in addition to the `FormData`, and running some logic based on whether the request method should be `POST` or `GET`. I’ll try to lay out the logic below:

Is the request using a `POST` method?

— Yes: is the form’s `[enctype](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/enctype)` attribute `multipart/form-data`?

— — Yes: set the body of the request to the `FormData` object. The browser will automatically set the “`Content-Type`” header to `multipart/form-data`.

— — No: set the body of the request to the `URLSearchParams` object. The browser will automatically set the “`Content-Type`” header to `application/x-www-form-urlencoded`.

— No: We can assume it’s a `GET` request. Modify the URL to include the data as query string parameters.

The refactored solution looks like:

```js
/** @param {Event} event */
function handleSubmit(event) {
  /** @type {HTMLFormElement} */
  const form = event.currentTarget;
  const url = new URL(form.action);
  const formData = new FormData(form);
  const searchParams = new URLSearchParams(formData);

  /** @type {Parameters<fetch>[1]} */
  const fetchOptions = {
    method: form.method,
  };

  if (form.method.toLowerCase() === 'post') {
    if (form.enctype === 'multipart/form-data') {
      fetchOptions.body = formData;
    } else {
      fetchOptions.body = searchParams;
    }
  } else {
    url.search = searchParams;
  }

  fetch(url, fetchOptions);

  event.preventDefault();
}
```

I really like this solution for a number of reasons:

* It can be used for any form.
* It relies on the underlying HTML as the declarative source of configuration.
* The HTTP request behaves the same as with an HTML form. This follows the principle of progressive enhancement, so file upload works the same when JavaScript is working properly or when it fails.

So, that’s it. That’s [uploading files with JavaScript](https://austingil.com/upload-files-with-javascript/).

Thank you so much for reading. I hope you found this useful. If you liked this article, and want to support me, the best ways to do so are to [share it](https://twitter.com/share?via=heyAustinGil), [sign up for my newsletter](https://austingil.com/newsletter/), and [follow me on Twitter](https://twitter.com/heyAustinGil).

