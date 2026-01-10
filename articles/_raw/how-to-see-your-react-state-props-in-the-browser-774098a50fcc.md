---
title: How to see your React state & props in the browser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T21:40:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-see-your-react-state-props-in-the-browser-774098a50fcc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QeEbGcmtoQ3T_zUdpG8TZw.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: coding
  slug: coding
- name: Firefox
  slug: firefox
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'By Andrew Bales

  If you’re building a web app with React, you may want to see the state or props
  of components in real-time. Here’s a quick solution for Chrome & FireFox!

  React Developer Tools

  Install the React Developer Tools extension for Chrome or ...'
---

By Andrew Bales

If you’re building a web app with React, you may want to see the state or props of components in real-time. Here’s a quick solution for Chrome & FireFox!

### React Developer Tools

Install the React Developer Tools extension for [Chrome](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) or [FireFox](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/). It allows you to inspect React component hierarchies within the developer tools — the same way you would peek at the DOM elements, console, or network.

### Inspecting React Components

1. Open your app and inspect the page with developer tools (Command+Option+I).
2. Select the React Developer Tools

![Image](https://cdn-media-1.freecodecamp.org/images/nRV4nSI2fdxIBQyhGSDu69Vz83ruxGJHk3tL)

3. Pick a component in the tree to see its state and current props.

![Image](https://cdn-media-1.freecodecamp.org/images/Wo9vvCc3YMSTCGv2R55u87Ttgi8mLdGdBR1E)

You can also select a React element directly from the page by hovering over it with the selection tool:

![Image](https://cdn-media-1.freecodecamp.org/images/-uN55RQ0UWYdHrjJ0quyPHmAEY5dlpumQlzF)
_Selection tool menu icon in developer tools_

### Modifying the State

If you want to update your state in the browser— you can! Modify it by clicking and editing state attributes in the React tab. This will re-render the DOM, passing the state down through the props.

Happy coding! ?

