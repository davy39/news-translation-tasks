---
title: How to Optimize Your CSS Code for Faster Web Pages
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-01-26T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-your-css-code-for-faster-web-pages
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/csstitle.png
tags:
- name: CSS
  slug: css
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'CSS is more than just a tool for styling. It also determines how web pages
  render in a browser. Well-optimized CSS means faster loading times and a smoother
  user experience.

  In today''s digital landscape, the performance of a website is a key factor i...'
---

CSS is more than just a tool for styling. It also determines how web pages render in a browser. Well-optimized CSS means faster loading times and a smoother user experience.

In today's digital landscape, the performance of a website is a key factor in its success. Writing efficient CSS code can greatly influence how quickly your web pages load, impacting everything from user experience to search engine rankings. 

This guide delves into effective strategies to help you refine your CSS, ensuring that your website not only looks great but also loads swiftly and runs smoothly.

## How CSS affects Web Performance

When a user visits a webpage, the browser retrieves the site's structural HTML and its stylistic CSS. This is a set of detailed instructions on how each part of the webpage should look. 

If the CSS is packed with too much information or is too complex, it's like giving the browser a puzzle that takes longer to solve. This can lead to longer waiting times for users, which can be annoying.

That's where the art of streamlining CSS comes into play. It's not just about tidying up the code, but also making sure the browser can get the webpage ready faster. 

When CSS is made leaner and simpler, it's like giving the browser a clear, easy-to-follow map. This makes webpages load faster, making everything feel more responsive. 

## 1. Write Shorter CSS

When writing CSS, use the popular software development principle Don’t Repeat Yourself (DRY). This advocates for conciseness and clarity in your code. 

This is important here, because in practice, CSS involves repeating properties across various selectors. The goal should be to identify and consolidate these repetitive properties. By doing so you eliminate redundancies, leading to cleaner and more manageable CSS.

For instance, in the code below, multiple elements (`h1`and `h2`) share the same font-size and color. 

```css
h1 {
    font-size: 20px;
    color: #fff;
}
h2 {
    font-size: 20px;
    color: #fff;
}
```

So instead of declaring these properties separately for each selector, you can group them under a common class. This not only streamlines your stylesheet but also makes future updates easier and less error-prone.

You can rewrite the above code to look like this:

```css
h1, h2 {
    font-size: 20px;
    color: #fff;
}
```

Using shorthand properties is another effective strategy for minimizing the size of your CSS, making your code more efficient. It also allows you to set multiple related CSS properties with a single declaration. Here's how you can write effective shorthand CSS:

When all sides of an element have the same value, use that one value.

```css
/* Before shorthand */
.same-sides {
    padding-top: 15px;
    padding-right: 15px;
    padding-bottom: 15px;
    padding-left: 15px;
}

/* After shorthand */
.same-sides {
    padding: 15px;
}
```

When all sides of an element have different values, use all four.

```css
/* Before shorthand */
.different-sides {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 15px;
    padding-left: 25px;
}

/* After shorthand */
.different-sides {
    padding: 10px 20px 15px 25px;
}
```

When top/bottom and right/left have the same value, use two values.

```css
/* Before shorthand */
.two-sides {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 10px;
    padding-left: 20px;
}

/* After shorthand */
.two-sides {
    padding: 10px 20px;
}
```

When only the right/left values are the same but the top and bottom aren't, use three values.

```css
/* Before shorthand */
.three-sides {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 15px;
    padding-left: 20px;
}

/* After shorthand */
.three-sides {
    padding: 10px 20px 15px;
}
```

## 2. Use Shallow CSS Selectors

Shallow CSS selectors are direct and concise selectors with fewer levels of nested elements that don't dig too deep into the HTML structure. 

Simplifying your selectors can significantly speed up your webpage rendering because deeply nested selectors take longer for browsers to evaluate, which results in a slower page render.

Consider the example in the code below: to assign property values to a deeply nested selector like `header nav ul li a` is cumbersome and will cause rendering delays because the browser needs time to check each level (header, then nav, then ul, and so on) to find the right **`<a>`** tag to style). 

