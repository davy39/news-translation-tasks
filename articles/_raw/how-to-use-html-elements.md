---
title: How to use HTML Elements – Headings, Paragraphs, and Text Formatting Elements
  Example
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-09-26T18:02:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-html-elements
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Pink-Minimalist-Digital-Marketing-Presentation.png
tags:
- name: beginner
  slug: beginner
- name: HTML
  slug: html
seo_title: null
seo_desc: HTML, which stands for HyperText Markup Language, is the standard markup
  language used to create webpages. HTML provides a structured way to organize content
  on a webpage, allowing web developers to present text and media in a clear and meaningful
  wa...
---

HTML, which stands for HyperText Markup Language, is the standard markup language used to create webpages. HTML provides a structured way to organize content on a webpage, allowing web developers to present text and media in a clear and meaningful way. 

In this article, we'll explore three fundamental HTML elements: headings, paragraphs, and text formatting elements, and learn how they play a crucial role in web content presentation. 

## How to use HTML Elements

Understanding HTML elements is foundational for anyone interested in web development. HTML relies on elements as the building blocks of web pages. Each element has a specific purpose and structure, contributing to the overall layout and functionality of a webpage. 

Elements can range from basic components like headings, paragraphs, and text formatting elements, to more complex ones such as links, forms, tables, and multimedia embeds. 

Learning how to use these elements, their attributes, and the proper nesting and hierarchy is essential for creating well-structured, accessible, and visually appealing web content. Let's go ahead and discuss some HTML elements in more detail.

### How to Structure Content with Headings in HTML

Headings in HTML serve the essential purpose of structuring content. They play a vital role in organizing and categorizing information, making it more comprehensible for both human users and search engine algorithms. 

HTML offers a total of six hierarchical levels of headings, ranging from `<h1>` to `<h6>`, each with a unique significance. `<h1>` is the highest level, typically used for the main title or primary section of a webpage, while `<h6>` represents the lowest level, usually reserved for sub-subsections or minor details within the content. 

By using these heading tags thoughtfully and hierarchically, web developers can create a visual and structural hierarchy that guides readers through the content's flow and importance, facilitating better comprehension and navigation. Properly structured headings also enhance the accessibility of web content, as they provide screen readers with vital cues about the content's structure and hierarchy.

Here's an example of how headings are used:

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Headings</title>
</head>
<body>
    <h1>Main Heading</h1>
    <p>This is some content under the main heading.</p>
    
    <h2>Subheading</h2>
    <p>More content under the subheading.</p>
</body>
</html>

```

In this example, we have a `<h1>` for the main heading and `<h2>` for the subheading. This hierarchy helps both search engines and screen readers understand the structure of the content, making it more accessible and SEO-friendly.

### Tips and Best Practices for using Headings in HTML

Here are some tips you should keep in mind when using heading in HTML:

**Use Headings Sequentially**: It's essential to use headings in sequential order. Start with an `<h1>` for the main title or section, followed by `<h2>` for subsections, `<h3>` for sub-subsections, and so on. This helps maintain a logical and organized structure.

**Avoid Skipping Levels**: Don't skip heading levels. For instance, don't use `<h1>` followed by `<h3>` without an `<h2>` in between. Skipping levels can confuse both users and search engines.

**Don't Overuse `<h1>`**: While `<h1>` is the highest-level heading and should represent the main topic of the page, avoid using it multiple times on a single page. It's better to use it only once for the primary title.

**Use Semantic Headings**: Choose headings that semantically represent the content they enclose. For example, use `<h3>` for subheadings that are less important than the main topic but more important than subsections.

**Consider Accessibility**: Ensure your headings are meaningful to users who rely on screen readers. They should provide a clear outline of the content's structure. Avoid using headings solely for styling purposes.

**Test Responsiveness**: Check how your headings appear on different devices and screen sizes. Ensure they remain legible and maintain the intended structure.

### How to Organize Text with Paragraphs in HTML

Paragraphs in HTML, represented by the `<p>` element, serve as the fundamental means of organizing textual content on webpages.  They are used to group together related text content. By wrapping text in `<p>` tags, you indicate that this content forms a cohesive unit. 

These tags play a crucial role in enhancing the readability and comprehension of the information presented. By encapsulating text within `<p>` tags, web developers signal to both browsers and readers that the enclosed content is a coherent and standalone unit of information. 

This structured approach not only separates different ideas or topics but also provides natural spacing and line breaks before and after each paragraph, ensuring a clean and visually appealing layout. 

Whether you're crafting articles, descriptions, or explanations, using `<p>` elements helps maintain a logical and organized flow of text. This ultimately contributes to a more user-friendly and accessible web experience. Paragraphs automatically add spacing before and after the text they contain, making each one visually distinguishable from the surrounding content.

Here's an example of how paragraphs are used:

```html
<p>This is a paragraph of text. It can contain multiple sentences</p>
<p>Another paragraph here, keeping the content organized.</p>

