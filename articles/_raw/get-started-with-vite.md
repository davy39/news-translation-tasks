---
title: Vite.js Tutorial – How to Install and Use Vite in Your Web Projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-26T21:41:58.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-vite
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/getting-started-with-vite.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Popoola Temitope

  Vite.js is a rapid development tool for modern web projects. It focuses on speed
  and performance by improving the development experience.

  Vite uses native browser ES imports to enable support for modern browsers without
  a build pr...'
---

By Popoola Temitope

[Vite.js](https://www.freecodecamp.org/news/p/e534a679-ce3c-4cf1-842b-96087d30944d/Vite.js) is a rapid development tool for modern web projects. It focuses on speed and performance by improving the development experience.

Vite uses native browser ES imports to enable support for modern browsers without a build process.

Vite consists of two major parts:

* The dev server provides support for Hot Module Replacement (HMR) for updating modules during the execution of the application. When changes are made to the source code of an application, only the changes are updated, rather than the entire application being reloaded. This feature helps speed up development time.
* The build command enables developers to bundle their code with Rollup, pre-configured to output highly optimized static assets for production.

## How Vite.js Works

When ES modules were introduced in ES2015, many browsers had poor support for ES6 modules. To address this, modern browsers now support native ES modules. This allows developers to use the `import` and `export` statements natively.

In native ES, the import must get either a relative or absolute URL because it does not support bare module imports such as:

```js
import { someMethod } from 'my-dep'
```

The above code will throw an error in the browser because many browsers do not have support for ES6 modules. So the question now is how does Vite handle this?

Vite will automatically detect bare module imports from your source files and perform the following two actions on them:

* Vite will pre-bundle the source files to speed up page loading and convert CommonJS / UMD modules to ESM.
* To allow browsers to import modules without throwing errors, Vite will rewrite the imports to a valid URLs like this

```
/node_modules/.vite/my-dep.js?v=f3sf2ebb
```

# Why Use Vite?

Now that we know what Vite is and how it works, you might be wondering why you should use Vite. 

There are many reasons why you should use Vite for your project. Let's take a brief look at some of them.

## Performance

Pre-bundling with Vite's ESbuild makes it 10 to 100 times faster than using any other JS bundler. This is because it helps improve page speed and convert CommonJS / UMD modules to ESM. 

According to the Vite documentation,

> "The pre-bundling step is performed with esbuild and makes Vite's cold start time significantly faster than any JavaScript-based bundler."

## Hot Module Replacement (HMR)

Vite uses HMR functionalities to keep track of changes in your application without reloading the full page. With the HMR API, the browser will only load the modified section of the page and still retain the application's state.

There's no need to manually configure the HMR API in your app. It's automatically  added to your project during application installation.

With HMR performance, you can design lighter and faster applications regardless of the number of modules or the size of your application.

## Configuration Options

Vite allows you to have more control over your project's configuration by extending the default configuration with `vite.config.js` or `vite.config.ts`. These are located in the project's base root directory.

You can also specify different config files with the `--config` CLI option, as shown below:

```bash
vite --config my-config.js
```

# What You'll Need

You must have the following software installed on your computer before you can create a Vite project:

* [Node.js version 12.2.0](https://nodejs.org/en/download/) or higher (to check if you have Node installed on your computer run **`node -v`** on the terminal)
* [Npm](https://www.npmjs.com/get-npm) / [Yarn](https://classic.yarnpkg.com/en/)

Once you have these installed on your computer, you can now create a Vite project.

# How to Create a Vite Project

To create a Vite application, open your terminal and navigate to the folder where you want to save the Vite program. Then run this command:

```bash
npm create @vitejs/app my-vite-app
```

**Note:** **`my_vite_app`** is the name of the Vite application that we want to create. You can change it to whatever name you prefer.

After running the above command, you'll be prompted to select a `framework` and the `template` (variant). For the purposes of this tutorial, we'll use React, but you can select any framework and template that you are familiar with.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/v-edit-1.jpg)

Next, run the following commands to finish the installation:

```bash
cd vite_application
npm install
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/v-edit-1.png)

The installation may take a few minutes, so just wait until it's completed.

# How to Run a Vite Application

To run your Vite application on the terminal, navigate to the application folder (`vite_application`) and then run the dev command below to start the development server:

```bash
npm run dev
```

Running the above command will start the development server. Then open your terminal and enter [`http://localhost:3000`](http://localhost:3000).

You should see something like this in the browser:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/vite-4.PNG)
_React application_

# Vite Folder Structure

Let's have a look at how Vite application folders are organized. We'll also look at a few of the folders and files in detail. 

Note: if you are using a different framework and template, the file name will not be the same.  


![Image](https://lh5.googleusercontent.com/Fgo6venfe73MifwcmqHXjOtatI5uix9yksTqNDoUpGXGQoyEiIozkcQ1sqrSOr1LQWBQuVWn3keKoY71aqFY91vjpOgFY2hpHV_7RfmuoV5hGerJqBzBLCfiA6FsjTmnMS-dcf-E)
_Vite folder structure_

### **node_modules folder**

The node_modules folder contains all the necessary dependencies for the application, which are specified in the package.json file. 

All of the configured dependencies in package.json will be downloaded into the node_modules folder once the `npm install` command is run.

When pushing your source code to GitHub, you don't need to push the node_modules folder because users can install all the necessary dependencies used in your application through the package.json.

You can find the package.json file in the application parent's root directory.

### **src folder**

The src folder is one of the folder that we interact with most when developing Vite applications. This folder contains app.jsx, main.jsx, app.css and index.js.

All of your application's assets, such as images, videos, and other files, must be stored in the src folder because Vite automatically rebases all URLs inside index.html.

### App.jsx and main.jsx

The app.jsx file is the base component that serves as a container for all of the other components used in the application. 

The main.jsx file is where you target the root id from the index.html and render all the components used in the application.

### index.css and app.css

These files contain all of the CSS styles used in the program. You can add your own CSS file or change the style.

# Conclusion

We've looked at what Vite is, how it works, and some of its features. We also learned how to create Vite applications.

In order to improve your development workflow and be more productive by creating lighter and faster applications you can learn more about [Vite in its docs](https://vitejs.dev/).

  

