---
title: How to manipulate the DOM in Vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T07:44:07.000Z'
originalURL: https://freecodecamp.org/news/dom-manipulation-in-vanilla-js-2036a568dcd9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G7VizI4PMgWNbR6rRV28Rw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By carlos da costa

  So you have learned variables, selection structures, and loops. Now it is time to
  learn about DOM manipulation and to start doing some cool JavaScript projects.

  In this tutorial, we will learn how to manipulate the DOM with vanilla...'
---

By carlos da costa

So you have learned variables, selection structures, and loops. Now it is time to learn about DOM manipulation and to start doing some cool JavaScript projects.

In this tutorial, we will learn how to manipulate the DOM with vanilla JavaScript. With no further ado, let’s jump right into it.

### 1. First things first

Before we dive into coding, let’s learn what the Dom really is:

> The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects. That way, programming languages can connect to the page. [Source](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

Basically, when a browser loads a page it creates an object model of that page and prints it on the screen. The object model is represented in a tree data structure, each node is an object with properties and methods, and the topmost node is the document object.

A programming language can be used to access and modify this object model, and this action is called DOM manipulation. And we will do that with JavaScript because JS is awesome.

### 2. The actual tutorial

For the tutorial, we are going to need two files, one index.html, and the other manipulation.js.

```html
<!-- Index.html file -->
<html>  
  <head>    
    <title>DOM Manipulation</title>  
  </head>  

  <body>     
    <div id="division">
      <h1 id="head">
        <em>DOM<em> manipulation
      </h1>      

      <p class="text" id="middle">Tutorial</p>
      <p>Sibling</p>      
      <p class="text">Medium Tutorial</p>    
    </div>    

    <p class="text">Out of the div</p>    

    <!-- Then we call the javascript file -->
    <script src="manipulation.js"></script>  
  </body>
</html>

```

So there we have our HTML file, and as you can see we have a div with the id of division. Inside of that we have an h1 element, and in the same line, you will understand why later, we have two p elements and the div closing tag. Finally we have a p element with a class of text.

#### 2.1. Accessing the elements

We can either access a single element or multiple elements.

#### 2.1.1. Accessing a single element

For accessing a single element, we will look at two methods: getElementByID and querySelector.

```html
// the method below selects the element with the id of head

let id = document.getElementById('head');
```

```html
// The code below selects the first p element inside the first div

let q = document.querySelector('div p');

```

```html
/* Extra code */

// This changes the color to red
id.style.color = 'red';

// Give a font size of 30px
q.style.fontSize = '30px';

```

Now we have accessed two elements, the h1 element with the id of **head** and the first **p** element inside the div.

**getElementById** takes as argument an id, and **querySelector** takes as argument a CSS selector and returns the first element that matches the selector. As you can see I assigned the methods outcome into variables, and then I added some styling at the end.

#### 2.1.2. Accessing multiple elements

When accessing multiple elements, a node list is returned. It is not an array but it works like one. So you can loop through it and use the length property to get the size of the node list. If you want to get a specific element you can either use the array notation or the item method. You will see them in the code.

For accessing multiple elements we are going to use three methods: getElementsByClassName, getElementsByTagName, and querySelectorAll.

```html
// gets every element with the class of text

let className = document.getElementsByClassName('text');
```

```html
// prints the node list

console.log(className);
```

```html
/* prints the third element from the node list using array notation */

console.log(className[2]);
```

```html
/* prints the third element from the node list using the item function */

console.log(className.item(2));
```

```html
let tagName = document.getElementsByTagName('p');
let selector = document.querySelectorAll('div p');
```

The code seems to be self-explanatory, but I will explain it anyway because I am a nice dude. :)

First, we use the **getElementsByClassName** that takes a class name as an argument. It returns a node list with every element that has **text** as a class. Then we print the node list on the console. We also print the third element from the list using the **array notation** and the **item method**.

Second, we select every **p** element using the getElementsByTagName method that takes a tag name as an argument and returns a node list of that element.

Finally, we use the **querySelectorAll** method, that takes as an argument a CSS selector. In this case, it takes **div p** so it will return a node list of **p** elements inside a div.

As a practice exercise, print all the elements from **tagName** and **selector** node list and find out their size.

#### 2.2. Traversing the DOM

So far we have found a way of accessing specific elements. What if we want to access an element next to an element that we have already accessed, or access the parent node of a previously accessed element? The properties **firstChild, lastChild, parentNode, nextSibling,** and **previousSibling** can get this job done for us.

**firstChild** is used to get the first child element of a node. **lastChild**, as you guessed, it gets the last child element of a node. **parentNode** is used to access a parent node of an element. **nextSibling** gets for us the element next to the element already accessed, and **previousSibling** gets for us the element previous to the element already accessed.

```html
// Gets first child of the element with the id of division
let fChild = document.getElementById('division').firstChild;

// Logs the first child to the console
console.log(fChild);

```

