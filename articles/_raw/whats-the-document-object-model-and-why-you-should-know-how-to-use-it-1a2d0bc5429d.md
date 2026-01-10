---
title: What’s the Document Object Model, and why you should know how to use it.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-07T21:16:41.000Z'
originalURL: https://freecodecamp.org/news/whats-the-document-object-model-and-why-you-should-know-how-to-use-it-1a2d0bc5429d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q8vHD5jcU_xZNqIgs-J-Pg.jpeg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Leonardo Maldonado

  So, you’ve studied HTML, you’ve created your first tags, learned about CSS, made
  beautiful forms, amazing buttons, responsive pages and have started to show everyone
  how amazing all that was.

  But then you decide that you want to...'
---

By Leonardo Maldonado

So, you’ve studied HTML, you’ve created your first tags, learned about CSS, made beautiful forms, amazing buttons, responsive pages and have started to show everyone how amazing all that was.

But then you decide that you want to take another step in your learning, and you’ve started wonder to yourself: “How can I add animation to my page? I wish that button made some animation on my page when I clicked it!”

Well, that’s where the DOM comes to solve your problem. You’ve probably heard a lot about it, but you might not know yet what is it and what problems it solves. So let’s dig in.

### So, what’s the DOM?

Do you know all those cool animations that you see around, that make you think to yourself, “Wow, I wish I could make something like that”? All of those animations are made by manipulating the DOM. I will now explain to you how to start manipulating it and making your websites look cooler.

The DOM (Document Object Model) is an interface that represents how your HTML and XML documents are read by the browser. It allows a language (JavaScript) to manipulate, structure, and style your website. After the browser reads your HTML document, it creates a representational tree called the Document Object Model and defines how that tree can be accessed.

### Advantages

By manipulating the DOM, you have infinite possibilities. You can create applications that update the data of the page without needing a refresh. Also, you can create applications that are customizable by the user and then change the layout of the page without a refresh. You can drag, move, and delete elements.

As I said, you have infinite possibilities — you just need to use your creativity.

### Representation by the browser

