---
title: 'AJAX Tutorial: What AJAX Is and How to Use it'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-22T17:37:00.000Z'
originalURL: https://freecodecamp.org/news/ajax-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c72740569d1a4ca3245.jpg
tags:
- name: Ajax
  slug: ajax
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'What is AJAX?

  AJAX stands for Asynchronous JavaScript And XML. It is not a programming language.
  It is a technology for developing better, faster and interactive Web Applications
  using HTML, CSS, JavaScript and XML.


  HTML : Hypertext Markup Language ...'
---

## **What is AJAX?**

**AJAX** stands for **Asynchronous JavaScript And XML**. It is not a programming language. It is a technology for developing better, faster and interactive Web Applications using HTML, CSS, JavaScript and XML.

1. HTML : Hypertext Markup Language (HTML) is used for defining the structure of a Web Application.
2. CSS : Cascading Style Sheet (CSS) is used to provide look and style to a Web Application.
3. JavaScript : JavaScript is used for making a Web Application interactive, interesting and user friendly.
4. XML : Extensible Markup Language (XML) is a format to store and transport data from the Web Server.

### What's the meaning of Asynchronous in AJAX?

Asynchronous means that the the Web Application could send and receive data from the Web Server without refreshing the page. This background process of sending and receiving data from the server along with updating different sections of a web page defines Asynchronous property/feature of AJAX.

## How AJAX works

AJAX makes use of a browser built-in **XMLHttpRequest object** to request data from a Web Server and **HTML DOM** to display or use the data.

**XMLHttpRequest Object** : It is an API in the form an object whose methods help in transfer of data between a web browser and a web server.

**HTML DOM** : When a web page is loaded, the browser creates a Document Object Model of the page.

![Image](https://i.imgur.com/pfC7QFH.png)

**Create a XMLHttpRequest Object :**

```javascript
var xhttp = new XMLHttpRequest();
```

**Properties of XMLHttpRequest object :**

`readystate` is a property of the XMLHttpRequest Object which holds the status of the XMLHttpRequest.

* 0: request not initialized
* 1: server connection established
* 2: request received
* 3: processing request
* 4: request finished and response is ready

```onreadystatechange``` is a property of the XMLHttpRequest Object which defines a function to be called when the readyState property changes.  
```status``` is a property of the XMLHttpRequest Object which returns the status-number of a request

* 200: "OK"
* 403: "Forbidden"
* 404: "Not Found"

**XMLHttpRequest Object Methods :** To send a request to a Web Server, we use the open() and send() methods of the XMLHttpRequest object.

```javascript
xhttp.open("GET", "content.txt", true);
xhttp.send();
```

**Create a function changeContent() using JavaScript :**

```javascript
function changeContent() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("foo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "content.txt", true);
  xhttp.send();
}
```

**AJAX example to change content of a web page :**

```html
<!DOCTYPE html>
<html>
<body>

<div id="foo">
<h2>The XMLHttpRequest Object</h2>
<button type="button" onclick="changeContent()">Change Content</button>
</div>

<script>
function changeContent() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("foo").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "content.txt", true);
  xhttp.send();
}
</script>

</body>
</html>
```

The file `content.txt` should be present in the root directory of the Web Application.

