---
title: How to Make a Chrome Extension – a Browser Plugin Development Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-25T19:04:48.000Z'
originalURL: https://freecodecamp.org/news/chrome-extension-with-parcel-tailwind
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/emile-perron-xrVDYZRGdw4-unsplash.jpg
tags:
- name: chrome extension
  slug: chrome-extension
- name: plugins
  slug: plugins
- name: tailwind
  slug: tailwind
seo_title: null
seo_desc: 'By Marouane Rassili

  Building a Chrome extension can be overwhelming. It''s different than building a
  web app in that you don''t want to put too much JavaScript overhead on the browser
  since your extension will be run along with the website you''re visit...'
---

By Marouane Rassili

Building a Chrome extension can be overwhelming. It's different than building a web app in that you don't want to put too much JavaScript overhead on the browser since your extension will be run along with the website you're visiting. You also don't usually get the benefit of bundling and debugging that are available with today's bundlers and frameworks.

When I decided to build a Chrome extension, I found that the number of blog posts and articles about building one is quite small. And there's even less information when you want to use one of the newer technologies like TailwindCSS.

In this tutorial we will discover how to build a Chrome extension using Parcel.js for bundling and watching and TailwindCSS for styling. We will also talk about how to separate your styling from the website to avoid colliding CSS – but more on that later.

**There are a few types of Chrome extensions worth mentioning:**

