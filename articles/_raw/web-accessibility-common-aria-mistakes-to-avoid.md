---
title: Web Accessibility – Common ARIA Mistakes to Avoid
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2023-01-11T21:58:45.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-common-aria-mistakes-to-avoid
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/a11y-image.jpeg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Accessible Rich Internet Applications – or ARIA – is a set of attributes
  and roles defined by the Web Accessibility Initiative. These make the web more accessible
  to people with disabilities.

  ARIA is extremely important for building accessible web ap...'
---

Accessible Rich Internet Applications – or ARIA – is a set of attributes and roles defined by the [Web Accessibility Initiative](https://www.w3.org/WAI/). These make the web more accessible to people with disabilities.

ARIA is extremely important for building accessible web applications. But it's very easy to misuse ARIA and make the website less accessible.

This article will demonstrate five common ARIA mistakes and how to fix them.

## Don't Use Unnecessary ARIA Labels

The first rule of ARIA is that you should not use ARIA unless you have to. HTML elements already have accessibility built in, and adding unnecessary ARIA labels can break accessibility.

For that reason, it's much better to use HTML elements, instead of constructing code with ARIA labels.

**Example of misusing ARIA labels:**

⛔ BAD: Below is a `button` element with `aria-label`:

```html
<button aria-label="Send">Send</button>
```

✅ GOOD: Below is a `button` element:

```html
<button>Send</button>
```

In the examples above, I am creating a button element. In the first code snippet, there is a `aria-label` with the label, “send”. HTML’s button element already has accessibility built into it. It is not necessary to add an `aria-label` so it's much better to remove the label.

The `button` element will read the text inside it already. We do not need to add the `aria-label` to describe it.

**Takeaway:** Don’t add unnecessary ARIA labels if you can use accessible HTML elements instead.

## Don't Use the Wrong ARIA Attributes

There are pre-defined ARIA states and properties defined by the ARIA working group, which is part of World Wide Web Consortium.

Developers should use the states and properties available – you cannot create your own in your code. You can find the list of properties and states on [W3's Website](https://www.w3.org/TR/wai-aria-1.0/states_and_properties).

**Example of using incorrect ARIA attributes:**

⛔ BAD

```html
<span aria-donotshow="true">Don’t show this</span>
```

✅ GOOD

```html
<span aria-hidden="true">Don’t show this</span>
```

This means that a new property, like `aria-donotshow`, is not correct. `aria-donotshow` is not a property in the W3 website so you shouldn't use it.

**Takeaway:** Don’t create your own ARIA attributes. You can only use the ones defined by the ARIA working group.

## Know When to Use `aria-labelledby`

Another common mistake is when developers use `aria-label` to describe content inside the DOM.

All interactive elements need an accessible name. If we want to add an accessible name to an element where the name needs some content from elsewhere in the DOM, we should use `aria-labelledby`. If there is no content that can be referred to to create an accessible name, then we can use `aria-label`.

**Example of when to use** `aria-labelledby`:

⛔ BAD

```html
<div aria-label="Related Content">				
    <span>Related Content</span>		
</div>
```

✅ GOOD

```html
<div aria-labelledby="nav-title">				
    <span id='nav-title'>Related Content</span>		
</div>
```

In the example above, the first code snippet uses `aria-label` and associates it with the text, “Related content”. But the `span` inside the text already has the correct content we want a screen reader to read.

Instead of using `aria-label` in this example, we should reference the span content by adding `aria-labelledby` that is associated with the id of the content we want to reference.

**Takeaway:** If you want to reference content from inside the DOM, use `aria-labelledby` with corresponding id.

## Know When to Use `aria-describedby`

Sometimes, we need to give more information to an element. For example, we might want to tell the user that the button they will press will open a new tab.

This information is important because the user needs to know where they are when navigating websites.

For these types of scenarios, we can use `aria-describedby` to give additional information.

**Example:**

⛔ BAD

```html
<button aria-label="Close" aria-label="Opens in a new tab">	
Show related		
</button>
```

✅ GOOD

```html
<button aria-label="Close" aria-describedby="description">			Show related		
</button>		
<div id="description">Opens in a new tab</div>
```

In the first example above, what engineers expect the screen reader to announce is: “button, Show related, opens in a new tab”.

But the screen reader does not do that. Instead, it says,“button, opens in a new tab”. The screen reader does not read the content inside, because aria-label always overrides the text content of the HTML5 element it has been applied to.

The second code snipped shows the correct way to use `aria-describedby`. The screen reader will read, “button, Show related, opens in a new tab”.

That information tells the user that the button is to show related content and if they press that button, it will navigate them to another tab.

**Takeaway:** Use `aria-describedby` to add additional information to elements.

## Don't Use ARIA Child Roles Without Parent Roles

There are some ARIA attributes that require a child/parent relationship. This means that you cannot use the ARIA child attribute without wrapping it around its parent ARIA attribute.

It’s easy to forget the child/parent relationship and build code that only uses the parent attribute without the child, or to build code that only uses child attribute without its parent.

If you forget the child/parent relationship, the code becomes more inaccessible, which defeats the purpose of ARIA.

**Example:**

⛔ BAD:

`role="listbox"` is a parent property. The `ul` list below does not have `role=option` which is its child property.

```html
<div role="listbox">
    <ul>
        <li></li>
    </ul>
</div>
```

✅ GOOD:

`role="listbox"` is a parent property. The `ul` list below has `role=option` which is its child property.

```html
<div role="listbox">
    <ul>
        <li option="option"></li>
    </ul>
</div>
```

In the code example above, the first code has a code snippet that has `role=listbox` which is a parent element. `listbox` needs children inside which is `option`. We cannot use `listbox` on its own to build accessible web sites.

**Takeaway:** Always use child/parent properties together.

## Summary

ARIA is a set of attributes and roles defined by WAI to make the web more accessible to people with disabilities. Although it's necessary to create an accessible web, it is very easy to misuse ARIA and make websites less accessible instead.

Try to avoid these five most common ARIA mistakes:

1. Don’t unnecessarily use aria-label. Built-in HTML semantics are always better.
    
2. Don’t create your own aria attribute. Only use the ones defined by ARIA.
    
3. Use `aria-labelledby` with an id when you have content that wraps divs and you want to group sections.
    
4. Use `aria-describedby` when you have sections that need more descriptions.
    
5. Do not use a child ARIA without a predefined parent ARIA.
    

ARIA was created to make websites more accessible to people with disabilities. If we avoid common mistakes, we will make sure our websites are accessible.
