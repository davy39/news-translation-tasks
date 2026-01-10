---
title: How to Build Your First Web Component
subtitle: ''
author: Joe Attardi
co_authors: []
series: null
date: '2023-10-19T20:35:35.000Z'
originalURL: https://freecodecamp.org/news/build-your-first-web-component
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/pexels-just-another-photography-dude-68725.jpg
tags:
- name: components
  slug: components
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In 2023, browser support for web components (also known as custom elements)
  is really good. There''s never been a better time to start building your own custom
  elements.

  Web components, also known as custom elements, are new HTML elements that you cre...'
---

In 2023, browser support for web components (also known as custom elements) is really good. There's never been a better time to start building your own custom elements.

Web components, also known as custom elements, are new HTML elements that you create. These elements encapsulate some markup, style, and interactivity. 

In this article, you'll learn the basics of web components and create a very simple web component that shows the current date.

This guide is intended as a gentle introduction to the concept, so it won't cover some more advanced aspects such as templates, slots, or shadow DOM. But, these are all powerful building blocks to building components that you should learn as you ramp up your skills.

## What is a Web Component?

A web component is a custom HTML element that you define, with its own tag name. Think of it as an encapsulated, reusable piece of code. Just like regular HTML elements, web components can accept attributes and you can listen for events.

Web components are a nice way to add some extra functionality to your web app. Since it's a web standard, there's no extra third-party code needed.

A web component can be as simple or complex as you want: it can simply display some text (as the example in this article will be doing), or it can be highly interactive. 

## Web Component Basics

To define a web component, create a class that extends from `HTMLElement`. This class will contain all of your web component's behavior. After that, you need to register it with the browser by calling `customElements.define`.

```javascript
class MyComponent extends HTMLElement {
	// component implementation goes here
}

customElements.define('my-component', MyComponent);
```

Once you've done this, you can use your component by just adding a `<my-component>` element to your HTML. That's it! You've just added a web component to your page.

Note that the component name has a hyphen. This is required by the specification, to prevent name clashes with potential future standard HTML elements.

### Lifecycle callbacks

Web components have a few lifecycle callbacks. These are functions that the browser calls at different parts of the component's lifecycle. Some of these callbacks are:

* `connectedCallback`: Called when the element is first added to the DOM
* `disconnectedCallback`: Called when the element is removed from the DOM
* `attributeChangedCallback`: Called when one of the element's watched attributes change. For an attribute to be watched, you must add it to the component class's static `observedAttributes` property.

For this simple component, you'll only need the `connectedCallback`. 

## How to Create the Component

In a new JavaScript file, create the component class and add the call to `customElements.define` as shown above. Here's the first pass at the `CurrentDate` component:

```javascript
class CurrentDate extends HTMLElement {
    // The browser calls this method when the element is
    // added to the DOM.
    connectedCallback() {
        // Create a Date object representing the current date.
        const now = new Date();
        
        // Format the date to a human-friendly string, and set the
        // formatted date as the text content of this element.
        this.textContent = now.toLocaleDateString();
    }
}

// Register the CurrentDate component using the tag name <current-date>.
customElements.define('current-date', CurrentDate);
```

In the `connectedCallback`, you are getting the current date and calling `toLocaleDateString`, which formats the date portion of the `Date` object in a more human friendly format. For example, in the `en-US` locale, this would be a format like `10/18/2023`.

There are no event listeners to clean up here, so there is no need for a `disconnectedCallback`.

Since `CurrentDate` extends from `HTMLElement`, it includes all of its properties and methods. This is why you can use the `textContent` property like with any other HTML element. This will set the formatted date as the value of a text node inside the `<current-date>` element.

## How to Use the Component

Before you use the component, you need to load it using an `import` statement or a `script` tag. Here's a simple usage example using a `script` tag:

```html
<script src="./currentDate.js"></script>

<h2>Today's Date</h2>
The current date is: <current-date></current-date>
```

Note that custom elements, even when they have no child content, cannot use the self-closing tag syntax supported by some elements. They must always have an explicit closing tag.

## Future Enhancements

Here are some ways you can enhance the `CurrentDate` component:

* Use `Intl.DateTimeFormat` to create a more human-readable format for the date. You could even add attributes to customize the date format used.
* Add support for a `date` attribute and adapt the component so that it can display any arbitrary date, not just the current date. Of course, in this case, you'll want to change the name from `CurrentDate` to something else like `FormattedDate`.
* Use the HTML `time` element inside the component to produce more semantic markup

## Conclusion

In this article, you took your first step into the world of web components. 

Web components have no third party dependencies, so using them won't have a big impact on your bundle size. But for more complex components, you may want to reach for a library like Svelte or Lit.

