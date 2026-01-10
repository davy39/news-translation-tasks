---
title: How to Manipulate the DOM in JavaScript – Most Commonly Used Techniques
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-12-07T22:19:23.000Z'
originalURL: https://freecodecamp.org/news/javascript-document-object-model-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/js-dom-manipulation-1.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Hi everyone! In this article, I’m going to cover everything you need to
  know about manipulating the DOM.

  Basically, each Element object in the DOM has properties and methods that you can
  use to interact with that element.

  The following are the most c...'
---

Hi everyone! In this article, I’m going to cover everything you need to know about manipulating the DOM.

Basically, each `Element` object in the DOM has properties and methods that you can use to interact with that element.

The following are the most common and practical ways you might want to manipulate the `Element` object:

1. [Change the Content of an Element](#heading-change-the-content-of-an-element)
2. [Manipulate the Class Attribute](#heading-manipulate-the-class-attribute)
3. [Setting CSS Styles Using JavaScript](#heading-setting-css-styles-using-javascript)
4. [Create, Add, and Remove Elements](#heading-create-add-and-remove-elements)
5. [Insert Element at a Specific Position](#heading-insert-element-at-a-specific-position)
6. [Manipulating Element Attributes](#heading-manipulating-element-attributes)
7. [Manipulating Data Attributes](#heading-manipulating-data-attributes)

Manipulating the DOM seems complex in theory, but as you’ll see in this article, there are a few methods that you’ll use over and over again in many scenarios.

Once you know about these methods, you will have leveled up your skill in DOM manipulation. Let’s begin!

## Change the Content of an Element

You can change the value or content of an element by setting the `innerText` property of that element.

For example, suppose you have a paragraph element as follows:

```html
<p class="myParagraph">This is a paragraph</p>

```

Next, you select the element and change its `innerText` value like this:

```js
const p = document.querySelector('.myParagraph');

p.innerText = 'A new day is dawning';

```

The `p` element would have its value changed as you see below:

```html
<p class="myParagraph">A new day is dawning</p>

```

And that’s how you change the value of an element.

## Manipulate the Class Attribute

You can add a new `class` attribute to an `Element` by using the `add()` method of the `classList` object:

```js
Element.classList.add('myClass');

```

You can remove a class using the `remove()` method:

```js
Element.classList.remove('myClass');

```

The `classList` object is a collection object that you can use to manipulate the `class` attribute of an `Element`.

You can’t directly edit the `classList` property because it’s a read-only property. But you can use its methods to change the element classes.

To replace an existing class with a new class, use the `replace()` method:

```js
Element.classList.replace('oldClass', 'newClass');

```

There’s also the `toggle()` method, which works like a switch: adds a class if it’s not there, removes a class if it’s there.

```js
Element.classList.toggle('myClass');

```

To check if an element contains a specific class, use the `contains()` method and pass the class you want to check as a string:

```js
Element.classList.contains('myClass');

```

The method returns `true` when the class is specified. Otherwise it returns `false`.

## Setting CSS Styles Using JavaScript

Since you’ve learned how to set and remove classes from an element, you can control the style of an element by adding or removing classes that change the style rules applied to an element.

For example, you might have the following style rules in your CSS code:

```css
.color-primary {
  color: #007bff;
}

.color-secondary {
  color: #6c757d;
}

.bold {
  font-weight: 700;
}

```

If you have an element with the `color-primary` class applied, you can replace it with `color-secondary` class, or add the `bold` class. 

Suppose you have a paragraph element as follows:

```html
<p class="myParagraph">A new day is dawning</p>

```

Here’s how you change the style using classes:

```js
const p = document.querySelector('.myParagraph');

// add a class to the element
p.classList.add('color-primary');

// replace a class
p.classList.replace('color-primary', 'color-secondary');

// remove a class
p.classList.remove('color-secondary');

```

At times, you might need to apply CSS directly to the DOM element you selected.

The `Element` object provides you with the `style` property which controls the inline style of the element.

For example, you can change the font weight of an element using the `Element.style.fontWeight` property like this:

```js
const p = document.querySelector('.myParagraph');

p.style.fontWeight = '700'; // set font weight
p.style.textTransform = 'uppercase'; // set to uppercase
p.style.color = '#007bff'; // set color

```

You can change the border style of an element as follows:

```js
p.style.border = '1px solid black';

```

The `style` property uses the camelCase instead of the hyphen-case, so `font-weight` becomes `fontWeight` and `text-transform` becomes `textTransform`.

And now you know how to set CSS styles using JavaScript. I would recommend that you change element styles by adding and removing classes because it’s more maintainable and follows the common approach.

Only access the `style` property if you won’t use the same style anywhere else.

## Create, Add, and Remove Elements

Besides creating a DOM tree out of your HTML file, you also have the ability to create DOM elements programmatically using JavaScript.

This is possible because the `document` object also has the `createElement()` method, which allows you to create any `Element` object, which is essentially the tags you write in your HTML file.

For example, you can create a paragraph element like this:

```js
const p = document.createElement('p');

```

After you create that element, you can add some content to it using the `innerText` property:

```js
p.innerText = 'This paragraph is created using JavaScript';

```

Now you need to add it to the existing DOM tree so that it appears on the screen. You can attach the element anywhere inside your existing tree structure.

Suppose you want to add the paragraph to the `body` tag. Then you need to use the `querySelector()` method to select the `body`, and call the `append()` method on the element:

```js
const p = document.createElement('p');

p.innerText = 'This paragraph is created using JavaScript';

const body = document.querySelector('body');

body.append(p);

```

The paragraph will be added as a child of the `body` tag as follows:

```html
<body>
<p>This paragraph is created using JavaScript</p>
</body>

```

If you want to remove an element, you can call the `remove()` method from the element you want to remove.

This code will remove the paragraph element:

```js
p.remove();

```

## Insert Element at a Specific Position

The `append()` method that we explored above will insert a new element as the last child of the parent element.

If you want to insert the element at a specific position, you can use the `insertBefore()` method.

Let’s see an easy example. Suppose you have an HTML content as follows:

```html
<body>
    <p id="first">The first paragraph</p>
</body>

```

To insert an element before the first paragraph, you need to call the `insertBefore()` method from the parent element (which is the `body` tag) and pass two arguments to it:

1. The new element you want to add
2. The sibling element before which the new element is inserted

Here’s an example of creating a second paragraph and inserting it before the first paragraph:

```js
let p2 = document.createElement('p');

p2.innerText = 'The second paragraph';

let body = document.querySelector('body');
let p1 = document.querySelector('#first');

body.insertBefore(p2, p1);

```

As a result of running the script above, the second paragraph will be inserted before the first paragraph:

```html
<body>
    <p>The second paragraph</p>
    <p id="first">The first paragraph</p>
</body>

```

Keep in mind that the DOM doesn’t provide an `insertAfter` method, because it’s not needed.

You use the `append()` method to insert an element at the last position, and if you want to control the position, use the `insertBefore()` method.

## Manipulating Element Attributes

The `classList` object only provide methods to change the `class` of an element. If you want to change other attributes like `id`, `href`, or `src`, you can use the `setAttribute()` method.

The `setAttribute()` method accepts two arguments:

1. The name of the attribute to set
2. The value of the attribute to set

For example, here’s how to set the `src` attribute of an `img` tag:

```html
<img id="profile-pic" src="feature-image.png" />

```

Select the `img` element using `querySelector()`, then call the `setAttribute()` method on the element:

```js
const img = document.querySelector('#profile-pic');

img.setAttribute('src', 'new-image.jpg');

```

The `src` attribute value would be changed as follows:

```html
<img id="profile-pic" src="new-image.jpg" />

```

If you want to the an attribute’s value, you can use the `getAttribute()` method.

Pass the attribute you want to check as an argument to the method. If the attribute is set, the method returns the value of that attribute as a string. If not, it returns `null`:

```js
img.getAttribute('src'); // new-image.jpg
img.getAttribute('href'); // null

```

You can use both `setAttribute()` and `getAttribute()` methods to interact with any HTML attributes.

If you want to delete an attribute, use the `removeAttribute()` method:

```js
const img = document.querySelector('#profile-pic');

// Delete the src attribute
img.removeAttribute('src');

```

## Manipulating Data Attributes

The data attribute is used to store extra information on HTML elements. How you use the data is up to you.

Suppose you have an HTML tag as follows:

```html
<div id="intro" data-attribute-theme="light" data-session="2022">
  Hello World!
</div>

```

You can access the data attributes from the `dataset` property of the element above like this:

```js
// Select the div
let myDiv = document.querySelector('#intro');

// Access the dataset property
console.log(myDiv.dataset.session) // 2022

// Use camelCase when your data attribute is more than one word
console.log(myDiv.dataset.attributeTheme) // light

```

If you want to change the attribute value, you can reassign the right `dataset` property to a new value directly:

```js
// Select the div
let myDiv = document.querySelector('#intro');

// Change the value of a data attribute
myDiv.dataset.session = '2023'

```

If you want to delete the data attribute, use the `removeAttribute()` method similar to how you delete a regular attribute:

```js
let myDiv = document.querySelector('#intro');

// Remove data-session attribute
myDiv.removeAttribute('data-session');

// Remove data-attribute-theme attribute
myDiv.removeAttribute('data-attribute-theme');

```

And that’s how you manipulate the data attribute using JavaScript.

## Conclusion

And that's all for now about DOM element manipulations. At this point, I hope you can see why JavaScript is required to build a modern web application. It allows you to interact and change the content that exists in your website.

This enables a whole lot of dynamic changes to the website you created.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!


