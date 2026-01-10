---
title: How to Handle File Uploads on the Back End in Node.js and Nuxt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-20T22:27:42.000Z'
originalURL: https://freecodecamp.org/news/handle-file-uploads-on-the-backend-in-node-js-nuxt
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Command-Line-Blog-Cover.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: JavaScript
  slug: javascript
- name: node
  slug: node
seo_title: null
seo_desc: 'By Austin Gil

  In some previous tutorials, I covered how to upload files using HTML and JavaScript.
  It requires sending HTTP requests with the [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)
  header set to multipa...'
---

By Austin Gil

In some previous tutorials, I covered how to upload files using [HTML](https://austingil.com/uploading-files-with-html/) and [JavaScript](https://austingil.com/upload-files-with-javascript/). It requires sending HTTP requests with the `[Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)` header set to `multipart/form-data`.

Today, we are going to the back end to receive those `multipart/form-data` requests and access the binary data from those files.

## Some Background

Most of the concepts in this tutorial should broadly apply across frameworks, runtimes, and languages, but the code examples will be more specific.

I’ll be working within a [Nuxt.js](https://nuxt.com/) project that runs in a [Node.js](https://nodejs.org/) environment. Nuxt has some specific ways of [defining API routes](https://nuxt.com/docs/guide/directory-structure/server) which require calling a global function called `defineEventHandler`.

```javascript
/**
 * @see https://nuxt.com/docs/guide/directory-structure/server
 * @see https://nuxt.com/docs/guide/concepts/server-engine
 * @see https://github.com/unjs/h3
 */
export default defineEventHandler((event) => {
  return { ok: true };
});
```

The `event` argument provides access to work directly with the underlying Node.js request object (a.k.a. `IncomingMessage`) through `event.node.req`. So we can write our Node-specific code in an abstraction, like a function called `doSomethingWithNodeRequest` that receives this Node request object and does something with it.

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  doSomethingWithNodeRequest(event.node.req);

  return { ok: true };
});

/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  // Do not specific stuff here
}
```

Working directly with Node in this way means the code and concepts should apply regardless of whatever higher-level framework you’re working with. Ultimately, finish things up working in Nuxt.js.

## How to Deal with `multipart/form-data` in Node.js

In this section, we’ll dive into some low-level concepts that are good to understand, but not strictly necessary. Feel free to skip this section if you are already familiar with chunks and streams and buffers in Node.js.

Uploading a file requires sending a `multipart/form-data` request. In these requests, the browser will split the data into little “[chunks](https://en.wikipedia.org/wiki/Chunking_(computing))” and send them through the connection, one chunk at a time. This is necessary because files can be too large to send in as one massive payload.

Chunks of data being sent over time make up what’s called a “[stream](https://en.wikipedia.org/wiki/Stream_(computing))”. Streams are kind of hard to understand the first time around, at least they were for me. They deserve a full article (or many) on their own, so I’ll share [web.dev’s excellent guide](https://web.dev/streams/) in case you want to learn more.

Basically, a stream is sort of like a conveyor belt of data, where each chunk can be processed as it comes in. In terms of an HTTP request, the backend will receive parts of the request, one bit at a time.

Node.js provides us with an event handler API through the request object’s `on` method, which allows us to listen to “data” events as they are streamed into the backend.

```javascript
/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  req.on("data", (data) => {
    console.log(data);
  }
}
```

For example, when I upload [a photo of Nugget making a cute yawny face](https://www.instagram.com/p/CmUxW6jDmWO/), then look at the server’s console, I’ll see some weird things that look like this:

![Screenshot of a terminal with two logs of text that begin with "<Buffer", then a long list of two digit hex values, and end with a large number and "... more bytes>"](https://austingil.com/wp-content/uploads/image-63-1080x103.png)
_I used a screenshot here to prevent assistive technology from reading that gibberish out loud. Could you imagine?_

These two pieces of garbled nonsense are called “[buffers](https://developer.mozilla.org/en-US/docs/Glossary/buffer)” and they represent the two chunks of data that made up the request stream containing the cute photo of Nugget.

> A buffer is a storage in physical memory used to temporarily store data while it is being transferred from one place to another. – [MDN](https://developer.mozilla.org/en-US/docs/Glossary/buffer)

Buffers are another weird, low-level concept I have to explain when talking about working with files in JavaScript. 

JavaScript doesn’t work directly on binary data, so we get to learn about buffers. It’s also OK if these concepts still feel a little vague. Understanding everything completely is not the important part right now, and as you continue to learn about file transfers, you’ll gain a better knowledge of how it all works together.

Working with one partial chunk of data is not super useful. What we can do instead is rewrite our function into something we can work with:

1. Return a `[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)` to make the async syntax easy to work with.
2. Provide an `[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)` to store the chunks of data to use later on.
3. Listen for the “data” event and add the chunks to our collection as they arrive.
4. Listen to the “end” event and convert the chunks into something we can work with.
5. Resolve the `Promise` with the final request payload.
6. We should also remember to handle “error” events.

```javascript
/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  return new Promise((resolve, reject) => {
    /** @type {any[]} */
    const chunks = [];
    req.on('data', (data) => {
      chunks.push(data);
    });
    req.on('end', () => {
      const payload = Buffer.concat(chunks).toString()
      resolve(payload);
    });
    req.on('error', reject);
  });
}
```

And every time that the request receives some data, it pushes that data into the array of chunks.

So with that function set up, we can actually `[await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)` that returned `Promise` until the request has finished receiving all the data from the request stream, and log the resolved value to the console.

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  const body = await doSomethingWithNodeRequest(event.node.req);
  console.log(body)

  return { ok: true };
});
```

