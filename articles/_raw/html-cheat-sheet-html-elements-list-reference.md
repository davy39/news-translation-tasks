---
title: HTML Cheat Sheet – HTML Elements List Reference
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-03T17:00:24.000Z'
originalURL: https://freecodecamp.org/news/html-cheat-sheet-html-elements-list-reference
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/html-cheat-sheet.png
tags:
- name: cheatsheet
  slug: cheatsheet
- name: HTML
  slug: html
- name: reference
  slug: reference
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In this tutorial, we will go over commonly used HTML tags, elements, and
  attributes. We''ll also see examples of how these tags, elements, and attributes
  work.

  You can use this article as a reference guide whether you''re a beginner or experienced
  deve...'
---

In this tutorial, we will go over commonly used HTML tags, elements, and attributes. We'll also see examples of how these tags, elements, and attributes work.

You can use this article as a reference guide whether you're a beginner or experienced developer.

## What Makes Up an HTML Document?

The following tags define the basic HTML document structure:

* `<html>` tag – This tag acts as a container for every other element in the document except the `<!DOCTYPE _html_>` tag. 
* `<head>` tag– Includes all the document's metadata. 
* `<title>` tag – Defines the title of the document which is displayed in the browser's title bar.
* `<body>` tag – Acts as a container for the document's content that gets displayed on the browser.

Here's what all that looks like:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title> My HTML Cheat Sheet </title>
  </head>
  <body></body>
</html>

```

`<!DOCTYPE _html_>` specifies that we are working with an HTML5 document.

The following tags give additional information to the HTML document:

* `<meta>` tag – This tag can be used to define additional information about the webpage.
* `<link>` tag – Used to link the document to an external resource.
* `<style>` tag – Used for defining styles for the document. 
* `<script>` tag – Used to write code snippets (usually JavaScript) or to link the document to an external script.

```html
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>My HTML Cheat Sheet</title>

    <style>
      * {
        font-size: 100px;
      }
    </style>

    <script>
      alert('This is an alert');
    </script>
 </head>
```

## HTML Document Structure

When you're fleshing out your HTML document, you'll use certain tags to create the structure.

The `<h1>` to `<h6>` tags show different levels of headings in a document, with <h1> being the largest and <h6> being the smallest.

```html
<h1> Heading 1 </h1>
<h2> Heading 2 </h2>
<h3> Heading 3 </h3>
<h4> Heading 4 </h4>
<h5> Heading 5 </h5>
<h6> Heading 6 </h6>
```

You use the `<p>` tag to create a paragraph.

```html
<p> This is a paragraph </p>
```

The `<div>` tag can be used to divide and style separate sections of the document. It also acts as a parent container for other elements. Here's how it works:

```html
<div class="newsSection">
  <h1> This is the news section </h1>
  <p> Welcome to the news section! </p>
</div>

<div class="contactSection">
  <h1> This is the contact us section </h1>
  <p> Hello world! </p>
</div>
```

We also have the `<span>` tag. This is similar to `<div>` but you use it as an inline container. 

```html
<p> I love <span class="keyword"> coding! </span></p>
```

There's the `<br/>` tag, which we use for creating line breaks. This has no closing tag.

```html
<p> I love <br/> freeCodeCamp </p>
```

The `<hr/>` tag is used to create a horizontal line. It also has no closing tag.

## Images in HTML

In HTML, we use the `<img/>` tag to display images. 

Here are some attributes of the `<img/>` tag:

* `src` is used to specify the path to the location of the image on your computer or the web.
* `alt` defines an alternate text that displays if the image cannot be rendered. The alt text is also good for screen readers.
* `height` specifies the height of the image.
* `width` specifies the width of the image.
* `border` specifies the thickness of the borders, which is set to 0 if no border is added.

```html
<img src="ihechikara.png" alt="a picture of Ihechikara" width="300" height="300">
```

## Text Formatting in HTML

We have many ways to format text in HTML. Let's go over them now briefly.

* `<i>` displays text in italics.
* `<b>` displays text in bold. 
* `<strong>` displays text in bold. Used to make important emphasis.
* `<em>` another emphasis tag that displays text in italics.
* `<sub>` defines subscript text, like the two atoms of oxygen in CO₂.
* `<sup>` defines a superscript like the power of a number, 10².
* `<small>` reduces the size of text.
* `<del>` defines deleted text by striking a line through the text.
* `<ins>` defines inserted text which is usually underlined. 
* `<blockquote>` is used to enclose a section of text quoted from another source.
* `<q>` is used for shorter inline quotes.
* `<cite>` is used for citing the author of a quote.
* `<address>` is used for showing the author's contact information.
* `<abbr>` denotes an abbreviation.
* `<code>` displays code snippets.
* `<mark>` highlights text.

```html
<p><i> italic text </i></p>
<p><b>bold text </b></p>
<p><strong> strong text </strong></p>
<p><em> strong text </em></p>
<p><sub> subscripted text </sub></p>
<p><sup> superscripted text </sup></p>
<p><small> small text </small></p>
<p><del> deleted text </del></p>
<p><ins> inserted text </ins></p>
<p><blockquote> quoted text </blockquote></p>
<p><q> short quoted text </q></p>
<p><cite> cited text </cite></p>
<p><address> address </address></p>
<p><abbr> inserted text </abbr></p>
<p><code> code snippet </code></p>
<p><mark> marked text </mark></p>
```

## Links

The `<a>` tag, also known as the anchor tag, is used to define hyperlinks that link to other pages (external web pages included) or to a section of the same page.

Here are some attributes of the `<a>` tag:

* `href` specifies the URL the link takes the user to when clicked.
* `download` specifies that the target or resource clicked is downloadable.
* `target` specifies where the link is to be opened. This could be in the same or separate window.

```html
<a href="https://www.freecodecamp.org/" target="_blank"> Learn to code </a>
```

## Lists

The `<ol>` tag defines an ordered list while the `<ul>` tag defines an unordered list.

The `<li>` tag is used to create items in the list.

```html
<!-- Unordered list -->
<ul>
  <li> HTML </li>
  <li> CSS </li>
  <li> JavaScrip t</li>
