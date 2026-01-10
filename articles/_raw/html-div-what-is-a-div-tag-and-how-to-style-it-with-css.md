---
title: HTML Div – What is a Div Tag and How to Style it with CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-07T15:08:40.000Z'
originalURL: https://freecodecamp.org/news/html-div-what-is-a-div-tag-and-how-to-style-it-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/divTag.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'The HTML division tag, called "div" for short, is a special element that
  lets you group similar sets of content together on a web page. You can use it as
  a generic container for associating similar content.

  The div tag is one of the most used tags an...'
---

The HTML division tag, called "div" for short, is a special element that lets you group similar sets of content together on a web page. You can use it as a generic container for associating similar content.
 
The `div` tag is one of the most used tags and doesn't seem to be going anywhere despite the introduction of semantic elements (these elements let you use several tags as a container).

In this tutorial, I will show you the various things you can do with the `div` tag, how you can use multiple divs the same HTML file without getting confused, and how to style it.

## When to Use the `div` Tag 

The `div` tag is multi-purpose – you can use it to do several things on a web page. You'll mostly use it in web layouts and CSS art, but it's super flexible. 

Ultimately, you'll almost always to use it to style whatever it contains or manipulate such things with JavaScript. 

### 1. Use `div` in Web Layouts

You'll primarily use the `div` tag to group similar content together so you can style it easily. A great example of this is using div to group different sections of a webpage together. You can put together the header, nav, sections, and footer of a page in an individual div tag so they can be styled together. 

Later in this tutorial, I will take you through how to make a web layout with multiple `div` tags without getting confused.

Div itself does not have a direct effect on the presentation of the content unless you style it.

### 2. Use `div` in CSS Art

With the div tag, you can make various shapes and draw anything because it is easy to style. 

- How to make a square with the `div` tag 

To make a square with `div` tag, you first need to define an empty div tag and attach a class attribute to it in the HTML. In the CSS, select the div with the class attribute, then set an equal height and width for it.

```html
<div class="square"></div>
```

```css
 body {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
      background-color: #f1f1f1;
    }
.square {
      background-color: #2ecc71;
      width: 200px;
      height: 200px;
    }
```

