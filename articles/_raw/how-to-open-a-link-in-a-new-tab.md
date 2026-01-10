---
title: How to Open a Link in a New Tab – HTML target blank Attribute Explained
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-05-31T14:53:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-open-a-link-in-a-new-tab
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/markus-spiske-4qbS830djfs-unsplash.jpg
tags:
- name: freeCodeCamp Curriculum Guide
  slug: freecodecamp-curriculum-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'There will be times where you will want your user to click on a website
  link and have it open in a new browser tab. But how do you do that in HTML?

  In this article, I will show you how to use the target="_blank" attribute through
  code examples. I wil...'
---

There will be times where you will want your user to click on a website link and have it open in a new browser tab. But how do you do that in HTML?

In this article, I will show you how to use the `target="_blank"` attribute through code examples. I will also talk about when you should consider using this attribute. 

## How to Open Up a New Browser Tab Using `target="_blank"`

The `target="_blank"` attribute is used inside the opening anchor tag like this:

```html
<a href="website-link-goes-here" target="_blank">
```

When the user clicks on the link, a new browser tab will automatically open to that page. 

In this example, I have nested a link inside a set of paragraph tags to direct people to freeCodeCamp. 

```html
<p>To learn how to code for free, please visit <a href="https://www.freecodecamp.org/learn" target="_blank">freeCodeCamp.org</a></p>
```

When you click on the freeCodeCamp link, then it will open up a new browser tab for you.

%[https://codepen.io/jessica-wilkins/pen/zYRRdmQ?editors=1000]

If I were to omit the `target="_blank"` attribute, then the default behavior would be to leave the current web page and go directly to the link without opening a new browser tab. 

## What is the `noopener` Keyword?

The `noopener` keyword in the `rel` attribute is used primarily for security reasons to prevent malicious users from messing with the original web page through the `[Window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)` property. If the malicious user gained access to your window object then they could redirect your page to a malicious URL.

You can use the `noopener` keyword as a way to help prevent that security issue from happening. Here is how the `noopener` keyword is used:

```html
<a target="_blank" rel="noopener" href="https://devdocs.io/html/element/heading_elements">DevDocs documentation</a>
```

If you want to learn more about the security concerns that `rel=noopener` helped solve, then please read through [this helpful article](https://mathiasbynens.github.io/rel-noopener/). 

### Updates to the `noopener` keyword

In 2021, there was an update made where modern browsers now set `rel=noopener` to any link using the `target=_blank` attribute. As you can see in this [Can I use table](https://caniuse.com/rel-noopener), the `noopener` keyword is supported by most browsers except for Internet Explorer 11. 

Even with this update, a lot of developers will still use `rel=noopener` for links using the `target=_blank` attribute.

## Should You Use the `target="_blank"` Attribute All the Time?

When users click on a link, the default behavior is to have that link open on the current page they are on without opening a new browser tab. In a lot of cases, you do not want to change this default behavior because users have grown to expect this. 

You have to think carefully about when it would be a good time to use the `target="_blank"` attribute. One good example would be if a user is working on a page and they don't want to leave that page if they click on a link.

In this example, we are linking to the [DevDocs](https://devdocs.io/) documentation, so the user can stay on their current page and look up a reference on a new tab.

%[https://codepen.io/jessica-wilkins/pen/qBxxPdb?editors=1000]

## Conclusion

You can use the `target="_blank"` attribute if you want your users to click on a link that opens up a new browser tab. 

The `target="_blank"` attribute is used inside the opening anchor tag like this.

```html
<a href="website-link-goes-here" target="_blank">
```

The `noopener` keyword in the `rel` attribute is added to prevent malicious users from messing with the original web page through the `[Window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)` property. 

```html
<a target="_blank" rel="noopener" href="link-goes-here">
```

You have to think carefully about when it would be a good time to use the `target="_blank"` attribute because you don't want to always change the default behavior of links.

I hope you enjoyed this article and best of luck on your programming journey. 