![Image](https://cdn-media-1.freecodecamp.org/images/3n6SPcMH0mmG6cFeB3SJBEA-9Yyfgp3xYZ7u)
_The representational tree that the browser create after it read your document._

In the image above, we can see the representational tree and how it is created by the browser. In this example, we have four important elements that you’re gonna see a lot:

1. **Document**: It treats all the _HTML_ documents.
2. **Elements**: All the tags that are inside your _HTML_ or _XML_ turn into a DOM element.
3. **Text**: All the tags’ content.
4. **Attributes**: All the attributes from a specific _HTML_ element. In the image, the attribute _class=”hero”_ is an attribute from the _<_p> element.

### Manipulating the DOM

Now we’re getting to the best part: starting to manipulate the DOM. First, we’re gonna create an HTML element as an example to see some methods and how events work.

```
<!DOCTYPE html>  <html lang="pt-br">  <head>      <meta charset="UTF-8">      <meta name="viewport" content="width=device-width, initial-scale=1.0">      <meta http-equiv="X-UA-Compatible" content="ie=edge">      <title>Entendendo o DOM (Document Object Model)</title>  </head>  <body>      <div class="container">          <h1><time>00:00:00</time></h1>          <button id="start">Start</button>          <button id="stop">Stop</button>          <button id="reset">Reset</button>      </div>  </body>  </html>
```

Very simple, right? Now we’re going to learn more about DOM methods: how to get our elements and start manipulating.

### Methods

The DOM has a lot of methods. They are the connection between our nodes (elements) and events, something that we’ll learn more about later. I’m gonna show you some of the most important methods and how they’re used. There are a lot more methods that I’m not going to show you here, but you can see all of them methods [here](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).

#### getElementById()

This method returns the element that contains the name _id_ passed. As we know, _id_’s should be unique, so it’s a very helpful method to get only the element you want.

```
var myStart = document.getElementsById('start');
```

**myStart**: Our variable name that looks similar to our _id_ passed.

**start**: _id_ passed. And in case we do not have any _id_ with that specific name, it returns _null_.

#### getElementsByClassName()

This method returns an _HTMLCollection_ of all those elements containing the specific name _class_ passed.

```
var myContainer = document.getElementsByClassName('container');
```

**myContainer**: Our variable name that looks similar to our _class_ passed.

**.container**: our _class_ passed. In case we do not have any _class_ with that specific name, it returns _null_.

#### getElementsByTagName()

This works the same way as those methods above: it also returns an _HTMLCollection,_ but this time with a single difference: it returns all those _elements_ with the tag name passed.

```
var buttons = document.getElementsByTagName('button');
```

**buttons**: Our variable name that looks similar to our _tag name_ passed.

**button**: _tag name_ that we want to get.

#### querySelector()

It returns the first _element_ that has the specific _CSS selector_ passed. Just remember that the _selector_ should follow the _CSS syntax_. In case you do not have any _selector_, it returns _null_.

```
var resetButton = document.querySelector('#reset');
```

**resetButton**: Our variable name that looks similar to our _selector_ passed.

**#reset**: _selector_ passed, and if you don’t have any _selector_ that matches it returns _null_.

#### querySelectorAll()

Very similar to the _querySelector()_ method, but with a single difference: it returns all the _elements_ that match with the _CSS selector_ passed. The _selector_ should also follow the _CSS syntax_. In case you do not have any _selector_, it returns _null_.

```
var myButtons = document.querySelector('#buttons');
```

**myButtons**: Our variable name that looks similar to our _selectors_ passed.

**#buttons**: _selector_ passed, if you don’t have any _selector_ that matches it returns _null_.

Those are some the most used DOM methods. There are several more methods that you can use, like the createElement(), which creates a new element in your HTML page, and setAttribute() that lets you set new attributes for elements HTML. You can explore them on your own.

Again, you can find all the methods [here](https://developer.mozilla.org/en-US/docs/Web/API/Element), on the left side in _Methods_. I really recommend you take a look at some of the others because you might need one of them sometime soon.

Now, we’re going to learn about **Events** — after all without them we can’t make animations in our pages.

### Events

The DOM elements have _methods_, as we just discussed, but they also have _events_. These events are responsible for make interactivity possible in our page. But here’s one thing that you might not know: _events_ are also _methods_.

#### click

One of the most used events is the click event. When the user clicks on a specific element, it will realize some action.

```
myStart.addEventListener('click', function(event) {
```

```
// Do something here.
```

```
}, false);
```

The addEventListener() parameters are:

1. The type of the event that you want (in this case ‘_click_’).
2. A callback function
3. The _useCapture_ by default is false. It indicates whether or not you want to “capture” the event.

#### select

This events is for when you want to _dispatch_ something when a specific element is selected. In that case we’re gonna _dispatch_ a simple _alert_.

```
myStart.addEventListener('select', function(event) {
```

```
alert('Element selected!');
```

```
}, false);
```

These are some of the most commonly used events. Of course, we have a lot of other events that you can use, like drag & drop events — when a user starts to drag some element you can make some action, and when they drop that element you can make another action.

Now, we’re gonna see how we can traverse the DOM and use some properties.

### Traversing the DOM

You can traverse the DOM and use some properties that we’re gonna see now. With these properties, you can return elements, comments, text, and so on.

#### .childNodes

This property returns a _nodeList_ of child _nodes_ of the given element. It returns text, comments, and so on. So, when you want to use it, you should be careful.

```
var container = document.querySelector('.container');
```

```
var getContainerChilds = container.childNodes;
```

#### .firstChild

This property returns the first child of the given element.

```
var container = document.querySelector('.container');
```

```
var getFirstChild = container.firstChild;
```

#### .nodeName

This property returns the name of the given element. In this case, we passed a _div_, so it will return “_div_”.

```
var container = document.querySelector('.container');
```

```
var getName = container.nodeName;
```

#### .nodeValue

This property is specific for **texts and comments**, as it returns or sets the value of the current _node_. In this case, since we passed a div, it will return _null_.

```
var container = document.querySelector('.container')
```

```
var getValue = container.nodeValue;
```

#### .nodeType

This property returns the **type** of the given element. In this case, it returns “_1_”.

```
var container = document.querySelector('.container')
```

```
var getValue = container.nodeType;
```

But, what does “_1_” mean anyway? It is basically the **nodeType** of the given element. In this case, it is an __ELEMENT_NODE__ and returns null. If this were an attribute, it would be returned as “_2_” to us and the attribute value.

![Image](https://cdn-media-1.freecodecamp.org/images/YOtuBjNlEsuJckztC-v5YHKvTJx2PNQBQQ23)
_A table containing all types of nodeTypes and the nodeName and nodeValue returned of each of them._

You can read more about _nodeTypes_ [here](https://www.w3schools.com/jsref/prop_node_nodetype.asp).

### Elements

These properties, instead of those above, return to us only **elements**. They are more often used and recommended because they can cause less confusion and are easier to understand.

#### .parentNode

This property returns the parent of the node given.

```
var container = document.querySelector('.container')
```

```
var getParent = container.parentNode;
```

#### .firstElementChild

Returns the first child element of the given element.

```
var container = document.querySelector('.container')
```

```
var getValue = container.firstElementChild;
```

#### .lastElementChild

Returns the last child element of the given element.

```
var container = document.querySelector('.container')
```

```
var getValue = container.lastElementChild;
```

These are some of the many properties that the DOM has. It’s very important for you to know the basics about the DOM, how it works, and its methods and properties, because some day you may need it.

### Conclusion

The DOM provides us with several important API's for creating fantastic and innovative applications. If you understand the basics of it you can create incredible things. If you want to read more about the DOM, you can click [here](https://developer.mozilla.org/en-US/docs/Glossary/DOM) and read all the MDN docs.

? F[**ollow me on Twitter!**](https://twitter.com/leonardomso)   
**⭐** F[**ollow me on GitHub!**](https://github.com/leonardomso)

_I’m looking for a remote opportunity, so if have any I’d love to hear about it, so please contact me!_

