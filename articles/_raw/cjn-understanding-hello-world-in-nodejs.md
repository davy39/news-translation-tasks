---
title: Understanding Hello World in Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-27T10:08:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-understanding-hello-world-in-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-26-at-3.14.04-PM.png
tags:
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
seo_title: null
seo_desc: "By Clark Jason Ngo\nHow I wish there was a documentation that shows me\
  \ a detailed explanation of what's happening in a Hello World example. \nWell. Instead\
  \ of wishing, I started to craft a nice visual for my own and I hope this would\
  \ help others as wel..."
---

By Clark Jason Ngo

How I wish there was a documentation that shows me a detailed explanation of what's happening in a Hello World example. 

Well. Instead of wishing, I started to craft a nice visual for my own and I hope this would help others as well.

**Some basic explanations:**

**What is Node.js?**

* An open source server environment.
* It allows you to run JavaScript on the server.

**Node.js uses asynchronous programming**

* generate dynamic page content
* create, open, read, write, delete, and close files on the server
* collect form data
* add, delete, and modify data in your database

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-150.png)
_HTTP Server_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-151.png)
_function and parameters req and res_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-152.png)
_Status code_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-153.png)
_Content-Type_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-154.png)
_Finishing the request_

---

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-155.png)
_Listening to the port_

---

Things you need to run this on your machine:

1. Install VSCode: [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Install Node.js: [https://nodejs.org/en/](https://nodejs.org/en/).
3. Create a file named `app.js`.
4. Copy the code below.
5. In your terminal, execute `node app.js`. 
6. In your browser, type [http://localhost:8080/](http://localhost:8080/) and hit Enter.

```js
var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
}).listen(8080);
```

%[https://youtu.be/sTB3oP_5UXU]

**References:**

[https://www.w3schools.com/nodejs/default.asp](https://www.w3schools.com/nodejs/default.asp)

[https://nodejs.org/api/http.html](https://nodejs.org/api/http.html)

