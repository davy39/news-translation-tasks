---
title: How to create a Buttons UI Kit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T17:27:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-buttons-ui-kit-fdd354ee0815
coverImage: https://cdn-media-1.freecodecamp.org/images/0*eUqmaII3aMOcV9hw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Florin Pop

  The theme for week #6 of the Weekly Coding Challenge is:

  Buttons

  “A button? ?” you might ask… Yes! A button! ?

  “But why?”

  Because a button is one of the building blocks of any website/web application. Whether
  you are on Facebook or Twit...'
---

By Florin Pop

The **theme** for week #6 of the [Weekly Coding Challenge](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) is:

### Buttons

“A button? ?” you might ask… Yes! A button! ?

“But why?”

Because a button is one of the building blocks of any website/web application. Whether you are on Facebook or Twitter or Google, etc, you’ll always find a button that allows you to interact with the application in some way. So this week we’re going to build buttons — lots of buttons!

If you want to participate in the Challenge, feel free to build any kind of buttons: **3D buttons**, buttons with **ripple effect**, **animating** buttons, etc — the sky is the limit ?. B**e creative!** You know how much I value creativity! ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*2aQjTjjd0_RMJpFR.gif)

In this article we are going to build multiple buttons and put all of them in a [Buttons UI Kit](https://codepen.io/FlorinPop17/full/MRbOMJ):

Before we move to the implementation part, let’s see the different states in which a button can be:

1. **Default** state
2. **Hover** state — when the mouse is over the button
3. **Active** state — when the button is pressed
4. **Focus** state — when the button is highlighted. Allowed on elements that accept keyboard events. This is used to give users that only use the keyboard some guidance as they traverse the application.
5. **Disabled** state

We need to style the buttons to cover all these states.

Also, we’ll have three different button types: `primary`, `secondary` and `tertiary` and two extra sizes: `large` and `small`.

### The HTML

```html
<div>
    <h4>Primary</h4>
    <button class="btn btn-primary">Default</button>
    <button class="btn btn-primary btn-hover">Hover</button>
    <button class="btn btn-primary" disabled>Disabled</button>
    <button class="btn btn-primary btn-large">Large</button>
    <button class="btn btn-primary btn-small">Small</button>

    <h4>Secondary</h4>
    <button class="btn btn-secondary">Default</button>
    <button class="btn btn-secondary btn-hover">Hover</button>
    <button class="btn btn-secondary" disabled>Disabled</button>
    <button class="btn btn-secondary btn-large">Large</button>
    <button class="btn btn-secondary btn-small">Small</button>

    <h4>Tertiary</h4>
    <button class="btn btn-tertiary">Default</button>
    <button class="btn btn-tertiary btn-hover">Hover</button>
    <button class="btn btn-tertiary" disabled>Disabled</button>
    <button class="btn btn-tertiary btn-large">Large</button>
    <button class="btn btn-tertiary btn-small">Small</button>
</div>
```

We are using classes to differentiate between the different types of buttons.

### The CSS

`.btn` is the main class used by all of our buttons:

```css
.btn {
    border-radius: 2px;
    border: 1px solid;
    color: #ffffff;
    cursor: pointer;
    font-family: 'Open Sans', sans-serif;
    font-size: 14px;
    padding: 8px 24px;
}
```

☝️ Some general styling to make it look better than the default version. ?

Next, we have the different states:

```css
.btn-hover,
.btn:hover {
    opacity: 0.9;
}

.btn:disabled {
    background-color: transparent;
    cursor: not-allowed;
    opacity: 0.7;
}

.btn:active {
    opacity: 1;
}

.btn:focus {
    outline: 0;
}
```

In order to have some difference between the states, we can play with the `opacity` property.

Initially the button has `opacity: 1` and we reduce that `opacity` slightly when we hover over the button and then a little more when the button is `disabled`. When we click on the button though, we'll set the opacity back to 1 as it gives a nice effect.

For the `focus` state, we remove the default `outline` property and we'll add a `box-shadow` property instead, but we'll do this separately for each button type because the color is changing depending on the class (see below).

The individual colors are set to the `.btn-primary`, `.btn-secondary` and `.btn-tertiary` classes:

```css
.btn-primary {
    border-color: var(--primary-color);
    background-color: var(--primary-color);
}

.btn-primary:disabled {
    color: var(--primary-color);
}

.btn-primary:focus {
    box-shadow: 0 0 5px var(--primary-color);
}

.btn-secondary {
    border-color: var(--secondary-color);
    background-color: var(--secondary-color);
}

.btn-secondary:disabled {
    color: var(--secondary-color);
}

.btn-secondary:focus {
    box-shadow: 0 0 5px var(--secondary-color);
}

.btn-tertiary {
    border-color: var(--tertiary-color);
    background-color: var(--tertiary-color);
}

.btn-tertiary:disabled {
    color: var(--tertiary-color);
}

.btn-tertiary:focus {
    box-shadow: 0 0 5px var(--tertiary-color);
}
```

As you can see we use the [CSS variables](https://www.w3schools.com/css/css3_variables.asp) method to set the same color on different properties. But for this to work, we need to declare the color variables on `:root` as follows:

```css
:root {
    --primary-color: #3457dc;
    --secondary-color: #ea4d67;
    --tertiary-color: #ea674d;
}
```

Note that it’s good practice to add the `:root` declaration in the top of the css file.

Lastly, let’s add the two extra sizes; `.btn-large` and `.btn-small` classes:

```css
.btn-large {
    font-size: 16px;
    padding: 12px 36px;
}

.btn-small {
    font-size: 12px;
    padding: 4px 12px;
}
```

### Conclusion

See how easy it is to create a _Buttons UI Kit_? ?

As a **bonus features** you can add a `ripple effect` to the buttons via **JavaScript**. I did this in a previous article - you can check it out by clicking [here](https://www.florin-pop.com/blog/2017/09/button-ripple-effect)!

I hope you liked this challenge and I can’t wait to see what you’re going to create!

Happy Coding! ?

_Originally published at [www.florin-pop.com](https://www.florin-pop.com/blog/2019/04/buttons-ui-kit/)._

