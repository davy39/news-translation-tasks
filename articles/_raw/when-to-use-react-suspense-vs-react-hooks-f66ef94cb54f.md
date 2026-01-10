---
title: When to use React Suspense vs React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T13:59:44.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-react-suspense-vs-react-hooks-f66ef94cb54f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7vvZM3wS9aUoDvyqt3yR9Q.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Vitalii Akimov

  React Suspense is to a Monad as Hooks are to Applicative Notation

  Monads and Applicative Functors are extensively used in functional programming.
  There is a relationship between them and React Suspense for Data Fetching and React
  Ho...'
---

By Vitalii Akimov

#### React Suspense is to a Monad as Hooks are to Applicative Notation

Monads and Applicative Functors are extensively used in functional programming. There is a relationship between them and React Suspense for Data Fetching and React Hooks APIs. This is a quick and simple introduction to Monads and Applicatives along with a description of their similarities.

The post is about future React Suspense for Data Fetching, not about recently released React Suspense for Code Splitting (`React.Suspense` and `React.lazy`) .

#### Monad do-notation

The React framework approach encourages developers to use functional programming techniques. At least component render functions should not have observable side effects. JavaScript has no way to ensure this, but there are programming languages which can. For example, Haskell doesn’t accept side effects at all.

Pure functions make the code modular, predictable and easier to verify. But they also significantly increase verbosity. Here is a statement from [Phil Walder](https://en.wikipedia.org/wiki/Philip_Wadler)’s [Monads for functional programming](https://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf)(1995) tutorial:

> It is with regard to modularity that explicit data flow becomes both a blessing and a curse. On the one hand, it is the ultimate in modularity. All data in and all data out are rendered manifest and accessible, providing a maximum of flexibility. On the other hand, it is the nadir of modularity. The essence of an algorithm can become buried under the plumbing required to carry data from its point of creation to its point of use.

Monads solve this problem for Haskell. And Suspense/Hooks solve the same problem in React.

So what is a Monad? It is a simple abstract interface which has two functions, let’s call them `of` and `chain`.

* `of` — takes any value and returns some monadic (effectful) value
* `chain` — takes an effectful value and a function from any value to an effectful one and returns another effectful value

The effectful values there may encapsulate any concrete implementation-specific information. There are no requirements what exactly it should be, it is some opaque data. The interface’s concrete implementations should follow a set of laws, and this is it.

There is nothing to say more about monads since they are abstract. They don’t necessarily store anything, wrap or unwrap anything or even chain anything.

But why do we need this if it is so abstract and defines almost nothing? The interface provides an abstract mean to compose computations with side effects.

If you write code in JavaScript, you may wonder now. You’ve already composed a lot of computations with side effects without seeing any Monad. But in fact, you can consider you’ve already used them there.

In computer science, Monads first appeared for studying side effects in imperative languages. They are a tool to embed imperative worlds into a pure math world for further studying.

This way if you want to convert your imperative program into math formulas representing it, doing this with Monad expressions would be the simplest and the most straightforward way. It is so straightforward what you don’t even need to do it manually, there are tools that do it for you.

Haskell has a syntax sugar called do-notation exactly for this. This makes writing imperative programs in Haskell possible. There is a special tool in its compiler. It converts such imperative programs into a Monadic pure Haskell expressions. The expressions are close to math you see in textbooks.

JavaScript is an imperative language. We can consider any imperative code to be a do-notation already. But unlike the one in Haskell’s, it is not abstract. It works only for built-in side effects. There is no way to add support of any new one except extending the language.

There are such extensions, namely generators, async and async generator functions. JavaScipt JIT compiler converts async and generator functions into concrete built-in API calls. Haskell doesn’t need such extensions. Its compiler converts do-notation into abstract Monads interface function calls.

Here is an example of how async functions simplify sources. This shows again why we need to bother having a syntax for effects.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uPPyZSrp-3AuABxNnfPhmA.gif)
_from [@manekinekko](http://www.async-await.xyz" rel="noopener" target="_blank" title="">www.async-await.xyz</a> by Wassim Chegham (<a href="https://twitter.com/@manekinekko" rel="noopener" target="_blank" title="))_

For this post, we need only two JavaScript built-in effects. Let’s call them Mutation and Exception. They have clear meanings. Mutations allow changing values of some references. JavaScript has the Exceptions effect embedded using `throw`/ `try-catch` statements.

We can convert some effects into others. This way we can write async code using Generators.

This conversion trick can be applied to other effects too. And apparently, just Mutation and Exception are enough to get any other effect. This means we can turn any plain function into an abstract do-notation already. And this is exactly what Suspense does.

When the code encounters some effectful operation and requires suspension it throws an exception. It contains some details (for example a Promise object). One of its callers catches the exception, waits while the promise in the argument is settled, stores the resulting value in a cache, and re-runs the effectful function from the beginning.

After the Promise is resolved the engine calls the function again. The execution goes from its start, and when it encounters the same operations it returns its value from the cache. It doesn’t throw an exception and continues execution until the next suspension request or the function’s exit. If the function doesn’t have any other side effects its execution should go the same paths and all pure expressions are recalculated producing the same values.

Let’s re-implement Suspense. Unlike React, this one works with the abstract Monads interface. For simplicity, my implementation also hides a resource cache. Instead, the runner function counts invoked effects and uses the current counter value as a key for the internal cache. Here is the runner for the abstract interface:

```js
/** effectful expression throws this object if it requires suspension */
const token = {};

/** Pointer to mutable data used to record effectful computations */
let context;

/** Runs `thunk()` as an effectful expression with `of` and `chain` as Monad's definition */
const run = (of, chain) => thunk => {
  /** here it caches effects requests */
  const trace = [];
  const ctx = {trace};
  return step();
  function step() {
    const savedContext = context;
    ctx.pos = 0;
    try {
      context = ctx;
      return of(thunk());
    } catch(e) {
      /** re-throwing other exceptions */
      if (e !== token)
        throw e;
      const {pos} = ctx;
      return chain(ctx.effect,
                   (value) => {
                     trace.length = pos;
                     /* recording the resolved value */
                     trace[pos] = value;
                     ctx.pos = pos + 1;
                     /** replay */
                     return step(value);
                   })
    } finally {
      context = savedContext;
    }
  }
}

/** marks effectful expression */
const M = eff => {
  /* if the execution is in a replay stage the value will be cached */
  if (context.pos < context.trace.length)
    return context.trace[context.pos++];
  /* saving the expression to resolve in `run` */
  context.effect = eff;
  throw token;
}
```

Now let’s add a concrete Async effects implementation. Promises, unfortunately, aren’t exactly monads since one Monad law doesn’t hold for them, and it is a source of subtle problems, but they are still fine for our do-notation to work.

Here is concrete Async effect implementation:

```js
const runPromise = run(
  v => Promise.resolve(v), 
  (arg, f) => arg.then(f));
```

And here’s a simple example, it waits for delayed values before rendering proceeds:

%[https://codesandbox.io/s/714n51l6mq?from-embed]

The sandbox also contains `Component` wrapper. It turns an effectful functional component into a React component. It simply adds `chain` callback and updates the state accordingly. This version doesn’t have a fallback on threshold feature yet, but the last example here does have it.

The runner is abstract, so we can apply it for something else. Let’s try this for the `useState` hook. It is a Continuation monad, not a State monad as its name may suggest.

Effectful value here is a function which takes a callback as an argument. This callback is called when the runner has some value to pass further. For example when the callback returned from `useState` is called.

Here, for simplicity, I use single callback continuations. Promises have one more continuation for failure propagation.

```js
const runCont = run(
  value => cont => cont(value),
  (arg, next) => cont => arg(value => next(value)(cont)));

const useState = initial =>
  M(cont => 
    cont([initial, function next(value) { cont([value,next]); }]));
```

And here is a working usage example, with most of “kit.js” copy-pasted, except the monad’s definition.

%[https://codesandbox.io/s/j79mv6yv0v?from-embed]

Unfortunately, this is not exactly the `useState` hook from React yet, and the next section shows why.

#### Applicative do-notation

There is another extension for do-notation in Haskell. It targets not only Monad abstract interface calls but also calls of Applicative Functors abstract interface.

Applicative interfaces shares the `of` function with Monads and there is another function, let’s call it `join`. It takes an array of effectful values and returns a single effectful value resolving to an array. The resulting array contains all the values to which each element of the argument array was resolved.

I use a different one from Haskell’s interface. Both are equal though — it is simple to convert Haskell’s interface into the one used here and back. I do this because this basis is much simpler to use in JavaScript, it doesn’t need any higher-order functions, and there is already its instance in the standard runtime.

In Haskell and in JavaScript any Monad is immediately an Applicative Functor. This means we don’t need to write a concrete implementation of Applicative interface, we can generate it automatically.

If there is a default implementation, why do we need Applicative Functors? There are two reasons. The first one is not all Applicative Functors are Monads, so there is no `chain` method from which we can generate `join`. Another reason is, even if there is `chain`, custom `join` implementation can do the same thing in a different way, probably more efficiently. For example, fetching resources in parallel rather than sequentially.

There is an instance of this interface for Promises in the standard runtime. It is `Promise.all`(ignoring some details here for simplicity again).

Let’s now return to the state example. What if we add another counter in the component?

%[https://codesandbox.io/s/3k0j3olk61?from-embed]

The second counter now resets its value when the first one is incremented. It is not how Hooks are supposed to work. Both counters should keep their values and work in parallel.

This happens because each continuation invocation erases everything after it in the code. When the first counter changes its value the whole next continuation is re-started from the beginning. And there, the second counter value is 0 again.

In the [run function implementation](https://medium.com/dailyjs/react-suspense-as-a-monad-notation-and-hooks-as-an-applicative-notation-f66ef94cb54f#fae1), the invalidation happens at line 26 — `trace.length = pos` — this removes all the memorized values after the current one (at `pos`). Instead, we could try to diff/patch the trace instead. It would be an instance of Adaptive Monad used for incremental computations. MobX and similar libraries are very similar to this.

If we invoke effectful operations only from a function’s top level, there are no branches or loops. Everything will be merged well overwriting the values on the corresponding positions, and this is exactly what Hooks do. Try to remove the line in the code sandbox for two counters above.

#### Transpiler alternative

Using Hooks already makes programs more succinct, reusable and readable. Imagine what you could do if there were no limitations (Rules of Hooks). The limitations are due to runtime-only embedding. We can remove these limitations by means of a transpiler.

[Effectful.JS](https://github.com/awto/effectfuljs) is a transpiler for embedding effectful into JavaScipt. It supports both Monadic and Applicative targets. It greatly simplifies programs in the designing, implementing, testing, and maintaining stages.

Unlike React Hooks and Suspense, the transpiler doesn’t need to follow any rules. It works for any JavaScript statement (branches, loops, exceptions etc). It never re-plays functions from the beginning. This is faster. Plus the functions can use any JavaScript built-in side effect.

Effectful.JS is not exactly a transpiler but rather a tool to create transpilers. There are also a few predefined ones and a lot of options for tuning. It supports double-level syntax, with special markers for effectful values (like `await`expressions in async functions, or Haskell’s do). And it also supports a single level syntax where this information is implicit (like Suspense, Hooks or languages with Algebraic Effects).

I’ve quickly built a Hooks-like transpiler for demo-purposes — [@effectful/react-do](https://github.com/awto/effectfuljs/tree/master/samples/react-do). Calling a function with names starting with “use” is considered effectful. Functions are transpiled only if their name starts with “use” or they have “component” or “effectful” block directive (a string at the beginning of the function).

There are also “par” and “seq” block-level directives to switch between applicative and monadic targets. With “par” mode enabled the compiler analyzes variable dependencies and injects `join` instead of `chain` if possible.

Here is the example with two counters, but now adapted with the transpiler:

%[https://codesandbox.io/s/mzp619y8wj?from-embed]

For demo purposes, it also implements Suspense for Code Splitting. The whole function is six lines long. Check it out in the runtime implementation [@effectful/react-do/main.js](https://github.com/awto/effectfuljs/blob/master/samples/react-do/main.js). In the next example, I’ve added another counter which rendering is artificially delayed for demo purposes.

%[https://codesandbox.io/s/nwmxwnp34j?from-embed]

#### Algebraic Effects

Algebraic Effects are often mentioned along with Suspense and Hooks. These may be internals details or a modeling tool, but React doesn’t ship Algebraic Effects to its userland anyway.

With access to Algebraic Effects, users could override operations behavior by using own Effect Handler. This works like exceptions with an ability to resume a computation after `throw`. Say, some library function throws an exception if some file doesn’t exist. Any caller function can override how it can handle it, either ignore or exit process, etc.

EffectfulJS doesn’t have built-in Algebraic Effects. But their implementation is a tiny runtime library on top of continuations or free monads.

Invoking a continuation also erases everything after the corresponding `throw`. There is also special syntax and typing rules to get Applicative (and Arrows) API — [Algebraic Effects and Effect Handlers for Idioms and Arrows](http://homepages.inf.ed.ac.uk/slindley/papers/aeia.pdf). Unline Applicative-do this prohibits using any anything which requires Monad operations.

#### Wrapping up

The transpiler is a burden, and it has its own usage cost. Like for any other tool, use it only if this cost is smaller than the value you get.

And you can achieve a lot with EffectfulJS. It is a new way to write JavaScript programs. It is useful for projects with complex business logic. Any complex workflow can be a simple maintainable script.

As an example, Effectful.JS can replace Suspense, Hooks, Context, and Components State with tiny functions. Error Boundaries are the usual `try-catch` statements. Async rendering is an async scheduler. But we can use it for any computations, not only for rendering.

There are a lot of other awesome application-specific uses, and I’m going to write more about them soon. Stay tuned!

