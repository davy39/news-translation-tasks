---
title: What does it mean when code is “easy to reason about”?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-30T14:52:14.000Z'
originalURL: https://freecodecamp.org/news/what-does-it-mean-when-code-is-easy-to-reason-about-4e6f63eb386f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ksdpItuqJJshToI3D39RaQ.png
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Preethi Kasireddy

  You’ve probably heard the expression “easy to reason about” enough times to make
  your ears bleed.

  The first time I heard this expression, I had no idea what the person meant by it.

  Does it mean functions that are easy to understa...'
---

By Preethi Kasireddy

You’ve probably heard the expression “easy to reason about” enough times to make your ears bleed.

The first time I heard this expression, I had no idea what the person meant by it.

_Does it mean functions that are easy to understand?_

_Does it mean functions that work properly?_

_Does it mean functions that are easy to analyze?_

After a while, I’d heard “easy to reason about” in so many contexts that I figured it was just another semi-meaningless developer buzzword.

…But is it really meaningless?

The truth is, the expression does have a significant meaning. It captures a fairly complex idea, which makes decoding it a bit tricky. Trickiness aside, having a high-level understanding of what “easy to reason about” code looks like absolutely helps us write better programs.

To that end, this post will be dedicated to dissecting the expression “easy to reason about” as it relates to the technical conversations we have as developers.

### Understanding your program’s behavior

Once you’ve written a piece of code, you typically also want to understand the program’s behavior, how it interacts with other parts of the program, and the properties it exhibits.

For example, take the piece of code below. This should multiply an array of numbers by 3.

How can we test that it works as intended? One logical way is to pass a bunch of arrays as input and ensure that it always returns the array with each item multiplied by 3.

Looks good so far. We’ve tested that the function does what we want it to do.

But how do we know it doesn’t do what we **_don’t_** want it to do? For instance, with careful inspection, we can see that the function mutates the original array.

Is that what we intended? What if we need references to both the original array and the resulting array? Too bad, I guess.

Next, let’s see what happens if we pass the same array a bunch of different times — does it always return the same result for a given input?

Uh oh. It looks like when we passed the array **[1, 2, 3]** to the function the first time, it returned **[3, 6, 9]**, but later it returned **[ 49, 98, 147 ]**. Those are very different results.

That’s because the **multiplyByThree** function relies on an external variable **multiplier**. So, if the external state of the program causes the variable **multiplier** to change in between calls to the function **multiplyByThree**, the behavior of the function changes even if we pass the same array into the function.

Eeek. Not looking that great anymore. Let’s dig a little deeper.

So far, we’ve tested perfect array inputs. Now, what if we were to do this:

What in the world?!?

The program looked great on the surface — when we take a few minutes to evaluate it, however, it was a different story.

We saw that it sometimes returns an error, sometimes returns the same thing you passed to it, and only occasionally returns the expected result. Moreover, it has some unintended side effects (mutating the original array) and doesn’t seem to be consistent in what it returns for a given input (since it relies on external state).

Now, let’s look a slightly different **multiplyByThree** function:

Just like above, we can test for correctness.

Looking good so far.

Let’s also test to see if it does what we don’t want it to do. Does it mutate the original array?

Nope. The original array is intact!

Does it return the same output for a given input?

Yep! Since the **multiplier** variable is now within the scope of the function, even if we declare a duplicate **multiplier** variable in the global scope, it won’t affect the result.

Does it return the same thing if we pass a bunch of different types of arguments?

Yep! Now the function behaves more predictably — it either returns an error or a new resulting array.

At this point, how confident are we that this function does exactly what we want it to do? Have we covered all the edge cases? Let’s try a few more:

Damn. Looks like our function still needs a little work. When the array itself contains unexpected items, like **undefined** or strings, we see weird behavior again.

Let’s try to fix it by adding another check in our for-loop checking for invalid array elements:

With this new function, why not try those two edge cases again:

