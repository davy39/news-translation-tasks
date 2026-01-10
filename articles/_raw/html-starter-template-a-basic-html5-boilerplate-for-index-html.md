---
title: HTML Starter Template – A Basic HTML5 Boilerplate for index.html
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-25T23:18:46.000Z'
originalURL: https://freecodecamp.org/news/html-starter-template-a-basic-html5-boilerplate-for-index-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pixabay-270404.jpg
tags:
- name: boilerplate
  slug: boilerplate
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: null
seo_desc: "By Dillion Megida\nHTML has different tags, some of which have semantic\
  \ meanings. A basic boilerplate for an HTML file looks like this:\n<!DOCTYPE html>\n\
  <html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\"\
  \ content=\"width=devic..."
---

By Dillion Megida

HTML has different tags, some of which have semantic meanings. A basic boilerplate for an HTML file looks like this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My Website</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>
  <body>
    <main>
        <h1>Welcome to My Website</h1>  
    </main>
	<script src="index.js"></script>
  </body>
</html>
```

In the rest of this article, I'll explain what each part of this boilerplate means.

# HTML Boilerplate Syntax
## DOCTYPE

```html
<!DOCTYPE html>
```

This element is the doctype declaration of the HTML file. `<!DOCTYPE html>` tells the browser to render the HTML codes as HTML5 (as opposed to some other version of HTML). 

This is important, because without this declaration, HTML5 elements like `section`, `article`, and so on may not be rendered correctly.

## html tag

```html
<html lang="en">
    ...
</html>
```

The `html` tag is the root of the HTML document. It houses the `head` tag, the `body` tag, and every other HTML element (except the DOCTYPE) used in your website.

It also has the `lang` attribute, which you can use to specify the language of the text content on a website. The default value is "unknown", so it is recommended that you always specify a language. 

Defining a language helps screen readers read words correctly and helps search engines return language-specific search results.

## head tag

```html
<head>
    ...
</head>
```

The `head` tag houses the metadata of your website. These are visually invisible data to the user, but they provide information about your website's content. Search engines especially use this data to rank your website.

Metadata in the head tag includes meta tags, title tags, link tags, scripts, stylesheets, and more.

## meta tags

```html
<meta ... />
```

The `meta` tag is a metadata element used to add more metadata to your website than the kind that non-meta tags like title provide.

You can use these tags for various purposes:
- adding metadata for social media platforms to create link previews
- adding a description for your website
- adding a character encoding for your website
- and many more.

Search engines, social media platforms, and web services use this metadata to understand the content of your website and determine how to present them to users.

## title tag

```html
<title>My Website</title>
```

The `title` tag is used to specify a title for your website. Your browser uses this to display a title at the title bar:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-07.38.56.png)

This tag also helps search engines show titles for your website on their search results:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-07.44.11.png)

## link tag
You use the `link` tag, as the name implies, to link to another document. Usually, this establishes different kinds of relationships between the current document and a separate document.

```html
<link rel="stylesheet" href="./style.css">
```

For example, as seen in the code block above, we've established a "stylesheet" document relationship with the styles.css file.

The most common use of this tag is to add stylesheets to a document and to also add favicons to a website:

```html
<link rel="icon" href="./favicon.ico" type="image/x-icon">
```

A favicon is a small image close to the title of the webpage, as seen below:


![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-07.38.56-1.png)



## body tag

```html
<body>
    ...
</body>
```

The `body` tag houses the body content of a website, which is visible to users. Although non-visible elements like `style` and `script` can also be added here, most body tags are usually visible.

From headings to paragraphs to media and lots more, those elements are added here. Any element not found here (which could be included in the head tag) will not be shown on the screen.

## main tag

```html
<main>
    ...
</main>
```

The `main` tag specifies the essential content of a website. This would be the content related to the website's title.

For example, a blog post page. The social media sharing on the left, advertisements on the right, header, and footer are minor parts of the web page. The post itself showing the cover image, the title, and post text content is the central part, which would be in the `main` element.

## h1 tag
HTML has different heading elements which are `h1`, `h2`, `h3`, `h4`, `h5` and `h6`. Heading elements are used to describe different sections of a web page. And these elements have an order, with the `h1` being the highest.

You should only have one `h1` element on a webpage as this starts the main section. And then, you have other sections and subsections for which you can use the other heading elements.

Also, note that you shouldn't skip headings. For example, you shouldn't use an `h4` element after using an `h2` element. A good structure could be like this:

```html
<h1>Welcome to my website</h1>

<h2>What do I have to offer</h2>

<h3>1. Financial Benefits</h3>

<h3>2. Society improves</h3>

<h4>a. Improving the tax system</h4>

<h4>b. Providing more refuse dumps</h4>

<h2>Who am I</h2>

<h2>Conclusion</h2>
```

From this code, you can see how the heading levels specify their position in sections and subsections.

# Wrap up
In this piece, we've seen an HTML starter boilerplate and what each tag used in this template means. 

This list of elements is non-exhaustive as many more elements can be found in the head tag and the body tag, with numerous attributes, too.

