---
title: HTML Drop-down Menu – How to Add a Drop-Down List with the Select Element
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-26T14:25:06.000Z'
originalURL: https://freecodecamp.org/news/html-drop-down-menu-how-to-add-a-drop-down-list-with-the-select-element
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--9-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: 'Many websites, applications, and web pages use drop-down menus to help
  display a list of information. You can use them to create navigation menus, options
  for forms, and more.

  If you''re looking at some of these menus or lists, you might imagine how c...'
---

Many websites, applications, and web pages use drop-down menus to help display a list of information. You can use them to create navigation menus, options for forms, and more.

If you're looking at some of these menus or lists, you might imagine how complex creating them could be. And yes – in some cases, it gets a little bit complex.

A drop-down menu is a list of options that gets revealed vertically when a user interacts with the menu by either clicking on it or hovering over it with their cursor.

This menu also disappears when the user stops interacting with the menu by clicking again or taking the cursor away from the menu.

In this article, you will learn how to add a drop-down list to the `select` element on your webpage. You'll also learn the various options available, and how to create a hoverable drop-down list/menu.

## How to Create an HTML Dropdown List

In HTML, by default, you can always create a drop-down list with the `select` tag alongside the option tag. This is mainly used within forms to select a value from a list of many options.

The select tag has two primary attributes: the `name` and `id` attributes.

```html
// Syntax
<select name="" id="">
  <option value="">...</option>
  // ...
</select>
```

You use the `name` attribute to identify the drop-down when a selection is submitted in a form. You can connect the `id` attribute to a `label` that has similar values to its `for` attribute.

```html
// Syntax
<label for="languages">List of Languages:</label>
<select name="" id="languages">
  <option value="">...</option>
  // ...
</select>
```

The `select` tag also has some optional boolean attributes like `disabled` (which disables the select fields), `required` (which makes the field required in a form), and lots more.

```html
<select name="" id="languages" required>
  // ...
</select>

// Or

<select name="" id="languages" disabled>
  // ...
</select>
```

Within the `select` tag, you can add many options in the individual `option` tag. The `option` tag has an attribute of `value` that specifies a value that is submitted from the form when an option gets selected.

```html
<select name="language" id="language">
  <option value="javascript">JavaScript</option>
  <option value="python">Python</option>
  <option value="c++">C++</option>
  <option value="java">Java</option>
</select>
```

There are other boolean attributes like `disabled` (which disables the option in the menu), and `selected` (which you use to set a particular option as the default selected option when the page loads rather than the first option).

```html
<select name="language" id="language">
  <option value="javascript" disabled>JavaScript</option>
  <option value="python">Python</option>
  <option value="c++">C++</option>
  <option value="java" selected>Java</option>
</select>
```

In the above code, the first option has an attribute of `disabled`, meaning you will not be able to select the option. The fourth option has an attribute of `selected`, meaning that instead of having JavaScript as the selected value by default, Java will be selected.

<iframe height="300" style="width:100%" src="https://codepen.io/olawanlejoel/embed/YzaNgmw?default-tab=html%2Cresult">
  See the Pen <a href="https://codepen.io/olawanlejoel/pen/YzaNgmw">
  Dropdown List</a> by Olawanle Joel (<a href="https://codepen.io/olawanlejoel">@olawanlejoel</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## How to Create a Hover-able Drop-down Menu

When you scroll through or visit many advanced and modern webpages, you will notice that they have drop-down menus.

These menus are used for navigation to help hold similar links together. Most times, when you hover on the parent menu, then the drop-down list appears.

![](https://paper-attachments.dropbox.com/s_B4C6D2ADDF91C398F7D0077C06A79A5494062ED47759B85768844AD11A4B757E_1664053790313_image.png align="left")

You can create these types of menues in various ways, as there is no direct syntax to build one.

You can create this using CSS styling to show and hide the drop-down list when the user hovers over the menu. A very good approach is to create a `div` that holds the menu and the drop-down.

```html
<div class="dropdown">
  <button>Profile</button>
  <div class="dropdown-options">
    <a href="#">Dashboard</a>
    <a href="#">Setting</a>
    <a href="#">Logout</a>
  </div>
</div>
```

This `div` serves as a container and you can style it to a `position` of `relative` and `display` of `inline-block`, so the drop-down options appear below the menu.

```css
.dropdown {
  display: inline-block;
  position: relative;
}
```

You can style your button and the `dropdown-options` however you wish. But the major style that controls the hover effect, by default, sets the `dropdown-options` not to display. Then when a mouse hovers over the menu, the display is not set to `block`, so the options are visible. You also set the `position` to `absolute`, so the options appear below the menu, and `overflow` to `auto` to enable scroll on small screens.

```css
.dropdown-options {
  display: none;
  position: absolute;
  overflow: auto;
}

.dropdown:hover .dropdown-options {
  display: block;
}
```

In the demo below, we add more styling to make the drop-down menu more attractive and nice:

<iframe height="300" style="width:100%" src="https://codepen.io/olawanlejoel/embed/ZExZGdK?default-tab=html%2Cresult">
  See the Pen <a href="https://codepen.io/olawanlejoel/pen/ZExZGdK">
  Hoverable dropdown menu</a> by Olawanle Joel (<a href="https://codepen.io/olawanlejoel">@olawanlejoel</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## Wrapping Up

In this article, you have learned how to create a drop-down list with the select tag. You've also learned how to create the hoverable drop-down menu with CSS to handle the hover effect.

You can learn more about the select tag in [this article on **HTML Select Tag – How to Make a Dropdown Menu or Combo List**](https://www.freecodecamp.org/news/html-select-tag-how-to-make-a-dropdown-menu-or-combo-list/) by [Kolade](https://www.freecodecamp.org/news/author/kolade/).
