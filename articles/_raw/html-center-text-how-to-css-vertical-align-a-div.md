---
title: HTML Center Text – How to CSS Vertical Align a Div
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-12T17:53:52.000Z'
originalURL: https://freecodecamp.org/news/html-center-text-how-to-css-vertical-align-a-div
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/align-div-vertically-in-css-1.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
seo_title: null
seo_desc: 'By Said Hayani

  In the HTML and CSS world, it''s all about the layout structure and the distribution
  of elements. We usually use HTML to define the markup and structure, while CSS helps
  us handle the styling and alignment of elements.

  In this post we a...'
---

By Said Hayani

In the HTML and CSS world, it's all about the layout structure and the distribution of elements. We usually use HTML to define the markup and structure, while CSS helps us handle the styling and alignment of elements.

In this post we are going to learn a little bit about the different ways we can center HTML elements and handle vertical alignment with CSS.

First we going to learn how to align text with CSS.

Next, we will cover how to align a div and any other elements.

And finally we will learn how we can put text and a `div` together within a container.

## How to center text 

There are many way to center text using CSS.

### Using the Float property

Float is an easy way to align text.

To place the text on the right side of the layout, we can simply use `right`  as a value for `float`.

To place the text on the left side, we use `left`, like `float:left`. Look at the example below:

```html
  .right {
        float: right;
      }
     
      .left {
        float: left;
      }
// HTML

    <span class="right">Right</span>
    <span class="left">Left</span>
```

%[https://codesandbox.io/s/center-html-elements-dlhfu?file=/index.html]

To center the text using float we can use `margin-left` or `margin-right` and make it  `50%`, like below.

```css
    .center {
    float: left;
    margin-left: 50%;
    }

/* HTML*/
<span class="center">Center</span>
```

You can learn more about the uses of `Float` [here](https://developer.mozilla.org/en-US/docs/Web/CSS/float).

### Using Text-align

`text-align` is a more convenient and more specific way to align text. It allows us to place the text at the `center` or to the `left` or `right` side, as the following example shows:

```css
.right {
text-align: right;
}

.left {
text-align: left;
}
.center {
text-align: center;
}
/* HTML */

<p class="right">Right</p>
<p class="center">Center</p>
<p class="left">Left</p>
```

%[https://codesandbox.io/s/text-align-71d6q?file=/index.html]

Learn more about `[text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)`.

## How to align a `div` 

Well, there are a plenty of ways to do that.

The same way we use `Float` to align text, we can use it to align a `div` element as well.

%[https://codesandbox.io/s/align-a-div-pn8yw?file=/index.html]

`Float` does the job, but CSS gives us better options that are more convenient and elegant. Have you heard of `Flexbox`? Or [css-grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)? 

Well, these two methods provide very modern ways to align and work with your layout in CSS. Let's look at Flexbox in more in detail.

## [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)   

Flexbox offers an easy and straightforward way to align a `div` – and it's my favorite method so far to handle layouts in CSS (I use it everyday). 

Let's look at what we'd do with `Flexbox` to see how it works by recreating the same example as above.

The example:

%[https://codesandbox.io/s/align-dev-with-flexbox-2pp1m]

The code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Flexbox</title>
    <style>
      .container {
        display: flex;
      }
      .container div {
        width: 33%;
        height: 60px;
      }

      .left {
        background: yellow;
      }
      .right {
        background: red;
      }
      .center {
        background: lightblue;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="left">Left div</div>
      <div class="center">centered div</div>
      <div class="right">right div</div>
    </div>
  </body>
</html>

```

let's break it down

* We always define a `div`  parent using `display:flex` to apply `Flexbox`. So we make all the div's children inside the parent `div` able to be handled using `Flexbox` properties .
* The  `flex-direction` uses the `row` direction by default, which means the elements will be placed vertically within the container.
*  With the `justify-content` property we can align a `div`'s children(s) in different directions like the following example:

```css
.container{
 display: flex:
 justify-content:center /* flex-start, flex-end, space-between, space-evenly, space-around etc */

}
```

* `justify-content:center`  places the elements in the center of the container.
* `justify-content:flex-start` puts the elements at the beginning of the container on the left.
* `justify-content:flex-end` places elements at the end of the container on the right side.
* `justify-content:space-around` makes the elements fit in the container and puts an equal gap between all the elements.
* `justify-content:space-evenly` distributes the elements within the parent container equally with the same space, and same width.

The example above applies to all elements' children as a group.

Imagine if  we wanted to align a single `div` inside the container. We can always use `[align-self](https://developer.mozilla.org/en-US/docs/Web/CSS/align-self)` to align a single element.

```css
.container div{
 align-self:center /* can have: flex-start, or flex-end*/
}
```

We can apply the same thing to a text with `Flexbox` as in the following example:

```css

<style>
.right{
    display: flex;
    align-items: flex-end;
    flex-direction: column;
}
  
</style>
<div class="right">
<span>right div</span>
</div>
```

This is a great tweet by [Julia Evans](https://twitter.com/b0rk) which illustrates centering in CSS in general:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/centering-css-tweet.jpeg)
_[Original Tweet here ](https://twitter.com/b0rk/status/1291417463507374097)_

## Wrap up

There are many way to center elements in CSS. And you will always learn new things over time as you practice more and more. 

So I recommend that you work through some examples from what you learned today so it sticks.

* You should follow me [Twitter](https://twitter.com/SaidHYN) ?
* Check out [My Github](https://github.com/hayanisaid) 
* Visit my [Blog](https://saidhayani.com/) 