![square](https://www.freecodecamp.org/news/content/images/2021/09/square.png)

- How to make a circle with the `div` tag 

You can make a circle with the `div` tag by coding an empty div in the HTML, setting an equal height and width for it in the CSS, then a `border-radius` of 50%.

```html
<div class="circle"></div>
```

```css
  body {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
      background-color: #f1f1f1;
    }

    .circle {
      background-color: #2ecc71;
      width: 200px;
      height: 200px;
      border-radius: 50%;
    }
```
![circle](https://www.freecodecamp.org/news/content/images/2021/09/circle.png)

- How to make the Nigerian flag with CSS 

Making the Nigerian flag with the `div` tag is not that hard. The flag is a rectangular shape with the colors green, white, and green. 

To make it, define 3 `div` tags and attach different classes, then style them appropriately in the CSS.

```html
<div class="naija-flag">
    <div class="first-green"></div>
    <div class="white"></div>
    <div class="second-green"></div>
</div>
```

```css
.naija-flag {
  display: flex;
}
.first-green {
  height: 100px;
  width: 60px;
  background-color: green;
}
.white {
  height: 100px;
  width: 60px;
  background-color: white;
}
.second-green {
  height: 100px;
  width: 60px;
  background-color: green;
}
```
![naija-flag](https://www.freecodecamp.org/news/content/images/2021/09/naija-flag.png)

## How to Style the `div` Tag

As we discussed above, the div tag is very easy to style. It's one of the reasons why many developers use it to group similar content.

The div tag accepts almost all CSS properties without a problem. Let's look at a few examples of that now.

### 1. How to Apply Font Properties with `div`

You can apply the CSS properties such as `font-size`, `font-family`, `font-weight`, and `font-style` on content grouped together with the `div` tag: 

```html
<div class="font-properties">
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate quo
        ullam modi alias assumenda, itaque libero? Quas quidem sint illo.
      </p>
      <p>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus
        ipsam eaque rem dicta, quos quas ipsum.
      </p>
</div>
```

```css
body {
      max-width: 900px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
      background-color: #f1f1f1;
    }

.font-properties {
      font-family: cursive, sans-serif;
      font-size: 1.3rem;
      font-weight: bolder;
      font-style: italic;
    }
```

![font](https://www.freecodecamp.org/news/content/images/2021/09/font.png)

### 2. How to Apply Color with the Div Tag

You can apply the CSS `color` and `background-color` properties on content grouped together with the `div` tag:

```html
<div class="color-properties">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate quo
    ullam modi alias assumenda, itaque libero? Quas quidem sint illo.
  </p>
  <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus
    ipsam eaque rem dicta, quos quas ipsum.
  </p>
</div>
```

```css
.color-properties {
  color: white;
  background-color: #2ecc71;
}
```
![color](https://www.freecodecamp.org/news/content/images/2021/09/color.png)

### 3. How to Style Texts with the Div Tag

You can apply the CSS `text-transform` and `text-decoration` properties on a `div` tag like this:

```html
<div class="text-properties">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate quo
    ullam modi alias assumenda, itaque libero? Quas quidem sint illo.
  </p>
  <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus
    ipsam eaque rem dicta, quos quas ipsum.
   </p>
</div>
```

```css
.text-properties {
    text-transform: uppercase;
    text-decoration: underline;
  }
```

![text](https://www.freecodecamp.org/news/content/images/2021/09/text.png)

### 4. How to Create a Shadow Effect with the Div Tag

You can create a shadow effect with the `div` tag with the box-shadow property:

```html
<div class="box-shadow">
      <p>
        Before paying to learn programming, checkout freeCodeCamp.org
        <br />
        The HTML, CSS, and JavaScript curricula would take you from zero to hero
        in web development.
      </p>
      <p>
        There is a Python curriculum that will get you a considerable knowledge
        in Python <br />
        And an upcoming Data Science curriculum.
      </p>
</div>
```

```css
.box-shadow {
      font-family: cursive, sans-serif;
      background-color: #2ecc71;
      color: white;
      padding: 10px;
      border-radius: 4px;
      box-shadow: 2px 2px 20px 23px #7fecad;
    }
```

What’s happening in the CSS above? 

I was able to create the shadow effect with the CSS box-shadow property. 

- The first value (2px) represents the offset on the x-axis (offset-x)
- The second (another 2px) represents the offset on the y-axis (offset-y)
- The next 20px is for the blur-radius, that is, how blurry you want the shadow to be.
- The 23px value is the spread radius (how far you want the shadow to spread)
- The last value is the shadow color – in this case, #7fecad. 

The output looks like this:
![box-shadow](https://www.freecodecamp.org/news/content/images/2021/09/box-shadow.png)

## How to Use Multiple Div Elements without Getting Confused

Div tags are commonly used to group similar content together. In older and even some newer web pages, you'll find divs all around, despite the fact that semantic tags are recommended for accessibility and better SEO. 

Since `div` tags are still very common, I recommend applying class and id attributes to them so you can manipulate individual div elements with those attributes.

I will walk you through how to put this into practice by making a basic web layout. 

The first section you'll want to make is the header, containing the logo and navbar:

```html
 <div class="header">
      <h2 class="logo">freeCodeCamp</h2>

      <ul class="nav">
        <li><a href="">Home</a></li>
        <li><a href="">About</a></li>
        <li><a href="">Serices</a></li>
        <li><a href="">Contact</a></li>
      </ul>
</div>
```


Before styling the navbar, I made some CSS resets to make things align correctly and display nicely: 

```css
* {
   margin: 0;
   padding: 0;
   box-sizing: border-box;
 }

.hero,
.about,
.services,
.contact {
  max-width: 1000px;
  margin: 0 auto;
  margin-bottom: 20px;
}
```

In the code snippet above: 

- I removed the default margin and padding
- I set a maximum width for the main sections so they don’t go all across for better UX
- I set a margin at the bottom of each section to give them some space
- I set a margin 0 at the top and bottom, auto on the left and right to center them.

To style the navbar appropriately, I will grab the container `div` tag with its class attribute, `header`. I'll give it a display of `flex`, alongside some other properties to lay it out nicely. I will also grab the `div` wrapped around the navbar (`ul` element) by its class and lay it out with Flexbox.

```css
.header {
      padding: 0 70px;
      display: flex;
      align-content: center;
      justify-content: space-between;
      margin-top: 20px;
      margin-bottom: 20px;
    }

.nav {
      display: flex;
      align-content: center;
      justify-content: center;
      gap: 60px;
      list-style-type: none;
    }

.nav li a {
      text-decoration: none;
      color: black;
      font-size: 1.2rem;
    }
```

For the remaining sections apart from the footer, the HTML and stylings are generic: 

```html
<div class="hero">
      <h1>Hero Section</h1>
</div>
<div class="about">
      <h1>About Us</h1>
</div>
<div class="services">
      <h1>Our Services</h1>
</div>
<div class="contact">
      <h1>Contact Us</h1>
</div>
<div class="footer">
      <p>&copy; 2021 All Rights Reserved</p>
</div>
```

```css
.hero {
      background-color: #eee;
      height: 200px;
    }

.hero h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.about {
      background-color: #eee;
      height: 200px;
    }

.about h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.services {
      background-color: #eee;
      height: 200px;
    }

.services h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.contact {
      background-color: #eee;
      height: 200px;
    }

.contact h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.footer {
      background-color: #777;
      height: 40px;
    }

.footer p {
      margin: 0 auto;
      line-height: 1.7;
    }
```


I gave the individual sections a greyish background color and a height of 200px. I positioned the h1 tags inside in their centers with Flexbox and applied a `line height` of 1.5 to each of them. 

Finally, I gave the footer a deeper grey background color to make it distinct, and centered the content in it with a `line height` of 1.7. 

The resulting layout looks like this:![layout](https://www.freecodecamp.org/news/content/images/2021/09/layout.gif)


## Conclusion 

The HTML div tag is commonly used among web developers everywhere.

Just keep in mind that you should usually use semantic HTML in place of the div tag unless none of them (the semantic tags) really match the content to group together. This is because semantic tags are better for accessibility and SEO. 

In short, the div tag remains useful and isn’t going anywhere anytime soon, so feel free to use it when necessary.

Thank you for reading and have a nice time.



