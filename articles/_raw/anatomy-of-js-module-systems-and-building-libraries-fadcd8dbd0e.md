---
title: Learn the basics of the JavaScript module system and build your own library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-08T17:06:32.000Z'
originalURL: https://freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TAApMtvwRDbQ3dTU4bAg7Q.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Kamlesh Chandnani

  Lately we all have been hearing a lot about “JavaScript Modules”. Everyone is likely
  wondering what to do with them, and how do they even play a vital role in our daily
  lives…?

  So what the heck is the JS module system? ?

  As JavaS...'
---

By Kamlesh Chandnani

Lately we all have been hearing a lot about “JavaScript Modules”. Everyone is likely wondering what to do with them, and how do they even play a vital role in our daily lives…?

### **So what the heck is the JS module system? ?**

As JavaScript development gets more and more widespread, namespaces and dependencies get much more difficult to handle. Different solutions have been developed to deal with this problem in the form of module systems.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xM9pXLcsQa641gzCfTz0iw.jpeg)

### Why is understanding the JS Module System important?

Let me tell you a story.

> Telling stories is as basic to human beings as eating. More so, in fact, for while food makes us live, stories are what make our lives worth living - Richard Kearney

Why am I even talking about all this stuff?  
   
So, my day job is to design and architect projects, and I quickly realized that there were many common functionalities required across projects. I always ended up copy-pasting those functionalities to new projects over and over again.

The problem was that whenever one piece of the code changed, I needed to manually sync those changes across all my projects. To avoid all these tedious manual tasks, I decided to extract the common functionalities and compose an npm package out of them. This way, others on the team would be able to re-use them as dependencies and simply update them whenever a new release was rolled out.

This approach had some advantages:

* If there was some change in the core library, then a change only had to be made in one place without refactoring all the applications’ code for the same thing.
* All the applications remained in sync. Whenever a change was made, all the applications just needed to run the “npm update” command.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aCeYnQZBAYNdxG4mkJCGrQ.png)
_Source code of library_

So, next step was to publish the library. Right? ?

This was the toughest part, because there were a bunch of things bouncing around in my head, like:

1. How do I make the tree shakeable?
2. What JS module systems should I target (commonjs, amd, harmony).
3. Should I transpile the source?
4. Should I bundle the source?
5. What files should I publish?

Everyone of us has had these kind of questions bubbling in our heads while creating a library. Right?

I’ll try to address all the above questions now.

### Different Types of JS Module Systems ?

**1. CommonJS**

* Implemented by **node**
* Used for the **server side** when you have modules installed
* No runtime/async module loading
* import via “**require**”
* export via “**module.exports**”
* When you import you get back an object
* No **tree shaking,** because when you import you get an object
* No static analyzing, as you get an object, so property lookup is at runtime
* You always get a copy of an object, so **no live changes** in the module itself
* Poor cyclic dependency management
* Simple Syntax

**2. AMD: Async Module Definition**

* Implemented by **RequireJs**
* Used for the **client side (browser)** when you want dynamic loading of modules
* Import via “require”
* Complex Syntax

**3. UMD: Universal Module Definition**

* Combination of **CommonJs + AMD** (that is, Syntax of CommonJs + async loading of AMD)
* Can be used for both **AMD/CommonJs** environments
* UMD essentially creates a way to use either of the two, while also supporting the global variable definition. As a result, UMD modules are capable of working on both **client and server**.

**4. ECMAScript Harmony (ES6)**

* Used for both **server/client** side
* **Runtime/static loading** of modules supported
* When you **import,** you get back **bindings value** (actual value)
* Import via “import” and export via “export”
* **Static analyzing** — You can determine imports and exports at compile time (statically) — you only have to look at the source code, you don’t have to execute it
* **Tree shakeable,** because of **static analyzing** supported by ES6
* Always get an **actual value** so live changes in the module itself
* Better cyclic dependency management than CommonJS

So now you know all about different types of JS module systems and how they have evolved.

Although the **ES Harmony** module system is supported by all the tools and modern browsers, we never know when publishing libraries how our consumers might utilize them. So we must always ensure that our libraries work in all environments.

Let’s dive in deeper and design a sample library to answer all the questions related to publishing a library in the proper way.