```html
// Gets the last element from the element with the id of division
let lChild = document.querySelector('#division').lastChild;

```

```html
// Gets the parent node of the element with the id division
let parent = document.querySelector('#division').parentNode;

// Logs the parent node to the console
console.log(parent);

```

```html
// Selects the element with the id of middle
let middle = document.getElementById('middle');

// Prints on the console the next sibling of middle
console.log(middle.nextSibling);

```

The code above first gets the **firstChild** element of the element with the division id and then prints it on the console. Then it gets the **lastChild** element from the same element with the division id. Then it gets the **parentNode** of the element with the id of division and prints it on the console. Finally, it selects the element with the id of middle and prints its **nextSibling** node.

Most browsers treat white spaces between elements as text nodes, which makes these properties work differently in different browsers.

#### 2.3. Get and Updating element content

**2.3.1. Setting and getting text Content**

We can get or set the text content of elements. To achieve this task we are going to use two properties: **nodeValue** and **textContent**.

**nodeValue** is used to set or get the text content of a text node. **textContent** is used to set or get the text of a containing element.

```html
// Get text with nodeValue
let nodeValue = document.getElementById('middle').firstChild.nodeValue;

// Log the value to the console
console.log(nodeValue);

```

```html
// Set text with nodeValue
document.getElementById('middle').firstChild.nodeValue = "nodeValue text";

```

```html
// Get text with textContent
let textContent = document.querySelectorAll('.text')[1].textContent;

// Log the textContent to the console
console.log(textContent);

```

```
// Set text with textContent
document.querySelectorAll('.text')[1].textContent = 'new textContent set';

```

Did you notice the difference between **nodeValue** and **textContent**?

If you look carefully at the code above, you will see that for us to get or set the text with **nodeValue**, we first had to select the text node. First, we got the element with the **middle** id, then we got its **firstChild** which is the text node, then we got the **nodeValue** which returned the word Tutorial.

Now with **textContent**, there is no need to select the text node, we just got the element and then we got its **textContent**, either to set and get the text.

**2.3.2. Adding and Removing HTML content**

You can add and remove HTML content in the DOM. For that, we are going to look at three methods and one property.

Let’s start with the **innerHTML** property because it is the easiest way of adding and removing HTML content. **innerHTML** can either be used to get or set HTML content. But be careful when using innerHTML to set HTML content, because it removes the HTML content that is inside the element and adds the new one.

```html
// Set innerHTML of the element with id 'division'
document.getElementById('division').innerHTML =
`<ul>
  <li>Angular</li>
  <li>Vue</li>
  <li>React</li>
</ul>`;

```

If you run the code, you will notice that everything else in the div with the id of division will disappear, and the list will be added.

We can use the methods: **createElement()**, c**reateTextNode()**, and **appendChild()** to solve this problem.

createElement is used to create a new HTML `element.createTextNode` used to create a text node, and `appendChild` is used to append a new element into a parent element.

```html
// First, we create a new p element using createElement
let newElement = document.createElement('p');

/* Then we create a new text node and 
append the text node to the element created */
let text = document.createTextNode('Text Added!');
newElement.appendChild(text);

```

```html
/* Then we append the new element with the text node 
into the div with the id division. */
document.getElementById('division').appendChild(newElement);

```

There is also a method called **removeChild** used to remove HTML elements.

```html
// First, we get the element we want to remove
let toBeRemoved = document.getElementById('head');

// Then we get the parent node, using the parentNode property
let parent = toBeRemoved.parentNode;

/* Then we use the removeChild method, with the 
element to be removed as a parameter. */
parent.removeChild(toBeRemoved);

```

So first we get the element that we want to remove, and then we get its parent node. Then we called the method removeChild to remove the element.

#### 2.4. Attribute node

Now we know how to handle elements, so let’s learn how to handle the attributes of these elements. There are some methods like **GetAttribute**, **setAttribute**, **hasAttribute**, **removeAttribute**, and some properties like **className** and **id**.

**getAttribute** as its name may suggest, it is used to get an attribute. Like the class name, the id name, the href of a link or any other HTML attribute.

**setAttribute** is used to set a new attribute to an element. It takes two arguments, first the attribute and second the name of the attribute.

**hasAttribute** used to check if an attribute exists, takes an attribute as an argument.

**removeAttribute** used to remove an attribute, it takes an attribute as an argument.

**Id** this property is used to set or get the id of an element.

**ClassName** is used to set or get the class of an element.

```html
// Selects the first div
let d = document.querySelector('div');

// Checks if it has an id attribute, returns true/false
console.log('checks id: '+d.hasAttribute('id'));

// Set a new class attribute
d.setAttribute('class','newClass');

// Returns the class name
console.log(d.className);

```

I know I am a good dude, but that code is just self-explanatory.

### Conclusion

That is it! We have learned so many concepts, but there is more to learn about DOM manipulation. What we have covered here gives you a good foundation.

Go ahead and practice, and create something new to cement this new knowledge.

Good day, good coding.

