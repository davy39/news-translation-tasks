---
title: What is HTML – Definition and Meaning of Hypertext Markup Language
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-24T16:38:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-html-definition-and-meaning
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/html.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: markup
  slug: markup
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "HTML, or Hypertext Markup Language, is a markup language for the web that\
  \ defines the structure of web pages. \nIt is one of the most basic building blocks\
  \ of every website, so it's crucial to learn if you want to have a career in web\
  \ development. \nIn..."
---

HTML, or Hypertext Markup Language, is a markup language for the web that defines the structure of web pages. 

It is one of the most basic building blocks of every website, so it's crucial to learn if you want to have a career in web development. 

In this article, I will walk you through what HTML is about in detail, how it does things on web pages, and we'll also touch on a really cool part of HTML – Semantic HTML.

## What is HTML?

To understand "HTML" from front to back, let's look at each word that makes up the abbreviation: 

**Hypertext**: text (often with embeds such as images, too) that is organized in order to connect related items

**Markup**: a style guide for typesetting anything to be printed in hardcopy or soft copy format

**Language**: a language that a computer system understands and uses to interpret commands.

HTML determines the structure of web pages. This structure alone is not enough to make a web page look good and interactive. So you'll use assisted technologies such as CSS and JavaScript to make your HTML beautiful and add interactivity, respectively. 

In this case, I like to break down the three technologies – HTML, CSS, and JavaScript – this way: they are like a human body. 

* HTML is the skeleton, 
* CSS is the skin, 
* and JavaScript is the circulatory, digestive, and respiratory systems that brings the structure and the skin to life.

You can also look at HTML, CSS, and JavaScript this way: HTML is the structure of a house, CSS is the interior and exterior decor, and JavaScript is the electricity, water system, and many other functional features that make the house livable.

## HTML Tags

Since HTML defines the markup for a particular web page, you'll want the text, images, or other embeds to appear in certain ways. 

For example, you might want some text to be big, other text to be small, and some to be bold, italic, or in bullet point form. 

HTML has "tags" that let you get this done. So, there are tags to create headings, paragraphs, bolded words, italicized words, and more.

The image below describes the anatomy of an HTML tag:

