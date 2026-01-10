---
title: Accessibility Best Practices – What to Remember When Building Accessible Web
  Apps
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2022-12-16T21:01:26.000Z'
originalURL: https://freecodecamp.org/news/accessibility-best-practices-to-make-web-apps-accessible
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/ben-kolde-bs2Ba7t69mM-unsplash-1.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: best practices
  slug: best-practices
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: 'Anyone should be able to use your websites and apps - both people with
  disabilities and those without. This will make your website accessible.

  Think about the last site you built, or your favorite site. Are you confident that
  anyone can use your site...'
---

Anyone should be able to use your websites and apps - both people with disabilities and those without. This will make your website accessible.

Think about the last site you built, or your favorite site. Are you confident that anyone can use your site and perform the critical actions it requires? Have you considered folks with motor disabilities, visual disabilities, cognitive disabilities, and auditory disabilities?

Accessibility is often left as an after-thought. When it is time to ship a feature, we do an accessibility test and find out that our site wasn't accessible and do a hacky fix. 

Making a site accessible is a huge undertaking. But if we keep accessibility in mind from the get-go, it makes it much easier to build an accessible web app. 

In this post, I will go over 5 things you can keep in mind WHILE building your app so you don't have to do a hacky slap together at the end.

## 5 Things to Remember for Good Accessibility

1. Semantinc HTML
2. Tabindex
3. Aria attributes
4. Role
5. Keyboard navigation and screen readers

In short, S.T.A.R.K.

If you need help remembering this, think of Tony Stark. 

![TonyStark](https://cdn.vox-cdn.com/uploads/chorus_image/image/55400215/ktokatitmir0.0.jpg)

Let's go through each of these to understand how to use them in your web apps.

### What is Semantic HTML?

Using semantic HTML is important for accessibility. This is because assistive technologies such as screen readers are able to interpret what's on the page by parsing the HTML of the page. They enable users to take actions based on the elements. 

For example, if a screen reader encounters a `button`, it signals to the user that they should click on it. 

Let's consider some use-cases of what can happen when you don't use semantic HTML:

#### Creating buttons by using `div` instead of `button`: 

`div`s are container elements, so when a screen reader encounters a div, it automatically thinks it is a presentational element. 

When a screen reader user encounters a `div` that has content or children within it, the screen reader announces `role="group"` and the user will completely miss that the `div` is interactive. So make sure you use the proper semantic element for its purpose. You get accessibility for free.

#### Using CSS to fake headings instead of using `h1-6` tags: 

Heading tags such as `<h1>` and `<h2>` let an assitive technology know that this is important text, and the screen reader will announce "Heading". 

When you use CSS to make a heading instead of using correct semantics, the significance of the text is lost to a screen reader.

So just make sure to use semantic HTML whenever possible.

### What is Tabindex?

Adding a `tabindex` makes interactive elements keyboard-navigable. When you add `tabindex` to an element, a user is able to navigate to it using only their keyboard and/or assitive technologies.

1. You use a tabindex of `0` to set focus to an element in the default tabbing order,
2. You use a tabindex of `-1` to programmatically focus an element using JavaScript.
3. Do not assign a value of > 1 to tabindex.

A word of caution though - you should only add `tabindex` to interactive elements. It is not a good practie to add `tabindex` to elements such as `div`. 

Instead of adding tabindex in that case, use a semantic element, such as a `button` since semantic elements already are tabbable and do not need an additional `tabindex` value.

### What are ARIA attributes?

Aria attributes such as `aria-checked`, `aria-label` give additional information to assistive technologies.

Aria attributes are a set of HTML attributes that you use to provide additional information about the purpose and state of elements on a web page. These attributes are especially beneficial to assistive technologies to provide more context and better navigation for users.

Some common aria-attributes include:

1. `aria-label`: used to provide a label or name for an element.
1. `aria-hidden`: used to indicate that an element should be hidden from assistive technologies. This can be useful for elements that are used for layout purposes but are not relevant to the content of the page.
1. `aria-describedby`: used to associate an element with a description, which helps to provide context of an element.
1. `aria-liv`e: used to indicate that an element's content may change dynamically, and that assistive technologies should pay attention to changes in the element's content.

You can use these attributes in combination with each other and with standard HTML attributes to create more accessible and user-friendly web content.

### What is the `aria-role` attribute?

You use the `aria-role` attribute to define the purpose of an HTML element and provide its semantic meaning. 

For example, if you are building a grid component with the help of CSS and divs, you can use `role="grid"` to let assistive technologies know about the semantics of the component.

Some common `aria-role`s include:

1. `button`: used to indicate that an element should be treated as a button.
2. `alert`: used to indicate that an element is an alertbox.
3. `presentation`: used to indicate that an element is only presentational.

It is important to exercise caution with `aria-role`. Remember to not overdo it.

### How to handle keyboard navigation and screen readers

Many users with motor disabilities rely on their keyboard and assitive technologies to navigate the web. So it's critical that every component be navigable using a keyboard and screen reader. 

You can test keyboard accessibility by navigating a site using only your keyboard. Here are some common keys:

1. `tab` key to navigate to different sections of the site.
2. `spacebar` to select elements, such as a checkbox.
3. `enter` to press buttons.

While testing keyboard navigation, make sure you think about the following:

1. Focus remains visible: Ensure that you can clearly see which element is being focused on the page. Focus should always remain visible.
2. Tab order: When tabbing through sections, the order of tabbing should follow the natural flow and logical structure of the website. It should not jump back and forth between sections.
3. Keyboard traps: Ensure that when navigating with the keyboard, the focus doesn't get trapped on an element. For example, this could happen when a modal is opened, or the focus is navigated to a widget, such as calendar or emoji picker. Ensure that when you select an element in the widget, you are able to navigate back to the site.

## Wrapping Up

Overall, testing for accessibility during development is an important part of the process that can help to create more usable and accessible software for all users. Testing for accessibility early helps to provide a great user experience for everyone.

In the next article, I will talk about the various accessibility tools and how to debug an accessibility issue. You can [sign up to get it in your inbox here.](http://tinyletter.com/shrutikapoor)

Until then, enjoy your holidays!

Feliz Navidad.



