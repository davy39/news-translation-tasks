---
title: How to Build a Dropdown Menu with JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-09T18:27:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-dropdown-menu-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/how-to-build-a-dropdown-menu-with-javascript.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Victor Eke

  If you use the internet, you''ve likely used a dropdown menu before. They primarily
  serve two purposes: collecting user input in web forms, and implementing action/navigation
  menus in web applications.

  Dropdowns are one of the best ways ...'
---

By Victor Eke

If you use the internet, you've likely used a dropdown menu before. They primarily serve two purposes: collecting user input in web forms, and implementing action/navigation menus in web applications.

Dropdowns are one of the best ways to offer numerous options for a similar collection of elements without needing to compromise an application's general layout flow. Aside from web apps, they're also used in standalone software, operating systems, and so on.

In this guide, you'll learn how to build a dropdown navigation menu using HTML, CSS, and JavaScript.  

Here's a screenshot of what you'll be building. At the end of this guide, I'll include the codepen file so you can play around with it.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/dropdown-menu-with-css.png)
_Final result of the dropdown menu_

Now that we've covered the fundamentals of the dropdown menu, let's discuss the steps for how to build one.

## Step 1 – Add the Markup for the Dropdown

Since we'll be using icons in this guide, we need to first import them. For simplicity, we'll be using a free library called [Boxicons](https://boxicons.com/). Feel free to pick other alternatives you prefer.

There are several ways to [setup](https://boxicons.com/usage) Boxicons in your site. But the simplest way is by defining the script tag in the `head` of your HTML file, like this:

```html
<head>
   <link 
     href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" 
     rel="stylesheet"
    />
 </head>
```

After importing the icons, create a `div` element with a class of `container`. This element will contain the `button` and dropdown menu.

Inside the container, create a button element and give it a class and id of `btn`. For the button, pass in the button text and the arrow icon. 

Here's the markup for the button.

```html
<button class="btn" id="btn">
  Dropdown
  <i class="bx bx-chevron-down" id="arrow"></i>
</button>
```

Next up, we'll add the markup for the dropdown menu itself. Underneath the button tag, create a `div` element and give it a class and id of `dropdown`. Inside the div element, create an `a` tag for each individual dropdown item and pass in their respective icon and text.

Here's what the markup looks like:

```html
<div class="dropdown" id="dropdown">
  <a href="#create">
    <i class="bx bx-plus-circle"></i>
    Create New
  </a>
  <a href="#draft">
    <i class="bx bx-book"></i>
    All Drafts
  </a>
  <a href="#move">
    <i class="bx bx-folder"></i>
    Move To
  </a>
  <a href="#profile">
    <i class="bx bx-user"></i>
    Profile Settings
  </a>
  <a href="#notification">
    <i class="bx bx-bell"></i>
    Notification
  </a>
  <a href="#settings">
    <i class="bx bx-cog"></i>
    Settings
  </a>
</div>
```

This is the output.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/dropdown-menu-markup.png)
_Dropdown menu markup preview_

It doesn't look good yet – so let's start styling the menu.

## Step 2 – Style the Dropdown Menu

First we'll reset the default margin and padding of every element on the page and store some values in variables so we can reuse it throughout our CSS file. Then we'll give the body element some global styling.

```css
@import url(https://fonts.googleapis.com/css?family=Inter:100,200,300,regular,500,600,700,800,900);

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Inter", sans-serif;
  --shadow: rgba(0, 0, 0, 0.05) 0px 6px 10px 0px,
    rgba(0, 0, 0, 0.1) 0px 0px 0px 1px;
  --color: #166e67;
  --gap: 0.5rem;
  --radius: 5px;
}

body {
  margin: 2rem;
  background-color: #b3e6f4;
  font-size: 0.9rem;
  color: black;
}
```

Next step is styling the button and the dropdown container itself. In order to speed things up, I'll explain only the important bits of the styling.

Copy the markup below and paste into your CSS file.

```css
.btn {
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  column-gap: var(--gap);
  padding: 0.6rem;
  cursor: pointer;
  border-radius: var(--radius);
  border: none;
  box-shadow: var(--shadow);
  position: relative;
}

.bx {
  font-size: 1.1rem;
}

.dropdown {
  position: absolute;
  width: 250px;
  box-shadow: var(--shadow);
  border-radius: var(--radius);
  margin-top: 0.3rem;
  background: white;
}

.dropdown a {
  display: flex;
  align-items: center;
  column-gap: var(--gap);
  padding: 0.8rem 1rem;
  text-decoration: none;
  color: black;
}

.dropdown a:hover {
  background-color: var(--color);
  color: white;
}
```

Since dropdown menus are usually placed over elements, the button was positioned relative and the dropdown menu, position absolute. This ensures that both elements will be close to each other and the dropdown menu will be placed over elements. This way, when toggled, it won't affect the flow of the page.

Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/dropdown-menu-with-css.png)
_Dropdown menu styling_

