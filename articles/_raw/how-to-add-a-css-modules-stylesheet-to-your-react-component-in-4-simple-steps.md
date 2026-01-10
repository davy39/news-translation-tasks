---
title: How to add a CSS Modules Stylesheet to your React component in 4 simple steps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-28T13:03:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-css-modules-stylesheet-to-your-react-component-in-4-simple-steps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca135740569d1a4ca4d4a.jpg
tags:
- name: CSS
  slug: css
- name: CSS Modules
  slug: css-modules
- name: React
  slug: react
seo_title: null
seo_desc: 'By Holly Atkinson

  Let’s say you’d like to add a CSS Modules Stylesheet to your project. You can find
  Create React App’s guidance here, but essentially — and as the guidance states — CSS
  Modules let you use the same CSS selector in different files wit...'
---

By Holly Atkinson

Let’s say you’d like to add a CSS Modules Stylesheet to your project. You can find Create React App’s [guidance](https://facebook.github.io/create-react-app/docs/adding-a-css-modules-stylesheet) here, but essentially — and as the guidance states — CSS Modules let you use the _same_ CSS selector in different files without worrying about naming clashes. This works because each HTML element in your file that you want to style is automatically given a _unique_ class name.

This can seem quite confusing at first, but really the process to implement CSS Modules can be simplified to just 4 steps, as demonstrated in the below example.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_lmno_4nmNyohGa-gM_GaEw.jpeg)
_Yes, really!_

### Adding modular CSS to a simple <Link /> component

1. A feature of React is that CSS Modules are “turned on” for files ending with the `.module.css` extension. Create the CSS file with a specific filename in the following format:

```bash
Link.module.css
```

2. Import styling to your component:

```jsx
import styles from ‘../styling/components/Link.module.css’
```

3. The styles in your CSS file can follow your preferred naming convention, for instance:

```css
.bold {  font-weight: bold;}
```

4. The style is applied to the HTML element as follows:

```jsx
className={styles.bold}
```

And that’s it!

_Photo credit:_ [_Adrian Swancar_](https://unsplash.com/photos/72El6N0cmj4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) _on_ [_Unsplash_](https://unsplash.com/search/photos/confused?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

