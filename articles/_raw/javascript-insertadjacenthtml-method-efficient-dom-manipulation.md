---
title: How to Use the JavaScript insertAdjacentHTML() method for Efficient DOM Manipulation
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2024-02-07T16:28:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-insertadjacenthtml-method-efficient-dom-manipulation
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/The-JavaScript-insertAdjacentHTML---Method.png
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, developers need to be able to dynamically update a page
  without replacing the entire content. A traditional method like innerHTML can cause
  performance issues, because these methods tend to replace the entire content of
  an element.

  The...'
---

In JavaScript, developers need to be able to dynamically update a page without replacing the entire content. A traditional method like `innerHTML` can cause performance issues, because these methods tend to replace the entire content of an element.

The `insertAdjacentHTML()` method leads to better performance because you use it to dynamically insert new HTML content without affecting the existing content.

In this tutorial, we'll cover the following:

* [Introduction to the `insertAdjacentHTML()` method](#heading-introduction-to-the-insertadjacenthtml-method)
* [Syntax of the `insertAdjacentHTML()` method](#heading-syntax-of-the-insertadjacenthtml-method)
* [Placement options in the](#placement-options-in-insertadjacenthtml-method) [`insertAdjacentHTML()` method](#placement-options-in-insertadjacenthtml-method)
* [Browser support for the `insertAdjacentHTML()` method](#browser-support-for-the-inneradjacenthtml-method)
* [Best Practices for using the](#best-practices-for-using-theinsertadjacenthtml-method) [`insertAdjacentHTML()` method](#best-practices-for-using-theinsertadjacenthtml-method)
* [Conclusion](#heading-conclusion)

## Introduction to the `insertAdjacentHTML()` method

The `insertAdjacentHTML()` method provides an efficient way to manipulate web page structure without replacing all the content of an element. It's also the go-to method for inserting HTML elements or text elements into a specific position.

`insertAdjacentHTML` is a method in JavaScript that allows you to insert HTML elements or text into a specific position relative to a given element in the DOM (Document Object Model). This method provides flexibility in manipulating the structure of a web page dynamically.

## Syntax of the `insertAdjacentHTML()` method

Here's what the syntax of the `insertAdjacentHTML()` method looks like:

```javascript
HTMLelement.insertAdjacentHTML(position, element);

```

The `insertAdjacentHTML` method takes two parameters:

1. **position:** This parameter is a string representation of where the new HTML should be inserted in relation to the `targetElement`. It must match one of the following strings:

* `**"beforebegin"**`: The `beforebegin` string value of the `insertAdjacentHTML()` method inserts the HTML element immediately before the specified element in the `DOM`.
* `**"afterbegin"**`: The `afterbegin` string value of the`insertAdjacentHTML()` method inserts the HTML element inside the `targetElement`, just before its first child.
* `**"beforeend"**`: The `beforeend` is a string value of  the `insertAdjacentHTML()` method that  inserts an HTML element inside the `targetElement`, after its last child.
* `**"afterend"**`: The `afterend` string value of the `insertAdjacentHTML()` method inserts an HTML element immediately after the specified element in the `DOM`.

2.   **element:** The element to be inserted into the `DOM` tree.

## Placement Options in the `insertAdjacentHTML()` Method

Now that you've seen the four possible parameters of the `insertAdjacentHTML()` method, let's see how they work with code.

* `beforebegin`: Here's an example using the `beforebegin` parameter in code:

```javascript

const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('beforebegin', '<h2>Lawal</h2>');
```

Here's the output:

![beforebegin](https://www.freecodecamp.org/news/content/images/2024/02/beforebegin.png)
_beforebegin_

Recall that the `beforebegin` string value of the `insertAdjacentHTML()` method inserts the HTML element immediately before the specified element in the `DOM`.

In the above code result, our newly inserted HTML element `h3` got inserted before our `targetElement` `h2`. I styleed our `targetElement` by adding a border to it for easy illustration.

* `afterbegin`: here's an example of using the `afterbegin` parameter in code:

```javascript
const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('afterbegin', '<h2>Lawal</h2>');

```

And here's the output:

![afterbegin](https://www.freecodecamp.org/news/content/images/2024/02/afterbegin.png)
_afterbegin_

As defined above, the `afterbegin` string value of the `insertAdjacentHTML()` method inserts the HTML element inside the `targetElement`, just before its first child.

By checking the output of our code, you may realize that our newly inserted HTML element `h3` got inserted inside our `targetElement` `h2`. Again, I styled our `targetElement` by adding a border to it for easy illustration.

* `beforeend`: here's an example of using `beforeend` in code:

```javascript
const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('beforeend', '<h2>Lawal</h2>');
```

And here's the output:

![beforeend](https://www.freecodecamp.org/news/content/images/2024/02/beforeend.png)
_beforeend_

The general definition of `beforeend` is that it's a string value of the `insertAdjacentHTML()` method that inserts an HTML element inside the `targetElement`, after its last child.

From the code result, our newly inserted `HTML` element `h3` got inserted inside our `targetElement` `h2` after its child. I styled our `targetElement` by adding a border to it for easy illustration.

* `afterend`: here's an example of using `aferend` in code:

```javscript
const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('afterend', '<h2>Lawal</h2>');
```

And here's the output:

![afterend](https://www.freecodecamp.org/news/content/images/2024/02/afterend.png)
_afterend_

As you now know, `afterend`  is a string value of the `insertAdjacentHTML()` method that inserts an `HTML` element immediately after the specified element in the `DOM`.

In the above code, our newly inserted HTML element `h3` got inserted immediately after our `targetElement` `h2`. I styled our `targetElement` by adding a border to it for easy illustration.

## Browser Support for the `insertAdjacentHTML()` Method

The `insertAdjacentHTML()` method is a widely supported method that can be relied upon for your `DOM` manipulation needs across different modern browsers. 

To see the browsers that support this method, check out the summary below:

![browser compatibility](https://www.freecodecamp.org/news/content/images/2024/02/browser-compat.png)
_browser compatibility_

1. **Edge**: Supported across all versions.
2. **Chrome**: Supported across all versions.
3. **Opera**: Supported across all versions.
4. **Safari**: Supported across all versions, except version 3.1-3.2
5. **Firefox**: Supported across all versions, except version 2-7

## Best Practices for Using the `insertAdjacentHTML()` Method

To effectively use the `insertAdjacentHTML()` method, here are some best practices to follow:

### Understand the method

Understanding how the method works helps you specify the position to insert your HTML content. Understand the various positions and choose appropriately based on your requirements.

```javascript
// Inserting the HTML content after the target element
document.getElementById('div').insertAdjacentHTML('afterend', '<div>New content before the target element</div>');

```

### Use it sparingly

Overusing dynamic HTML element insertion methods is bad for code maintenance.

For a simple application, a direct `DOM` manipulation will do the job.

```javascript
/ Consider Using this:
let newElement = document.createElement('div');
newElement.textContent = 'New element';
element.appendChild(newElement);


// Instead of this:
element.insertAdjacentHTML('beforeend', '<div>New element</div>');
```

### Be conscious of performance

If you frequently insert large amounts of HTML content, manipulating the `DOM` can be expensive for performance. Try to minimize `DOM` updates, especially in performance scenarios:

```javascript


// Consider using batch insertion:
let section = '';
data.forEach(item => {
  section += `<div>${item}</div>`;
});
element.insertAdjacentHTML('beforeend', section);


// Instead of inserting one by one in a loop:
data.forEach(item => {
  element.insertAdjacentHTML('beforeend', `<div>${item}</div>`);
});
```

### Handling errors

When using the `insertAdjacentHTML()` method, if the HTML content you're trying to insert is invalid, the method may throw an error. Use try-catch blocks to handle these situations appropriately. 

```javascript
const div  = document.getElementById('div');

try {
    // Check if the value of div is true
    if (div.insertAdjacentHTML) {
        div.insertAdjacentHTML('beforeend', '<div>New Element</div>');
    } else {
        throw new Error('insertAdjacentHTML is not supported.');
    }
} catch (error) {
    // Handling the error
    
    console.error('Error:', error.message);
    

    // Alternate code
    div.innerHTML += '<div>Fallback: New Element</div>';
}

```

## Conclusion

In this tutorial, you learned about the syntax and placement options of the `insertAdjacentHTML()` method. We also looked at browser compatibility, and some best practices while using the `insertAdjacentHTML()` method.

