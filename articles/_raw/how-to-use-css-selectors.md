---
title: How to Use CSS Selectors
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-07-06T19:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-selectors
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-karolina-grabowska-4016510.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "You can apply CSS to elements like paragraphs and ordered lists, which\
  \ you can learn more about by reading this article. But you're not just restricted\
  \ to those two approaches. \nAs we'll see in this tutorial, you can also control\
  \ content behavior usi..."
---

You can apply CSS to elements like paragraphs and ordered lists, which you can learn more about by [reading this article](https://www.freecodecamp.org/news/css-style-sheets-basics/). But you're not just restricted to those two approaches. 

As we'll see in this tutorial, you can also control content behavior using custom or `ID` styles, pseudo classes, and inheritance. This happens through the use of selectors.

CSS selectors target HTML elements based on their tag names, attributes, classes, IDs, or their position in the document structure. When a selector matches an element, the styles defined in the corresponding CSS rule are applied to that element.

Here's some code that'll illustrate how selectors can work to control various kinds of elements. Read through it and try to understand what everything does, then we'll work through it one section at a time.

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Target elements with a class */
    .highlight {
      background-color: yellow;
      font-weight: bold;
    }

    /* Target elements with an ID */
    #special {
      color: red;
      text-decoration: underline;
    }

    /* Target elements based on their tag name */
    p {
      font-size: 16px;
    }

    /* Target elements based on their relationship */
    ul li {
      list-style-type: square;
    }

    /* Target elements based on attribute values */
    input[type="text"] {
      border: 1px solid gray;
    }
  </style>
</head>
<body>
  <h1 id="special">Welcome to my Website</h1>

  <p>This paragraph will have a font size of 16 pixels.</p>

  <ul>
    <li>List item 1</li>
    <li>List item 2</li>
    <li class="highlight">List item 3</li>
  </ul>

  <input type="text" placeholder="Enter your name">
</body>
</html>

```

This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). If you'd like, you can follow the video version here:

%[https://youtu.be/X_F5vK7XeiI]

## CSS Custom and ID Styles

This first style is an example of a custom selector called `highlight`. 

```
    /* Target elements with a class */
    .highlight {
      background-color: yellow;
      font-weight: bold;
    }

```

That HTML might look like this:

```
<li class="highlight">List item 3</li>
```

Next, this ID selector (`#special`):

```
    /* Target elements with an ID */
    #special {
      color: red;
      text-decoration: underline;
    }

```

...will be applied in the HTML through the `id=` attribute:

```
<h1 id="special">Welcome to my Website</h1>
```

We've already seen how associating a style with an HTML element like `p` works:

```
    /* Target elements based on their tag name */
    p {
      font-size: 16px;
    }

```

...But the _shape_ of the background coloring applied to `<ul>` tags and the border color of the text input field are controlled by these two styles:

```
    /* Target elements based on their relationship */
    ul li {
      list-style-type: square;
    }

    /* Target elements based on attribute values */
    input[type="text"] {
      border: 1px solid gray;
    }

```

Now, in addition to the HTML snippets we've already examined, we can also see how the third bullet point has the `highlight` class attribute, so it'll get both a yellow background and that background will be square. Finally, the `<input type="text">` field will get a gray border.

```
<body>
  <h1 id="special">Welcome to my Website</h1>

  <p>This paragraph will have a font size of 16 pixels.</p>

  <ul>
    <li>List item 1</li>
    <li>List item 2</li>
    <li class="highlight">List item 3</li>
  </ul>

  <input type="text" placeholder="Enter your name">
</body>

```

If save all that code to a `.html` file and load it in your favorite browser, you'll see that it all looks exactly the way we wanted it. Hopefully, at least.

## How to Work with the CSS `pseudo class`

There's another kind of class in CSS we call a `pseudo class`. They're called "pseudo" since these aren't exactly traditional classes, but _class controls_. 

You've probably already seen pseudo classes in action on web pages you've visited. Links or page elements will change their appearances when different actions are occurring around them.

