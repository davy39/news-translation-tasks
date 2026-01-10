---
title: HTML for Beginners
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-05T14:19:09.000Z'
originalURL: https://freecodecamp.org/news/html-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/ht-ml.jpeg
tags:
- name: HTML
  slug: html
- name: youtube
  slug: youtube
seo_title: null
seo_desc: "HTML is used to create web pages. \nThis article will teach you the basics\
  \ of HTML. I also created a 45-minute video course on the freeCodeCamp.org YouTube\
  \ channel that teaches you HTML in the context of creating an actual web page.\n\
  If you are just le..."
---

HTML is used to create web pages. 

This article will teach you the basics of HTML. I also created a 45-minute [video course on the freeCodeCamp.org YouTube channel](https://youtu.be/916GWv2Qs08) that teaches you HTML in the context of creating an actual web page.

If you are just learning HTML, I recommend both reading this article and watching the video course.

HTML stands for Hyper Text Markup Language. Every website on the internet uses HTML & CSS. Most also use JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-187.png)
_HTML everywhere!_

In a website, HTML is the structure, CSS is the style, and JavaScript is the functionality.

Here is a great interactive diagram from [codeanalagies.com](https://blog.codeanalogies.com/2018/05/09/the-relationship-between-html-css-and-javascript-explained/). Move the slider back and forth.

<iframe src="https://blog.codeanalogies.com/wp-admin/admin-ajax.php?action=h5p_embed&id=1" width="726" height="478" frameborder="0" allowfullscreen="allowfullscreen" title="House to Page Structure- HTML, CSS, JS"></iframe><script src="https://blog.codeanalogies.com/wp-content/plugins/h5p/h5p-php-library/js/h5p-resizer.js" charset="UTF-8"></script>

You can actually see the HTML that makes up any element on a webpage by right-clicking an element and then selecting "Inspect".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-190.png)

## HTML Structure

Here is the HTML that makes up a very basic webpage:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First Website!</title>
</head>
<body>
  <p>This is an amazing website!</p>
  <img src="cat-picture.jpg" alt="The internet is powered by cat pictures.">
</body>
</html>
```

Let's break things down even more.

### Elements

HTML is made up of HTML elements. An element is an individual component of HTML.

Here is an HTML element from the code above: 

```html
<p>This is an amazing website!</p>
```

### Tags

HTML tags mark the beginning and end of an element (and are considered part of the element). Tags are containers. They tell you something about the content between the opening & closing tags.

In the element above, the tags are `<p>` (opening tag) and `</p>` (closing tag). You will notice that the closing tag has a `/`. This particular tag is a `p`aragraph tag. It specifies a paragraph in the HTML document. The words between the opening and closing tags are a paragraph.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/html-tag-attributes.png)
_Anatomy of an HTML tag. Source: [clearlydecoded.com](https://clearlydecoded.com/anatomy-of-html-tag)_

### Kinds of Elements

Elements can be either container elements (they hold content) or stand-alone elements, sometimes called self-closing elements.

Paragraph elements are containers: `<p>Hi, I contain content</p>`

Image elements are stand-alone: `<img src="beau.jpg" />`

Notice in the stand-alone `img` element, there is no closing tag but there is a `/` before the final angle bracket.

### Attributes

Attributes provide additional information about HTML elements. Attribute tags include `class`, `id`, `style`, `lang`, and `src` (source).

Here is an example of an HTML element with the attribute tag `id`:

```
<p id="info">This is an amazing website!</p>
```

Some things to note about attributes:

* Attributes are positioned inside the opening tag, before the right bracket.
* Attributes are paired with values (in this example, the value is `info`).
* Key / value pairs are an important concept in programming.
* Attributes are selected from a pre-defined set of possible attributes depending on the element.
* Values are assigned to attributes and they must be contained inside quotation marks.

Here is another example of an element with at attribute:

```html
<div class="container">
   A bunch of stuff!
</div>
```

### Nesting

HTML elements 'nest' inside of one another. The element that opens first closes last.

When nesting elements, spaces and tabs are often used to show the level of nesting. However, the spacing is not required and is only used to make HTML easier to read for humans.

Here is an example of some HTML with a few levels of nesting elements:

```html
<body>
  <div class="outer-div">
    <p>This is an amazing website!</p>
    
    <a href="https://www.freecodecamp.org">freeCodeCamp</a>

    <div class="inner-div">
      <ol>
        <li>Thing 1</li>
        <li>Thing 2</li>
        <li>Thing 3</li>
      </ol>
    </div>
  </div>