![anatomy-of-an-html-tag](https://www.freecodecamp.org/news/content/images/2021/08/anatomy-of-an-html-tag.png)


## HTML Elements

An element consists of the opening tag, a character, the content, and a closing tag. Some elements are empty – that is, they don't have a closing tag but instead have a source or link to content that you want to embed on the web page. 

An example of an empty element is `<img>`, which you use to embed images on a web page.

HTML elements are often used interchangeably with tags, but there's a small difference between the two. An element is a combination of the opening and closing tag, and then the content between them.

I made another image to help you visualize the anatomy of an HTML element:

![anatomy-of-an-html-element](https://www.freecodecamp.org/news/content/images/2021/08/anatomy-of-an-html-element.png)

## HTML Attributes
 
HTML tags also take what are called attributes. These attributes are placed in the opening tag and range from style and ids to classes. They take values, which convey more information about the element and help you do things such as styling and manipulation with JavaScript.

In the infographic below, the opening tag contains a `class` attribute with a value of `“text”`. This can be used to style the element or select it with JavaScript for interactivity.

![attribute-1](https://www.freecodecamp.org/news/content/images/2021/08/attribute-1.png)

Here's the anatomy of a basic HTML page:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Definition of HTML</title>
  </head>
  <body>
    <!--Page content such as text and images goes in here-->
  </body>
</html>
```

Let's look at the important bits of code here:

`<!Doctype html>`: Specifies that we're using HTML5 in this code. Before the introduction of HTML5, you had to explicitly state which version of HTML you were coding in with the `<!Doctype>` tag. For example, HTML4.0, 3.2, and so on. But now we no longer need it. When “html” is written in the code, the browser automatically assumes that you are coding in HTML5.

`<html></html>`: the root, or top-level element of every HTML document. Every other element must be wrapped in it.

`<head></head>`: one of the most crucial parts of the HTML document. Web crawlers look inside the head tags to get important information about the page. It contains info such as the page title, stylesheets, meta information for SEO, and lots more.

`<meta />`: this is an empty element that conveys meta-information about the page. Such information may include the author, what type of encoding it's using (almost always UTF-8), responsiveness, compatibility, and a lot more. Web crawlers always look at the meta tag to get information about the web page, which will play a crucial role in SEO.

`<title></title>`: this defines the title of the web page. It is always shown in the browser tab.

`<body></body>`: all the content of the HTML document is located inside the body tag. There can only be one `<body>` tag on the whole page.
  
## What is Semantic HTML?

Semantic HTML means that your HTML tags convey the actual meaning of what they are used for. 

Semantics has been an integral part of HTML since its inception in the early 90s. But it never gained particular relevance until the late 90s when CSS started working in most browsers. 

With semantic HTML, semantically-neutral tags such as `<div>` and `<span>` are frowned upon since semantically more descriptive tags such as `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>` and `<article>` can do the same thing they do.

A noticeable advantage of using semantic tags is that web crawlers are able to index the web page or website easily, improving SEO in return. 

In addition, a website that uses semantics becomes more informative, adaptable, and accessible to those who use screen readers to access websites. 

### Important Semantic Tags and What they Do 

Let's look at some of the most commonly used semantic HTML tags:

`<header>`: The `<header>` element defines the introductory section of a web page. It contains items such as the logo, navigation, theme switcher, and search bar.

`<nav>`: The `<nav>` element specifies the navigation items of the page such as home, contact, about, FAQs, and so on.

`<main>`: The `<main>` element is conventionally treated as the immediate descendant of the <body> tag. It contains the main sections of the HTML document apart from `<header>` and `<footer>`. Ideally, there should be just one of these in the whole HTML document.
    
`<section>`: The `<section>` element defines a particular section of the web page. This may be the showcase section, about section, contact section, or others. You can use numerous sections in a single HTML document.
 
`<article>`: The `<article>` element represents a certain part of a web page that conveys some particular information. Such information could be a combination of text, images, videos, and embeds. Look at this element as a standalone blog post on a page containing excerpts about other blog posts.

`<aside>`: As the name implies, this represents a sidebar on a web page. It is usually a part of the web page that is not directly related to the main content.

`<footer>`: The `<footer>` element accommodates items such as quick links, copyright information, or any other data related to the entire website or web page.

Note that since semantic elements convey actual meaning and what some particular content actually does (such as `nav` for navigation, `aside` for a sidebar, and so on), these elements are not automatically positioned where they are supposed to be. You still have to do that with CSS. 

A super simple semantic HTML document looks like this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Definition of HTML</title>
  </head>

  <body>
    <header>
      <h1 class="logo">LOGO</h1>
      <nav>
        <ul>
          <li>Home</li>
          <li>About</li>
          <li>Contact</li>
          <li>FAQs</li>
        </ul>
      </nav>
    </header>
    <main>
      <section class="about-me">
        <article>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Optio magni
          est asperiores nemo, adipisci minus itaque quam, rem libero aliquam
          nesciunt, nisi inventore assumenda earum repellat labore ratione
          architecto eos quis. Soluta mollitia cupiditate dolorem. Consequatur a
          soluta laudantium nihil. Molestias, officiis ut! Nobis adipisci
          voluptatem quam at officia beatae!
        </article>
      </section>
      <section class="contact-me">
        You can find me on
        <a href="https://twitter.com/koladechris">Twitter</a> You can find me on
        <a href="https://Instagram.com/koladechris">Instagram</a>
      </section>
      <aside class="address">My Address</aside>
    </main>
    <footer>© 2020 All Rights Reserved</footer>
  </body>
</html>
```
Here's what it looks like in the browser:

![semanticHTML-4](https://www.freecodecamp.org/news/content/images/2021/08/semanticHTML-4.png)

You can see that the content inside the `<aside>` tag isn't in the sidebar and the content inside the `<nav>` tag is not automatically available as the navigation bar. This is why you still have to make them look the way they are supposed to look with CSS.

## Conclusion 

I hope this article has helped you learn the basics of HTML and what it does. Now you can start to learn more advanced technologies such as CSS and JavaScript, and then start forming a solid career in web development. 

Thanks a lot for reading and have a nice time.



