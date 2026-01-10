---
title: The Difference Between Pseudo-Classes and Pseudo-Elements in CSS
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2023-04-21T17:34:29.000Z'
originalURL: https://freecodecamp.org/news/the-difference-between-pseudo-classes-and-elements-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pseudo-1.png
tags:
- name: CSS
  slug: css
seo_title: null
seo_desc: "In CSS, pseudo-classes and pseudo-elements are two types of keywords that\
  \ you can combine with selectors. They are used to target the element's state or\
  \ specific parts of an element. \nIn this article, we'll explore the differences\
  \ between the two alo..."
---

In CSS, pseudo-classes and pseudo-elements are two types of keywords that you can combine with selectors. They are used to target the element's state or specific parts of an element. 

In this article, we'll explore the differences between the two along with their history and best practices.

###### Syntax

* The single colon `:` refers to pseudo-classes
* The double colon `::` refers to pseudo-elements

## Pseudo-Classes vs Pseudo-Elements

[Pseudo](https://www.dictionary.com/browse/pseudo#:~:text=2%20of%202)-,pseudo%2D,names%20of%20isomers%20(pseudoephedrine).) itself means false, unreal, or fake. The prefix `pseudo-`, is used to reference classes or elements that are not "real". Not real in this context means not a DOM (Document Object Model) element, but instead a virtual element created for styling purposes. 

To form a better definition, let's discuss the difference between pseudo-classes and pseudo-elements in greater detail.

### What are Pseudo-Classes in CSS?

Pseudo-classes (`:`) are primarily used to style an element that's under various states. When referring to state, this includes the condition or user behavior, for example hover, active, focus, or disabled. States generally involve user interaction.

For example, we can target all links to have a text color of lavender when the user hovers over the link.

```css
a:hover {
  color: lavender;
}

```

Inspect the Chrome DevTools and you will find other examples of state. Here you can also test out and debug applied styles based on the state (and the related pseudo-class used) by toggling them on and off. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-10.13.42-AM.png)

There are over [50 types of pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes#alphabetical_index), so I highly suggest looking over all of the possibilities.

Test out the code example below, inspect the pseudo-classes, and try to add a new one. 

%[https://codepen.io/nataliepina/pen/xxyRWYm]

#### Functional Pseudo-Classes

Another variation of the pseudo-class type is the functional pseudo-class. These function calls take in a parameter of a [selector-list](https://developer.mozilla.org/en-US/docs/Web/CSS/Selector_list#selector_list) to match elements. 

Unlike other types of pseudo-classes that target static state such as hover, these can dynamically target events and user interactions.

```css
:is()
/* The matches-any pseudo-class matches any element that matches any of
the selectors in the list provided. */

:not()
/* The negation, or matches-none, pseudo-class represents any element 
that is not represented by its argument. */

:where()
/* The specificity-adjustment pseudo-class matches any element that
matches any of the selectors in the list provided without adding any 
specificity weight. */

:has()
/* The relational pseudo-class represents an element if any of the 
relative selectors match when anchored against the attached element. */
```

### What are Pseudo-Elements in CSS?

Pseudo-elements (`::`) are used to style specified parts of an element. They can be used to target the first letter or first line. Or they can be used to insert content before or after the element. 

It's worth getting familiar with this [index of pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements#alphabetical_index) to learn more about the available keywords.

As an example, to create a large first letter of a paragraph, you can do that using `first-letter` like this:

```css
p::first-letter {
  font-size: 9em;
}
```

Another common example of a pseudo-element is to use `::before` or `::after` to insert content before or after the targeted element.

Test out the code example below to see how you can use `::before` and `::after` to create lines before and after a text element.

%[https://codepen.io/nataliepina/pen/qBJqpgq]

## The Difference between `:` and `::` in CSS

As a takeaway, remember that there is a key difference between a single and double colon. Most importantly that `:` refers to pseudo-classes and `::` refers to pseudo-elements.

### History of the `::` 

Historically, there was only a single colon `:`  to both define pseudo-classes and pseudo-elements. The `::` notation was introduced with CSS3 as a way to differentiate the two.

Pseudo-elements and pseudo-classes are related concepts that provide different ways to style an element. As a result, the slight variation in syntax between them is logical.

Using only the single colon syntax is not recommended for both, as it has become deprecated. Browsers will still accept `:` for both currently, for backwards compatibility reasons. Since it's possible to encounter either syntax, understanding the historical context around this is beneficial.

## Best Practices for using `:` vs `::`

The best practice when choosing which colon syntax to use is to stick with current standards of CSS3. Following these standards will improve the maintainability of your codebase, so it's helpful to keep and enforce guidelines around this for your codebase.

It will also help to future-proof your CSS. As we discussed, browsers currently accept the single colon syntax for both, but that may not always be the case. By using the double-colon syntax for pseudo-elements, you can help prevent errors and bugs in the future as CSS continues to change and evolve.

The syntax distinction between the two offers readability improvements. This clarifies what you are targeting, and is helpful when dealing with intricate selectors that involve multiple pseudo-elements and pseudo-classes together.

## Wrapping Up

Understanding the difference between a pseudo-class and a pseudo-element is essential for writing maintainable CSS. Pseudo-classes are used to target state. Pseudo-elements are used to target specific parts of an element.

I hope this article helped to understand the differences between pseudo-classes and pseudo-elements, along with the history, and best practices when using them. 

Happy styling! 

If you want to learn more about CSS, you can find me on [Twitter](https://twitter.com/ui_natalie). 








