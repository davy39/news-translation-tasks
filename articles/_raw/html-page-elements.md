---
title: HTML Page Elements – Explained for Beginners
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-06-13T21:01:13.000Z'
originalURL: https://freecodecamp.org/news/html-page-elements
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-joshua-135018.jpg
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "HTML, which stands for Hypertext Markup Language, is the standard markup\
  \ language used for creating web pages and structuring their content on the World\
  \ Wide Web. \nHTML serves as the backbone of web development and acts as a fundamental\
  \ building bloc..."
---

HTML, which stands for **Hypertext Markup Language**, is the standard markup language used for creating web pages and structuring their content on the World Wide Web. 

HTML serves as the backbone of web development and acts as a fundamental building block for creating web-based documents. Let's take a quick look at how it works.

## What Does HTML Do?

The main role of HTML is to define the structure and layout of a web page by using a set of tags or elements. These tags represent different types of content such as headings, paragraphs, images, links, forms, and tables. 

HTML tags are enclosed in angle brackets (<>) and are composed of an opening tag, content, and a closing tag (which is identified by its forward slash - "/").

This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). If you'd like, you can follow the video version here:

%[https://youtu.be/jWOVD6MtjyI]

By using HTML, web developers can define the semantic structure of a webpage, specifying elements like headings, paragraphs, lists, and sections. Here's a typical example of an HTML page with `<head>`, `<body>`, `<header>`, and `<footer>` sections clearly identified:

```
<!DOCTYPE html>
<html>
<head>
	<title>My Demo</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<header>
	<h3>My Demo</h3>
</header>
<div class="container2">
	<!--And a comment!
	-->
	Here are some important points to consider:<br>
	<ul>
	<li>Point One
	<li>Point Two
	<li>Point Three
	</ul>
<footer>
  <p>&copy; 2023 My Demo. All rights reserved.</p>
  <nav>
    <ul>
      <li><a href="/about">About</a></li>
      <li><a href="/contact">Contact</a></li>
      <li><a href="/privacy">Privacy Policy</a></li>
    </ul>
  </nav>
</footer>
</div>
</body>
</html>
```

Additionally, HTML allows for the inclusion of multimedia content like images and videos. It also lets you integrate other web technologies such as CSS (Cascading Style Sheets) for styling, and JavaScript for interactivity.

Here's an example code snippet showing an image and a video being incorporated into a web page.

```
<img src="test_image.png" width="800" alt="A test image">
<hr>

<div class="video-container">
  <video controls>
    <source src="sample_video.mkv" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>
```

HTML documents are interpreted by web browsers, which render the structured content and present it to users. It enables browsers to understand the hierarchy, relationships, and presentation of elements on a webpage. It ensures that everything displays as intended and that there's appropriate interactivity.

In this guide, we're going to explore the core HTML elements, including document structure, external links, embedded media, and simple forms. And we're going to do all that by actually creating stuff. No more boring slides.

## Understanding HTML Page Structure

Ok. The basic structure of an HTML document, sometimes described as the HTML skeleton, provides a foundation for creating web pages. It consists of several essential elements that establish the structure and define the content of the page. 

When I right-click on a page, I can select the View Page Source option and I'll find myself looking at the HTML source code.

Well begin at the top. The Document Type Declaration (<!DOCTYPE>) is placed at the very beginning of an HTML document to specify the HTML version being used. It ensures that the browser interprets the page correctly.

The HTML tag is the root element of an HTML document. It encloses the entire content of the page and serves as a container for all other HTML elements. 

If you scroll all the way to the bottom of a page, you'll see a _closing_ tag like this: `</html>`.

### What's in the <head> section of your HTML code?

The head tag contains metadata and other non-visible information about the web page. It can include elements such as the page title, character encoding, linked stylesheets, and JavaScript files. The content within the head tag is not directly visible to users who load the page.

The _characterset_ tag in this case uses **UTF-8**. What's that all about? HTML character encoding refers to the method used to represent and display characters, symbols, and special characters within an HTML document. 

Here's how all that might look:

```
<!DOCTYPE html>
<html>
<head>
	<title>My Demo</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
```

Since HTML is a text-based markup language, it needs a standardized way to represent characters beyond the basic alphanumeric set of uppercase A-Z, lowercase a-z, and the numbers 0-9. 

When using UTF-8 encoding, characters [outside the ASCII range](https://www.freecodecamp.org/news/get-the-ascii-value-of-any-character-with-one-line-of-code/) are represented using multiple bytes. For example, a basic Latin character like "A" is represented by a single byte (0x41), while certain non-Latin characters may require two or more bytes.

The `<head>` section can also contain style information that could just as easily have been placed in an accompanying CSS file. Here's how that might look:

```
<style>
  .video-container {
    width: 500px; /* Set the desired width */
  }
</style>
```

The body tag represents the _visible_ content of the web page. It contains all the elements that will be displayed on the screen, such as text, images, headings, paragraphs, and links. The content within the body tag is what users see when they visit the page.

Heading tags, like h1, h2, and so on, are used to define the headings or titles of sections within the body of the page. The h1 tag represents the main heading, followed by h2 for subheadings, h3 for sub-subheadings, and so on.

Paragraph tags, `<p>`, define blocks of text or content within the body of the page. They create separate paragraphs and are commonly used for structuring textual content.

```
<p>Here is some new text:</p>
```

## Understanding Semantic Tags

Finally, **HTML5** introduced a set of semantic tags that provide more meaningful and descriptive structure to the content. These tags include header, nav, section, article, aside, and footer. 

Even though they don't always have any direct impact on the way a page will display in your browser, semantic tags help with organization and make it easier for us to understand the purpose of different sections of the page.

A tag that begins with an exclamation mark is actually used for comments that won't be visible to your users and that have no impact on the way browsers read the page. Here's an example:

```
<!-- Here's a comment that's just for developers' eyes. -->
```

The goal of comment tags is to help us remember the purpose and function of various code sections. It's all about documenting your code.

In fact, "readability" is an important feature of _all_ well-written HTML code. Each of the elements we've seen here – whether controlling metadata, styles, scripts, navigation, or plain text – can, when presented intelligently, contribute to the value of both the page seen by your users and of the code itself.

_This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)_