Sweet. Now it also returns an error if any of the items in the array are not numbers instead of some random funky output.

### Finally, a definition

By going through the the above steps, we’ve slowly built up a function that is easy to reason about because it has these key qualities:

1. Does not have unintended side effects
2. Does not rely on or affect external state
3. Given the same argument, it will always return the same corresponding output (also known as “[referential transparency](https://en.wikipedia.org/wiki/Referential_transparency)”).

### Ways we can guarantee these properties

There’s a lot of different ways we can guarantee that our code is easy to reason about. Let’s take a look at a few:

#### **Unit tests**

Firstly, we can write unit tests to isolate pieces of code and verify that they function as intended:

Unit tests like these help us verify that our code behaves correctly and give us living documentation about how small pieces of the overall system work. The caveat with unit tests is that unless you’re very thoughtful and thorough, it’s incredibly easy to miss problematic edge cases.

For example, we would never have figured out that the original array is being mutated unless we somehow thought to test for it. So our code is only as robust as our tests.

#### **Types**

In addition to tests, we might also use types to make it easier to reason about code. For example, if we were using a static type checker for JavaScript like [Flow](https://flowtype.org/), we could ensure that the input array is always an array of numbers:

Types force us to explicitly state that the input array is an array of numbers. They help create restrictions on our code which prevent many kinds of runtime errors like we saw earlier. In our case, we no longer have to think about checking to make sure that each item in the array is a number — this is a guarantee given to us with types.

#### **Immutability**

Lastly, another thing we can do is use immutable data. Immutable data just means that the data cannot be changed once it’s created. This helps avoid unintended side effects.

In our earlier example, for instance, if the input array were immutable, it would have prevented the unpredictable behavior where the original array is mutated. And if the **multiplier** were immutable, it would prevent situations where some other part of the program can mutate our multiplier.

Some of the ways we can reap the benefits of immutability is by using a functional programming language that inherently ensures immutability or by using an external library, like [Immutable.js](https://facebook.github.io/immutable-js/), that enforces immutability on top of an existing language.

As a fun exploration, I’ll use [Elm](http://elm-lang.org/), a typed functional programming language, to demonstrate how immutability helps us:

This little snippet does the same thing as our JavaScript **multiplyByThree** function from before, except it’s now in [Elm](http://elm-lang.org/). Since Elm is a typed language, you’ll see on line 6 that we define the input and output types for the function **multiplyByThree** as both being a list of numbers. The function itself uses the basic **map** operation to generate the resulting array.

Now that we’ve defined our function in Elm, let’s do one last round of the same tests we did for our earlier **multiplyByThree** function:

As you can see, the result is what we expected and the **originalArray** has not been mutated.

Now, let’s throw Elm for a trick and try mutating the multiplier:

Aha! Elm restricts you from doing this. It throws a very friendly error.

What if we were to pass a string as an argument, instead an array of numbers?

Looks like Elm caught that as well. Because we declared the argument as a List of numbers, we cannot pass anything but a List of numbers even if we tried!

We cheated a little bit in this example by using a functional programming language which has both types and immutability. The point I wanted to prove is that with these two features, we no longer have to think about manually adding checks for all the edge cases in order to gain the three properties we discussed. Types and immutability guarantee that for us, and in turn, we can reason about our code more easily ?

### Now it’s your turn to reason about your code

I challenge you to take a moment next time you hear someone say, _“XYZ makes it easy to reason about code”_ or _“ABC makes is difficult to reason about code.”_ Replace that fancy buzzword with the properties mentioned above, and try to understand what the person means. What properties does the piece of code have that makes it easy to reason about?

Personally, doing this exercise has helped me critically think about code and, in turn, has motivated me think about how to write programs that are easier to reason about. I hope it does the same for you too!

I’d love to hear your thoughts on other properties that I might have missed that you think are important. Please leave your feedback in the comments!

