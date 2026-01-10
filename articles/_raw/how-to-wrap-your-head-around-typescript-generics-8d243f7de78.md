---
title: How to wrap your head around Typescript generics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T17:12:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-wrap-your-head-around-typescript-generics-8d243f7de78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gKVGuI3cUiJ043SjQn81hw.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nadeesha Cabral

  Sometime back when the “Flow vs. Typescript” debate was raging, I had to pick a
  side. And I picked Typescript. Fortunately, that was one of the better decisions
  I made. When I had to make that decision, ultimately what convinced me...'
---

By Nadeesha Cabral

Sometime back when the “Flow vs. Typescript” debate was raging, I had to pick a side. And I picked Typescript. Fortunately, that was one of the better decisions I made. When I had to make that decision, ultimately what convinced me was [Typescript’s support for call-time generics](https://medium.com/@nadeesha/why-i-choose-typescript-specifying-generic-parameters-during-call-time-706003f55675).

Today, let me try to walk you through what generics accomplish and how it helps us write safer, cleaner and more maintainable code.

### Example #1: Asserting a simple type

Let’s say we need a function that takes any value and puts that into an object. A naive implementation of this in Typescript would look and run like:

So much for type-safety.

It’s true that `myValue` can be of any type. But what we need to tell the controller is that the output of the function, although it cannot be foreseen as the developer writing the code, can be “inferred” by the type of the input type. In other words, we can have a “generic definition” of what the output is.

Generic implementation of the above function would be something like this:

What we’re simply saying is that `myValue` can have a type of `T`. It can be “any type” but not `any` type. In other words, it has a type we care about.

If you try to write the earlier execution in Typescript, you won’t be able to run it, as the compiler gives a helpful warning:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1uIU75xsSfWbGWVOmOUsKg.png)

### Example #2: Writing idx with Generics

`idx` is a “Library for accessing arbitrarily nested, possibly nullable properties on a JavaScript object”. It’s especially useful when you work with complex Javascript objects like REST API responses that may have nullable fields.

If you don’t mind me oversimplifying this a bit, it accomplishes this by basically `try`ing the function given as the second parameter with `props`. If it fails, it `catch`es and returns an `undefined` value safely, without throwing.

Again, a naive implementation of this would be:

But, if we’re a bit clever with generics, we can get Typescript to help us with this.

We’ve introduced two generics here.

`T` for the input type, and we “hint” that it’s an object by saying `T extends {}`. `U` is for the output type. And with these, we can express that the `selector` function is something that takes `T` and returns `U` of undefined.

Now if you attempt to write the same code as before with this definition of `idx`, you will get a compile error:

![Image](https://cdn-media-1.freecodecamp.org/images/1*pdasjNVJPY2ClKdENWBw6A.png)

### Example #3: Using type inference and generics to get the return type of a function

Suppose that I have a function, and I need to supply the consumer with the type of output. If I call this type `FooOutput`, I’ll write something like:

But by using generics and type inference, I can write a `ReturnType` generic type, that can “infer” the return type of a function:

We’re playing with a `T extends (...args: any[]) =>` any here. This just means th`a`t T is a generic function type that takes any number `of` any arguments and produces a value. Then we use it `to in`fer another ty`p`e R, and return it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gKVGuI3cUiJ043SjQn81hw.png)

Using this, I avoid the need to write my return type in the above example manually. Since `foo` is a function and I need that function’s type to use `ReturnType`, I’ve to get the type of `foo` by using `typeof`.

### Helpful utilities in my toolbox ?

I use a bunch of these utilities in everyday programming. Most of the utility generics are defined in the typescript `lib.es5.d.ts` over [here](https://github.com/Microsoft/TypeScript/blob/master/lib/lib.es5.d.ts#L1411). Some of my most-used ones include:

Hopefully, this helps you grasp Typescript generics a bit more. If you have questions, don’t hesitate to leave a question down below.

