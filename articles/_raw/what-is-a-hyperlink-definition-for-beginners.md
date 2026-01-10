---
title: What is a Hyperlink? HTML Links Explained with Examples
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-08-16T23:33:49.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-hyperlink-definition-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/uide-to-writting-a-good-readme-file--3--1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Let's begin with a quick question: How did you land on this article and\
  \ this site today? \nWell, quite literally, by clicking or tapping on a link, right?\
  \ That's how powerful this element is – it will get you to any part of the Internet\
  \ just by clicki..."
---

Let's begin with a quick question: How did you land on this article and this site today? 

Well, quite literally, by clicking or tapping on a link, right? That's how powerful this element is – it will get you to any part of the Internet just by clicking on a link.

So, what are links and hyperlinks in HTML? 

## What are Links and Hyperlinks in HTML?
A link is a chain that connects pages both within a website and to other websites. Without links, we wouldn't have any websites. 

For example, let's have a look at this URL, `https://www.freecodecamp.org/`. When you type it in the address bar it will take you to the official freeCodeCamp site. 

In simpler terms we can say that links are just the web addresses of web page that allow you to connect with different servers.

Perhaps you are wondering, then, what a Hyperlink might be? Well, they are what allows us to link documents to other documents or resources via refrences called <mark>anchor tags</mark>. They are a fundamental concept behind the World Wide Web which makes navigation between web pages easier via links. 

Hyperlinks can be presented in different forms, like an image, icon, text, or any type of visible element that, when clicked, redirects you to a specified url.

For example, if you were to click [HERE](https://www.freecodecamp.org/news/author/larymak/), you will land in my profile with a list of my other articles. That's a hyperlink.


## How to Create Links in HTML

### How to use `<a>` links 
You can create a basic link by wrapping the text (or any other related content) in the `<a></a>` element and using the `href` attribute which contains the address. 

Here's an example in action: 
```html
<a href="https://www.freecodecamp.org">Visit: Freecode Camp!</a>
``` 

### How to style links 
There are usually links inserted in the `.html` file that link the main to the styling and funtionality file. And they're typically named with the `.css` and `.js` file extensions.

Here's how to link to a CSS file:

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
``` 

And here's how to link to a JS file. You can either place what you want linked in the head or body tag.

```html
<!DOCTYPE html>
<html>
<head>
  <script src="myScript.js"></script>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

## How to Link Within a Site
### Links to different page within a Site
You use this type of link to direct a user to different pages on the same site. 

Take a case where your site has 5 pages. You'll want a user to be able to access all the pages from one point, like the navbar. 

First you will have to create all the pages and then link them. In this case we will do it like this:

```html 
<nav>
    <ul>
        <li><a href="home.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="pricing.html">Pricing</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>
</nav>
``` 

The above example will link to different parts of the site – the 'Home' page, 'Services', 'Pricing', and 'About', in that order. Writing only the name of the file is enough because all the work is shared in the same work folder.

### How to Link to a specific section of a site

Let's say that, somewhere on your site, you mentioned a particular topic or page. And you would like your readers or visitors to jump straight to that section with a click.

First you will have to add the `id` attribute to that section of the page. Maybe it is a paragraph – if so, this is how it would look:

```html
<p id="detailed-info"> Read more on Upcoming Events </p>
``` 
After this in your link add the `id` in the `href`:
```html
<a href="#detailed-info"> Read more about upcoming events </a>
``` 

This code will take them right to the Upcoming Events section.

## Other Types of Links in HTML

### How to Link to a Downloadable file

When you want to link to a resource that a user needs to download rather than open in the browser, you can use the `download` attribute. This provides a default save filename. 

The download attribute is great for PDFs, image files, video and audio clips, and other media content that you would like users to save on their computer or mobile device. 

Here's an example with a download link:
```html
<a href="https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"
   download="firefox-latest-64bit-installer.exe">
  Download Latest Firefox for Windows (64-bit) (English, US)
</a>
```

### How to Add E-mail Links

Email Links allow us to create hyperlinks to an email address. You can create these links using the HTML `<a></a>` tag – but in this case, instead of passing a URL, we pass the recipient’s email address. 

You use the `mailto` attribute to specify the email address in your anchor tag. 

for example: 
```html
<a href="mailto:hillarynyk@gmail.com">Send email to Me</a>
```

In addition to the email address, you can provide other information. In fact, any standard mail header fields can be added to the `mailto` URL you provide. The most commonly used are "subject", "cc", and "body". 

Here's an example that includes a cc, bcc, subject, and body: 
```html
<a href="mailto:hillarynyk@gmail.com?cc=larymak4@gmail.com&bcc=larymak8@gmail.com&subject=The%20subject%20of%20the%20email&body=The%20body%20of%20the%20email">
  Send mail with cc, bcc, subject and body
</a>
``` 

## HTML Link Attributes 

HTML links have various attributes that you can use to provide more speicifc information. Here are some of the most commonly used.

1. **href** attribute
The `href` attribute defines the target URL address for an HTML link. It makes the marked word or phrase clickable. The href attribute creates a hyperlink to another web page, and HTML links would not work as intended without it.

2. **target** attribute
The `target` attribute defines where the HTML link will be opened. Ever visited a website and when you click on a link it automatically opens in a new tab? Well that's the work of this attribute. 

Here are all the possible options you can use with the `target` attribute:

* **-blank** => Opens the link in a new tab. Mostly used to avoid losing a site's visitors. By default, when a user clicks a link it opens in the same tab – but this changes that. 
```html
<a href= "https://www.freecodecamp.org/" target="_blank"> freeCodeCamp</a>
```

* **_self** => Loads the URL in the same window or the tab where it was clicked. This is usually the default and does not need to be specified.
```html
<a href="https://www.freecodecamp.org" target="_self">freeCodeCamp</a>
```

* **_parent** => Loads the URL in the parent frame. It’s only used with frames. 
```html
<a href="https://www.freecodecamp.org" target="_parent">freeCodeCamp</a>
```

* **_top** => Loads the linked document in the full body of the window.
```html
<a href="https://www.freecodecamp.org" target="_top">freeCodeCamp</a>
```

3. **title** attribute
The `title` attribute outlines extra information about the link’s purpose. If a user hovers their mouse over the link, a tooltip will appear which describes the objective, title, or any other information about the link: 

```html
<a href="https://www.freecodecamp.org" title="Link to free learning Resources">Learn to code</a>
``` 

## Quick HTML Link Tips and Recap
In this article, we learned all about links and hyperlinks in HTML. Here are some final tips to help you work with links.

Firt, when you're using an image as a link, it's always a good idea to include the `alt` tag with the text. This provides alternative text that's displayed in case the picture doesn't load.

Second, you should practise specifying the language of the document which the anchor is linked to using the `hreflang` attribute.
```html
<a href="https://www.freecodecamp.org" hreflang="en">Freecode Camp</a>
```

The Web is really just a library of hyperlinked documents where the anchor tags act as bridges between related documents. 

We have seen how to use links and how to create them, and why they are important in web development. 

It's time to go practise and perfect your new skill.

Enjoy Coding ❤




