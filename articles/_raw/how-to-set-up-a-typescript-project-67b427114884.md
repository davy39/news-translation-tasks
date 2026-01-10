---
title: How to set up a TypeScript project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T18:24:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-typescript-project-67b427114884
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wyxuq21keffc5b0d_lMkUw.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By David Piepgrass

  A thorough guide for beginners making web apps with React


  _Photo by [Unsplash](https://unsplash.com/photos/ZMraoOybTLQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Art...'
---

By David Piepgrass

#### A thorough guide for beginners making web apps with React

![Image](https://cdn-media-1.freecodecamp.org/images/1*wyxuq21keffc5b0d_lMkUw.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/ZMraoOybTLQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Artem Sapegin</a> on <a href="https://unsplash.com/search/photos/project?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

In all my years as a developer, I’ve never encountered a wilderness as overwhelming as The JavaScript World. It’s a world of bewildering complexity, where making a very simple project seems to require installing numerous tools, editing several text files that connect all those tools together, and running a bunch of terminal commands.

There are some tools that try to hide the complexity from you, with varying degrees of success. But as long as those tools don’t have universal adoption, they just seem to me like even more things you have to learn on top of everything else.

For me, the biggest source of irritation is that most tutorials assume you are **already** familiar with the ecosystem so they don’t bother to explain the basics. To make this worse, many tutorials try to push a bunch of extra tools on you — like [Webpack](https://webpack.js.org/), [Bower](https://bower.io/), [NVM](https://github.com/creationix/nvm), and [Redux](https://redux.js.org/) — with little explanation.

It’s ironic, because JavaScript itself is already installed on virtually every computer in the world, including phones. Why should writing an app the “professional” way have to be so complex compared to writing an HTML file with some JavaScript code in it?

If, like me, you have an **innate need** to understand what is going on and:

* if you can’t stand blindly copying commands into terminals and text files
* if you want to make sure you need a tool before you install it
* if you’re wondering why your npm-based project is 50MB before you’ve written your first line of code

then welcome! You’ve come to the right place.

On the other hand, if you wanted to start programming in 5 minutes flat, I know a trick for that: skip the introduction here and start reading about [Approach A](https://medium.com/p/67b427114884#682d) in Section 2. Or if you think I’m giving you too much information, just skip the parts you don’t want to learn about as you go along.

In this tutorial, I will assume you have **some** programming experience with HTML, CSS and JavaScript, but **no** experience with [TypeScript](https://www.typescriptlang.org/), [React](https://reactjs.org/), or [Node.js](https://nodejs.org/en/).

I’ll give you an overview of the JavaScript ecosystem as I understand it. I’ll explain why I think TypeScript and React (or [Preact](https://preactjs.com/)) are your best bet for making web apps. And I’ll help you start a project without unnecessary extras.

In section 2, we will discuss how and why to add extras to your project, **if** you decide you want them.

### Table of Contents

[Section 1: Overview of the JavaScript ecosystem](https://medium.com/p/67b427114884#51cb)

[Section 2: Actually Setting Up the Project](https://medium.com/p/67b427114884#7248)

* [Common Steps](https://medium.com/p/67b427114884#682d)
* [Approach A: The Easy Way](https://medium.com/p/67b427114884#719b)
* [Other approaches](https://medium.com/p/67b427114884#3e81)
* [Approach B: The Way of Fewest Tools](https://medium.com/p/67b427114884#9220)
* [Approach C: The Webpack Way](https://medium.com/p/67b427114884#9b91)
* [Summary](https://medium.com/p/67b427114884#0690)

### Section 1: Overview of the JavaScript ecosystem

For many programming languages, there’s a certain way of doing things that everybody knows about.

For example, if you want to make a C# app, you install [Visual Studio](https://visualstudio.microsoft.com/), create a Windows Forms project with a few mouse clicks, click the green “play” button to run your new program, and then start writing code for it. The package manager ([NuGet](https://www.nuget.org/)) is built-in and the debugger Just Works. Sure, it might take a few hours to install the IDE, and [WPF](https://docs.microsoft.com/en-us/dotnet/framework/wpf/getting-started/introduction-to-wpf-in-vs) is about as fun as banging your head against a brick wall, but at least **getting started** is easy. (Except if you’re not using Windows, then it’s totally different, but I digress.)

In JavaScript, on the other hand, there are so many competing libraries and tools for almost every aspect of the development process. This barrage of tools can become overwhelming before you write your first line of code! When you go Googling “how to write a web app”, every web site you visit seems to give different advice.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IP44ejhk2c78Nt_xUckWbw.png)
_Thanks [draw.io](https://draw.io" rel="noopener" target="_blank" title=") for the diagramming tool!_

The one thing most people seem to agree on is using the Node Package Manager ([NPM](https://www.npmjs.com/)) for downloading JavaScript libraries (both server-side and browser-only). But even here, some people are using [Yarn](https://yarnpkg.com/en/), which is npm-compatible, or possibly Bower.

NPM is bundled with Node.js, a web server you control entirely with JavaScript code. NPM is tightly integrated with Node. For example, the `npm start` command runs `node server.js` by default.

Even if you were planning to use a different web server (or to use **no** web server and just double-click an HTML file), everybody seems to assume you’ll have Node.js installed. So you may as well go ahead and [install node.js](https://nodejs.org/en/download/) which gives you `npm` as a side-effect.

Node.js isn’t just a web server — it can also run command-line apps written in JavaScript. In that sense, the TypeScript compiler is a Node.js app!

Beyond NPM you have several choices:

#### Which flavor of JavaScript do you want?

The official name of JavaScript is actually ECMAScript, and the most widely-deployed version is ECMAScript 6 or ES6 for short. Old browsers, notably Internet Explorer, support only ES5.

ES6 adds lots of useful and important new features such as modules, let, const, arrow functions (or lambda functions), classes, and destructuring assignment.

ES7 adds a few more features, most notably something called async/await.

If you don’t need to support old browsers and your code isn’t very large, running your code directly in the browser is an attractive option, because you don’t have to “compile” your JavaScript before opening it in the browser.

**But** there are many reasons to use a compile step:

* If you need to support old browsers, you’ll want a “transpiler” so you can use new features of JavaScript in old browsers. A transpiler is a compiler whose output code is a high-level language, in this case JavaScript. I would guess the most popular transpiler is [Babel](https://babeljs.io/), with [TypeScript](https://www.typescriptlang.org/) in second place.
* If you want to use the popular React framework (but without TypeScript), you’ll probably be writing “JSX” code — fragments of XML inside JavaScript code. JSX is not supported by browsers and so requires a preprocessor (typically Babel).
* If you want to “minify” your code so it uses less bandwidth (or is obfuscated), you’ll need a “minifier” preprocessor. [Popular minifiers](http://typescript-react-primer.loyc.net/minification.html) include UglifyJS, JSMin, and the Closure Compiler.
* If you want type checking or high-quality code completion (also known as IntelliSense), you’ll want to use TypeScript, a superset of JavaScript (meaning every JavaScript file is also a TypeScript file… ostensibly). TypeScript supports both ES7 features and JSX, and its output is ES5 or ES6 code. When TypeScript and JSX code are used together, the file extension must be `.tsx`. Some people are using a different language, similar in concept to TypeScript, called Flow.
* If you don’t like JavaScript, you could try a totally different language that transpiles to JavaScript, such as Elm, ClojureScript, or Dart.

Luckily it’s possible to automate compiling so that your code is recompiled whenever you save a file.

This tutorial uses TypeScript, a superset of JavaScript with a comprehensive type system. The benefits of TypeScript are that:

1. You get compiler error messages when you make type-related mistakes (instead of discovering mistakes indirectly when your program misbehaves). In IDEs such as Visual Studio Code your mistakes are underlined in red.
2. You can get refactoring features. For example, in Visual Studio Code, press `**F2**` to rename a function or variable across multiple files, without affecting other things that have the same name.
3. Types allow IDEs to provide code-completion popups, also known as IntelliSense, which makes programming much easier because you don’t have to memorize all the names and expected arguments of the functions you call:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hDqFqucAtKLhDzEpACzsFA.png)
_Visual Studio Code’s IntelliSense™_

**Tip**: To play with TypeScript without installing anything, [visit its playground](http://www.typescriptlang.org/play/).

#### Client versus server

Your can run code in a client (front-end browser), a server (Node.js back-end), or both. The client is not under your control. The user might use Firefox, Chrome, Safari, Opera, Edge, or in the worst case, Internet Explorer.

For security reasons, keep in mind that the user can modify a browser’s behavior using browser extensions or the `**F12**` developer tools. You can’t even be sure that your code is running in a real browser.

Developers used to rely on the [jQuery](https://jquery.com/) library to get consistent behavior in different browsers, but these days you can rely on different browsers to behave the same way in **most** cases (except perhaps Internet Explorer).

In this tutorial, we’ll run all the important code in the browser, but we’ll also set up a simple Node.js server to serve the app to the browser. Many other servers are available, such as [Apache](https://httpd.apache.org/), [IIS](https://www.iis.net/), or a static server like [Jekyll](https://jekyllrb.com/).

But Node.js has become a sort of standard, likely because Node.js and NPM are bundled together.

#### User Interface frameworks

HTML and CSS alone are great for plain-old articles with images, or simple forms. If that’s all you’re doing, there’s probably no need for JavaScript at all. CSS can even do some things that once required JavaScript, such as [pull-down menus](https://www.cssscript.com/pure-css-mobile-compatible-responsive-dropdown-menu/), pages that [completely reformat themselves for small/mobile browsers or printing](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries), and [animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations).

If you need something more complex than that, or if your pages are generated dynamically from raw data, you’ll probably want to use JavaScript with an optional user-interface library or framework. I’ll show you [later](http://typescript-react-primer.loyc.net/tutorial-5.html) how to use React, which has earned a position as the most popular UI framework, and its little cousin Preact.

The “large” [popular alternatives](https://stateofjs.com/2017/front-end/results) include [Angular 2](https://angular.io/) and [Vue.js](https://vuejs.org/), while the “small” ones include [D3](https://d3js.org/), [Mithril](https://mithril.js.org/) and an old classic called jQuery.

If your web server runs JavaScript (Node.js), you can run React on the server to pre-generate the initial appearance of the page.

#### Build tools

Several [tools for “building” and “packaging” your code](https://stateofjs.com/2017/build-tools/results) are available — Webpack, [Grunt](https://gruntjs.com/), [Browserify](http://browserify.org/), [Gulp](https://gulpjs.com/), [Parcel](https://parceljs.org/) — but all these things are optional. I’ll show you how make do with just `npm` and, if you want, Parcel or Webpack.

#### CSS Flavors

In this article we’ll use plain CSS. If you’re going to have a compile step anyway, you might want to try SCSS, an “improved” derivative of CSS with extra features. Or you could use SASS, which is conceptually identical to SCSS but has a more concise syntax.

Either way you’ll need the [Sass preprocessor](https://sass-lang.com/). And as always in the JavaScript World, there are [a bunch of alternatives](https://stateofjs.com/2017/css/results/), notably [LESS](http://lesscss.org/).

#### Unit testing

The popular unit testing libraries are [Mocha](https://mochajs.org/), [Jasmine](https://jasmine.github.io/) and [Jest](https://jestjs.io/). [See here for more](https://stateofjs.com/2017/testing/results). NPM has a special command for testing, `npm test` (which is short for `npm run test`).

#### Other libraries

Besides Redux, [other](https://stateofjs.com/2017/other-tools/) popular JavaScript libraries include [Lodash](https://lodash.com/), [Ramda](https://ramdajs.com/), [Underscore](https://underscorejs.org/), and [GraphQL](https://graphql.org/).

The most popular linting utility is [ESLint](https://eslint.org/).

[Bootstrap](https://getbootstrap.com/) is a popular CSS library but it requires a JavaScript part (and it’s really SASS, not CSS).

When you see `$` in JavaScript code, it typically refers to jQuery. When you see `_` it typically refers to either Lodash or Underscore.

And perhaps it’s worth mentioning popular templating libraries: [Jade](http://jade-lang.com), [Pug](https://pugjs.org/), [Mustache](https://mustache.github.io/) and [Handlebars](https://handlebarsjs.com/).

#### Non-web apps

I won’t say anything more about this, but TypeScript and JavaScript can be used outside the web.

With [Electron](https://electronjs.org/) you can write cross-platform desktop apps. With [React Native](https://electronjs.org/) you can write JavaScript apps for Android/iOS devices that have a “native” user interface. You can also write [command-line apps with Node.js](https://scotch.io/tutorials/build-an-interactive-command-line-application-with-nodejs).

#### Module types

For the longest time, all JavaScript code ran in a single global namespace. This caused conflicts between unrelated code libraries, so various kinds of “module definitions” were invented to **simulate** what other languages call packages or modules.

Node.js uses [CommonJS](https://en.wikipedia.org/wiki/CommonJS) modules, which involves a magic function called `require('module-name')` to import modules and a magic variable called `module.exports` to create modules. To write modules that work in both browsers and Node.js, one can use Universal Module Definition ([UMD](https://github.com/umdjs/umd) modules). Modules that can be asynchronously loaded use [AMD](https://github.com/amdjs/amdjs-api/wiki/AMD).

ES6 introduced a module system involving `import` and `export` keywords, but Node.js and some browsers still don’t support it. Here’s a [primer on the various module types](https://www.jvandemo.com/a-10-minute-primer-to-javascript-modules-module-formats-module-loaders-and-module-bundlers/).

#### Polyfills & Prototypes

As an experienced developer, I can think of only two words (other than the names of libraries and tools) that are used only in JavaScript Land: **polyfill** and **prototype**.

Polyfills are backward-compatibility helpers. They are pieces of code written in JavaScript that allow you to use new features in old browsers. For example, the expression `"food".startsWith('F')` tests whether the String `'food'` starts with F (for the record, that’s `false` - it starts with `f`, not `F`.) But `startsWith` is a new feature of JavaScript that is not available in older browsers.

You can “polyfill it” with this code:

```
String.prototype.startsWith = String.prototype.startsWith ||  function(search, pos) {    return search ===       this.substr(!pos || pos < 0 ? 0 : +pos, search.length);  };
```

This code has the form `X = X || function(...) {...}`, which means “if X is defined, set X to itself (don’t change it), otherwise set X to be this function.” The function shown here behaves the way `startsWith` is supposed to.

This code refers to one of the other unique things about JavaScript, the idea of prototypes. Prototypes correspond **roughly** to classes in other languages, so what this code is doing is actually changing the definition of the built-in `String` data type. Afterward when you write `'string'.startsWith()` it will call this polyfill (if `String.prototype.startsWith` was not already defined). There are various articles out there to teach you about prototypes and prototypical inheritance, like [this one](https://hackernoon.com/understanding-javascript-prototype-and-inheritance-d55a9a23bde2).

Even some advanced browser features have polyfills. Have you heard of [WebAssembly](https://webassembly.org/), which lets you run C and C++ code in a browser? There’s a [JavaScript polyfill](https://github.com/lukewagner/polyfill-prototype-1) for it!

#### Credit

I’d like to thank the [State of Javascript](https://stateofjs.com/) survey and [State of JavaScript frameworks](https://www.npmjs.com/npm/the-state-of-javascript-frameworks-2017-part-2-the-react-ecosystem) for much of the information above! For a few items I used [npm-stat](https://npm-stat.com/) to measure popularity. See also this [other new survey](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results).

### Section 2: Actually Setting Up the Project

Hey there! Still awake? Now we will go on a tour of the JavaScript tools ecosystem. This part is not about React (we’ll get to that [later](http://typescript-react-primer.loyc.net/tutorial-5.html)) but it includes a simple React component.

This is somewhat of a **grand** tour, so we’ll talk about writing your app in three different ways (with a [summary](http://typescript-react-primer.loyc.net/tutorial-3.html) afterward):

* A. The Easiest Way (with Parcel)
* B. The Way of Fewest Tools (or the do-it-yourself way)
* C. The Webpack way

The first six steps are the same in all three approaches, so let’s get started!

#### Step 1: Install Node.js/npm

If you haven’t yet, go [install Node.js](https://nodejs.org/en/download/) which will also install the command-line package manager, `npm`.

If you want to deploy your app on some other web server, I recommend worrying about how to do that later.

#### Step 2: Install Visual Studio Code or other editor

One of the main reasons to use TypeScript instead of JavaScript is that it supports code completion features.

To enjoy this benefit, you’ll need to edit your TypeScript `.ts` files in a compatible editor such as [Visual Studio Code](https://code.visualstudio.com/download) — which is free and multi-platform. It’s also the most popular text editor for JavaScript apps. Alternatives include [Atom](https://atom.io/) and [Sublime Text](https://www.sublimetext.com/).

Visual Studio Code (VS Code) is folder-oriented: you open a folder in VS Code and that folder will be treated like the current “project”. During installation (on Windows, anyway) it will offer a checkbox to add an “Open with Code” action for folders (directories). I recommend using that option as an easy way to start VS Code from any folder:

![Image](https://cdn-media-1.freecodecamp.org/images/0*g75_7UBpUFqxHqwo.png)

Create an empty folder for your app, then open that folder in VS Code. Notice that VS Code has a built-in terminal so you won’t need a separate terminal window.

#### Step 3: Set up package.json

The `package.json` file will represent your project configuration. This includes its name, build commands, the list of npm modules used by your project, and more.

If you haven’t done so yet, create an empty folder for your app and open a terminal window in that folder.

In the terminal, run `npm init`.

`npm init` will ask you some questions in order to produce `package.json`. Leave a field blank to accept the default suggestion.

I wanted to make a small educational app to draw some graphs demonstrating how climate science explains the 20th century temperature record.

So I called my app `climate-app`:

```
C:\Dev\climate-app>npm initThis utility will walk you through creating a package.json file.It only covers the most common items, and tries to guess sensible defaults.[....]
```

```
package name: (climate-app)version: (1.0.0)description: Demo to visualize climate dataentry point: (index.js) test command:git repository:keywords:author: David Piepgrasslicense: (ISC) MIT
```

```
About to write to C:\Dev\climate-app\package.json:{  "name": "climate-app",  "version": "1.0.0",  "description": "Demo to visualize climate data",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "author": "David Piepgrass",  "license": "MIT"}
```

```
Is this ok? (yes)
```

Notice the reference to `index.js`. Oddly, this file does not need to exist and we won’t be using it. It is used only [if you share your code via npm](https://stackoverflow.com/a/27971810/22820).

#### Step 4: Install Typescript

VS Code [reportedly](https://code.visualstudio.com/docs/languages/typescript) has TypeScript “language support” rather than a TypeScript **compiler**, so now we need to install the compiler.

There are two ways to install TypeScript with npm. Either use

```
npm install --global typescript
```

or

```
npm install --save-dev typescript
```

If you use the `--global` option, then the TypeScript compiler `tsc` will be available in all projects on the same machine. It will also be available as a terminal command, but it will not be added to your `package.json` file. Therefore, if you share your code with others, TypeScript will **not** be installed when another person gets your code and runs `npm install`.

If you use `--save-dev`, TypeScript will be added to `package.json` and installed in your project’s `node_modules` folder (current size: 34.2 MB), but it will **not** be available directly as a terminal command.

You can still run it from the terminal as `./node_modules/.bin/tsc`, and you can still use `tsc` inside the `npm` `"scripts"` section of `package.json`.

**Fun fact**: the TypeScript compiler is multiplatform because it is written in TypeScript — and compiled to JavaScript.

#### Step 5: Install React or Preact

To add React to your project:

```
npm install react react-domnpm install --save-dev @types/react @types/react-dom
```

**Note:** `--save-dev` marks things as “used for development” while `--save` (which is the default, and therefore optional) means “used by the program when it is deployed”.

`@types` packages provide type information to TypeScript, but they are not used when your code is running/deployed.

If you forget `--save-dev` or if you use it on the wrong package, **your project will still work**. The distinction is only important if you share your project as an npm package.

Alternately you can use Preact, which is [almost the same](https://preactjs.com/guide/differences-to-react) as React but more than 10 times smaller. Preact has TypeScript type definitions built-in, so you only need a single command to install it:

```
npm install preact
```

**Tip:** `npm i` is a shortcut for `npm install`, and `-D` is a short for `--save-dev`.

**Note:** do not to install `preact` and `@types/react` in the same project, or `tsc` will go insane and give you about 150 errors (see [preact issue #639](https://github.com/developit/preact/issues/639)). If this happens, uninstall the React types with `npm uninstall @types/react @types/react-dom`

#### Step 6: Write some React code

Make a file called `app.tsx` with this small React program:

**Note:** in order for the embedded JSX (HTML/XML) to work, the file extension must be `tsx`, not `ts`.

If you have any trouble making your code work, try this code instead — it’s the simplest possible React program:

```
import * as ReactDOM from 'react-dom';import * as React from 'react';
```

```
ReactDOM.render(React.createElement("h2", null, "Hello, world!"),                document.body);
```

We’ll discuss how the code works later. For now, let’s focus on making it run.

If you’re using Preact, change the first two lines like so:

```
import * as React from 'preact';import * as ReactDOM from 'preact';
```

Some notes about Preact:

* There is a [preact-compat library](https://github.com/developit/preact-compat) which allows you to use preact with zero changes to your React code. Usage instructions exist for users of Webpack/Browserify/Babel/Brunch, and [this page](https://github.com/parcel-bundler/parcel/pull/850) shows how to use preact-compat with Parcel.
* There are rumors that in Preact you should write `/** @jsx h */` at the top of the file, which tells TypeScript to call `h()` instead of the default `React.createElement`. In this case you **must not** do that or you’ll get a error in your browser that `h` is not defined (`React.h`, however, is defined). In fact Preact defines `createElement` as an alias for `h`, and since our `import` statement assigns `'preact'` to `React`, `React.createElement` exists and works just fine.

#### Optional: running TypeScript scripts

This tutorial is focused on making **web pages** that run TypeScript code. If you would like to run a TypeScript file directly from the command prompt, the easiest way is to use `ts-node`:

```
npm install --global ts-node
```

After installing `ts-node`, run `ts-node X.ts` where `X.ts` is the name of a script you want to run. In the script you can call `console.log("Hello")` to write text to the terminal (reading text from a user is [more complicated](https://nodejs.org/api/readline.html#apicontent)). On Linux systems you can put a “shebang” at the top of the script if you would like to be able to run `./X.ts` directly (without mentioning `ts-node`):

```
#!/usr/bin/env ts-node
```

**Note:** if you don’t need to run `.ts` files from a terminal then you don’t need to install `ts-node`.

### Running your project, Approach A: The Easy Way

I discovered Parcel when I was mostly done writing this article. Honestly, if I knew about Parcel from the beginning I might not have bothered writing about the other approaches. Don’t get me started on how easy Parcel is! It deserves a medal!

It’s very large, though (81.9 MB), so you should install it as a global:

```
npm install --global parcel-bundler
```

The truth is I’ve been lying to you. Parcel is **so** easy, you don’t even need all six steps above! You only really need Steps 1, 2 and 6 (install Node, install an editor, and write some code) because Parcel will do steps 3, 4, and 5 for you automatically.

So all we have to do now is to create an `index.html` file that refers to our `app.tsx` file, like this:

Then, simply open a terminal in the same folder and run the command `parcel index.html`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xgfsNFJwzrxfbxEL.png)

This can’t run directly in a browser, of course, so Parcel:

1. Automatically compiles `app.tsx`
2. Installs React or Preact if it wasn’t already installed, because it notices that you’re using it
3. Bundles your app with its dependencies into a single file called `app.dd451710.js` (or some other funny name)
4. Creates a modified `index.html` that refers to the compiled and bundled app
5. Puts these new files in a folder called `dist`.

And then it does everything else for you:

1. It runs your app on a mini web server at `http://127.0.0.1:1234` — viewable on a web browser on the same machine
2. It watches for changes to your code (`app.tsx` and `index.html`) and recompiles when you change them
3. As if that wasn’t enough, when your files change, it will send a command to your web browser to **automatically refresh!**
4. Even better, it updates the page without fully reloading it using its [Hot Module Replacement](https://parceljs.org/hmr.html) feature

It can be challenging to set up a conventional build that does all of these things. This tutorial only covers how to do #1 and #2 in a conventional build, with only code recompilation (not HTML).

To learn about more features of Parcel, have a look at the [Parcel documentation](https://parceljs.org/getting_started.html).

One limitation of Parcel is that it doesn’t perform type checking (your code is translated to JavaScript, but type errors are not detected).

For small projects, this is not a big problem because Visual Studio Code performs its own type checking. It gives you red squiggly underlines to indicate errors and all errors are listed in the “Problems” pane (press `**Ctrl**`+`**Shift**`+`**M**` to show it). But if you want, you can `npm install parcel-plugin-typescript` for [enhanced TypeScript support](https://www.npmjs.com/package/parcel-plugin-typescript#features) including type checking ([not currently working for me](https://github.com/fathyb/parcel-plugin-typescript/issues/43)).

### Other approaches

The other approaches are more well-known and are standard practice in the JavaScript community. We will be creating a folder with the following files inside:

* `**app/**index.html`
* `**app/**app.tsx`
* `package.json`
* `tsconfig.json`
* `server.js`
* `webpack.config.js` (optional)

As a matter of communicating to other people who look at your code later, it is useful to separate your program’s **front-end code** from its **build configuration** and **app server**.

The root folder of a project tends to become cluttered with extra files over time (such as `.gitignore` if you use git, `README` and `LICENSE` files, `appveyor`/`travis` files if you use [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration).) Therefore, we should separate the code of our front-end into a different folder.

In addition to the files **we** create, TypeScript will compile `app.tsx` into `app.js` and `app.js.map`, while `npm` creates a folder called `node_modules` and a file called `package-lock.json` . I can’t imagine why it’s called “lock”, but [this page explains why it exists](https://medium.com/@Quigley_Ja/everything-you-wanted-to-know-about-package-lock-json-b81911aa8ab8).

So please begin by creating an `app` folder and putting your `app.tsx` there.

### Running your project, Approach B: The Way of Fewest Tools

It seems like everybody’s JavaScript project uses a dozen tools plus the kitchen sink. Is it possible to make a small program without any extra tools? It certainly is! Here’s how.

#### Step B1: Create tsconfig.json

Create a text file called `tsconfig.json` in your root folder, and put this code in it:

This file marks the folder as a TypeScript project and enables build commands in VSCode with `**Ctrl**`+`**Shift**`+`**B**` (the `tsc: watch` command is useful — it will automatically recompile your code whenever you save it.)

**Silly fact**: `tsc` allows comments in `.json` files but `npm` does not.

This file is very important because if the settings aren’t right, something may go wrong and mysterious errors may punch you in the face. Here is the [documentation of tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html), but compiler options are [documented separately](https://www.typescriptlang.org/docs/handbook/compiler-options.html).).

#### Step B2: Add a build script

To allow `npm` to build your TypeScript code, you must also add entries in the `scripts` part of `package.json`. Modify that section so it looks like this:

```
"scripts": {  "test": "echo \"Error: no tests installed\" && exit 1",  "build": "tsc",  "start": "node server.js"},
```

The `build` script simply runs `tsc` which compiles your code according to the options in `tsconfig.json.` To invoke this script you write `npm run build` on the command line.

“But wait!” you may be thinking. “It’s really much easier to type `tsc` than `npm run build`!” That’s true, but there are two reasons to define a `build` script:

1. If you installed TypeScript with `--save-dev` but not `--global`, you can’t run `tsc` directly from the command line because it’s not in the `PATH`.
2. There’s a good chance your build process will become more complicated later. By creating a build script you can easily add other commands to the build process later.

**Note:** `npm` runs the `prestart` script automatically whenever someone runs the `start` script, so you **could** add this additional an additional script:

```
"prestart": "npm run build",
```

This would build your project whenever you start your server with `npm start` or `npm run start`.

But this has two disadvantages:

1. `tsc` is a bit slow
2. if `tsc` finds type errors then your server won’t start

When TypeScript detects type errors, that doesn’t stop it from writing JavaScript output files, and you may find it is occasionally useful to run your code even with type errors.

The default behavior of `npm start` is to run `node server.js`, so it seems redundant to include `"start": "node server.js"`. However, if your server is written in TypeScript you’ll need this line because `server.js` doesn’t exist until `server.ts` is compiled. And if `server.js` doesn’t exist, `npm start` will give the error `missing script: start` unless you include this line.

#### Step B3: Make a simple server

To make sure Node.js is working, create a text file called `server.js` and put this code in it:

```
const http = require('http');
```

```
http.createServer(function (request, response) {  // Send HTTP headers and body with status 200 (meaning success)  response.writeHead(200, {'Content-Type': 'text/html'});  response.end(`    <html><body>      <h1>Hello, world!</h1>      You asked for: ${request.url}    </body&gt;</html>`);}).listen(1234);
```

Run `npm start` to start it, visit `http://127.0.0.1:1234/index.html` to make sure it works, then press `**Ctrl**`+`**C**` to stop the server.

To get IntelliSense for Node.js, you need to install type information for it with this command:

```
npm install @types/node --save-dev
```

Then in VS Code, type `http.` to make sure it works:

![Image](https://cdn-media-1.freecodecamp.org/images/0*TmTm83d-pJmb6iM5.png)

Behind the scenes, VS Code uses the TypeScript engine for this. However, if you rename your file to `server.ts`, **IntelliSense doesn’t work**! Is TypeScript broken in Node.js? Not really. TypeScript can still compile it, it just doesn’t grok `require` in a `.ts` context. So in TypeScript files, you should use `import` instead of `require`:

```
import * as http from 'http';
```

**Note**: this is confusingly different from Node’s `.mjs` files, which require `import http from 'http';` ([Details](https://stackoverflow.com/questions/50661510/why-doesnt-fs-work-when-imported-as-an-es6-module))

TypeScript then converts `import` to `require` in its output (because of the `"module": "umd"` option in `tsconfig.json`).

Now let’s change our server so it can serve any file from our `/app` folder:

You’ll notice that this code has some funny… nesting. That’s because Node.js functions are normally asynchronous. When you call functions in `fs`, instead of **returning** a result, they pause your program until they are done and then they **call** a function provided by you, sending that function either an error (`err`) or some information (`fileInfo`).

For example, instead of **returning** information about a file, `fs.stat` **sends** information to a callback.

A fishy thing about this web server is that it ignores `[request.method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)`, treating every request as if it were a `GET`. But it works well enough to get started.

#### Step B4 (optional): Use Express

If you want your server side to do any “routing” that is more complicated than serving a few files, you should probably learn about the most popular Node.js server framework: [Express](https://expressjs.com/).

If we use Express, our server code will be much shorter.

Just install it with `npm install express` and put the following code in `server.js`:

```
const express = require('express');const app = express();
```

```
app.use('/node_modules', express.static('node_modules'));app.use('/', express.static('app'));app.listen(1234, () => console.log(    'Express server running at http://127.0.0.1:1234'));
```

#### Step B5: Make a web page to hold your app

Finally, in your `app` folder, create an `index.html` file in there to load your app:

This page includes both React (`react.development.js` and `react-dom.development.js`) and Preact (`preact.dev.js`) so I don’t need to give you separate instructions for each one. You can remove whichever one you aren’t using, but the page can still load with unresolved script elements.

At this point you should be able to build your code (`npm run build`), start your server (`npm start`) and visit `http://127.0.0.1:1234` to view your app!

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZUymOkFeZhtmNjYF.png)

Remember, you can recompile your code automatically in VS Code: press `**Ctrl**`+`**Shift**`+`**B**` and choose `tsc: watch`.

**Note**: It’s important to load `app.js` at the end of the `body`, or React will say `Error: Target container is not a DOM element` because `app.js` would be calling `document.getElementById('app')` before the app element exists.

At this point it’s worth noting that this code is a little hacky. Especially this part:

```
<script>    module = {exports:{}}; exports = {};    window.require = function(name) { return window[name]; };    window['react'] = window['React'];    window['react-dom'] = window['ReactDOM'];<;/script>
```

What’s this for? The short answer is that if your code contains `import`, TypeScript **cannot** produce code that “just works” in a browser, and this is one of many possible workarounds for that problem.

The long answer? First of all, remember that the JavaScript ecosystem has multiple module systems. Right now, your `tsconfig.json` file uses the `"module": "umd"` option, because `"module": "umd"` and `"module": "commonjs"` are the only modes that can be used in both Node.js and a web browser.

I asked you to make a `server.js` (not `server.ts`) file, but by using `"module": "umd"` you could write your server code in TypeScript if you want to.

UMD is the natural choice since it’s supposed to make a “universal” module definition, but TypeScript doesn’t really try to be universal — it simply won’t attempt to work in a web browser unaided.

Instead, it expects to find predefined symbols either for an AMD module system or a CommonJS (or Node.js) module system. If neither of these is defined, the module exits without even logging an error message.

Even if we **could** use the `"module": "es6"` option, which keeps `import` commands unchanged in the output file, it wouldn’t work because Chrome somehow **still** doesn’t support `import` in 2018. Also, the URLs of our modules have little in common with the string in our `import` statements, and I have learned that TypeScript [path mapping aliases](https://www.typescriptlang.org/docs/handbook/module-resolution.html#base-url) can’t solve the problem because they don’t change the compiler’s output.

TypeScript’s CommonJS implementation requires the `require` to be defined, of course — it’s used to import modules. But it also looks for `exports` and `module.exports`, even though our module doesn’t export anything. So our little hack must define all three.

The UMD versions of React, ReactDOM, and Preact set global variables called `React`, `ReactDOM` and `preact` respectively. But “global” variables in a browser are actually members of a special object called `window`. And in JavaScript, `window.something` means exactly the same thing as `window['something']` except that you can use special characters, such as dashes, in the latter form. Therefore, `window['preact']` and/or `window['React']` already exist. So by defining a `require` function that simply returns `window[name]`, it allows React or Preact to be imported.

However, we also need to create lowercase aliases `'react'` and `'react-dom'` because those are the names we must use in our TypeScript code (those names are recognized by the TypeScript compiler because those are the names of the folders in `node_modules`).

There’s another thing in our index.html that is a bit… unfortunate:

```
<script src="node_modules/react/umd/react.development.js"></script><script src="node_modules/react-dom/umd/react-dom.development.js"></script><script src="node_modules/preact/dist/preact.dev.js"></script>
```

What makes this code less than ideal?

1. We already have `import` statements in our `app.tsx` file, so it’s unfortunate that we need a **separate** command to load the modules in our `index.html`.
2. We’re specifically referring to the **development** versions of the code, which include comments and are a lot more readable than minified versions. But if we roll out our web site to a large audience we’ll want to switch to the minified versions so that pages load faster. It would be nice if we could do that without losing the debugging benefits of the development versions.
3. It assumes we can access files in `node_modules`, which is an unusual way to set up a server.

All the disadvantages described here lead us to want some kind of additional tool to help us deploy code to our web browser. We discussed Parcel already, but the most popular one is Webpack.

### Running your project, Approach C: The Webpack Way

The most popular thing to do with front-end apps is to “pack” all the modules (React + your code + anything else you need) into a single file. This is comparable to what they call “linking” in some other languages, such as C++. That’s basically what Parcel and Webpack are built to do (Gulp is not — it requires extra tools installed separately.)

#### Steps C1 & C2: Create tsconfig.json and server.js

If you skipped approach B, please do steps B1 and B4 now.

#### Step C3: Install webpack

You **could** install it like this:

```
npm install --save-dev webpack webpack-cli
```

Unfortunately, Webpack is over-sized: these two packages have 735 dependencies weighing in at 50.9 MB (13,198 files in 1868 folders). And for some reason, `webpack-cli` requires the Webpack package but doesn’t mark it as a dependency, hence you must install both of them explicitly.

And although `webpack-cli` is ostensibly “just” the command-line interface for Webpack’s APIs, it is disproportionately large for some reason (Webpack alone is only 13.6 MB).

Due to its size, it probably makes more sense to install it as a global:

```
npm install --global webpack webpack-cli 
```

When using `--global`, keep in mind that if you share your code with someone else, the other person won’t get Webpack automatically when they type `npm install`, so you’ll want to explain how to install in your `README` file.

If you change your mind and want to switch from `--save-dev` to `--global`, just run the `--global` installation command and then use `npm uninstall webpack webpack-cli` to delete the local copy.

#### Step C4: Add build scripts

To allow `npm` to build and serve your project, add entries in the `"scripts"` section of `package.json`.

You **could** modify that section so it looks like this:

```
"scripts": {  "test": "echo \"Error: no tests installed\" && exit 1",  "build": "tsc && webpack app/app.js -o app/app.bundle.js --mode=production",  "build:dev": "tsc && webpack app/app.js -o app/app.bundle.js --mode=development",  "start": "node server.js"},
```

With these scripts, you would use either `npm run build` to build a minified production version, or `npm run build:dev` to build a development version with full symbols and comments. However, this is inconvenient, because when you change your code, you have to manually repeat the `npm run build:dev` command.

In Approach B we could use `tsc: watch` in VS Code, but that won’t work this time because we **also** need to run Webpack — and `tsc` doesn’t know that.

Can we set it up to rebuild automatically when our code changes? Yes, but we will need a Webpack plugin to accomplish this. One of the plugins that can do the job is called `awesome-typescript-loader`. Install it like this:

```
npm install awesome-typescript-loader --save-dev
```

Then in `package.json`, change your `"scripts"` section to look lke this:

This makes `webpack` fully responsible for building our TypeScript code, and therefore we can use its `--watch` option to watch for code changes. The command to build and watch for code changes is `npm run watch`.

#### Step C5: Start server and Webpack

You’ll need two separate terminals, one for your build system (`npm run watch`) and one for your server (`npm start`). If your server is written in TypeScript, then you need to run `npm run watch` first, otherwise it doesn’t matter which one you start first.

It’s worth noting that VS Code can keep track of multiple terminals. You can create two terminals and run one command in each, like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*VRyly_6gxW6aIN8M.png)

#### Step C6: Create index.html and load it

In Approach C, your `index.html` file is much simpler than in Approach B:

```
<!DOCTYPE html><html><head>  <title>App</title>  <meta charset="utf-8"/></head><body>  <h1>Mini React app ❤</h1>  <div id="app"></div>  <script src="app.bundle.js"></script></body></html>
```

Visit `**http://127.0.0.1:1234**` and the page should load. You’re done!

#### Step C7: Create a webpack.config.js file (optional)

Our build command is getting rather long, and is very similar for our three modes. Also, we’ve only set up the `tsx` file extension so `webpack` doesn’t know how to compile `ts` files yet.

The most popular way of using Webpack is with a special configuration file, separate from `package.json`. The `"build"` script above becomes the following `webpack.config.js` file:

```
module.exports = {  entry: __dirname+'/app/app.tsx',  output: {    path: __dirname+'/app',    filename: 'app.bundle.js'  },  module: {    rules: [      { test: /\.(ts|tsx)$/, loader: 'awesome-typescript-loader' }    ]  }};
```

After you create this file, change your `scripts` in `package.json` as follows:

As before you can build and watch for changes with `npm run watch`, or use `npm run build` for a minified production build.

### You’re done!

That’s it! Click here for a [summary](http://typescript-react-primer.loyc.net/tutorial-3.html) of all the steps above and [here](http://typescript-react-primer.loyc.net/tutorial-4.html) to continue learning about TypeScript. Any questions?