For instance, as you can see from this CSS code, there are definitions for _normal_, _hover_, _focus_, and _active_ states.

```
/* Normal state */
button {
  background-color: blue;
  color: white;
}

/* Hover state */
button:hover {
  background-color: lightblue;
}

/* Focus state */
button:focus {
  outline: 2px solid red;
}

/* Active state */
button:active {
  background-color: darkgreen;
}


```

You should take those CSS styles and apply them to some simple HTML code. This example shows how they could all be applied to the `Click me` button text in the HTML.

```
<button>Click me</button>

```

Let's see how that'll work.

The normal, at-rest appearance of a button might have a blue background color and white text. But when you hover your mouse over top of the button, the background turns light blue. 

```
/* Hover state */
button:hover {
  background-color: lightblue;
}
```

If you would use the `Tab` key on your keyboard to cycle through all the page elements, once you reach the button, the state will become `Focus` and the outline will turn red. 

```
/* Focus state */
button:focus {
  outline: 2px solid red;
}
```

When I would actually click and hold the button, the background will change to dark green.

```
/* Active state */
button:active {
  background-color: darkgreen;
}
```

## CSS Inheritance

CSS inheritance is a mechanism that allows properties defined on parent elements to be inherited by their child elements. When a property is set on a parent element, its value is automatically inherited by its descendants unless overridden.

Inheritance applies to various CSS properties, such as font styles, text colors, and some layout properties. For example, if you set the font family or font size on a parent element, the child elements within it will inherit those values unless explicitly specified otherwise.

In some cases, certain properties are _not_ inherited by default. For instance, properties like background color, border properties, and box-model properties are typically not inherited. In these cases, child elements will not inherit the values from their parent elements unless explicitly set.

CSS inheritance simplifies the styling process by allowing you to set properties once on parent elements, reducing the need for repetitive styling on child elements. However, it's essential to be aware of which properties are inherited and which ones are not to ensure the desired styling outcome.

This code creates a `#parent` style that sets the font and font color. It also creates a second style that'll apply to paragraphs within the HTML. But this second style is also a `child` of the `parent`.

```
<style type="text/css">
#parent {
  font-family: Arial, sans-serif;
  color: blue;
}
p {
  font-size: 24px;
}
</style>

```

The HTML exists within a `<div>` that uses the `id=` attribute to adopt the `parent` style. There are two lines of text, one inside the `<p>` tag and one outside.

```
<div id="parent">
  Here is some regular text.
  <p>This is a paragraph inside the parent element.</p>
</div>

```

When we load our code in a browser we'll see that both those lines of text will be printed in blue - which means that the `child` element has, indeed, adopted the parents values. But it'll also get its own larger font formatting. This kind of formatting can be powerful when you want to very precisely control overall, global behavior, while maintaining the ability to further define individual elements.

To _prevent_ inheritance and establish a completely new value, the `inherit` keyword can be used to override the inherited value. Additionally, the initial keyword can be used to reset a property to its default value.

One more important point that's particularly relevant when you're working with multiple CSS styles. What happens when, between your inline CSS, multiple stand alone CSS files, and layers of parents and children, there's a conflict between styles? Well there's a set of rules that determine how everything will be handled.

Inline code within an HTML file's `<style>` tags always comes first. The more specific a selector is, the greater its priority. The further down in the code a style appears the greater priority it's given. And the `!important` attribute will always win.

### Rule Precedence in CSS

Here's a quick summary of rule precedence in CSS:

* Inline CSS overrides CSS rules in style tag and CSS file
* A more specific selector takes precedence over a less specific one
* Rules that appear later in the code override earlier rules if both have the same specificity
* A CSS rule with `!important` always takes precedence.

## Wrapping Up

You've seen how customizing your CSS styles through attributes like `id` and applying structures like pseudo classes can go a long way to liven up your HTML pages. And you've seen how all of that works through CSS selectors. 

You also saw how CSS inheritance can help you closely control the way objects on your web pages behave.

So you're all set to start building some pretty sophisticated websites. Why not start today?

_This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)_