I’ve built a small UI library (you can find the source code on [GitHub](https://github.com/kamleshchandnani/js-module-system)), and I’ll share all my experiences and explorations for transpiling, bundling, and publishing it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1HxrxTNgFJmIVMd5I-ucw.png)
_Directory Structure_

Here we have a small UI library which has 3 components: Button, Card, and NavBar. Let’s transpile and publish it step by step.

### Best practices before publishing ?

1. **Tree Shaking ?**

* **Tree shaking** is a term commonly used in the context of JavaScript for dead-code elimination. It relies on the [static structure](http://exploringjs.com/es6/ch_modules.html#static-module-structure) of ES2015 module syntax, that is, `[import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)` and `[export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)`. The name and concept have been popularized by the ES2015 module bundler [rollup](https://github.com/rollup/rollup).
* Webpack and Rollup both support **Tree Shaking,** meaning we need to keep certain things in mind so that our code is tree shakeable.

2. **Publish all module variants**

* We should publish all the module variants, like `UMD` and `ES`, because we never know which browser/webpack versions our consumers might use this library/package in.
* Even though all the bundlers like [**Webpack**](https://webpack.js.org) and [**Rollup**](https://rollupjs.org) understand ES modules, if our consumer is using **Webpack 1.x,** then it cannot understand the ES module.

```
// package.json
```

```
{"name": "js-module-system","version": "0.0.1",...
```

```
"main": "dist/index.js","module": "dist/index.es.js",
```

```
...}
```

* The `main` field of the `package.json` file is usually used to point to the `UMD` version of the library/package.
* **You might be wondering — how can I release the `ES` version of my library/package? ?**  
The m`odule` field of the p`ackage.json` is used to point to the E`S` version of the library/package. Previously, many fields were used like j`s:next` and j`s:main` , but m`odule` is now standardized and is used by bundlers as a lookup for the E`S v`ersion of the library/package.

> **Less well-known fact:** Webpack uses [resolve.mainfields](https://webpack.js.org/configuration/resolve/#resolve-mainfields) to determine which fields in `package.json` are checked.

> **Performance Tip:** Always try to publish the `ES` version of your library/package as well, because all the modern browsers now support `ES` modules. So you can transpile less, and ultimately you’ll end up shipping less code to your users. This will boost your application’s performance.

**So now what’s next? Transpilation or Bundling? What tools should we use?**

Ah, here comes the trickiest part! Let’s dive in. **?**

### Webpack vs Rollup vs Babel?

These are all the tools we use in our day to day lives to ship our applications/libraries/packages. I cannot imagine modern web development without them — **#_blessed_**. Therefore, we cannot compare them, so that would be the wrong question to ask! ❌

Each tool has it’s own benefits and serves different purpose based on your needs.

Let’s look at each of these tools now:

#### **Webpack**

[Webpack](https://webpack.js.org) is a great module **bundler ?** that is widely accepted and mostly used for building SPAs. It gives you all the features out of the box like c[ode splitting,](https://webpack.js.org/guides/code-splitting/) a[sync loading](https://webpack.js.org/guides/code-splitting/#dynamic-imports) of bundles, t[ree shaking,](https://webpack.js.org/guides/tree-shaking/) and so on. It uses the C**ommonJS** module system.

**PS:** [Webpack-4.0.0](https://github.com/webpack/webpack/issues/6064) alpha is already out ?. Hopefully with the stable release it will become the universal bundler for all types of module systems.

#### **RollupJS**

[Rollup](https://rollupjs.org/) is also a module **bundler** similar to Webpack. However, the main advantage of rollup is that it follows new standardized formatting for code modules included in the **ES6** revision, so you can use it to bundle the **ES module** variant of your library/package. It doesn’t support **async loading** of bundles.

#### **Babel**

[Babel](http://babeljs.io/) is a **transpiler** for JavaScript best known for its ability to turn ES6 code into code that runs in your browser (or on your server) today. Remember that it just **transpiles** and doesn’t bundle your code.

My advice: use Rollup for libraries and Webpack for apps.

### Transpile (Babel-ify) the source or Bundle it

Again there’s a story behind this one. ?

I spent most of my time trying to figure out the answer to this question when I was building this library. I started digging out my node_modules to lookup all the great libraries and check out their build systems.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JJ0hPQW4V7rnaCVHO0nV4w.jpeg)
_Libraries vs Packages build output comparision_

After looking at the build output for different libraries/packages, I got a clear picture of what different strategies the authors of these libraries might have had in mind before publishing. Below are my observations.

As you can see in the above image, I’ve divided these libraries/packages into two groups based on their characteristics:

1. UI Libraries (`styled-components`, `material-ui`)
2. Core Packages (`react`, `react-dom`)

If you’re a good observer ? you might have figured out the difference between these two groups.

**UI Libraries** have a `dist` folder that has the bundled and minified version for **ES** and **UMD/CJS** module systems as a target. There is a `lib` folder that has the **transpiled** version of the library.

**Core Packages** have just one folder which has the bundled and minified version for **CJS** or **UMD** module system as a target.

**But why is there a difference in build output of UI libraries and Core Packages? ?**

#### **UI Libraries**

Imagine if we just publish the bundled version of our library and host it on CDN. Our consumer will use it directly in a`<scrip`t/> tag. Now if my consumer wants to use jus`t the <`;Button/> component, they have to load the entire library. Also, in a browser, there is no bundler which will take care of tree shaking, and we’ll end up shipping the whole library code to our consumer. We don’t want this.

```
<script type="module">import {Button} from "https://unpkg.com/uilibrary/index.js";</script>
```

Now if we simply transpile the `src` into `lib` and host the `lib` on a CDN, our consumers can actually get whatever they want without any overhead. “Ship less, load faster”. ✅

```
<script type="module">import {Button} from "https://unpkg.com/uilibrary/lib/button.js";</script>
```

#### Core Packages

Core packages are never utilized via the `<scrip`t/> tag, as they need to be part of main application. So we can safely release the bundled ver**sion (U**MD, ES) for these kinds of packages and leave the build system up to the consumers.

For example, they can use the **UMD** variant but no tree shaking, or they can use the **ES** variant if the bundler is capable of identifying and getting the benefits of tree shaking.

```
// CJS requireconst Button = require("uilibrary/button");
```

```
// ES importimport {Button} from "uilibrary";
```

But…what about our question: should we **transpile (Babelify) the source or bundle it? ?**

For the UI Library, we need to **transpile** the source with **Babel** with the `es` module system as a target, and place it in `lib`. We can even host the `lib` on a CDN.

We should **bundle** and minify the source using **rollup** for `cjs/umd` module system and `es` module system as a target. Modify the `package.json` to point to the proper target systems.

```
// package.json
```

```
{"name": "js-module-system","version": "0.0.1",...
```

```
"main": "dist/index.js",      // for umd/cjs builds"module": "dist/index.es.js", // for es build
```

```
...}
```

For **core packages**, we don’t need the `lib` version.

We just need to **bundle** and minify the source using **rollup** for `cjs/umd` module system and `es` module system as a target. Modify the `package.json` to point to the proper target systems, same as above.

**Tip**: We can host the `dist` folder on the CDN as well, for the consumers who are willing to download the whole library/package via `<scrip`t/> tag.

### How should we build this?

We should have different scripts for each target system in `package.json` . You can find the [rollup config](https://github.com/kamleshchandnani/js-module-system/blob/master/rollup.config.js) in the GitHub repo.

```
// package.json
```

```
{..."scripts": {"clean": "rimraf dist","build": "run-s clean && run-p build:es build:cjs build:lib:es","build:es": "NODE_ENV=es rollup -c","build:cjs": "NODE_ENV=cjs rollup -c","build:lib:es": "BABEL_ENV=es babel src -d lib"}...}
```

### What should we publish?

* License
* README
* Changelog
* Metadata(`main` , `module`, `bin`) — **package.json**
* Control through **package.json** `files` property

In `package.json` , the `"files"` field is an array of file patterns that describes the entries to be included when your package is installed as a dependency. If you name a folder in the array, then it will also include the files inside that folder.

We will include the `lib` and `dist` folders in `"files"` field in our case.

```
// package.json
```

```
{..."files": ["dist", "lib"]...}
```

Finally the library is ready to publish. Just type the `npm run build` command in the terminal, and you can see the following output. Closely look at the `dist` and `lib` folders. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*C0wMVo17NTVcTroA8dPe9g.png)
_Ready to publish ?_

### Wrap up

Wow! Where does the time go? That was a wild ride, but I sincerely hope it gave you a better understanding of the JavaScript Module system and how you can create your own library and publish it.

Just make sure you take care of the following things:

1. Make it **Tree Shakeable**. ?
2. Target at least **ES Harmony** and **CJS** module systems. ?
3. Use **Babel** and **Bundlers** for libraries. ?
4. Use **Bundlers** for Core packages. ?
5. Set the `module` field of `package.json` to point to the **ES** version of your module (PS: It helps in tree shaking). ?
6. Publish the folders which have **transpiled** as well as **bundled** versions of you module. ?

### Trending this week ?

1. [Webpack-V4](https://github.com/webpack/webpack/issues/6064) alpha released. ?
2. [ParcelJs](https://parceljs.org/): Blazing fast, zero configuration web application bundler. ?
3. [Turbo](https://medium.com/@ericsimons/introducing-turbo-5x-faster-than-yarn-npm-and-runs-natively-in-browser-cc2c39715403): 5x faster than Yarn & NPM, and runs natively in-browser ?

_Thanks to [Juho Vepsäläinen](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) and [Lakshya Ranganath](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) for their reviews & feedback, [Sean T. Larkin](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) and [Tobias Koppers](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) for sharing the insights of webpack at [ReactiveConf](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined), [Addy Osmani](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) for sharing workings of different JS module Systems in [“Writing Modular JavaScript With AMD, CommonJS & ES Harmony”](https://addyosmani.com/writing-modular-js/)._

**_P.S. If you like this, make sure to recommend (by clap? ) , f[ollow me on twitter,](https://twitter.com/_kamlesh_) and share this with your friends!?_**

