---
title: HTML Roving tabindex Attribute Explained with Examples
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-06-14T20:15:00.000Z'
originalURL: https://freecodecamp.org/news/html-roving-tabindex-attribute-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/photo-1578401058525-35aaec0b4658--1-.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: 'Have you ever used the CSS order or direction properties? You''ve probably
  used them dozens of times, but did you realize that these properties will cause
  a disconnect between what''s being displayed and what''s actually in the DOM?


  Using the order pro...'
---

Have you ever used the CSS `order` or `direction` properties? You've probably used them dozens of times, but did you realize that these properties will cause a disconnect between what's being displayed and what's actually in the DOM?

> Using the order property will create a disconnect between the visual presentation of content and DOM order. – MDN docs

While I was recreating the "Twitter Customize Theme UI", I came across this odd inconsistency when I changed the direction of an element using `dir="rtl`.

This happened because the element only changes the direction visually, while the HTML remains the same. This caused my keyboard navigation to begin from the back.

%[https://youtu.be/sAC387rF7aA] 

We can fix this odd disconnection with `tabindex`. But using `tabindex` with a value other than `0` is highly discouraged and frowned upon by many developers (including me).

So we'll fix this using a technique called **Roving tabindex**. But before we look at this technique, let's first refresh our memories on what the `tabindex` HTML attribute does.

### HTML Tabindex Attribute

You use the HTML `tabindex` attribute to set an element's tab position, and it usually indicates that an element can be tabbed with the `Tab` key.

`tabindex` only accepts integers as value from `0` to `32767`. If you don't specify a value it takes the default value of `0`.

`tabindex="0"` will put any element in the natural tab order:

`<span tabindex="0"> Now I'm in the natural tab order <span>`

`tabindex="-1"` will remove an element from the natural tab order:

`<button tabindex="0"> I'm no longer part of the natural tab order </button>`

A `tabindex` greater than `0` will move an element to the front of the natural tab order.

If you are not familiar with the `tabindex` attribute you can read more about it [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex).

## What is a Roving Tabindex?

Now that we have looked at `tabindex`, what is the roving tabindex technique?

A roving tabindex basically sets the `tabindex` to `-1` for all children of the element except the currently focused one.

```html
<div class"btns js-btns"> 
    <button tabindex="0"> currently focused </button> 
    <button tabindex="-1"> next button </button> 
    ... 
</div>
```

Then using an `EventListener` we can determine which button currently has focus. When the event fires, set the formerly focused button `tabindex` to `-1`, then set the next child's (to be focused) `tabindex` to `0` and call the `focus()` method on it. Do this repeatedly until you get to the last one.

Here is a more detailed guide on the [**roving tabindex**](https://developers.google.com/web/fundamentals/accessibility/focus/using-tabindex) [**method**](https://developers.google.com/web/fundamentals/accessibility/focus/using-tabindex)**.**

### How to Use the Roving Tab Index

Let's apply this method to the strange disconnected behavior we get when we use the `dir="rtl"` attribute in HTML.

We use the `dir="rtl"` attribute to reverse (visually) the `order` of the HTML code below (which is equivalent to using the `direction` property in CSS).

If you are unsure or unfamiliar with the `dir` attribute in HTML you can [read more about it here](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir).

```html
<div class="btns js-btns" dir="rtl"> 
    <button="btn js-btn" aria-label="button name"> button </button> 
    <button="btn js-btn" aria-label="button name"> button </button> 
    <button="btn js-btn" aria-label="button name"> button </button> 
    <button="btn js-btn" aria-label="button name"> button </button> 
    <button="btn js-btn" aria-label="button name"> button </button> 
</div>
```

First we add the `tabindex` attribute to all the buttons and set its value to `-1`:

```js
let btns = document.querySelectorAll("button"); 
btns.forEach((btn, index) => { 
// set first button tabindex to 0 
// and set every other button tabindex to -1 
if (index == btns.length - 1) { 
btn.setAttribute("tabindex", 0); 
} else { 
btn.setAttribute("tabindex", -1); 
}
```

Notice how we set the last item `tabindex` to `0` first (`if (index == btns.length - 1)`). Visually that's the first element a user sees, because of the `dir="rtl"` attribute we set on the HTML:

```html
<div class="btns js-btns" dir="rtl"> 
    //buttons 
</div>
```

We then add an `EventListener` where we set the `tabindex` of the currently focused button to `-1`. We keep setting the next child's `tabindex` to `0` repeatedly until it gets to the last one. Then it moves the focus back to the first and vice versa.

```js
// add an event listener when tab key is pressed 
btn.addEventListener("keydown", (e) => { 
if (e.keyCode == 9) { 
// prevent the default behaviour 
e.preventDefault(); 
// set current button tabindex to 0 
btn.setAttribute("tabindex", -1); 
// if not last button keep setting tabindex to 0 
if (btn.previousElementSibling != null) { 
let nextEl = btn.previousElementSibling; 
nextEl.setAttribute("tabindex", 0); 
nextEl.focus(); 
} else { 
// when we get to last element set first element to tabindex 0 
// and call focus method on it. 
// note the .lastElementChild the last element becomes our first 
// that's because of the direction we changed 
let firstEl = document.querySelector(".js-btns").lastElementChild; firstEl.setAttribute("tabindex", 0); firstEl.focus(); 
} 
} 
});
});
```

And after all that, the code now looks like this:‌

```js
let btns = document.querySelectorAll("button"); 
btns.forEach((btn, index) => { 
// set first button tabindex to 0 
// and set every other button tabindex to -1 
if (index == btns.length - 1) { 
btn.setAttribute("tabindex", 0); 
} else { 
btn.setAttribute("tabindex", -1); 
} 
// add an event listener when tab key is pressed 
btn.addEventListener("keydown", (e) => { 
if (e.keyCode == 9) { 
// prevent the default behaviour 
e.preventDefault(); 
// set current button tabindex to 0 
btn.setAttribute("tabindex", -1); 
// if not last button keep setting tabindex to 0 
if (btn.previousElementSibling != null) { 
let nextEl = btn.previousElementSibling; 
nextEl.setAttribute("tabindex", 0); 
nextEl.focus(); 
} else { 
// when we get to last element set first element to tabindex 0 
// and call focus method on it. 
// note the .lastElementChild the last element becomes our first 
// that's because of the direction we changed 
let firstEl = document.querySelector(".js-btns").lastElementChild; firstEl.setAttribute("tabindex", 0); 
firstEl.focus(); 
} 
} 
});
}); 
```

Here is a working version of this on Codepen (try navigating using your keyboard). You can also view the live demo of the completed Twitter Customize UI at [Spruce.com.ng](http://Spruce.com.ng) by clicking on the theme button.

%[https://codepen.io/Spruce_khalifa/pen/BaQemGw] 

‌

But hold on a sec – before you decide to use this technique, remember that almost every design implementation comes with a cost. So let's look at the pros and cons of using the roving tabindex technique:

### Pros of roving tabindex:‌

1. Improves keyboard navigation experience problems
    
2. Fixes the order disconnect problem caused by the direction change‌
    

### Cons of roving tabindex:

1. Solely depends on JavaScript – if the user turns off JavaScript for whatever reason, keyboard navigation would create an odd experience again.
    
2. No support for assistive technology users‌
    

## Conclusion

There is no particular or preferred way to implement the roving tabindex technique. So however you decide to write and implement your code is perfectly fine, as long as you follow these procedures:

1. Set all the elements' `tabindex`s to `-1` except the first one
    
2. Add a keyboard event listener to determine which element is focused
    
3. Set the previously focused child `tabindex` to `-1`
    
4. Then set the next child `tabindex` to `0`
    
5. Call the `focus()` method on it
    

If you found this tutorial useful, please follow me on twitter [@sprucekhalifa](https://twitter.com/sprucekhalifa).