This is the request body. Isn’t it beautiful?

![Sceenshot of a terminal containing a long string of unintelligible text including alphanumerical values as well as symbols and characters that cannot be rendered. It legitimately looks like alien writing](https://austingil.com/wp-content/uploads/image-64-1080x479.png)
_I honestly don’t even know what a screen reader would do with if this was plain text._

If you upload an image file, it’ll probably look like an alien has hacked your computer. Don’t worry, it hasn’t. That’s literally what the text contents of that file look like. You can even try opening up an image file in a basic text editor and see the same thing.

If I upload a more basic example, like a `.txt` file with some plain text in it, the body might look like this:

```
Content-Disposition: form-data; name="file"; filename="dear-nugget.txt"
Content-Type: text/plain

I love you!
------WebKitFormBoundary4Ay52hDeKB5x2vXP--
```

Notice that the request is broken up into different sections for each form field. The sections are separated by the “form boundary”, which the browser will inject by default. 

I’ll skip going into excess details, so if you want to read more, check out `[Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition)` on MDN. The important thing to know is that `multipart/form-data` requests are much more complex than just key/value pairs.

Most server frameworks provide built-in tools to access the body of a request. So we’ve actually reinvented the wheel. For example, Nuxt provides a global `readBody` function. So we could have accomplished the same thing without writing our own code:

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  const body = await readBody(event.node.req);
  console.log(body)

  return { ok: true };
});
```

This works fine for other content types, but for `multipart/form-data`, it has issues. The entire body of the request is being read into memory as one giant string of text. This includes the `Content-Disposition` information, the form boundaries, and the form fields and values. Never mind the fact that the files aren’t even being written to disk. 

The big issue here is if a very large file is uploaded, it could consume all the memory of the application and cause it to crash.

The solution is, once again, working with streams.

When our server receives a chunk of data from the request stream, instead of storing it in memory, we can pipe it to a different stream. Specifically, we can send it to a stream that writes data to the file system using `[createWriteStream](https://nodejs.org/api/fs.html#filehandlecreatewritestreamoptions)`. As the chunks come in from the request, that data gets written to the file system, then released from memory.

That’s about as far down as I want to go into the low-level concepts. Let’s go back up to solving the problem without reinventing the wheel.

## How to Use a Library to Stream Data onto Disk

Probably my best advice for handling file uploads is to reach for a library that does all this work for you:

* Parse `multipart/form-data` requests
* Separate the files from the other form fields
* Stream the file data into the file system
* Provide you with the form field data as well as useful data about the files

Today, I’m going to be using this library called [formidable](https://github.com/node-formidable/formidable/). You can install it with `npm install formidable`, then import it into your project.

```javascript
import formidable from 'formidable';
```

Formidable works directly with the Node request object, which we conveniently already grabbed from the Nuxt event (“Wow, what amazing foresight!!” 🤩).

So we can modify our `doSomethingWithNodeRequest` function to use formidable instead. It should still return a promise because formidable uses callbacks, but promises are nicer to work with. Otherwise, we can mostly replace the contents of the function with formidable. 

We’ll need to create a formidable instance and use it to parse the request object. As long as there isn’t an error, we can resolve the promise with a single object that contains both the form fields and the files.

```javascript
/**
 * @param {import('http').IncomingMessage} req
 */
function doSomethingWithNodeRequest(req) {
  return new Promise((resolve, reject) => {
    /** @see https://github.com/node-formidable/formidable/ */
    const form = formidable({ multiples: true })
    form.parse(req, (error, fields, files) => {
      if (error) {
        reject(error);
        return;
      }
      resolve({ ...fields, ...files });
    });
  });
}
```

This provides us with a handy function to parse `multipart/form-data` using promises and access the request’s regular form fields, as well as information about the files that were written to disk using streams.

Now, we can examine the request body:

```javascript
export default defineEventHandler((event) => {
  const nodeRequestObject = event.node.req;

  const body = await doSomethingWithNodeRequest(event.node.req);
  console.log(body)

  return { ok: true };
});
```

We should see an object containing all the form fields and their values, but for each file input, we’ll see an object that represents the uploaded file, and not the file itself. This object contains all sorts of useful information including its path on disk, name, [mimetype](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types), and more.

```javascript
{
  file-input-name: PersistentFile {
    _events: [Object: null prototype] { error: [Function (anonymous)] },
    _eventsCount: 1,
    _maxListeners: undefined,
    lastModifiedDate: 2023-03-21T22:57:42.332Z,
    filepath: '/tmp/d53a9fd346fcc1122e6746600',
    newFilename: 'd53a9fd346fcc1122e6746600',
    originalFilename: 'file.txt',
    mimetype: 'text/plain',
    hashAlgorithm: false,
    size: 13,
    _writeStream: WriteStream {
      fd: null,
      path: '/tmp/d53a9fd346fcc1122e6746600',
      flags: 'w',
      mode: 438,
      start: undefined,
      pos: undefined,
      bytesWritten: 13,
      _writableState: [WritableState],
      _events: [Object: null prototype],
      _eventsCount: 1,
      _maxListeners: undefined,
      [Symbol(kFs)]: [Object],
      [Symbol(kIsPerformingIO)]: false,
      [Symbol(kCapture)]: false
    },
    hash: null,
    [Symbol(kCapture)]: false
  }
}
```

You’ll also notice that the `newFilename` is a hashed value. This is to ensure that if two files are uploaded with the same name, you will not lose data. You can, of course, modify how files are written to disk.

Note that in a standard application, it’s a good idea to store some of this information in a persistent place, like a database, so you can easily find all the files that have been uploaded. But that’s not the point of this post.

Now there’s one more thing I want to fix. I only want to process `multipart/form-data` requests with formidable. Everything else can be handled by a built-in body parser like the one we saw above.

So I’ll create a “body” variable first, then check the request headers, and assign the value of the body based on the “Content-Type”. I’ll also rename my function to `parseMultipartNodeRequest` to be more explicit about what it does.

Here’s what the whole thing looks like (note that `getRequestHeaders` is another built-in Nuxt function):

```javascript
import formidable from 'formidable';

/**
 * @see https://nuxt.com/docs/guide/concepts/server-engine
 * @see https://github.com/unjs/h3
 */
export default defineEventHandler(async (event) => {
  let body;
  const headers = getRequestHeaders(event);

  if (headers['content-type']?.includes('multipart/form-data')) {
    body = await parseMultipartNodeRequest(event.node.req);
  } else {
    body = await readBody(event);
  }
  console.log(body);

  return { ok: true };
});

/**
 * @param {import('http').IncomingMessage} req
 */
function parseMultipartNodeRequest(req) {
  return new Promise((resolve, reject) => {
    /** @see https://github.com/node-formidable/formidable/ */
    const form = formidable({ multiples: true })
    form.parse(req, (error, fields, files) => {
      if (error) {
        reject(error);
        return;
      }
      resolve({ ...fields, ...files });
    });
  });
}
```

This way, we have an API that is robust enough to accept `multipart/form-data`, plain text, or URL-encoded requests.

## 📯📯📯 Finishing up

There’s no emoji rave horn, so those will have to do. We covered kind of a lot, so let’s do a little recap.

When we upload a file using a `multipart/form-data` request, the browser will send the data one chunk at a time, using a stream. That’s because we can’t put the entire file in the request object at once.

In Node.js, we can listen to the request’s “data” event to work with each chunk of data as it arrives. This gives us access to the request stream.

Although we could capture all of that data and store it in memory, that’s a bad idea. A large file upload could consume all the server’s memory, causing it to crash.

Instead, we can pipe that stream somewhere else, so each chunk is received, processed, then released from memory. One option is to use `[fs.createWriteStream](https://nodejs.org/api/fs.html#fscreatewritestreampath-options)` to create a `[WritableStream](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream)` that can write to the file system.

Instead of writing our own low-level parser, we should use a tool like formidable. But we need to confirm that the data is coming from a `multipart/form-data` request. Otherwise, we can use a standard body parser.

We covered a lot of low-level concepts, and landed on a high-level solution. Hopefully, it all made sense and you found this useful.

If you have any questions or if something was confusing, please go ahead and [reach out to me](https://austingil.com/). I’m always happy to help.

Thank you so much for reading. If you liked this article, and want to support me, the best ways to do so are to [share it](https://twitter.com/share?via=heyAustinGil), [sign up for my newsletter](https://austingil.com/newsletter/), and [follow me on Twitter](https://twitter.com/heyAustinGil).

