---
title: Why would you NOT use TypeScript?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-02T00:22:26.000Z'
originalURL: https://freecodecamp.org/news/why-would-you-not-use-typescript-67d0baa3eaca
coverImage: https://cdn-media-1.freecodecamp.org/images/0*p8qXhijgzkr7h2wT.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Creamer

  In a world where JavaScript is arguably the most popular tool for building software
  these days, it seems like it’s everywhere now. With Node.js, it’s on the backend,
  with Electron it’s native on your machine, with React Native, it...'
---

By Jonathan Creamer

In a world where JavaScript is arguably the [most popular](https://insights.stackoverflow.com/survey/2017#technology) tool for building software these days, it seems like it’s everywhere now. With Node.js, it’s on the backend, with Electron it’s native on your machine, with React Native, it’s native on your phone. There’s no doubt that JavaScript is nothing but at least pervasive across so many ecosystems.

So, the next question I have is, if JavaScript is so popular, then TypeScript by nature of what is is, also should be popular. After all, in case you didn’t realize it…

> _Any JavaScript you can possibly write which is at least ECMA stage 3 is valid TypeScript._

![Image](https://cdn-media-1.freecodecamp.org/images/0*TsjAfKA-gbrLIXeu.gif)

### VSCode

First and foremost, if you’re not using Visual Studio Code to write JavaScript, you should be, so [go get it](https://code.visualstudio.com/), and also go get [all this stuff](http://vscodecandothat.com/) from [Burke Holland](https://twitter.com/burkeholland).

Under the covers, the TypeScript compiler will do a lot of amazing things for you without you even having to think twice about it. The reason it’s able to do this is, VS Code is running your JavaScript through the TypeScript compiler, whether you realize it or not.

[**Microsoft/TypeScript**](https://github.com/Microsoft/TypeScript/wiki/JavaScript-Language-Service-in-Visual-Studio)  
[_TypeScript is a superset of JavaScript that compiles to clean JavaScript output._github.com](https://github.com/Microsoft/TypeScript/wiki/JavaScript-Language-Service-in-Visual-Studio)

On top of that, it also uses something called Automatic Type Definitions using the phenomenal [Definitely Typed](https://github.com/DefinitelyTyped/DefinitelyTyped) library of type definitions to automatically download types for thousands of popular JavaScript libraries.

### From JS to TS, TypeScript’s got you

In the following example, we’re simply formatting a price string.

It could be easy to forget that if pass a string here, this function will asplode because `toFixed` doesn't exist on a string.

Simply adding types can save you runtime bugs…

But, there’s even better news…

![Image](https://cdn-media-1.freecodecamp.org/images/0*p8qXhijgzkr7h2wT.jpg)

You may or may not already be a big user of JSDoc, but if you are, you will be pleased as punch to know that as of a recent version of TypeScript, you can add `// @ts-check` to the top of a JavaScript file, and get typechcking in it!

![Image](https://cdn-media-1.freecodecamp.org/images/0*nJs9Zs2Uib62uz7_.png)

Here’s more info about what all you can do with JSDoc… [https://github.com/Microsoft/TypeScript/wiki/JSDoc-support-in-JavaScript](https://github.com/Microsoft/TypeScript/wiki/JSDoc-support-in-JavaScript)

With VSCode you can enable full type typechecking with the following User Settings option…

```
"javascript.implicitProjectConfig.checkJs": true
```

You can add a globals.d.ts file and declare things under the global namespace if you have any interfaces you want to define across the whole project.

```
declare global {  interface IFormatPrice {}}
```

### React

Cool thing is, TypeScript also supports React out of the box by adding the following to your tsconfig…

```
{ "jsx": "react" }
```

Now for the real fun…

![Image](https://cdn-media-1.freecodecamp.org/images/0*5jBFBOXnVAi_A9JB.jpeg)

PropTypes are a great way to catch runtime React bugs. But the frustrating thing about them is, you don’t know if something is broken generally until your app builds, the browser or hot loading reloads, and you see a cryptic red error message in the console.

Wouldn’t it be nice to just catch that bug while working on the component?

Now, check this out…

![Image](https://cdn-media-1.freecodecamp.org/images/0*iI_CtUfjUjoLqTZ1.gif)

It’s amazing to be able to get intellisense on props. You can start typing, or in VSCode hit Control + Space to pull open the Intellisense menu.

You can even get intellisense on React classes as well…

![Image](https://cdn-media-1.freecodecamp.org/images/0*4aH83IUb9UbmjI8D.png)

### Conclusion

Whether or not you decide to go full on TypeScript, it’s clear you can see many benefits even if you stick with pure JavaScript.

_Originally published at [jonathancreamer.com](http://jonathancreamer.com/why-would-you-not-use-typescript/) on February 2, 2018._

