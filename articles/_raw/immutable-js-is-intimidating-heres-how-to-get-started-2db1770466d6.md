---
title: Immutable.js is intimidating. Here’s how to get started.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T22:58:26.000Z'
originalURL: https://freecodecamp.org/news/immutable-js-is-intimidating-heres-how-to-get-started-2db1770466d6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*INNhwAgxu9lkEdMBz0hp9Q.png
tags:
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By William Woodhead

  You hear that you should be using Immutable. You know you should, but you aren’t
  quite sure why. And when you go to the docs, the first snippet of code looks like
  this:

  identity<T>(value: T): T

  You think: Nah… maybe another time.

  ...'
---

By William Woodhead

You hear that you should be using [Immutable](https://facebook.github.io/immutable-js/). You know you should, but you aren’t quite sure why. And when you go to the [docs](https://facebook.github.io/immutable-js/docs/#/), the first snippet of code looks like this:

```
identity<T>(value: T): T
```

You think: Nah… maybe another time.

So, here’s a simple and fast introduction to get you started with Immutable. You won’t regret it:

_At [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=immutable&utm_campaign=awareness), we introduced [Immutable](https://facebook.github.io/immutable-js/) into our applications about 12 months ago. It has been one of the best decisions we have made. Our apps are now much more readable, robust, bug-free and predictable._

### **The basics**

#### Converting into Immutable

In normal JavaScript, we know two common data types: **Object** `{}` and **Array** `[]`.

To translate these into Immutable:

* **Object** `{}` becomes **Map** `Map({})`
* **Array** `[]` becomes **List** `List([])`

To convert normal JavaScript into Immutable, we can use the **Map**, **List,** or **fromJS** functions that Immutable provides:

```
import { Map, List, fromJS } from 'immutable';
```

```
// Normal Javascript
```

```
const person = {  name: 'Will',  pets: ['cat', 'dog']};
```

```
// To create the equivalent in Immutable:
```

```
const immutablePerson = Map({  name: 'Will',  pets: List(['cat', 'dog'])});
```

```
// Or ...
```

```
const immutablePerson = fromJS(person);
```

`fromJS` is a useful function that converts nested data into Immutable. It creates `Maps` and `Lists` in the conversion.

#### Converting back from Immutable to normal JavaScript

It is very simple to get your data back from Immutable to plain old JavaScript. You just call the `.toJS()` method on your Immutable object.

```
import { Map } from 'immutable';
```

```
const immutablePerson = Map({ name: 'Will' });const person = immutablePerson.toJS();
```

```
console.log(person); // prints { name: 'Will' };
```

> **_Keynote:_ _Data structures should be thought of as EITHER plain JavaScript OR Immutable._**

### Start using Immutable

Before explaining why Immutable is so useful, here are three simple examples of where Immutable can help you out right away.

#### 1. Getting a nested value from an object without checking if it exists

First in normal JavaScript:

```
const data = { my: { nested: { name: 'Will' } } };
```

```
const goodName = data.my.nested.name;console.log(goodName); // prints Will
```

```
const badName = data.my.lovely.name;// throws error: 'Cannot read name of undefined'
```

And now in Immutable:

```
const data = fromJS({ my: { nested: { name: 'Will' } } });
```

```
const goodName = data.getIn(['my', 'nested', 'name']);console.log(goodName); // prints Will
```

```
const badName = data.getIn(['my', 'lovely', 'name']);console.log(badName); // prints undefined - no error thrown
```

In the above examples, the normal JavaScript code throws an error, whereas the Immutable one does not.

This is because we use the `getIn()` function to get a nested value. If the key path doesn’t exist (that is, the object isn’t structured as you thought), it returns undefined rather than throwing an error.

You don’t need to check for undefined values all the way down the nested structure like you would in normal JavaScript:

```
if (data && data.my && data.my.nested && data.my.nested.name) { ...
```

This simple feature makes your code much more readable, less wordy, and much more robust.

#### 2. Chaining manipulations

First in normal JavaScript:

```
const pets = ['cat', 'dog'];pets.push('goldfish');pets.push('tortoise');console.log(pets); // prints ['cat', 'dog', 'goldfish', 'tortoise'];
```

Now in Immutable:

```
const pets = List(['cat', 'dog']);const finalPets = pets.push('goldfish').push('tortoise');
```

```
console.log(pets.toJS()); // prints ['cat', 'dog'];
```

```
console.log(finalPets.toJS());// prints ['cat', 'dog', 'goldfish', 'tortoise'];
```

Because `List.push()` returns the result of the operation, we can “chain” the next operation right onto it. In normal JavaScript, the `push` function returns the length of the new array.

This is a very simple example of chaining, but it illustrates the real power of Immutable.

This frees you up to do all sorts of data manipulation in a manner that is more functional and more concise.

> **_Keynote: Operations on an Immutable object return the result of the operation._**

#### 3. Immutable data

It’s called Immutable after all, so we need to talk about why this is important!

Let’s say you create an Immutable object and you update it — with Immutable, the initial data structure is not changed. It is immutable. (lower case here!)

```
const data = fromJS({ name: 'Will' });const newNameData = data.set('name', 'Susie');
```

```
console.log(data.get('name')); // prints 'Will'console.log(newNameData.get('name')); // prints 'Susie'
```

In this example we can see how the original “data” object is not changed. This means that you will not get any unpredictable behaviour when you update the name to “Susie.”

This simple feature is really powerful, particularly when you are building complex applications. It is the backbone of what Immutable is all about.

> **_Keynote_: _Operations on an Immutable object do not change the object, but instead create a new object._**

### Why Immutable is useful

The developers at [Facebook](https://www.facebook.com) sum up the benefits on the [homepage](https://facebook.github.io/immutable-js/) of the docs, but it’s quite tricky to read. Here is my take on why you should start using Immutable:

#### Your data structures change predictably

Because your data structures are immutable, you are in charge of how your data structures are operated upon. In complex web applications, this means you don’t get funny re-rendering issues when you change a bit of data that is being accessed for the UI.

#### **Robust data manipulation**

By using Immutable to manipulate data structures, your manipulations themselves are much less error-prone. Immutable does a lot of the hard work for you — it catches errors, offers default values, and builds nested data structures out-of-the-box.

#### Concise readable code

The functional design of Immutable can be confusing at first, but once you get used to it, function chaining makes your code much shorter and more readable. This is great for teams working on the same code base.

### Next steps

The learning curve is undeniably tricky with Immutable, but really worth it. Get started just having a play around.

Here are the keynotes that were noted as we went through. If you can keep these in your mind, you will take to Immutable like a duck to water!

1. Data structures should be thought of as EITHER plain JavaScript OR Immutable.
2. Operations on an Immutable object return the result of the operation.
3. Operations on an Immutable object do not change the object itself, but instead create a new object.

Good luck!

_If you liked this story, please ? and please share with others. Also please check out my company p[ilcro.com.](https://www.pilcro.com/?utm_source=medium&utm_medium=immutable&utm_campaign=awareness) Pilcro is brand software for G-Suite — for marketers and brand agencies._

![Image](https://cdn-media-1.freecodecamp.org/images/ntTfRnp-62XC61l4808bH5vhCSTaRhOs7opG)

