---
title: Learn TypeScript Data Types – From Zero to Hero
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-25T09:58:40.000Z'
originalURL: https://freecodecamp.org/news/learn-typescript-data-types-from-zero-to-hero
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/road-trip-with-raj-o4c2zoVhjSw-unsplash-1.jpg
tags:
- name: Angular
  slug: angular
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Sexton

  It''s all the rage these days in the world of web development - TypeScript.  I''d
  wager by now you have heard about it, even in passing.  But, if you haven''t or
  if you''re just curious then you''ve come to the right place my friend!

  I''...'
---

By Jonathan Sexton

It's all the rage these days in the world of web development - [TypeScript](https://www.typescriptlang.org/).  I'd wager by now you have heard about it, even in passing.  But, if you haven't or if you're just curious then you've come to the right place my friend!

I'm currently learning TypeScript in conjunction with Angular (an article on this is in the works, so stay tuned!) because it's what our web application is built in at work.  I decided to write up something easy and simple to follow so you can get up and running with TypeScript data types.

I'll break this article up into two posts for simplicity - the first will be a brief overview of what TypeScript is, the data types, and some supporting examples.  The second article will be focused on getting TypeScript installed and running locally on your machine.

## What Is It?

Before we start, here's a super condensed description of TypeScript in my own words.  It's a **_superset_** of JavaScript - which essentially means it's a form of JavaScript that gives you certain benefits along with all of the greatness included in 'vanilla' JavaScript.  It's an open source language written and maintained by Microsoft.

TypeScript transpiles to JavaScript and will run in any environment that native JavaScript runs.  You may use TypeScript for both front end and back end applications.

It's written just like JavaScript, with a few exceptions that we'll go over soon.  Here's an example of some TypeScript:

![code showing typescript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image.png)
_TypeScript in all it's glory_

Try not to focus on all of the colons and extra stuff you see above, we'll dig into that below.  Instead, focus on the things that stand out - we're just declaring variables with values, these are strings, arrays, and objects just like in JavaScript.

Another great thing that I've learned about TypeScript is you can mix JavaScript in with the code and have no issues doing so.  Check the screenshot below (this is inside an Angular app):

![typescript and javascript code](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-1.png)
_TypeScript and JavaScript used together in the same file_

## Data Types

