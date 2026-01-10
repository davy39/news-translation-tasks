---
title: What is TypeScript? A Beginner's Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-21T15:55:07.000Z'
originalURL: https://freecodecamp.org/news/what-is-typescript-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/blog.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Emmanuel Ohans

  A few weeks ago, I published an Intermediate TypeScript and React Handbook.

  It received many views and I got several emails. Most were “thank you” emails, but
  then there were others like:


  “… I am new to programming, what is TypeScr...'
---

By Emmanuel Ohans

A few weeks ago, I published an [Intermediate TypeScript and React Handbook](https://www.freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript/).

It received many views and I got several emails. Most were “thank you” emails, but then there were others like:

> “… I am new to programming, what is TypeScript?”

And:

> “Thanks for this free ebook, but how do I learn TypeScript as a beginner?”

I had explained at the beginning that the handbook was for intermediate developers who already knew some TypeScript—but when did that ever stop anyone from downloading a free resource! :)

So in this guide, I’ve decided to answer the queries in those emails with the article I wish I had when I learned TypeScript.

Now, if you’re still reading, I’ll assume you’re a TypeScript beginner.

Buckle up. You’re in for a fun ride.

## Explain TypeScript Like I'm 5

My approach to teaching has always remained the same.

If you can’t explain it to a 5-year-old, then perhaps you don’t know the subject well enough.

Instead of overwhelming you with a lot of technical jargon, let’s try something different.

Let’s use an analogy you’ll never forget.

When was the last time you visited the grocery store?

Consider TypeMart:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-134.png)
_The TypeMart grocery store_

TypeMart is your typical **big** grocery store.

You want a variety of grocery items picked up after work? They’ve got you covered.

On the other hand, here’s JMart:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-135.png)
_The JMart grocery store_

JMart is a smaller grocery store for quick purchases.

In Berlin, where I live, we call these [Spätis](https://allaboutberlin.com/glossary/Sp%C3%A4ti#:~:text=A%20Sp%C3%A4ti%20or%20Sp%C3%A4tkauf%20(pronounced,and%20bodegas%20in%20other%20countries.). These are essentially small convenience shops.

But I’m sure you’re not here for a German lesson.

What’s important to us here is how the grocery stores, JMart and TypeMart, work.

### How JMart and TypeMart work

With _JMart_, you go into the shop, find the grocery item you need, and take it over to the cashier.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-136.png)
_Going over to the Cashier to pay your bill_

At this point, you’re not quite sure how much the grocery item you’ve picked costs.

Well, that’s why you go to the cashier!

The cashier takes your item, scans it, and tells you how much it costs.

If they’re “better” at their job, they’ll tell you how much the item costs off the top of their head (or some manual catalog they keep in the drawer).

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-137.png)
_Receiving the bill from the Cashier_

The process seems brittle, but boy does it work!

These cashiers are smart as heck. No items are off limits. And they know what every item costs.

One beautiful Tuesday, you decide to try out _TypeMart_.

You soon realise that things are different in TypeMart.

_"Those pesky big stores,"_ you may say.

Unlike JMart, they’ve got a price tag for everything in the store.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-139.png)
_Basket of fruits with price tags_

They rob you of the thrill and the look on the cashier’s face as they compute your bill.

On the other hand, what they give you is some sort of assurance.

There are no surprises!

You know exactly how much every item you’ve picked up costs.

That is beneficial for days when your wallet is slim.

Every cent matters.

### Why does this analogy matter?

Your intuition was correct.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-140.png)
_JMart represents JavaScript. Typemart, TypeScript._

In the analogy, JMart represents JavaScript and TypeMart, TypeScript.

When you go to a supermarket, there’s an unwritten contract: they promise to have what you need at a fair price.

And you promise to pay for what you buy (except if you’re shoplifting. Don’t do this.)

The same is true for code.

It’s an unwritten contract, but a clear and brutal one.

Your contract is with the user of your application. And you promise that your application works.

Consider an example with a conference call application like Google meet.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-141.png)
_The Google meet web interface. Source: https://shrtm.nu/L0yk_

The promise with Google meet is you’ll always be able to make video calls. They also promise you can mute the button while you chat to your partner or watch a quick TikTok.

Good thing they can’t hear you!

Or so you think?

Imagine if the mute button didn’t do what it promised.

There go your secrets. And with it goes your trust in Google meet.

The same is true for the applications you write.

You promise a working application, and your users trust that’s the case — assuming you’ve earned their trust.

Let’s now bring this home.

In JMart and TypeMart, the goods are money. With software, the goods are data.

Assume you had a basic counter application.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-142.png)
_A basic counter application user interface_

Your user sees a fancy UI, but under the hood what’s really making magic is the counter _variable_ you increase or decrease.

