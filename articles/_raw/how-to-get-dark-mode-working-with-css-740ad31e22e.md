---
title: How to get dark mode working with CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-09T22:04:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-dark-mode-working-with-css-740ad31e22e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y2utWiZeebjS3t5ofXLZPA.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Frank Lämmer

  I have been playing around with MacOS Mojave’s dark mode lately. It’s not 100% pleasing
  to my eyes, yet. But it’s especially useful when nerding out at night time with
  little ambient light.

  Dark mode is a design trend. Many reading ap...'
---

By Frank Lämmer

I have been playing around with MacOS Mojave’s dark mode lately. It’s not 100% pleasing to my eyes, yet. But it’s especially useful when nerding out at night time with little ambient light.

**Dark mode is a design trend.** Many reading applications (Medium App, Twitter …) have it already. It’s not only about just inverting all colors, but it’s also about art direction.

![Image](https://cdn-media-1.freecodecamp.org/images/7MXofS94AfNVI-oYG-rNDkZ9WH8i-PvyNcUB)
_In macOS Mojave you can turn your interface dark. Safari and Firefox are supporting it already._

#### Not everything is dark (yet)

One thing that can be a bit shocking when working in dark mode is the flash of light when opening a document with a big white background. This post explores how to deal with dark mode on the web and styling dark mode with CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/6vFnrxWHWhxykOVOCl6-jcsMpypqSQpbeNAf)
_The author opening this Medium post in dark mode with little ambient light._

### Dealing with dark mode user settings

So wouldn’t it be nice if documents and websites would respect the current surrounding theme?

#### Automatic color conversion?

At least Safari and Firefox already have a “Reader mode” with support for light text on a dark background. Here, the <article> context gets rendered using custom styles for best readability and removing clutter, and there is a setting for inverting colors. Extending on that, browsers might invert websites automatically with smart styles. Sounds scary! But at least Apple Mail is doing so already. It even inverts colors for some HTML mail.

![Image](https://cdn-media-1.freecodecamp.org/images/kSO148kZlhL9q5FvYT-08ooWX2eZXys6f4jI)
_OMG all colors inverted in a HTML mail in Apple Mail, macOS Mojave_

Smart-inverting colors might or might not be a solution. What else?

#### Media query to the rescue!

I am not alone. Dark mode for CSS is currently (August 2018) [**being discussed** in “CSS Working Group Editor Drafts”](https://github.com/w3c/csswg-drafts/issues/2735). The idea is to make that available as a media query. [Something](https://bugs.webkit.org/show_bug.cgi?id=186606) has already landed in Safari ([private](https://twitter.com/rmondello/status/1007400236514504706)), see also [here](https://github.com/WebKit/webkit/commit/46198bd7636f0d1f85e36d830fd3108707d4c169).

So in theory you can do this:

```
@media (prefers-color-scheme: dark) {   color: white;   background: black}
```

Let’s wait until all browsers are ready. I think there is some way to go for standardization. The OS makers might need to agree on something as well.

### Inverted is not dark mode

![Image](https://cdn-media-1.freecodecamp.org/images/K33cTogRj84FtU2LvVq19-VIXMpLli8sEFEs)
_Fun fact: You can invert the colors in dark mode as well._

Did you know: There already is a [media feature for “inverted-colors”](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/inverted-colors) in Media Queries Level 4. That’s not the same as dark mode. A kind of “dark mode” has been around for a while. Windows has also **High Contrast** mode. There are many different takes on that.

Nevertheless, it would be really cool if website authors could decide if and how to deal with it when a user with enabled “dark mode” visited their site. So you, as the designer, have full control over how your website will look in “lights off mode”. Much more work for you? No, it’s easy. Read on.

### Incognito is not dark mode

![Image](https://cdn-media-1.freecodecamp.org/images/C6PA7T3Uj9e0HnFtBfltKMnXvOwLfhS-kVar)
_This is NOT dark mode!_

When opening an incognito window for private browsing, many browsers will present a dark browser chrome to highlight the difference. That’s also not dark mode, but it’s dark.

### Using CSS vars for theming dark mode

Thanks to “CSS custom properties” (also known as “CSS Vars”), we can now more easily than ever create themes with very little CSS. The most simple invert theme:

```
root: {  --text-color: DarkBlue;  --back-color: Azure;}
```

```
body { color: var(--text-color); background: var(--back-color)}
```

```
@media (prefers-dark-interface) {  root: {   --text-color: Azure;   --back-color: DarkBlue;  } }
```

Shameless plug: My (great new) CSS framework Teutonic CSS already makes use of such simple inverting:

![Image](https://cdn-media-1.freecodecamp.org/images/2oe6YHeKR513YrwBo3gSPRqppu46nE27OEFj)
_Put “.inverted” on the outer container to invert all colors via CSS Vars. See it in action [here](https://teutonic.co/examples/colors#inverted" rel="noopener" target="_blank" title=")._

### Websites changing browser chrome

This article is about how a user setting can change the appearance of a website. It also works the other way around: a website can change the way the browser looks. There are some proprietary meta tags available, so far only for mobile browsers:

```
<meta name="theme-color" content="black"><meta name="msapplication-navbutton-color" content="black"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black">
```

_ARGH!_

### Further readings

The article “[**OS: High Contrast versus Inverted Colors**](http://adrianroselli.com/2017/11/os-high-contrast-versus-inverted-colors.html)” by Adrian Roselli discusses the differences between “inverted” and “high contrast” in Windows and macOS.

The article “[**How “invert brightness” can improve accessibility and help us use our devices**](https://developer.paciellogroup.com/blog/2017/12/how-invert-brightness-can-improve-accessibility-and-help-us-use-our-devices/)” by Matthew Atkinson discusses how inverting colors helps with the user experience. You can also find the concept of “smart inverting” colors there.

### Summary

![Image](https://cdn-media-1.freecodecamp.org/images/hNpXvSYGCgpEBw1FoDrNj0bKDeNCiEAQ1umU)
_A day/night switch on microsoft developer pages. Nice detail: this setting is persistent (localstorage or cookie)._

The nice thing about standards is that you have so many to choose from.

While “night mode” is definitely a trend, different implementations are floating around. Raise your voice to make that ONE web standard. Get your CSS forward compatible so you can support that without too much hustle.

