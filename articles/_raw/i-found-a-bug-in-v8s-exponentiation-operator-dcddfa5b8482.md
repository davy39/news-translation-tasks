---
title: I found a bug in V8’s Exponentiation Operator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T14:35:08.000Z'
originalURL: https://freecodecamp.org/news/i-found-a-bug-in-v8s-exponentiation-operator-dcddfa5b8482
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c61X5rQY1EerMPy61Ud-ng.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Christoph Michel

  I always thought that the new ES6 exponentiation operator [x ** y](https://tc39.github.io/ecma262/#sec-exp-operator-runtime-semantics-evaluation)
  was the same as [Math.pow(x,y)](https://tc39.github.io/ecma262/#sec-math.pow).

  Indee...'
---

By Christoph Michel

I always thought that the new ES6 exponentiation operator `[x ** y](https://tc39.github.io/ecma262/#sec-exp-operator-runtime-semantics-evaluation)` was the same as `[Math.pow(x,y)](https://tc39.github.io/ecma262/#sec-math.pow)`.

Indeed this is what [the specification](https://tc39.github.io/ecma262/#sec-math.pow) says about `Math.pow`:

> Return the result of Applying the ** operator with base and exponent as specified in 12.6.4.

12.6.4 — _Applying the ** Operator_ states that the result is _implementation-dependent_ — but there should still be no discrepancy between `**` and `Math.pow`.

However, evaluating the following in the current V8 JS Engine (Chrome / Node) results in this:

```
console.log('1.35 ** 92', 1.35 ** 92)                   // 978828715394.7672console.log('Math.pow(1.35, 92)', Math.pow(1.35, 92))   // 978828715394.767
```

The exponentiation operator `**` returns a more accurate approximation.

But this is not the only weirdness with the exponentiation operator: Let’s try evaluating the same with variables ([REPL](https://repl.it/@MrToph/ExponentiationBugs)) — it shouldn’t make any difference:

![Image](https://cdn-media-1.freecodecamp.org/images/THt5NNcrKd1S9dd99OY4jUhPB0nw9wrHiY0K)

```
const exponent = 92;console.log(`1.35 ** exponent`, 1.35 ** exponent)                   // 978828715394.767console.log('1.35 ** 92', 1.35 ** 92)                               // 978828715394.7672console.log(`Math.pow(1.35, exponent)`, Math.pow(1.35, exponent))   // 978828715394.767console.log('Math.pow(1.35, 92)', Math.pow(1.35, 92))               // 978828715394.767
```

But it does: `1.35 ** 92` differs from `1.35 ** exponent`.

So what seems to be happening here is that the compiler processes the JS code `1.35 ** 92` which is already [constant folded](https://en.wikipedia.org/wiki/Constant_folding)

This makes sense as V8 really compiles to machine code.

**V8 increases performance by compiling JavaScript to native machine code before executing it, versus executing bytecode or interpreting it.**

V8 works by first interpreting the JS code with their **Ignition Interpreter.** It does a second run with the **TurboFan compiler** [**optimizing** the machine code](https://v8project.blogspot.com/2017/05/launching-ignition-and-turbofan.html).

![Image](https://cdn-media-1.freecodecamp.org/images/TyMWLEdnZyqL2oDHhD8mWqiYH0vsL6vgjp9J)
_From [Understanding V8’s bytecode](https://medium.com/dailyjs/understanding-v8s-bytecode-317d46c94775" rel="noopener" target="_blank" title=")_

TurboFan now does **constant folding.** Its exponentiation algorithm has a better precision than the JIT compiler’s (Ignition) exponentiation algorithm.

If you try the same in other JS engines like Firefox’s _SpiderMonkey_, the result is a consistent value of `978828715394.767` among all computations.

#### Is it a bug?

I would say so, although it wasn’t severe in my code. But it’s still not following the spec that says `Math.pow` and `**` should result in the same value.

If you’re transpiling the code with babel, `x ** y` is translated to `Math.pow(x,y)`, which again leads to discrepancies between transpiled and untranspiled code. As we have seen, `Math.pow(1.35, 92)` is **not** being optimized (only **operators** seem to be optimized by V8). Therefore, `1.35 ** 92` results in different code when [transpiled to ES5](https://babeljs.io/repl/#?babili=false&browsers=&build=&builtIns=false&spec=false&loose=false&code_lz=IwOgzArABAVDUE4BMQ&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=true&fileSize=false&sourceType=module&lineWrap=false&presets=es2015%2Creact%2Cstage-2&prettier=false&targets=&version=6.26.0&envVersion=).

Using this bug and disregarding any clean code practices, we can write a nice function to determine if we’re running on Chrome (unless you transpile your code ?):

```
function isChrome() {    return 1.35 ** 92 !== Math.pow(1.35, 92)}
```

Still more readable than user agent strings. ?

Originally published at [cmichel.io](https://cmichel.io/bugs-in-exponentiation-operator/)

![Image](https://cdn-media-1.freecodecamp.org/images/9APsDGxF26LJJOgAusJLRrMPLw3zBSbLoP8u)

