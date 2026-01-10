---
title: Here’s how I created a markdown app with Electron and React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T17:12:38.000Z'
originalURL: https://freecodecamp.org/news/heres-how-i-created-a-markdown-app-with-electron-and-react-1e902f8601ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AUYsysbayWGQXG23G0L-3g.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tzahi Vidas

  This article is a step-by-step tutorial on how to create a basic markdown application
  using Electron and React.

  I’ll describe why, how, and what I used to create the markdown app, which I call
  Mook.

  The source code for Mook can be foun...'
---

By Tzahi Vidas

This article is a step-by-step tutorial on how to create a basic markdown application using [Electron](https://electron.atom.io/) and [React.](https://facebook.github.io/react/)

I’ll describe why, how, and what I used to create the markdown app, which I call **Mook**.

The source code for Mook can be found on [GitHub](https://github.com/kazuar/mook).

### Motivation

There are a couple of reasons I started this project.

Recently, I’ve been seeing more impressive and interesting things that you can do with JavaScript. I’ve also been wanting to do something with [Electron](https://electron.atom.io/) for a while now.

I had always felt weird coding with JavaScript, and, as such, avoided it. Every time I tried to do something with JavaScript, I always felt like I was just hammering on a keyboard to get whatever it was to work.

![Image](https://cdn-media-1.freecodecamp.org/images/utrP4W38SfxvfTxeSADlp9z-cV8e6T3Copww)

However, I recently found myself looking more into JavaScript. It suddenly felt like a good tool to use to solve some of the problems I’ve been working on.

On another note (see the pun?), whenever I use a note-taking application, I always feel like there’s a feature missing that I can find in another app. But the other app will not have the features that the third app might provide. And so I’m always on the lookout for new and better note-taking apps.

With these thoughts in mind, I decided to learn JavaScript while building a markdown notes editor with Electron.

### Requirements

Some of the requirements I came up with for the markdown app are as listed.  
Note that there are many more, but the following are on my initial list.

* Editor and preview panes
* Split screen between the editor and preview panes that can be dynamically moved
* Support for code blocks and code language highlighting
* Support for saving and syncing notes on GitHub
* A hierarchy of notebooks and markdown notes
* Support for LaTeX / math equations in the editor
* Ability to group different notebooks with a shared topic
* Ability to share notebooks on GitHub and on Dropbox, Google Docs and others.

### The stack

I had to make a few decisions for this project. For example:

Should I use a [boilerplate](https://github.com/chentsulin/electron-react-boilerplate)?

Should I use React, [AngularJS](https://en.wikipedia.org/wiki/AngularJS), [Riot](http://riotjs.com/), or [Vue](https://vuejs.org/)?

What kind of packages would I use?

And so on.

In the end, I decided to avoid the boilerplate approach (at least for now). I did this because I wanted to build the foundations of the app myself and learn more about it in the process.

I tried to build the app with React because I’ve heard a lot about it from friends. It appears that this is what the cool kids are using these days.

![Image](https://cdn-media-1.freecodecamp.org/images/ICDj0frNAuq-cLLBJApvUQ7frLzuVitvq3lw)

### Creating the environment for the app

Because we are using React, we’ll start by creating a basic React application and then add Electron to it.

We’ll start our project using [create-react-app](https://github.com/facebookincubator/create-react-app).

#### Preparing the environment

An easy way to create React applications with a basic configuration is to use the **create-react-app**.

First, make sure that you have the latest node and npm versions on your machine. To check, run the following commands:

```
node -v
npm -v
yarn — version
```

When I was writing this article, these were the versions on my machine:

```
node = v8.4.0
npm = 5.3.0
yarn = 1.0.1
```

#### Creat a React app with create-react-app

To install **create-react-app** as a global package, type the following command:

```
npm install -g create-react-app
```

To create a new React app and `cd` in it:

```
create-react-app mook
cd mook
```

This is what our project looks like now. I’ve excluded the `**node_modules**` folder from view so that you can get a clear view of the project.

```
tree -I “node_modules”
.
├── README.md
├── package.json
├── public
│ ├── favicon.ico
│ ├── index.html
│ └── manifest.json
├── src
│ ├── App.css
│ ├── App.js
│ ├── App.test.js
│ ├── index.css
│ ├── index.js
│ ├── logo.svg
│ └── registerServiceWorker.js
└── yarn.lock

2 directories, 13 files
```

Now that we have a basic React app, to see what it looks like, let’s run the `start` script that’s defined in the `**package.json**` file:

```
yarn run start
```

That starts a new browser window with the following page:

![Image](https://cdn-media-1.freecodecamp.org/images/lsK3QALqqYu3tMMGYdKdP9z5l4qDsQFkoTbN)

#### Install Electron

Electron allows us to build an application that has the ability to run across platforms.

To install the Electron package:

```
yarn add electron — dev
```

Open the `**package.json**` file.

If everything’s OK, you should be able to see the Electron package in the `**devDependencies**` section of the file.

Update the `**package.json**` file with the following changes:

* To add the following line to the scripts section:

```
“electron-start”: “electron .”
```

* To add a top-level `**main**` property and point it to the main Electron file (this file doesn’t exist yet, but we will be creating it shortly):

```
“main”: “public/main.js”
```

The `**package.json**` file now looks like this:

```json
{
  “name”: “mook”,
  “version”: “0.1.0”,
  “main”: “public/main.js”,
  “private”: true,
  “dependencies”: {
    “react”: “¹⁵.6.1”,
    “react-dom”: “¹⁵.6.1”,
    “react-scripts”: “1.0.13”
  },
  “scripts”: {
    “start”: “react-scripts start”,
    “build”: “react-scripts build”,
    “test”: “react-scripts test — env=jsdom”,
    “eject”: “react-scripts eject”,
    “electron-start”: “electron .”
  },
  “devDependencies”: {
    “electron”: “¹.7.6”
  }
}
```

Next, we’ll add some of [Electron’s events](https://github.com/electron/electron/blob/master/docs/api/app.md) to control the application’s life cycle. We will implement the following events:

* [**ready**](https://github.com/electron/electron/blob/master/docs/api/app.md#event-ready)**:** Runs when Electron has finished initializing. In the code, this will run `**createWindow**`**,** which creates a browser window with React’s local URL, `**http://localhost:3000**`, and sets the about panel and the `**mainWindow**` to `null` on `close`.
* [**activate**](https://github.com/electron/electron/blob/master/docs/api/app.md#event-activate-macos)**:** Runs when the application is activated. We’ll want to call the `**createWindow**` function to create a new window.
* [**window-all-closed**](https://github.com/electron/electron/blob/master/docs/api/app.md#event-window-all-closed)**:** Emitted when all windows have been closed. This will close the app on all platforms, except Mac, which will only close the window but will explicitly require the user to quit the program.

Add the following code to `**public/main.js**`:

```js
const electron = require(‘electron’);
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({width: 900, height: 680});
  mainWindow.loadURL(‘http://localhost:3000');
                     
  app.setAboutPanelOptions({
    applicationName: “Mook”,
    applicationVersion: “0.0.1”,
  })
  
  mainWindow.on(‘closed’, () => mainWindow = null);
}

app.on(‘ready’, createWindow);

app.on(‘window-all-closed’, () => {
  if (process.platform !== ‘darwin’) {
    app.quit();
  }
});

app.on(‘activate’, () => {
  if (mainWindow === null) {
    createWindow();
  }
});
```

Make sure that React is still running in the background. If not, run it again with the following command:

```
yarn run start
```

Open a new command line window in the project’s folder and run the following command:

```
yarn run electron-start
```

After you run the command, the following window opens:

![Image](https://cdn-media-1.freecodecamp.org/images/Mo590jpoclfSSANaDlvQ8r7tIlPeQifWNh7L)

If React is not running in the background, the Electron app will open with a blank white window.

#### Creating a stable development and build process

Now that we have a working template for our project using Electron and React, we need to make sure that we have a stable build for development and distribution.

What we have created until now is great for development, but eventually we want to create the distribution versions of the app for OS X, Windows, and Linux.

I also didn’t like that we have to separately run the React server and Electron app in two different command line shells.

After doing some research into the topic, I found the following post, “[From React to an Electron app ready for production](https://medium.com/@kitze/%EF%B8%8F-from-react-to-an-electron-app-ready-for-production-a0468ecb1da3)” by [@thekitze](http://twitter.com/thekitze), which helped me a lot.

We will need to add the following packages to our project:

* [electron-builder](https://www.electron.build/) — A complete solution to package and build a ready-for distribution Electron app for MacOS, Windows, and Linux with “auto update” support out of the box. We will use this package to build our app for distribution.
* [concurrently](https://github.com/kimmobrunfeldt/concurrently) — Runs commands concurrently. We will use this package to run React and Electron concurrently in one command.
* [wait-on](https://github.com/jeffbski/wait-on) — Command line utility and Node.js API, which will wait for files, ports, sockets, and http(s) resources to become available. We will use this package to wait for the React server to begin running before starting the Electron app.

Run the following commands to add these packages to our app:

```
yarn add electron-builder wait-on concurrently — dev
```

Since these packages are only required for development, we will add the flag `— dev` to the `yarn add` command. This will also automatically add the packages to the `**devDependencies**` part of `**package.json**`.

#### Create a dev script

We want to create a development script to use while we’re building the app. This will help us test new features that we developed in the application and also to debug and make sure that we’re not breaking anything while we’re editing the code.

We’ll add a new script in the `**scripts**` section of our `**package.json**` file:

```
“electron-dev”: “concurrently \”BROWSER=none yarn start\” \”wait-on http://localhost:3000 && electron .\””
```

There are a lot of things happening in this line, so let’s break it down:

![Image](https://cdn-media-1.freecodecamp.org/images/4vjCPBpvCmt8MH03cfx56EoQ4dm6wSMUv1Bv)

1. “**concurrently”** — Runs the following commands at the same time.
2. “**BROWSER=none yarn start”** — Starts the react application and sets “**BROWSER=none”**. This means that the browser will not automatically open the React application.
3. “**wait-on http://localhost:3000 && electron”** — Waits for the development server to start. Once it’s up, it will start the Electron application.

Now, if you run the following from your command line, you will only get a single Electron application window with the React logo.

```
yarn run electron-dev
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1__2brQgn4gVrugCl65hwQXQ.png)

#### Create a build script

Creating the build script is a bit easier.

We need to add a couple of scripts to the `**scripts**` section in the `**package.json**` file:

* Here is a script to build the React app before building the Electron app:

```
“preelectron-pack”: “yarn build”
```

* Here is a script for packaging the Electron app. This script builds the application package with **electron-builder**.

```
“electron-pack”: “build — em.main=build/electron.js”
```

Next, we will have to specify the `**build**` property. This is because of a minor conflict between **create-react-app** and **electron-builder**. Both are using the `**build**` folder for a different purpose.

In order to solve this conflict, we need to manually configure **electron-builder’s** correct folders for the build step. Add the following `**build**` section to the `**package.json**` file:

```json
“build”: {
  “appId”: “com.mook”,
  “files”: [
    “build/**/*”,
    “node_modules/**/*”
  ],
  “directories”: {
    “buildResources”: “assets”
  }
}
```

We also need to add the `**homepage**` property to allow the packaged Electron app to find the JavaScript and CSS files:

```
“homepage”: “./”
```

At this point, your `**package.json**` file should look like this:

```json
{
  “name”: “mook”,
  “version”: “0.1.0”,
  “main”: “public/main.js”,
  “homepage”: “./”,
  “private”: true,
  “scripts”: {
    “start”: “react-scripts start”,
    “build”: “react-scripts build”,
    “test”: “react-scripts test — env=jsdom”,
    “eject”: “react-scripts eject”,
    “electron-start”: “electron .”,
    “electron-dev”: “concurrently \”BROWSER=none yarn start\” \”wait-on http://localhost:3000 && electron .\””,
    “electron-pack”: “build — em.main=build/main.js”,
    “preelectron-pack”: “yarn build”
  },
  “dependencies”: {
    “react”: “¹⁵.6.1”,
    “react-dom”: “¹⁵.6.1”,
    “react-scripts”: “1.0.13”,
    “electron-is-dev”: “⁰.3.0”
  },
  “devDependencies”: {
    “concurrently”: “³.5.0”,
    “electron”: “¹.7.6”,
    “electron-builder”: “¹⁹.27.7”,
    “wait-on”: “².0.2”
  },
  “build”: {
    “appId”: “com.mook”,
    “files”: [
      “build/**/*”,
      “node_modules/**/*”
    ],
    “directories”: {
      “buildResources”: “assets”
    }
  }
}
```

The last step will be to update `**public/main.js**`. Until now, we’ve only supported the development version of the app. In production we won’t be able to use `**localhost:3000**`, instead we will serve the `**index.html**` file from the `**build**` folder.

First, we need to install [electron-is-dev](https://github.com/sindresorhus/electron-is-dev), which will help us determine if Electron is running in development.

To install the **electron-is-dev** package:

```
yarn add electron-is-dev
```

To update `**public/main.js**` to use [electron-is-dev:](https://github.com/sindresorhus/electron-is-dev)

* To add the package to the code:

```js
const isDev = require(‘electron-is-dev’);
const path = require(‘path’);
```

* To change the `**mainWindow.loadURL**` functionality in the `**createWindow**` function:

```js
mainWindow.loadURL(isDev ? ‘http://localhost:3000' : `file://${path.join(__dirname, ‘../build/index.html’)}`);
```

This code checks if we are in development mode, and if we are, it will use `**localhost:3000**`. Otherwise it will serve`**/build/index.html**`**.**

Your `**public/main.js**` file should now look like this:

```
const electron = require(‘electron’);
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const isDev = require(‘electron-is-dev’);
const path = require(‘path’);

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({width: 900, height: 680});
  mainWindow.loadURL(isDev ? ‘http://localhost:3000' : `file://${path.join(__dirname, ‘../build/index.html’)}`);
  
  app.setAboutPanelOptions({
    applicationName: “Mook”,
    applicationVersion: “0.0.1”,
  })
  
  mainWindow.on(‘closed’, () => mainWindow = null);
}

app.on(‘ready’, createWindow);

app.on(‘window-all-closed’, () => {
  if (process.platform !== ‘darwin’) {
    app.quit();
  }
});

app.on(‘activate’, () => {
  if (mainWindow === null) {
    createWindow();
  }
});
```

Now, let’s try to run the build script with the following command:

```
yarn run electron-pack
```

When the script run is complete, you should see a new folder named `**dist**` in your project’s directory. You can find your packaged application in the folder named after your operating system. For example, Mac users will be able to find the packaged application `**mook.app**` in the `**dist/mac**` folder.

When you run that file, you should get the same screen you get for the debug version:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1__2brQgn4gVrugCl65hwQXQ-1.png)

Excellent, we’ve just finished the build infrastructure for our app.

![Image](https://cdn-media-1.freecodecamp.org/images/lInY6KaaZ7USQOYq9c1KZoiKFmJ-tVpUxt7G)

### Adding main functionalities

Now we’re able to start adding building blocks to our markdown app.

#### Creating a split pane screen

Let’s start by adding the split pane component, [react-split-pane](https://github.com/tomkp/react-split-pane), to our application.

To install the **react-split-pane** package:

```
yarn add react-split-pane
```

To add the following JavaScript code to the `**src/App.js**` file:

* Import `**react-split-pane**`:

```js
import SplitPane from ‘react-split-pane’;
```

* Replace the render function with the following code. This code adds the `**SplitPane**` element to the render function with two divs, one for the editor and one for the preview pane:

```jsx
render() {
  return (
    <div className=”App”>
      <SplitPane split=”vertical” defaultSize=”50%”>
        <div className=”editor-pane”>
        </div>
        <div className=”view-pane”>
        </div>
      </SplitPane>
    </div>
  );
}
```

We also need to add some CSS.

To add the following code to `**src/App.css**`:

```css
.Resizer {
  background: #000;
  opacity: 0.4;
  z-index: 1;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -moz-background-clip: padding;
  -webkit-background-clip: padding;
  background-clip: padding-box;
}
.Resizer:hover {
  -webkit-transition: all 2s ease;
  transition: all 2s ease;
}
.Resizer.horizontal {
  height: 11px;
  margin: -5px 0;
  border-top: 5px solid rgba(255, 255, 255, 0);
  border-bottom: 5px solid rgba(255, 255, 255, 0);
  cursor: row-resize;
  width: 100%;
}
.Resizer.horizontal:hover {
  border-top: 5px solid rgba(0, 0, 0, 0.5);
  border-bottom: 5px solid rgba(0, 0, 0, 0.5);
}
.Resizer.vertical {
  width: 11px;
  margin: 0 -5px;
  border-left: 5px solid rgba(255, 255, 255, 0);
  border-right: 5px solid rgba(255, 255, 255, 0);
  cursor: col-resize;
}
.Resizer.vertical:hover {
  border-left: 5px solid rgba(0, 0, 0, 0.5);
  border-right: 5px solid rgba(0, 0, 0, 0.5);
}
.Resizer.disabled {
  cursor: not-allowed;
}
.Resizer.disabled:hover {
  border-color: transparent;
}

```

If you refresh the app or run it with the command `**yarn run electron-dev**`, you should see the following screen, which is currently just an empty page divided into two panes:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_N7OaT0YRZHck2YnRZ6BHyA.png)

You can play around with the separator bar and see how it resizes the different panes.

### Creating the editor and preview panes

Now that we have our split screen, we need to add functionalities for the editor and preview panes.

We want to set up the panes like they are usually set up in markdown editors, with the editor pane on the left and the preview pane on the right. We will write our markdown in the editor pane, and the preview pane will update every time we change something in the editor pane.

#### Creating the editor pane

Let’s start with the editor pane.

We will use [CodeMirror](https://codemirror.net/), which is a JavaScript text editor.

Install the React package for code mirror [React-CodeMirror](https://github.com/JedWatson/react-codemirror). Because “[Code mirror value doesn’t update with state change](https://github.com/JedWatson/react-codemirror/issues/106)" in **React-CodeMirror**, we will install `[**@skidding/react-codemirror**](http://twitter.com/skidding/react-codemirror)` , which solves that issue:

```
yarn add @skidding/react-codemirror
```

Create a new file called `**src/editor.js**`, with a new class called `Editor` that extends React’s Component class:

```jsx
import React, { Component } from ‘react’;

class Editor extends Component {
}

export default Editor;
```

This class will basically wrap the **react-codemirror** package that is a React component for CodeMirror.

Next, we will import `**@skidding/react-codemirror**` and some CSS files that we want to use for the CodeMirror component, syntax highlighting, and markdown mode.

We will also add a `render` function that will return the CodeMirror element and add a `**constructor**` to the `**Editor**` class. This **constructor** allows us to initialize the CodeMirror with a value from the main file.

We’ll set the `CodeMirror` component to `**markdown**` mode and the theme to `**monokai**`:

```jsx
import React, { Component } from ‘react’;
import CodeMirror from ‘@skidding/react-codemirror’;

require(‘codemirror/lib/codemirror.css’);
require(‘codemirror/mode/javascript/javascript’);
require(‘codemirror/mode/python/python’);
require(‘codemirror/mode/xml/xml’);
require(‘codemirror/mode/markdown/markdown’);
require(‘codemirror/theme/monokai.css’);

class Editor extends Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    var options = {
      mode: ‘markdown’,
      theme: ‘monokai’,
    }
    return (
      <CodeMirror value={this.props.value} 
 options={options} height=”100%”/>
    );
  }
}

export default Editor;
```

In the `**src/App.js**` file, we will import `**editor.js**` (add to the beginning of the file):

```js
import Editor from ‘./editor.js’;
```

In the `**App**` class, let’s add a constructor with an initial value for our editor:

```jsx
constructor(props) {
  super();
  
  this.state = {
    markdownSrc: “# Hello World”,
  }
}
```

In the `**render**` function of the `**App**` class, add the `**Editor**` component and set the value to `**markdownSrc**`:

```jsx
render() {
  return (
    <div className=”App”>
      <SplitPane split=”vertical” defaultSize=”50%”>
        <div className=”editor-pane”>
          <Editor className=”editor” value={this.state.markdownSrc}/>
        </div>
        <div className=”view-pane”>
        </div>
      </SplitPane>
    </div>
  );
}
```

The `**src/App.js**` file should look like this:

```jsx
import React, { Component } from ‘react’;
import logo from ‘./logo.svg’;
import SplitPane from ‘react-split-pane’;
import Editor from ‘./editor.js’;

import ‘./App.css’;

class App extends Component {
  constructor(props) {
    super();
    
    this.state = {
      markdownSrc: “# Hello World”,
    }
  }
  
  render() {
    return (
      <div className=”App”>
        <SplitPane split=”vertical” defaultSize=”50%”>
          <div className=”editor-pane”>
            <Editor className=”editor” value={this.state.markdownSrc}/>
          </div>
          <div className=”view-pane”>
          </div>
        </SplitPane>
      </div>
    );
  }
}

export default App;
```

Update the CSS file `**src/App.css**` with the following changes:

1. In the `**_._App**` section (at the top of the file), remove `text-align: center_;_` so that the text is not aligned to the center.
2. Add the following CSS code, so that it will stretch the editor to full height and add a little padding to the right side of the text:

```css
.editor-pane {
  height: 100%;
}

.CodeMirror {
  height: 100%;
  padding-top: 20px;
  padding-left: 20px;
}

.ReactCodeMirror {
  height: 100%;
}
```

Refresh the app or run it with the command `**yarn run electron-dev**`, and you should see the following screen:

![Image](https://cdn-media-1.freecodecamp.org/images/qrzujQdXJKWkneuwg3GkQ9VJwI-9pmvY4Lsj)

#### Creating the preview pane

We want the right pane to be a live preview of the editor that is on the left pane.

In order to do that, we will use the [React-Markdown](https://github.com/rexxars/react-markdown) package:

```
yarn add react-markdown
```

In the `**src\App.js**` file, add the following import:

```js
import ReactMarkdown from ‘react-markdown’;
```

Add the `**ReactMarkdown**` component inside the `view-pane` div:

```jsx
<div className=”view-pane”>
  <ReactMarkdown className=”result” source={this.state.markdownSrc} />
</div>
```

Set the source of the `**ReactMarkdown**` component so that it is the same as the one in the editor, `**this.state.markdownSrc**`.

You can now run the yarn application and see the preview pane:

```
yarn run electron-dev
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_xJEfP8eefOh1U-_u1P6BBA.png)

We can see the text in the preview pane. However, if we type something in the editor (left) pane, it won’t transfer to the preview (right) pane.

What we’re going to do is make every change in the editor pass to the preview, through the `**App**` class.

Adding the `onMarkdownChange` function to `**src\App.js**` will update `**markdownSrc**` with updated text from the editor. This function will run on every change that happens in the editor.

Add the following code to `**src\App.js**`:

```jsx
constructor(props) {
  super();
  
  this.state = {
    markdownSrc: “# Hello World”
  }
  
  this.onMarkdownChange = this.onMarkdownChange.bind(this);
}

onMarkdownChange(md) {
  this.setState({
    markdownSrc: md
  });
}
```

In the `render` function, add the following to the `Editor` element:

```jsx
<Editor className=”editor” value={this.state.markdownSrc} onChange={this.onMarkdownChange}/>
```

In the `**src/editor.js**` file, bind the `onChange` function of **CodeMirror** to the `onChange` of the parent:

```jsx
constructor(props) {
  super(props);
  
  this.updateCode = this.updateCode.bind(this);
}

updateCode(e) {
  this.props.onChange(e);
}
```

In the `**render**` function, add the following to the `**CodeMirror**` element:

```jsx
<CodeMirror
  value={this.props.value}
  onChange={this.updateCode}
  options={options}
  height=”100%”
/>
```

The `**src/App.js**` file should look like:

```jsx
import React, { Component } from ‘react’;
import logo from ‘./logo.svg’;
import SplitPane from ‘react-split-pane’;
import Editor from ‘./editor.js’;
import ReactMarkdown from ‘react-markdown’;

import ‘./App.css’;

class App extends Component {
  constructor(props) {
    super();
    
    this.state = {
      markdownSrc: “# Hello World”
    }
    
    this.onMarkdownChange = this.onMarkdownChange.bind(this);
  }
  
  onMarkdownChange(md) {
    this.setState({
      markdownSrc: md
    });
  }
  
  render() {
    return (
      <div className=”App”>
        <SplitPane split=”vertical” defaultSize=”50%”>
          <div className=”editor-pane”>
            <Editor className=”editor” value={this.state.markdownSrc} onChange={this.onMarkdownChange}/>
          </div>
          <div className=”view-pane”>
            <ReactMarkdown className=”result” source={this.state.markdownSrc} />
          </div>
        </SplitPane>
      </div>
    );
  }
}

export default App;
```

The `**src/editor.js**` file now looks like this:

```jsx
import React, { Component } from ‘react’;
import CodeMirror from ‘@skidding/react-codemirror’;

require(‘codemirror/lib/codemirror.css’);
require(‘codemirror/mode/javascript/javascript’);
require(‘codemirror/mode/python/python’);
require(‘codemirror/mode/xml/xml’);
require(‘codemirror/mode/markdown/markdown’);
require(‘codemirror/theme/monokai.css’);

class Editor extends Component {
  constructor(props) {
    super(props);
    
    this.updateCode = this.updateCode.bind(this);
  }
  
  updateCode(e) {
    this.props.onChange(e);
  }
  
  render() {
    var options = {
      mode: ‘markdown’,
      theme: ‘monokai’,
    }
    return (
      <CodeMirror value={this.props.value} onChange={this.updateCode} options={options} height=”100%”/>
    );
  }
}

export default Editor;
```

When you reload the application, you should be able to update the editor on the left with text and see the changes on the preview pane on the right.

![Image](https://cdn-media-1.freecodecamp.org/images/YCGmL8j7lBA8FXFxS2lhipmwEtWomD82DJx5)

Full source code can be found on [GitHub](https://github.com/kazuar/mook).

### What’s next?

There are still many things that we need to accomplish here:

1. Save and open files
2. Autosave while editing
3. Toolbar / control over the layout of the panes
4. Backup notes on GitHub, Dropbox and others.
5. Support saving notes in groups or unified in a “notebook”
6. Support math equations in M[edium](https://medium.com/@kazuarous/1e902f8601ca)
7. More amazing features!

I guess that’s what we’ll be doing next time…

![Image](https://cdn-media-1.freecodecamp.org/images/QyZbClSqx8tpBopkHwX7uxeV8TQP429pojtE)

Follow me on [Twitter](http://@kazuarous) for updates about progress, upcoming features, or for any other reason.

### Contributions

You can contribute in any way you want. Any help is appreciated.  
Don’t hesitate to share your suggestions or comments.

Also, if you want to see a feature that you think is important, feel free to ask in the comments below or just open an issue on [GitHub](https://github.com/kazuar/mook).