With JMart (analogous to JavaScript), the goods are not labelled (price tagged). You don’t know how much anything costs. You go to the cashier to meet your fate.

This is similar to how JavaScript works.

You define and manipulate all sorts of variables, but there’s no explicit label for what the variables are.

You trust what you’ve written and pass it on to the JavaScript compiler to meet your fate.

Consider the following trivial JavaScript code:

```js
const JMart = {
    bananas: true,
    apples: true,
    mangos: true
}
```

In a standard JavaScript application, you may go ahead to write the following:

```js
const myOrder = JMart.cars.price

```

Even though `cars` does not exist on the `JMArt` object, there’s no explicit label that defines that.

So, as you write your code, you may not know that this line of code is faulty…Until you go to the cashier to meet your fate.

The cashier here is the JavaScript interpreter. Typically, this happens when you run the code in a browser.

If you do, you then get an error that reads `can't read price of undefined`.

If you shipped this code (mistakenly) to production, your uses will be met with this ugly error as well.

You’ve just compromised their trust in your application.

With TypeScript, things are different. Every piece of data is “labelled” just like in TypeMart.

Before you go to the cashier (aka the browser) to run the code, you can tell if your application is working as it should!

The TypeScript compiler will throw an error letting you know you’ve made a mistake accessing an incorrect value.

This happens within your code editor, before you open the application in a browser.

Like picking up a grocery item you can’t afford at TypeMart, you see the price label.

You know what’s in your wallet. It’s fair to say you’ve been warned.

This right here is the major initial difference between TypeScript and JavaScript that you should know.

> TypeScript is JavaScript with syntax for types.

Where types are labels dangling around your grocery item (data), telling you exactly what each piece of code represents.

Consider the following trivial JavaScript example:

```js

const myFunction = (a, b) => {
   return a * b
}

```

In TypeScript, this code could look like this:

```ts
const myFunction = (a: string, b: string) => {
	return a * b
}
```

Note how this looks almost identical to the JavaScript code.

But it’s got a major difference: the data `a` and `b` are `'labelled'`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-143.png)
_The type function parameter type annotations_

This code specifically states that `a` and `b` expected in `myFunction` are strings.

With this information (called type annotation), TypeScript can now show you errors as you write your code.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-144.png)
_View this code in the TypeScript playground: https://shrtm.nu/FlC0_

These errors will usually render in the form of red squiggly lines. Similar to errors in applications like Microsoft Word.

You may then hover over these lines to view the details of the error.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-145.png)
_The details of the TypeScript error_

In this simple example, the crux of the error is that the multiplication operation should not be run on strings.

### Non-exception errors

If you’re a more experienced JavaScript developer, you can already notice that the code example above doesn’t throw an error in standard JavaScript.

```js
const myFunction = (a, b) => {
    return a * b
}

```

If you compute `“1” * "6"` in JavaScript, you’ll get `6`.

Internally, JavaScript coerces the strings to numbers, and performs the multiplication operation.

These sorts of errors that don’t fail in JavaScript, but error out in TypeScript, are called non-exception errors.

These are supposed to help you prevent nasty bugs in your application.

You shouldn’t necessarily worry about this at this stage of your TypeScript journey, but it’s worth mentioning.

As you can see, TypeScript goes far and beyond to help you catch unwanted behaviours in your code.

A simple way to fix this would be to type the parameters explicitly, that is, `a` and `b` as numbers:

```ts
const myFunction = (a: number, b: number) => {
   return a * b
}
```

And away goes the error!

Don’t be made at Typescript for bringing these non-exception errors to your attention.

They are potential sources of bugs in your application.

Typescript to the rescue 💪🏽

## Conclusion

Ask yourself, do I now know what TypeScript is?

Yes, you do – conceptually.

TypeScript is to JavaScript what TypeMart is to JMart.

TypeScript gives you an organised way to _label_ the data within your application to prevent unknown errors.

These errors will be caught and brought to your attention before you go to the cashier – that is, before you run your application.

Take a moment to digest this information. It’ll be crucial as you [learn more TypeScript](https://www.freecodecamp.org/news/an-introduction-to-typescript/).

Give yourself a pat on the back, and go write your first TypeScript application.



### Further Resources

* [Intermediate TypeScript and React Handbook](https://www.freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript/): Learn intermediate Typescript with React by building a strongly typed Polymorphic component.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-148.png)
_[Intermediate TypeScript and React Handbook](https://www.freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript/)_



* Fancy a quick Typescript exercise? Spot and fix the error in the earlier described example. Use the official online editor called the Typescript playground here: [[https://shrtm.nu/FlC0](https://shrtm.nu/FlC0)]

