---
title: How to Install and Start Using TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-13T08:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-and-begin-using-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/florian-klauer-mk7D-4UCfmg-unsplash-4.jpg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Jonathan Sexton

  TypeScript is one of the current hot topics in web development, and for good reasons.

  It allows us to type cast when declaring variables which means we explicitly set
  the type of data we expect back. Then it throws errors if the re...'
---

By Jonathan Sexton

TypeScript is one of the current hot topics in web development, and for good reasons.

It allows us to type cast when declaring variables which means we explicitly set the type of data we expect back. Then it throws errors if the returned data is not the type we expected to get back, or if a function call has too few or too many arguments. And that's just a sampling of everything it offers.

If you'd like an overview of the data types you will find it helpful to read my [previous article](https://jonathansexton.me/blog/learn-typescript-data-types-from-zero-to-hero/). Reading that article isn't required but it will give you a great understanding of the data types and syntax for TypeScript.

_Before we start, it's important to note that TypeScript can be used in conjunction with a framework/library but it can also be used independent of a framework/library. TypeScript is the default in Angular projects and I have an article in the works about getting started with it._

_Also, this article assumes you have a basic understanding of JavaScript programming._

So, now we're ready to get started with TypeScript and start making use of its awesome features.

Let's dig in!

## Installing TypeScript

