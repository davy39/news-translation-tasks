---
title: Inline Style in HTML – CSS Inline Styles
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-08T21:24:31.000Z'
originalURL: https://freecodecamp.org/news/inline-style-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template-1.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: style
  slug: style
seo_title: null
seo_desc: 'Cascading Style Sheets (CSS) is a markup language that determines how your
  web pages will appear. It manages the colors, fonts, and layouts of your website
  elements, as well as allowing you to add effects or animations to your pages.

  We can style an ...'
---

Cascading Style Sheets (CSS) is a markup language that determines how your web pages will appear. It manages the colors, fonts, and layouts of your website elements, as well as allowing you to add effects or animations to your pages.

We can style an HTML file/page in three ways: external styling, internal styling, and inline styling. In this article, we'll be focusing on inline styling.

## How to Use Inline Style in HTML

Using the style attribute, we can apply styling to our HTML inside individual HTML tags with inline styling.

```html
<h1 style="...">...</h1>
```

The style attribute works in the same way as any other HTML attribute. We use `style`, followed by the equality sign (=), and then a quote where all of the style values will be stored using the standard CSS property-value pairs - `"property: value;"`.

**Note:** We can have as many property-value pairs as we want as long as we separate them with a semicolon (;).

It's worth noting that the `style` attribute is typically used in the opening HTML tag because that's the part of the HTML element that can contain text, data, an image, or nothing at all. An example of inline style is as follows:

```html
<h1 style="color: red; font-size: 40px;">Hello World</h1>
```

This is similar to this:

```css
h1 {
  color: red;
  font-size: 40px;
}
```

The only difference is that the inline style applies only to the tag to which it is applied, whereas this second code example affects all `p` tags on your html page.

### When to Use Inline Styles

Using inline styles is not considered best practice, though, because it results in a lot of repetition – because the styles cannot be reused elsewhere.

But there are times when inline styles are the best (or only) option, such as when styling HTML e-mail, CMS content like WordPress, Drupal, and so on. You can also use them when styling dynamic content, which is HTML-created or changed by JavaScript.

With the exception of the `!important` declaration, inline styles have a [high specificity/highest priority](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#Understanding_the_cascade), which means they will override most other rules in internal and external stylesheets.

Assume we have two paragraph texts with inline styling set to `red` and internal styling set to `green`:

```html
<html>
  <head>
      <title>Hello World</title>
      <style>
       p {
           color: green;
       }
   </style>
  </head>
 
  <body>
     <p style="color: red;">Paragraph one is red.</p>
     <p style="color: red;">Paragraph two is also red.</p>
  </body>
</html>
```

The CSS from our inline styles will override the CSS from the internal styling, so both paragraphs will be `red`.

## Advantages and Disadvantages of Inline styles

So far, we've learned what inline style is and how to use it within HTML tags. Now, let's look at the advantages and disadvantages to see when we should use inline styles and when we shouldn't.

### Advantages of Inline CSS:

* Inline takes precedence over all other styles. Any styles defined in the internal and external style sheets are overridden by inline styles.
    
* You can quickly and easily insert CSS rules into an HTML page, which is useful for testing or previewing changes and performing quick fixes on your website.
    
* There is no need to create an additional file.
    
* To apply styling in JavaScript, use the `style` attribute.
    

### Disadvantages of Inline CSS:

* Adding CSS rules to each HTML element takes time and makes your HTML structure unorganized. It's difficult to keep up, reuse, and scale.
    
* The size and download time of your page can be affected by styling multiple elements.
    
* Inline styles cannot be used to style pseudo-elements and pseudo-classes. For example, you can style the visited, hover, active, and link colors of an anchor tag using external and internal style sheets.
    

## Conclusion

In this article, we learned how to use inline style in HTML, when to use it, and some of the benefits and drawbacks of doing so.

Since inline styling takes precedence over all other styles, one of the best times to use it is when testing or previewing changes and performing quick fixes on your website.
