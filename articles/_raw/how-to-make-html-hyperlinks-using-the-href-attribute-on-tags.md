---
title: How to Make HTML Hyperlinks Using the HREF Attribute on Tags
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-21T11:15:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-html-hyperlinks-using-the-href-attribute-on-tags
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/coverfcc.png
tags:
- name: HTML
  slug: html
seo_title: null
seo_desc: "By Ibrahima Ndaw\nA website is a collection of web pages. And these pages\
  \ need to be linked or connected by something. And to do so, we need to use a tag\
  \ provided by HTML: the a tag. \nThis tag defines a hyperlink, which is used to\
  \ link from one page t..."
---

By Ibrahima Ndaw

A website is a collection of web pages. And these pages need to be linked or connected by something. And to do so, we need to use a tag provided by HTML: the `a` tag. 

This tag defines a hyperlink, which is used to link from one page to another. And the most important attribute of the `a` element is the `href` attribute, which indicates the link's destination.

In this guide, I will show you how to make HTML hyperlinks using the `href` attribute on the `a` tag.

* [What is a link?](#heading-what-is-a-link)
* [How to create internal links](#heading-how-to-create-internal-links)
* [Browse to pages on the same level](#heading-browse-to-pages-on-the-same-level)
* [Browse to pages located on another folder](#browse-to-pages-located-on-another-folder)
* [Browse from a page located in a folder to the root](#heading-browse-from-a-page-located-in-a-folder-to-the-root)
* [How to create external links](#heading-how-to-create-external-links)
* [How to create anchor links](#heading-how-to-create-anchor-links)
* [Navigate on the same page](#heading-navigate-on-the-same-page)
* [Navigate on another page](#heading-navigate-on-another-page)
* [Conclusion](#heading-conclusion)

## What is a link?

A link is clickable text that allows you to browse from one page to another, or to a different part of the same page. 

In web development, there are several ways to create links, but the most common is by using the `a` tag and the `href` attribute. This last is where we specify the destination address of the link.

The `a` tag helps us create three main kinds of links: an internal link, an external link, and an anchor link. That said, we can now dive into how to create an internal link in the next section.

## How to create internal links

When it comes to building a website, it makes sense to have a connection between pages. And as long as these links allow us to navigate from page A to page B, it's called an internal link (since it's always in the same domain name or on the same website). So, an internal link is a link that allows navigating to another page on a website.

Now, considering our folder is structured as follows:

```
├── folder1
|  └── page2.html
├── page1.html
├── index.html

```

Here we have three use cases, and for each, we will create an example.

### Browse to pages on the same level

* `index.html`

```html
<a href="page1.html">Browse to Page 1</a>

```

As you can see, the page `page1.html` is on the same level, therefore the path of the `href` attribute is just the name of the page.

### Browse to pages located in another folder

* `page1.html`

```html
<a href="./folder1/page2.html">Browse to Page 2</a>

```

Here, we have a different use case since the page we want to visit is now not on the same level. And to be able to navigate to that page, we should specify the complete path of the file including the folder.

Great! Let's now dive into the last use case.

### Browse from a page located in a folder to the root

* `page2.html`

```html
<a href="../index.html">Browse to the Home Page</a>

```

Now, here to navigate to the `index.html` page, we should first go one level up before being able to browse to that page.

We have now covered internal links, so let's move on and introduce how to navigate to external links.

## How to create external links

It's always useful to have the ability to navigate to external websites as well.

```html
<a href="https://www.google.com/">Browse to Google</a>

```

As you can see here, to navigate to Google, we have to specify its URL to the `href` attribute.

External and internal links are used to navigate from page A to page B. However, sometimes we want to stay on the same page and navigate to a specific part. And to do so, we have to use something called anchor link, let's dive into it in the next section.

## How to create anchor links

An anchor link is a bit more specific: it allows us to navigate from point A to point B while remaining on the same page. It can also be used to go to a part on another page.

### Navigate on the same page

```html
<a href="#about">Go to the anchor</a>
<h1 id="about"></h1>

```

Compared to the others, this one is a bit different. Indeed it is, but it still works the same way.

Here, instead of a page link, we have a reference to an element. When we click on the link, it will look for an element with the same name without the hashtag (`about`). If it finds that id, it browses to that part.

### Navigate on another page

```html
<a href="page1.html#about">Go to the anchor</a>

```

This is pretty the same as the previous example, except that we have to define the page in which we want to browse and add the anchor to it.

## Conclusion

The `href` is the most important attribute of the `a` tag. It allows us to navigate between pages or just a specific part of a page. Hopefully, this guide will help you build a website with plenty of links.

Thanks for reading.

_Feel free to reach out to me!_

[TWITTER](https://twitter.com/ibrahima92_)   [BLOG](https://www.ibrahima-ndaw.com/)  [NEWSLETTER](https://ibrahima-ndaw.us5.list-manage.com/subscribe?u=8dedf5d07c7326802dd81a866&id=5d7bcd5b75)  [GITHUB](https://github.com/ibrahima92)  [LINKEDIN](https://www.linkedin.com/in/ibrahima-ndaw/)  [CODEPEN](https://codepen.io/ibrahima92)  [DEV](https://dev.to/ibrahima92)

Photo by [JJ Ying](https://unsplash.com/@jjying?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/link?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