There are two main ways to install TypeScript.  The first is through [Visual Studio](https://visualstudio.microsoft.com/vs/) (not to be confused with [Visual Studio Code](https://code.visualstudio.com/?wt.mc_id=DX_841432)) which is an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment).  The 2015, 2017, and I believe 2019 versions come with TypeScript installed already.

This is not the route I'll be covering today since I mainly use Visual Studio Code for all of my needs.

The second way, and the way we'll focus on, is through [NPM](https://www.npmjs.com/get-npm) (Node Package Manager).

If you don't already have NPM and/or [Node](https://nodejs.org/en/) installed (you get NPM when you install Node), now is a great time to do so as it's a requirement for the next steps (and by association a requirement to use TypeScript).

![the node js download page](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-1-1024x550.png)
_The Node download page - it's a good idea to use the LTS version as it's the most stable_

Once you have Node and NPM installed, open your terminal in VS Code and run the following command:

`npm install -g typescript`

Once it's finished installing, you'll see that 1 package has been added. You'll also see a message stating the version of TypeScript that was installed.

This is everything you need to start compiling TypeScript to JavaScript.

Now you're ready to start writing TypeScript!

## Starting A TypeScript Project

Let's create a TypeScript project so we can take advantage of all those great features that come along with using it.

In your editor of choice (I'm using VS Code) let's create an HTML file to be the visual side of our code.  Here's what my basic HTML file looks like:

![html text on a dark background](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-2-1024x376.png)
_Basic HTML boilerplate with some placeholder text_

Honestly, we're just using this HTML so we can have something to look at on the page. What we're really concerned with is using the console.

You'll notice I have `app.js` linked in the head of our `index.html` file.

You're probably saying to yourself _I thought this was an article about TypeScript?_

Well hold your horses, it is. I just want to highlight some of the differences between JavaScript and TypeScript (You'll learn where this file comes from down below).

Below you'll see a simple variable declaration and a console log statement:

![javascript code showing a username variable declaration](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-4.png)
_A simple variable declaration and console log statement_

As a side note, if you want to disable some [ES-Lint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) rules you can place the rules at the top in comments like I've done above.  Or if you want to **completely** disable ES-Lint for that file only you can place `/* eslint-disable */` at the top of the file.

And here is the browser console:

![the console inside of the firefox browser](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-5.png)
_Our userName variable inside FireFox_

Let's pretend that I'm building an application and for the `userName` I expect to always get a string back.  Along the way, I may make a mistake or my data may get mutated from another source.

Now, `userName` is a number :(

![javascript code showing a username variable declaration](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-6.png)
_Now userName is a number!_

And here is the browser console showing the changes to `userName` that we likely didn't want to happen if this were a production application:

![Image](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-7.png)
_The FireFox console showing the results of the variable mutation_

What if the returned `userName` was then passed into another function or used as a piece of a larger data puzzle?

It would not only be a mess to figure out where the mutation occurred (especially if we had a larger application), but also would create an untold number of bugs in our code.

Now, let's try that same experiment in TypeScript.  To do that, we'll need to create a new file with the `.ts` extension to denote a TypeScript file.

I'll name mine `app.ts` to stay consistent with naming conventions and put the same code from our JavaScript file into our new TypeScript file.

![typescript code on a dark background ](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-8.png)
_The same code from our JavaScript copied over into the TypeScript file_

You'll notice that I'm using type casting when declaring my variable now, and I'm explicitly telling TypeScript that this variable should point to a string value only.

You'll also notice that I have an error line under `userName` when I'm reassigning its value.

## Compiling TypeScript With the CLI

To see what this looks like in our console we have to compile it to JavaScript. We do that by running `tsc app.ts` in our VS Code console (you can also run the same command in any terminal as long as you're in the correct directory).

When we run this command it will compile our TypeScript into JavaScript. It'll also generate another file with the same name, only with a `.js` extension.

This is where that `app.js` file came from that I mentioned earlier in the article.

To compile multiple files at once, just provide those names in your command, one after the other: `tsc app.ts header.component.ts`

It's also possible to compile multiple TypeScript files into a single JavaScript file by adding the `--out` flag:

`tsc *.ts --out index.js`

There’s also a watch command which will recompile all of the TypeScript automatically anytime a change is detected. This keeps you from having to run the same command over and over:

`tsc *.ts --out app.js --watch`

Here's the output from that `tsc app.ts` command above:

![Image](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-9-1024x408.png)
_The error in my console_

This error tells us that there's a problem with the reassignment of `userName`. Because we explicitly set our variable to be a string (_even if I hadn't set the variable to a string the error would still occur because TypeScript infers data types_) we cannot reassign it to a number.

This is a great feature because it forces us to be explicit with our variable declarations and saves us from making mistakes that could prove annoying and time consuming. If you expect a particular type of data you should get that data, otherwise you should get an error.

## Using Explicitly Declarative Arrays and Objects

Let's say I'm building a project and instead of manually setting the navigation links, I want to store that info in an array of objects.

I'll expect a specific format for the information that's stored so it's consistent across all of the links.

Here's how I can set a "complex" array in TypeScript:

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-1-1024x51.png)
_An array with a specific format_

On the left side we declare the name of the variable `navLinks`, followed by a colon. At the curly braces is where we start declaring the format of the information we expect in this array.

We're telling TypeScript that we expect this array to contain an object or objects with these property names and types. We expect a `name` which is a string, a `link` which is a string, and an `alt` which is also a string.

As with other [data types](https://jonathansexton.me/blog/learn-typescript-data-types-from-zero-to-hero/), if we deviate from the format we established for this variable, we run into errors.

Here we tried to add a new entry that was blank and we got the following error:

`Type '{}' is missing the following properties from type '{ name: string; link: string; alt: string; }' : name, link, <sub>alt ts(2739)</sub>`

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-3-1024x97.png)

We get similar errors if we try to add another entry with the wrong type of information:

`{ name: 'Jonathan', link: 15, alt: false }`  ❌

`{ name: ['Jon','Marley'], link: `https://link123.net`, alt: null }`  ❌

`this.navLinks[0].img = '../../assets/img'` ❌

`this.navLinks[0].name = 'Barnaby'`✔️

You get the idea though. Once we establish the format, TypeScript will hold us to that format and inform us if/when we deviate from it with an error.

Also, here's a few ways to define an array:

`const arr1: Array<any> = ['Dave', 35, true];` _// will allow us to have any number of elements with any type_

`const people: [string,string,string] = ['John', 'Sammy', 'Stephanie'];` _// will throw an error if more than 3 strings or any non string elements appear in the array_

`const people: Array<string> = ['Jimmy', 'Theresa', 'Stanley'];` _//will allow us to have any number of only string elements in our array_

Objects work much the same way as arrays do in TypeScript. They can be explicitly defined with set types or you can let TypeScript do all the inferring. Here's a basic example of an object:

`const person: {name:string, address: string, age: number} = {name: 'Willy', address: '123 Sunshine Ln', age: 35}`

Again, on the left side we're declaring person as the variable name with the first set of curly braces defining the format we want our data to be in.

It is important to note that in objects, the order we define our properties in does not have to match the order of the format:

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-5.png)
_The properties do not have to match the order in which they were defined_

## Functions, Parameters & Arguments

Some of the greatest benefits you'll see in TypeScript come when using functions.

Have you ever built a function to do a specific task only to find out it's not working as you intended?

While using TypeScript it won't be because you didn't get/send the correct type of data or use the correct number of parameters/arguments.

Here's a great example:

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-1024x454.png)
_A TypeScript function that should return a number_

In our function we expect to receive 3 arguments when `calculator` executes. However, if we receive the wrong number of arguments (too few or too many) TypeScript will give us a nice error:

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-4.png)
_The error we get when calling a function with the incorrect amount/type of arguments_

Likewise, if we receive the wrong type of data when executing this function TypeScript will generate an error and the function will not run.

`calculator('12', '11', 'add) ;` ❌

Now you may be saying to yourself _'So what? That's all well and good but it doesn't seem like that's a huge deal.'_ But imagine that your application is dozens and dozens of files with many layers of abstractions.

A great example of this would be an Angular application with services, data models, multilevel components, and all the dependencies that go along with that. It becomes increasingly difficult to pinpoint where an error is coming from when your application gets to be large.

## That's All

Hopefully you can see the benefits of TypeScript now. There are plenty more than those I have outlined here and I encourage you to read the documentation if you want to find more.

You can find this article and others like it on my [blog](https://jonathansexton.me/blog). I'd love for you to stop by!

While you’re there why not sign up for my **Newsletter**  –  you can do that at the top right of the main blog page. I promise I’ll never spam your inbox and your information will not be shared with anyone/site. I like to occasionally send out interesting resources I find, articles about web development, and a list of my newest posts.

If you haven’t yet, you can also connect with me on social media! All of my links are also at the top right of that page as well. I love connecting with others and meeting new people so don’t afraid to say hi. ?

Have an awesome day, friend, and happy coding!

