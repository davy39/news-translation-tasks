---
title: CSS Variables Definition – What are CSS Vars and How to Use Them?
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-25T22:47:25.000Z'
originalURL: https://freecodecamp.org/news/what-are-css-variables-and-how-to-use-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pankaj-patel-6JVlSdgMacE-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: variables
  slug: variables
seo_title: null
seo_desc: "CSS variables are custom variables that you can create and reuse throughout\
  \ your stylesheet. \nIn this article, I will show you how to create CSS variables\
  \ on the :root pseudo selector and show you how to access them using the var() function.\
  \ \nHow to ..."
---

CSS variables are custom variables that you can create and reuse throughout your stylesheet. 

In this article, I will show you how to create CSS variables on the `:root` pseudo selector and show you how to access them using the `var()` function. 

## How to Create a CSS Custom Variable

Here is the basic syntax for defining a custom CSS variable:

```css
--css-variable-name: css property value;
```

It is best practice to define all of your variables at the top of your stylesheet. For larger projects, it is common to create a separate file just for your custom color variables so you can reuse them throughout other stylesheets. 

If you want to access that variable, then you would use the `var()` function. Here is the basic syntax.

```css
css property: var(--css-variable-name);
```

In this example, I want to create custom background and text color variables that I can reuse throughout the stylesheet. I am going to name these variables `--main-bg-color` and `--main-text-color`. 

```css
  --main-bg-color: #000080;
  --main-text-color: #fff;
```

I am going to place these variables inside of the `:root` pseudo selector which represents the root element in my HTML document. 

```css
:root {
  --main-bg-color: #000080;
  --main-text-color: #fff;
}
```

In my `body` selector, I am going to reference those variables using the `var()` function.

```css
body {
  background-color: var(--main-bg-color);
  color: var(--main-text-color);
}
```

Here is a working example:

%[https://codepen.io/jessica-wilkins/pen/LYeoOmP?editors=1100]

If I wanted to add more content to the page then I could reuse those variables throughout the rest of the stylesheet and avoid unnecessary repetition like this:

```css
.example-class-1 {
  background-color: #000080;
  display: flex;
  flex-direction: column;
}

.example-class-2 {
  font-size: 2.1rem;
  color: #fff;
}

.example-class-3 {
  background-color: #000080;
  color: #fff;
  border: 2px solid black;
}

```

In this second example, I have 6 red, green, and blue boxes on the page. I first created the HTML markup for the boxes.

```html
<div class="box-container">
  <div class="box red-box">Box 1</div>
  <div class="box green-box">Box 2</div>
  <div class="box blue-box">Box 3</div>
</div>
<div class="box-container">
  <div class="box blue-box">Box 4</div>
  <div class="box green-box">Box 5</div>
  <div class="box red-box">Box 6</div>
</div>
```

 I then created a set of custom red, green, and blue variables.

```css
:root {
  --maroon-red: #800000;
  --dark-green: #013220;
  --navy-blue: #000080;
  --white: #fff;
}
```

Lastly, I applied those variables to my boxes using the `var()` function.

```css
.red-box {
  background-color: var(--maroon-red);
}

.green-box {
  background-color: var(--dark-green);
}

.blue-box {
  background-color: var(--navy-blue);
}
```

Here is what the complete code and final result looks like:

%[https://codepen.io/jessica-wilkins/pen/WNdBXXZ?editors=1100]

## How to Name CSS Variables

When it comes to naming variables, you want to choose short descriptive names so other developers know what those variables are. 

This would be an example of a bad variable name:

```css
 background-color:var(--color);
```

What is `--color`?

Is it some shade of red? Green? Blue? Something else?

Is it a main background color or main text color? 

You don't want other developers to have to go back and look at the CSS definition to figure out what it should be. 

Another example is if you were creating custom CSS variables for different shades of colors, then you could choose to name them this way:

```css
:root {
  --maroon-red: #800000;
  --light-red: #ff0000;
  --crimson-red: #e32636;
}
```

Every developer will have their own way of naming variables. The important thing to remember is to provide descriptive names for your variables. 

## Conclusion

CSS variables are custom variables that you can create and reuse throughout your stylesheet.  

Here is the basic syntax for defining a custom CSS variable.

```css
--css-variable-name: css property value;
```

If you want to access that variable, then you would use the `var()` function. Here is the basic syntax.

```css
css property: var(--css-variable-name);
```

Every developer will have their own way of naming variables but it is best practice to create short descriptive names.

I hope you enjoyed this article and best of luck on your CSS journey.   

