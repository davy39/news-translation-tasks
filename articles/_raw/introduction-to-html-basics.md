---
title: HTML for Beginners – HTML Basics With Code Examples
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2024-05-07T19:45:50.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-html-basics
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/cover-img.jpg
tags:
- name: HTML
  slug: html
seo_title: null
seo_desc: 'Welcome to the exciting world of web development! In this beginner''s guide,
  you will learn the fundamentals of HTML, the backbone of every web page.

  Imagine a tree: its roots anchor and nourish the entire plant. Similarly, HTML,
  the root of web devel...'
---

Welcome to the exciting world of web development! In this beginner's guide, you will learn the fundamentals of HTML, the backbone of every web page.

Imagine a tree: its roots anchor and nourish the entire plant. Similarly, HTML, the root of web development, provides the foundation for every webpage.

Understanding HTML's role is like grasping a tree's roots, it forms the fundamental basis for comprehending how web pages come to life.

By the end of this tutorial, you'll be equipped with the knowledge to kick-start your coding journey.

## Table of Contents

* [What is HTML?](#heading-what-is-html)
    
* [Basic Structure of an HTML Document](#heading-basic-structure-of-an-html-document)
    
* [Comments](#heading-comments)
    
* [Tags and Elements](#heading-tags-and-elements)
    
* [HTML Attributes](#heading-html-attributes)
    
* [HTML Multimedia](#heading-html-multimedia)
    
* [Best Practices](#heading-best-practices)
    

## What is HTML?

HTML, which stands for Hypertext Markup Language, is the standard language used for creating and designing the structure of a web page. It allows you to organize content on your website, define its structure, and establish the relationships between different elements.

## Basic Structure of an HTML Document

An HTML document follows a specific structure that acts as the foundation for your web page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link />
</head>
<body>
  <!-- your web page content goes here -->
</body>
</html>
```

Let's break it down:

`<!DOCTYPE html>`: defines the document type and version of HTML being used (HTML5 in this case).

`<html lang="en">` and `</html>`: opening and closing tag of the root element that wraps the entire HTML content. The attribute `lang="en"` defines the language (in this case, USA English)

`<head>` and `</head>`: opening and closing tag of the `head` element contains meta-information `<meta >` about the HTML document, the page title `<title></title>` you see in the browser tab, and link `<link />` which defines a link between your HTML document and an external resources, like stylesheet, favicon, import and so on.

`<body>` and `</body>` : opening and closing `body` tag encloses all the visible content of a web page, including text, images, links, forms, and other elements that users interact with.

**Note**: All HTML elements have opening (`**< >**`) and closing (`**</ >**`) tags, except for self-closing (`**< >**` or `**< />**`) tags, which I will explain in more detail later.

## Comments

Notice this `<!-- your web page content goes here -->` in the above html basic structure, it's called comments. Comments are used to add explanatory notes that are not displayed when the web page is viewed in a browser. They are useful for documenting your code, providing information to other developers, or temporarily excluding specific parts of the code. You can create comment using this tag `<!--` `your comment goes here` `-->`.

There are:

1. **Single-line commen**t: `<!-- This is a single-line comment -->`
    
2. **Multi-line comment**: `<!-- This is a multi-line comment. It can span multiple lines. All content within the comment block will be ignored by the browser. -->`
    

## Tags and Elements

HTML uses tags to define different elements on a webpage. Tags are enclosed in angle brackets (`< >`). There are opening (`< >`) and closing (`</ >`) tags, and self-closing (`< >` or `< />`) tag. Here are a few examples:

### Headings

```html
<h1>This is a Heading 1</h1>
<h2>This is a Heading 2</h2>
<!-- ... up to <h6> -->
```

The heading tags `<h1>` to `<h6>` are used to define headings or subheadings within a document. These tags represent a hierarchy of headings, with `<h1>` being the highest level (main heading) and `<h6>` being the lowest level (lowest subheading level).

Its purpose is to structure and organize the content of a web page, making it more readable and accessible.

### Paragraph

The paragraph tag (`<p> your text goes here </p>`) is used to separate blocks of text into distinct paragraphs. It is a block-level element that represents a unit of text or a block of content, and it is commonly used to structure and separate text on a webpage.

The `<p>` tag is part of the structural markup in HTML and helps in creating well-organized and readable content.

### Line Breaks

To create a line break without starting a new paragraph, use the break (`<br>`) tag.

Example 1 - Basic Line Break:

```html
<p>This is the first line.<br>This is the second line.</p>
```

This will render as:

This is the first line.  
This is the second line.

Example 2 - Line Breaks in Text:

```html
<p>This text contains a<br>line break.</p>
```

This will render as:

This text contains a  
line break.

Example 3 - Line Breaks in List:

```html
<ul>
  <li>Item 1</li>
  <li>Item 2<br>with a line break</li>
  <li>Item 3</li>
</ul>
```

This will render as:

* Item 1
    
* Item 2  
    with a line break
    
* Item 3
    

Example 4 - Line Breaks in Address:

```html
<address>
  Nuel Cas<br>
  23 Musa Yar'Dua VI<br>
  Lagos, Nigeria
</address>
```

This will render as:

Nuel Cas  
23 Musa Yar'Dua VI  
Lagos, Nigeria

Example 5: Line Breaks with Multiple  
Tags

```python
<p>This is a paragraph with<br><br>multiple line breaks.</p>
```

This will render as:

This is a paragraph with

multiple line breaks.

While break (`<br>`) tag is commonly used for simple line breaks, CSS and block-level elements like `<p>` and `<div>` tags are often preferred for more complex layouts.

Overusing `<br>` tags for layout purposes is discouraged. CSS is generally more suitable for controlling the spacing and layout of elements on a webpage.

### Div

A `<div>` tag, which stands for "division" is one of the most commonly used container elements in HTML. It is a block-level container that is used to group other HTML elements together and apply styles or scripting to them collectively.

Here's an example:

```html
<div>
  <p>This is a paragraph inside a div.</p>
  <ul>
    <li>List item 1</li>
    <li>List item 2</li>
  </ul>
</div>
```

In this example, the `<div>` element wraps around a paragraph (`<p>`) and an unordered list (`<ul>`). This grouping allows you to apply styles or manipulate these elements together using CSS or JavaScript.

**Note**: The `<div>` tag is often used for layout purposes, helping structure the content of a webpage. For more semantic and specific meanings, HTML5 introduced new semantic tags like `<section>`, `<article>`, `<header>`, `<footer>`, and so on, which provide better clarity about the content's purpose.

### Semantic Tags

They are like special labels that tell web browsers and developers what different parts of a webpage are all about. They help make websites easier to understand for both people and computers.

By using these tags, you can make your websites more accessible and easier to find on search engines. Here are some common HTML semantic tags along with examples:

1. `<header>`: The header tag represents introductory content at the beginning of a section or webpage. It typically contains logos, navigation menus, and other introductory elements.
    

Example:

```html
  <header>
  <h1>Website Title</h1>
  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
</header>
```

2. `<nav>`: Use nav tag to define navigation links within your webpage. It contains links to other pages or sections of the website.
    

Example:

```html
<nav>
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

3. `<main>`: Used to define the main content of a webpage. It helps improve the accessibility and structure of your HTML code, as it clearly identifies the main content area for screen readers and other assistive technologies. It also helps search engines understand the relevance of the content on your page, which can improve your website's Search Engine Optimization (SEO).
    

Example:

```html
<main>
  <article>
    <h2>Page Title</h2>
    <p>Page content goes here...</p>
  </article>
</main>
```

4. `<section>`: Use the `section` tag when you want to define sections within a webpage. Also, for grouping related content together.
    

Example:

```html
<section>
  <h2>Section Title</h2>
  <p>Section content goes here...</p>
</section>
```

5. `<article>`: Use the `article` tag when you want to define an independent piece of content that can stand alone, such as a blog post, news article, or forum post.
    

Example:

```html
<article>
  <h2>Article Title</h2>
  <p>Article content goes here...</p>
</article>
```

6. `<aside>`: Use the `aside` tag when you want to define content that is related to the main content but not part of it, such as sidebars, advertisements, or related links.
    

Example:

```html
<aside>
  <h3>Related Links</h3>
  <ul>
    <li><a href="#">Link 1</a></li>
    <li><a href="#">Link 2</a></li>
    <li><a href="#">Link 3</a></li>
  </ul>
</aside>
```

7. `<footer>`: Used to define the footer of a webpage, typically containing copyright information, contact details, or links to related pages.
    

Example:

```html
<footer>
  <p>&copy; Nuel Cas Website</p>
</footer>
```

### List Tag

Lists `<li>` allow you to organize and structure content in a hierarchical manner. They are two types: ordered `<ol>` (numbered) and unordered (`<ul>`) (bulleted) lists.

Ordered List: Use `<ol>` for ordered lists, and `<li>` for list items.

Example:

```html
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```

This will render as:

1. First item
    
2. Second item
    
3. Third item
    

Unordered List: The `<ul>` tag is used to create an unordered list, where the order of the items doesn't matter, it renders bulleted items. Each item in the list is represented by the `<li>` (list item) tag.

Example:

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

This will render as:

* Item 1
    
* Item 2
    
* Item 3
    

Lists can be nested within each other. For example, you can have an ordered list within an unordered list or vice versa.

Example:

```html
<ul>
  <li>Unordered List Item 1</li>
  <li>Unordered List Item 2
    <ol>
      <li>Ordered List Item 1</li>
      <li>Ordered List Item 2</li>
    </ol>
  </li>
  <li>Unordered List Item 3</li>
</ul>
```

This will render as:

* Unordered List Item 1
    
* Unordered List Item 2
    

1. Ordered List Item 1
    
2. Ordered List Item 2
    

* Unordered List Item 3
    

List items can also have attributes. For example, you might use the `type` attribute with the `<ol>` tag to change the numbering style.

Example:

```html
<ol type="A">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>
```

This will render as:

A. Item 1  
B. Item 2  
C. Item 3

The `<ul>`, `<ol>`, and `<li>` tags in HTML are essential for creating organized lists and structuring content on web pages. They provide flexibility in presenting information in both ordered and unordered formats.

### Span Tag

The `<span>` tag is a generic inline (it does not create a line break) container used to group and apply styles to inline elements or text. It is typically used when you want to apply styles or using JavaScript to manipulate specific portions of text within a larger block of content without affecting the overall structure.

Here's an example of how the `<span>` tag can be used in HTML:

```html
<p>This is a <span style="color: red; font-weight: bold;">highlighted</span> text.</p>
```

In this example, the word "highlighted" will be displayed in red and bold, as specified by the inline styles applied to the `<span>` element.

### Links

The `<link>` tag is used to define a link between a document and an external resource. Its primary purpose is to include external resources, such as stylesheets, icons, and other documents. Let's look at the common use cases of the `<link>` tag:

**Linking stylesheet**: The most common use of the `<link>` tag is to link an external CSS (Cascading Style Sheets) file to an HTML document. This allows you to separate the styling of your website from its structure, making it easier to maintain and update.

Example:

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

In this example, the `rel` attribute specifies the relationship between the HTML document and the linked resource (stylesheet), the `type` attribute indicates the type of the linked resource (`text/css` for stylesheets), and the `href` attribute specifies the path to the external CSS file.

**Note**: Linking a CSS file should be done inside the `<head>` element.

**Linking icon**: The `<link>` tag is also commonly used to link the favicon icon for a webpage, which is the small icon that appears in the browser tab or next to the URL in the address bar.

```html
<link rel="icon" href="favicon.ico" type="image/x-icon">
```

In this case, the `rel` attribute is set to "icon" to indicate that it is an icon file, and the `href` attribute specifies the path to the icon file. The `type` attribute indicates the type of the linked file, in this case, `image/x-icon` for icons.

**Linking external documents**: The `<link>` tag can be used to link other external documents, such as:

1. Stylesheet for printing: Imagine you have a special design for when someone wants to print your webpage. The `<link>` tag can connect your webpage to a separate stylesheet designed just for printing. This way, when someone prints your page, it looks nice and tidy.
    

Example:

```html
<!-- Link to the stylesheet for printing -->
  <link rel="stylesheet" type="text/css" href="print-styles.css" media="print">
```

2. Alternative versions of a document (like translations): Sometimes, you might have different versions of your webpage for different languages or purposes. The `<link>` tag can connect your webpage to these alternative versions.
    

Example:

```html
<link rel="alternate" hreflang="es" href="spanish-version.html">
```

3. Feeds for content syndication: Let's say you have a blog, and you want others to easily see your latest posts. The `<link>` tag can help by connecting your webpage to a feed, which is like a stream of your latest content.
    

Example:

```html
<link rel="alternate" type="application/rss+xml" title="RSS Feed" href="rss-feed.xml">
```

The `<link>` tag is like a connector that helps your webpage interact with other files on the internet.

### Anchor Tag

The anchor tag, represented by `<a>`, is used to create hyperlinks or anchor points within a webpage. It is primarily used to define a hyperlink, allowing users to navigate to another webpage, a different section of the same page, or even an external resource.

The anchor tag uses the `href` attribute to specify the destination URL (Uniform Resource Locator).

Example:

```html
<a href="https://www.example.com">Visit Example.com</a>
```

### Form tag

HTML forms are essential for user interaction on websites. They allow users to input data that can be sent to a server for processing. The basic structure of an HTML form involves several key elements:

```html
<form>
  <!-- Your form elements go here -->
</form>
```

The `<form>` tag marks the beginning and end of your form. It acts as a container for various form elements. It commonly houses label, input types, textarea, and button tags.

#### Label

The `<label>` tag is used to define a label for an input element. Example:

```html
<label for="username">Username:</label>
```

#### Input type

In a form, different input types serve various purposes. The input (`<input>`) tag defines an interactive element for users to enter data. Commonly used ones are:

Text Input:

```html
<input type="text" name="username" placeholder="Enter your username">
```

Password Input:

```html
<input type="password" name="password" placeholder="Enter your password">
```

Radio Buttons:

```html
<input type="radio" name="gender" value="male"> Male
<input type="radio" name="gender" value="female"> Female
```

Checkboxes:

```html
<input type="checkbox" name="subscribe" value="yes"> Subscribe to newsletter
```

#### Textarea

The `<textarea>` tag defines a multi-line text input control, commonly used within form elements. Example:

```python
<textarea name="message" placeholder="Enter your message"></textarea>
```

#### Button (for submitting forms)

The most crucial part of a form is allowing users to submit their input. For this, you can use a button (`<button>`) tag to submit:

Example:

```python
<button type="submit">Submit</button>
```

The `<button>` tag creates a clickable button. The `type="submit"` attribute indicates that clicking this button will submit the form.

### Quick Tips

* Always include a `name` attribute in your form elements. It helps identify and process the data on the server.
    
* Use the `placeholder` attribute to give users a hint about the expected input.
    
* Consider the user experience when choosing input types. For instance, use radio buttons for mutually exclusive options.
    

Here is a code snippet demonstrating usage of a form element:

```html
<form>
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" placeholder="Enter your username">

  <label for="password">Password:</label>
  <input type="password" id="password" name="password" placeholder="Enter your password">

  <label>Gender:</label>
  <input type="radio" name="gender" value="male"> Male
  <input type="radio" name="gender" value="female"> Female

  <label>Subscribe to newsletter:</label>
  <input type="checkbox" name="subscribe" value="yes">

  <label for="message">Your Message:</label>
  <textarea id="message" name="message" placeholder="Enter your message"></textarea>

  <button type="submit">Submit</button>
</form>
```

### Self-closing Tags

The `<input>` or `<input />` element above is a self-closing tag, which means it doesn't require a separate closing tag.

There are other self-closing tags in HTML:

* Image (`<img>` or `<img />`).
    
* Line breaks (`<br>` or `<br />`).
    
* External resource link (`<link>` or `<link />`).
    
* Horizontal rule (`<hr>` or `<hr />`).
    
* Meta data (`<meta>` or `<meta />`).
    
* Table column (`<col>` or `<col />`).
    
* Base URL for relative links (`<base>` or `<base />`).
    
* Word break opportunity (`<wbr>` or `<wbr />`).
    
* Area (`<area>` or `<area />`) which defines an area inside an image map so the image can have a clickable region.
    

Note: HTML5 (latest version of HTML) allows you to omit the slash (`/`) at the end of self-closing tags, but including it ensures compatibility with older standards like XHTML and some tools.

## HTML Attributes

This is an additional information or characteristics that you can apply to HTML elements to modify their behavior, appearance, or define certain properties. Attributes are always included in the opening tag of an HTML element and are written as name-value pairs.

The basic syntax for an HTML attribute is:

```html
<tagname attribute="value">Content</tagname>
```

Here, `attribute` is the name of the attribute, and `"value"` is the value assigned to that attribute.

There are many attributes available for various HTML elements, here are few ones:

### id Attribute

It provides a unique identifier for an HTML element. It should be unique within the entire HTML document.

"id" attribute helps you uniquely identify and control specific elements on a webpage, just like how each student's ID number helps identify them uniquely in a school.

Example:

```html
<div id="header">This is a div with an id attribute.</div>
```

### class Attribute

Used to assign one or more class names to an HTML element. It also helps you organize and style different parts of a webpage by grouping them together.

Here is the syntax for class attribute:

```html
<tagname class="classname1 classname2 ...">Content</tagname>
```

Suppose you want to style multiple paragraphs with the same font and color. Instead of writing the same CSS styles for each paragraph individually, you can assign a common class to all those paragraphs and define the styles for that class in your CSS file. Example:

```html
<body>
  <p class="highlight">This is the first paragraph.</p>
  <p class="highlight">This is the second paragraph.</p>
  <p class="highlight">This is the third paragraph.</p>
</body>
```

**Note**: The "id" attribute and the "class" attribute in HTML serve similar purposes in that they both allow you to uniquely identify elements on a webpage. However, there are key differences between the two:

* Use the "id" attribute when you need to uniquely identify a single element.
    
* Use the "class" attribute when you want to group multiple elements together and apply styling or functionality to them collectively.
    

While both attributes can be used for styling, the "id" attribute is more suitable for unique styling, while the "class" attribute is ideal for applying consistent styles to multiple elements.

### src (source) Attribute

It specifies the source URL of an image to be displayed. Example:

```html
<img src="image.jpg" alt="Nuel Cas Photo">
```

**Note**: The `alt` attribute is used to provide alternative text for an image if the image fails to load. It serves as a descriptive text that is displayed in place of the image, helping users understand the content or purpose of the image even when it's not visible.

### href Attribute (for links)

It specifies the URL that the hyperlink points to. Example:

```html
<a href="https://www.nuelcas.com">Visit Nuel Cas</a>
```

### width and height Attribute (for images)

It determines the width and height of an image in pixels. Example:

```html
<img src="image.jpg" alt="Nuel Cas Photo" width="400" height="300">
```

### style Attribute

Allows you to apply inline CSS styles to an HTML element. Example:

```html
<p style="color: red; font-size: 18px;">This is a red text.</p>
```

### disabled Attribute (for form elements)

Allows you to disable user interaction with form element. Example:

```html
<input type="text" disabled>
```

### type Attribute (for form element and list items)

You can use the `type` attribute with the `<ol>` tag to change the numbering style. Example:

```html
<ol type="A">
  <li>Item A</li>
  <li>Item B</li>
  <li>Item C</li>
</ol>
```

This will render as:

```text
A. Item A
B. Item B
C. Item C
```

Also, you can use `type` attribute to specify the input type of form element. Say you want to notify the browser that this input is for password, use the code below

```python
<input type="password" name="password" placeholder="Enter your password">
```

### name attribute (for form element)

The `name` attribute provides a unique identifier for each form field. When the form is submitted to the server, the data entered into each field is sent with the corresponding name as a *key-value* pair. The code snippet below shows that you want the server to identify this input as email.

```python
 <input type="email" id="email" name="email" placeholder="Enter your email">
```

**Note**: Understanding and using attributes effectively is essential for controlling the appearance and behavior of elements in your HTML documents.

## HTML Multimedia

You may need to integrate various types of media content into web pages, such as images, audio, and video. These media elements enhance the user experience by making web content more engaging and dynamic.

Here are the different types of multimedia you can use in HTML:

### Images

Images are the most common type of multimedia in HTML. You can add images to a web page using the `<img>` tag. Example:

```html
<img src="image.jpg" alt="Description of the image" width="200" height="150">
```

In the above example, `src` specifies the source URL of the image, `alt` provides alternative text for accessibility and SEO, and `width` and `height` are optional attributes to set the dimensions of the image.

### Audio

You can embed audio files directly into a web page using the `<audio>` tag. This allows you to play audio clips, music, or other sound recordings. Example:

```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  Your browser may not support the audio element.
</audio>
```

In the above example, `controls` provides play, pause, and volume controls for the user, `src`specifies the source URL of the audio file, while `type` specifies the [MIME](https://en.wikipedia.org/wiki/MIME) (Multipurpose Internet Mail Extensions) type of the audio file.

### Video

The `<video>` tag is used to embed video files into a web page. This allows you to play videos within the content. Example:

```html
<video controls width="640" height="360">
  <source src="video.mp4" type="video/mp4">
  Your browser may not support the video element.
</video>
```

In the above example, `controls` provides play, pause, and volume controls for the user, `width` and `height` specifies the dimensions of the video, `src` specifies the source URL of the video file, while `type` specifies the MIME type of the video file.

### iframe

`<iframe>` allows you to display content from a different source or page inside a frame on your webpage. This can be useful for embedding videos, maps, web pages, or other external content. Example using `<iframe>` to embed a video from YouTube:

```html
<iframe 
  src="https://www.youtube.com/embed/VIDEO_ID" 
  width="560" 
  height="315" 
  title="YouTube Video" 
  frameborder="0" 
  allowfullscreen>
</iframe>
```

In the above code snippet, `src` attribute specifies the URL of the page or content you want to embed. Sizes are controlled using the `width` and `height` attributes. `title` attribute provides a description for the content, which is important for accessibility.

The `frameborder` attribute controls whether the iframe has a border (0 for no border, 1 for a border), while the `allowfullscreen` attribute allows the video to be played in full-screen mode.

**Note**: Replace `"VIDEO_ID"` with the ID of the YouTube video you want to embed.

## Best Practices

1. Follow proper HTML document structure:
    

* Start your HTML document with a `<!DOCTYPE html>` declaration to ensure browser compatibility and standards compliance.
    
* Always include the `<html>`, `<head>`, and `<body>` tags in your document.
    
* Use the `<meta charset="UTF-8">` tag to specify the character encoding of your document.
    
* Define the language of your document using the language (`<html lang="en">`) attribute.
    
* Include a descriptive title (`<title>`) tag within the head (`<head>`) section to provide context for the page.
    

2. Use semantic HTML element:
    

* Utilize semantic HTML elements like `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, and `<footer>` to provide clarity and structure to your content. Semantic elements improve accessibility, SEO, and maintainability of your code.
    

3. Comment your code:
    

* Use comments `<!-- -->` to document your HTML code, explaining its purpose and functionality. Comments improve code readability and facilitate collaboration among developers.
    

4. Structure your content with proper tags:
    

* Use heading tags `<h1>` to `<h6>` for defining the hierarchy of your content.
    
* Utilize paragraph tags `<p>` to separate blocks of text into distinct paragraphs.
    
* Employ lists (`<ul>`, `<ol>`, `<li>`) to organize and structure content in a hierarchical manner.
    

5. Group elements with `<div>` and `<span>` sparingly:
    

* Use `<div>` and `<span>` tags as needed to group and style elements, but avoid excessive nesting and over-reliance on these elements. Prefer more semantic alternatives where appropriate.
    

6. Do not overuse line breaks (`<br>`):
    

* While `<br>` tags can be useful for simple line breaks, avoid overusing them for layout purposes. Instead, use CSS and block-level elements for more complex layouts to maintain better code readability and maintainability.
    

7. Always use alternative text for images (`alt` attribute):
    

* Always include descriptive alternative text using the `alt` attribute for images (`<img>` tags). This improves accessibility for users with visual impairments and ensures that content remains understandable even if images fail to load.
    

8. Optimize forms for user experience (UX):
    

* Include meaningful `name` attributes for form elements to identify and process data accurately on the server.
    
* Utilize appropriate input types (`type` attribute) for form fields to enhance user experience and ensure data validation.
    
* Use the `placeholder` attribute to provide hints or expected input for form fields.
    

9. Ensure compatibility with older browsers:
    

* Your code should undergo [compatibility testing](https://www.freecodecamp.org/news/cross-browser-compatibility-testing-best-practices-for-web-developers/) across different browsers and devices to ensure consistent rendering and functionality.
    
* Include appropriate fallbacks for newer HTML features or attributes, this will help maintain compatibility with older browsers.
    

10. Stay updated with HTML standards:
    

* Keep yourself updated with the latest HTML standards and best practices to leverage new features, improve performance, and enhance the user experience of your web applications.
    

By adhering to these best practices, you can create well-structured, accessible, and maintainable HTML code that contributes to the overall quality and usability of your web projects.

#### If you have read, enjoyed, and desire more of this piece, feel free to reach out to me on [X](https://twitter.com/casweb_dev) and [LinkedIn](https://www.linkedin.com/in/casmir-onyekani/) for further collaboration.
