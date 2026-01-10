---
title: How to Center a Div with CSS
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-27T19:58:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-a-div-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pixabay-161043-1.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'There are a few common coding problems you might encounter when you start
  practicing what you''ve learned by building projects.

  One common problem you''ll face as a web developer is how to place an element at
  the center of a page or within an element a...'
---

There are a few common coding problems you might encounter when you start practicing what you've learned by building projects.

One common problem you'll face as a web developer is how to place an element at the center of a page or within an element acting as its container. It's the ubiquitous "How do I center a div?" problem.

In this article, we'll see how we can center elements using various CSS properties. We'll see code examples in each section and a visual representation of the elements in all the examples.

## How to Center a Div Using the CSS Flexbox Property

In this section, we'll see how we can use the CSS Flexbox property to center an element horizontally, vertically, and at the center of a page/container.

You can use an image if you prefer that, but we'll just use a simple circle drawn with CSS. Here's the code:

```html
<div class="container">

      <div class="circle">

      </div>

</div>
```

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--276-.png)

Positioning with Flexbox requires that we write the code in the parent or container element's class.

### How to Center a Div Horizontally Using Flexbox

Now we'll write the code to center the `div` element horizontally. We're still making use of the circle we created above.  

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
  display: flex;
  justify-content: center;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

We've added two lines of code to center the circle horizontally. These are the lines we added:

```css
display: flex;
justify-content: center;
```

`display: flex;` allows us to use Flexbox and its properties, while `justify-content: center;` aligns the circle to the center horizontally. 

Here is the position of our circle:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--278-.png)

### How to Center a Div Vertically Using Flexbox

What we'll be doing in this section is similar to the last one, except for one line of code.

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
  display: flex;
  align-items: center;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

In this example, we used `align-items: center;` to center the circle vertically. Recall that we are required to write `display: flex;` first before specifying the direction.

Here's the position of our circle:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--280-.png)

### How to Position a Div at the Center Using Flexbox

In this section, we'll position the circle at the center of the page using both the horizontal and vertical alignment properties of CSS Flexbox. Here's how:

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
  display: flex;
  justify-content: center;
  align-items: center;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

Here are the three lines of code we added to the container class above:

```css
display: flex;
justify-content: center;
align-items: center;
```

As expected, we begin with `display: flex;` which allows us to use Flexbox in CSS. We then used both the `justify-content` (horizontal alignment) and `align-items` (vertical alignment) properties to position the circle at the center of the page.

Here is the position of our circle:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--282-.png)

## How to Center a Div Horizontally Using the CSS `margin` Property

In this section, we'll be using the `margin` property to center our circle horizontally.

Let's create our circle again.

```html
<div class="container">

      <div class="circle">

      </div>

</div>
```

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--276-.png)

This time we'll write the code in the `circle` class. Here's how:

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
  margin: 0 auto;
}
```

All we've added is the `margin: 0 auto;` line of code to the `circle` class.

Let's have a look at the position of the circle:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--278--1.png)

## How to Center Text Horizontally Using the CSS `text-align` Property

In this section, we'll see how to center text horizontally.

This method only works when we are working with text written within an element.

Here is an example:

```html
<div class="container">

    <h1>Hello World!</h1>
      
</div>
```

In the example above, we have created a `div` with a class of container and a `h1` element with some text. This is what it looks like at the moment:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--272-.png)

Let's write the CSS code.

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

h1 {
  text-align: center;
}
```

In other to align the text in the `h1` element at the center of the page, we had to use the `text-align` property, giving it a value of `center`. Here's what it looks like now in the browser:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--274-.png)

## Conclusion

In this article, we saw how we can center elements horizontally, vertically, and at the center of the page using Flexbox and the margin and text-align properties in CSS.

In each section, we saw both a code example and a visual representation of what the code does.

Happy coding!

