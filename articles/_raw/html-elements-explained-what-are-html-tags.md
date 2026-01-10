---
title: 'HTML Elements Explained: What are HTML Tags and How Do You Use Them?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/html-elements-explained-what-are-html-tags
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce7740569d1a4ca34cb.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'What are HTML Elements?

  Elements are the building blocks of HTML that describe the structure and content
  of a web page. They are the “Markup” part of HyperText Markup Language (HTML).

  HTML syntax uses the angle brackets (”<” and ”>”) to hold the name...'
---

## What are HTML Elements?

Elements are the building blocks of HTML that describe the structure and content of a web page. They are the “Markup” part of HyperText Markup Language (HTML).

HTML syntax uses the angle brackets (”<” and ”>”) to hold the name of an HTML element. Elements usually have an opening tag and a closing tag, and give information about the content they contain. The difference between the two is that the closing tag has a forward slash.

Let's look at some specific examples of HTML tags.

## p Element

The `<p>` tag stands for paragraph, which is the most common tag used to create lines of text inside an HTML document.

The use of the `<p>` is compatible with other tags, allowing to add hyperlinks (`<a>`) and bold (`<strong>`) text, among other things.

### Example

```html
<html>
  <head>
    <title>Paragraph example</title>
  </head>
  <body>
    <p>
      This is a paragraph. It is the first of many.
    </p>
    <p>
      This is another paragraph. It will appear on a separate line.
    </p>
  </body>
</html>

```

You can also nest an anchor element `<a>` within a paragraph.

### Example

```html
<p>Here's a <a href="https://freecodecamp.org">link to freeCodeCamp</a>.</p>
```

## Heading Elements

There are six heading elements — `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`. 

Heading elements are used to signify the importance of the content below them. The lower the number of the heading, the higher the importance. 

For example, the `<h1>` element represents the main heading of the page, and there should only be one per page. This helps search engines understand the main topic of the page. `<h2>` elements have less importance, and should be below the higher level `<h1>` element.

### Example

```
<h1>This is main heading.</h1>
<h2>This is subheading h2.</h2>
<h3>This is subheading h3.</h3>
<h4>This is subheading h4.</h4>
<h5>This is subheading h5.</h5>
<h6>This is subheading h6.</h6>

```

## a Element

The anchor (`<a>`) element creates a hyperlink to another page or file. In order to link to a different page or file the `<a>` tag must also contain a `href` attribute, which indicates the link's destination.

The text between the opening and closing `<a>` tags becomes the link. This text should be a meaningful description of the link destination, and not a generic phrase such as "Click here". This better enables users with screen readers to navigate among the various links on a page and understand what content each one will link to.

By default, a linked page is displayed in the current browser window unless another target is specified. The default link styles are as follows:

* An unvisited link is underlined and blue
* A visited link is underlined and purple
* An active link is underlined and red

### Examples

```html
  <a href= "https://guide.freecodecamp.org/">freeCodeCamp</a>

```

You can also create a link to another section on the same page:

```html
  <h1 id="top"></h1>
  <a href= "#top">Go to top</a>

```

An image can also be turned into a link by enclosing the `<img>` tag in an `<a>` tag:

```html
  <a href= "https://guide.freecodecamp.org/"><img src="logo.svg"></a>

```

## List Elements

There are two main types of lists in HTML: ordered (`<ol>`) and unordered (`<ul>`). All lists must contain one or more list elements (`<li>`).

### Unordered list

The unordered list starts with `<ul>` tag and list items start with the `<li>` tag. In unordered lists all the list items marked with bullets by default.

```
<ul>
  <li>Item</li>
  <li>Item</li>
  <li>Item</li>
</ul>

```

Output:

* Item
* Item
* Item

### Ordered list

The ordered list starts with `<ol>` tag and list items start with the `<li>` tag. In ordered lists all the list items are marked with numbers.

```
<ol>
  <li>First Item</li>
  <li>Second Item</li>
  <li>Third Item</li>
</ol>

```

Output:

1. First Item
2. Second Item
3. Third Item

## em Element

The `<em>` element is used to _emphasize_ text in an HTML document. This can be done by wrapping the text you would like to be emphasized in an `<em>` tag and an `</em>` tag respectively. Most browsers will render text wrapped in an `<em>` tag as italicized.

Note: The `<em>` tag should not be used to stylistically italicize text. The `<em>` tag is used to stress emphasis on text. Typically, CSS formatting is used to stylistically italicize text.

### Example

```
<body>
  <p>
    Text that requires emphasis should go <em>here</em>.
  </p>
</body>

```

## i Element

The `<i>` element is used to denote text that is set apart from its surrounding text in some way. By default, text surrounded by `<i>` tags will be displayed in italic type.

In previous HTML specifications, the `<i>` tag was solely used to denote text to be italicized. In modern semantic HTML, however, tags such as `<em>` and `<strong>` should be used where appropriate. 

You can use the `class` attribute of the `<i>` element to state why the text in the tags is different from the surrounding text. You may want to show that the text or phrase is from a different language:

