---
title: What is the Correct Content-Type for JSON? Request Header Mime Type Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-08T22:07:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-correct-content-type-for-json-request-header-mime-type-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fcf4739e6787e098393bd6d.jpg
tags:
- name: browser
  slug: browser
- name: internet
  slug: internet
- name: json
  slug: json
- name: servers
  slug: servers
seo_title: null
seo_desc: 'By Dillion Megida

  Every resource used on the internet has a media type, also known as a MIME type
  which stands for Multipurpose Internet Mail Extension. This information is necessary
  for transactions between server and client.

  The browser needs to kn...'
---

By Dillion Megida

Every resource used on the internet has a media type, also known as a MIME type which stands for Multipurpose Internet Mail Extension. This information is necessary for transactions between server and client.

The browser needs to know the media type of resources sent to it so that it can handle them properly.

The same goes for the server. It needs to know the type of resources sent to it for accurate parsing and processing.

## Where is the Content-Type declared?

The media type of any resource is declared in the `Content-Type` property of the request header (on the client, when making a request to the server) or in the response header (on the server, when sending a response).

Without explicitly declaring the content type of a resource, the client may attempt to automatically detect the type, but the result may not be accurate. This is why it's important to explicitly declare it.

## Media Types

Media types exist in various forms. They are categorized into various groups:

- application
- audio
- font
- example
- image
- message
- model
- multipart
- text
- and video

These categories also have their types. For example, `application/json` is a type under `application` and `text/html` is a type under `text`.

You can find a complete list of media types in the [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml) (a body that coordinates some of the key elements on the internet) media types.

All these types cover various data types like text, audio, images, HTML, and many more types that are used across the internet.

## The browser needs to know the media type of a resource

As I mentioned above, the browser needs to know what type of content it receives. Here's an example to illustrate that.

The following code is a Node server that serves an HTML file:

```js
const http = require("http");
const fs = require("fs");
const path = require("path");

const server = http.createServer(function (req, res) {
	const filePath = path.join(__dirname, "index.html");
	var stat = fs.statSync(filePath);

	res.writeHead(200, {
		"Content-Type": "text/css",
		"Content-Length": stat.size,
	});

	const readStream = fs.createReadStream(filePath);
	readStream.pipe(res);
});

server.listen(5000);

console.log("Node.js web server at port 5000 is running..");
```

Do not worry about the specifics of the code. All you're concerned with is the `index.htm` file we're serving and that the `Content-Type` is `text/css`.

Here's the content of `index.html`:

```html
<h1>Homepage</h1>
```

Of course, an HTML document is different from a  CSS file. Here's the result on `localhost:5000` when the server is started:

![Screenshot-2020-12-08-at-10.12.32](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-08-at-10.12.32.png)

You can also confirm the response gotten by checking the headers in the network tab of the DevTools.

Here's the result on a Chrome browser:

![Screenshot-2020-12-08-at-10.13.34](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-08-at-10.13.34.png)

The browser got the content as a CSS type, therefore, it tried treating it as CSS.

Also, note that full knowledge of the type of content gotten by the browser also reduces security vulnerabilities as the browser knows security standards to put in place for that data.

Now that you understand the concept of MIME types and their importance, let's head over to JSON.

## The Correct Content-Type for JSON

JSON has to be correctly interpreted by the browser to be used appropriately. `text/plain` was typically used for JSON, but according to [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml), the official MIME type for JSON is `application/json`.

This means when you're sending JSON to the server or receiving JSON from the server, you should always declare the `Content-Type` of the header as `application/json` as this is the standard that the client and server understand.

## Conclusion

As stated above, the server (just like the browser) needs to know the type of data sent to it, say, in a POST request. That's the reason `forms` with files usually contain the `enctype` attribute with a value of `multipart/form-data`. 

Without encoding the request this way, the POST request won't work. Also, once the server knows the type of data it has gotten, it then knows how to parse the encoded data.

In this article, we looked at what MIME types are and their purpose. Also, we looked at the official content type for JSON. I hope you now know why it's important to declare resource types when used across the internet.



