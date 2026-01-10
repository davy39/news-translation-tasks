---
title: Cool Chrome DevTools tips and tricks you wish you knew already
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-03-21T03:43:40.000Z'
originalURL: https://freecodecamp.org/news/cool-chrome-devtools-tips-and-tricks-you-wish-you-knew-already-f54f65df88d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7B6B7FIxj18TSeYxh1ssLA.png
tags:
- name: Google Chrome
  slug: chrome
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Check out my overview of Chrome DevTools if you’re new to this awesome browser feature!

  1. Drag-and-drop in the Elements panel

  In the Elements panel, you can drag and drop any HTML el...'
---

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

_Check out my [overview of Chrome DevTools](https://flaviocopes.com/browser-dev-tools/) if you’re new to this awesome browser feature!_

### 1. Drag-and-drop in the Elements panel

In the Elements panel, you can drag and drop any HTML element and change its position across the page

![Image](https://cdn-media-1.freecodecamp.org/images/J3dSB29NHaiRsAyWJoY3CtiY5YfvRiHztkkz)
_Drag-and-drop in the Elements panel_

### 2. Reference the currently selected element in the Console

Select a node in the Elements panel, and type `$0` in the console to reference it.

If you’re using jQuery, you can enter `$($0)` to access the jQuery API on this element.

![Image](https://cdn-media-1.freecodecamp.org/images/uBex4ymprtLR2QDMMBJEACRiGwM5tCJqX0zo)
_Reference the currently selected element in the Console_

### 3. Use the value of the last operation in the Console

Use `$_` to reference the return value of the previous operation executed in the Console

![Image](https://cdn-media-1.freecodecamp.org/images/-aFTiSJharifJBxSjaWA58lKtao6TYP6ws24)
_Use the value of the last operation in the Console_

### 4. Add CSS and edit the element state

In the Elements panel there are two super useful buttons.

The first lets you add a new CSS property with any selector you want, but pre-filling the currently selected element:

![Image](https://cdn-media-1.freecodecamp.org/images/aLksEN0rT35gMIVX1a-OKKH4GO6pPLUl2TYl)
_Add CSS rules_

The second one lets you trigger a state for the selected element, so you can see the styles applied when it’s active, hovered, or on focus.

![Image](https://cdn-media-1.freecodecamp.org/images/tcLTyDx-Cpj63K80yhGngLvCJUC8vq00JKL9)
_Edit the element state_

### 5. Save to file the modified CSS

Click the name of the CSS file that you edited. The inspector opens it into the Sources pane, and from there you can save it with the live edits you applied.

This trick does not work for new selectors added using +, or into the `element.style` properties, but only for modified, existing ones.

![Image](https://cdn-media-1.freecodecamp.org/images/cjIJRyFBsrqtacu7x-2hI2A138q1IkzGkOCx)
_Save to file the modified CSS_

### 6. Screenshot a single element

Select an element and press `cmd-shift-p` (or `ctrl-shift-p` in Windows) to open the Command Menu, and select **Capture node screenshot**

![Image](https://cdn-media-1.freecodecamp.org/images/VY-9pqkmmxqQ65gagIT9ny1chbAFilNSARYx)
_Screenshot a single element_

### 7. Find an element using CSS selectors

Pressing `cmd-f` (`ctrl-f` in Windows) opens the search box in the Elements panel.

You can type any string in there to match the source code, or you can also use CSS selectors to have Chrome generate an image for you:

![Image](https://cdn-media-1.freecodecamp.org/images/Et49Lo99VjJ8U7ecVlVHiDUKjbtgYlv3iQ-l)
_Find an element using CSS selectors_

### 8. Shift-enter in the Console

To write commands that span over multiple lines in the Console, press `shift-enter`.

Once you’re ready, press enter at the end of the script to execute it:

![Image](https://cdn-media-1.freecodecamp.org/images/Zp-kmkNp-xwadTjGHYBtG8iVDd2doLcvSF5c)
_Shift-enter in the Console to write multiline commands_

You can clear the console using the _Clear_ button on the top-left of the console, or by pressing `ctrl-l` or `cmd-k`.

### 9. Go to…

In the Sources panel:

* `cmd-o` (`ctrl-o` in Windows), shows all the files loaded by your page.
* `cmd-shift-o` (`ctrl-shift-o` in Windows) shows the symbols (properties, functions, classes) in the current file.
* `ctrl-g` goes to a specific line.

![Image](https://cdn-media-1.freecodecamp.org/images/puVmoQLIN2MNVSZCth0a2uIXoQtUYektEvXo)
_Go to file_

### 10. Watch Expression

Instead of writing again and again a variable name or an expression you are going to check a lot during a debug session, add it to the _Watch Expression_ list.

![Image](https://cdn-media-1.freecodecamp.org/images/bu7wYPMPNH4P3QTIepcO17XaU-Ydsl0vxjlR)
_Watch Expression_

### 11. XHR/Fetch debugging

From the debugger open the **XHR/Fetch Breakpoints** panel.

You can set it to break any time an XHR/Fetch call is sent, or just on specific ones:

![Image](https://cdn-media-1.freecodecamp.org/images/uoE2VO1YJrvhZ2gc8NgpRdInyu9TKtPjiihw)
_XHR/Fetch debugging_

### 12. Debug on DOM modifications

Right-click an element and enable _Break on Subtree Modifications._ Whenever a script traverses that element’s children and modifies them, the debugger stops automatically to let you inspect what’s happening.

![Image](https://cdn-media-1.freecodecamp.org/images/hvvrtgLnmMgnDQogl0m9A2gF9FCyfUZfnpbk)
_Debug on DOM modifications_

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