</ul>

<!-- Ordered list -->
<ol>
  <li> HTML </li>
  <li> CSS </li>
  <li> JavaScript </li>
</ol>
```

## Forms

The `<form>` tag is used to create a form in HTML. Forms are used to get user inputs. Here are some attributes associated with the `<form>` element:

* `action` specifies where the form information goes when submitted.
* `target` specifies where to display the form's response.
* `autocomplete` can have a value of on or off. 
* `novalidate` specifies that the form should not be validated.
* `method` specifies the HTTP method used when sending form data.
* `name`  specifies the name of the form.
* `required` specifies that an input element cannot be left empty.
* `autofocus` gives focus to the input elements when the page loads.
* `disabled` disables an input element so the user can longer interact with it.
* `placeholder` is used to give users a hint on what information is required for an input element.

Here are other input elements associated with forms:

* `<textarea>` for getting user text input with multiple lines.
* `<select>` specifies a list of options the user can choose from.
* `<option>` creates an option under the select element.
* `<input>` specifies an input field where the user can enter data. This has a `type` attribute that specifies what type of data the user can input.
* `<button>` creates a button.

```html
<form action="/info_url/" method="post">

    <label for="firstName"> First name: </label>
    <input type="text" 
           name="firstName" 
           placeholder="first name" 
           required
    >
    
    <label for="lastName"> Last name: </label>
    <input type="text" 
           name="lastName" 
           placeholder="last name" 
           required
    >

    <label for="bio"> Bio: </label>
    <textarea name="bio"></textarea>

    <select id="age">
      <option value="15-18">15-18</option>
      <option value="19-25">19-25</option>
      <option value="26-30">26-30</option>
      <option value="31-36">31-36</option>
    </select>

    <input type="submit" value="Submit">
    
  </form>
```

## Tables

* The `<table>` tag defines a HTML table.
* `<thead>` specifies information for each column in a table.
* `<tbody>` specifies the body or content of the table.
* `<tfoot>` specifies the footer information of the table.
* `<tr>` denotes a row in the table.
* `<td>` denotes a single cell in the table.
* `<th>` denotes the value column's heading.

```html
<table>
    
  <thead>
    <tr>
      <th> Course </th>
      <th> Progress </th>
    </tr>
  </thead>
    
  <tbody>
    <tr>
      <td> HTML </td>
      <td> 90% </td>
    </tr>
    <tr>
      <td> CSS </td>
      <td> 80% </td>
    </tr>
  </tbody>
    
  <tfoot>
    <tr>
      <td> JavaScript </td>
      <td> 95% </td>
    </tr>
  </tfoot>
    
</table>
```

## Tags introduced in HTML5

Here are some tags introduced in HTML5:

* `<header>` specifies the webpage header
* `<footer>` specifies the webpage footer. 
* `<main>` specifies a main content section.
* `<article>` specifies an article's section, usually for content that can stand alone on the webpage.
* `<section>` is used to create separate sections.
* `<aside>` is usually used to when placing items in a sidebar.
* `<time>` is used for formatting date and time.
* `<figure>` is used for figures like charts.
* `<figcaption>` denotes a description of a figure.
* `<nav>` is used to nest navigation links.
* `<meter>` is used to measure data within a range.
* `<progress>` is used as a progress bar.
* `<dialog>` is used to create a dialog box.
* `<audio>` is used to embed an audio file in the web page.
* `<video>` is used to embed video.

```html
  <header>
    <h1> Welcome </h1>
    <h3> Hello World! </h3>
  </header>

  <nav>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">About us</a></li>
    </ul>
  </nav>

  <article>
      
    <h1> An article about us </h1> 
    <p> Article content </p>

    <aside>
      <p> It's sunny today </p>
    </aside>
      
  </article>

  Progress: <progress min="0" max="100" value="50"> </progress>

  <footer> Copyright 2022-2099. All Rights Reserved. </footer>
```

## Conclusion

In this article, we have seen a lot of HTML tags, elements, and attributes commonly used by developers. This is not all there is, but should serve as a good reference resource.

I hope you found this helpful. Thank you for reading.

