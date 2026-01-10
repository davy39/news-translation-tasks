---
title: HTML textarea – How to Add a Text Box Input Type Tag to Your Website
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-26T16:21:53.000Z'
originalURL: https://freecodecamp.org/news/html-textarea-how-to-add-text-box-to-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template--3-.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: A text box is a section of your website where users can enter text. A blinking
  cursor appears when you click or tap on or inside the text box, indicating that
  you are ready to begin typing. And an on-screen keyboard will appear if you're using
  a tabl...
---

A text box is a section of your website where users can enter text. A blinking cursor appears when you click or tap on or inside the text box, indicating that you are ready to begin typing. And an on-screen keyboard will appear if you're using a tablet or smartphone.

Text boxes are classified into two types: text fields and text areas. These two text boxes serve different purposes and help your user understand what they should be typing into the text box.

A text field is a small, typically rectangular box where you can enter a single line of text, such as a name, number, or any other short text type.

A text area is a larger box where you can enter multiple lines of text, such as descriptions, paragraphs, and so on.

When you tap the enter button in a text field, the cursor will either move to the following field or submit the form. In a text area, on the other hand, the cursor will move to a new line, creating a line break.

![](https://paper-attachments.dropbox.com/s_64572030E8D25CA21F18BD5EC8523ECF39BB95CA9E14781CDD6E156EE366692C_1661531495728_Untitled.drawio+1.png align="left")

## How to Add a Text Field to Your Website

Whenever you want a user to input something into a webpage, you can use the `<input>` tag. Then, to ensure this is a text field, you can add the type attribute of `text`:

```html
<form>
  <input type='text' />
</form>
```

This will output a single-line text field on our web page, which can take in all forms of text values. We can also add a label tag or other attributes like the `placeholder` attribute to let users know what to input in the text field.

```html
<form>
  <input type='text' placeholder='Enter your name...' />
</form>

Or

<form>
  <label>Name:</label> </br>
  <input type='text' />
</form>
```

There are many more attributes we can define on a text field, such as the `maxlength` and `minlength`, to help define the maximum or the minimum amount of text a field can accept.

```html
<form>
  <input type='text' maxlength="100" minlength="10" placeholder='Enter your name' />
</form>
```

We can also pass in default values to our text filed with the value attribute:

```html
<form>
  <input type='text' value='John Doe' placeholder='Enter your name...' />
</form>
```

![](https://paper-attachments.dropbox.com/s_64572030E8D25CA21F18BD5EC8523ECF39BB95CA9E14781CDD6E156EE366692C_1661546622536_image.png align="left")

## How to Add a Text Area to Your Website

A text area is defined by a `<textarea>` tag. You use it to collect unlimited multi-line text like comments or reviews.

You specify the size of a text area by the `cols` and `rows` attributes (or with CSS).

```html
<form>
  <textarea rows="5" cols="33"></textarea>
</form>
```

The textarea field does not use the value attribute to pass in default values, but you can place default content between the opening and closing tags.

```html
<form>
  <textarea rows="5" cols="33">
    This is the default comment...  
  </textarea>
</form>
```

![](https://paper-attachments.dropbox.com/s_64572030E8D25CA21F18BD5EC8523ECF39BB95CA9E14781CDD6E156EE366692C_1661546930588_image.png align="left")

Like the input tags, we can add the `maxlength`, `minlength` and `placeholder` attributes to the textarea field.

```html
<form>
  <textarea placeholder='Enter comment...' maxlength='1000' minlength='100'>
    This is the default comment...  
  </textarea>
</form>
```

## Conclusion

In this article, you have learned how to add a text box to your website using the `<textarea/>` and `<input/>` tags, depending on the `type` of `text` you wish to add.

You can learn more about HTML tags in the following resources:

* [HTML for Beginners - freeCodeCamp](https://www.freecodecamp.org/news/html-crash-course/#:~:text=Common%20HTML%20Tags&text=html%20%3A%20After%20the%20doctype%2C%20all,the%20name%20of%20your%20page.)
    
* [What are HTML Tags, and How Do You Use Them?](https://www.freecodecamp.org/news/html-elements-explained-what-are-html-tags/)
    
* [HTML Cheat Sheet – HTML Elements List Reference](https://www.freecodecamp.org/news/html-cheat-sheet-html-elements-list-reference/)
    

Have fun coding!