</body>
```

### Common HTML Tags

Here are some common tags that are in almost all HTML documents.

`doctype`: This is the first element on every HTML page. It tells the browser to expect HTML and what version to use. For the newest version of HTML, the element should look like this: `<!doctype html>`

`html`: After the doctype, all page content must be contained in the `<html>` tags.

`head`: This element contains the page title and metadata.

`body`: This element contains all the visible content in a page.

`title`: This optional element is the name of your page. It is always nested in the `head` tag.

`div`: This tag is one of the most used tags. It is used to create a basic container of other HTML or content. 

`p`: A paragraph or section of body copy.

`h1`-`h6`: These designate different levels of headings or titles.

`ol`: Creates an ordered (numbered) list.

`ul`: Creates an unordered list.

`li`: List element.

### Links

Anchor elements ( `<a></a>`) are used to link to other sites on the web or within your project.

This element links to another website:

`<a href="https://freecodecamp.com">freeCodeCamp</a>`

This element links to another page of your website:

`<a href="about.html">About Me</a>`

The `<link>` element is a different type of link. Unlike the anchor element, it specifies relationships between the current document and an external resource.

It is often used to link a CSS file with an HTML file so that the external CSS file is used to style the HTML.

Here is an example:

`<link src="main.css" rel='stylesheet' />`

### Comments

Like any other good coding language, HTML offers comments. They operate like comments in any other language. They are ignored by the browser engine.

`<!-- Hello, I am a comment. -->`

### Tables

Tables are a way to represent complex information in a grid format. They are made of rows and columns.

Tables are compound elements (similar to lists) they are made up of several elements.

`table`: Table element.

`tr`: Table row.

`td`: Table cell.

`th`: Table header cell (optional).

Here is an example of a table. First you will see the HTML. Then you will see how the HTML displays.

```html
<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Favorite Animal</th>
  </tr>
  <tr>
    <td>Beau</td>
    <td>Carnes</td>
    <td>cow</td>
  </tr>
  <tr>
    <td>Quincy</td>
    <td>Larson</td>
    <td>dog</td>
  </tr>
</table>
```

<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Favorite Animal</th>
  </tr>
  <tr>
    <td>Beau</td>
    <td>Carnes</td>
    <td>cow</td>
  </tr>
  <tr>
    <td>Quincy</td>
    <td>Larson</td>
    <td>dog</td>
  </tr>
</table>

### Trivia time!

1. What is wrong with this code?

```html
<html>
	<head>
    <body>
    </head>
    
    </body>
</html>
```

<button id="button1" title="Click to Show/Hide Content" type="button" onclick="if(document.getElementById('spoiler1').style.display=='none') {document.getElementById('spoiler1') .style.display='';document.getElementById('button1').innerText='Hide Answer'}else{document.getElementById('spoiler1') .style.display='none';document.getElementById('button1').innerText='Show Answer'}">Show Answer</button>
<div id="spoiler1" style="display:none">
    Closing <code>head</code> tag should be before opening <code>body</code> tag.
</div>

2. What is wrong with this code?

```html
<html>
  <head>
    <title>The best site ever!!
  </head>
  <body>    
    <p>Check out this great content.</p>
  </body>
</html>
```

<button id="button2" title="Click to Show/Hide Content" type="button" onclick="if(document.getElementById('spoiler2').style.display=='none') {document.getElementById('spoiler2') .style.display='';document.getElementById('button2').innerText='Hide Answer'}else{document.getElementById('spoiler2') .style.display='none';document.getElementById('button2').innerText='Show Answer'}">Show Answer</button>
<div id="spoiler2" style="display:none">
    There is no closing <code>title</code> tag.
</div>

3. What is wrong with this code?

```html
<p id=content>Check out this great content.</p>
```

<button id="button3" title="Click to Show/Hide Content" type="button" onclick="if(document.getElementById('spoiler3').style.display=='none') {document.getElementById('spoiler3') .style.display='';document.getElementById('button3').innerText='Hide Answer'}else{document.getElementById('spoiler3') .style.display='none';document.getElementById('button3').innerText='Show Answer'}">Show Answer</button>
<div id="spoiler3" style="display:none">
    There should be quotation marks around the value "content".
</div>

## Conclusion

You've now learned the basics of HTML syntax.

Next you should watch this [HTML crash course I created](https://www.youtube.com/watch?v=916GWv2Qs08) that teaches HTML in the context of building a simple web page.

%[https://www.youtube.com/watch?v=916GWv2Qs08]

After you learn HTML, you should learn CSS and JavaScript. I have also created courses on those topics. You can watch them next:

%[https://www.youtube.com/watch?v=ieTHC78giGQ]



%[https://www.youtube.com/watch?v=PkZNo7MFNFg&t=145s]


