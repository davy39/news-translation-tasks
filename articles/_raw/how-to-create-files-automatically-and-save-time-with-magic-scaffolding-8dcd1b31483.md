---
title: How to create files automatically and save time with magic scaffolding
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T19:47:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-files-automatically-and-save-time-with-magic-scaffolding-8dcd1b31483
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4xIsUwu1lTMXm0IZ
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jonathan Wood

  Before we begin: This article uses JavaScript / Node.js example code, but you can
  port these concepts to any language using the right tools.

  An exciting intro

  Do you ever find yourself creating the same files over and over again in y...'
---

By Jonathan Wood

**Before we begin:** This article uses JavaScript / Node.js example code, but you can port these concepts to any language using the right tools.

### An exciting intro

**Do you ever find yourself creating the same files over and over again in your projects?**

I do, too.

#### My fingers hurt!

I’m not surprised. You’re taking work from the robots.

Creating the same files repeatedly is boring and unnecessary.

#### TLDR? I got you — Here’s a demo

![Image](https://cdn-media-1.freecodecamp.org/images/1*DVXreOfKQqtyY4CfLxiJ8w.gif)
_Magical automation — as promised._

#### Show me the code

I respect your sense of urgency — I’ll cut to the chase.

### The Code

We want to automate file creation — that’s why you all showed up today. First, we need to identify the files we want to create.

I’ve been creating a lot of React components lately, so my setup revolves around that — but you can tweak this for literally anything.

I’ve split this into four steps. Just telling you now so you can manage your expectations. If you can’t handle anything longer than three steps, then we’re in trouble...

#### Step 1: Templates

Set them up once and profit.

We need templates. I used [Template Literals](https://developers.google.com/web/updates/2015/01/ES6-Template-Strings), but do it in whatever way makes sense to you — be creative.

These are the files I’m creating every time I make a React component:

1. **index.jsx**
2. **{Component}.test.js**
3. **{Component}.sass**

**Note:** {Component} implies [string interpolation](https://en.wikipedia.org/wiki/String_interpolation#Examples).

I’m testing with [Jest](https://jestjs.io/docs/en/tutorial-react), and using the [create-react-app](https://github.com/facebook/create-react-app) boilerplate. I know a lot of people prefer [CSS-in-JS](https://alligator.io/react/css-in-js-roundup-styling-react-components/) these days — but hey. Let me know in the comments what you’re into.

Anyway — Here we go:

```js
const templates = {
  
  index: name => `// @flow
import React from 'react';
import './${name}.css';
// TODO: write rest of ${name} component
const ${name} = () => (
  <div className="${name.toLowerCase()}">
    <span>rest of component</span>
  </div>
);
export default ${name};`,
  
  test: name => `// TODO: TDD
import { shallow, render } from 'enzyme';
import renderer from 'react-test-renderer';
import React from 'react';
import ${name} from '.';
const component = <${name} />;
describe('The ${name} component', () => {
  it('renders correctly', () => {
    const wrapper = render(component);
    expect(wrapper.hasClass('${name.toLowerCase()}')).toBeTruthy();
    const tree = renderer.create(component).toJSON();
    expect(tree).toMatchSnapshot();
  });
});`,
  
  sass: name => `.${name.toLowerCase()}
  background: initial`,
};
```

That’s the messiest piece of code you’ll see here — pinky promise.

So, we have an object with three properties: index, test, and sass. Each hosts a function which takes a name and returns a template with that name interpolated. Seems legit.

#### Step 2: Let’s make some functions!

We’re using the [fs module](https://nodejs.org/api/fs.html#fs_file_system) packaged with Node. It’s fab. It does many things.

We’re going to use some [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) and a little [functional programming](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/). Don’t be scared — just go with it.

The double arrow function syntax is called [currying](https://stackoverflow.com/questions/32782922/what-do-multiple-arrow-functions-mean-in-javascript). It’s okay if it looks weird. I was freaked out when I first saw it, but it allows for [super cool stuff](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch04.html#cant-live-if-livin-is-without-you). In fact, here’s a quick demo:

```js
const fs = require('fs');

const fileExists = path => file => fs.existsSync(`${path}/${file}`);

const fileExistsInSrc = fileExists('/src'); // file => fs.existsSync(`${path}/${file}`)

fileExistsInSrc('index.js') // true || false
```

So that’s [currying](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch04.html#cant-live-if-livin-is-without-you) with [partial application](https://stackoverflow.com/questions/218025/what-is-the-difference-between-currying-and-partial-application) — it’s also a [closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).

**Sidebar**: Hopefully nobody calls me out here on some technicality, but please do harass me in the comments if you feel the need.

Let’s carry on:

```js
const fs = require('fs');

const fileExists = path => file => fs.existsSync(`${path}/${file}`);

const writeToPath = path => (file, content) => {
  const filePath = `${path}/${file}`;

  fs.writeFile(filePath, content, err => {
    if (err) throw err;
    console.log("Created file: ", filePath);
    return true;
  });
};
```

First we require [**fs**](https://nodejs.org/api/fs.html#fs_file_system). We need it in our life.

Then we declare **fileExists** as a [function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function).

Finally we have another [function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function) called **writeToPath.** It takes the **path** and returns another function which accepts a **file** string and the **content** of that file. It then writes the file or throws an error (worst case scenario).

You get it right? We’re creating some files.

#### **Step 3: Meet Chokidar**

Fun fact: It’s a [Hindi word](https://en.wiktionary.org/wiki/chowkidar#English).

> **Chowkidar** — (_India_) watchman, caretaker, gatekeeper; one who inhabits a “chowki”, police station or guard house.

We’re talking about the [npm package](https://github.com/paulmillr/chokidar) though. It’s based on our new friend [fs](https://nodejs.org/api/fs.html#fs_class_fs_fswatcher) and you could use it for so many delightful things.

It watches our files for us [like a hawk](https://idioms.thefreedictionary.com/watch+like+a+hawk).

Well not exactly like a hawk.

It is not a bird.

Like at all.

Anyway, here’s the code…

```js
const chokidar = require("chokidar");

const watcher = chokidar
  .watch("src/components/**", { ignored: /node_modules/ })
  .on("addDir", (path, event) => {
    const name = path.replace(/.*\/components\//, "");
    const goodToGo = /^[^\/_]*$/.test(name);
    if (goodToGo) createFiles(path, name);
  });
```

First we require it.

Next we define what we want to watch. I’m watching the **src/components** directory, but you can watch any set of paths. You can even pass an [array of paths](https://github.com/paulmillr/chokidar#api). If you don’t recognize the ****** part in **src/components/**** — it’s called a [glob pattern](https://en.wikipedia.org/wiki/Glob_%28programming%29).

After that, we define what events we want to listen for. I’m only listening for adding a directory with **.on(“addDir”)** but you can listen for [other events](https://github.com/paulmillr/chokidar#methods--events) too.

Next let’s extract the name of the component by replacing anything before the component name:

```
src/components/Header/components/Title
```

becomes

```
Title
```

Finally we will check that the component name passes this regex:

```
/^[^\/_]*$/
```

So as long as it doesn’t have a forward slash or underscore — it’s good to go. This avoids polluting __tests__ folders or nested/directories by mistake.

#### Step 4: Time to make some files!

You reached the last step. Congratulations! It’s been pretty great.

This next function is aptly named **createFiles**.

It’s a bit messy — it could be refactored.

I apologize in advance if the code below offends you.

Let’s dig in:

```js
function createFiles(path, name) {
  const files = {
    index: "index.jsx",
    test: `${name}.test.js`,
    sass: `${name}.sass`
  };

  if (name !== "components") {
    const writeFile = writeToPath(path);
    const toFileMissingBool = file => !fileExists(path)(file);
    const checkAllMissing = (acc, cur) => acc && cur;

    const noneExist = Object.values(files)
      .map(toFileMissingBool)
      .reduce(checkAllMissing);

    if (noneExist) {
      console.log(`Detected new component: ${name}, ${path}`);
      Object.entries(files).forEach(([type, fileName]) => {
        writeFile(fileName, templates[type](name));
      });
    }
  }
}
```

So at the top, we declare the **files** object — it’s a list of file name strings which we’re injecting the **name** parameter into. You might have noticed that it has the same keys as the **templates** object. That’s important.

The **if** statement is very specific to my setup. I don’t want to create my files **if** the new folder is called components. I am only creating components **within** a components sub-folder.

* **writeFile** is our function **writeToPath** [partially applied](https://stackoverflow.com/questions/218025/what-is-the-difference-between-currying-and-partial-application). It’s a function that creates a file in the given path when called with a filename and some content.
* **toFileMissingBool** takes a file name and returns true if that file doesn’t exist in the given path. I know the function names are weird, but I promise it kind of makes more sense in a few lines.
* **checkAllMissing** is a function that we are going to pass to [**reduce**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce). It takes two booleans and returns true if both are true. This is [boolean algebra](https://benmccormick.org/2018/03/27/cs-basics-boolean/). We are also using the [**reduce**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) method of **Array**. Don’t be afraid of reduce. It’s super cool and really useful in this kind of situation.

Let’s talk about the variable **noneExist**. If it’s true, then none of the files we want to create exist in the new folder. The idea is that you don’t mess with a folder just because it doesn’t have a test file or a sass file. Maybe that folder doesn’t need one.

```js
const noneExist = Object.values(files)
  .map(toFileMissingBool)      
  .reduce(checkAllMissing);
```

That’s why I created those strangely named functions above.

We **map** the values in **files** to a **boolean** which represents if that file is missing or not. Then we take that **array of booleans** and **reduce** them to a single **boolean** value which represents whether all the files exist or not.

So if they’re all **true,** then **noneExist** is also **true.** But if even one is **false,** then **noneExist** will be **false**.

I hope you got all that. It’s a [bit of a mouthful](https://www.ldoceonline.com/dictionary/a-bit-of-a-mouthful).

Last bit of code:

```js
Object.entries(files).forEach(([type, fileName]) => {
  writeFile(fileName, templates[type](name)); 
});
```

We take the key (**type)** and value **(fileName)** and write a file in the given path with the content from the relevant template.

#### [Fin.](https://www.quora.com/What-does-fin-mean-at-the-end-of-a-film-or-story?share=1)

![Image](https://cdn-media-1.freecodecamp.org/images/0*rv8KkV_Kvdfj941i)
_“Big sea turtle swimming through the ocean at Kaputas Beach” by [Unsplash](https://unsplash.com/@ruizra?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Randall Ruiz</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

That picture of a sea turtle represents how free you must be feeling now you have automated everything.

If you want the whole code for auto-creating react components, [it’s here](https://gist.github.com/Bamblehorse/6ad136c83e6fd2ea62375fa92d843a14).

Let me know what you thought — Keep in touch.

Tell me if you find any errors.

Follow me on [Twitter](https://twitter.com/Bamblehorse), [Medium](https://medium.com/@Bamblehorse) or [Github](https://github.com/Bamblehorse).

