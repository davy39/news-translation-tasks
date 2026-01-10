---
title: How to master advanced TypeScript patterns
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T17:35:32.000Z'
originalURL: https://freecodecamp.org/news/typescript-curry-ramda-types-f747e99744ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s8OOdE6Qmx0HhbQwexsR1Q.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Ramda
  slug: ramda
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Pierre-Antoine Mills

  Learn how to create types for curry and Ramda


  _Photo by [Unsplash](https://unsplash.com/photos/2jXkA7GAz9M?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">sergio sou...'
---

By Pierre-Antoine Mills

#### Learn how to create types for curry and Ramda

![Image](https://cdn-media-1.freecodecamp.org/images/gHHbXSKPmkakVPjav7Z2U9wiAA7Jcdfhde3t)
_Photo by [Unsplash](https://unsplash.com/photos/2jXkA7GAz9M?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">sergio souza</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Despite the popularity of currying and the rise of functional programming (and of TypeScript), it is still a hassle today to make use of curry and have **proper type checks**. Even famous libraries like Ramda do not provide generic types for their curry implementations (but we will).

However, you need no functional programming background to follow this guide. The guide is about currying but it is only a topic of my choice to teach you advanced TypeScript techniques. You just need to have practised a bit with TypeScript’s primitive types. And by the end of this walk-through, you will be a real TS wizard ?.

If you’re a functional programmer, you are probably already using currying to create powerful compositions and partial applications… And if you are a bit behind, it’s time to take the leap into functional programming, start shifting away from the imperative paradigm and solve problems faster, with ease, and promote reusability within your codebase.

At the end of this guide, you will know how to create **powerful types** like:

![Image](https://cdn-media-1.freecodecamp.org/images/0jtoHxd5Keq7fx457IldtUAfFG4ThZx8YoGq)

In fact, Ramda does have some kind of mediocre types for curry. These types are not generic, **hard-coded**, limiting us to a certain amount of parameters. As of version 0.26.x, it only follows a **maximum of 6 arguments** and does not allow us to use its famous **placeholder** feature very easily with TypeScript. Why? It’s hard, but we agree that we had enough and we’re going to fix this!

![Image](https://cdn-media-1.freecodecamp.org/images/J6jdoXiM9B8ZUX02zbSXyE8-Aw-add4QIJP5)
_Source: [Giphy](https://giphy.com/gifs/glitch-falling-JWXIa2DAQNoQg" rel="noopener" target="_blank" title=")_

#### What is currying?

But before we start, let’s make sure that you have a very basic understanding of what currying is. Currying is the process of transforming a function that takes multiple arguments into a series of functions that take one argument at a time. Well that’s the theory.

I prefer examples much more than words, so let’s create a function that takes two numbers and that returns the result of their addition:

![Image](https://cdn-media-1.freecodecamp.org/images/iMtzZhZle3U2g9OSU2m8KJuYqaKlyJSy9xbm)

The curried version of `simpleAdd` would be:

![Image](https://cdn-media-1.freecodecamp.org/images/XwJ0THXXpg29kt4ji36b7AwRcJPFB48JnYg-)

In this guide, I will first explain how to create TypeScript types that work with a standard curry implementation.

Then, we will evolve them into more **advanced types** that can allow curried functions to take 0 or more arguments.

And finally, we will be able to use “gaps” that abstract the fact that we are not capable or willing to provide an argument at a certain moment.

**TL;DR**: We will create types for “classic curry” & “advanced curry” (Ramda).

### Tuple types

Before we start learning the most advanced TypeScript techniques, I just want to make sure that you know **tuples**. Tuple types allow you to express an array where the type of a fixed number of elements is known. Let’s see an example:

![Image](https://cdn-media-1.freecodecamp.org/images/QEdtDxuaor9oABVKDXIz91aGwFeT7xyUQx8S)

They can be used to enforce the kind of values inside a fixed size array:

![Image](https://cdn-media-1.freecodecamp.org/images/k9PLODTdaIIJJjsEhHg5i3S-AYPF8jcrMlXr)

And can also be used in combination of rest parameters (or destructuring):

![Image](https://cdn-media-1.freecodecamp.org/images/hhoq8DXKwuEGzzFnkUlHnu8Roc3sDHhpszc8)

But before starting to build our awesome curry types, we’re going to do a bit of a warmup. We are going to create the first tools that we need to build one of the most basic curry types. Let’s go ahead.

Maybe you could guess… We are going to work with tuple types a lot. We’ll use them as soon as we extracted the parameters from the “original” curried function. So for the purpose of an example, let’s create a basic function:

![Image](https://cdn-media-1.freecodecamp.org/images/J9peTtIATeaP8jp76F1Kj7dwI5uonYaxpBcj)

We extracted the parameter types from `fn00` thanks to the magic of `Parameters`. But it’s not so magical when you recode it:

![Image](https://cdn-media-1.freecodecamp.org/images/U39IDHFcnsZ-dLyoZv6Fbno1Q0GZxZA7Ky-A)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/r4JRkERGOwT3aAYa96iNWbljXlP3Xr4qAPex)

Good, it works just as `Parameters` does. Don’t be scared of `infer`, it is one of the most powerful keywords for building types. I will explain it in more detail right after we practiced some more:

#### Head

Earlier, we learnt that a “classic curried” function takes one argument at a time. And we also saw that we can extract the parameter types in the form of a tuple type, very convenient.   
So `Head` takes a tuple type `T` and returns the **first type** that it contains. This way, we’ll be able to know what argument type has to be taken at a time.

![Image](https://cdn-media-1.freecodecamp.org/images/CHlmvskq9CbDrfVK8qEokxPJWHAoi0VK1OwK)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/3BllaJUgiKEujqHjG--NxRLVwAuLXGx8N1A1)

#### Tail

A “classic curried” function consumes arguments **one by one**. This means that when we consumed the `Head<Params&`lt;F>>, we somehow need to mov**e on to the ne**xt parameter that hasn’t been consumed yet. This is the `pur`pose of Tail, it conveniently removes the first entry that a tuple might contain.

As of TypeScript 3.4, we cannot “simply” remove the first entry of a tuple. So, we are going to work around this problem by using one very **valid trick**:

![Image](https://cdn-media-1.freecodecamp.org/images/LJIrVYehTvk0lnEforfoD-XfLHApWxHytjgu)

Using **function types**, we were able to tell TypeScript to infer the tuple that we wanted. If you do not understand it yet, it is not a problem, this is just a warmup, remember?

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/s1M8asD9pTUySKKNzdN8ThS7tI3nccrUYEW0)

#### HasTail

A curried function will return a function until all of it’s parameters have been **consumed**. This condition is reached when we called `Tail` enough times that there is no tail left, nothing’s left to consume:

![Image](https://cdn-media-1.freecodecamp.org/images/aBBaqEP52ccLHllwPYRywYqKm15CkqhWISj1)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/MSslnHhpafGiSGZIDIVtPskqgoP2ufaE4jEU)

### Important keywords

You have encountered three important keywords: `**type**`, `**extends**` and `**infer**`. They can be pretty confusing for beginners, so these are the ideas they convey:

* `**extends**`:   
To keep it simple, you are allowed to think of it as if it was our dear old  
JavaScript’s `**===**`. When you do so, you can see an `extends` statement as a **simple ternary**, and then it becomes much simpler to understand. In this case, `extends` is referred to as a **conditional type**.
* `**type**`:   
I like to think of a type as if it was a **function**, but for types. It has an input, which are types (called **generics**) and has an output. The output depends on the “logic” of a type, and `extends` is that block of logic, similar to an `if` clause (or ternary).
* `**infer**`:  
It is the magnifying glass of TypeScript, a beautiful inspecting tool that can **extract types** that are trapped inside different kinds of structures!

I think that you understand both `extends` & `type` well and this is why we are going to practice a bit more with `infer`. We’re going to extract types that are contained inside of different generic types. This is how you do it:

#### Extract a property’s type from an object

![Image](https://cdn-media-1.freecodecamp.org/images/e7TW4m93Q3H1MNUwVGDTM0Ref93NWtRGYfyC)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/CWPhfFjc1-XnMUOy8RzZZ6q6iHwVR1WtZpzh)

**Extract inner types from function types**

![Image](https://cdn-media-1.freecodecamp.org/images/7Dz648h0mzss0jbsAMu1LxHdZTWYEkTNBMzD)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/iqqzJqqwwFGHGB0lLjU3gpMamLtR3lmAT5j-)

**Extract generic types from a class or an interface**

![Image](https://cdn-media-1.freecodecamp.org/images/AaiIqlv-8HPqcnnItAEOCDwuiTlnIGVk38xq)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/7SwlN4zLQb-GkVU0z53bg5G0nZrWrTFhf8ek)

**Extract types from an array**

![Image](https://cdn-media-1.freecodecamp.org/images/8qYXZ0XBi6NkAeQkOJAhTcN98KxyX1bHfgF0)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/3WNFqxUGSvt-TJpJ6MoJc6EqyvraHbyLN6pN)

**Extract types from a tuple**

![Image](https://cdn-media-1.freecodecamp.org/images/Pb-j222BGW7K46xR9rgakjVeOwdFa2iG9k6N)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/jngjN2i1yCScQMVS6aHjYfPXAH1MZ5Y3ugYI)

We tried to infer the type of the **rest of the tuple** into a type `B` but it did not work as expected. It is because TypeScript **lacks** of a feature that would allow us to **deconstruct** a tuple into another one. There is an active proposal that tackles these issues and you can expect improved manipulation for tuples in the future. This is why `Tail` is constructed the way it is.

`infer` is very powerful and it will be your **main tool** for type manipulation.

![Image](https://cdn-media-1.freecodecamp.org/images/1A2co54z4low60cVicsPW57m979hefFOjD7i)
_Source: [Giphy](https://giphy.com/gifs/cheezburger-see-5K3Vw3jUqwV56" rel="noopener" target="_blank" title=")_

### Curry V0

The warm-up ? is over, and you have the knowledge to build a “classic curry”. But before we start, let’s summarize (again) what it must be able to do:

![Image](https://cdn-media-1.freecodecamp.org/images/VE5KCCPIbmYfSrGgTsB2UCa2HBLkzD59uq7D)

Our first curry type must take a tuple of **parameters** `P` and a **return** type `R`. It is a **recursive** function type that **varies** with the **length of** `P`:

![Image](https://cdn-media-1.freecodecamp.org/images/CgIczre6OeRg6wAd2vGYnPYZoAUj4K6Id7Vn)

If `HasTail` reports `false`, it means that **all** the parameters were **consumed** and that it is time to **return** the return type `R` from the original function. Otherwise, there’s parameters **left to consume**, and we **recurse** within our type. Recurse? Yes, `CurryV0` describes a function that has a return type of `CurryV0` as long as there is a `Tail` (`HasTail<P> extend`s true).

This is as simple as it is. Here is the proof, without any implementation:

![Image](https://cdn-media-1.freecodecamp.org/images/6psb7bd4KeXlfysR-QlqZuua7cJXrRdiz4PN)

![Image](https://cdn-media-1.freecodecamp.org/images/7T9oP6a4U46tlbK3a6OMnM7AHuikSwMglTOs)

But let’s rather visualize the recursion that happened above, step by step:

![Image](https://cdn-media-1.freecodecamp.org/images/Keu0siYpxvmqzzNuh1iUsLaDI8hZwLm7JioR)

And of course, type hints work for an **unlimited** amount of parameters ?:

![Image](https://cdn-media-1.freecodecamp.org/images/hbX-Y5WQPVnVVCPL02Gk7GI-VWCSjsPPnVf8)

### Curry V1

Nice, but we forgot to handle the scenario where we pass a **rest parameter**:

![Image](https://cdn-media-1.freecodecamp.org/images/5s8kSoNvfuZ9MOZiXd7QPH1N0sAXJQZbAkal)

We tried to use a rest parameter, but it won’t work because we actually expected a **single** parameter/argument that we earlier called `**arg0**`. So we want to take at least one argument `arg0` and we want to receive any extra (optional) arguments inside a rest parameter called `rest`. Let’s enable taking rest parameters by upgrading it with `Tail` & `Partial`:

![Image](https://cdn-media-1.freecodecamp.org/images/sqex95FBdDbnidAj6eq2Q2HZYCDbTqGV4kPk)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/AeHZhJ110EifXklHor2T4OULadbnwBxIHYwT)

![Image](https://cdn-media-1.freecodecamp.org/images/5zjjyKorZYH5Ku93nwOiBFLUiLSySjtqjPCa)

But we made a horrible mistake: the arguments are consumed very badly. According to what we wrote, this will not produce a single TS error:

![Image](https://cdn-media-1.freecodecamp.org/images/Bob3CnZ0vCZqpmvqNpCsU55y8enzw17npqri)

In fact there is a big **design problem** because we said that we would force taking a single `arg0`. Somehow, we are going to need to **keep track** of the arguments that are **consumed** at a time. So, we will first get rid of `arg0` and start tracking consumed parameters:

![Image](https://cdn-media-1.freecodecamp.org/images/0uydMEZMPLc6-mr5YSZvzvEhCigKphy7bSTi)

There, we made use of a **constrained** generic called `**T**` that is going to **track** any taken arguments. But now, it is completely broken, there is no more type checks because we said that we wanted to track `**any[]**` kind of parameters (the constraint). But not only that, `Tail` is completely useless because it only worked well when we took one argument at a time.

There is only one solution: **some more tools** ?.

### Recursive types

The following tools are going to be used to determine the next parameters to be consumed. How? By tracking the consumed parameters with `T` we should be able to **guess what’s left**.

Fasten your seat belt! You are about to learn another powerful technique ?:

#### Last

Take your time to try to understand this complex yet very short type. This  
example takes a tuple as a parameter and it extracts its last entry out:

![Image](https://cdn-media-1.freecodecamp.org/images/-Lz8QpB1iizm5Ht5AQXVopGg7spFsvcs3tTi)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/sB6a0YyguI4OIakTZKFLpn4UMN-4azlSCaQp)

This example demonstrates the power of conditional types when used as an indexed type’s **accessor**. A what? A conditional type that accesses a type’s inner types in a command line fashion. For a more visual explanation:

![Image](https://cdn-media-1.freecodecamp.org/images/xgzVrAX64CLiquY0yLF0qthPMfF21skZpnRo)

This technique is an **ideal** approach and a safe way to do **recursion** like we just did. But it is not only limited to recursion, it is a nice and a visual way to **organise** complex **conditional types**.

### Basic tools #1

Where were we? We said that we needed tools in order to **track arguments**. It means that we need to know what parameter types we can take, which ones have been consumed and which ones are the next to come. Let’s get started:

#### Length

To do the analysis mentioned above, we will need to **iterate** over tuples. As  
of TypeScript 3.4.x, there is no such iteration protocol that could allow us to iterate freely (like a `for`). Mapped types can map from a type to another, but they are too limiting for what we want to do. So, ideally, we would like to be able to manipulate some sort of **counter**:

![Image](https://cdn-media-1.freecodecamp.org/images/wYeuZrAjfFdM6B9NXAUv3rCt0Cc8cIHXP23E)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/2oF0r2YpVc-ukCwlfdbrXVCb-4upiPPMkXdC)

By **topping** a tuple up with `any`, we created something that could be similar to a variable that can be **incremented**. However, `Length` is just about giving the size of a tuple, so it also works with any other kind of tuple:

![Image](https://cdn-media-1.freecodecamp.org/images/8zKoWai2QpSrTYWPq6DXtRR6eiwsgqT3AlCf)

#### Prepend

It adds a type `E` at the **top** of a tuple `T` by using our first TS trick:

![Image](https://cdn-media-1.freecodecamp.org/images/xh7GuVMyKVoNGQc43TrYy-ZTvMrJNYNj7ZJB)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/Z9ElT2pecidPyZKluv0V4pkzXDOljBqdRtAa)

In `Length`’s examples, we manually increased a counter. So `Prepend` is the ideal candidate to be the base of a **counter**. Let’s see how it would work:

![Image](https://cdn-media-1.freecodecamp.org/images/PpHPCHNCKbXVADtErbDfAMCY4HZq5YSstTEK)

#### Drop

It takes a tuple `T` and drops the first `N` entries. To do so we are going to use the same techniques we used in `Last` and our brand new counter type:

![Image](https://cdn-media-1.freecodecamp.org/images/3iXvCx2E5qJAQ3INjsoT-8DwmBqjbLPZaQ0k)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/1TupbmvJtwskYCMImwUlAaMAei8DENnfL2t0)

What happened?

The `Drop` type will recurse until `Length<`;**I> m**atches the val`u`e of N that we passed. In other words, the type of `i`ndex 0 is chosen by the conditional accessor until that condition is met. And we `used Prepend&l`t;any, I> so **that we** can increase a counter like we would do in a `loop. Thu`s, Length<I> is us**ed as a** recursion counter, and it is a way to freely iterate with TS.

### Curry V3

It’s been a long and tough road to get here, well done! There’s a reward for you ?.

Now, let’s say that we tracked that 2 parameters were consumed by our curry:

![Image](https://cdn-media-1.freecodecamp.org/images/F2IJOT9pYiP-yYyC5c-qXEkbUUZfHg3XXkiA)

Because we know the amount of consumed parameters, we can guess the ones that are still left to be consumed. Thanks to the help of `Drop`, we can do this:

![Image](https://cdn-media-1.freecodecamp.org/images/BOHkaHyXDA91p4oDFZw1bQuJUFNZa8EjhgJ3)

It looks like `Length` and `Drop` are precious tools. So let’s revamp our previous version of curry, the one that had a broken `Tail`:

![Image](https://cdn-media-1.freecodecamp.org/images/uXP4yGlh8Eioxhzko8m9CMafcHHuNUfdUSvX)

What did we do here?

First, `Drop<Length<`T>, P> means that we remove consumed parameters out.  
Then, if th`e length of Drop&l`t;Length<T>`,` P> is not equal to 0**, our curry type h**as to continue recursing with the dropped paramete**rs** until… Finally, when all **of the** parame`ters w`ere consumed, the Length of the dropped parameters is equal to 0, and the return type is R.

![Image](https://cdn-media-1.freecodecamp.org/images/t4FRePSoaR2dAZ4IC0GJkUxvm0S3bJdfUosX)
_Source: [Giphy](https://giphy.com/gifs/ice-goat-LumJYWwnr6fSg" rel="noopener" target="_blank" title=")_

### Curry V4

But we’ve got another error above: TS complains that our `Drop` is not of type `any[]`. Sometimes, TS will **complain** that a type is not the one you expected, but you know it is! So let’s add another tool to the collection:

#### Cast

It requires TS to **re-check** a type `X` against a type `Y`, and type `Y` will only be enforced if it fails. This way, we’re able to stop TS’s complaints:

![Image](https://cdn-media-1.freecodecamp.org/images/0tjYGqAsnLhkMuRvnZJO0Vc450zaY3CGSafN)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/PNWd5VOWmkDXtc3GhpQiKDCl7yHi38W4C2NT)

And this is our previous curry, but without any complaint this time:

![Image](https://cdn-media-1.freecodecamp.org/images/PUf9EeCVGQni5QaKgjsD694AvetAXOirWY2p)

Remember earlier, when we lost the type checks because we started tracking consumed parameters with `T extends any[]`? Well it has been fixed by casting `T` to `Partial<`;P>. We added a constrain`t withCast<T,Pa`rtial<P>>!

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/TtZf06ws-uNqgtzb7R18yyTf4VpC08LbGVwa)

![Image](https://cdn-media-1.freecodecamp.org/images/RtUUGbB03dr9ZqLnQ5c6dNo7-9bMunXnfHHr)

![Image](https://cdn-media-1.freecodecamp.org/images/VwhBIFhYeITpAOfCeY2hqOazp0wedjPzEgQr)

### Curry V5

Maybe you thought that we were able to take rest parameters. Well, I am very sorry to inform you that we are not there yet. This is the reason why:

![Image](https://cdn-media-1.freecodecamp.org/images/qJUVcf7HJye7spkqBobl9Nlg6afIsspcYhfM)

Because rest parameters can be **unlimited**, TS’s best guess is that the length of our tuple is a `number`, it’s kind of clever! So, we **cannot** make use of `Length` while dealing with rest parameters. Don’t be sad, it’s not so bad:

![Image](https://cdn-media-1.freecodecamp.org/images/c-770wkJstOyLT4lV0DnwdM0LJqhDKY8zAO4)

When all the non-rest parameters are consumed, `Drop<Length<`;T>,P> can `only ma`tch […any[]]. Thanks to th`is, we used` [any,…any[] as a c**ond**ition to end the recursion.

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/QKEwC3TzYAW6nm8jHvtg9nWtWQbOBogY0bLW)

![Image](https://cdn-media-1.freecodecamp.org/images/4197K0vwe6DMbxp1QHp0hLGCgbDLv71zDqJp)

![Image](https://cdn-media-1.freecodecamp.org/images/M5msqRMawT7UuEeMQ80U02YrKI6mZxjKTwGp)

Everything works like a charm ?. You just got yourself a smart, g**eneric,** v**ariadic curry type.** You will be able play with it very soon… But before you do so, what if I told you that our type can get even more awesome?

### Placeholders

How awesome? We are going give our type the ability to **understand** partial application of **any combination of arguments**, on any position. According to Ramda’s documentation, we can do so by using a **placeholder** called `_`. It states that for any curried function `f`, these calls are equivalent:

![Image](https://cdn-media-1.freecodecamp.org/images/8hxR2PKAItfGpkkI451SiG84L3o8JsQFvvnW)

A placeholder or “gap” is an object that abstracts the fact that we are not  
capable or willing to provide an argument at a certain moment. Let’s start by  
defining what a placeholder is. We can directly grab the one from Ramda:

![Image](https://cdn-media-1.freecodecamp.org/images/5qEGVxAeMGTSN77Itw2H9qFCQYqIZgKTgU72)

Earlier, we have learnt how to do our first type iterations by increasing a tuple’s length. In fact, it is a bit confusing to use `Length` and `Prepend` on our counter type. And to make it **clearer**, we will refer to that counter as an **iterator** from now on. Here’s some new aliases just for this purpose:

#### Pos (Position)

Use it to query the position of an iterator:

![Image](https://cdn-media-1.freecodecamp.org/images/2XiBFO4R97iAoam8JVXck1SIvt-yNFLojq0A)

#### Next (+1)

It brings the position of an iterator up:

![Image](https://cdn-media-1.freecodecamp.org/images/hI4x2iy4H1smshUSP9KICQ6Lk9a-IYYXBS7m)

#### Prev (-1)

It brings the position of an iterator down:

![Image](https://cdn-media-1.freecodecamp.org/images/OmpB2K2jHbNkx1Ms-W4YCSK0DkuKjf6dXEPl)

Let’s test them:

![Image](https://cdn-media-1.freecodecamp.org/images/Lkedx1ruYGBRIwrO-S9HcdYSaWrYuDXOYjBG)

#### Iterator

It creates an iterator (our counter type) at a position defined by `Index` and is able to start off from another iterator’s position by using `From`:

![Image](https://cdn-media-1.freecodecamp.org/images/AJsinWfsGJmL6cV1-wGQXv137cng1eGL1mbE)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/kJbgjeGI0MHUhp6WtpVXhCG83m3FleLPFgOo)

### Basic tools #2

Good, so what do we do next? We need to **analyze** whenever a placeholder is passed as an argument. From there, we will be able to tell if a parameter has been “skipped” or “postponed”. Here’s some more tools for this purpose:

#### Reverse

Believe it or not, we still lack a few basic tools. `Reverse` is going to give us the freedom that we need. It takes a tuple `T` and turns it the other way around into a tuple `R`, thanks to our brand new iteration types:

![Image](https://cdn-media-1.freecodecamp.org/images/mV237zmN8G6M5OGxtkvsQLKCS5UIbtQCj4ff)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/16lb4ggNoGBQ328a-FaQUnBNlVYB0jFP4uqt)

#### Concat

And from `Reverse`, `Concat` was born. It simply takes a tuple `T1` and merges it with another tuple `T2`. It’s kind of what we did in `test59`:

![Image](https://cdn-media-1.freecodecamp.org/images/eKKnFeG25Qso0D1O2Zqc4BGnZrRc7JOo683l)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/KTTlVtOGKv9Sx3phQnlCMcjz5WUI3nOQzSUZ)

#### Append

Enabled by `Concat`, `Append` can add a type `E` at the end of a tuple `T`:

![Image](https://cdn-media-1.freecodecamp.org/images/Wl-T8NRPiEAwLXmZGCjaNLNAZltxNCIgl9w8)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/UMvrhshMeARwFndD-CUp0BNPh0Ew08STCXzV)

### Gap analysis

We now have enough tools to perform **complex type checks**. But it’s been a while since we discussed this “gap” feature, how does it work again? When a gap is specified as an argument, its matching parameter is **carried over** to the next step (to be taken). So let’s define types that understand gaps:

#### GapOf

It checks for a placeholder in a tuple `T1` at the position described by an iterator `I`. If it is found, the matching type is **collected** at the same position in `T2` and carried over (saved) for the next step through `TN`:

![Image](https://cdn-media-1.freecodecamp.org/images/SuAOfNSC7M1N0EMcE79GcpyON-fQsHvgzm68)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/qiwU1IXQv2b9zRz4VksfFzK9Y9HxfewhUDmy)

#### GapsOf

Don’t be impressed by this one. It calls `Gap` over `T1` & `T2` and stores the results in `TN`. And when it’s done, it concats the results from `TN` to the parameter types that are left to be taken (for the next function call):

![Image](https://cdn-media-1.freecodecamp.org/images/Lop0oZKqLXoe7Wv15mXq9kEoEBdalufa-Tpb)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/6i2Xc1q6E6f3y8Agca4uOKkEKK5CbKjt6fDQ)

#### Gaps

This last piece of the puzzle is to be applied to the tracked parameters `T`. We will make use of **mapped types** to explain that is is possible replace any argument with a **placeholder**:

![Image](https://cdn-media-1.freecodecamp.org/images/Ib8MHDLBtIhnPAoCobC8-G69cTew-umwBGXN)

A mapped type allows one to iterate and **alter properties** of another type. In this case, we altered `T` so that each entry can be of the placeholder type. And thanks to `?`, we explained that each entry of `T` is optional. It means that we no longer have the need to use `Partial` on the tracked parameters.

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/E3fgCRtmWtHBFBv5vdxT7OdzCaXBkYWt2uoH)

Ugh, we never said that we could take `undefined`! We just wanted to be able to omit a part of `T`. It is a **side effect** of using the `?` operator. But it is not that bad, we can fix this by re-mapping with `NonNullable`:

![Image](https://cdn-media-1.freecodecamp.org/images/h6zieDXDvoLGLsl8LNP5aLC508Hgou04fw1x)

So let’s put the two together and get what we wanted:

![Image](https://cdn-media-1.freecodecamp.org/images/TlR8l43TjvH1FVVKOqqnob38k2PyMk1QZDDy)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/0wvpT0toDEO1MWpZqJnbiC9nl1QTnOKg8NBS)

### Curry V6

We’ve built the last tools we will ever need for our curry type. It is now time to put the last pieces together. Just to remind you, `Gaps` is our new replacement for `Partial`, and `GapsOf` will replace our previous `Drop`:

![Image](https://cdn-media-1.freecodecamp.org/images/RtM7MwxrFcQmlr4oI0ZvOAT7R1Vb2WVz0KZs)

Let’s test it:

![Image](https://cdn-media-1.freecodecamp.org/images/tnIPwlUxOi4MFOeGA83BhsMdReeZsesE5YsP)

In order to make sure that everything works as intended, I am going to force the values that are to be taken by the curried example function:

![Image](https://cdn-media-1.freecodecamp.org/images/Y9DQVOnURiopXB7ved6yQwawFzS8zjH-d9oT)

![Image](https://cdn-media-1.freecodecamp.org/images/tkeaGYZtras0kQcUjKSCHt9aqBgeYoZlLv7t)

There is just a little problem: it seems like we’re a bit ahead of Ramda! Our type can understand very complex placeholder usages. In other words, Ramda’s placeholders just **don’t work** when they’re combined with rest parameters ?:

![Image](https://cdn-media-1.freecodecamp.org/images/2IZ4S7mBajskuaaDrTdD2GXUAQEnCiZ1-jCp)

![Image](https://cdn-media-1.freecodecamp.org/images/NsZjbAymZITMsw0wKe0Q32LOspQGCGRJqVv5)

However, even if this looks perfectly correct, it will result in a complete crash. This happens because the implementation of Ramda’s curry does not deal well with combinations of **placeholders and rest parameters**. This is why I opened a ticket with Ramda on Github, in the hope that the types we’ve just created could one day work in harmony with the library.

![Image](https://cdn-media-1.freecodecamp.org/images/gfN-AekkhygN4jzQF95nyvODxjc8D-BNUyyf)
_Source: [Giphy](https://giphy.com/gifs/jess-3osxYciDsUpfwZXZV6" rel="noopener" target="_blank" title=")_

### Curry

This is very cute, but we have one last problem to solve: **parameter hints**. I don’t know about you, but I use parameter hints a lot. It is very useful to know the names of the parameters that you’re dealing with. The version above does not allow for these kind of hints. Here is the fix:

![Image](https://cdn-media-1.freecodecamp.org/images/j6cwCzOiM5lQBIaH-OKjbAzMa-VZ7quGpG63)

I admit, it’s completely awful! However, we got hints for **Visual Studio Code**.  
What did we do here? We just replaced the parameter types `P` & `R` that used to stand for parameter types and return type, respectively. And instead, we used the **function type** `F` from which we extracted the equivalent of `P` with `Parameters<`;F>`;` and R `with ReturnT`ype<F>. Thus, TypeScript is able to conserve the name of the parameters, even after currying:

![Image](https://cdn-media-1.freecodecamp.org/images/beEnT-ydrNb4m1QxH9HdcWzAym01d9P905lw)

There’s just one thing: when using gaps, we’ll lose the name of a parameter.

_A word for IntelliJ users only: You won’t be able to benefit from proper hints. I recommend that you switch to Visual Studio Code as soon as possible. And it is community-driven, free, much (much) faster, and supports key bindings for IntelliJ users. :)_

### LAST WORDS

Finally, I would like to inform you that there is a current proposal for [variadic types](https://github.com/Microsoft/TypeScript/issues/5453). What you’ve learned here is not going to become obsolete — this proposal aims to ease the **most common** tuple type manipulations, so it is a very good thing for us. In a close future, it will enable easier tuple concatenations like the `Append`, `Concat`, and `Prepend` we’ve built, as well as destructuring and a better way to describe variable function parameters.

That’s it. I know that it’s a lot to digest at once, so that’s why I released a [developer version](https://github.com/pirix-gh/medium/blob/master/types-curry-ramda/src/index.ts) of this article. You can clone it, test it, and change it with TypeScript 3.3.x and above. Keep it close to you and learn from it until you become more comfortable with the different techniques ?.

**High-five ? if you enjoyed this guide, and stay tuned for my next article!**

**EDIT:** [It’s available for Ramda 0.26.1](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/33628)

**Thanks for reading**. And if you have any questions or remarks, you are more  
than welcome to leave a comment.

