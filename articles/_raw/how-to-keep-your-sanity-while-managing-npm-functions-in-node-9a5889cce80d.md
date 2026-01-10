---
title: How to keep your sanity while managing NPM & functions in Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T22:03:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-sanity-while-managing-npm-functions-in-node-9a5889cce80d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h4bO2japPTG77hSqSBf12g.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Ted Gross

  Introduction

  In my career, I have trolled through hundreds of articles dealing with NodeJS and
  many full examples of NodeJS, either in the typical MEAN stack, or specific examples
  using various NPM modules. An integral part of writing in...'
---

By Ted Gross

### Introduction

In my career, I have trolled through hundreds of articles dealing with NodeJS and many full examples of NodeJS, either in the typical MEAN stack, or specific examples using various NPM modules. An integral part of writing in NodeJS is using NPM or Yarn to install libraries which do certain things. To give an example which all Node programmers will know of, there is the Express-Passport-JWT-Mongo NPM libraries.

We all know the stack as well will not stop there. Express will probably also require installation of “body-parser” and “cors”, and possibly sub Express NPM modules. Don’t forget Lodash, Underscore, Moment…and the list goes on and on as there are thousands upon thousands of NPM modules to make use of.

### Maintaining NPM Module Structure In A Sane Way

Normally, when you review code snippets or systems in a search, or write your own, each file will contain the modules required for that specific file. The following code snippets are taken from real code snippets available on the net:

* _Please note for these examples the ‘var’ should be replaced with ‘let’ or ‘const’ depending upon what is being done._

```
var express = require('express');var path = require('path');var favicon = require('serve-favicon');var logger = require('morgan');var bodyParser = require('body-parser');
```

Then another file will may start with:

```
var morgan = require('morgan');var mongoose = require('mongoose');var passport = require('passport');
```

And a third file will start with:

```
var mongoose = require('mongoose');var Schema = mongoose.Schema;var bcrypt = require('bcrypt-nodejs');
```

You can imagine the rest of the files and there are usually many, even in micro-services, of how they look.

What makes this practice even worse, is that you can find _‘require’_ in the middle of a file as well. In other words, code can go along for many lines and suddenly the coder will introduce yet another NPM module. This usually happens with inexperienced or non-organized coders, yet it is an incredibly common practice and wreaks havoc with understanding and debugging code.

The problem as you can well see, is this plethora of NPM modules, sooner rather than later will cause a huge headache in maintaining a system, especially within a team of programmers, who need to know what has already been installed and is available and what has not.

Node programmers are notorious for installing, testing and discarding NPM modules, (I admit to being one of them). The question of course is, how to maintain sanity, order, and most importantly control over installed NPM modules and a common method of calling them.

Fortunately, Node allows for a fairly simple method of dealing with these problems. The following is a method I use for back-end teams dealing with the stack. It keeps things orderly, easy to find, and everyone knowing what is installed and not installed in the system. It also allows for clean uninstalls when an NPM module is no longer needed.

If you are a “functional” programmer, in other words not everything must be OOP with classes and “this->”, the following may actually allow you to reconsider a whole new method of using functions and stored procedures.

My suggestion would be to create a directory under your root project directory. I usually call this directory _“env”_, but you can call it whatever you like. _“env”_ is where I keep all my function libraries and stored procedures including, if used, the environment file needed by the _“dotenv”_ NPM library. (The environment variables can be held anywhere, they do not need to be held in the root project directory. Yet a discussion about environment variables and “dotenv” is for another article.) In other words, your _“env”_ directory should only contain files which should be required or accessed by parts of the systems.

In the _“env”_ directory off the root, create a file called _“helperMods.js”_. (Again, you can call this file whatever you like.) Additionally, if your system is going to use many NPM modules, or those just used for development purposes (such as “chalk”), you my want to divide this into two or three files. However, for our simple example we will use one file.

```
module.exports = {    request: require("request"), //used for request http    fs: require('fs'),    path: require('path'),    chalk: require('chalk'),    moment: require('moment'),    express: require('express'),    session: require('express-session'),    eJWT: require('express-jwt'),    bodyParser: require('body-parser'),    cors: require('cors'),    passport: require('passport'),    passportLocal: require('passport-local'),    crypto: require('crypto'),    dotenv: require('dotenv'),    jwt: require('jsonwebtoken'),    jwtclaims: require('jwt-claims'),    redis: require('redis'),    mongodb: require('mongodb'),    mongoose: require('mongoose'),    assert: require('assert'),    shortid: require('shortid'),    badWords: require('bad-words'),    enum: require('enum'),    errorHandler: require('errorhandler'),    morgan: require('morgan')};
```

First, install an NPM module you want to use, for example:

```
npm i jsonwebtoken --s
```

Now decide upon a caller for that module. For instance, in the above file, jsonwebtoken is defined first as “jwt”. Then require the actual module you installed. So, the line will read:

```
jwt: require('jsonwebtoken'),
```

