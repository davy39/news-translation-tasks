---
title: How to use JavaScript libraries in Angular 2+ apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-12T09:57:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-javascript-libraries-in-angular-2-apps
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_FDIQCYA3BNp9Ek-tqGeQjA-1--1.png
tags:
- name: Angular
  slug: angular
- name: angular2
  slug: angular2
- name: angular6
  slug: angular6
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Mohammad Kermani\nDo you remember when you were learning AngularJS (version\
  \ 1), and tutorials kept telling you that you don’t need to add JQuery into your\
  \ project? \nThat hasn't changed - you don’t need to add JQuery to your Angular\
  \ 2+ project. But ..."
---

By Mohammad Kermani

_Do you remember when you were learning AngularJS (version 1), and tutorials kept telling you that you don’t need to add JQuery into your project?_ 

That hasn't changed - you don’t need to add JQuery to your Angular 2+ project. But if, for any reason, you might need to use some JavaScript libraries, you need to know how to use them in Angular. So, let’s get started from zero.

_I’m going to add_ [_underscore.js_](http://underscorejs.org/) _to a project and show you how it works._

### 1. Create a new project using Angular CLI

If you don’t already have CLI installed on your machine, [install it](https://cli.angular.io/). After installation, create a new project (if you don’t already have one).

ng new learning

Now you will have a new Angular project named “**learning**”.

### 2. Install the package into your project

Go to the project we just made:

cd learning

Use your preferred package manager to install the library you’re going to use; I use `npm` to install `underscore.js`.

npm install --save underscore

### 3. Import the library into Angular (TypeScript)

We are writing code in TypeScript, and we should follow its rules. TypeScript needs to understand `underscore.js`.

As you might know, TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. TypeScript has its own syntax, function and variables can have defined types. But when we are going to use an external library such as underscore, we need to declare type definitions for TypeScript.

In JavaScript, the type of arguments are not important and you will not get an error while you’re writing code. But TypeScript won’t let you to give an array to a function that accepts a string as input. Then here is the question: should we rewrite the `underscore.js` in TypeScript and define types there?

Of course not - TypeScript provides declaration files _(*.d.ts)_ which define types and standardize a JavaScript file/libraries for TypeScript.

Some libraries include a typing file and you don’t need to install TypeScript’s type destination for them. But in case a library does not have a  `.d.ts` file, you need to install it.

We just need to find and import `underscore.js` type definition file. I suggest that you use [Type Search](https://microsoft.github.io/TypeSearch/) to find the declaration file for the libraries you need.

Search for `underscore` in [Type Sceach](https://microsoft.github.io/TypeSearch/) and it redirects you to[types/underscore](https://www.npmjs.com/package/@types/underscore). Install the declaration file using the following command:

`npm install --save @types/underscore`

### 4. Import type declaration into Angular app

Let’s say you’re going to use underscore in your `app.component.ts` file. Open the `app.component.ts` by your IDE and add the following code in the top of the file:

```
import * as _ from 'underscore';/*** OR simply:* import 'underscore';*/
```

The TypeScript in that component now understands `_` and it easily works as expected.

### Question: How to use a library which does not have type definition (*.d.ts) in TypeScript and Angular?

Create it if the `src/typings.d.ts` does not exist. Otherwise open it, and add your package to it:

```
declare var 
```

In your TypeScript, now you need to import it by the given name:

```
import * as yourPreferedName from 'yourLibrary';yourPreferedName.method();
```

### Conclusion

To wrap up, let’s make a simple example to see a working example of `_`. Open `app.component.ts` and inside the `appComponent` class write a `constructor` which returns the last item of an array using underscore's `_.last()` function:

```
...
import * as _ from 'underscore';
...
export class AppComponent {
  constructor() {
    const myArray: number[] = [9, 1, 5];
    const lastItem: number = _.last(myArray); //Using underscore
    console.log(lastItem); //5
  }
}
```

If you open your Angular app now, you will get `5` in the console, which means we could correctly add `underscore` into our project and it’s working as expected.

You can add any JavaScript libraries to your project just by following the same steps.

---

You can follow [me](https://medium.com/@kermani) for more articles on technology and programming.

