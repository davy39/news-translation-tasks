---
title: The Best HTML and HTML5 Tutorials
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-26T00:41:00.000Z'
originalURL: https://freecodecamp.org/news/best-html-html5-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f0a740569d1a4ca4084.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: "HyperText Markup Language (HTML) is a markup language used to construct\
  \ online documents and is the foundation of most websites today. A markup language\
  \ like HTML allows us to\n\ncreate links to other documents, \nstructure the content\
  \ in our document, ..."
---

HyperText Markup Language (HTML) is a markup language used to construct online documents and is the foundation of most websites today. A markup language like HTML allows us to

* create links to other documents, 
* structure the content in our document, and 
* ascribe context and meaning to the content of our document.

An HTML document has two aspects to it. It contains structured information (Markup), and text-links (HyperText) to other documents. We structure our pages using [HTML elements](https://guide.freecodecamp.org/html#). They are constructs of the language providing [structure](https://guide.freecodecamp.org/html#) and [meaning](https://guide.freecodecamp.org/html#) in our document for the browser and the element links to other documents across the internet.

The internet was originally created to store and present static (unchanging) documents. The aspects of HTML discussed above were seen perfectly in these documents which lacked all design and styling. They presented structured information that contained links to other documents.

HTML5 is the latest version, or specification, of HTML. The World Wide Web Consortium (W3C) is the organization responsible for developing standards for the World Wide Web, including those for HTML. As web pages and web applications grow more complex, W3C updates HTML’s standards.

HTML5 introduces a host of semantic elements. Though we discussed how HTML helped to provided meaning to our document, it wasn’t until HTML5s’ introduction of [semantic elements](https://guide.freecodecamp.org/html#) that its potential was realized.

## **A simple example of HTML Document**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Page Title</title>
</head>
<body>

  <h1>My First Heading</h1>
  <p>My first paragraph.</p>

</body>
</html>
```

!DOCTYPE html: Defines this document to be HTML5

html: The root element of an HTML page

head: The element contains meta information about the document

title: The element specifies a title for the document

body: The element contains the visible page content

h1: The element defines a large heading

p: The element defines a paragraph

# Tutorials for starting with HTML and HTML5

The best place to start learning HTML is with freeCodeCamp's [2-hour intro to HTML tutorial](https://www.youtube.com/watch?v=pQN-pnXPaVg).

Then, if you're feeling more adventurous, we have an entire [12-hour course that covers HTML, HTML5, and CSS in detail](https://www.youtube.com/watch?v=mU6anWqZJcc).

![Image](https://img.youtube.com/vi/mU6anWqZJcc/maxresdefault.jpg)

## **Page Structure**

To create your pages in `HTML`, you need to know how to structure a page in `HTML`. Basically, the structuring of a page follows the order below:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Title of the Page</title>
  </head>
  <body>
    <!-- Content -->
  </body>
</html>
```

1 - The `<!DOCTYPE html>` statement must always be the first to appear on an `HTML` page and tells the browser which version of the language is being used. In this case, we are working with `HTML5`.

2 - The `<html>` and `</html>` tags tell the web browser where the `HTML` code starts and ends.

3 - The `<head>` and `</head>` tags contains information about the web site, for  example: style, meta-tags, scripts, etc…

4 - The `<title>` and `</title>` tags tell the browser what the page title is. The title can be seen by identifying the tab in your internet browser. The text that is defined between these tags is also the text that is used as title by the search engines when they present the pages in the results of a search.

5 - Between the `<body>` and `</ body>` tags the page content is placed, which is what is displayed in the browser.

## Changes in HTML5

#### **Introduction of semantic tags**

Instead of using `<div>` for every other container, there are several semantic (these tags help screenreaders which are used by visually impaired) tags such as `<header>` `<footer>` . So it is advisable to use these tags instead of the generic `<div>`.

# **HTML Elements**

Elements are the building blocks of HTML that describe the structure and content of a web page. They are the “Markup” part of HyperText Markup Language (HTML).

HTML syntax uses the angle brackets (”<” and ”>”) to hold the name of an HTML element. Elements usually have an opening tag and a closing tag, and give information about the content they contain. The difference between the two is that the closing tag has a forward slash.

Here’s an example using the [p element](https://guide.freecodecamp.org/html/elements#) (`<p>`) to tell the browser that a group of text is a paragraph:

```html
<p>This is a paragraph.</p>
```

Opening and closing tags should match, otherwise the browser may display content in an unexpected way.

![XKCD comic showing the text "Q: How do you annoy a developer?" surrounded by an opening div tag and closing span tag](http://imgs.xkcd.com/comics/tags.png)

## **Self-closing Elements**

Some HTML elements are self-closing, meaning they don’t have a separate closing tag. Self-closing elements typically insert something into your document.

An example is the [br element](https://guide.freecodecamp.org/html/elements#) (`<br>`), which inserts a line break in text. Formerly, self-closing tags had the forward slash inside them (`<br />`), however, HTML5 specification no longer requires this.

## **HTML Element Functionality**

There are many available HTML elements. Here’s a list of some of the functions they perform:

* give information about the web page itself (the metadata)
* structure the content of the page into sections
* embed images, videos, audio clips, or other multimedia
* create lists, tables, and forms
* give more information about certain text content
* link to stylesheets which have rules about how the browser should display the page
* add scripts to make a page more interactive and dynamic

## **Nesting HTML Elements**

You can nest elements within other elements in an HTML document. This helps define the structure of the page. Just make sure the tags close from the inside-most element first.

Correct: `<p>This is a paragraph that contains a <span>span element.</span></p>`

Incorrect: `<p>This is a paragraph that contains a <span>span element.</p></span>`

## **Block-level and Inline Elements**

Elements come in two general categories, known as block-level and inline. Block-level elements automatically start on a new line while inline elements sit within surrounding content.

Elements that help structure the page into sections, such as a navigation bar, headings, and paragraphs, are typically block-level elements. Elements that insert or give more information about content are generally inline, such as [links](https://guide.freecodecamp.org/html/elements#) or [images](https://guide.freecodecamp.org/html/elements#).

## **The HTML Element**

There’s an `<html>` element that’s used to contain the other markup for an HTML document. It’s also known as the “root” element because it’s the parent of the other HTML elements and the content of a page.

Here’s an example of a page with a [head element](https://guide.freecodecamp.org/html/elements#the-head-element), a [body element](https://guide.freecodecamp.org/html/elements#the-body-element), and one [paragraph](https://guide.freecodecamp.org/html/elements#the-p-element):

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>I'm a paragraph</p>
  </body>
</html>
```

## **The HEAD Element**

This is the container for processing information and metadata for an HTML document.

```html
<head>
  <meta charset="utf-8">
</head>
```

## **The BODY Element**

This is a container for the displayable content of an HTML document.

```html
<body>...</body>
```

## **The P Element**

Creates a paragraph, perhaps the most common block level element.

```html
<p>...</p>
```

## **The A(Link) Element**

Creates a hyperlink to direct visitors to another page or resource.

```html
<a href="#">...</a>
```

# Images in HTML

You can define images by using the `<img>` tag. It does not have a closing tag since it can contain only attributes. To insert an image you define the source and an alternative text which is displayed when the image can not be rendered.

`src` - This attribute provides the url to the image present either on your P.C./Laptop or to be included from some other website. Remember the link provided should not be broken otherwise the image will not be produced on your webpage.

`alt` - This attribute is used to overcome the problem of broken image or incapability of your browser to produce image on webpage. This attribute, as the name suggests, provides an “Alternative” to an image which is some ‘TEXT’ describing the image.

## **Example**

```html
<img src="URL of the Image" alt="Descriptive Title" />
```

### **To define height and width of an image you can use the height and width attribute:**

```html
<img src="URL of the Image" alt="Descriptive Title" height="100" width="150"/>
```

### **You can also define border thickness (0 means no border):**

```html
<img src="URL of the Image" alt="Descriptive Title" border="2"/>
```

### **Align an image:**

```html
<img src="URL of the Image" alt="Descriptive Title" align="left"/>
```

### **You are also able to use styles within a style attribute:**

```html
<img src="URL of the Image" alt="Descriptive Title" style="width: 100px; height: 150px;"/>
```

# How to use links in HTML

In HTML you can use the `<a>` tag to create a link. For example you can write `<a href="https://www.freecodecamp.org/">freeCodeCamp</a>` to create a link to freeCodeCamp’s website.

Links are found in nearly all web pages. Links allow users to click their way from page to page.

HTML links are hyperlinks. You can click on a link and jump to another document.

When you move the mouse over a link, the mouse arrow will turn into a little hand.

Note: A link does not have to be text. It can be an image or any other HTML element.

In HTML, links are defined with the `<a>` tag:

```html
<a href="url">link text</a>
```

Example

```html
<a href="https://www.freecodecamp.org/">Visit our site for tutorials</a>
```

The href attribute specifies the destination address (https://www.freecodecamp.org) of the link.

The link text is the visible part (Visit our site for tutorials).

Clicking on the link text will send you to the specified address.

# How to Use Lists in HTML

Lists are used to specify a set of consecutive items or related information in a well formed and semantic way, such as a list of ingredients or a list of procedural steps. 

HTML markup has three different types of lists - **ordered**, **unord**e**red** and **description** lists.

### **Ordered Lists**

An ordered list is used to group a set of related items, in a specific order. This list is created with `<ol>` tag. Each list item is surrounded with `<li>` tag.

##### **Code**

```html
<ol>
    <li>Mix ingredients</li>
    <li>Bake in oven for an hour</li>
    <li>Allow to stand for ten minutes</li>
</ol>
```

##### **Example**

1. Mix ingredients
2. Bake in oven for an hour
3. Allow to stand for ten minutes

### **Unordered Lists**

An unordered list is used to group a set of related items, in no particular order. This list is created with `<ul>`tag. Each list item is surrounded with `<li>` tag.

##### **Code**

```html
<ul>
    <li>Chocolate Cake</li>
    <li>Black Forest Cake</li>
    <li>Pineapple Cake</li>
</ul>
```

#### **Example**

* Chocolate Cake
* Black Forest Cake
* Pineapple Cake

### **Description Lists**

A description list is used to specify a list of terms and their descriptions. This list is created with `<dl>` tag. Each list item is surrounded with `<dd>` tag.

##### **Code**

```html
<dl>
    <dt>Bread</dt>
    <dd>A baked food made of flour.</dd>
    <dt>Coffee</dt>
    <dd>A drink made from roasted coffee beans.</dd>
</dl>
```

##### **Output**

**Bread** A baked food made of flour. **Coffee** A drink made from roasted coffee beans.

#### **Styling List**

You can also control the style of the list. You can use `list-style` property of lists. Your list can be bullets, squares, in Roman numerals, or can be images if you want.

`list-style` property is shorthand for `list-style-type`, `list-style-position`, `list-style-image`.

