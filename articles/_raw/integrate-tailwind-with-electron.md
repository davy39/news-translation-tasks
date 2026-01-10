---
title: How to Integrate Tailwind with Electron – With Code Examples
subtitle: ''
author: Abhijeet Dave
co_authors: []
series: null
date: '2025-08-13T17:22:22.821Z'
originalURL: https://freecodecamp.org/news/integrate-tailwind-with-electron
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755102784797/0a2d19f0-3539-47c6-a29d-68fab3d430ba.png
tags:
- name: Tailwind CSS
  slug: tailwind-css
- name: Electron
  slug: electron
seo_title: null
seo_desc: 'In this article, you’ll learn how to integrate Tailwind CSS with Electron
  to build stylish, responsive desktop applications.

  You’ll set up Tailwind in an Electron project, configure your project, style the
  components, and optimize the development wor...'
---

In this article, you’ll learn how to integrate Tailwind CSS with Electron to build stylish, responsive desktop applications.

You’ll set up Tailwind in an Electron project, configure your project, style the components, and optimize the development workflow. This is perfect for developers who are looking to combine Tailwind's utility-first CSS framework with Electron's cross-platform capabilities.

## Table of Content

* [A Quick Overview of Electron](#heading-a-quick-overview-of-electron)
    
* [What is Tailwind CSS?](#heading-what-is-tailwind-css)
    
* [Why Electron and Tailwind Work So Well Together](#heading-why-electron-and-tailwind-work-so-well-together)
    
* [What We’ll Build?](#heading-what-well-build)
    
* [Prerequisites](#heading-prerequisites)
    
* [How to Initialize an Electron Project](#heading-how-to-initialize-an-electron-project)
    
* [How to Integrate Tailwind CSS with Electron?](#heading-how-to-integrate-tailwind-css-with-electron)
    
* [How to Use a Tailwind Component Library – a Practical Example](#heading-how-to-use-a-tailwind-component-library-a-practical-example)
    
* [Let’s Test FlyonUI JS Components](#heading-lets-test-flyonui-js-components)
    
* [Conclusion](#heading-conclusion)
    

## A Quick Overview of Electron

[**Electron**](https://www.electronjs.org/) is a framework that lets developers create desktop applications for Windows, macOS, and Linux using familiar web technologies like HTML, CSS, and JavaScript, along with Node.js for backend features.

It's open-source, MIT-licensed, and completely free to use – whether you're building personal projects or commercial apps.

In this guide, we’ll look at why so many developers and companies choose Electron for building modern desktop apps.

## **What is Tailwind CSS?**

[**Tailwind CSS**](https://tailwindcss.com/) is essentially a utility-first framework for styling web interfaces. Unlike frameworks that provide full-blown, pre-designed UI components, Tailwind offers a comprehensive set of single-purpose utility classes. You apply these classes directly to your HTML elements, which means you can rapidly build out custom layouts and designs without diving into separate CSS files.

The big advantage? Precision and flexibility – you can assemble unique, responsive interfaces by combining these classes however you see fit, all while keeping you markup lean and maintainable.

## **Why Electron and Tailwind Work So Well Together**

Electron uses HTML, CSS, and JavaScript to build desktop applications. Essentially, it runs a web app in a desktop shell. This makes it easy to integrate modern frontend tools like Tailwind CSS.

Tailwind's utility-first approach allows you to style interfaces directly in you HTML, which can speed up UI development. Instead of writing custom styles or managing large CSS files, you apply predefined classes directly to elements. This aligns well with Electron's structure, where layout and styles are tightly connected within the same HTML environment.

Tailwind also provides sensible defaults and a consistent design system out of the box. This helps you prototype and build visually consistent desktop apps faster. While some familiarity with CSS is still helpful, Tailwind's approach can reduce the overhead of setting up and managing styles, especially in smaller or design-light projects.

Together, Electron and Tailwind offer a straightforward path to building desktop apps.

## What We’ll Build?

In this tutorial, we will create a basic Electron desktop app styled with Tailwind CSS and improved with FlyonUI components. You don’t need any prior experience with Electron or Tailwind.

By the end of the guide, you'll have:

* A working desktop window (Electron)
    
* Styled UI with Tailwind CSS
    
* A reusable button component
    
* A fully functional modal dialog powered by FlyonUI
    

This will provide a solid base for building more complex apps in the future.

## **Prerequisites**

Before we dive in, make sure you have the following:

* **Basic knowledge of HTML, CSS, and JavaScript**. You don’t need to be an expert, but understanding how to structure HTML and use basic JavaScript will help you follow along.
    
* **Familiarity with Node.js and npm**. We'll use npm (Node Package Manager) to install dependencies and run build commands.
    
* **Node.js installed on your machine**. You can download it from [nodejs.org](http://nodejs.org)[.](https://nodejs.org/)
    
* **A code editor**. I recommend [Visual Studio Code.](https://code.visualstudio.com/)
    
* **Terminal / Command Line Access**. You’ll need to run commands in the terminal to set things up.
    

## **How to Initialize an Electron Project**

Let’s set up a basic Electron app from scratch. This will launch a simple desktop window that loads an HTML file, serving as the foundation for your UI.

### 1\. **Create Your Project Folder**

First, open your terminal and create a new project folder:

```bash
mkdir my-electron-app
cd my-electron-app
```

This creates a new folder called `my-electron-app` and changes the directory to it. This folder will be your project workspace.

### 2\. **Install Electron**

Next, install Electron as a development dependency:

```bash
npm install electron --save-dev
```

This will add Electron to your project’s `node_modules` and update your `package.json` file.

This command installs Electron as a development dependency. Electron allows you to build desktop apps across different platforms using web technologies like HTML, CSS, and JavaScript.

### 3\. **Configure** `package.json`

Update your `package.json` to point to a file named `main.js`, and add a script for easily starting the app.

**Edit your** `package.json` like this:

```json
"main": "main.js",
"scripts": {
  "start": "electron ."
}
```

* `"main"` defines the entry point of your Electron app (the main process).
    
* `"start"` is a shortcut to launch the app using `npm start`.
    

### 4\. **Create** `main.js`

Create a file named `main.js` in your root folder and add the following code:

```javascript
const { app, BrowserWindow } = require("electron/main");

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
  });

  win.loadFile("index.html");
};

app.whenReady().then(() => {
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
```

This is your **main process**. It creates and manages the app window while loading your HTML file.

### 5\. **Create** `index.html` **(Renderer Process)**

```xml
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'" />
    <title>Hello from Electron renderer!</title>
  </head>
  <body>
    <h1>Hello from Electron renderer!</h1>
    <p></p>
    <p id="info"></p>
    <script src="./renderer.js"></script>
  </body>
</html>
```

This is the **frontend (renderer)** of your Electron app. You can use standard HTML, CSS, and JavaScript here, just like in a browser.

> Optional: Create a renderer.js file if you want to add JavaScript interactivity.

### 6\. **Run the Electron App**

Now, create a file called `main.js` in the root of your project. This is the main process that starts your Electron app:

```bash
npm start
```

This command runs the app using the script you set up in `package.json`. A desktop window should open, displaying your HTML content.

![hello form electron renderer](https://cdn.hashnode.com/res/hashnode/image/upload/v1754292319523/58168908-40ed-4aca-920f-fbab7435b580.webp align="center")

## **How to Integrate Tailwind CSS with Electron?**

For this guide, we’ll be using the [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli) approach.

The Tailwind CLI is a command-line tool that allows you to generate and compile Tailwind utility classes directly into a CSS file. You don’t need complex build tools like Webpack or PostCSS. This makes it perfect for simple projects like Electron apps, where you’d want minimal setup and quick styling. The CLI also has a `--watch` mode that automatically rebuilds CSS when files change. This feature helps you stay productive.

### 1\. **Install Tailwind CSS**

First, install Tailwind CSS. Make sure Node.js is installed as well, then run:

```bash
npm install tailwindcss @tailwindcss/cli
```

This command installs Tailwind and its CLI tool as a development dependency in your project. We’ll use the CLI to build and monitor our Tailwind styles.

### 2\. **Set Up Tailwind CSS**

Create a `input.css` file with the following content to set up Tailwind:

```css
@import "tailwindcss";
```

This line instructs Tailwind to generate all its utility classes into one output file, which we’ll compile next.

### 3\. **Add a Build Script**

Then update your `package.json` to include a build script:

```json
"scripts": {  
 "watch:css":"npx @tailwindcss/cli -i ./input.css -o ./output.css --watch",
}
```

This command watches your `input.css` file and continuously builds a compiled CSS file (`output.css`) whenever it detects changes. You’ll include this file in your HTML.

### 4\. **Link** `output.css` **in** `index.html`

Open your `index.html` file and add this inside the `<head>`

```html
<link href="./output.css" rel="stylesheet">
```

Then compile Tailwind CSS with this command:

```bash
npm run watch:css
```

This step includes the compiled Tailwind styles in your Electron app UI.

### 5\. **Compile Tailwind CSS**

Run this script to start watching for changes and generate your CSS:

```bash
npm run watch:css
```

Keep this process running in a terminal window. It updates `output.css` live as you work.

### 6\. **Update the UI with Tailwind Classes**

Replace your `<body>` content with this example layout:

```xml
<body class="flex items-center justify-center h-screen bg-gray-100">
  <button type="button"
    class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-purple-600 text-white hover:bg-purple-700 focus:outline-hidden cursor-pointer focus:bg-purple-700 disabled:opacity-50 disabled:pointer-events-none">
    Hello Tailwindcss
  </button>
</body>
```

### 7\. **Run the Electron App**

Run the electron server with this command:

```bash
npm start
```

Your Electron window should now open with a well-styled button in the center, thanks to Tailwind CSS.

![run electron server](https://cdn.hashnode.com/res/hashnode/image/upload/v1754374369750/f79a6c6d-bc59-4a2b-a6eb-f3b63f8bccc4.png align="center")

## How to Use a Tailwind Component Library – a Practical Example

We are going to use [FlyonUI](https://flyonui.com/), an open source Tailwind component library. It includes a mix of utility classes in addition to JavaScript plugins. FlyonUI draws ideas from daisyUI but also from Preline, and combines flexibility and simplicity. It also helps you build interfaces that respond well and appear consistent.

### 1\. **Install FlyonUI**

You can install FlyonUI with the command below. Make sure Node.js is installed, then run:

```bash
npm install -D flyonui@latest
```

Installs FlyonUI into your project as a development dependency, making its CSS and JS functionality available for integration.

### 2\. Add FlyonUI as plugin in the `input.css`:

```css
@import "tailwindcss";
@plugin "flyonui";
@import "./node_modules/flyonui/variants.css"; /* Needed for JS components */
@source "./node_modules/flyonui/dist/index.js"; /* Needed for JS components */
```

* `@plugin "flyonui"` injects FlyonUI’s semantic classes into your build.
    
* The `@import` includes custom variants created for the JS Components.
    
* The `@source` line is required for the classes used in the js gets generated.
    

### 3\. **Include FlyonUI JavaScript for Interactivity**

Right before closing the `</body>` tag in your HTML, include:

```html
<script src="../node_modules/flyonui/flyonui.js"></script>
```

This script enables the interactive behaviors for FlyonUI components, such as overlays, modals, and dropdowns.

### 4\. **Use a FlyonUI Component**

For example, update your UI with:

```xml
<body class="flex items-center justify-center h-screen bg-gray-100">
  <button type="button" class="btn btn-primary">
    Hello FlyonUI
  </button>
</body>

```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1754374843709/41f9d3e3-d0be-4a32-a569-ce0618bea0e9.png align="center")

* The `.btn` and `.btn-primary` classes come from FlyonUI—giving you styled, semantic components without crafting custom CSS.
    

### **Why It Matters**

* **Cleaner Code**: FlyonUI’s semantic classes make your templates more readable and maintainable compared to verbose utility classes.
    
* **Interactive Without the Overhead**: Easily add dynamic features like modals or accordions through FlyonUI’s JS plugins—no need to code them from scratch.
    
* **Effortless Styling**: FlyonUI builds on Tailwind’s utility approach, so you can customize components with familiar classes instantly.
    

## Let’s Test FlyonUI JS Components

To show how FlyonUI works, we’ll test one of its JavaScript-powered UI components, the **Modal**. Modals are common UI elements that grab user attention for alerts, confirmations, or extra information without moving away from the current page.

### Why Test the Modal?

Testing the modal helps you:

* Check that FlyonUI’s JavaScript components load and work properly within your Electron and Tailwind setup.
    
* See how simple it is to add interactive features using FlyonUI’s built-in classes and data attributes.
    
* Understand how the modal responds to different screen sizes and how the UI reacts to user actions like opening and closing dialogs.
    

### How to Test the Modal

Copy the following example code into your `index.html` file. This button will open a modal dialog with some placeholder content:

We’ll use this [**Modal example**](https://flyonui.com/docs/overlays/modal/) for testing. Copy the following code in your `index.html`:

```html
<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="basic-modal" data-overlay="#basic-modal">Open modal</button>

<div id="basic-modal" class="overlay modal overlay-open:opacity-100 hidden overlay-open:duration-300" role="dialog" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#basic-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#basic-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```

After updating the file, restart your Electron app:

```html
npm start
```

Here’s the result:

![final result](https://cdn.hashnode.com/res/hashnode/image/upload/v1754374899394/4f153f2b-ca41-495f-b27e-18a2424a1952.png align="center")

## **Conclusion**

You can use Tailwind CSS and Electron to build desktop applications that look good and operate well on different devices. This adds to Electron's many functions and Tailwind's good styling system, letting you stay productive and utilize clean design methods.

The full code and more details are in the repository here: [ts-electron-tailwindcss](https://github.com/themeselection/ts-electron-tailwind).

I have written this tutorial with the help of [Pruthvi Prajapati](https://github.com/PruthviPraj00), an experienced Tailwind CSS developer.