Let's get started with the fun stuff - data types!  (There are a few data types we won't cover - never, null, undefined.  This is simply because there isn't much to them.  I want you to know they exist and if you'd like to dig in more on those types, here is a link to the official [TypeScript documentation](https://www.typescriptlang.org/docs/handbook/basic-types.html) for your reference.)

TypeScript will infer the type of data assigned to a variable without you explicitly setting the type but for simplicity and good measure I like to declare the data type when declaring my variables.

We assign data types by simply placing a colon after the variable name but before the equal sign:

_**const {variable name}: {variable type} = {variable value**_}

This is the convention that the majority of TypeScript data types are declared with the exception of functions and objects.

Some data types come with a bit more complexity than that, but you get the general idea.  Below are some brief explanations of data types and examples of how to declare them.

#### Boolean

Booleans in TypeScript work the same way as they do in JavaScript.  Variables of data type boolean are declared like so:

`const myBool: boolean = false`;

#### String

Strings in TypeScript work the same way as they do in JavaScript.  Variables of data type string are declared like so:

_`let myString: string = 'bacon'`_

#### Number

Numbers in TypeScript work the same way as they do in JavaScript.  Variables of data type number are declared like so:

`const myNum: number = 1207;`

#### **Array**

Arrays in TypeScript are, like other data types, just like arrays in JavaScript.  Variables of data type array are declared two separate ways :

`const myArr: number[] = [12, 90, 71];`

The above way is how you'd declare an array if all of the elements inside that array are numbers.

`const myArr: Array<number> = [12, 90, 71];`

This way of declaring an array uses the generic array type set to number.  Functionally, there is no difference in how these ways produce the end result of declaring a variable with array type.

If the data types inside the array are unknown or a mixture of data types, the array can be declared using the _<any>_ type (this is a type all on it's own that is discussed below):

`const myArr: Array<any> = [12, 'thirteen', false];`

This way will allow you to mix data types in the array.

#### **Tuples**

Tuples are a data type unique to TypeScript.  Think of them as arrays with a fixed number of elements.  This data type is best used when you know exactly how many variables you should have.  It is possible to reassign the value of the indices but not the amount of elements in the tuple.

Variables of data type tuple are declared just like an array:

`let mine: [number, string];`

If we'd like to change the _values_ of elements, we can do that as long as they match the types we provided when declaring our variable:

`mine[0] = 14`  ✔️

`mine[0] = 'Steve'`  ❌

Since we defined `mine` as a tuple, the order of the values matter as well and cannot be changed  Also, assigning an index outside of the original defined number will produce an error:

`mine[0] = ['Dave', 71]`  ❌

`mine = [121, 'Dave', 'Steve'];`  ❌

`mine = [121, 'bacon'];`  ✔️

#### **Function**

Functions can be as explicit as you want them to be.  What I mean by that is we can apply types to the parameters and returned values.  Below are two examples:

![a function that returns the number 91](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-2.png)
_We explicitly define the type of value we expect this function to return_

This function will throw an _error_ if any value is returned that is not a number.  It may return a variable _**only if**_ that variable points to a number.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-81.png)
_We can define the types of parameters we expect as well_

Above, we're type checking on the parameters being passed into our function.  This is a great way to avoid mistakes because if the number of parameters is off or if their data type doesn't match what we're expecting TypeScript will let us know with an error.

If I want a function that should not return a value, I can set the type as _void_ (a data type that means the absence of any data.  While it can be used when declaring variables it typically isn't because then we'd have to set the variable to _null_ or _undefined_,  I've only used when functions should have no return value) and if the function returns anything TypeScript will throw an error:

![a typescript function with the type set to void](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-3.png)
_A function with the type set to void_

By setting the type to _void_ I'm being explicit about my returns and establishing that while this function may still run, it should not _return_ a value.  If it does return a value, I'll get an error.

#### **Enum**

Enums are a welcomed (in my humble opinion) addition to the data types.  Think of them as a more user friendly approach to giving names to numeric values.  Here is an example of an enum:

`enum Foods {'bacon', 'tomato', 'lettuce'};`

console.log(Foods[0]) // yields 'bacon' console.log(Foods.bacon) // yields 0  console.log(Foods['lettuce']) // yields 2

It's also possible to assign the numbering index format with enums as well.  Many languages including C# have enums and I'm happy to see them come to JavaScript.

You can be as creative as you want with the names.  You can even change the numeric representation of the indices.  If you want your first index to start at 18 instead of 0, it's as simple as:

`enum Foods {'bacon'= 18, 'tomato', 'lettuce'};`

`console.log(Foods['bacon']); // 18`

Let's say we had the value 18 but were unsure of what it mapped to in our `Foods` enum, we can check that as well:

`console.log(Foods[18]); // 'bacon'`

One piece of noteworthy information is now that we've set the first index to start at 18, the next index will be 19, and so on following the numbering convention you establish.

**Object**

Objects in TypeScript are defined in similar ways as objects in JavaScript are defined.  We can be as implicit or explicit with our definition as we like or as the situation dictates:

`let data: = {name: 'Jonathan', age: 30, hobbies: ['running','swimming','coding']};`  ✔️

`let data: {name: string, age: number, hobbies: string[]} = {name: 'Jonathan', age: 30, hobbies: ['running','swimming','coding']};`  ✔️

When creating objects, the property names are immutable, but the order in which they appear does not matter, even if we define them in a specific order.

Also, we can have simple objects like those above, or we can define complex objects that take advantage of multiple data types like the one below (this object is for demonstration purposes only):

![a complex object data type in TypeScript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-4.png)
_Here we explicitly set data types where possible in this complex object_

#### Type Alias/Interface

With the example of a complex object above, you might be thinking this is awesome but what happens the next time I need to create a complex object?  I need to type all of this out manually again?

Fear not, the type alias and interface types are here to help!  A type alias is a data type that allows us to save other data types inside of it and then reference a variable instead of rewriting code over and over.

As a side note, type aliases and interfaces work in very similar ways.  Both allow us to scaffold an object/blueprint for how our data should be structured.  However, there are **_subtle differences_** that we won't cover here.  Instead, here is a [post that explains those differences](https://medium.com/@martin_hotell/interface-vs-type-alias-in-typescript-2-7-2a8f1777af4c) in an extremely efficient fashion if you'd like to dig deeper.

There are details between the two that we should be aware of - when using the type alias, we use an equals sign (=) to declare values, the interface does not require an equal sign.

![the interface data type in typescript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-6.png)
_The interface type works very similarly to the type alias but requires no equals sign (=)._

![an alias data type in typescript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-5.png)
_Alias data types do require an equals sign (=)._

Now that we have our alias declared, it's time to make use of that alias.  When we want to "build" our new variable from this alias, we simply set it as the data type:

![a typescript object ](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-7.png)
_Scaffolding objects using the interface / type data types is extremely useful :)_

It's important to note that the _interface_ is specific to TypeScript.  It is used only at compile time to do type checking and to catch any errors that may have slipped past our watchful eye.  **The data from our interface will end up in our final code, but the interface itself is compiled out**.

**Classes**

Classes are, in part, the veritable "bread and butter" of TypeScript (at least in my humble opinion).  Staying with this idea of scaffolding new objects, classes allow us to build data in a much easier way than just manually typing them out each time the need arises.

Classes can be thought of as blueprints for how our data should be defined and what actions, if any, it should be capable of through methods.

Below is an example of a class in TypeScript (which is made possible by the introduction of classes in ES6):

![typescript code showing the use of class data type](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-10.png)
_A TypeScript class, ready for instantiation :)_

