---
title: What is a Hyperlink? Definition for HTML Link Beginners
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-30T22:07:57.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-hyperlink-definition-for-html-link-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/bas-van-den-eijkhof-aJfOuWeNzko-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
seo_title: null
seo_desc: 'Links are a defining featute of the Web and you''ll find them everywhere.

  As their name suggests, they create links, or connections, between pages. This allows
  us to navigate quickly and easily from one webpage to another.

  You''ll find many types of li...'
---

Links are a defining featute of the Web and you'll find them everywhere.

As their name suggests, they create links, or connections, between pages. This allows us to navigate quickly and easily from one webpage to another.

You'll find many types of links on the Web.

There are links that go from one website to another. There are links that go from one page of a site to another page of the same site. And there are links that go from one section of a site to another section within the same site.

This article goes over the definition of a hyperlink and how to create a variety of different links in HTML.


## What is a Hyperlink?

A hyperlink, also called a link or web link, contains an address for a destination and acts as a reference to data. A user can easily follow, jump to, and be directed to the destination by either clicking, tapping on, or hovering over the link. 

A hyperlink can be a piece of text, an image, an icon, or a graphic that, when you click on it, points to and navigates you to a different webpage or document. It can also point to a specific section or element within the same webpage or document.

Basically, hyperlinks are clickable pointers to a resource.

For example [this link to freeCodeCamp's homepage](https://www.freecodecamp.org/) is a hyperlink. When you click on the underlined text, the browser leaves this current page and redirects you there instead.

Each Google search result is a hyperlink. When you click on one of them, you leave the search page and go to the result. 

Without hyperlinks, you would need to know each and every URL (Uniform Resource Locator) of every webpage on the Internet in order to visit them.

## Hyperlinks and HTML

A hyperlink is an element in an HTML document. 

Hypertext is text with hyperlinks. The linked text (the reference to data) is called **anchor text**. 

You use **anchor tags** to create hyperlinks to other webpages. They create links: a clickable text or image that, when clicked, takes us to a new page or to a different part of the same page.

HTML consists of hyperlinks. They are an essential and defining feature of the World Wide Web, and they're what has made the Web so successful. They enabled the very idea of browsing. 

They give us the ability to connect a document to another document across different computers and networks. 

The idea initially originated from scolarly referencing and footnotes in scientific documents, but this lead to the discoverability of other people's websites as time went on.

Users could click between the pages of not only one author's website, but through to other authors' websites and move from one webpage to another. Anything could link to anything else, making navigating to different places on the Web easy. And this provided users with wider access to information.

The World Wide Web is made up of trillions of hyperlinks linking trillions of webpages to each other, creating something that could resemble a very large spider web.


## How to Create an HTML Link

You create links with the  `<a>`  inline element, where "a" stands for *anchor* tag.

Here's an example of an HTML link tag:

```html
<a href="https://www.freecodecamp.org/"> freeCodeCamp Home Page </a>
```

Let's break it down:

- The link element has an opening `<a>` and closing `</a>` tag.
- The text the users see and can click on is between the opening and closing `a` tags – in this case `freeCodeCamp Home Page`. It's called *link text* and it should be descriptive of where the link goes.
- On the opening tag, `<a>`, an `href` *attribute* is added, which is short for `hypertext reference`. The value of the `href` attribute specifies the desired URL you want the link to take users to when the link text is clicked.
- Don't forget the equals sign `=` and quotation marks `""` that go along with the `href` attribute.

Hyperlinks by default look different than regular plain text. This is done for usability purposes and to let users know that this is indeed a link.

By default, the text will have a blue color with an underline. You can change this, however, by adding different CSS styles.

On a computer, when you hover over a link, the pointer changes from an arrow into a hand to indicate something is clickable.

This type of hyperlink in the example above links to other sites. It's an external link, used to connect two pages from two completely different websites.

In this case, the value of `href` is an **absolute** URL – that is a full web address of the site with its domain name.

## How to Link to a Different Page within a Site

Internal links are links that direct the user to different pages of the same site. They don't point to external sites.

In such cases,the `href` attribute has a **relative** URL.

For example:

```html
<nav>
    <ul>
        <li><a href="about.html">  About  </a> </li>
        <li><a href="posts.html">   Blog Posts </a> </li>
        <li><a href="projects.html"> My projects </a>< /li>
        <li><a href="contact.html">  Contact Me  </a> </li>
    </ul>
</nav>

```

In the above example we created a navigation that contains links to different pages of the same site. They point to the "About" page, the "Blog Posts" page, the "My projects" page, and the "Contact Me" page, respectively.

We don't need to specify the domain name and full URL in the `href` attribute in this case, as these files are *relative* to our project and current working directory. 

In this case all files are in the same folder and have the same hierarchical  structure, so writing just the name of the file is enough.

## How to Create a Link to a Specific Section of a Site

What about when we want a link to jump to a specific part of the page?

Maybe you mentioned a topic and want to refer readers to a section later on in the page where you talk about it in more detail.

We can create links that connect content on the same page.

First, go to the section you want the link to go to, and in the opening tag add an `id` attribute.

For example maybe we have a paragraph we want to reference:

```html
<p id="extra-info"> Best cities to visit </p>
```

Then in your link, append a `#` and the value you gave the `id` attribute, in this case `extra-info`:

```html
<a href="#extra-info"> Read more information about cities to visit here </a>
```

## How to Open a Link in a New Tab

When a link points to an external site, it is good practice to make it open in a separate tab. We don't want to lose our site's visitors.

By default the browser opens links in the same tab.

We can change this link:

```html
<a href= "https://www.freecodecamp.org/"> freeCodeCamp Home Page </a>
```

To this one:

```html
<a href= "https://www.freecodecamp.org/" target="_blank"> freeCodeCamp Home Page </a>
```

You add the `target` attribute to the opening `<a>` tag, and give it the value `_blank` which opens links in a new tab.


## How to Create Email Links

Links can do other actions aside from just linking to another page or website.

For example, there are links that pop up and open the default email program and start a new email to a specified address.

```html
<a href="mailto:hellothere@gmail.com">Email Me!</a>
```

This time the `href` attribute starts with `mailto:` and then the email address you want to send a message to.

The link by default doesn't look any different than the other links we've talked about here. But when it's clicked on, it automatically starts to  compose a new email with the user's default email client. 

When that happens, the `to` field is already filled out with the email address of where you want to send it to.

## Conclusion

In this article, we went over the definition of a hyperlink and why they are such an important part of the Web.

We also learned how to create different types of links in HTML.

Thanks for reading and happy coding!