- **Content scripts**: The first type of Chrome extension is the most common. It runs in the context of a web page and can be used to modify its content. This is the type of extension we'll be creating.
- **Popup**: Popup-based extensions use the extension icon to the right of the address bar to open a popup which can contain any HTML content that you like.
- **Options UI**: You guessed it! This is a UI for customizing options as an extension. It's accessible by right clicking the extension icon and selecting "options" or by navigating to the extension's page from the Chrome extensions list `chrome://extensions`
- **DevTools Extension**: "A DevTools extension adds functionality to the Chrome DevTools. It can add new UI panels and sidebars, interact with the inspected page, get information about network requests, and more". -[Google Chrome documentation](https://developer.chrome.com/extensions/devtools)

In this tutorial we will build a Chrome extension using only content scripts by displaying content on the web page and interacting with the DOM.

## How to bundle your Chrome Extension using Parcel.js V2

Parcel.js is a zero-configuration web application bundler. It can use any kind of file as an entry point. It's simple to use and will work for any type of app including Chrome Extensions.

First create a new folder called `demo-extension` (make sure you have `yarn` or `npm` installed, I am going to use `yarn` for this post):

`$ mkdir demo-extension && cd demo-extension && yarn init -y`

Next we will install Parcel as a local dependency:

`$ yarn add -D parcel@next`

Now create a new directory called `src`:

`$ mkdir src`


### Adding a manifest file

Every browser extension needs a manifest file. This is where we define the version and meta data about our extension, but also the scripts that are used (content, background, popup, .etc) and permissions if any. 

You can find the full schema in Chrome's documentation: https://developer.chrome.com/extensions/manifest

Let's go ahead and add a new file in `src` called `manifest.json` with this content:

```json
{
  "name": "Demo extension",
  "description": "An extension built with Parcel and TailwindCSS.",
  "version": "1.0",
  "manifest_version": 2,
}
```

Now, before we go into more detail about how chrome extensions work and the kind of stuff you can make with them, we are going to set up [TailwindCSS](https://tailwindcss.com/)


### How to use TailwindCSS with your Chrome Extension

TailwindCSS is a CSS-framework that uses lower-level utility classes to create reusable but also customizable visual UI components.

Tailwind can be installed in two ways, but the most common way to use it is via its NPM package: 

`$ yarn add tailwindcss`

Also, go ahead and add `autoprefixer` and `postcss-import`:

`$ yarn add -D autoprefixer postcss-import`

You need these to add vendor prefixes to your styles and to be able to write syntax like `@import "tailwindcss/base"` to import Tailwind files directly from `node_modules`, respectively.

Now that we have it installed, let's make a new file inside our root directory and call it `postcss.config.js`. This is the configuration file for PostCSS and it will contain, for now, these lines:

```js
module.exports = {
  plugins: [
    require("postcss-import"),
    require("tailwindcss"),
    require("autoprefixer"),
  ],
};
```

*Order of plugins matters here!*

That's it! That's all you need to get started using TailwindCSS within your Chrome extension.

Create a file called `style.css` inside your `src` folder and include Tailwind files:

```css
@import "tailwindcss/base";
@import "tailwindcss/utilities";
```

### Remove unused CSS using PurgeCSS

Let's also make sure we only import the styles we use by enabling Tailwind's purging capability.

Create a new Tailwind configuration file by running: 

`$ npx tailwindcss init`: this will create a new `tailwind.config.js` file.

To remove unused CSS, we're going to add our source files to the purge field like this:

```js
module.exports = {
  purge: [
    './src/**/*.js', 👈
  ],
  theme: {},
  variants: {},
  plugins: [],
}
```

Now our CSS will be purged and unused styles will be removed when you build for production.

### How to enable Hot Reloading within your Chrome Extension

One more thing before adding some content to our extension: let's enable hot reloading.

Chrome doesn't reload the source files when you make new changes – you need to hit the "Reload" button on the extensions page. Fortunately, there's an NPM package that does hot reloading for us.

`$ yarn add crx-hotreload`

In order to use it, we'll create a new file called `background.js` inside our `src` folder and import `crx-hotreload`

```js
import "crx-hotreload";
```

Finally point to `background.js` in `manifest.json` so it can be served with our extension (hot reloading is disabled in production by default):

```json
{
  "name": "Demo extension",
  "description": "An extension built with Parcel and TailwindCSS.",
  "version": "1.0",
  "manifest_version": 2,
  "background": { 👈
    "scripts": ["background.js"]
  },
}
```

Enough with configuration. Let's build a small script form within our extension.

#### Types of scripts in a Chrome extension

As mentioned in the beginning of this post, in Chrome extensions there a few types of scripts you can use.

*Content scripts* are scripts that run in the context of the visited web page. You can run any JavaScript code that is otherwise available in any regular web page (including accessing/manipulating the DOM). 

A background script, on the other hand, is where you can react to browser events, and it has access to the Chrome extension APIs.

### Adding a content script

Create a new file called `content-script.js` under the `src` folder.

Let's add this HTML form to our newly created file:

```js
import cssText from "bundle-text:../dist/style.css";

const html =
`
<style>${cssText}</style>

<section id="popup" class="font-sans text-black z-50 w-full fixed top-0 right-0 shadow-xl new-event-form bg-white max-w-sm border-2 border-black p-5 rounded-lg border-b-6">
  <header class="flex mb-5 pl-1 items-center justify-between">
    <span class="text-2xl text-black font-extrabold">New event!</span>
  </header>
  <main class="event-name-input mb-6">
    <div class="mb-6">
      <label
        for="event-name"
        class="font-bold pl-1 block mb-1 text-black text-xl"
        >
      Event name
      </label>
      <div class="duration-400 flex bg-white border-black border-2 rounded-lg py-4 px-4 text-black text-xl focus-within:shadow-outline">
        <input
          id="event-name"
          name="event-name"
          type="text"
          placeholder="web.dev LIVE"
          class="font-medium w-full focus:outline-none"
          />
      </div>
    </div>
    </div>
    <div class="mb-6">
      <label
        for="event-date"
        class="font-bold pl-1 block mb-1 text-black text-xl"
        >
      Date
      </label>
      <div class="event-date-input duration-400 border-black flex bg-white border-2 rounded-lg py-4 px-4  text-xl focus-within:shadow-outline">
        <input
          id="event-date"
          name="event-date"
          type="date"
          class="font-medium w-full focus:outline-none"
          />
      </div>
    </div>
    <div class=" mb-8">
    <label
      for="event-time-input"
      class="font-bold pl-1 block mb-1  text-xl"
      >
    Time
    </label>
    <div class="inline-flex items-center">
      <input
        id="event-time-input"
        type="time"
        value="17:30"
        class="border-black mr-4 lowercase duration-400 w-auto bg-white text-xl border-2  rounded-lg px-4 py-4 focus:outline-none focus:shadow-outline"
        />
      <div class="inline-flex flex-col">
        <span class="text-xl font-bold">Casablanca</span>
        <span class="text-base font-normal">Africa</span>
      </div>
    </div>
  </main>
  <footer>
  <button 
    class="duration-400 bg-green-400 text-xl py-4 w-full rounded-lg border-2 border-b-6 leading-7 font-extrabold border-black focus:outline-none focus:shadow-outline"
    >
  Save
  </button>
  </footer
</section>
`

const shadowHost = document.createElement("div");
document.body.insertAdjacentElement("beforebegin", shadowHost);
const shadowRoot = shadowHost.attachShadow({ mode: 'open' });

shadowRoot.innerHTML = html
```

Styling a browser extension is not as straightforward as you may think because you need to make sure that the website styles are not affected by your own styles. 

In order to separate them, we are going to use something called the *Shadow DOM*. The Shadow DOM is a powerful encapsulation technique for styles. This means that styling is scoped to the Shadow tree. Therefore, nothing is leaked out to the visited web page. Also outside styles do not override the Shadow DOM's content, although CSS variables can still be accessible.

A *shadow host* is any DOM element we would like to attach our Shadow tree to. A *Shadow Root* is what is returned from `attachShadow` and its content is what gets rendered.

**Beware**, the only way to style the content of a Shadow tree is by inlining styles. Parcel V2 has a new built-in feature where you can import the content of one bundle, and use it as compiled text inside your JavaScript files. Then Parcel will replace it at the time of packaging.

We did exactly that with our `style.css` bundle. Now we can inline the CSS automatically to the Shadow DOM at build time.

Now we have to tell the browser about this new file, let's go ahead and include it by adding these lines to our manifest:

```json
{
  "name": "Demo extension",
  "description": "An extension built with Parcel and TailwindCSS.",
  "version": "1.0",
  "manifest_version": 2,
  "background": {
    "scripts": ["background.js"]
  },
  👇
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content-script.js"],
    }
  ]
}
```

In order to serve our extension, we are going to add a few scripts to our `package.json`:

```json
  "scripts": {
    "prebuild": "rm -rf dist .cache .parcel-cache",
    "build:tailwind": "tailwindcss build src/style.css -c ./tailwind.config.js -o dist/style.css",
    "watch": "NODE_ENV=development yarn build:tailwind && cp src/manifest.json dist/ && parcel watch --no-hmr src/{background.js,content-script.js}",
    "build": "NODE_ENV=production yarn build:tailwind && cp src/manifest.json dist/ && parcel build src/{background.js,content-script.js}",
  }
```

Finally you can run `yarn watch`, go to `chrome://extensions`, and make sure *Developer Mode* is enabled on the top right of the page. Click on "Load Unpacked" and select the `dist` folder under `demo-extension`.

- *If you get this error: `Error: Bundles must have unique filePaths` you can simply fix it by removing the `main` field in your `package.json`*

## How to publish your extension to the Google Chrome Web Store

Before going further into this, let's add a new NPM script that will help us compress the extension files as required by Chrome.

```json
  "scripts": {
    "prebuild": "rm -rf dist .cache",
    "build:tailwind": "tailwindcss build src/style.css -c ./tailwind.config.js -o dist/style.css",
    "watch": "NODE_ENV=development yarn build:tailwind && cp src/manifest.json dist/ && parcel watch --no-hmr src/{background.js,content-script.js}",
    "build": "NODE_ENV=production yarn build:tailwind && cp src/manifest.json dist/ && parcel build src/{background.js,content-script.js}",
    "zip": "zip -r chrome-extension.zip ./dist" 👈
  }
```

If you haven't installed `zip` yet, please do so:
- MacOS: `brew install zip`
- Linux: `sudo apt install zip`
- For Windows, you can use the powershell command `Compress-Archive` similarly: `powershell Compress-Archive -Path .\\dist\\ -Destination .\\chrome-extension.zip`

Now all you have to do is head to [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole/register) to set up your account and publish your extension ?


- *You can find the complete demo for this tutorial hosted on my GitHub account [here](https://github.com/mrassili/extension-demo)*

## Conclusion

In the end, Chrome extensions are not that different from web apps. Today you learned how to develop an extension using the latest technologies and practices in web development. 

Hopefully this tutorial helped you speed up your extension development a little bit!

If you found this helpful, please Tweet about it and follow me at [@marouanerassili](https://twitter.com/marouanerassili).

Thank you!



