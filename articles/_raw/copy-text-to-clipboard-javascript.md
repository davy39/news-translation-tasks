---
title: How to Copy Text to the Clipboard with JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-14T21:18:48.000Z'
originalURL: https://freecodecamp.org/news/copy-text-to-clipboard-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--14-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: When you're building advanced web pages and applications, you'll sometimes
  want to add the copy feature. This lets your users simply click a button or icon
  to copy text rather than highlighting the text and clicking a couple of buttons
  on the keyboar...
---

When you're building advanced web pages and applications, you'll sometimes want to add the copy feature. This lets your users simply click a button or icon to copy text rather than highlighting the text and clicking a couple of buttons on the keyboard.

This feature is mostly used when someone needs to copy an activation code, recovery key, code snippet, and so on. You can also add functionalities like an alert or text on the screen (which could be a modal) to inform the user that the text has been copied to their clipboard.

Previously you would've handled this with the `document.execCommand()` command, but that is deprecated (no longer recommended). You can now use the Clipboard API, which allows you to respond to clipboard commands (cut, copy, and paste) and asynchronously read from and **write to** the system clipboard.

In this article, you will learn how to write (copy) text and images to the clipboard with the Clipboard API.

In case you are in a rush, here is the code:

```js
<p id="myText">Hello World</p>
<button class="btn" onclick="copyContent()">Copy!</button>

<script>
  let text = document.getElementById('myText').innerHTML;
  const copyContent = async () => {
    try {
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
  }
</script>
```

If you are not in a rush, let’s understand more about the Clipboard API and see how this works with a demo project.

## How to Check the Browser's Permissions

It is important to know that the Clipboard API is only supported for pages served over HTTPS. You should also check for browser permissions before attempting to write to the clipboard to verify if you have the write access. You can do this with the `navigator.permissions` query:

```js
navigator.permissions.query({ name: "write-on-clipboard" }).then((result) => {
  if (result.state == "granted" || result.state == "prompt") {
    alert("Write access granted!");
  }
});
```

## How to Copy Text to the Clipboard

To copy text with the new *Clipboard API*, you will use the asynchronous `writeText()` method. This method accepts only one parameter - the text to copy to your clipboard. This can be a string, a template literal holding variables and other strings, or a variable used to hold a string.

Since this method is asynchronous, it returns a promise. This promise is resolved if the clipboard has been updated successfully, and is rejected otherwise:

```js
navigator.clipboard.writeText("This is the text to be copied").then(() => {
  console.log('Content copied to clipboard');
  /* Resolved - text copied to clipboard successfully */
},() => {
  console.error('Failed to copy');
  /* Rejected - text failed to copy to the clipboard */
});
```

You can also use async/await alongside try/catch:

```js
async function copyContent() {
  try {
    await navigator.clipboard.writeText('This is the text to be copied');
    console.log('Content copied to clipboard');
    /* Resolved - text copied to clipboard successfully */
  } catch (err) {
    console.error('Failed to copy: ', err);
    /* Rejected - text failed to copy to the clipboard */
  }
}
```

### Copy text to clipboard example

Here is a demo showing how it works using a real-life example. In this example, we're fetching quotes from a public quote API. Then when you click the copy icon, the quote and its author get copied, showing that you can adjust what you copy into the `writeText()` method.

See the Pen [copy text JS](https://codepen.io/olawanlejoel/pen/MWGLXyX) by Olawanle Joel ([@olawanlejoel](https://codepen.io/olawanlejoel)) on [CodePen](https://codepen.io).

## Wrapping Up

In this article, you have learned how to copy text to the clipboard with JavaScript using the Clipboard API without having to think outside the box or install any JavaScript library.

Have fun coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
