---
title: How to paste images directly into an article in Draft.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T18:50:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-paste-images-directly-into-an-article-in-draft-js-e23ed3e0c834
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4SnkY7WxnP785isausYzEg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Andrey Semin

  The problem

  For some of you this may be a surprise, but Draft.js doesn’t support images out
  of the box. To be able to display images in the Editor, you need to install and
  configure [draft-js-image-plugin](https://www.draft-js-plugins...'
---

By Andrey Semin

### The problem

For some of you this may be a surprise, but Draft.js doesn’t support images out of the box. To be able to display images in the Editor, you need to install and configure `[draft-js-image-plugin](https://www.draft-js-plugins.com/plugin/image)` (we won’t cover this topic here as its docs are pretty comprehensive). This also means there is no support for such a common feature like pasting images (or any other file) into the Editor. The goal of this post is to show how you can add basic support for pasting files (we will focus on images).

### Solution

Let’s start by reading the [Draft.js docs](https://draftjs.org/docs/getting-started). It turns out there is a prop called `[handlePastedFiles](https://draftjs.org/docs/api-reference-editor#handlepastedfiles)` in the Editor. It receives an array of files and is supposed to provide you the option to manipulate with files on a paste action. However, things don’t work exactly this way.

> _There is an issue: when you try to paste multiple files into the Editor you will receive an array containing only one of them. This is a known problem and there was an [issue](https://github.com/facebook/draft-js/issues/1955) opened in the [Draft.js repo](https://github.com/facebook/draft-js) on 11 of December 2018. Which means it’s pretty young but still annoying._

Now we need to define which file types we’re going to handle. For images, those are `image/png`, `image/jpeg` and `image/gif` .

Now when we know we are going to work only with images, it is time to actually read the data from the file. To do this we will implement a function called `readImageAsDataUrl` and use the `[FileReader](https://developer.mozilla.org/en-US/docs/Web/API/FileReader)` API and `[readAsDataUrl](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL)` methods in particular. This combination of steps allows us to read the file and its content in base64 encoding which later can be used as a value of the `src` attribute of the `img` element.

Now when we have our base64 encoded image, all we need to do is to create a Draft.js entity and update the Editor’s state to contain this entity.

We can start by using the `[create](https://draftjs.org/docs/api-reference-entity#create)` method of the `Entity` module that is a part of Draft.js. (Keep in mind, though, that the documentation states `Entity.create` is deprecated and developers should use `contentState.createEntity`. The last one was not working at the time this post was written. So we’ll proceed with the usage of `Entity` but will keep track of this change).

We need to provide 3 arguments here:

* the first is the type of entity we’re about to create (`image` in our case)
* the second is the mutability of the entity (`IMMUTABLE` means we can’t edit the content of the text containing this entity. If we try to remove something from it, the whole text range would be removed)
* and the third is an optional object containing any data you want to store with an entity (in our case it is `src` which is required by `draft-js-image-plugin`).

In return we get a key by which we can address this entity in the Editor state. Now we need to use this key to insert a block into the editor and attach this exact entity to this block. We will use the `insertAtomicBlock` function of the `AtomicBlockUtils` module from Draft.js. We need to pass the current Editor state, entity key, and a character (that should not be empty string — that’s why we use single space) and we will get a new Editor state!

Now when all is set let’s combine everything together and take a look at our `handlePastedFiles` function:

Voilà! Now we can paste the image into Draft.js editor by simply pressing CTRL+V. You can extend this functionality in any way we want! For example we can allow our users to change the size of the images with some fancy UI.

If you’ve read this post all the way through, you may also want to check out [my previous post](https://hackernoon.com/draft-js-how-to-remove-formatting-of-the-text-cd191866d9ad) about Draft.js enchantment. You may want to apply it to your project as well.

