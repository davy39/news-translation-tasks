---
title: Learn HTML – Responsive Web Design Study Guide
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-06-27T16:41:05.000Z'
originalURL: https://freecodecamp.org/news/freecodecamp-responsive-web-design-study-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/jackson-sophat-wUbNvDTsOIc-unsplash.jpg
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'HTML (HyperText Markup Language) is an important markup language for building
  websites. HTML represents the content of the web page.

  But when you are learning this information for the first time, it can be hard to
  keep track of all of the different H...'
---

HTML (HyperText Markup Language) is an important markup language for building websites. HTML represents the content of the web page.

But when you are learning this information for the first time, it can be hard to keep track of all of the different HTML elements. 

In this article, I have created a study guide for the entire [Learn HTML by Building a Cat Photo App practice project](https://www.freecodecamp.org/learn/2022/responsive-web-design/#learn-html-by-building-a-cat-photo-app). This study guide is filled with additional information, links, and videos to help you understand the concepts better. 

Feel free to reference this guide as you go through the certification. If you are interested in a detailed introduction into HTML, please read through [this freeCodeCamp HTML article](https://www.freecodecamp.org/news/what-is-html-what-does-html-stand-for-solved/). 

Here is the complete list of topics covered. Click on any of the links below to learn more about the topic. 

## Table of Contents

* [Heading elements - Steps 1-2, 17, 18,25,33](#heading-heading-elements)
* [Paragraph elements - Step 3](#heading-paragraph-elements)
* [HTML comments - Step 4](#heading-html-comments)
* [Main element - Step 5](#heading-main-element)
* [HTML indentation - Step 6](#heading-html-indentation)
* [Image elements - Steps 7-9, 21,28,29](#heading-image-elements)
* [Anchor elements - Steps 10-11,63](#heading-anchor-elements)
* [Nesting anchor elements inside paragraphs - Step 12](#heading-nesting-anchor-elements-inside-paragraphs)
* [Target attributes - Step 13](#heading-target-attributes)
* [Nesting images inside anchor tags - Step 14](#heading-nesting-images-inside-anchor-tags)
* [Section elements - Steps 15-16,32](#heading-section-elements)
* [Unordered List elements - Steps 19-20](#heading-unordered-list-elements)
* [Figure and Figcaption elements - Steps 22-23,27,30](#heading-figure-and-figcaption-elements)
* [Emphasis Elements - Step 24](#heading-emphasis-elements)
* [Ordered List elements - Step 26](#heading-ordered-list-elements)
* [Strong elements - Step 31](#heading-strong-elements)
* [Form elements - Steps 34-35](#heading-form-elements)
* [Form text inputs and submit buttons  - Steps 36-42](#heading-form-text-inputs-and-submit-buttons)
* [Form radio buttons - Steps 43,47,48](#heading-form-radio-buttons)
* [Label elements - Steps 44-46,55](#heading-label-elements)
* [Fieldset and Legend elements - Steps 49-52](#heading-fieldset-and-legend-elements)
* [Form checkbox elements - Steps 53-54,56-58](#heading-form-checkbox-elements)
* [Value and checked attributes - Steps 59-60](#heading-value-and-checked-attributes)
* [Footer elements - Steps 61-62](#heading-footer-elements)
* [Head and title element - Steps 64-65](#heading-head-and-title-elements)
* [lang attribute - Step 66](#heading-lang-attribute)
* [DOCTYPE - Step 67](#heading-doctype)

## Additional HTML resources

* [Learn HTML – Full Tutorial for Beginners (2022)](https://www.youtube.com/watch?v=kUMe1FH4CHE)
* [HTML Full Course - Build a Website Tutorial](https://www.youtube.com/watch?v=pQN-pnXPaVg)
* [HTML Tutorial - How to Make a Super Simple Website](https://www.youtube.com/watch?v=PlxWf493en4)

## Heading elements

HTML heading elements represent the main heading and subheadings of a web page. 

The `h1` element represents the most important heading and should only be used once per web page.

```html
<h1>I represent the main heading of a web page</h1>
```

The `h2` element represents the second most important heading on the page.

```html
<h2>I am the second most important heading element</h2>
```

There are a total of six section heading elements. 

```html
<h1>I am the most important heading element</h1>
<h2>I am the second most important heading element</h2>
<h3>I am the third most important heading element</h3>
<h4>I am the fourth most important heading element</h4>
<h5>I am the fifth most important heading element</h5>
<h6>I am the least important heading element</h6>
```

This is what it looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-9.19.27-PM.png)

To learn more about heading elements, please read through this [DevDocs detailed heading elements explanation](https://devdocs.io/html/element/heading_elements). 

## Paragraph elements

Paragraph elements represent the paragraphs on a web page.

```html
<p>I love learning with freeCodeCamp. They have thousands of free articles and videos to help me learn how to code.</p>
```

This is what it looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-9.55.21-PM.png)

To learn more about paragraph elements, please read through this [DevDocs `p` element detailed explanation](https://devdocs.io/html/element/p). 

## HTML comments

HTML comments can be helpful in code when you need to leave messages for your future self or other developers reading your code. Comments will not be rendered to the web page.

```html
<!--I am a comment. I am not displayed on the web page.-->
<p>I am a paragraph element.</p>
```

This is what the result looks like rendered to the web page. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-10.10.32-PM.png)

To learn more about HTML comments, I suggest reading through these helpful articles.

* [Comment out HTML – Code Example](https://www.freecodecamp.org/news/comment-out-html-code-example/)
* [HTML Comment – How to Comment Out a Line or Tag in HTML](https://www.freecodecamp.org/news/html-comment-how-to-comment-out-a-line-or-tag-in-html/)

## Main element

The `main` element is used to group all of the main content of the web page.

```html
<h1>What freeCodeCamp has to offer</h1>
<main>
  <p>The core freeCodeCamp curriculum teaches full stack JavaScript and Python. There are hundreds of lessons to go through to get you ready for an entry level developer job.</p>

  <p>freeCodeCamp has thousands of free articles on their news publication. They also have hundreds of videos on their YouTube channel.</p>
</main>
```

This is what the code looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-10.34.18-PM.png)

To learn more about the `main` element, please read through this [DevDocs detailed `main` element explanation](https://devdocs.io/html/element/main). 

## HTML indentation

Whenever you have HTML elements nested inside other HTML elements, it's best to use indentation. Nested elements are known as children of their parent element.

Indentation is used to make your code more readable by other developers. To indent your code, you will move the element two spaces to the right. 

This is an example **without** indentation. 

```html
<main>
<h2>Let's learn about indentation</h2>
<p>There is no indentation here</p>
</main>
```

But if I edit the code by moving the `h2` and `p` elements two spaces to the right, now we have proper indentation.

```html
<main>
  <h2>Let's learn about indentation</h2>
  <p>This is indentation</p>
</main>
```

Now we can see that the `h2` and `p` elements are children of the `main` element.

To learn more about HTML indentation and why it is important, please read through [this helpful indentation article](https://www.freecodecamp.org/news/how-to-indent-in-html-and-why-it-is-important/). 

## Image elements

`img` elements are used to add images to the web page. 

The `src` attribute represents the location of the image and the `alt` attribute is descriptive text for the image. 

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="plate of lasagna">
```

This is the what code looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-11.41.23-PM.png)

To learn more about the `img` element, please read through this helpful [`img` element tutorial](https://www.freecodecamp.org/news/img-html-image-tag-tutorial/). 

## Anchor elements

An anchor element represents a link on the web page. 

Here is the basic syntax:

```html
<a href="link-where-you-want-to-go">anchor text goes here</a>
```

This is what it looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-5.10.07-PM.png)

You use the `href` attribute to tell the hyperlink where to go. 

```html
href="link-where-you-want-to-go"
```

The anchor text is what gets displayed on the screen to users.

Here is an example of an anchor tag that links to freeCodeCamp.

```html
<a href="https://www.freecodecamp.org/">freeCodeCamp</a>
```

This is what it looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-5.41.36-PM.png)

To learn more about HTML anchor elements, I suggest reading through these helpful articles.

* [The HTML <a> Tag – Anchor Tag Example Code](https://www.freecodecamp.org/news/the-html-a-tag-anchor-tag-example-code/)
* [HTML <a> Tag – Anchor Link HREF Example](https://www.freecodecamp.org/news/html-a-tag-anchor-link-href-example/)

## Nesting anchor elements inside paragraphs

If you want to include links inside your paragraphs, then you can nest anchor tags inside the paragraph tags.

In this example we have the text "I love freeCodeCamp".

```html
<p>I love freeCodeCamp</p>
```

If I wanted to turn the word freeCodeCamp into a link, then I would wrap it inside a set of anchor tags.

```html
<p>I love <a href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

This is what the result looks like rendered to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-8.53.45-PM.png)

Nesting links inside paragraph tags is helpful when you want to direct your users to additional information concerning the main content on the page.

To learn more about nesting anchor tags inside paragraphs, I suggest reading through this helpful article.

* [HTML Link – How to Turn an Image into a Link and Nest Links Inside Paragraphs](https://www.freecodecamp.org/news/how-to-turn-text-and-images-into-links-using-html/)

## Target attributes 

You use the `target="_blank"` attribute inside the opening anchor tag like this:

```html
<a href="website-link-goes-here" target="_blank">
```

When the user clicks on the link, a new browser tab will automatically open to that page.

In this example, I have nested a link inside a set of paragraph tags to direct people to freeCodeCamp.

```html
<p>To learn how to code for free, please visit <a href="https://www.freecodecamp.org/learn" target="_blank">freeCodeCamp.org</a></p>
```

When you click on the freeCodeCamp link, then it will open up a new browser tab for you.

%[https://codepen.io/jessica-wilkins/pen/zYRRdmQ]

To learn more about the target attribute, I suggest reading through this helpful article.

* [How to Open a Link in a New Tab – HTML target blank Attribute Explained](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/)

## Nesting images inside anchor tags

In HTML, we can use the `<img>` element to add images on the page. In this example, we are adding an image of five cats.

```html
<img  src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"  alt="Five cats looking around a field."/>
```

![Screen-Shot-2022-06-02-at-10.39.02-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-02-at-10.39.02-PM.png)

  
If we wanted to make that image a clickable link, then we can place it inside a set of anchor tags.

```html
<a href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Five cats looking around a field."/></a>
```

We can also add the `target="_blank"` attribute to have that link open up in a new tab.

```html
<a target="_blank" href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Five cats looking around a field." /></a>
```

When you hover your mouse over the image, you will see the cursor pointer indicating that it is a link directing you to an article about cats.

%[https://codepen.io/jessica-wilkins/pen/XWZYRgy]

## Section elements

The `section` element is used to group sections of content in the HTML document.

Here is an example of the `section` element.

```html
<h1>Let's learn about section elements</h1>
<section>
  <h2>Defintion</h2>
  <p>The section element is used to group sections of content in the HTML document.</p>
</section>
```

This is what the result looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-9.34.22-PM.png)

To learn more about `section` elements, please read through this [DevDocs `section` element detailed explanation](https://devdocs.io/html/element/section). 

## Unordered List elements

The `ul` list element is used to display a list of items in no particular order. The `li` element represents the individual list item. 

Here is an example of a list of food items.

```html
<h2>Favorite foods</h2>
<ul>
  <li>Salad</li>
  <li>Pizza</li>
  <li>Burger</li>
  <li>Carrots</li>
</ul>
```

This is what it looks like rendered to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.07.42-PM.png)

To learn more about the unordered list element, please read through this helpful article. 

* [HTML Bullet Points – How to Create an Unordered List with the <ul> Tag Example](https://www.freecodecamp.org/news/html-bullet-points-how-to-create-an-unordered-list-with-the-ul-tag-example/)

## Figure and Figcaption elements

The `figure` element represents self contained content which is often used with images and captions. The optional `figcaption` is a short descriptive text for the image.

In this example, we have an image of five kittens in the grass with a small caption underneath.

```html
<figure>
  <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Five cats looking around a field." />
  <figcaption>Five kittens looking around in the grass</figcaption>
</figure>
```

This is what it looks like rendered on the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.24.35-PM.png)

To learn more about the `figure` and `figcaption` elements, please read through [this helpful DevDocs explanation](https://devdocs.io/html/element/figure). 

## Emphasis elements

The `em` element is used to place extra emphasis on a section of text. 

In this example we have the sentence, "We need to get out of the building now!"

```html
<p>We need to get out of the building now!</p>
```

If I wanted to place emphasis on the word now, then I can wrap it in `<em>` tags.

```html
<p>We need to get out of the building <em>now</em>!</p>
```

This is what the result looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.38.35-PM.png)

To learn more about emphasis elements, please read through this helpful DevDocs explanation. 

* [The Emphasis element](https://devdocs.io/html/element/em)

## Ordered List elements

The `ol` element is used to display a list of items in a particular order. The `li` element represents the individual list item.

Here is an example of a set of steps for a recipe. 

```html
<h1>How to bake a cake</h1>
<h2>Directions for recipe</h2>
<ol>
  <li>Prep the oven</li>
  <li>Whisk the flour, sugar and cocoa in a bowl</li>
  <li>Mix the milk, vegetable oil, eggs, and vanilla</li>
  <li>Bake for 30 minutes</li>
  <li>Remove from oven, cool for 10 minutes and frost cake</li>
</ol>
```

This is what the result looks like rendered on the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.53.18-PM.png)

To learn more about ordered list elements, please read through this helpful article. 

* [Ordered List in HTML – OL Tag Example](https://www.freecodecamp.org/news/ordered-list-in-html-ol-tag-example/)

## Strong elements

Strong elements are sections of text that represent a sense of urgency or seriousness. 

In this example we have the following sentence:

```html
<p>Danger! Unsafe area ahead</p>
```

We can use `strong` tags to emphasize the strong sense of seriousness of the word "Danger".

```html
<p><strong>Danger!</strong> Unsafe area ahead</p>
```

Here is what the result looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-8.41.09-AM.png)

## Form elements

Form elements are used to collect data from a user like names and email addresses. Examples of forms might be survey forms or forms to join a mailing list. 

Here is the basic syntax for a form:

```html
<form action="url-where-data-should-be-sent-to">
  <!--inputs go inside here-->
</form>
```

The `action` attribute is the URL of where the user data will be sent. Inside the `form` tags, there will be inputs which is where the user provides their information. 

Inputs will be covered more in the next section. 

## Form text inputs and submit buttons

The text `input` is a text field where users can enter in their information. These inputs go inside the `form` element. 

Here is the basic syntax:

```html
<form action="url-where-data-should-be-sent-to">
  <input type="text">
</form>
```

`type="text"` tells the computer that this is a text input. 

Here is what the result looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-9.44.59-AM.png)

The `name` attribute is used to represent the value of the data being submitted. 

```html
<input type="text" name="username">
```

The `placeholder` text is used to provide users information on what should go inside the text inputs. 

In this example, the placeholder text shows users an example username. Once you start typing in the input, the placeholder text disappears. 

```html
  <input type="text" name="username" placeholder="Ex.codergirlrules">
```

%[https://codepen.io/jessica-wilkins/pen/oNqvBmb]

The submit button is used to submit the form information to the server. `type="submit"` tells the computer what type of button it is.

```html
<button type="submit">Submit form</button>
```

The `required` attribute is used to ensure that a user has to fill out the required inputs before submitting the form. If you try to submit a form without completing the required inputs then a message will pop up directing you to fill out that information.

```html
  <input required type="text" name="username" placeholder="Ex.codergirlrules">
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-10.00.04-AM.png)

To learn more about form inputs, please read through this article.

* [HTML Form – Input Type and Submit Button Example](https://www.freecodecamp.org/news/html-form-input-type-and-submit-button-example/)

## Form radio buttons

Radio buttons represent a group of options that a user can choose from. Only one option in that group can be selected at a time. 

Here is the basic syntax:

```html
<input type="radio">
```

This is what it looks like rendered to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-10.20.33-PM.png)

In this example we are using a group of radio buttons where the user can choose between beef, chicken, fish or other. When using a group of radio buttons, all of the buttons in the group must have the same value for the `name` attribute. 

```html
<input type="radio" id="beef" name="food">Beef
<input type="radio" id="chicken" name="food">Chicken
<input type="radio" id="fish" name="food">Fish
<input type="radio" id="other" name="food">Other
```

Try out the example below and notice how you can only select one option at a time. Notice how all of the inputs have the same  `name="food"` value. 

%[https://codepen.io/jessica-wilkins/pen/yLKBPzE?editors=1000]

You can learn more about the radio buttons by reading through [this DevDocs radio button documentation](https://devdocs.io/html/element/input/radio). 

## Label elements

The `label` element associates the label text with the input. 

Here is an example of using the `label` element to associate the text of "Beef" with the input.  

```html
  <label for="beef">Beef</label>
  <input type="radio" id="beef" name="food">
```

The `for` attribute is used to connect the label to the input so when a user clicks on the label text it will select the input. The value of the `for` attribute is the same as the `id` of the input. 

Try out the example below by clicking on the label text. You will see that the radio input is selected. 

%[https://codepen.io/jessica-wilkins/pen/vYRBWdG?editors=1000]

You can also nest the input inside the `label` element. In this case you do not need to use the `for` attribute because the association between the two elements is implicit.

```html
  <label>Beef
    <input type="radio" id="beef" name="food">
  </label>
```

To learn more about the `label` element, please read through this helpful article.

* [HTML Label – Label Tag Example](https://www.freecodecamp.org/news/html-label-label-tag-example/)

## Fieldset and Legend elements

The `fieldset` element is used to group form controls which are inputs and labels. The `legend` element is used to provide a caption for the `fieldset` element. 

Here is an example of the `fieldset` element:

```html
<form action="">
  <fieldset>

  </fieldset>
</form>
```

This is what it looks like rendered to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-11.42.04-PM.png)

Here is an example of the `legend` element:

```html
<form action="">
  <fieldset>
    <legend>Choose your favorite programming language</legend>
  </fieldset>
</form>
```

This is what it looks like rendered to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-11.43.51-PM.png)

Here is the complete example of how the `fieldset` and `legend` elements work with form inputs and labels. 

```html
<form action="">
  <fieldset>
    <legend>Choose your favorite programming language</legend>
      
    <input type="radio" id="JavaScript" name="programming">
    <label for="JavaScript">JavaScript</label>

    <input type="radio" id="Python" name="programming">
    <label for="Python">Python</label>

    <input type="radio" id="Rust" name="programming">
    <label for="Rust">Rust</label>
  </fieldset>
</form>
```

%[https://codepen.io/jessica-wilkins/pen/GRxKypM?editors=1000]

## Form checkbox elements

`checkbox` elements are boxes where a user can select multiple options in a form. 

Here is an example of a checkbox:

```html
    <input type="checkbox" id="London" name="London">
    <label for="London">London</label>
```

This is what is looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-27-at-12.14.29-AM.png)

Here is a full example using multiple checkboxes for different cities.

```html
<form action="">
  <fieldset>
    <legend>Cities you would like to visit</legend>

    <input type="checkbox" id="London" name="London">
    <label for="London">London</label>

    <input type="checkbox" id="Barcelona" name="Barcelona">
    <label for="Barcelona">Barcelona</label>

    <input type="checkbox" id="Venice" name="Venice">
    <label for="Venice">Venice</label>

    <input type="checkbox" id="Tokyo" name="Tokyo">
    <label for="Tokyo">Tokyo</label>
  </fieldset>
</form>
```

Try out the example below and you will be able to select multiple options.

%[https://codepen.io/jessica-wilkins/pen/wvmwpeE?editors=1000]

To learn more about checkbox elements, please read through [the DevDocs checkbox documentation](https://devdocs.io/html/element/input/checkbox). 

## Value and checked attributes

The `value` attribute represents the value for the input. 

Here is an example.

```html
<input type="checkbox" id="London" name="London" value="London">
```

The checked attribute is used to indicate which inputs should be checked by default on page load. 

Here is an example. 

```html
    <input type="checkbox" id="London" name="London" value="London" checked>
    <label for="London">London</label>
```

Here is what the result looks like rendered to the page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-27-at-12.42.20-AM.png)

## Footer elements

The `footer` element is located at the bottom of the HTML document and contains information like copyrights, or links to other related information for the page. 

Here is a basic example:

```html
<footer>
  <p>© 2022 Jessica Wilkins</p>
</footer>
```

To learn more about the `footer` element, please read through [this DevDocs explanation of the `footer` element](https://devdocs.io/html/element/footer). 

## Head and title elements

The `<head>` tags contain information that is processed by machines. Inside the `<head>` tags, you will nest metadata which is data that describes the document to the machine.

```html
<head>
  <!--important meta data goes inside here-->
  <!--title element also goes inside here-->
</head>
```

The `<title>` tag is the title for the web page. This text is shown in the browser's title bar.

```html
    <title>HTML 5 Boilerplate</title>

```

![Screen-Shot-2021-07-30-at-4.15.25-AM](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-30-at-4.15.25-AM.png)

This is an example of what a `head` would look like on a real web page. None of this information is displayed on the web page itself. 

```html
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
```

For a detailed description of each meta tag listed, please read through [this article on an HTML5 Boilerplate](https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/).

## `lang` attribute

The `lang` attribute inside the opening `<html>` tag sets the language for the page. It is also good to include it for accessibility reasons, because screen readers will know how to properly pronounce the text.

```html
<html lang="en">
```

## DOCTYPE

The first line in your HTML code should be the doctype declaration. A doctype tells the browser what version of HTML the page is written in.

```html
<!DOCTYPE html>
```

If you forget to include this line of code in your file, then some of the HTML 5 tags like `<article>`, `< footer >`, and `<header>`  may not be supported by the browser.

