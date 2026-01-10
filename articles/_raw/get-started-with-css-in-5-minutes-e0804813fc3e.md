---
title: Learn CSS in 5 minutes - A tutorial for beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T22:59:16.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-css-in-5-minutes-e0804813fc3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s2XVUr_QAwNKET1JPOZeEg.jpeg
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  A quick tutorial on the design language of the web.


  _Want to take our free CSS course? Click here!_

  CSS (Cascading Style Sheets) is what makes web pages look good and presentable.
  It’s an essential part of modern web development...'
---

By Per Harald Borgen

#### A quick tutorial on the design language of the web.

![Image](https://cdn-media-1.freecodecamp.org/images/V1j9VppYwp81V7cTFYNrnRG4ubi5lgXUWEZc)
_Want to take our free CSS course? [Click here!](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotocss_5_minute_article)_

CSS (Cascading Style Sheets) is what makes web pages look good and presentable. It’s an essential part of modern web development and a must-have skill for any web designer and developer.

In this article, I’ll give you a quick introduction to help you get started with CSS.

**We’ve also launched a free full-length CSS course on Scrimba.** **[Click here to check it out.](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_5_minute_article)**

I’m assuming that you have a basic understanding of HTML, but other than that there are no prerequisites for this tutorial.

### Getting Started

Let’s start with learning how we can include CSS in our projects. There are typically three ways we do that.

#### 1. Inline CSS

First off, we can include CSS directly in our HTML elements. For this, we make use of the `style` attribute and then we provide properties to it.

```html
<h1 style="color: blue"> Hello world! </h1>

```

Here we’re giving it the property of `color`, and setting the value to `blue`, which results in the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ig1ubv9fGhYQauKUsi18YQ.png)

We can also set multiple properties inside the `style` tag if we wanted. However, I don’t want to continue down this path, as things start to get messy if our HTML is cluttered with lots of CSS inside it.

This is why the second method to include CSS was introduced.

#### 2. Internal CSS

The other way to include CSS is using the `style` element in the `head` section of the HTML document. This is called internal styling.

```html
<head>  
    <style>  
        h1 {  
            color: blue;  
        }  
    </style>  
</head>

```

In the style element, we can give the styling to our HTML elements by selecting the element(s) and provide styling attributes. Just like we applied the`color`property to the `h1` element above.

#### 3. External CSS

The third and most recommended way to include CSS is using an external stylesheet. We create a stylesheet with a `.css` extension and include its link in the HTML document, like this:

```html
<head>  
    <link rel="stylesheet" href="style.css">  
</head>

```

In the code above, we have included the link of `style.css` file using the `link` element. We then write all of our CSS in a separate stylesheet called `style.css` so that it’s easily manageable.

```css
h1 {  
   color: blue;  
}

```

This stylesheet can also be imported into other `HTML` files, so this is great for reusability.

### CSS Selectors

As we discussed earlier, CSS is a design language which is used to style HTML elements. And in order to style elements, you first have to select them. You’ve already seen a glimpse of how this works, but let’s dive a bit deeper into CSS selectors, and look at three different ways you can select HTML elements.

#### 1. Element

The first way to select an HTML element is by simply using the name, which is what we did above. Let’s see how it works:

```css
h1 {  
    font-size: 20px;  
}  
p {  
    color: green;  
}  
div {  
    margin: 10px;  
}

```

The example above is almost self-explanatory. We are selecting different elements like `h1`, `p`, `div` and giving them different style attributes. The `font-size` controls the size of the text, `color` sets the text color, and `margin` adds spacing around the element.

#### 2. Class

Another way of selecting HTML elements is by using the class attribute. In HTML, we can assign different classes to our elements. Each element can have multiple classes, and each class can also be applied to multiple elements as well.

Let’s see it in action:

```html
<div class='container'>  
    <h1> This is heading </h1>  
</div>

```

```css

.container {  
    margin: 10px;  
}

```

In the code above, we have assigned the class of `container` to the div element. In the stylesheet, we select our class using `.className` format and giving it a `10px` margin.

#### 3. ID

Like classes, we can also use IDs to select HTML elements and apply styling to them. The only difference between class and ID is that one ID can be assigned to only one HTML element.

```html
<div>  
    <p id='para1'> This is a paragraph </p>  
</div>

```

```css

#para1 {  
    color: green;  
    font-size: 16px;  
}

```

The example above displays how we assign an ID to the paragraph element and later use the ID selector in the stylesheet to select the paragraph and apply the style to it.

### Fonts & Colors

CSS provides us with literally hundreds of options for playing around with fonts and colors and making our HTML elements look pretty. We can choose from two types of font family names:

**1. Generic Family:** a group of font families with a similar look (like ‘Serif’ or ‘Monospace’)

**2. Font Family:** a specific font family (like ‘Times New Roman’ or ‘Arial’)

For colors, we can use predefined color names, or RGB, HEX, HSL, RGBA, HSLA values.

```html
<div class='container'>  
    <h1 class='heading1'>  
        CSS is Coooooool!!!!  
    </h1>  
</div>

```

```css
.container {  
    width: 500px;  
    height: 100px;  
    background-color: lightcyan;  
    text-align: center;  
}

.heading1 {  
    font-family: 'Courier New';  
    color: tomato;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*OBQCn1lDTG8cskhUYwNTDg.png)

As you can see in the above example, we have a div element with the class of `container`. Inside this div, there is an `h1` tag with some text inside it.

In the stylesheet, we select the container class and set its `width`, `height`, `background-color`, and `text-align`.

Finally, we select the `.heading1` class — which is applied to the `h1` tag — and give it the attributes of `font-family` and `color`.

### Conclusion

You might feel a bit overwhelmed by all this information, but don’t worry.

Just check out our [free Intro to CSS course on Scrimba](https://scrimba.com/g/gintrotocss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_5_minute_article) and you’ll be a web design ninja in less than an hour.

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotocss_5_minute_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotocss_5_minute_article)_

