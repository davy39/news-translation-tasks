---
title: HTML Lists – Ordered, Unordered and Definition List Examples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-04T16:01:18.000Z'
originalURL: https://freecodecamp.org/news/html-lists-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Blue-And-White-Modern-Effective-Leadership-In-Business-Presentation.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Imagine you're creating an article with a list of recommendations or a\
  \ web page with a menu of options. How do you structure this information to make\
  \ it visually appealing and easy to navigate? \nThis is where HTML lists come to\
  \ the rescue. In this ar..."
---

Imagine you're creating an article with a list of recommendations or a web page with a menu of options. How do you structure this information to make it visually appealing and easy to navigate? 

This is where HTML lists come to the rescue. In this article, we'll dive into the world of HTML lists and explore how they can help you organize and present your content effectively.

## The Basics of HTML Lists

HTML lists come in three main categories: **unordered lists**, **ordered lists**, and **definition lists**. Each type serves a specific purpose and can be customized to fit your design and content needs.

### How to create unordered lists

Unordered lists are perfect for presenting items that do not have a particular sequence or order. They are typically displayed with bullet points, which make them visually distinct from ordered lists. An example might be a grocery shopping list.

To create an unordered list, you can use the `<ul>` (unordered list) element and nest individual list items within `<li>` (list item) elements:

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

```

This code will generate a simple unordered list like this:

* Item 1
* Item 2
* Item 3

You can further customize the appearance of bullet points using CSS to match your website's style.

### How to create ordered lists

Ordered lists, as the name suggests, are useful when you want to present items in a specific sequence or order. They are displayed with numbers or letters by default, but you can customize the numbering style using CSS. An example might be a ranked list of your favorite movies.

To create an ordered list, use the `<ol>` (ordered list) element and nest list items within `<li>` elements:

```html
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>

```

This code will produce an ordered list like this:

1. First item
2. Second item
3. Third item

Ordered lists are useful for creating step-by-step instructions, ranking items, or any situation where a specific order matters.

### How to create definition lists

Definition lists are designed to present terms and their corresponding definitions. They consist of a list of terms enclosed in `<dt>` (definition term) elements and their associated definitions enclosed in `<dd>` (definition description) elements. Here's an example:

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language, used for structuring content on the web.</dd>
  
  <dt>CSS</dt>
  <dd>Cascading Style Sheets, used for styling web documents.</dd>
  
  <dt>JavaScript</dt>
  <dd>A programming language used for adding interactivity to web pages.</dd>
</dl>

```

This code will create a definition list like this:

**HTML**  
HyperText Markup Language, used for structuring content on the web.

**CSS**  
Cascading Style Sheets, used for styling web documents.

**JavaScript**  
A programming language used for adding interactivity to web pages.

Definition lists are particularly handy for glossaries and dictionaries, where you need to pair terms with their meanings.

## How to Customize Lists with CSS

HTML provides the basic structure for lists, but to make them visually appealing and fit your website's design, you can apply CSS styles. Here are some common CSS properties you can use to customize lists:

### Changing the Bullet or Number Style

To change the style of bullets in unordered lists or the numbering style in ordered lists, you can use the `list-style-type` property. For example, to use square bullets in an unordered list, you can add the following CSS rule:

```css
ul {
  list-style-type: square;
}

```

With this CSS applied, the unordered list will look like this:

<ul style="list-style: none;">
  <li>&#9632; Item 1</li>
  <li>&#9632; Item 2</li>
  <li>&#9632; Item 3</li>
</ul>


### Adding Margins and Padding

You can control the spacing around list items by adjusting the `margin` and `padding` properties. For instance, you can add space between list items like this:

```css
li {
  margin-bottom: 10px;
}

```

With this CSS rule, the list items will have extra space between them, making the list more readable.

### Styling List Items

You can style individual list items differently by targeting them directly using CSS. For instance, you can change the color of list items when users hover over them:

```css
li:hover {
  color: blue;
}

```

With this CSS, the list items will change their color to blue when a user hovers over them, providing visual feedback.

### Creating Custom Icons

If you want to use custom icons instead of the default bullets for unordered lists, you can achieve this with CSS by using the `::before` pseudo-element. This allows you to add custom content before each list item. Here's an example of how you can use a custom checkmark icon:

```css
ul {
  list-style: none; /* Remove default bullets */
}

li::before {
  content: "✔"; /* Unicode checkmark symbol */
  margin-right: 5px; /* Add spacing between icon and text */
}

```

With this CSS applied, the unordered list will have custom checkmark icons before each item, like this:

✔ Item 1  
✔ Item 2  
✔ Item 3

## How to Make Lists More Accessible

It's essential to consider accessibility when designing lists. Proper HTML semantics and CSS can make lists more accessible to screen readers and other assistive technologies. 

### Semantic Elements:

You'll want to make sure that you use semantic elements correctly to provide context to users who rely on screen readers. For example:

```html
<ol>
  <li><strong>Step 1:</strong> Prepare your ingredients</li>
  <li><strong>Step 2:</strong> Preheat the oven to 350°F</li>
  <li><strong>Step 3:</strong> Mix the dry ingredients</li>
</ol>

```

In this ordered list, `<strong>` elements are used within list items to emphasize important steps. This not only makes the list more visually appealing but also enhances the understanding of the content for screen readers.

### ARIA Roles and Labels:

For more complex lists or when additional accessibility information is needed, you can use ARIA (Accessible Rich Internet Applications) attributes. For example:

```html
<ul role="list" aria-label="Features">
  <li role="listitem">Responsive design</li>
  <li role="listitem">Accessibility</li>
  <li role="listitem">Cross-browser compatibility</li>
</ul>

```

In this unordered list, the `role` attribute is set to "list" to indicate that it's a list, and the `aria-label` attribute provides a label for the list. These attributes assist screen readers in properly interpreting and conveying the list's purpose and content.

## Conclusion

Incorporating HTML lists into your web content is a powerful way to organize information, create engaging interfaces, and enhance user experiences. 

By understanding the different types of lists – unordered, ordered, and definition lists – and knowing how to style them with CSS, you have the tools to make your content more visually appealing and user-friendly.

Incorporate lists into your HTML documents wisely, considering both design and accessibility. Use CSS to fine-tune their appearance to align with your website's style, and ensure that everyone, regardless of their abilities, can navigate your content effortlessly.

Remember, lists are more than just bullet points or numbers. They are a cornerstone of effective web design and communication.

## Get Hands-On

Now that you've learned about HTML lists, why not try creating your own lists in an HTML document? Experiment with different styles and see how CSS can transform the look of your lists. Practice is key to mastering this essential web development skill.

