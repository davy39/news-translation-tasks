---
title: Meta Tag in HTML – What is Metadata and Meta Description Example
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-04T18:52:11.000Z'
originalURL: https://freecodecamp.org/news/meta-tag-in-html-what-is-metadata-and-meta-description-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/nathan-da-silva-k-rKfqSm4L4-unsplash.jpg
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In this article, you''ll learn what meta tags are in HTML and how to use
  them. Then we''ll go over some of the most important meta tags that you need to
  include in every new HTML project.

  Let''s get started!

  How to set up an HTML project

  When setting up...'
---

In this article, you'll learn what `meta` tags are in HTML and how to use them. Then we'll go over some of the most important `meta` tags that you need to include in every new HTML project.

Let's get started!

## How to set up an HTML project

When setting up new HTML projects, you'll find that you have to include the same few tags every single time.

These tags are essential, and you'll need them to get your HTML site up and running properly, following best practices.

Some code editors offer shortcuts to automatically fill out and enter the tags that you use in every new HTML project. This can save you considerable time.

In the [Visual Studio Code editor](https://code.visualstudio.com/download), you can do this in the following way:

1) Make sure you've created a file ending in `.html` - here you'll write all of your HTML code.
2) Inside the empty file type an exclamation mark, `!`.

![Screenshot-2021-12-23-at-12.34.11-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-23-at-12.34.11-PM.png)

3) Click on the exclamation mark with the mention that the following is an Emmet Abbreviation.

[Emmet](https://emmet.io/) is a plugin for code editors that's built into Visual Studio Code by default, and it helps you optimise your HTML workflow.

You'll then see the following code filled out:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

When viewing the `.html` file in the browser of your choice, you'll see just an empty page.

Le'ts zoom in to the following section of the code that was created:


```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
```

What are these `meta` tags exactly? Why are they there and what purpose do they serve when creating a webpage?

This article will focus on explaining the basics of  `meta` tags and why they are used in HTML documents.


## What are `meta` tags in HTML?

`meta` tags live within the `head` tag of the HTML document.

The `head` tag is used for configurating the HTML file.

You use the `head` tag to add a title to the webpage, link to a CSS stylesheet, and define more information about the HTML document.

`meta` tags represent metadata. They are essentially used for defining and describing data about data, and are used to add extra information to the data inside the webpage.

There are many `meta` tags. Some of them help improve the SEO (Search Engine Optimisation) of your website, making sure that the content of your site is relevant to what people are searching for.

### How to define the character set of a website

`<meta charset="UTF-8">` defines the character set that will be used in the site.

`UTF-8`, which stands for 8-bit Unicode Transformation Format, is the standard character encoding used with the latest version of HTML, which is HTML5.

This line should be included in every single webpage created, as it ensures that every character from every language in the world is displayed properly in every browser.

By using the universal `UTF-8` as the character set, characters from non-latin languages will not be distorted.

The Google Chrome browser has automatically set the encoding to `UTF-8`, so you won't have to worry about that when designing for this browser. But you still need to include  `<meta charset="UTF-8">` in every HTML file in case this feature is not supported by other browsers.

For example, look at what happens in the Safari browser when this line is not added and I write a heading in a non-latin language, such as Greek:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Γεία σου κόσμε!</h1> <!-- Hello world! -->
</body>
</html>
```

![Screenshot-2021-12-23-at-6.47.05-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-23-at-6.47.05-PM.png)

When the HTML document is viewed in the browser, all the characters are distorted.

### How to let Microsoft's Internet Explorer know which rendering view to use

You use the `http-equiv="X-UA-Compatible" content="IE=edge"` meta tag to choose and define the version of Internet Explorer in which the web page will be renedered. 

Always choose the latest one, which is `IE=edge`.

There are many versions of Microsoft's browser. In the past the different advances caused headaches to web designers and web developers alike, who worked on making sure websites were usable on legacy browsers.

This tag will ensure that the website will not be rendered as an older version of Internet Explorer, which tend to be buggy.

### How to adjust viewport settings

Nowadays, it is important that all sites look good on all devices, especially mobile phones.

So, you need to include the `meta name="viewport" content="width=device-width, initial-scale=1.0"` tag in every HTML file.

`viewport` refers to how the site is displayed on different screen sizes, and how much visual area a user has available.

Each device has a different viewport. For example, mobile devices have a smaller one and desktop computers have a larger one.

`content="width=device-width` is the first step to making sure that websites look good on mobile devices. 

It prevents a site that is viewed from a mobile device from looking like it would on a laptop – that is small and far away zoomed out.

This ensures that the HTML will adjust to the width of the device's screen.

`initial-scale=1.0` sets how the webpage scales,and sets the initial zoom when the page is first loaded by the browser.

## Additional `meta` tags to add to your HTML project

### How to add a description of your webpage

Using a meta description tag for your page helps search engines figure out and rank your website against other websites. It's used primaraly for SEO (Search Engine Optimization) purposes.

The meta description tag is used to explain in a brief and concise way what your website is about.

A meta description tag could look something like this:

```html
 <meta name="description" content="Our mission: to help people learn to code for free. We accomplish this by creating thousands of videos, articles, and interactive coding lessons - all freely available to the public.">
```

You use the `name` and `content` attributes, with the text value passed to `content` showing up in the search results:

![Screenshot-2021-12-26-at-3.23.14-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-at-3.23.14-PM.jpeg)

#### Things to consider when writing a description of your website

- Make sure to keep the description of your website short and not over 160 characters.
- Include useful keywords and key-phrases that people tend to use often when searching for the services that your website provides.
- Explain clearly what your website does and the mission behind it. It is important to get across what sets you apart and the value you provide.
- Be consistent with the voice and tone of your brand.
- Most importantly, stick to describing the content your website actually provides. Don't try and trick your readers by only aiming to appear high in searches and rankings.

### How to add the name of the website's author

Another useful `meta` element to include is the author's name.

This could look like the following:

```html
<meta name="author" content="Quincy Larson">
```

It can be helpful to know who authored the page. 

This info shares who created and built the website, who authored the content, or to whom the copyright belongs.

## Conclusion

To summarise, all HTML documents need to include at least the following three `meta` tags:

- `<meta charset="UTF-8">`, to specify the character set.
- `<meta name="description>"`, to add a clear description of the site and the services the site provides to readers/customers.
- `<meta name="viewport>`, which is the first step sites need to take to be usable on a variety of screen devices.

To learn more about HTML and CSS, check out the [Responsive Web Design Certification](https://www.freecodecamp.org/learn/2022/responsive-web-design/) by freeCodeCamp, where you'll learn in an interactive way while building fun projects along the way.

Thanks for reading and happy coding!



