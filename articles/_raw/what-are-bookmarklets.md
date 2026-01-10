---
title: What are Bookmarklets? How to Use JavaScript to Make a Bookmarklet in Chromium
  and Firefox
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-06-17T00:53:04.000Z'
originalURL: https://freecodecamp.org/news/what-are-bookmarklets
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cover-defectivefox-o-1.png
tags:
- name: automation
  slug: automation
- name: Google Chrome
  slug: chrome
- name: Firefox
  slug: firefox
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'Bookmarklets are browser bookmarks that execute JavaScript instead of opening
  a webpage. They''re also known as bookmark applets, favlets, or JavaScript bookmarks.

  Bookmarklets are natively available in all major browsers, including Mozilla Firefox
  an...'
---

[Bookmarklets](https://en.wikipedia.org/wiki/Bookmarklet) are browser bookmarks that execute JavaScript instead of opening a webpage. They're also known as bookmark applets, favlets, or JavaScript bookmarks.

Bookmarklets are natively available in all major browsers, including Mozilla Firefox and Chromium-based browsers like Chrome or Brave.

## Scripting with JavaScript

Learning how to write scripts provides many benefits, namely the huge time-savings from automating repetitive or tedious tasks.

If you aren't a developer, the idea of learning to code might be intimidating, however scripting doesn't require software engineering knowledge or design patterns. The goal isn't to make scalable software, but rather to automate specialized or trivial tasks.

Regardless of profession, even if you've never written code before, consider what you do in your browser. If you ever feel what you do is repetitive or robotic, consider the possibility of delegating the task to an actual robot.

## Use Cases for Bookmarklets

With bookmarklets, you can manipulate the current page as the function will have the context of the current tab. This means you can:

* Click buttons virtually
    
* Modify the content
    
* Use the content of the page to open a new page
    
* Remove elements from the page
    

You can also make bookmarks that don't utilize the context at all, such as conditionally opening a URL, or generating HTML for a new tab.

You'll find some bookmarklets I made for this article in [Example Bookmarklets](#heading-example-bookmarklets). They're just for demonstration, but should make the capabilities and implementations apparent.

## How to Create Bookmarklets

Creating a bookmarklet is almost identical to creating a regular bookmark. The only difference is that you'll write JavaScript in the URL field instead of an HTTP/HTTPS URL.

### Navigate to the Bookmark Menu

#### Mozilla Firefox

Either in your bookmarks bar, or in the Bookmarks sidebar (`CTRL` + `B`), you can right-click, then click "Add Bookmark...":

![The "Add bookmark" modal when creating a new bookmark in Firefox.](https://www.freecodecamp.org/news/content/images/2021/06/firefox-1.png align="left")

#### Chromium

You can right-click your bookmarks bar, then click "Add page...". Alternatively, you can go to your Bookmarks manager, then right-click and click "Add new bookmark":

![The "Edit bookmark" modal when creating a new bookmark in Chromium.](https://www.freecodecamp.org/news/content/images/2021/06/chromium.png align="left")

## How to Write a Bookmarklet

In the URL field of the bookmark modal, write a JavaScript function in the following format.

```js
javascript: (() => {
  // Your code here!
})();
```

`javascript:` is the URL's protocol. This indicates that the browser should execute the bookmark as JavaScript.

`(() => { })` defines an anonymous function (lambda). You should write the code you want to execute between the curly braces.

`();` will execute the anonymous function you just created.

```js
javascript: (() => {
  alert('Hello, World!');
})();
```

![A browser alert with the message: "Hello, World!"](https://www.freecodecamp.org/news/content/images/2021/06/image-147-1.png align="left")

You can also make it generate HTML and open it as an HTML document:

```js
javascript: (() => {
  return '<h1 style="color: white; background-color: black;">Hello, World!</h1>';
})();
```

### Spacing for Bookmarklets

Most browsers don't allow a multiline input field in the bookmark URL, so you'll usually have to make strict use of curly braces (`{` and `}`) and semi-colons (`;`) when writing bookmarklets. This is especially important when scoping conditional constructs (`if`/`for`/`while`).

Other than this, spacing doesn't matter. Don't be afraid to have a lot of code in one line because that's all you've got:

```js
javascript: (() => {   const documentHTML = document.documentElement.outerHTML;   const matches = documentHTML.matchAll(/[\w.+=~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*/g);   const flatMatches = Array.from(matches).map((item) => item[0]);   const uniqueMatches = Array.from(new Set(flatMatches));      if (uniqueMatches.length > 0) {     const result = uniqueMatches.join('\n');     alert(result);   } else {     alert('No emails found!');   } })();
```

If your script is complex, it'll be easier to maintain your bookmarklet in a code editor like [Visual Studio Code](https://code.visualstudio.com/). You can copy and paste it over to your browser when it's ready.

### How to Interact with Websites

The most common thing you'd do with bookmarklets is manipulating or interacting with websites you have open.

#### The Global Document Object

As the bookmarklet has the context of the page you're on, you have access to the `[document](https://developer.mozilla.org/en-US/docs/Web/API/Document)` object.

The ideal functions for selecting elements for our use case are:

* [`querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) to select a single element by CSS selector.
    
* [`querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) to select all matching elements by CSS selector.
    
* `[evaluate](https://developer.mozilla.org/en-US/docs/Web/API/Document/evaluate)` to select all matching elements by XPath.
    

There are other functions like `[getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)` and `[getElementsByClassName](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName)`, but we want to avoid false-positives, so we'll always make a strict selection using multiple element attributes.

#### CSS Selectors and XPath

If you're only selecting elements based on element names, IDs, classes, and other attributes, using a CSS selector will be simple and efficient.

CSS selectors are used to select elements in HTML documents to apply styles. If you're familiar with web development or CSS in general, then you already know how to use CSS selectors. (More Info: [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors), [freeCodeCamp](https://www.freecodecamp.org/news/css-selectors-cheat-sheet/))

If you need to match the text content of an element as well, then you'll have to use XPath instead.

XPath is used to traverse XML documents, it provides all the capabilities of CSS selectors and more, including comparing the content of elements or using a regular expression to match it. (More Info: [MDN](https://developer.mozilla.org/en-US/docs/Web/XPath), [Wikipedia](https://en.wikipedia.org/wiki/XPath))

#### How to Select Elements from the Webpage

One of the most common uses for bookmarklets is manipulating webpages. To interact with, manipulate, or remove elements from the page, you'll always have to select the elements first.

1. First open the browser development tools by pressing `F12`, or `CTRL` + `SHIFT` + `I`.
    
2. Click the [Inspector](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector)/[Elements](https://developer.chrome.com/docs/devtools/dom/) tab, which displays the full HTML document of the page you have open.
    
3. Use the element selector tool (`CTRL` + `SHIFT` + `C`) and click on the element you want to interact with. The document viewer will scroll to the element you clicked in the HTML document. You'll see the element ID, classes, and attributes.
    
4. Check if you're on the correct element. Elements can be nested where it's easier to navigate to it manually in the HTML. For example, you may have clicked an `svg` element, but actually needed the `button` or `div` it was inside of.
    
5. Define a CSS selector or XPath that matches everything you want, you might want to make it more strict than necessary to avoid potential false-positives.
    

For example, suppose I wanted to dismiss all topic suggestions on Twitter because they're annoying. Here is how a clickable element to dismiss a topic looks like.

![Twitter topic suggestions, with an X button to mark it as "Not interested".](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-16-at-04.19.17.png align="left")

*Twitter topic suggestions, with an X button to mark it as "Not interested".*

```html
<div aria-label="Dismiss" role="button" tabindex="0" class="...">
  <!-- The parent div element has the click listener. -->
  <div class="...">
    <svg viewBox="0 0 24 24" aria-hidden="true" class="...">
      <!-- The actual X icon. -->
    </svg>
  </div>
</div>
```

An appropriate selector is `div[aria-label=Dismiss][role=button]`.

We need to use the `querySelectorAll` function from [The Global Document Object](#heading-the-global-document-object), then call the `[click](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)` method to simulate a click.

A bookmarklet can be implemented to select every dismiss button, and trigger a click event to all of them with a 250ms interval.

```js
javascript: (() => {
  const selector = 'div[aria-label=Dismiss][role=button]';
  const topics = document.querySelectorAll(selector);
    
  for (let i = 0; i < topics.length; i++) {
    let topic = topics[i];
    setTimeout(() => topic.click(), i * 250);
  }
})();
```

## How to Redistribute Bookmarklets

To "install" a bookmarklet, users create a bookmark on their browser and copy and paste the code to it.

This can be inconvenient, so it's common to link bookmarklets when sharing. This is as simple as putting it in the `href` attribute of your link anchor.

```html
<a href="javascript: (() => {   alert('Hello, World!'); })();">
  Hello, World!
</a>
```

Now users can right-click and "Bookmark Link", or drag it to the bookmarks bar for easy access.

Clicking the link on the web page will execute the script immediately. Ensure it's not going to obstruct what a user is trying to achieve on your site if they accidentally click it.

For example, the following link will display an alert with "Hello, World!".

### User Content and Content Security Policy Bypass

If you run a service that allows user-generated content to contain custom HTML, it's important to sanitize link anchors (`a`).

The bookmarklet is executing like code in the developer tools console, and bypasses the configured [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP).

The "Hello, World!" link can just as easily send data to another server, including the input of form fields, or cookies.

As a service provider, it's important to be wary that users can exploit this to share malicious code on your platform. If their link anchor is running on a page under your domain, it can access sensitive information on the page and `[document.cookies](https://developer.mozilla.org/en-US/docs/web/api/document/cookie)`.

You can try it yourself in a sandbox environment:

```html
<a href="javascript: (() => {   alert(document.cookie); })();">
  EvilScript
</a>
```

### Only Run Code You Trust

As a user, it's important to note that any code can be malicious, only click or add bookmarklets where at least one of the following are true:

* It came from a reputable source.
    
* You know JavaScript, and you reviewed what it does.
    
* Someone you trust knows JavaScript, and they reviewed it for you.
    

## Privacy and Security

Bookmarklets can be handy, but we also have [web extensions](https://en.wikipedia.org/wiki/Browser_extension) and [user scripts](https://en.wikipedia.org/wiki/Userscript) too. What makes them different?

Web extensions are incredibly user-friendly and flexible. Bookmarklets can't block network requests, update content as the page changes, or manage tabs.

However, there're some benefits to using bookmarklets over anything else, namely for privacy and security.

An extension that modifies the font on all pages must get permission to access all data on all web pages. On Firefox and Chrome, this includes all input and password fields. (More Info: [Mozilla](https://support.mozilla.org/kb/permission-request-messages-firefox-extensions#w_access-your-data-for-all-websites), [Google](https://developer.chrome.com/docs/extensions/mv3/permission_warnings/#permissions_with_warnings))

In contrast, a bookmarklet only has access to the page for the very moment it's executing, and only when manually triggered by the user.

This results in less risk of malware, a rogue employee can't push a malicious update, and data won't silently get sent to other servers.

The Chrome Web Store has previously had several malicious extensions which had to be taken down. Some of which had millions of installations before being removed. ([More Info](https://en.wikipedia.org/wiki/Chrome_Web_Store#Malware))

## Example Bookmarklets

Here's a list of bookmarklet ideas, along with the code that implements it. You can copy and paste them into new bookmarks to try them out.

```js
javascript: (() => {
  const documentHTML = document.documentElement.outerHTML;
  const matches = documentHTML.matchAll(/[\w.+=~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*/g);
  const flatMatches = Array.from(matches).map((item) => item[0]);
  const uniqueMatches = Array.from(new Set(flatMatches));
  
  if (uniqueMatches.length > 0) {
    const result = uniqueMatches.join('\n');
    alert(result);
  } else {
    alert('No emails found!');
  }
})();
```

```js
javascript: (() => {
  const xpath = "//a [contains(., 'Jobs') or contains(., 'Careers') or contains(., 'Hiring')]";
  const elements = document.evaluate(xpath, document);
  const element = elements.iterateNext();
    
  if (element) {
    element.click();
  } else {
    alert('No links for jobs found!');
  }
})();
```

```js
javascript: (() => {
  const allElements = document.querySelectorAll('*');

  for (let element of allElements) {
    element.style.fontFamily = 'Comic Sans MS';
  }
})();
```

```js
javascript: (() => {
  const destination = "https://www.freecodecamp.org/";
  const alternate = "https://tenor.com/Y6jj.gif";
  
  const date = new Date();
  const hours = date.getHours();
    
  if (hours < 3 || hours >= 6) {
    window.open(destination);
  } else {
    window.open(alternate);
  }
})();
```

Thank you for reading! Now go forth and create your own bookmarklets.
