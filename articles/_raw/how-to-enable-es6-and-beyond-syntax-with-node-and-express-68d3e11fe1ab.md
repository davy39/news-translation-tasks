---
title: How to enable ES6 (and beyond) syntax with Node and Express
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-23T16:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-enable-es6-and-beyond-syntax-with-node-and-express-68d3e11fe1ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VAo90seDRpFYq7utRkPEJg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jonathan Cunanan

  Have you ever tried to write front-end apps using ES6 syntax, but then  when you
  decided to learn back-end development with Node.js and Express,  you realized that
  you can’t use stuff like import from and  export default?  If so, ...'
---

By Jonathan Cunanan

Have you ever tried to write front-end apps using ES6 syntax, but then  when you decided to learn back-end development with Node.js and Express,  you realized that you can’t use stuff like `import from` and  `export default`?  If so, you came to the right place! This is step by step guide on how  to configure your dev and prod environments, setup scripts, and as a  bonus we’ll learn how to add tests!

### Table of Contents / Summary of topics

* [How does it work?](#heading-how-does-it-work-a-high-level-view-of-what-we-need)
* [Prerequisites](#heading-prerequisites)
* [Installing express](#heading-installing-express)
* [Setting up scripts](#heading-setting-up-scripts)
* [Bonus](#heading-bonus-add-tests)
* [TL;DR](#heading-tldr)

### How does it work? A high level view of what we need

To enable a front-end development-like experience while developing back-end apps, here’s a high level view of the processes happening to your project.

#### Code Transpiler from ES6+ to ES5

We need a package that translates ES6 and above syntax to ES5 code. ES5 code is the JS syntax style that is readable to node.js, such as `module.exports` or `var module = require('module')` . Note that in today’s time, almost 99% of ES6+ syntax can be used in Node.js. This is where the package called [_babel_](https://babeljs.io/) shines.

Babel takes a js file, converts the code in it, and outputs into a new file.

#### Script that removes files

Whenever we change something in our code, we feed it to the transpiler, and it outputs a fresh copy every-time. That’s why we need a script that removes files before the fresh transpiled copy enters. And for that, there’s an existing package called [rimraf](https://www.npmjs.com/package/rimraf). Rimraf deletes files. We’ll demonstrate that later.

#### Watcher of file changes

When coding in Node.js, automatic restart of our server doesn’t come out of the box just like when doing a project made on-top of create-react-app or vue-cli. That’s why we’ll install a package called [nodemon,](https://www.npmjs.com/package/nodemon) that executes something whenever we change a file in our code. We can leverage nodemon to restart our server every-time a file is changed.

So that’s the high-level view of how it works under the hood. With that, let’s start on how should we setup or project.

### Prerequisites

Before we begin, we need some things setup first.

1. Make sure you have Node.js and npm installed. I recommend installing their latest LTS or current stable version. You can install it via [Node.js Source](https://nodejs.org/en/download/) or [NVM](https://github.com/creationix/nvm) (Node Version Manager)
2. Basic knowledge of terminal commands. Most of the commands are in the tutorial anyway so you don’t have to worry about them.
3. Make sure you have your terminal open and your favorite text editor installed.

That’s it, we’re good to go!

### Installing Express

Using the Express generator, we will create a new project with generated code, move some files, and convert some code to ES6 syntax. We need to convert it at this early stage because we need a way to verify if our ES6 code works.

#### Project Setup

Run this command in your terminal. You can name `your-project-name` with the name you like. `--no-view` flag means that we won’t be using any templating engine such as handlebars, ejs, or pug, for our skeleton Express app.

`npx express-generator your-project-name --no-view`

After creating your app, you need to go to your app directory. For Windows Powershell and Linux terminals, use:

`cd your-project-name`

Next, open the text editor you like. For me, I just use VSCode so I just have my terminal and text editor open at the same time. But you can use any text editor you want.

#### Installing Packages and Moving and Deleting Files

After we have the generated project ready, we need to `install` the dependencies and move some folders. Run this command to install Express and other packages.

npm install

While you’re waiting for the dependencies to install, follow these steps.

* create a `server/` folder
* Put `bin/` , `app.js` , and `routes/` inside the `server/` folder.
* Rename `www`, found in `bin` to `[www.js](http://www.js)`
* Leave `public/` folder at your project root.

Your file structure will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image.png)
_This is how our file structure looks like. `public/` folder is at the root, and all the `.js` files are inside `server/` folder._

Now, because we modified the file structure, our start server script won’t work. But we’ll fix it along the way.

#### Converting to ES6 code

Converting the generated code to ES6 is a little bit tedious, so I’ll just post the code here and feel free to copy and paste it.

Code for `bin/www.js`:

Now, because we modified the file structure, our start server script won’t work. Here’s what we’ll do to fix it. On your package.json file, rename start script to `server`found in a JSON Object called `"scripts"`

```json
// package.json
{
  "name": "your-project-name",
  // ....other details
  "scripts": {
    "server": "node ./server/bin/www"
  }
}
```

You’ll see that we changed the file path from `./bin/www`to `./server/bin/www` because we moved files to `server/`. We’ll use start script later on.

Try it! Try running the server by typing `npm run server` on your terminal, and go to `localhost:3000` on your browser.

#### Converting the top level code to use ES6 imports

Converting the generated code to ES6 is a little bit tedious, so I’ll just post the code here and feel free to copy and paste it.

Code for `bin/www.js`:

```json
// bin/www.js
/**
 * Module dependencies.
 */
import app from '../app';
import debugLib from 'debug';
import http from 'http';
const debug = debugLib('your-project-name:server');
// ..generated code below.
```

Almost all of our modifications are only at the top and bottom of the files. We are leaving other generated code as is.

Code for `routes/index.js` and `routes/users.js`:

```json
// routes/index.js and users.js
import express from 'express';
var router = express.Router();
// ..stuff below
export default router;
```

Code for `app.js`:

```json
// app.js
import express from 'express';
import path from 'path';
import cookieParser from 'cookie-parser';
import logger from 'morgan';
import indexRouter from './routes/index';
import usersRouter from './routes/users';
var app = express();
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, '../public')));
app.use('/', indexRouter);
app.use('/users', usersRouter);
export default app;
```

In `app.js` , because we left `public/` at the project root , we need to change the Express static path one folder up. Notice that the path `'public'` became `'../public'` .

`app.use(express.static(path.join(__dirname, '../public')));`

Okay we’re done with converting the code! Let’s setup our scripts now.

### Setting up Scripts

In setting up scripts, each script performs a different role. And we reuse each npm script. And for our development and production environments, they have a different configuration. (Almost identical, you’ll see later) That’s why we need to compose our scripts so we can use them without repeatedly typing the same stuff all over again.

#### Install `npm-run-all`

Since some terminal commands won’t work on windows cmd, we need to install a package called `npm-run-all` so this script will work for any environment. Run this command in your terminal project root.

`npm install --save npm-run-all`

#### Install babel, nodemon, and rimraf

Babel is modern JavaScript transpiler. A transpiler means your modern JavaScript code will be transformed to an older format that Node.js can understand. Run this command in your terminal project root. We will be using the latest version of babel (Babel 7+).

Note that Nodemon is our file watcher and Rimraf is our file remover packages.

`npm install --save [@babel/core](http://twitter.com/babel/core) [@babel/cli](http://twitter.com/babel/cli) [@babel/preset-env](http://twitter.com/babel/preset-env) nodemon rimraf`

#### Adding transpile script

Before babel starts converting code, we need to tell it which parts of the code to translate. Note that there are a lots of configuration available, because babel can convert a lot of JS Syntaxes for every different kinds of purpose. Luckily we don’t need to think about that because there’s an available default for that. We are using default config called as preset-env (the one we installed earlier) in our package.json file to tell Babel in which format we are transpiling the code.

Inside your `package.json` file, create a `"babel"` object and put this setting.

```
// package.json
{  
  // .. contents above
  "babel": {
    "presets": ["@babel/preset-env"]
  },
}
```

After this setup we are now ready to test if babel really converts code. Add a script named transpile in your `package.json`:

```
// package.json
"scripts": {
    "start": "node ./server/bin/www",
    "transpile": "babel ./server --out-dir dist-server",
}
```

Now what happened here? First we need to run the cli command `babel` , specify the files to convert, in this case, the files in `server/` and put the transpiled contents in a different folder called `dist-server` in our project root.

You can test it by running this command

`npm run transpile`

You’ll see a new folder pop up.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-1.png)
_New folder popped up called dist-server because of the script we ran._

Yay it worked! ✅ As you can see, there’s a folder that has the same folder structure as our server folder but with converted code inside. Pretty cool right? Next step is to run try if our server is running!

#### Clean script

To have a fresh copy every-time we transpile code into new files, we need a script that removes old files. Add this script to your package.json

```
"scripts": {
  "server": "node ./dist-server/bin/www",
  "transpile": "babel ./server --out-dir dist-server",
  "clean": "rimraf dist-server"
}
```

This npm script that we made means it removes the folder `dist-server/`

Now to combine transpile and clean, add a script called `build` , which combines the two processes.

```
// scripts
"build": "npm-run-all clean transpile"
```

#### Running dev script

Now we have a build script, we need to run our dev server. We’ll add a script called `dev` in our package.json. This takes care of setting our Node Environment to “development”, removing old transpiled code, and replacing it with a new one.

```
"scripts": {
  "build": "npm-run-all clean transpile"
  "server": "node ./dist-server/bin/www",
  "dev": "NODE_ENV=development npm-run-all build server",
  "transpile": "babel ./server --out-dir dist-server",
  "clean": "rimraf dist-server"
}
```

Note here that we’ve changed again the file we are running on our server script. We’re running the file-path with the transpiled code, found in `dist-server/`.

#### Adding prod scripts

If we have a dev script that sets the Node Environment to development, we have a `prod` script that sets it to “production.” We use this configuration when we are deploying. (Heroku, AWS, DigitalOcean, etc..) We’re now adding again our start script and prod script in our package.json again.

```
"scripts": {
  "start": "npm run prod"
  "build": "npm-run-all clean transpile"
  "server": "node ./dist-server/bin/www",
  "dev": "NODE_ENV=development npm-run-all build server",
  "prod": "NODE_ENV=production npm-run-all build server",
  "transpile": "babel ./server --out-dir dist-server",
  "clean": "rimraf dist-server"
}
```

We set `start` script default to prod because start script is being used always by deployment platforms like AWS or Heroku to start a server.

Try either by running `npm start` or `npm run prod` .

```
// package.json
...
"nodemonConfig": { 
  "exec": "npm run dev",
  "watch": ["server/*", "public/*"],
  "ignore": ["**/__tests__/**", "*.test.js", "*.spec.js"]
},
"scripts": { 
  // ... other scripts
  "watch:dev": "nodemon"
}
```

#### How about auto-restarting the server whenever a file change?

One final script, in order to complete our development setup. We need to add a file watcher script that runs a command whenever a change is made in a file. Add a JSON Object named “nodemonConfig” in your package.json. This is where we store what we tell the watcher what to do when a file changes.

Also, add a script called `watch:dev` in your package.json

```
// package.json
...
"nodemonConfig": { 
  "exec": "npm run dev",
  "watch": ["server/*", "public/*"],
  "ignore": ["**/__tests__/**", "*.test.js", "*.spec.js"]
},
"scripts": { 
  // ... other scripts
  "watch:dev": "nodemon"
}
```

Nodemon config contains settings related to

* Which command to run whenever a file changes, in our case `npm run dev`
* What folders and files to watch
* And which files to ignore

More about configuration of nodemon [here](https://github.com/remy/nodemon#config-files).

Now that we have our file watcher, you can now just run `npm run watch:dev` , code, and save your file. and whenever you go to `localhost:3000` , you’ll see the changes. Try it out!

### Bonus: Add tests!

To add tests in our project, simply install [Jest](https://www.npmjs.com/package/jest) from npm, add a few config, and add a script called `test` in our package.json

`npm i -D jest`

Add an object called “jest”, and a test script in your package.json

```
// package.json
...
"jest": { 
  "testEnvironment": "node"
},
"scripts": {
  // ..other scripts 
  "test": "jest"
}
```

Try it out, make a file sample.test.js, write any tests, and run the script!

`npm run test`

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-2.png)
_Sample Screenshot of running npm run test._

### TL;DR

Here are the simplified steps for how to enable ES6 in Node.js. I’ll also include the repo so you can copy and inspect the whole code.

* Make a new project using `express your-project-name` terminal command.
* Move the `bin/`, `routes/` and `app` into a new folder called `src/` , and convert the code into ES6. Also don’t forget to rename `bin/www` to `[www.js](http://www.js)`
* Install all the dependencies and devDependencies

```
npm i npm-run-all @babel/cli @babel/core @babel/preset-env nodemon rimraf --save
npm i -D jest
```

* Add these scripts to your package.json

```js
"scripts": { 
  "start": "npm run prod", 
  "build": "npm-run-all clean transpile", 
  "server": "node ./dist-server/bin/www", 
  "dev": "NODE_ENV=development npm-run-all build server", 
  "prod": "NODE_ENV=production npm-run-all build server", 
  "transpile": "babel ./server --out-dir dist-server", 
  "clean": "rimraf dist-server", 
  "watch:dev": "nodemon", 
  "test": "jest" 
}
```

* Put configurations for babel, nodemon, and jest in your package.json

```js
"nodemonConfig": {
  "exec": "npm run dev",
  "watch": [ "server/*", "public/*" ],
  "ignore": [ "**/__tests__/**", "*.test.js", "*.spec.js" ] 
}, 
"babel": { 
  "presets": [ "@babel/preset-env" ]
},
"jest": {
  "testEnvironment": "node"
},
```

* Test your scripts by running `npm run your-script-here`
* You’ll see the [complete repo at my github](https://github.com/jcunanan05/express-es6-sample/tree/master)

### Notes and disclaimers

Note that this setup may not be proved ideal for all situations, specially for big projects. (like 1k files of code). Transpiling step and deleting might slow down your development environment. Plus, ES Modules, is almost coming to node. But, nevertheless, this is a good eductational material to understand how transipiling runs under the hood like when we are developing front-end apps :)

### Conclusion

All right! I hope you learned a lot. Thank you for reading this far.

Happy Coding!

[Check the full repo here.](https://github.com/jcunanan05/express-es6-sample/tree/master)

This article is published in freeCodecamp news.

[? Twitter](https://twitter.com/devJonathanC_) - [? freeCodeCamp](https://www.freecodecamp.org/jcunanan05) -  [? Portfolio](https://jonathancunanan.com) - [⚛️ Github](https://github.com/jcunanan05)

