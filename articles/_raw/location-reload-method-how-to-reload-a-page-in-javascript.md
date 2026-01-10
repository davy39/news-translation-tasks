---
title: 'Location Reload Method: How to Reload a Page in JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-09T21:43:00.000Z'
originalURL: https://freecodecamp.org/news/location-reload-method-how-to-reload-a-page-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ecf740569d1a4ca3f4d.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript Location.reload() method provides means to reload the page at
  current URL.

  The syntax is the following:

  object.reload(forcedReload);, where forceReload is an optional parameter.

  To simply reload the page, you can input window.location as o...'
---

JavaScript `Location.reload()` method provides means to reload the page at current URL.

The syntax is the following:

`object.reload(forcedReload);`, where `forceReload` is an optional parameter.

To simply reload the page, you can input `window.location` as object.

Optional parameters `force reload` is a boolean value, which if set to:

`True` reloads the page from the server (e.g. does not store the data cached by the browser):

```text
window.location.reload(true);
```

`False` reloads the page using the version of the page cached by the browser.

```text
window.location.reload(false);
```

`False` is the default parameter, so if left blank, `object.reload()` reloads the page using the broswer’s cached data, i.e. is identical to using the method as `object.reload(false)`.

To create the effect of browser-provided “Refresh”-option, you may want to create HTML-button and do either of the following:

* attach `Location.reload()` to the HTML button-markup, like this:

```text
<input type="button" value="Refresh Button" onClick="window.location.reload()"> 
```

* assign on-click event to the button with the function that uses the method, where the button looks similar to

```text
<button type="button" onClick="reloadThePage()">Refresh!</button>
```

```text
<script>
function reloadThePage(){
    window.location.reload();
} 
</script>
```

### **Example:**

```javascript
// Reload the current resources from the server
window.location.reload(true);

// Reload the current resources from the browser's cache
window.location.reload();
```

This will reload the page at the current URL from the server.

#### **More Information:**

* [MDN](https://developer.mozilla.org/docs/Web/API/Location/reload)

