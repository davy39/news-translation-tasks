---
title: How to Upload Files with HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-04T20:17:14.000Z'
originalURL: https://freecodecamp.org/news/upload-files-with-html
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/HTML-Blog-Cover-1.png
tags:
- name: HTML
  slug: html
seo_title: null
seo_desc: 'By Austin Gil

  When building applications with HTML, you may eventually come to a point where you
  need to allow users to upload files. Surprisingly, it''s not quite as straightforward
  as you might assume.

  In this post, we''ll look at all things you need...'
---

By Austin Gil

When building applications with HTML, you may eventually come to a point where you need to allow users to upload files. Surprisingly, it's not quite as straightforward as you might assume.

In this post, we'll look at all things you need to support file uploads in HTML.

## How to Access Files

The very first step is accessing a file to upload. Unfortunately, or rather, fortunately, browsers can’t access our file systems. If they did, it would be a major security concern.

There is work being done on the [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API), but it’s experimental and will be limited access, so let’s just pretend it doesn’t exist.

Accessing a file requires user interaction, which means we need something in the UI for the user to interact with. Conveniently, there is the [input element with a file `type` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file).

```html
<input type="file" />
```

On its own, a file input isn’t very useful. It allows a user to select a file from their device, but that’s about it.

To actually send the file to a server, we need to make an [HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP), which means we need a `[<form>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)`. We’ll put the file input inside along with a `[<button>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)` to submit the form. 

The input will also need a `[<label>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)` to make it [accessible](https://austingil.com/category/accessibility/) for assistive technology, an `[id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)` attribute to associate it with the label, and a `name` attribute in order to include its data along with the HTTP request.

```html
<form>
  <label for="file">File</label>
  <input id="file" type="file" />
  <button>Upload</button>
</form>
```

Looks good 👍.

Doesn’t work good, though 👎.

## How to Include a Request Body

If we watch the [network tab](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/network/) as we submit the form, we can see that it generates a [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) request, and the payload is sent as a [query string](https://en.wikipedia.org/wiki/Query_string) that looks like this: “`?name=filename.txt`”. It’s essentially a key-value pair, with the key being the input [`name`](https://developer.mozilla.org/en-US/docs/Web/API/Attr/name) and the value being the name of the file.

This is sent as a string.

Not quite what we’re going for here.

We can’t actually send a file using a GET request because you can’t put a file in the query string parameters. We need to put the file in the [body of the request](https://developer.mozilla.org/en-US/docs/Web/API/Request/body). 

To do that, we need to send a [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) request, which we can do by changing the form’s `[method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/method)` attribute to `"post"`.

```html
<form method="post">
  <label for="file">File</label>
  <input id="file" name="file" type="file" />
  <button>Upload</button>
</form>
```

Now, if we explore that request, we can see that we are making a post request. We can also see that the request has a payload containing the form’s data. Unfortunately, the data is still just a key-value pair with the input `name` and the filename.

## How to Set the Content-Type

We’re still not actually sending the file, and the reason has to do with the request “[`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)”.

By default, when a form is submitted, the request is sent with a `Content-Type` of `application/x-www-form-urlencoded`. And unfortunately, we can’t send the binary file information as [URL encoded data](https://en.wikipedia.org/wiki/URL_encoding).

In order to send the file contents as [binary data](https://en.wikipedia.org/wiki/Binary_data), we have to change the `Content-Type` of the request to `multipart/form-data`. And in order to do that, we can set the form’s `[enctype](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/enctype)` attribute.

```html
<form method="post" enctype="multipart/form-data">
  <label for="file">File</label>
  <input id="file" name="file" type="file" />
  <button>Upload</button>
</form>
```

Now, if we submit the form one more time, we can see the request uses the POST method and has the `Content-Type` set to `multipart/form-data`. In Chromium browsers, you’ll no longer see the request payload, but you can see it in the Firefox DevTools under the request Params tab.

We did it!

## Recap

With all that in place, we can upload files using HTML. To re-iterate, sending files with HTML requires three things:

1. Create an input with the `type` of file to access the file system.
2. Use a form with `method="post"` to include a body on the request.
3. Set the request’s `Content-Type` to `multipart/form-data` using the `enctype` attribute.

Thank you so much for reading. If you liked this article, and want to support me, the best ways to do so are to [share it](https://twitter.com/share?via=heyAustinGil), [sign up for my newsletter](https://austingil.com/newsletter/), and [follow me on Twitter](https://twitter.com/heyAustinGil).

