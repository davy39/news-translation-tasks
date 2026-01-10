---
title: Unable to Find Images Based on URL in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/unable-to-find-images-based-on-url-in-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a93740569d1a4ca266c.jpg
tags:
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
- name: url
  slug: url
seo_title: null
seo_desc: "If you're new to React and are having trouble accessing images stored locally,\
  \ you're not alone.\nImagine you have your images stored in a directory next to\
  \ a component like this:\n/src\n  /components\n    - component1\n    - component2\n\
  /img\n  - img1\n  - ..."
---

If you're new to React and are having trouble accessing images stored locally, you're not alone.

Imagine you have your images stored in a directory next to a component like this:

```
/src
  /components
    - component1
    - component2
/img
  - img1
  - img2
```

And you're trying to access the images in the `/img` directory from `component2`:

```jsx
import React, { Component, useState, useEffect } from 'react';
import { render } from 'react-dom'
import { useTransition, animated, config } from "react-spring";
import imgArr from './images';
import '../App.css';

const Slideshow = () => {
  const [index, set] = useState(0)
  const transitions = useTransition(imgArr[index], item => item.id, {
    from: { opacity: 0 },
    enter: {opacity: 1 },
    leave: { opacity: 0 },
    config: config.molasses,
  })
  useEffect(() => void setInterval(() => set(state => (state + 1) % 4), 2000), [])
  return transitions.map(({ item, props, key }) => (
    <animated.div
      key={key}
      className="bg"
      style={{ ...props, slideshowContainerStyle}}
    >
      <img className="img" src={require(item.url)} alt=""/>
    </animated.div>
  ))
}

const slideshowContainerStyle = {
 width: '80%',
 height: '300px'
}


export default Slideshow;

```

You've tried the paths `../img/img1.jpg` and `..img/img1.jpg`, but get `Error: Cannot find module '<path>'` .

So what's going on here?

## A little about `create-react-app`

Like most people, you probably used `create-react-app` to bootstrap your project.

In that case, using relative paths can be a bit tricky because `create-react-app` builds the HTML, CSS, and JavaScript files to an output folder:

```
/public
  - index.html
  - bundle.js
  - style.css
```

There are a number of ways to use images with `create-react-app`, but one of the easiest is to include your images into `/public`. When your project is built, `/public` serves as the root directory.

You can read more about adding images or other assets in the [Create React App docs](https://create-react-app.dev/docs/adding-images-fonts-and-files/).

## Importing images

If you took a look at the docs, you'll notice that the code includes `import` statements to load assets like images and fonts.

Importing is useful when your asset, in this case an image, is in the same directory or near the component that uses it, and won't be used anywhere else. For example, if you have an input component with buttons that use SVGs for thumbs up and thumbs down icons.

A bit advantage of using `import` is that it will throw an error during build time if there's a typo. This sort of checking helps ensure users won't see a broken image that slipped by.

