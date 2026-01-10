---
title: JS DOM Manipulation Best Practices – with Examples
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-12T17:41:27.000Z'
originalURL: https://freecodecamp.org/news/dom-manipulation-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/freecodecamp-javascript-benjamin-semah.png
tags:
- name: best practices
  slug: best-practices
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, you can manipulate the content of a web page using the Document
  Object Model (DOM). But how do you write code that is readable, easy to maintain,
  and not prone to performance issues?

  That''s what we''ll cover in this article. I''ll discus...'
---

In JavaScript, you can manipulate the content of a web page using the Document Object Model (DOM). But how do you write code that is readable, easy to maintain, and not prone to performance issues?

That's what we'll cover in this article. I'll discuss some important best practices so that you can manipulate the DOM with confidence.

## Table of Contents

* [Introduction](#)
    
* [Use the DOMContentLoaded Event](#user-the-domcontentloaded-event)
    
* [Cache Selected Elements](#cache-selected-elements)
    
* [Query Parent Instead of Document](#query-parent-elements-instead-of-document)
    
* [Use CSS Classes to Style Elements](#use-css-classes-to-style-elements)
    
* [Use innerHTML With Caution](#use-innerhtml-with-caution)
    
* [Write Readable Event Listeners](#write-readable-event-listeners)
    
* [Use Event Delegation to Handle DOM Events](#use-event-delegation-to-handle-dom-events)
    
* [Batch DOM Updates With Fragment](#batch-dom-updates-with-fragment)
    
* [Use the stopPropagation Method](#use-the-stoppropagation-method)
    
* [Test your DOM Manipulation code](#test-your-dom-manipulation-code)
    
* [Conclusion](#conclusion)
    

## User the `DOMContentLoaded` Event

The `DOMContentLoaded` event is fired when the HTML document is fully loaded. Using this event ensures that your DOM manipulation code runs only after the document is fully loaded.

To use the `DOMContentLoaded`, add an event listener to the document and listen for the `DOMContentLoaded` event. This helps prevent any issues that may come up when you try to manipulate elements that are yet to be rendered.

Example:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  // Your DOM manipulation code goes here...
})
```

## Cache Selected Elements

When you have frequently used elements, querying the DOM for the same element anytime over and over is inefficient. It's better to query the DOM once and store the result in variables.

```javascript
const cachedElement = document.getElementById('exampleId')
```

This way you can reference the variables anytime you want to use them. This helps improve performance as it reduces unnecessary work.

## Query Parent Elements Instead of Document

When you cache an element, you can also query it to select any of its descendants. This can help improve performance because it limits the scope of the query and reduces the number of times the entire document is queried.

Example:

```html
<div id="parent">
    <p id="child">Example paragraph</p>
</div>
```

```javascript
const parentElement = document.getElementById('parent')

// Options 1: Querying entire document ❌
const childFromDocument = document.getElementById('child') 

// Options 2: Query the parent element ✅
const childFromParent = parentElement.querySelector('#child')
```

In the example above is a simple markup containing a `#parent` div and `.child` paragraph. Then there are two options for selecting the child element.

Technically, both options are correct and will select the same element. But the difference is in the scope of the query.

Example 1 queries (or searches) the entire document to find and select the child. This is less performant and not even necessary because the parent of the element you intend to select is already cached.

Example 2 narrows the scope of the query (or search) by querying only the parent element and not the whole document. That's why it's preferred because it's more performant – especially when the document is large.

Also, note that the method used for querying the parent is `querySelector`. Using `getElementById` to query the parent won't work and will result in an error.

## Use CSS Classes to Style Elements

It's best to use CSS classes to style elements instead of using inline styles. Classes are easy to maintain compared to inline styles which can be hard to manage.

The `classList` property has useful properties like add, remove, toggle, and others that makes it easy to modify styles.

Example:

```css
.styledClass {
  color: red;
}
```

```javascript
element.classList.add('styledClass')
```

This example uses the `.add` property of `classList` to add the `styledClass` to the element. Assuming you wanted to remove the class from the element, you can easily do so using the `.remove` property in place of add.

## Use `innerHTML` with Caution

The `innerHTML` property reads and parses HTML markup that you pass to it. This means it can read and run code in a script tag passed to it. And this can pose a security risk to your application.

Where possible, use the `innerText` or `textContent` property to render strings. But if you need to use `innerHTML`, be sure you're using it to insert content from trusted sources. Or sanitize and validate the provided content with a library like DOMPurify.

You can read [this freeCodeCamp article](https://www.freecodecamp.org/news/innerhtml-vs-innertext-vs-textcontent/#what-is-the-innerhtml-property) to learn more about `innerHTML`.

## Write Readable Event Listeners

Often you will pass two arguments to event listeners. The first is the event you're listening to and the second is the event handler (the function that fires when the event occurs).

To make your code easy to read and maintain, you can define the event handler function outside of the event listener. Then you can call it within the even listener, like in example 1 below:

```javascript
Example 1 ✅

MyElement.addEventListener('click', handleClick) 

function handleClick() { 
    // your logic goes here.. 
} 

// Example 2 ❌ 

myElement.addEventListener('click', function() { 
    // your logic goes here... 
})
```

Both are technically correct and will do the same thing. But example 1 is preferred because it's easier to read. Also, you can reuse the `handleClick` function if you need to. This helps you observe the DRY (Don't Repeat Yourself) principle.

## Use Event Delegation to Handle DOM Events

Event delegation is when you attach an event listener on a parent element to listen to events on its descendants. With this technique, you can reduce the number of event listeners to include in your code.

For example, assume you have five buttons inside a parent div:

```html
<div id="parent"> 
    <button id="btn-1">1st Button</button> 
    <button id="btn-2">2nd Button</button> 
    <button id="btn-3">3rd Button</button> 
    <button id="btn-4">4th Button</button> 
    <button id="btn-5">5th Button</button> 
</div>
```

You can add an event listener to each of the five buttons to listen to a click. Or using event delegation, you can a single event on only the parent div:

```javascript
const parentElement = document.getElementById('parent') 

parentElement.addEventListener('click', handleClick) 

function handleClick(event) { 
  alert(event.target.id) 
}
```

In this example, the event to delegated to the parent element. And we're using `event.target.id` to get the actual button the user clicked. If you are curious, you can [run the code on Stackblitz](https://stackblitz.com/edit/js-r3qjyd?file=index.html,index.js) to see how it works.

Event delegation help saves time improve performance. Imagine how this technique can come in handy when dealing with a large amount of dynamic content.

## Batch DOM Updates With Fragment

Frequent updates to the DOM can affect the performance of your application. Try to reduce the number of updates where possible.

A useful feature you can use to batch updates is the `.createDocumentFragment` property. It allows you to group multiple updates before inserting them into the document. This reduces reflows and makes your code more effecient.

Example without Fragment:

```javascript
const container = document.getElementById('container')

for (let i = 0; i < 1000; i++) { 
    const listItem = document.createElement('li')
    listItem.textContent = `Item ${i}`
    container.appendChild(listItem) 
}
```

This code updates with each iteration of the loop. That means the DOM will be update 1,000 times. There is a more efficient way of doing this with the code below that uses fragment.

Example with fragment:

```javascript
const container = document.getElementById('container') 
const fragment = document.createDocumentFragment()

// Add multiple list items to the fragment 
for (let i = 0; i < 1000; i++) { 
    const listItem = document.createElement('li') 
    listItem.textContent = `Item ${i}` 
    fragment.appendChild(listItem)
} 

container.appendChild(fragment)
```

The code above appends the `listItem` to the `fragment` with each iteration of the loop. It only appends the child to the `container` element after the loop is done running. This means the DOM is updated only once instead of 1,000 times like before.

## Use the `stopPropagation` Method

The `stopPropagation` method controls the flow of events in the DOM. By default, when an event occurs on an element, it bubbles (propagates) through its ancestors.

This event propagating behaviour can sometimes lead to unintended results. The `stopPropagation` method provides a way to stop the event from propagating to the parent and other ancestors.

Let's take a situation where you have a button inside a parent div. And you want to handle a click event on the button without registering the click on the div:

```html
<div id="container">
    <button id="button">Click me</button>
</div>
```

```javascript
const containerDiv = document.getElementById('container')
const buttonElement = document.getElementById('button')

containerDiv.addEventListener('click', handleDivClick)
buttonElement.addEventListener('click', handleBtnClick)

function handleDivClick() { 
    console.log('Div clicked')
} 

function handleBtnClick(event) { 
    event.stopPropagation()
    console.log('Button clicked')
}
```

Without using the `stopPropagation` method, a click event on the button will also trigger a click event on the parent div. This means both event handlers will run.

But the `event.stopPropagation()` line in the code will prevent the `handleDivClick` function from running when a user clicks the button.

You can [run the code on Stackblitz](https://stackblitz.com/edit/js-wjmnd5?file=index.html,index.js) to see how it works. Comment out the line with the `stopPropagation` method and see the difference.

## Test Your DOM Manipulation Code

When you write tests, you create scenarios that mimic user interactions or application states. You also verify that your application gives you the expected outcomes.

Testing your DOM manipulation code is a best practice because it will make your code reliable and easy to maintain. It also gives you confidence that your code behaves as expected, even as it evolves over time when you make changes and add features.

You can use testing frameworks and libraries available for JavaScript, such as Jest, Mocha, Jasmine, and others to automate testing your apps.

The following example uses the Jest framework to test DOM Manipulation code for adding a class to an element.

```javascript
test('Adding a highlight class changes text color to red', () => {
    myElement.classList.add('highlight');
    expect(getComputedStyle(myElement).color).toBe('red');
});
```

Adding the `highlight` class is expected to change the text color to red. If the test passes, it means your DOM manipulation code works as expected. If not, you will need to figure out what figure out what's wrong and fix the issue.

## Conclusion

In this article you've learned ten best practices to keep in mind when working with the DOM. Some of them are general while others are situation specific. By using these best practices in your workflow, you will be building your web applications with a code base that is easy to maintain.

If you want to dive deep into DOM manipulation, [I wrote a whole handbook](https://www.freecodecamp.org/news/the-javascript-dom-manipulation-handbook/) that covers the subject in depth.

Thanks for reading. And happy coding! For more in-depth tutorials, feel free to [subscribe to my YouTube channel](https://www.youtube.com/@DevAfterHours)
