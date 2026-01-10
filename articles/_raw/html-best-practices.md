---
title: HTML Best Practices – How to Build a Better HTML-Based Website
subtitle: ''
author: Cess
co_authors: []
series: null
date: '2022-01-03T23:42:00.000Z'
originalURL: https://freecodecamp.org/news/html-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/HTML-Best-Practices---How-to-Build-a-Better-HTML-Based-Website--1-.png
tags:
- name: best practices
  slug: best-practices
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "HTML is the backbone of any website. It's the first thing people see. Without\
  \ it, there would be no website. \nBecause of this, it's important that you stick\
  \ to good coding practices. If you don't follow the best practices, you will create\
  \ a bad user ..."
---

**HTML** is the backbone of any website. It's the first thing people see. Without it, there would be no website. 

Because of this, it's important that you stick to good coding practices. If you don't follow the best practices, you will create a bad user experience for the web user.

There's always something new to learn in HTML, whether you're a coding newbie or an experienced pro.

In this article, we will talk about the basic best practices of HTML.

Let's get started. 💃

## HTML Best Practices

**HTML best practices** are rules that help you create websites that are easy to maintain and read.

Here are some guidelines to keep in mind when building an HTML-based website:

### Use only one <h1> element for one code sheet

There are six different heading tags in HTML,  `<h1>` to `<h6>`. The `<h1>` tag is the main heading (subject of the web page) while the `<h6>` tag is the least important heading.

The `<h1>` tag is bigger than the `<h2>` tag, the `<h2>` tag is bigger than the `<h3>`tag, all the way down to the `<h6>` tag. Each of the headings decreases in size according to its importance.

It is important to avoid using more than one `<h1>` element for one code sheet.

Don't do this  ⬇️:

```
<main>
<div>
<h1>Can Coding be fun?</h1>
<p>The more you code the better you become</p>
</div>

<div>
<h1>Coding is fun</h1>
<p>It is always better when you have fun coding</p>
</div>
</main>
```

In the above example, we used the `<h1>` tag on the first and second `<div>`. Coding this way will work, but although you will achieve the same goal, this is not the best practice.

Do this instead ⬇️:

```
<main>

<div>
<h1>Can coding be fun?</h1>
<p>The more you code the better you become</p>
</div>

<div>
<h2>Coding is fun</h2>
<p>It is always better when you have fun coding</p>
</div>

</main>

```

Having only one `<h1>` element on a web page is vital for Search Engine Optimization (SEO). It helps search engines understand what a web page is all about (the main idea of a web page).  

### Do not skip heading levels in HTML

When using the header tags, it's vital to proceed from `<h1>` to `<h2>` to `<h3>` to `<h4>` and so on...

Don't use `<h1>` and then jump to `<h3>` when using header tags. It's difficult for web visitors using a screen reader to understand the contents of your web page when you skip heading levels.

A screen reader is a technology that helps people who have difficulty seeing access and interact with digital content, like websites or applications via audio or touch. The main users of screen readers are people who are blind or have very limited vision.  

