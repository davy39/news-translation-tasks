---
title: CSS display:none and visibility:hidden – What's the Difference?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-15T23:13:53.000Z'
originalURL: https://freecodecamp.org/news/css-display-none-and-visibility-hidden-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/11.-display-visibility-2.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  display:none and visibility:hidden are two style declarations you can use to hide
  elements on the screen with CSS. But what are the differences between them?

  When building applications, there are times that you want to hide elements...'
---

By Dillion Megida

`display:none` and `visibility:hidden` are two style declarations you can use to hide elements on the screen with CSS. But what are the differences between them?

When building applications, there are times that you want to hide elements visually (not deleting them from the DOM, just the screen). You can do this in different ways. 

Two common approaches include using the `display` property with a **none** value or the `visibility` property with a **hidden** value.

Although both approaches hide the element visually, they cause the element to behave in different ways. I'll explain these differences in this article.

Here is [the video version](https://youtu.be/nMq3U65wAdQ) of this article if you're interested.

Here's the example I'll use to explain how this all works:

The HTML:

```html
<div class="container">
  <div class="block1"></div>
  <div class="block2"></div>
  <div class="block3"></div>
</div>
```

And the CSS:

```css
.container {
  padding: 20px;
  width: max-content;
  display: flex;
  border: 1px solid black;
}

.block1,
.block2,
.block3 {
  height: 40px;
  width: 120px;
}

.block1 {
  background-color: rgb(224, 110, 49);
  margin-right: 20px;
}

.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
}

.block3 {
  background-color: rgb(12, 154, 142);
}
```

We have a `div` with a class of **container**. This `div` has three children `div`s with classes of **block1**, **block2** and **block3**, respectively. We've specified some styles for the `divs`. The first `div` child is orange, the second is `blue`, and the third is `teal`.

Here's the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-77.png)

## How to Use `display: none` in CSS

The `display` property sets how an element is displayed (as **inline** or **block**) and also determines the layout of the children of an element (as **flex**, **grid**, and so on).

With a **none** value for this property, the display for the element is turned off. This means the element – as well as its children – will not be displayed. The document is rendered without the element **like it did not exist**.

Now let's see how `display: none` works. Here is an example with this style applied to the **.block2** element:

```css
.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  display: none;
}
```

Here's the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-78.png)

As you can see here, the **.container** element has reduced in width. It's just like the **.block2** element does not exist. Because we used `display:none` on this element, it is not rendered in the document. So its space on the screen becomes vacant for other elements to occupy.

We can also test this by moving adding `display:none` to the **.block1** element:

```css
.block1 {
  background-color: rgb(224, 110, 49);
  margin-right: 20px;
  display: none;
}

.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  display: none;
}
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-79.png)

Here you see that **.block1** and **.block2** are not rendered, so their spaces are occupied.

## How to Use `visibility: hidden` in CSS

The `visibility` property, as the name implies, specifies whether an element is visible or not. But, this property does not affect the element's layout. This is the major difference when compared to the `layout` property.

With a **hidden** value for this property, the element it is applied to becomes "invisible". The space required by the element's [box model](https://youtu.be/opHpcJIUbEU) stays but the element itself is hidden.

Let's see how this property applies to our example above. Here is the result of this style applied to the **.block2** element:

```css
.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  visibility: hidden;
}
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-80.png)

As you'll notice here, unlike `display: none`, the **.block2** element is invisible, but its layout stays intact. In fact, the `margin-right` on this element is still there. Only the element itself is hidden.

Let's also add this style to **.block1** to see the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-81.png)

Now both elements are invisible, but they are still rendered in the document so their space is not vacant.

The next thing you may be thinking is that "what is the difference between `visibility: hidden` and `opacity: 0`?"

## `visibility: hidden` vs `opacity: 0`

Both styles look very similar. I can show you this by replacing `visibility:hidden` with `opacity:0` in our above examples:

```css
.block1 {
  background-color: rgb(224, 110, 49);
  margin-right: 20px;
  opacity: 0;
}

.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  opacity: 0;
}
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-82.png)

You can see that there's no difference visually between this result and the previous one. But there is a difference in the behavior of the elements.

Elements with `visibility: hidden` are **non-interactable**. I don't know if this is the best word for this 😂 but what I mean is that users cannot interact (for example, by clicking) with such elements. That's because such elements are indeed invisible.

Elements with `opacity: 0` on the other hand are **interactable** as they are actually visible, just very transparent. The `opacity` property doesn't specify the visibility of an element – it only specifies transparency.

We can verify this difference with an example. Let's say the **.block2** element had an `onclick` attribute like this:

```html
<div class="block2" onclick="alert('hello')"></div>
```

If you use `visibility:hidden` on this element, clicking on the space where the element is will trigger nothing. But if you use `opacity:0` on this element, clicking on that same space will trigger the alert modal showing the "hello" text. You can test this on your browser to see this live.

## Use Cases for `display:none` and `visibility:hidden`

These style declarations can serve different purposes depending on what you want to achieve.

In my experience, I use `display:none` when I want to hide anything. Think of hiding a popup, a todo list item on the UI that has been checked, or the sidebar in a page. 

Using `visibility:hidden` for these things causes their space to be retained, and it could make a page look odd when there's a blank space.

The only times I use `visibility:hidden` is when I want to display some animation while I "hide" or "show" an element. The `display` property does not animate between values but the `visibility` property can. I use `visibility` in combination with `opacity` for such fade in and fade out animations.

## Wrap up

In summary, `display:none`, `visibility:hidden`, and `opacity:0` can be used to hide elements visually but:

* `display:none` turns off the layout of the elements, so they are not rendered
* `visibility:hidden` hides the elements without changing their layouts
* `opacity:0` causes the elements to be very transparent but users can still interact with them.

If you enjoyed this article, please share it with others to learn 😇


