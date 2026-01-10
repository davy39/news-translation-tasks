---
title: HTML Label – Label Tag Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-03T16:37:47.000Z'
originalURL: https://freecodecamp.org/news/html-label-label-tag-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/label.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'You use the HTML <label> tag to caption form controls. <label> is an inline
  element – meaning it doesn''t take up an entire line unless you put a break tag
  before it.

  By definition, form controls refer to the elements inside a form element.

  Examples o...'
---

You use the HTML `<label>` tag to caption form controls. `<label>` is an inline element – meaning it doesn't take up an entire line unless you put a break tag before it.

By definition, form controls refer to the elements inside a form element.

Examples of form controls include `<input type="text"/>`, `<input type="number"/>`, `<input type="radio"/>`, `<input type="checkbox"/>`, `<textarea></textarea>`, `<button></button>` and so on.

The ultimate advantage of labeling a form control is that the form control gets bound to the label. This means that the user doesn't have to click only the input before it becomes active.

Binding a label to a form control also helps visually impaired users because a screen reader will always read out the label when the input is focused.

In this article, I will show you how to use the `<label>` tag so you can step up your projects in a unique way.

## How to Use the `<label>` Tag

There are 2 ways you can use the `<label>` tag:

- as a standalone element by binding a form control to it with the for attribute
- wrapping it around the form control

If you are using it as a standalone element, you have to connect it to the form control by assigning the same value to the label `for` attribute and the form control `id` attribute. 

In addition, the user won't have to get the form control focused only by clicking on it. If they click the label, too, the control becomes focused. This is a plus for user experience.

This is how it works: 
```html
<form>
      <label for="name"> Name: </label>
      <input type="text" id="name" />
</form>
```
![label](https://www.freecodecamp.org/news/content/images/2022/02/label.gif)

This CSS makes the page a little better:

```css
body {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      height: 100vh;
      background-color: #cacaca;
    }
```

If you are wrapping it around a form control, you don’t need the `for` and `id` attributes. In this case, the input and label are implicitly associated. 

It works like this:
```html
<form>
      <label>
        Name:
        <input type="text" />
      </label>
</form>
```
![label](https://www.freecodecamp.org/news/content/images/2022/02/label.gif)

**P.S.:** If the values of the `for` attribute of the label and the `id` attribute of the form control are not the same, the form control will not get focused when the label is clicked.

## Conclusion

In this article you learned how to use the `label` tag the right way because its an essential part of user experience and accessibilty.

With the correct labeling, you can always make a form your users will be happy filling out.

Thank you for reading.


