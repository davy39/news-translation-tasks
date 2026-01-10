---
title: HTML Link – How to Insert a Link to a Website with HREF Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-01T18:22:00.000Z'
originalURL: https://freecodecamp.org/news/html-link-code-how-to-insert-a-link-to-a-website-with-href-3
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd76c26e6787e098393e8a7.jpg
tags:
- name: HTML
  slug: html
- name: Website design
  slug: website-design
seo_title: null
seo_desc: "By Dillion Megida\nA website is made up of of various pieces of information\
  \ that live in different sections and on different pages within the site itself.\
  \ \nYou can also find information relating to that site on pages that are on different\
  \ websites. \nA..."
---

By Dillion Megida

A website is made up of of various pieces of information that live in different sections and on different pages within the site itself. 

You can also find information relating to that site on pages that are on different websites. 

All these sections and pages are linked together in HTML using the `href` attribute.

In this article, we'll look at the term *Hyperlink*. Then we'll learn about the different ways you can create hyperlinks, what `href` does, and how to appropriately use the `href` attribute to link sections and pages.

## What are Hyperlinks?

In HTML, there are various forms of links. In images, there is the `src` attribute to "link" the source of an image. 

For stylesheets, there is the `link` tag with the `href` attribute to "link" the source of a stylesheet. 

For anchor tags, there is the `href` attribute to "link" the referenced section or page. Anchor links are also called hyperlinks.

When a user follows a hyperlink, they are navigating to that page. Hyperlinks are elements that reference another document, such that when a user clicks on that element, they are directed to the new document.

## When to Use Hyperlinks

As stated above, you may want to link various pages (within your website or externally) or sections on your website. 

In this article, I'll highlight three ways of creating hyperlinks. These different ways are important to know because they determine the values of the `href` attribute. 

Alright, let's look at those three different ways now.

### 1. When you want to link to sections of a page

You might use this method, for example, when you're creating a page with a table of contents.

In this case, you may not want your readers to have to scroll down to the last section. It would be nice if they could just click on it in the table of contents and the browser would take them there directly. 

This type of linking occurs in the same document, and just takes the reader to different sections. We'll learn how to create a hyperlink for this use case when we learn about the `href` attribute.

### 2. When you want to link to another page within a website

On your site, you might have a home page, about page, services page, and other types of pages. This method helps users navigate from one page to another.

### 3. When you want to link to external pages

Sometimes, your website may not contain certain information and another website may have it. In such cases, you might want to reference the other website. 

To do this, you would create an external hyperlink that navigates the user to the other website.

These are the three major ways of linking pages. Let's now see how the `href` attribute can help you enable them.

## How to Use the `href` Attribute

The `href` is an attribute used to reference another document. You can find it on `link` tags and `anchor` tags.

The `href` attribute is used on anchor tags (`a`) to create hyperlinks in websites. The value of the attribute contains the URL which the hyperlink points to. You can use it like this:

```html
<a href="URL">Hyperlink</a>
```

However, the URL values can be different depending on what you're pointing to. For the three ways we looked at earlier, let's see how you can use `href`.

### 1. How to use `href` to link sections within a document

In this case, the value will be the `id` of the element that starts the section. That means we will have something like this:

```html
<a href="#second-section">Go to second section</a>
<!--
  Some stuffs here
 -->
<section id="second-section">
	<h2>Second section</h2>
</section>
```

When the "Go to second section" hyperlink is clicked, the browser scrolls down to the section with the associated `id`. Also the URL in the URL bar of the browser changes. 

For example, if the previous URL was `mywebsite.com`, the new URL will be `mywebsite.com#second-option`.

### 2. How to use `href` to link pages within a website

To use `href` this way, you need to understand what Relative URLs and Absolute URLs are.

Relative URLs are short URLs that point to a document on the same website. It's more like, from where you are, how do you get to this other place on the same website? 

This is in contrast to Absolute URLs. For these, you aren't concerned with where you currently are – you provide the full details to get to another place like you were starting from the beginning.

For navigations between pages that live on a website, you can use any of these URLs, but Relative URLs are commonly used.

Say you're on the home page, and you want to reference the about page. Here's how to use the `href` attribute to do that:

```html
<a href='/about' >About page</a>
```

From the homepage (say `mywebsite.com`), the above link will navigate to `mywebsite.com/about`.

There's something worth noting about the slash (`/`) before the link. The `/` tells the browser to append the link to the root of the site (which is the domain). So the root is `mywebsite.com` and the link is appended like so: `mywebsite.com/about`.

If the slash was absent (`<a href='about'>`), the browser would replace the current path with `/about`.

For example, if we were currently on `mywebsite.com/projects/generator`, and we had the following links:

```html
<a href='about'>About 1</a>
<a href='/about'>About 2</a>
```

"About 1" would navigate to `mywebsite.com/projects/about` (replacing the current path `/generator`) and "About 2" would navigate to `mywebsite.com/about`

### 3. How to use `href` to link to pages on another website

Since it's on a different website, there's no way we can use Relative URLs. For this, we need to specify the absolute source of the document we are referencing.

For example, say we're on `mywebsite.com`, and we want to reference `google.com`, this is how we'd do it with `href`:

```html
<a href='https://google.com'>Google<a>
```

If we had only written `google.com`, the browser would treat it as a page within a website, thereby appending it to `mywebsite.com`.

## Conclusion

In this article, we've seen how the `href` attribute allows us to create different types of links. These various links show the different ways that documents/pages can be referenced within a website.