(The comma at the end is due to the JSON format of the file.)

The things to be aware of in this file are as follows:

1. Keep your calling names distinct.

2. Despite what you see above, I would alphabetize according to calling names or NPM module alphabet order.

3. Remember, as well, even if it is a built-in NodeJS module such as “crypto” (yes “crypto” is now finally part of the internal NodeJS) or “request” you need to require it.

4. Indeed, if you do require many “native” modules you can separate these into files which can all be called from the first few lines in each file you run.

5. Remember, “namepaces” will protect you from loading a module twice into memory. Once you call that module in your require, even if you call it again from another file, it will not take up more or “duplicate” memory.

Once you have your file setup, the method of calling from any file is fairly easy.

Each file you set up or use, should start with two (or more) lines depending upon the modules you need to require. For example:

```
"use strict";const helpMods = require("./env/helperMods");
```

Those above lines above will require all the modules in your file. It then becomes a simple method to call them using dot notation.

For instance, if you need to call the badWords module, your dot notation will look like this:

```
helpMods.badWords.(do whatever needs to be done normally here)
```

If you forget the helpMods, an IDE such as WebStorm will throw you out an error warning that the module has not been required which will immediately tell you that you forgot the correct dot notation or that you have forgotten to include that module in your main exports file.

### Maintaining User Functions In A Sane Way

Again, when looking at many examples you will find functions within the file. Many times, these functions are a “one-off”, in other words specifically used for a very specific situation which will not repeat itself. Or will it?

In years of experience I have learned that once you have a function running correctly, there is a good chance you will use it again from another file. Perhaps the parameters may be different, or you may need to add to the parameters it receives (easily done with a good IDE), _but chances are you will use it again_.

For this reason, I maintain a set of function libraries in the _“env”_ directory. I usually try to divide these functions into logical structures. For instance, all CRUD and other DB activities will go into one function library file. All security functions will go into another. This is just a suggestion.

What this type of programming does:

* Gives you and your team control over the environment.
* Reduces the requires of specific modules over and over again in each file.
* Grants immediate access to NPM modules which you may have not thought you needed in a file.
* Uses standard dot notation, without any workarounds.
* Allows you to divide up your structure in any way you deem fit, including calling functions in function files etc. in this manner. However, a function file is not written in the same type of structure. You will require:

```
"use strict";const helpMods = require("./env/helperMods");
```

**And any other module files you decided upon.**

For this example we will use a few functions, separated into order for our system Then write and define all functions, with callbacks, promises or async/await. Let us call the file _“generalFuncs.js”_ Each function though does have a name.

```
Function(getExactTime(passed params go in here){/do stuff in here}
```

```
Function(logFile(passed params go in here){//do stuff in here}
```

Add as many functions as you need to this file. **So, at the end of the function file you should write:**

```
module.exports = {getExactTime, logfile, HTMLResponse, getRemoteConnect, doesKeyExist, generateUniqueKey, restartAll, createDateFromString};
```

The above will allow these functions to be available in dot.notation to any file you add the following:

```
"use strict";const helpMods = require("./env/helperMods");const generalFuncs = require (../env/generalFuncs");
```

Now when you use the function “getExactTime” you access it as follows:

```
generalFuncs.getExactTime(whatever is needed goes here);
```

As an added plus in any good IDE, you will be able to see which functions are not ever exported as they will never be required in any system.

### Conclusion

The above methods will allow you to maintain control and understanding of what is being used in the system. The function files will allow refactoring of functions along the route whenever it needs to be done. Dot notation will allow you to call the modules or functions in a simple orderly fashion.

It does add a further level into your directory structure which may drive you crazy accessing them from other sub-directories, unless you know exactly how Node handles directory structures (which you should know anyway). **_If you would rather not do this you can leave them in your root app directory._**

None of this, by the way, will interfere with GitHub Versions or version controls. Indeed, checking, refactoring and testing will become that much easier. Single lines can be marked only for development systems others for production systems.

If you can wrap your ahead around this coding style, at least in terms of modules and possibly functions, you will find your code cleaner, easier to read, available to the entire team & easier to refactor.

________________________________________________________

About the Author: Ted Gross served as a CTO for many years with an expertise in database technology, NodeJS, MongoDB, Encryption, PHP and OOP. He has expertise in Virtual World Technologies & Augmented Reality. He has also published many articles on technological topics especially on Big Data & Chaos Theory (in professional journals and online @ Medium & LinkedIn). [**He is also an author of literary fiction, children’s books and various non-fiction articles**](http://amazon.com/author/tedgross). His short story collection, [_“Ancient Tales, Modern Legends”_](http://www.amazon.com/Ancient-Tales-Modern-Legends-Collection/dp/1469901714) has received excellent reviews.

Ted can be reached via email: tedwgross@gmail.com; [Twitter](https://twitter.com/tedwgross) (@tedwgross); [LinkedIn](http://il.linkedin.com/in/tedwgross); [Medium](https://medium.com/@tedwgross)

