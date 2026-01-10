---
title: How to make your data transformations more efficient using transducers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-20T10:57:07.000Z'
originalURL: https://freecodecamp.org/news/efficient-data-transformations-using-transducers-c779043ba655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3kXGy7LMUX2qPG3gapZD5Q.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Guido Schmitz

  Transforming large collections of data can be expensive, especially when you’re
  using higher order functions like map and filter.

  This article will show the power of transducers to create efficient data transformation
  functions, whic...'
---

By Guido Schmitz

Transforming large collections of data can be expensive, especially when you’re using [higher order functions](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528) like _map_ and _filter_.

This article will show the power of transducers to create efficient data transformation functions, which do not create temporary collections. Temporary collections are created when _map_ and _filter_ functions are chained together. This is because these functions return a new collection and will pass the result to the next function.

Imagine having records of **1,000,000** people and wanting to create a subset of “names of women above the age of 18 that live in The Netherlands”. There are different ways to solve this, but let’s start with the _chaining_ approach.

If this approach is new to you, or you want to learn more about it, I’ve written a blog post on using [higher order functions](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528).

```
const ageAbove18 = (person) => person.age > 18;const isFemale = (person) => person.gender === ‘female’;const livesInTheNetherlands = (person) => person.country === ‘NL’;const pickFullName = (person) => person.fullName;
```

```
const output = bigCollectionOfData  .filter(livesInTheNetherlands)  .filter(isFemale)  .filter(ageAbove18)  .map(pickFullName);
```

Below is the visualisation of using the chained approach that creates temporary arrays. Imagine the expense of looping over 1,000,000 records 3 times!

![Image](https://cdn-media-1.freecodecamp.org/images/G7mX8Ht-mfOiYsTYYv-kesUmfmOfrdYVo74O)

Of course, the filtered collections will be reduced by some amount, but it’s still quite expensive.

A key insight, however, is that _map_ and _filter_ can be defined using _reduce_. Let’s implement the above code in terms of _reduce_.

```
const mapReducer = (mapper) => (result, input) => {  return result.concat(mapper(input));};
```

```
const filterReducer (predicate) => (result, input) => {  return predicate(input) ? result.concat(input) : result;};
```

```
const personRequirements = (person) => ageAbove18(person)  && isFemale(person)  && livesInTheNetherlands(person);
```

```
const output = bigCollectionOfData  .reduce(filterReducer(personRequirements), [])  .reduce(mapReducer(pickFullName), []);
```

We can further simplify the _filterReducer_ by using [**function composition**](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-function-composition-20dfb109a1a0).

```
filterReducer(compose(ageAbove18, isFemale, livesInTheNetherlands));
```

When using this approach we reduce (haha!) the number of times we create a temporary array. Below is a visualization of the transformation when using the _reduce_ approach.

![Image](https://cdn-media-1.freecodecamp.org/images/dtnQEQo-2hzZ25uM-ycsYAbh8MCV51WRuvJs)

Beautiful, right? But we were talking transducers. Where are our transducers?  
It turns out, the _filterReducer_ and _mapReducer_ we created are **reducing functions**. We can express this as:

```
reducing-function :: result, input -> result
```

Transducers are functions that accept a **reducing function** and return a reducing function. This can be expressed as the following:

```
transducer :: (result, input -> result) -> (result, input -> result)
```

The most interesting part is that transducers are roughly symmetric in their type signature. They take one reducing function and return another.

Because of this we can compose any number of transducers using function composition.

#### **Building your own Transducers**

Hopefully it’s all starting to make more sense now. Let’s build our own transducer functions for _map_ and _filter_.

```
const mapTransducer = (mapper) => (reducingFunction) => {  return (result, input) => reducingFunction(result, mapper(input));}
```

```
const filterTransducer = (predicate) => (reducingFunction) => {  return (result, input) => predicate(input)    ? reducingFunction(result, input)    : result;}
```

Using the transducers we’ve created above, let’s transform some numbers. We will use the [_compose_](http://ramdajs.com/docs/#compose) function from RamdaJS.

[**RamdaJS**](http://ramdajs.com) is a library that provides practical functional methods and is specifically designed for functional programming styles.

```
const concatReducer = (result, input) => result.concat(input);const lowerThan6 = filterTransducer((value) => value < 6);const double = mapTransducer((value) => value * 2);
```

```
const numbers = [1, 2, 3];
```

```
// Using Ramda's compose hereconst xform = R.compose(double, lowerThan6);
```

```
const output = numbers.reduce(xform(concatReducer), []); // [2, 4]
```

The _concatReducer_ is called the **iterator function**. This will be called on every iteration and will be responsible for transforming the output of the transducer function.

In this example, we simply concat the result. Because every transducer only accepts a reducing function, we cannot use _value.concat_.

When we compose multiple transducers into a single function, most of the time it’s called a _xform_ transducer. So when you see this somewhere, you know what it means.

#### **Composing multiple transducers**

We’ve been using ordinary function composition in the previous example, and you may be wondering what the order of evaluation is. Although function composition applies functions from right to left, the transformations will actually be evaluated from left to right at execution time — which is far more intuitive to those of us who read in left-to-right languages.

It takes a little bit of thinking to see why this is true: given our transducer _double_ which returns a reducing function, and our transducer _lowerThan6_ which also returns a reducing function, when you compose _double_ and _lowerThan6_, the output of _double_ will be passed to _lowerThan6_, which will then return the reducing function of _lowerThan6_. Thus, _double_ is the result of the composition and the order of evaluation is indeed from left to right.

I’ve created a JSBin [**example**](https://jsbin.com/kezugajaqa/1/edit?js,console) with some _console.log_ statements, so you can have a look at it for yourself.

#### **Using RamdaJS to improve readability**

Since transducers are a perfect example for a functional programming style, let’s look at the way Ramda can help us by using their set of methods.

```
const lowerThan6 = R.filter((value) => value < 6);const double = R.map((value) => value * 2);const numbers = [1, 2, 3];
```

```
const xform = R.compose(double, lowerThan6);
```

```
const output = R.into([], xform, numbers); // [2,4]
```

With Ramda, we can use their _map_ and _filter_ methods. This is because Ramda’s internal [_reduce_](https://github.com/ramda/ramda/blob/v0.25.0/source/internal/_reduce.js) method uses the [Transducer Protocol](https://github.com/cognitect-labs/transducers-js#the-transducer-protocol) under the hood.

> _“The goal of the Transducer Protocol is that all JavaScript transducer implementations interoperate regardless of the surface level API. It calls transducers independently from the context of their input and output sources and specifies only the essence of the transformation in terms of an individual element._  
> _Because transducers are decoupled from input or output sources, they can be used in many different processes — collections, streams, channels, observables, etc. Transducers compose directly, without awareness of input or creation of intermediate aggregates.”_

#### **Conclusion**

Transducers are a powerful and composable way to build transformations that you can reuse in many contexts. Once you’ve got a transducer, you can do an open set of things.

They’re especially useful when transforming big datasets, but you can also use the same transducer to transform a single record.

If you want to learn more about this subject, I recommend the following articles:

[https://clojure.org/reference/transducers](https://clojure.org/reference/transducers)  
[http://blog.cognitect.com/blog/2014/8/6/transducers-are-coming](http://blog.cognitect.com/blog/2014/8/6/transducers-are-coming)  
[https://github.com/cognitect-labs/transducers-js#the-transducer-protocol](https://github.com/cognitect-labs/transducers-js#the-transducer-protocol)

#### ?? If you enjoyed this article, hit that clap button below ?. It would mean a lot to me and it helps other people see this post.

#### Follow me to get notified for more programming content like this.

