---
title: Minify CSS – CSS Minifying and Compression Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-18T15:20:23.000Z'
originalURL: https://freecodecamp.org/news/minify-css-css-minifying-and-compression-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-magda-ehlers-2590535.jpg
tags:
- name: compression
  slug: compression
- name: CSS
  slug: css
- name: optimization
  slug: optimization
seo_title: null
seo_desc: "By Dillion Megida\nMinification is the process of reducing code size to\
  \ reduce the size of your files. So how does this apply to CSS?\nTake a look at\
  \ this code:\nh1 {\n  color: yellow;\n}\n\np {\n  color: pink;\n}\n\nAnd the compressed\
  \ version of it:\nh1 { color..."
---

By Dillion Megida

Minification is the process of reducing code size to reduce the size of your files. So how does this apply to CSS?

Take a look at this code:

```css
h1 {
  color: yellow;
}

p {
  color: pink;
}
```

And the compressed version of it:

```css
h1 { color: yellow; } p { color: pink; }
```

These two code blocks are the same thing, and they work the same way because they have the correct CSS syntax. But there are two differences between these code blocks:

* the first one is more readable and understandable compared to the second one with a one-liner
* the first one results in bigger file size compared to the second one.

On testing this on my computer, the first one has a size of **46 bytes** while the second is **40 bytes**. This difference may seem insignificant, but it becomes noticable when you consider the difference that a compressed version of a bigger codebase can make.

## Why does the compressed size matter?

When a browser gets an HTML document from a server, it fetches the resources linked in the document. These resources include images, scripts, and also stylesheets.

The larger a CSS file is, the more resources (such as network bandwidth) it takes to download. Also, the longer it takes to download such files. This results in slower page load times and affects the overall user experience.

These expenses can be ignored for small CSS files, but as a program grows, compression becomes an essential factor in improving page load times.

## All the browser needs is valid CSS, not readable or formatted CSS

Compressed file sizes do not affect how the browser parses CSS. The browser does not need readable CSS to be able to interpret it on a web page. It only needs valid CSS (CSS code with a correct syntax – curly braces, semi-colons, and so on). 

Therefore, the extra spaces, comments, and indentations do not matter to the browser. It only matters for development. 

For deployed applications, you need a **distributable** version of CSS.

The **distributable** version isn't meant to be read by humans or used during development – but rather it's used for deployed applications as they only matter to the browser.

## How does minified CSS work?

The goal of minification is to remove the parts of your CSS code that are irrelevant to the browser to interpret the CSS.

For example, this code:

```css
h1 {
  /* a header */
  color: yellow;
}
```

Here's a graphical presentation of the parts of the code that matter and those that do not:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-85.png)

Code comments can help developers work together, remember why decisions are made, and understand the purpose of different parts of code. But the browser does not need that information.

Spaces and indentation improve the readability of code by humans, but the browser can read code without spaces.

The element selector, curly braces, and semi-colon are essential parts of the code as they follow the CSS syntax and help the browser interpret the code correctly.

CSS minification methods take these parts that the browser does not need from the code, which result in a lower-sized file, and makes it faster for the browser to download such files from the server.

The minified version of the above code is:

```css
h1{color:yellow;}
```

And everything still works perfectly on the browser.

## How to minify CSS

Now you understand the relevance of compressed CSS files and how they work. So how do you minify your CSS files?

Of course, you cannot write minified CSS code during development because it makes code collaboration, reading, and understanding difficult. 

Here are some tools you can use to minify your CSS.

### clean-css

[clean-css](https://www.npmjs.com/package/clean-css) is an NPM library you can use to minify your CSS files either locally or from a remote server.



![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-88.png)

### Dan's Tools CSS Minifier

[Dan's Tools Minifier](https://www.cleancss.com/css-minify/) is an online CSS minification tool for minifying CSS. You can paste the CSS in an input field, enter a URL where the CSS file lives, or paste the CSS file.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-86.png)
_Screenshot from the Dan's Tools CSS Minifier page_

### Toptal CSS Minifier

[Toptal CSS Minifier](https://www.toptal.com/developers/cssminifier/) provides a UI to add your CSS, and see the minified output. It also provides an API and plugins that makes the process automated.


![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-87.png)
_Toptal CSS Minifier screenshot_

There are more tools and configurations you can apply to make the process easier – these are just a few.

## Wrap up

Minification, generally, is a great approach for optimizing websites. Minifying CSS files increases page load times and requires fewer resources by the browser to download.

During development, comments, indentation, and other forms of formatting improve code readability and collaboration. But the browser does not need that. 

CSS minification is the process of compressing CSS file sizes by taking out the irrelevant part of the files that the browser does not need to interpret on a webpage.

Fortunately, some tools make it easier, so you can enjoy the process of development and also get a distributed version at the end.


