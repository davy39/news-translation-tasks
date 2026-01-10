---
title: Why You Should Use Tab Space Instead of Multiple Non-Breaking Spaces (nbsp)
  in HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T18:19:00.000Z'
originalURL: https://freecodecamp.org/news/tab-space-instead-of-multiple-non-breaking-spaces
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dbb740569d1a4ca3959.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: null
seo_desc: 'There are a number of ways to insert spaces in HTML. The easiest way is
  by simply adding spaces or multiple &nbsp; character entities before and after the
  target text. Of course, that isn''t the DRYest method.

  Instead, to keep your code easy to mainta...'
---

There are a number of ways to insert spaces in HTML. The easiest way is by simply adding spaces or multiple `&nbsp;` character entities before and after the target text. Of course, that isn't the DRYest method.

Instead, to keep your code easy to maintain and reduce repetition, you can use the `<span>` and `<pre>` elements, along with a bit of CSS:

## **Using the `<span>` element**

An example of how to use `<span>` to control the spacing between text can be seen below:

```html
<p>Hello my name is <span class="tab"> James</p>
```

Note that `<span>` tags are self closing, meaning they do not need a `/>`.

Then you can use an external or internal styling to give the class `tab` some properties. For example, the following code will work in an external stylesheet:

```css
.tab {
  padding-left: 2px;
}
```

You can also give the `<span>` some inline-style properties, as shown below.

Alternatively, you can give `<span>` the same properties as inline styles as shown below:

```html
<p>Hello my name is <span style="padding-left: 2px;"> James</p>
```

## Using the `<pre>` element

For an easy way to add a tab space, simply wrap your text in `<pre>` tags. For example:

The `<pre>` element simply represents _preformated_ text. In other words, any spaces or tabs in the inner text will be rendered. For example:

```html
<pre>
function greeting() {
  console.log('Hello world!');
}
</pre>
```

Just keep in mind that any actual tab characters (not a bunch of spaces that look like tabs), that you use with this method might appear ridiculously wide. This is because the `tab-size` property for the `<pre>` element is set to 8 spaces by default.

You can change this with a bit of CSS:

```css
pre {
  tab-width: 2;
}
```

## More info about HTML:

HyperText Markup Language (HTML) is a markup language used to construct online documents and is the foundation of most websites today. 

A markup language like HTML allows us to

* create links to other documents, 
* structure the content in our document, and 
* ascribe context and meaning to the content of our document.

An HTML document has two aspects to it. It contains structured information (Markup), and text-links (HyperText) to other documents. 

We structure our pages using [HTML elements](https://guide.freecodecamp.org/html#). They are constructs of the language providing [structure](https://guide.freecodecamp.org/html#) and [meaning](https://guide.freecodecamp.org/html#) in our document for the browser and the element links to other documents across the internet.

The internet was originally created to store and present static (unchanging) documents. The aspects of HTML discussed above were seen perfectly in these documents which lacked all design and styling. They presented structured information that contained links to other documents.

HTML5 is the latest version, or specification, of HTML. The World Wide Web Consortium (W3C) is the organization that develops the standards for the World Wide Web, including those for HTML. As web pages and web apps grow more complex, W3C updates HTML’s standards.

HTML5 introduces a whole bunch of semantic elements. While HTML helps provide meaning to our document, it wasn’t until the introduction of [semantic elements](https://guide.freecodecamp.org/html#) with HTML5 that its potential was fully known.

## **A simple example of an HTML Document**

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

## HTML Versions

Since the early days of the web, there have been many versions of HTML

* HTML1991
* HTML 2.01995
* HTML 3.21997
* HTML 4.011999X
* HTML2000
* HTML52014

#### **Other Resources**

* [HTML Elements](https://guide.freecodecamp.org/html/elements)
* [Semantic HTML](https://guide.freecodecamp.org/html/html5-semantic-elements)
* [HTML Attributes](https://guide.freecodecamp.org/html/attributes)