Now that the dropdown has been styled, we want it to appear only when the button has been clicked rather than immediately. To hide it, we'll use CSS.

In a previous article I wrote about [How to build a modal with JavaScript](https://freecodecamp.org/news/how-to-build-a-modal-with-javascript), we used `display: none` to hide the modal element initially from the viewport. But the drawback of utilizing this property was that it was not animatable, according to [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties).

So in this guide, we'll be following a different approach to hide the dropdown menu. This involves combining the `visibility` and `opacity` properties together to get the desired result. This method is how [GitHub](https://github.com) implements its dropdown menu. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/github-dropdown-menu.png)
_Dropdown menu on GitHub_

Inside the dropdown class we created earlier, add a visibility property and give it a value of hidden and set the opacity to `0`. Doing this will hide the dropdown menu from the page.

In order to show the modal, we'll create a separate class called `show`. This class will hold the visibility property with a value of `visible` and opacity of `1`. And we can inject this class into the modal using JavaScript in a bit.

Here's the code:

```css
.dropdown {
  position: absolute;
  width: 250px;
  box-shadow: var(--shadow);
  border-radius: var(--radius);
  margin-top: 0.3rem;
  background: white;
  transition: all 0.1s cubic-bezier(0.16, 1, 0.5, 1);
    
  transform: translateY(0.5rem);
  visibility: hidden;
  opacity: 0;
}

.show {
  transform: translateY(0rem);
  visibility: visible;
  opacity: 1;
}

.arrow {
  transform: rotate(180deg);
  transition: 0.2s ease;
}
```

Alongside the styling to hide the modal element, we added another class to rotate the arrow icon when the dropdown button is clicked.

## Step 3 — Add the Dropdown Functionality

For starters, let's store our respective elements into variables so they are reusable. 

```js
const dropdownBtn = document.getElementById("btn");
const dropdownMenu = document.getElementById("dropdown");
const toggleArrow = document.getElementById("arrow");
```

The next step is to create a function to toggle the `show` class on the dropdown element and to rotate the dropdown arrow when the button is clicked. We'll name this function `toggleDropdown`.

```js
const toggleDropdown = function () {
  dropdownMenu.classList.toggle("show");
  toggleArrow.classList.toggle("arrow");
};
```

And then we can call this function on the dropdown button using the `addEventListener` method. So anytime the button is clicked, it will fire the function which controls showing and hiding the dropdown menu.

```js
dropdownBtn.addEventListener("click", function (e) {
  e.stopPropagation();
  toggleDropdown();
});
```

If you noticed, we added a `stopPropagation()` method inside the dropdown function. This prevents the function of the button element from being passed down to the parent element, thus stopping the function from running twice. You'll understand more about this in the next section. 

Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/toggle-dropdown-menu-.gif)
_dropdown menu toggle_

## How to Close the Dropdown Menu When a DOM Element is Clicked

Dropdown menus are usually closed in four different ways: 

* By clicking the button that activates it
* By clicking on any of its child elements
* By clicking outside of the menu (on the body)
* By hitting the Escape or down arrow keys

But for this guide, let's concentrate on the first three.

First we'll select the root element `<html>` using `document.documentElement`. And as before, we'll pass in the `toggleDropdown()` function inside. 

But this time, we want to define a condition that checks if the dropdown menu contains the `show` class or not. Only when it does do we want to fire the close function.

```js
document.documentElement.addEventListener("click", function () {
  if (dropdownMenu.classList.contains("show")) {
    toggleDropdown();
  }
});
```

Here's the final result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/close-dropdown-when-dom-element-is-clicked.gif)
_Close dropdown when DOM element is clicked_

And that is how you build a dropdown menu with JavaScript. Below is the codepen file to test this dropdown menu in action. 

<iframe height="400" style="width: 100%;" scrolling="no" title="Dropdown menu" src="https://codepen.io/evavic44/embed/eYKQJjJ?default-tab=html%2Cresult&theme-id=light" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/evavic44/pen/eYKQJjJ">
  Dropdown menu</a> by Eke (<a href="https://codepen.io/evavic44">@evavic44</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## Conclusion

I sincerely hope you found this post interesting or useful. If you did, kindly share with your friends or subscribe to my blog so you won't miss any future postings. Thanks for reading.

[GitHub](https://github.com/evavic44) | [Twitter](https://twitter.com/victorekea) | [Blog](https://eke.hashnode.dev) | [Portfolio](https://victoreke.com)