Alternatively, giving it a direct class `.nav-link` is straightforward and quicker for browsers to interpret. Class selectors are generally more efficient than nested tags because the browser simply looks for elements with a class and applies the styles, without worrying about their position in the DOM tree.

```css
/* Less efficient: Deeply nested selector */
header nav ul li a { 
   color: #000;
   font-size: 10px;
 }

/* More efficient: Class selector */
.nav-link {
   color: #000;
   font-size: 10px;
}
```

## 3. Segment CSS Code

Segmenting your CSS code into smaller, more focused segments like separate files for different website components and creating page-specific styles can greatly improve your website's performance. This approach not only makes it easier to find and edit specific styles but also ensures that webpages load only the CSS they need, avoiding unnecessary bulk.

Enhanced maintainability and faster page loading are the most obvious key benefits. Smaller CSS files are easier to manage, much like a well-organized toolbox where everything is easy to find. But also, by loading only the essential CSS for each page, the browser has less work to do hence improving the user experience.

### Original CSS 

Suppose you have a CSS file that contains styles for various parts of your website:

```css
/* Styles for the home page */
.homepage {
    background-color: #f0f0f0;
    padding: 10px;
}

/* Styles for the services page */
.services {
    background-color: #333;
    color: white;
}

/* Styles for the contact page */
.contact {
    background-color: #222;
    color: white;
    padding: 20px;
}
```

### Segmented CSS

Now, let's segment this CSS into different files based on their purpose:

1. **Home page Styles (homepage.css):**

```css
.homepage {
    background-color: #f0f0f0;
    padding: 10px;
}
```

2. **Services page Styles (services.css):**

```css
.services {
    background-color: #333;
    color: white;
}
```

3. **Contact page Styles (contact.css):**

```css
.contact {
    background-color: #222;
    color: white;
    padding: 20px;
}
```

Each CSS file is focused on a specific part of the website. Now, when a user visits your website, each page loads only the CSS it requires hence enhancing the website's performance.

## 4. Optimize CSS Delivery

You can make your CSS files lighter and faster to load by shrinking your CSS – that is, you can remove extra spaces and lines (this is called minifying). Then you can compress these files so they're smaller and quicker for users to download. 

Also, make sure the most important styles of your website load first, so people see your page faster. The other styles can load in the background without slowing things down.

You can also make your website faster for people who visit more than once, by saving some of your CSS in their browser (this is known as caching). This means it doesn’t have to load again every time they visit. 

Also, if you use a CDN or a network of servers, your CSS files can be stored in many places around the world to load faster no matter where your users are. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/minifycss.png)
_Graphic comparing file size between an unminified CSS file at 167KB and a minified CSS file at 92KB_

### Original CSS

```css
/* Main Stylesheet */
/* Header Style */
header {
  background-color: #333;
  color: white;
  padding: 10px;
}

/* Navigation Style */
nav {
  background-color: #444;
  margin-top: 10px;
}
```

The above CSS code is readable and well-commented, but it contains extra spaces and comments that increase the file size.

### Minified CSS

```css
header{background-color:#333;color:white;padding:10px}nav{background-color:#444;margin-top:10px;}
```

The minified version combines all the rules into a single line, removing unnecessary spaces and comments, which reduces the file size for quicker loading.

## Conclusion

Optimizing your CSS speeds up your website and consequently improves the overall user experience. 

By implementing the practices outlined in this article, you can achieve more performant, efficient and maintainable CSS. The performance savings may not be significant from tweaking a few lines but over hundreds more across different stylesheets, the impact will begin to show. 

Remember, web performance is an ongoing process. Regularly review and refine your CSS to keep up with best practices and emerging trends.

### Additional Resources

* [MDN Web Docs on CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Google Web Fundamentals](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency)
* [Web Performance In Action](https://www.oreilly.com/library/view/web-performance-in/9781617293771/)

