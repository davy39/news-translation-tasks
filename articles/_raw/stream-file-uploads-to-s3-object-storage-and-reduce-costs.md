---
title: How to Stream File Uploads to S3 Object Storage and Reduce Costs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-23T19:51:05.000Z'
originalURL: https://freecodecamp.org/news/stream-file-uploads-to-s3-object-storage-and-reduce-costs
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-pixabay-219717.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: node js
  slug: node-js
- name: S3
  slug: s3
seo_title: null
seo_desc: "By Austin Gil\nTo support file uploads in your application, you will have\
  \ to learn how to send files from the frontend and receive files on the backend.\
  \ \nThis tutorial is going to take a step back and explore architectural changes\
  \ that'll help you red..."
---

By Austin Gil

To support file uploads in your application, you will have to learn how to [send files from the frontend](https://austingil.com/uploading-files-with-html/) and [receive files on the backend](https://austingil.com/file-uploads-in-node/). 

This tutorial is going to take a step back and explore architectural changes that'll help you reduce costs when adding file uploads to your applications.

## Here's what we'll cover:

1. [What is Object Storage?](#heading-what-is-object-storage)
2. [What is S3?](#heading-what-is-s3)
3. [Start with an Existing Node.js Application](#id="start-with-an-existing-node-js-application")
4. [Set Up the S3 Client](#heading-set-up-the-s3-client)
5. [How to Modify formidable](#heading-how-to-modify-formidable)
6. [Walkthrough of the Whole Flow](#heading-walkthrough-of-the-whole-flow)
7. [Caveats](#heading-caveats)
8. [Closing Thoughts](#heading-closing-thoughts)

And here's a video walkthrough you can use to supplement this tutorial if you like:

%[https://www.youtube.com/watch?v=cJ6IuSJabXk]

Before we get too far, you should already be familiar with sending and receiving a `multipart/form-data` request, parsing the request, accessing the file stream, and writing that file to the disk **on the application server**.

Note that the flow described above writes files to the application server. This is pretty common, but there are some issues with this approach.

First, this approach doesn’t work for distributed systems that may rely on several different machines. If a user uploads a file it can be hard (or impossible) to know which machine received the request, and therefore, where the file is saved. This is especially true if you’re using serverless or edge compute.

Secondly, storing uploads on the application server can lead to the server to run out of disk space. At which point, we’d have to upgrade our server. That could be much more expensive than other cost-effective solutions.

And that’s where [Object Storage](https://www.linode.com/products/object-storage/) comes in.

## What is Object Storage?

You can think of Object Storage like a folder on a computer. You can put any files (aka “objects”) you want in it, but the folders (aka “buckets”) live within a cloud service provider. You can also access files via URL.

Object Storage provides a couple of benefits:

* It’s a single, central place to store and access all of your uploads.
* It’s designed to be highly available, easily scalable, and super cost-effective.

For example, if you consider [shared CPU servers](https://www.linode.com/products/shared/), you could run an application for $5/month and get 25 GB of disk space. If your server starts running out of space, you could upgrade your server to get an additional 25 GB, but that’s going to cost you $7/month more.

Alternatively, you could put that money towards Object Storage and you would get 250 GB for $5/month. So 10 times more storage space for less cost.

Of course, there are other reasons to upgrade your application server. You may need more RAM or CPU, but if we’re talking purely about disk space, Object Storage is a much cheaper solution.

With that in mind, the rest of this article will cover connecting an existing Node.js application to an Object Storage provider. We’ll use [formidable](https://github.com/node-formidable/formidable) to parse multipart requests, but configure it to upload files to Object Storage instead of writing to disk.

If you want to follow along, you will need to have an Object Storage bucket set up, as well as the access keys. Any S3-compatible Object Storage provider should work. 

Today, I’ll be using [Akamai’s cloud computing services](https://bit.ly/austinode) (formerly Linode). If you want to do the same, [here’s a guide that shows you how to get going](https://www.linode.com/docs/products/storage/object-storage/get-started/).

[And here’s a link to get $100 in free credits for 60 days](https://bit.ly/austinode).

## What is S3?

We'll get hands on with code shortly, but before we do, there’s one more concept that I should explain: S3. S3 stands for “Simple Storage Service”, and it’s an Object Storage product originally developed at AWS.

Along with their product, AWS came up with a standard communication protocol for interacting with their Object Storage solution.

As more companies started offering Object Storage services, they decided to also adopt the same S3 communication protocol for their Object Storage service, and S3 became a standard.

As a result, we have more options to choose from for Object Storage providers and fewer options to dig through for tooling. We can use the same libraries (maintained by AWS) with other providers. That’s great news because it means the code we write today should work across any S3-compatible service.

Today, we'll be working with a Node.js application and the libraries we’ll need are [`@aws-sdk/client-s3`](https://www.npmjs.com/package/@aws-sdk/client-s3) and [`@aws-sdk/lib-storage`](https://www.npmjs.com/package/@aws-sdk/lib-storage):

```
npm install @aws-sdk/client-s3 @aws-sdk/lib-storage
```

These libraries will help us upload objects into our buckets.

Okay, let’s write some code!

## Start with an Existing Node.js Application

We’ll start with an example [Nuxt.js](https://nuxt.com/) event handler that writes files to disk using formidable. It checks if a request contains `multipart/form-data` and if so, it passes the underlying Node.js request object (aka `IncomingMessage`) to a custom function `parseMultipartNodeRequest`. Since this function uses the Node.js request, it will work in any Node.js environment and tools like formidable.

```
import formidable from 'formidable';

/* global defineEventHandler, getRequestHeaders, readBody */

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
    const form = formidable({ multiples: true });
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

We’re going to modify this code to send the files to an S3 bucket instead of writing them to disk.

## Set Up the S3 Client

The first thing we need to do is set up an S3 Client to make the upload requests for us, so we don’t have to write them manually. We’ll import the `S3Client` constructor from `@aws-sdk/client-s3` as well as the `Upload` command from `@aws-sdk/lib-storage`. We’ll also import Node’s `stream` module to use later on.

```
import stream from 'node:stream';
import { S3Client } from '@aws-sdk/client-s3';
import { Upload } from '@aws-sdk/lib-storage';
```

Next, we need to configure our client using our S3 bucket **endpoint**, [**access key**](https://www.linode.com/docs/products/storage/object-storage/guides/access-keys/), [**secret access key**](https://www.linode.com/docs/products/storage/object-storage/guides/access-keys/), and **region**. Again, you should already have set up an S3 bucket and know where to find this information. If not, [check out this guide](https://www.linode.com/docs/products/storage/object-storage/get-started/) ([$100 credit](https://bit.ly/austinode)).

I like to store this information in environment variables and not hard-code the configuration into the source code. We can access those variables using `process.env` to use in our application.

```
const { S3_URL, S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION } = process.env;
```

If you’ve never used environment variables, they’re a good place for us to put secret information such as access credentials. You can [read more about them here](https://nodejs.dev/en/learn/how-to-read-environment-variables-from-nodejs/).

With our variables set up, I can now instantiate the S3 Client we’ll use to communicate to our bucket.

```
const s3Client = new S3Client({
  endpoint: `https://${S3_URL}`,
  credentials: {
    accessKeyId: S3_ACCESS_KEY,
    secretAccessKey: S3_SECRET_KEY,
  },
  region: S3_REGION,
});
```

It’s worth pointing out that the endpoint needs to include the HTTPS protocol. In Akamai’s Object Storage dashboard, when you copy the bucket URL, but it doesn’t include the protocol (`bucket-name.bucket-region.linodeobjects.com`). So I just add the prefix here.

With our S3 client configured, we can start using it.

## How to Modify formidable

In our application, we’re passing any multipart Node request into our custom function, `parseMultipartNodeRequest`. This function returns a Promise and passes the request to formidable, which parses the request, writes files to the disk, and resolves the promise with the form fields data and files data.

```
function parseMultipartNodeRequest(req) {
  return new Promise((resolve, reject) => {
    const form = formidable({ multiples: true });
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

This is the part that needs to change. Instead of processing the request and writing files to disk, we want to pipe file streams to an S3 upload request. So as each file chunk is received, it’s passed through our handler to the S3 upload.

We’ll still return a promise and use formidable to parse the form, but we have to change formidable’s [configuration options](https://github.com/node-formidable/formidable#options). We’ll set the `fileWriteStreamHandler` option to a function called `fileWriteStreamHandler` that we’ll write shortly.

```
/** @param {import('formidable').File} file */
function fileWriteStreamHandler(file) {
  // TODO
}
const form = formidable({
  multiples: true,
  fileWriteStreamHandler: fileWriteStreamHandler,
});
```

Here’s what their documentation says about `fileWriteStreamHandler`:

> `options.fileWriteStreamHandler` **{function}** – default `null`, which by default writes to host machine file system every file parsed; The function should return an instance of a [Writable stream](https://nodejs.org/api/stream.html#stream_class_stream_writable) that will receive the uploaded file data. With this option, you can have any custom behavior regarding where the uploaded file data will be streamed for. If you are looking to write the file uploaded in other types of cloud storages (AWS S3, Azure blob storage, Google cloud storage) or private file storage, this is the option you’re looking for. When this option is defined the default behavior of writing the file in the host machine file system is lost.

As formidable parses each chunk of data from the request, it will pipe that chunk into the Writable stream that’s returned from this function. So our `fileWriteStreamHandler` function is where the magic happens.

Before we write the code, let’s understand some things:

1. This function must return a [Writable stream](https://nodejs.org/api/stream.html#stream_class_stream_writable) to write each upload chunk to.
2. It **also** needs to pipe each chunk of data to an S3 Object Storage.
3. We can use the `Upload` command from `@aws-sdk/lib-storage` to create the request.
4. The request body can be a stream, but it must be a [Readable stream](https://nodejs.org/api/stream.html#stream_class_stream_readable), not a Writable stream.
5. A [Passthrough stream](https://nodejs.org/api/stream.html#stream_class_stream_passthrough) can be used as **both** a Readable and Writable stream.
6. Each request formidable will parse may contain multiple files, so we may need to track multiple S3 upload requests.
7. `fileWriteStreamHandler` receives one parameter of type [`formidable.File` interface](https://github.com/node-formidable/formidable#file) with properties like `originalFilename`, `size`, `mimetype`, and more.

OK, now let’s write the code. We’ll start with an `Array` to store and track all the S3 upload requests outside the scope of `fileWriteStreamHandler`. 

Inside `fileWriteStreamHandler`, we’ll create the `Passthrough` stream that will serve as both the Readable body of the S3 upload and the Writable return value of this function. 

We’ll create the `Upload` request using the S3 libraries, and tell it our bucket name, the object key (which can include folders), the object Content-Type, the Access Control Level for this object, and the `Passthrough` stream as the request body. 

We’ll instantiate the request using `Upload.done()` and add the returned `Promise` to our tracking `Array`. We might want to add the response `Location` property to the `file` object when the upload completes, so we can use that information later on. 

Lastly, we’ll return the `Passthrough` stream from this function:

```
/** @type {Promise<any>[]} */
const s3Uploads = [];

/** @param {import('formidable').File} file */
function fileWriteStreamHandler(file) {
  const body = new stream.PassThrough();
  const upload = new Upload({
    client: s3Client,
    params: {
      Bucket: 'austins-bucket',
      Key: `files/${file.originalFilename}`,
      ContentType: file.mimetype,
      ACL: 'public-read',
      Body: body,
    },
  });
  const uploadRequest = upload.done().then((response) => {
    file.location = response.Location;
  });
  s3Uploads.push(uploadRequest);
  return body;
}
```

A couple of things to note:

* `Key` is the name and location where the object will exist. It can include folders that will be created if they do not currently exist. If a file exists with the same name and location, it will be overwritten (fine for me today). You can avoid collisions by using hashed names or timestamps.
* `ContentType` is not required, but it’s helpful to include. It allows browsers to create the downloaded response appropriately based on Content-Type.
* `ACL`: is also optional, but by default, every object is private. If you want people to be able to access the files via URL (like an `<img>` element), you’ll want to make it public.
* Although `@aws-sdk/client-s3` supports uploads, you need `@aws-sdk/lib-storage` to support Readable streams.
* You can read more about the parameters [on NPM](https://www.npmjs.com/package/@aws-sdk/client-s3).

This way, formidable becomes the plumbing that connects the incoming client request to the S3 upload request.

Now there’s just one more change to make. We are keeping track of all the upload requests, but we aren’t waiting for them to finish.

We can fix that by modifying the `parseMultipartNodeRequest` function. It should continue to use formidable to parse the client request, but instead of resolving the promise immediately, we can use `Promise.all` to wait until all the upload requests have resolved.

The whole function looks like this:

```
/**
 * @param {import('http').IncomingMessage} req
 */
function parseMultipartNodeRequest(req) {
  return new Promise((resolve, reject) => {
    /** @type {Promise<any>[]} */
    const s3Uploads = [];

    /** @param {import('formidable').File} file */
    function fileWriteStreamHandler(file) {
      const body = new PassThrough();
      const upload = new Upload({
        client: s3Client,
        params: {
          Bucket: 'austins-bucket',
          Key: `files/${file.originalFilename}`,
          ContentType: file.mimetype,
          ACL: 'public-read',
          Body: body,
        },
      });
      const uploadRequest = upload.done().then((response) => {
        file.location = response.Location;
      });
      s3Uploads.push(uploadRequest);
      return body;
    }
    const form = formidable({
      multiples: true,
      fileWriteStreamHandler: fileWriteStreamHandler,
    });
    form.parse(req, (error, fields, files) => {
      if (error) {
        reject(error);
        return;
      }
      Promise.all(s3Uploads)
        .then(() => {
          resolve({ ...fields, ...files });
        })
        .catch(reject);
    });
  });
}
```

The resolved `files` value will also contain the `location` property we included, pointing to the Object Storage URL.

## Walkthrough of the Whole Flow

We covered a lot, and I think it’s a good idea to review how everything works together. If we look back at the original event handler, we can see that any `multipart/form-data` request will be received and passed to our `parseMultipartNodeRequest` function. The resolved value from this function will be logged to the console:

```
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
```

With that in mind, let’s break down what happens if I want to upload [a cute photo of Nugget making a big ol’ yawn](https://www.instagram.com/p/CmUxW6jDmWO/).

1. For the browser to send the file as binary data, it needs to make a `multiplart/form-data` request with an [HTML form](https://austingil.com/uploading-files-with-html/) or [with JavaScript](https://austingil.com/upload-files-with-javascript/).
2. Our Nuxt.js [application receives the `multipart/form-data`](https://austingil.com/file-uploads-in-node/) and passes the underlying Node.js request object to our custom `parseMultipartNodeRequest` function.
3. `parseMultipartNodeRequest` returns a `Promise` that will eventually be resolved with the data. Inside that `Promise`, we instantiate the formidable library and pass the request object to formidable for parsing.
4. As formidable is parsing the request when it comes across a file, it writes the chunks of data from the file stream to the `Passthrough` stream that’s returned from the `fileWriteStreamHandler` function.
5. Inside the `fileWriteStreamHandler` we also set up a request to upload the file to our S3-compatible bucket, and we use the same `Passthrough` stream as the body of the request. So as formidable writes chunks of file data to the `Passthrough` stream, they are also read by the S3 upload request.
6. Once formidable has finished parsing the request, all the chunks of data from the file streams are taken care of, and we wait for the list of S3 requests to finish uploading.
7. After all that is done, we resolve the `Promise` from `parseMultipartNodeRequest` with the modified data from formidable. The `body` variable is assigned to the resolved value.
8. The data representing the fields and files (not the files themselves) are logged to the console.

So now, if our original upload request contained a single field called “file1” with the photo of Nugget, we might see something like this:

```
{
  file1: {
    _events: [Object: null prototype] { error: [Function (anonymous)] },
    _eventsCount: 1,
    _maxListeners: undefined,
    lastModifiedDate: null,
    filepath: '/tmp/93374f13c6cab7a01f7cb5100',
    newFilename: '93374f13c6cab7a01f7cb5100',
    originalFilename: 'nugget.jpg',
    mimetype: 'image/jpeg',
    hashAlgorithm: false,
    createFileWriteStream: [Function: fileWriteStreamHandler],
    size: 82298,
    _writeStream: PassThrough {
      _readableState: [ReadableState],
      _events: [Object: null prototype],
      _eventsCount: 6,
      _maxListeners: undefined,
      _writableState: [WritableState],
      allowHalfOpen: true,
      [Symbol(kCapture)]: false,
      [Symbol(kCallback)]: null
    },
    hash: null,
    location: 'https://austins-bucket.us-southeast-1.linodeobjects.com/files/nugget.jpg',
    [Symbol(kCapture)]: false
  }
}
```

It looks very similar to the object formidable returns when it writes directly to disk. But this time it has an extra property, `location`, which is the Object Storage URL for our uploaded file.

Throw that sucker in your browser and what do you get?

![Screenshot of my browser showing a cute photo of Nugget making a big yawn, and there's a box highlighting the URL from Akamai Object Storage.](https://austingil.com/wp-content/uploads/image-65-1080x608.png)

That’s right! A cute photo of Nugget making a big ol’ yawn 🥰

I can also go to my bucket in my [Object Storage dashboard](https://cloud.linode.com/object-storage) and see that I now have a folder called “files” containing a file called “nugget.jpg”.

![Screenshot of my Akamai Object Storage dashboard showing "nugget.jpg" inside the "files" folder inside the "austins-bucket" Object Storage instance.](https://austingil.com/wp-content/uploads/image-62-1080x568.png)

## Caveats

I would be remiss if I didn’t mention the following. (In fact, I **was** remiss because I didn’t mention it until after someone pointed it out to me 🤣)

Streaming uploads through your backend to Object Storage is not the only way to upload files to S3. You can also use **signed URLs**. 

Signed URLs are basically the same URL in the bucket where the file will live, but they include an authentication signature that can be used by anyone to upload a file, as long as the signature has not expired (usually quite soon).

Here’s how the flow generally works:

1. Frontend makes a request to the backend for a signed URL.
2. Backend makes an authenticated request to the Object Storage provider for a signed URL with a given expiry.
3. Object Storage provider provides a signed URL to the backend.
4. Backend returns the signed URL to the frontend.
5. Frontend uploads the file directly to Object Storage thanks to the signed URL.
6. Optional: Frontend may make another request to the Backend if you need to update a database that the upload completed.

This flow requires a little more choreography than Frontend -> Backend -> Object Storage, but it has some benefits.

* It moves work off your servers, which can reduce load and improve performance.
* It moves the file upload bandwidth off your server. If you pay for ingress and have several large file uploads all the time, this could add up.

It also comes with its own costs.

* You have much less control over what users can upload. This might include malware.
* If you need to perform functions on the files like optimizing, you can’t do that with signed URLs.
* The complex flow makes it much harder to build an upload flow with progressive enhancement in mind.

As with most things in web development, there is not one right solution. It will largely depend on your use case. I like going through my backend, so I have more control over the files and I can simplify the frontend.

I wanted to share this streaming option, largely because there is hardly any content out there about streaming. Most content uses signed URLs (maybe I’m missing something). If you’d like to learn more about using signed URLs, [here is some documentation](https://www.linode.com/docs/products/storage/object-storage/guides/urls/#signed-urls) and [here’s a handy tutorial](https://dev.to/gathoni/how-to-upload-an-image-to-a-linode-storage-bucket-using-a-pre-signed-url-1ba7) by [Mary Gathoni](https://twitter.com/remigathoni).

## Closing Thoughts

Okay, we covered a lot today. I hope it all made sense. If not, feel free to reach out to me with questions. Also, reach out and let me know if you got it working in your own application.

I’d love to hear from you, because using Object Storage is an excellent architectural decision if you need a single, cost-effective place to store files.

Thank you so much for reading. If you liked this article, and want to support me, the best ways to do so are to [share it](https://twitter.com/share?via=heyAustinGil), [sign up for my newsletter](https://austingil.com/newsletter/), and [follow me on Twitter](https://twitter.com/heyAustinGil).