You can read a little [introduction to screen readers here](https://abilitynet.org.uk/factsheets/introduction-screen-readers).

Don't do this  ⬇️:

```
<h1>Coding is fun</h1>
<h3>It is always better when you have fun coding</h3>
<h5>Consistency is Key</h5>
```

Do this instead  ⬇️:

```
<h1>Can coding be fun?</h1>
<h2>The more you code the better you become</h2>
<h3>Coding is fun</h3>
```

### Use the figure element to add captions to your images in HTML

It's advisable to use the `<figure>` element when adding captions to your images. It is important to use the `<figcaption>` element along with the `<figure>` element for it to work.

Don't do this  ⬇️:

```
<div>
<img src=“a-man-coding.jpg” alt=“A man working on his computer”>
<p>This is a picture of a man working on his computer</p>
</div>
```

The above example will work as expected but is not the best way to go about it. In a situation where the image fails to load you will have the `alt` text and the text on the `<p>` element showing on the screen. It will be difficult for a web visitor using a screen reader to tell the difference between the `<p>` and `alt` text.

Always keep in mind that just because your code works doesn't mean you're following best practices.

Do this instead  ⬇️:

```
<figure>
<img src=“a-man-coding.jpg” alt=“A man working on his computer”>
<figcaption> This is a picture of a man working on his computer</figcaption>
</figure>
```

The above example is the best way to add captions to your images.

It is important to add captions to your images this way for:

* Search engine optimization: It is easier to find your images on search engines.
* It will be easier for web visitors who use screen readers to understand the content of your web page.

### Do not use divs to create headers and footers – use semantic elements instead

HTML semantic elements mark up the structure of a document in a more meaningful way on a webpage. It is best practice to use HTML semantic elements for the proper assembly of your web page.

Avoid using `<divs>` in place of HTML semantics. Do not use `<div>` elements to show headers and footers on your web page. Use semantic `<header>` and `<footer>` elements instead.

The `<header>` element shows the navigation or the opening part of the web page.

The `<footer>` element shows copyright information or navigation links about the web page.

Don't do this  ⬇️:

```
<div class="header">
<a href="index.html">Home</a>
<a href="#">About</a>
<a href="#">Contact</a>
</div>

<div class="footer">
<a href="index.html">Home</a>
<a href="#">About</a>
<a href="#">Contact</a>
</div>
```

In the above example, we used the `<div>` tag as a container for the `<header>` and `<footer>`. Coding this way will work, but although you will achieve the same goal, this is not the best practice.

Do this instead  ⬇️:

```
<header>
<h1></h1>
</header>

<footer>
<a href="index.html">Home</a>
<a href="#">About</a>
<a href="#">Contact</a>
</footer>
```

The above example is the best way to add `<footers>` and `<headers>` to your web page.

It is important to add `<footer>` and `<header>` using HTML semantic elements because:

* Using semantic elements for your `header` and `footer` makes your code easier to read. 

* It provides a better user experience for web visitors. It will be easier for web visitors who use screen readers to understand the content of your web page.


Checkout this article to know more about [HTML semantic elements](<https://www.freecodecamp.org/news/semantic-html5-elements/#:~:text=Semantic%20HTML%20elements%20are%20those,content%20that%20is%20inside%20them>).

### Avoid using `<b>` and `<i>` to bold and italicize texts on a web page

The `<b>` and `<i>` tags are also known as the bold and italics tag. They are both used to highlight words in a text on a web page.

You shouldn't use `<b>` and `<i>` for bolding and italics because they have no semantic meaning. Use the `font-weight` CSS property or use the `<strong>` and the `<em>` tags instead.

You use the `<strong>` tag to make a text on a webpage important. It highlights or bolds a text on a webpage. The `<em>` tag emphasizes the text in a webpage. It also displays the text in italics like the `<i>` tag.

Don't do this  ⬇️:

```
<p><i>Code at your own pace</i><p>

<p><b>code at your own pace</b><p>
```

The displayed texts will be bold and italicized in the example above. It will be of no importance to the web user using a screen reader. It has no semantic meaning.

**The** **HTML5** specification says that the `<b>` and `<i>` tags should only be used as a last resort if no other tag is available.

Do this instead  ⬇️:

```
 <p><strong>Code at your own pace</strong><p>

<p><em>code at your own pace</em><p>
```

### Don't place block-level element within inline elements

Block-level elements start in a new line on a web page. By default, they stretch from the beginning of the line to the end on a web page. You won't be able to add more content inline to a block element without using CSS.

The `<p>`, `<h1>-<h6>`, and the `<div>` elements are some of the examples of a block level element.

The inline element covers the smallest area on a web page. They do not start on a new line on a web page.

The `<span>`, `<em>`, and the `<a>` elements are some of the examples of inline elements.

You cannot place block elements inside inline elements.

Don't do this  ⬇️:

```
<a href="#" >
    
    <p> Visit freecodecamp </p>
    
</a>
```

You cannot wrap `<p>` inside a `<a>` element because `<p>` is a block-level element and `<a>` is an inline element.

Do this instead  ⬇️:

```
<p>
Visit <a href="www.freecodecamp. org" target="_blank">FreecodeCamp</a> 
to learn Javascript
</p>
```


The above example is the best way to nest inline elements inside a block-level element.

It is important to note that:

* The block-level element cannot be nested inside an inline element.
* The inline element can be nested inside a block-level element.
* The inline and the block-level element can be nested inside the block-level element.

Just a quick note: nested, in the above example, means to place inside. So when I say it can't be nested, I'm referring to the fact that it can't be placed inside.

I hope you understand these three simple rules used for nesting elements.

It is also possible to convert block-level elements to inline elements and vice versa using CSS. Use `display: inline-block` and `display: inline` to convert from block-level to inline element.

It's important to remember that just because your code works doesn't mean you're following best practices.

This is why I always recommend using the [W3C markup validation service](https://validator.w3.org/) to double-check your codes.

This validator checks the markup validity of web documents in HTML, XHTML, SMIL, MathML, etc: [W3c markup validation service](https://validator.w3.org/).

You can double-check your code by copying its URL and pasting it on the site or uploading your HTML file.

## Conclusion
I hope this article helped you learn a thing or two about HTML best practices. I tried to include only the most useful tips so you can start using them right away! 
 
If you have any other questions or comments, please feel free to contact me anytime on Twitter: [@cessss_](http://www.twitter.com/cessss_) and LinkedIn: [Success](https://www.linkedin.com/in/success-eriamiantoe/) 
 
I'll try to respond as soon as possible! Thank you for reading 💙.



