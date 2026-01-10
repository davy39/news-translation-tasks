---
title: How to detect a user’s preferred color scheme in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:54:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-detect-a-users-preferred-color-scheme-in-javascript-ec8ee514f1ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QPIhIZte1bW0DKQoLoXwxw.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Neo4j
  slug: neo4j
- name: General Programming
  slug: programming
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Oskar Hane

  In recent versions of macOS (Mojave) and Windows 10, users have been able to enable
  a system level dark mode. This works well and is easy to detect for native applications.

  Websites have been the odd apps where it’s up to the website pu...'
---

By Oskar Hane

In recent versions of macOS (Mojave) and Windows 10, users have been able to enable a system level dark mode. This works well and is easy to detect for native applications.

Websites have been the odd apps where it’s up to the website publisher to decide what color scheme the users should use. Some websites do offer theme support. For the users to switch, they have to find the configuration for it and manually update the settings for each individual website.

Would it be possible to have this detection done automatically and have websites present a theme that respects the user’s preference?

![Image](https://cdn-media-1.freecodecamp.org/images/1*QPIhIZte1bW0DKQoLoXwxw.png)
_Light vs Dark theme in Neo4j Browser_

### CSS media query ‘`prefers-color-scheme'` draft

There is a CSS media queries draft level 5 where [prefers-color-scheme](https://drafts.csswg.org/mediaqueries-5/#descdef-media-prefers-color-scheme) is specified. It is meant to detect if the user has requested the system to use a light or dark color theme.

This sounds like something we can work with! We need to stay up to date with any changes to the draft, though, as it might change at any time since it’s just a… draft. The `prefers-color-scheme` query can have three different values: `light`, `dark`, and `no-preference`.

### Web browser support as of March 2019

The current browser support is _very_ limited, and it’s not available in any of the stable releases of any vendor. We can only enjoy this in [Safari Technology Preview of version 12.1](https://developer.apple.com/safari/technology-preview/) and in [Firefox 67.0a1](https://www.mozilla.org/en-US/firefox/67.0a1/releasenotes/). What’s great is that there are binaries that do support it, so we can work with it and try it out in web browsers. For current browser support, check out [https://caniuse.com/#search=prefers-color-scheme](https://caniuse.com/#search=prefers-color-scheme).

### Why CSS only detection isn’t enough

The common approach I’ve seen so far is to use a CSS only approach and override CSS rules for certain classes when a media query is matched.  
Something like this:

```css
/* global.css */

.themed {
  display: block;
  width: 10em;
  height: 10em;
  background: black;
  color: white;
}

@media (prefers-color-scheme: light) {
  .themed {
    background: white;
    color: black;
  }
}

```

As this works fine for many use cases, there are styling techniques that do not use CSS in a way like this. If [styled-components](https://www.styled-components.com) is used for theming, for example, then a JS object is replaced when the theme is changed.

Having access to the preferred scheme is also useful for analytics and more predictable CSS overrides as well as more fine-grained control over which elements should be themed and not.

### Initial JS approach

I’ve learned in the past that you can do media query detection by setting the CSS `content` of an element to a value if a media query is matched. This is definitely a hack, but it works!

Something like this:

```css
/* global.css */

html {
  content: "";
}

@media (prefers-color-scheme: light) {
  html {
    content: "light";
  }
}

@media (prefers-color-scheme: dark) {
  html {
    content: "dark";
  }
}

```

So when a user loads the CSS and the media query matches one of the above color schemes, the `content` property value of the `html` element is set to either ‘light’ or ‘dark’.

The question then is, how do we read the `content` value of the `html` element?

We can use [window.getComputedStyle](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle), like this:

```js
const value = window
  .getComputedStyle(document.documentElement)
  .getPropertyValue('content')
  .replace(/"/g, '')

// value is now "dark", "light" or empty string

```

And this works fine! This approach is fine for a **one-time read**, but it’s not reactive and automatically updates when the user changes their system color scheme. To be updated, a page reload is needed (or have the above read done at an interval).

### Reactive JS approach

How can we know when the user changes the system color scheme? Are there any events we can listen to?

Yes there are!

There is [window.matchMedia](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia) available in [modern web browsers](https://caniuse.com/#feat=matchmedia).

What’s great with `matchMedia` is that we can attach a listener to it that will be called anytime the match changes.

The listener will be called with an object containing the information if the media query started matching or if it stopped matching. With this info, we can skip the CSS altogether and just work with JS.

```js
const DARK = '(prefers-color-scheme: dark)'
const LIGHT = '(prefers-color-scheme: light)'

function changeWebsiteTheme(scheme) {
  // 'dark' or 'light' string is in scheme here
  // so the website theme can be updated
}

function detectColorScheme() {
  if (!window.matchMedia) {
    return
  }

  function listener({ matches, media }) {
    if (!matches) {
      // Not matching anymore = not interesting
      return
    }

    if (media === DARK) {
      changeWebsiteTheme('dark')
    } else if (media === LIGHT) {
      changeWebsiteTheme('light')
    }
  }

  const mqDark = window.matchMedia(DARK)
  mqDark.addListener(listener)

  const mqLight = window.matchMedia(LIGHT)
  mqLight.addListener(listener)
}

```

This approach works really well in the supported web browsers and just opts out if `window.matchMedia` isn't supported.

### React hook

Since we are using React in [neo4j-browser](https://github.com/neo4j/neo4j-browser), I wrote this as a custom React hook to make it easy to re-use in all of our apps and fit into the React system.

```js
// useDetectColorScheme.js
import { useState, useEffect } from 'react'

// Define available themes
export const colorSchemes = {
  DARK: '(prefers-color-scheme: dark)',
  LIGHT: '(prefers-color-scheme: light)',
}

export default function useDetectColorScheme(defaultScheme = 'light') {
  // Hook state
  const [scheme, setScheme] = useState(defaultScheme)

  useEffect(() => {
    // No support for detection
    if (!window.matchMedia) {
      return
    }

    // The listener
    const listener = (e) => {
      // No match = not interesting
      if (!e || !e.matches) {
        return
      }

      // Look for the matching color scheme
      // and update the hook state
      const schemeNames = Object.keys(colorSchemes)
      for (let i = 0; i < schemeNames.length; i++) {
        const schemeName = schemeNames[i]

        if (e.media === colorSchemes[schemeName]) {
          setScheme(schemeName.toLowerCase())
          break
        }
      }
    }

    // Loop through and setup listeners for the
    // media queries we want to monitor
    let activeMatches = []
    Object.keys(colorSchemes).forEach((schemeName) => {
      const mq = window.matchMedia(colorSchemes[schemeName])

      mq.addListener(listener)
      activeMatches.push(mq)
      listener(mq)
    })

    // Remove listeners, no memory leaks
    return () => {
      activeMatches.forEach((mq) => mq.removeListener(listener))
      activeMatches = []
    }
    // Run on first load of hook only
  }, [])

  // Return the current scheme from state
  return scheme
}

```

It’s a bit more code than in the first short proof-of-concept. We have better error detection and we also remove the event listeners when the hook un-mounts.

In our use case, the users can choose to override the autodetected scheme with something else (we offer an outlined theme for example, often used when doing presentations).

And then use it like this in the application layer:

```jsx
// App.jsx
import React from 'react'
import ThemeProvider from './ThemeProvider'
import useDetectColorScheme from './useDetectColorScheme'
export default function App({ configuredTheme, themeData, children }) {
  // Detect scheme and have 'light' as the default
  const autoScheme = useDetectColorScheme('light')

  // Check if user want to override the auto detected scheme
  const scheme = configuredTheme === 'auto' ? autoScheme : configuredTheme

  // Pass the theme data to a theme provider component
  return <ThemeProvider theme={themeData[scheme]}>{children}</ThemeProvider>
}

```

The last part depends on how theming is made in your application. In the example above, the theme data object is passed into a context provider that makes this object available throughout the whole React application.

### End result

Here’s a gif with the end result, and as you can see, it’s instant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dp2Nj97f12YMhEXuUiybTA.gif)

### Final thoughts

This was a fun experiment made during a so-called “Lab Day” we have in the UX team at [Neo4j](https://neo4j.com). The early stages of the spec and (therefore) the lack of browser support does not justify this to make it into any product yet. But support might come sooner than later.

And besides, we do ship some Electron-based products and there is an `[electron.systemPreferences.isDarkMode()](https://github.com/electron/electron/blob/master/docs/api/system-preferences.md#systempreferencesisdarkmode-macos)` available there...

### About the author

[Oskar Hane](https://twitter.com/oskarhane) is a team lead / senior engineer at [Neo4j](https://neo4j.com).  
He works on multiple of Neo4j:s end-user applications and code libraries and have authored two tech books.

Follow Oskar on twitter: [@oskarhane](https://twitter.com/oskarhane)