```html
<p>The French phrase <i class="french">esprit de corps</i> is often 
used to describe a feeling of group cohesion and fellowship.</p>

```

## strong Element

The `<strong>` element is used to denote text that is of strong importance or urgency. Most browsers will render text wrapped in an `<strong>` tag as bold.

Note: The `<strong>` tag should not be used to style the text as bold. Use CSS to do that.

### Example:

```
<body>
  <p>
    <strong>This</strong> is really important.
  </p>
</body>

```

## img Element

A simple HTML `<img>` element can be included in an HTML document like this:

```html
<img src="path/to/image/file" alt="this is a cool picture" title="Some descriptive text goes here">

```

Note that `<img>` elements are self-closing, and do not require a closing tag.

`alt` tags provide alternate text for an image. One use of the `alt` tag is for visually impaired people using a screen reader; they can be read the `alt` tag of the image in order to understand the image's meaning.

The `title` attribute is optional and will provide additional information about the image. Most browsers display this information in a tooltip when the user hovers over it.

Note that the path to the image file can be either relative or absolute. Also, remember that the `img` element is self-closing, meaning that it does not close with the `</img>` tag and instead closes with just a single `>`.

### Examples

```html
<img src="https://example.com/image.png" alt="my picture" title="This is an example picture">

```

(This is assuming that the HTML file is at [https://example.com/index.html](https://example.com/index.html), so it's in the same folder as the image file)

is the same as:

```html
<img src="image.png" alt="my picture" title="This is an example picture">

```

Sometimes an `<img>` element will also use two other attributes to specify its size, `height` and `width`, as shown below:

```html
<img src="image.png" alt="my picture" width="650" height="400" />

```

The values are specified in pixels, but the size is usually specified in CSS rather than HTML.

## **nav Element**

The `<nav>` element is intended for major block of navigation links. NOT all links of a document should be inside a `<nav>` element.

Browsers, such as screen readers for disabled users, can use this element to determine whether to omit the initial rendering of this content.

### Example

```html
<nav class="menu">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

## **header Element**

The `<header>` tag is a container which is used for navigational links or introductory content. It may typically include heading elements, such as `<h1>`, `<h2>`, but may also include other elements such as a search form, logo, author information, and so on.

Although not required, the `<header>` tag is intended to contain the surrounding sections heading. It may also be used more than once in an HTML document. It is important to note that the `<header>` tag does not introduce a new section, but is simply the head of a section.

### Example

```html
<article>
  <header>
    <h1>Heading of Page</h1>
  </header>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</article>
```

## **textarea Element**

The HTML textarea tag allows you to enter a box that will contain text for user feedback or interaction. In most cases, it is common to see the textarea used as part of a form.

Programmers use textarea tag to create multiline field for user input (useful especially in case when user should be able to put on the form longer text). Programmers may specify different attributes for textarea tags.

### Example

```html
    <form>
      <textarea name="comment" rows="8" cols="80" maxlength="500" placeholder="Enter your comment here..." required></textarea>
    </form>
```

Most common attributes: `row` and `cols` attributes determine the height and width of the textarea `placeholder` attribute specifies the text which is visible to the user, it helps the user to understand what data should be typed in `maxlength` attribute determines the maximum length of the text which can be typed in the textarea, user cannot submit more characters `required` attribute means that this field must be filled in before the form submission.

## label Element

The `<label>` tag defines a label for an `<input>` element.

A label can be bound to an element either by using the “for” attribute, or by placing the element inside the **element.**

### Example

```text
<label for="id">Label</label>
<input type="text" name="text" id="id" value="yourvalue"><br>
```

As you can see, the _for_ attribute of the **tag should be equal to the id attribute of the related element to bind them together.**

### Platform Support

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.01.48-PM.png)

### Attributes

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.02.13-PM.png)

### **Global Attribute**

The `<label>` tag supports the Global Attributes in HTML.

### **Event Attribute**

The `<label>` tag supports the Event Attributes in HTML.

The `<label>` element does not render as anything special for the user. However, it provides a usability improvement for mouse users, because if the user clicks on the text within the **element, it toggles the control.**

## **Meta Tag**

The `<meta>` tag provides the metadata about the HTML document.

This metadata is used to specify a page’s charset, description, keywords, the author, and the viewport of the page.

This metadata will not appear on the website itself, but it will be used by the browers and search engines to determine how the page will display content and assess search engine optimization (SEO).

### Example

```html
<head>
  <meta charset="UTF-8">
  <meta name="description" content="Short description of website content here">
  <meta name="keywords" content="HTML,CSS,XML,JavaScript">
  <meta name="author" content="Jane Smith">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- HTML5 introduced a method to let web designers take control over the viewport, through the <meta> tag. The viewport is the user's visible area of a web page. A <meta> viewport element gives the browser instructions on how to control the page's dimensions and scaling. -->  
</head>
```

## **div Element**

The `<div>` tag is a generic container that defines a section in your HTML document. A `<div>` element is used to group sections of HTML elements together and format them with CSS. 

A `<div>` is a block-level element. This means that it takes up its own line on the screen. Elements right after the `<div>` will be pushed down to the line below. For similar grouping and styling that is not block-level, but inline, you would use the `<span>` tag instead. The tag is used to group inline-elements in a document.

### **Example**

Here is an example of how to display a section in the same color:

```html
<div style="color:#ff0000">
  <h3>my heading</h3>
  <p>my paragraph</p>
</div>
```

## section Element

The `<section>` element defines a section where there isn't a more specific semantic HTML element to represent it. Typically, a `<section>` element will include a heading element (`<h1>` - `<h6>`) as child element.

For example, a web page could be divided into various sections such as welcome, content and contact sections.

A `<section>` element should not be used in place of a `<div>` element if a generic container is needed. It should be used to define sections within an HTML page.

```html
<html>
<head>
  <title>Section Example</title>
</head>
<body>
  <section>
    <h1>Heading</h1>
    <p>Bunch of awesome content</p>
  </section>
</body>
</html>

```

## **footer Element**

The `<footer>` tag denotes the footer of an HTML document or section. Typically, the footer contains information about the author, copyright information, contact information, and a sitemap. Any contact information inside of a `<footer>` tag should go inside an `<address>` tag.

### **Example**

```html
<html>
<head>
  <title>Paragraph example</title>
</head>
<body>
  <footer>
    <p>&copy; 2017 Joe Smith</p>
  </footer>
</body>
</html>
```

## **audio Element**

The `<audio>` tag defines an audio element, that can be used to add audio media resource to an HTML document that will be played by native support for audio playback built into the browser rather than a browser plugin.

The audio tag currently supports three file formats OGG, MP3 and WAV which can be added to your html as follows.

### Adding an OGG

```text
<audio controls>
  <source src="file.ogg" type="audio/ogg">
</audio>
```

### Adding an MP3

```text
<audio controls>
  <source src="file.mp3" type="audio/mpeg">
</audio>
```

### Adding a WAV

```text
<audio controls>
  <source src="file.wav" type="audio/wav">
</audio>
```

It may contain one or more audio sources, represented using the src attribute or the source element.

### Adding Multiple Audio Files

```text
<audio controls>
  <source src="file-1.wav" type="audio/wav">
  <source src="file-2.ogg" type="audio/ogg">
  <source src="file-3.mp3" type="audio/mpeg">
</audio>
```

### Browser Support for different file types is as follows

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.06.46-PM.png)

### **Supported Attributes**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.07.17-PM.png)

## **iframe Element**

The HTML `<iframe>` element represents an inline frame, which allows you to include an independent HTML document into the current HTML document. The `<iframe>` is typically used for embedding third-party media, your own media, widgets, code snippets, or embedding third-party applets such as payment forms.

### **Attributes**

Listed below are some of the `<iframe>`’s attributes:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-31-at-2.02.44-PM.png)

Iframe tags are used to add an existing web page or app to your website within a set space.

When using the iframe tags the src attribute should be used to indicate the location of the web page or app to use within the frame.

```html
<iframe src="framesite/index.html"></iframe>
```

You can set the width and height attributes to limit the size of the frame.

```html
<iframe src="framesite/index.html" height="500" width="200"></iframe>
```

Iframes have a border by default, if you wish to remove this you can do so by using the style attribute and setting CSS border properties to none.

```html
<iframe src="framesite/index.html" height="500" width="200" style="border:none;"></iframe>
```

### **Examples**

Embedding a YouTube video with an `<iframe>`:

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/v8kFT4I31es" 
frameborder="0" allowfullscreen></iframe>
```

Embedding Google Maps with an `<iframe>`:

```html
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d774386.2436462595!2d-74.53874786161381!3d40.69718109704434!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sau!4v1508405930424" 
width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>
```

### **Alternative Text**

The content between the opening and closing `<iframe>` tags is used as alternative text, to be displayed if the viewer’s browser does not support iframes.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/v8kFT4I31es" frameborder="0">
  <p>Your browser does not support iframes.</p>
</iframe>
```

### **Targeting an iframe in a Link**

Any anchor element can target the content of an `<iframe>` element. Rather than redirect the browser window to the linked webpage, it will redirect the `<iframe>`. For this to work, the `target` attribute of the `<a>` element must match the `name` attribute of the `<iframe>`.

```html
<iframe width="560" height="315" src="about:blank" frameborder="0" name="iframe-redir"></iframe>

<p><a href="https://www.youtube.com/embed/v8kFT4I31es" target="iframe-redir">Redirect the Iframe</a></p>
```

This example will show a blank `<iframe>` initially, but when you click the link above it will redirect the `<iframe>` to show a YouTube video.

### **JavaScript and iframes**

Documents embedded in an `<iframe>` can run JavaScript within their own context (without affecting the parent webpage) as normal.

Any script interaction between the parent webpage and the content of the embedded `<iframe>` is subject to the same-origin policy. This means that if you load the content of the `<iframe>` from a different domain, the browser will block any attempt to access that content with JavaScript.