Now, you might be asking yourself what are the differences between a _class_, a _type alias_, and an _interface_?  Great question!  The main difference between is that classes can be instantiated (we can create new instances of them) but an interface cannot.

There are, of course, other differences but that's not contained in the scope of this article.  If you'd like to dig deeper, here is a [great article](https://ultimatecourses.com/blog/classes-vs-interfaces-in-typescript#Using_TypeScript_class_vs_using_Typescript_interface) I read to help me understand those differences.  You'll find use cases for all of them, as I have, when using TypeScript.

**Union**

This is, far and away, my favorite data type of TypeScript!  The union type allows us declare a variable and then set it to an "either or" value.  What I mean by that is let's say we're expecting data to be passed into a function but we aren't sure if it's a string or a number - this is the perfect (and intended) purpose of the union type.

We use the single pipe character (on Windows it's Shift + the key right above Enter) when defining the type.  Here's what it would look like when defining a variable with union data type:

`const numOfDoors: string | string[ ];`

This tells TypeScript that _numOfDoors_ is a variable that can hold either a string or an array of strings.

Here is an example of that function I mentioned earlier using union type:

![typescript code showing the use of union type](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-11.png)

**Any**

Any is the type we set whenever we're unsure of the types of data we'll be getting.  Maybe we're getting something from a third party or some dynamic data and we aren't 100% sure if we're getting a string, a number, or maybe an array of information.  This is the perfect use case for type _any_.

![typescript code showing use of the any type](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-12.png)
_Data type any is a way to opt out of type checking_

I will caution against using type _any_ unless you absolutely must because when used we're opting out of one of the core features of TypeScript - type checking.

However, this data type has it's use cases just like all of the data types mentioned.

## That's A Wrap!

I told you this wouldn't take too long :D

I hope you enjoyed this article about TypeScript and are exited about the how it can prove useful to your code base.  In the next article, we'll dig into the practical side of TypeScript.  We'll go over installing it, compiling, and using it in your project (not just Angular projects either)!

This was originally posted to my [blog](https://jonathansexton.me/blog).

While you’re there don't forget to sign up for my **Newsletter** –   you can do that at the top right of the page.  I promise I’ll never spam your inbox and your information will not be shared with anyone/site.  I like to occasionally send out interesting resources I  find, articles about web development, and a list of my newest posts.

If you haven't yet, you can also connect with me on social media!  All of my links are also at the top right of this page.  I love connecting with others and meeting new people so don't afraid to say hi :)

Have an awesome day friend and happy coding!

