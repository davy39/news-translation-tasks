---
title: An introduction to the JavaScript DOM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-27T18:19:32.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-javascript-dom-512463dd62ec
coverImage: https://cdn-media-1.freecodecamp.org/images/0*QqW2LsIY0wf5BeDv
tags:
- name: Document Object Model
  slug: document-object-model
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Gabriel Tanner

  The Javascript DOM (Document Object Model) is an interface that allows developers
  to manipulate the content, structure and style of a website. In this article, we
  will learn what the DOM is and how you can manipulate it using Javasc...'
---

By Gabriel Tanner

The Javascript DOM (Document Object Model) is an interface that allows developers to manipulate the content, structure and style of a website. In this article, we will learn what the DOM is and how you can manipulate it using Javascript. This article can also be used as a reference for the basic DOM operations.

### What is the DOM?

At the most basic level, a website consists of an HTML and CSS document. The browser creates a representation of the document known as Document Object Model (DOM). This document enables Javascript to access and manipulate the elements and styles of a website. The model is built in a tree structure of objects and defines:

* HTML elements as objects
* Properties and events of the HTML elements
* Methods to access the HTML elements

![Image](https://cdn-media-1.freecodecamp.org/images/g42eKZ-RmFNQVN5EZ1lF2wj67VqIdX7DMk4Z)
_HTML DOM model_

The places of the elements are referred to as nodes. Not only elements get nodes but also the attributes of elements and text get their own node (attribute-nodes and text-nodes).

### DOM Document

The DOM Document is the owner of all other objects in your webpage. That means if you want to access any object on your webpage you always have to start with the document. It also contains many important properties and methods that enable us to access and modify our website.

### Finding HTML Elements

Now that we understand what the DOM document is we can start getting our first HTML elements. There are many different ways to do so using the Javascript DOM here are the most common:

#### Get element by ID

The _getElementById()_ method is used to get a single element by its id. Let’s look at an example:

```
var title = document.getElementById(‘header-title’);
```

Here we get the element with the id of header-title and save it into a variable.

#### Get elements by class name

We can also get more than one object using the _getElementsByClassName()_ method which returns an array of elements.

```
var items = document.getElementsByClassName(‘list-items’);
```

Here we get all items with the class _list-items_ and save them into a variable.

#### Get element by tag name

We can also get our elements by tag name using the _getElementsByTagName()_ method.

```
var listItems = document.getElementsByTagName(‘li’);
```

Here we get all _li_ elements of our HTML document and save them into a variable.

#### Queryselector

The _querySelector()_ method returns the first element that matches a specified _CSS selector._ That means that you can get elements by id, class, tag and all other valid CSS selectors. Here I just list a few of the most popular options.

**Get by id:**

```
var header = document.querySelector(‘#header’)
```

**Get by class:**

```
var items = document.querySelector(‘.list-items’)
```

**Get by tag:**

```
var headings = document.querySelector(‘h1’);
```

**Get more specific elements:**

We can also get more specific elements using _CSS Selectors_.

```
document.querySelector(“h1.heading”);
```

In this example we search for a tag and a class at the same time and return the first element that passes the CSS Selector.

#### Queryselectorall

The _querySelectorAll()_ method is completely the same as the _querySelector()_ except that it returns all elements that fit the CSS Selector.

```
var heading = document.querySelectorAll(‘h1.heading’);
```

In this example, we get all _h1_ tags that have a class of _heading_ and store them in an array.

### Changing HTML Elements

The HTML DOM allows us to change the content and style of an HTML element by changing its properties.

#### Changing the HTML

The innerHTML property can be used to change the content of an HTML element.

```
document.getElementById(“#header”).innerHTML = “Hello World!”;
```

In this example we get the element with an id of header and set the inner content to “Hello World!”.

InnerHTML can also be used to put tags in another tag.

```
document.getElementsByTagName("div").innerHTML = "<h1>Hello World!</h1>"
```

Here we put a h1 tag into all already existing div.

#### **Changing a value of an attribute**

You can also change the value of an attribute using the DOM.

```
document.getElementsByTag(“img”).src = “test.jpg”;
```

In this example we change the src of all _<im_g/> t_ags to te_st.jpg.

#### Changing the style

To change the style of an HTML element we need to change the style property of our elements. Here is an example syntax for changing styles:

```
document.getElementById(id).style.property = new style
```

Now lets look at an example where we get an element and change the bottom border to a solid black line:

```
document.getElementsByTag(“h1”).style.borderBottom = “solid 3px #000”;
```

The CSS properties need to be written in camelcase instead of the normal css property name. In this example we used borderBottom instead of border-bottom.

### Adding and deleting elements

Now we will take a look at how we can add new elements and delete existing ones.

#### Adding elements

```
var div = document.createElement(‘div’);
```

Here we just create a div element using the _createElement()_ method which takes a tagname as a parameter and saves it into a variable. After that we just need to give it some content and then insert it into our DOM document.

```js
var newContent = document.createTextNode("Hello World!"); 
div.appendChild(newContent);
document.body.insertBefore(div, currentDiv);
```

Here we create content using the createTextNode() method which takes a String as a parameter and then we insert our new div element before a div that already exists in our document.

#### Deleting elements

```js
var elem = document.querySelector('#header');
elem.parentNode.removeChild(elem);
```

Here we get an element and delete it using the removeChild() method.

#### Replace elements

Now let’s take a look at how we can replace items.

```js
var div = document.querySelector('#div');
var newDiv = document.createElement(‘div’);
newDiv.innerHTML = "Hello World2"
div.parentNode.replaceChild(newDiv, div);
```

Here we replace an element using the _replaceChild()_ method. The first argument is the new element and the second argument is the element which we want to replace.

#### Writing directly into the HTML output stream

We can also write HTML expressions and JavaScript directly into the HTML output stream using the write() method.

```js
document.write(“<h1>Hello World!</h1><p>This is a paragraph!</p>”);
```

We can also pass JavaScript expressions like a date object.

```
document.write(Date());
```

The write() method can also take multiple arguments that will be appended to the document in order of their occurrence.

### Event Handlers

The HTML DOM also allows Javascript to react to HTML events. Here I’ve just listed some of the most important ones:

* mouse click
* page load
* mouse move
* input field change

#### Assign Events

You can define events directly in your HTML code using attributes on your tags. Here is an example of an _onclick_ event:

```
<h1 onclick=”this.innerHTML = ‘Hello!’”>Click me!</h1>
```

In this example, the text of the <h1/> will change to “Hello!” when you click the button.

You can also call functions when an event is triggered as you can see in the next example.

```
<h1 onclick=”changeText(this)”>Click me!</h1>
```

Here we call the _changeText()_ method when the button is clicked and pass the element as an attribute.

We can also assign the same events in our Javascript code.

```
document.getElementById(“btn”).onclick = changeText();
```

#### Assign Events Listeners

Now let’s look at how you can assign event listeners to your HTML elements.

```
document.getElementById(“btn”)addEventListener('click', runEvent);
```

Here we just assigned a clickevent that calls the runEvent method when our btn element is clicked.

You can also assign multiple events to a single element:

```
document.getElementById(“btn”)addEventListener('mouseover', runEvent);
```

### Node Relationships

The nodes in the DOM Document have a hierarchical relationship to each other. This means that the nodes are structured like a tree. We use the terms parent, sibling and child to describe the relationship between nodes.

The top node is called the root and is the only node that has no parent. The root in a normal HTML document is the <html/> tag because it has no parent and is the top tag of the document.

#### Navigating Between Nodes

We can navigate between nodes using these properties:

* parentNode
* childNodes
* firstChild
* lastChild
* nextSibling

Here is an example how you can get the parent element of an h1.

```
var parent = document.getElementById(“heading”).parentNode
```

### Conclusion

You made it all the way until the end! Hope that this article helped you understand the Javascript DOM and how to use it to manipulate elements on your website.

If you want to read more articles just like this one you can visit my [website](https://gabrieltanner.org/) or start following my [newsletter](https://gabrieltanner.us20.list-manage.com/subscribe/post?u=9d67fc028348a0eb71318768e&amp;id=6845ed3555).

If you have any questions or feedback, let me know in the comments down below.

