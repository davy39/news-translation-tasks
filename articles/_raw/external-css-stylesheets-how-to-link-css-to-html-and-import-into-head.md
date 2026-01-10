---
title: External CSS Stylesheets – How to Link CSS to HTML and Import into Head
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-24T15:44:49.000Z'
originalURL: https://freecodecamp.org/news/external-css-stylesheets-how-to-link-css-to-html-and-import-into-head
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-martin-damboldt-814499.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'It is considered a best practice to have your CSS stylesheets in an external
  file. So how can you link that CSS to your HTML file?

  Linking to an external CSS file is an important part of any HTML page boilerplate.
  And in this article, we''ll learn how...'
---

It is considered a best practice to have your CSS stylesheets in an external file. So how can you link that CSS to your HTML file?

Linking to an external CSS file is an important part of any [HTML page boilerplate](https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/). And in this article, we'll learn how to do it.

## **How to Link a CSS File to an HTML File**

You can link your CSS file to your HTML file by adding a `link` element inside the `head` element of your HTML file, like so:

```html
<!DOCTYPE html>
  <html>
    <head>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
    
    </body>
</html>
```

The `link` element has many uses, and it is important to specify the right attributes so that you can use it to import an external CSS stylesheet. We'll look at some important attributes now.

## **The `rel` attribute**

The first of the two indispensable attributes is the `rel` attribute. You will use this attribute to tell the browser what the relationship is with the imported file.

You'll write `rel="stylesheet"` to tell the browser that you are importing a stylesheet.

## **The `href` attribute**

The second indispensable attribute is the `href` attribute, which specifies the file to import.

A common situation is that the CSS file and the HTML file are in the same folder. In such a case you can write `href="style.css"`.

If the CSS file and the HTML file are in different folders, you need to write the correct path that needs to go from the HTML file to the CSS file.

For example, a common situation is that the CSS file is in a folder that is a sibling to the HTML file, like so:

```
project --- index.html
            css ---------- style.css
```

In this case you would need to write a path like `"css/styles.css"`.

## **The `type` attribute**

```html
<link rel="stylesheet" href="style.css" type="text/css">
```

You use the `type` attribute to define the type of the content you're linking to. For a stylesheet, this would be `text/css`. But since `css` is the only stylesheet language used on the web, it is not only optional, but it is even a best practice not to include it.

## **The `media` attribute**

```html
<link rel="stylesheet" href="style.css" media="screen and (max-width: 600px)">
```

The media attribute is not visible in the example. It's an optional attribute that you can use to specify when to import a certain stylesheet. Its value must be a media type / media query.

This can be useful in case you want to separate the styles for different devices and screen sizes in different files. You would need to import each CSS file with its own `link` element.

You can check out these articles (or other sources) on media queries to learn more about what you can write as an attribute value:

* [How to Use CSS Media Queries to Create Responsive Websites](https://www.freecodecamp.org/news/how-to-use-css-media-queries-to-create-responsive-websites/)
* [How to Set Width Ranges for Your CSS Media Queries](https://www.freecodecamp.org/news/media-queries-width-ranges/)
* [Media Query CSS Tutorial – Standard Resolutions, CSS Breakpoints, and Target Phone Sizes](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/)

# **Conclusion**

In this article, you learned how to add an external style sheet to your web page using the `link` element and the `href` and `rel` attributes.

You also learned that you can import multiple stylesheets and use the `media` attribute to determine when each one should be applied.

Have fun creating web pages!