```

_Result:_

<p>This is a paragraph of text. It can contain multiple sentences</p>
<p>Another paragraph here, keeping the content organized.</p>

### Tips and Best Practices for using Paragraphs in HTML

**Use for Text Content**: Use `<p>` elements for text content, including plain text, articles, descriptions, and more. It helps maintain readability and separates different ideas or topics.

**Avoid Excessive Line Breaks**: Don't use multiple `<p>` elements with just a few words each. If text logically belongs together, keep it within a single paragraph.

**Maintain Consistent Formatting**: Keep the formatting of paragraphs consistent throughout your website. This includes consistent line spacing, font size, and text alignment.

**Avoid Using `<p>` for Headings**: While `<p>` elements are for text content, avoid using them to simulate headings. Use heading tags `<h1>` to `<h6>` for headings instead.

**Use Semantic Markup**: When using paragraphs, ensure that they convey the intended meaning of the content. For example, use paragraphs for introductory text, explanations, or body content.

**Check Mobile Readability**: Ensure that paragraphs are readable on mobile devices without excessive horizontal scrolling or zooming.

### How to Enhance Readability with Text Formatting Elements in HTML

HTML provides various elements for text formatting to enhance the readability and visual appeal of your content. These formatting elements provide both aesthetic improvements and semantic meaning to your text, making it more engaging and accessible to your audience.

Here are some of the formatting elements in HTML:

#### How to use Bold and Italics Formatting Elements

You can make text **bold** using the `<b>` element or _italic_ using the `<em>` element.

```html
<p>This text is <b>bold</b>, and this text is <em>italic</em>.</p>

```

Result:

<p>This text is <b>bold</b>, and this text is <em>italic</em>.</p>

However, it's essential to note that when emphasizing text for semantic purposes, it's generally better to use the `<strong>` element to provide both visual styling and semantic meaning. Use `<b>` when the primary goal is merely to make the text bold for stylistic reasons.

#### How to use Underline and Strikethrough Formatting Elements

Text can also be underlined using the `<u>` element, and you can strikethrough using the `<s>` or `<strike>` element (deprecated in HTML5 but still widely supported).

```html
<p>This text is <u>underlined</u>, and this text is <s>strikethrough</s>.</p>

```

Result:

<p>This text is <u>underlined</u>, and this text is <s>strikethrough</s>.</p>


#### How to use Superscript and Subscript Formatting Elements

Superscript and subscript text can be achieved with the `<sup>` and `<sub>` elements, respectively.

```html
<p>Water is H<sub>2</sub>O, and E=mc<sup>2</sup>.</p>

```

Result:

<p>Water is H<sub>2</sub>O, and E=mc<sup>2</sup>.</p>

#### How to use Code and Keyboard Input Elements

To display code or keyboard input, you can use the `<code>` and `<kbd>` elements.

```html
<p>To open a file in the terminal, type <code>cd folder</code>. To save, press <kbd>Ctrl + S</kbd>.</p>

```

<p>To open a file in the terminal, type <code>cd folder</code>. To save, press <kbd>Ctrl + S</kbd>.</p>

### Tips and Best Practices for using Text Formatting Elements in HTML

**Use Formatting Sparingly**: While text formatting can make content visually appealing, don't overdo it. Excessive use of bold, italics, or other formatting elements can make the page look cluttered and distract readers from the intended message.

**Maintain Readability**: The primary goal of text formatting is to enhance readability. Ensure that formatted text remains legible and doesn't strain the reader's eyes.

**Combine Formatting**: Combine different formatting elements when necessary. For example, you can use `<strong>` for emphasis within a paragraph that's already in italics using `<em>`.

**Semantic Meaning**: Use formatting elements to convey semantic meaning. For instance, use `<em>` for emphasizing text and `<strong>` for indicating strong importance.

**Use CSS for Styling**: While HTML provides basic text formatting, CSS (Cascading Style Sheets) is the preferred method for styling web content. CSS gives you more control over fonts, colors, and spacing.

These text formatting elements provide not only visual enhancement, but also semantic meaning to your content, which can be important for screen readers and search engine optimization.

## Conclusion

HTML elements like headings, paragraphs, and text formatting tags are essential tools for structuring and presenting content on the web. They provide clarity, hierarchy, and readability to your webpages, making them accessible to both humans and machines. 

As you dive deeper into web development, mastering these fundamental elements will be crucial for creating well-structured and user-friendly websites. Remember to follow best practices to ensure your HTML content is not only functional but also visually appealing and accessible to a wide range of users.

### Recommended Learning Resources

[The freeCodeCamp Responsive Web Design Certification](https://www.freecodecamp.org/learn/2022/responsive-web-design/)

[The HTML Handbook for Beginners](https://www.freecodecamp.org/news/the-html-handbook/)

[HTML & Coding Introduction – Video Course for Beginners](https://www.freecodecamp.org/news/html-coding-introduction-course-for-beginners/)

