---
title: Recursive generators and how to not chew up all your memory using them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-07T17:07:44.000Z'
originalURL: https://freecodecamp.org/news/recursive-generator-f8bc30e5e412
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pfeC96_K9bAt1CSAfKC-IA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Jeff M Lowery

  A short while back I wrote a post touching upon combinatorics. Part of the code
  of that article used a Combinator object, which generated combinations of choices
  and stored them in an array.

  The problem with combinatorial operations ...'
---

By Jeff M Lowery

A short while back [I wrote a pos](https://medium.com/@jefflowery/combinatorics-handle-with-care-ed808b48e5dd#.2nv74yf0c)t touching upon combinatorics. Part of the code of that article used a [Combinator](https://gist.github.com/JeffML/0cee0d09d32347ea95e0f9cb4f851cd8) object, which generated combinations of choices and stored them in an array.

The problem with combinatorial operations is that the number of combinations [can grow explosively fast](https://en.wikipedia.org/wiki/Combinatorial_explosion) with every additional choice added — greater than exponentially fast, in some cases.

If I have three items and allow 0, 1, 2, or 3 of those to be chosen, I get 8 unique choices if I **disregard order, allow no repeats and include the null set**. Double that to six items and you wind up with 64 choices (8*8). Double that again (12 items), there are 4096 choices (64*64). In this case, with the restrictions noted above, the number of combinations is 2 to the power of n choices, so it grows merely(!) exponentially.

For a large number of items, storing every combination in an array could lead to memory exhaustion. Instead of having the Combinator return an array only after all combinations have been generated, how about if it returned each combo one-by-one, as needed? Since the Combinator is _generating_ combinations, can it be converted to a [generator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)?

### Original Combinator.js

In the original code, every combination created by calling **combine()** is stored in a **combinations** array:

```js
var Combinator = function (opts) {
    var combinations = [];

    function combine(current, remainder) {
        if (remainder.length === 0) {
            if (current.length >= (opts.min || 0) &&
                current.length <= (opts.max || current.length))
                combinations.push(current);
        } else {
            combine(current.concat(remainder[0]), remainder.slice(1, remainder.length));
            combine(current, remainder.slice(1, remainder.length));
        }
        return this;
    }
    return {
        combinations: combinations,
        combine: combine
    }
}

module.exports = Combinator;
```

The algorithm is embellished a bit with the addition of min/max options — these limit the number of combinations that contain at least **min**, and at most **max**, elements. I can be used like so:

```js
var menu = {
   threeItems: {
        min: 0,
        max: 3,
        values: [1, 2, 3]
    }
}

var threeCombos = new Combinator({
            min: menu.threeItems.min,
            max: menu.threeItems.max
        })
        .combine([], menu.threeItems.values)
        .combinations;
```

The **menu.threeItems.values** property has (surprise!) three values. The **min** and **max** properties determine the set of combinations to be generated. In this case, we ask for sets from 0 length (the null set) to full length (the entire values set). Remember that we’re not interested in order, nor do we allow duplicates. Let see it in action:

```js
console.log('threeCombos.length =', threeCombos.length, threeCombos);

-- output --

threeCombos.length = 8 [ [ 1, 2, 3 ], [ 1, 2 ], [ 1, 3 ], [ 1 ], [ 2, 3 ], [ 2 ], [ 3 ], [] ]
```

Now, instead of using an array to store all combinations, let’s convert this bit of JavaScript to use the new ES6 generator functionality. A generator is a stateful function that yields values one-by-one, in an iterative fashion.

### Naive attempt

A generator function is declared using **function*** instead of **function.** The **yield** operator is called within the generator function to return single values back to the caller. The generator remembers the state of the previous call, so subsequent **yield**s will return the next logical value. The caller uses the **next()** method to get each subsequent value from the generator function. No arrays required!

![Image](https://cdn-media-1.freecodecamp.org/images/1*TEk49bwXt313Cj-_aCL4Bg.jpeg)

I can be pretty lazy at times, so I took the tl;dr approach to the JavaScript [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) on generators and just winged it. The first attempt was:

```js
var CombinatorGenerator = function (opts) {
    function* combine(current, remainder) {
        if (remainder.length === 0) {
            if (current.length >= (opts.min || 0) &&
                current.length <= (opts.max || current.length)) {
                yield(current);
            }
        } else {
            combine(current.concat(remainder[0]), remainder.slice(1, remainder.length))
            combine(current, remainder.slice(1, remainder.length))
        }
    }
    return {
        combine: combine
    }
}
```

This makes sense, right? Instead of pushing a set of choices to an array, I just yield a value. In the client code, I keep calling next() until the generator tells me it’s done.

```js
var menu = require('./menu');
var Combinator = require('./Combinator-generator-naive');

function run() {
    var threeCombos = new Combinator({
            min: menu.threeItems.min,
            max: menu.threeItems.max
        })
        .combine([], menu.threeItems.values);

    for (;;) {
        var it = threeCombos.next();
        if (it.done) {
            console.log("done!")
            break;
        }
        console.log("choice", it.value);
    }
}

run();
```

Alas, my hopes were dashed. The output is:

```
PS C:\Users\Jeff\workspace\Generator> node .\test-generated.js

done!
```

Alright, so obviously the new Combinator is returning before the first yield does, so we’re “done!” before we’re actually done.

### Intuitive attempt

Still loathe to read documentation, I next try to intuit the bug fix. So what happens if I just yield from the internal **combine** calls — logical, no? Instead of:

```js
} else {
            combine(current.concat(remainder[0]), remainder.slice(1, remainder.length))
            combine(current, remainder.slice(1, remainder.length))
        }
```

I try yielding from the recursive calls:

```js
} else {
   yield combine(current.concat(remainder[0]), remainder.slice(1, remainder.length)).next()
   yield combine(current, remainder.slice(1, remainder.length)).next()
}
```

Truly, this will work. So let’s run it:

```bash
PS C:\Users\Jeff\workspace\Generator> node .\generated.js
choice { value: { value: { value: [Object], done: false }, done: false },
  done: false }
choice { value: { value: { value: [Object], done: false }, done: false },
  done: false }
done!
```

Hmmm…that’s no good — what gets returned are the recursive generators’ state, but not the actual values from the **yield** operations.

### Thoughtful attempt

Okay, time to buckle down. A little googling on “recursive generator” turns up a reference to Python’s **yield from.** That syntax delegates the yield calls to another generator. Is there an equivalent in JavaScript?

Yes! — and it’s the **yield*** syntax. This is actually in the document link about [generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*); had I read it, I possibly would have figured this out sooner (laziness, like crime, doesn’t [always] pay). The correct syntax is:

```js
} else {
            yield* combine(current.concat(remainder[0]), remainder.slice(1, remainder.length))
            yield* combine(current, remainder.slice(1, remainder.length))
        }
```

And now, when I call the **combine** method, I see:

```
node .\generated.js
choice [ 1, 2, 3 ]
choice [ 1, 2 ]
choice [ 1, 3 ]
choice [ 1 ]
choice [ 2, 3 ]
choice [ 2 ]
choice [ 3 ]
choice []
done!
```

Good! I’m getting back all the combinations, one-by-one. Success!

Full code used in this post can be found [here](https://github.com/JeffML/Generator). Happy generating!

**_Update 2/26/2017_**

After reading [this article](https://medium.com/javascript-scene/7-surprising-things-i-learned-writing-a-fibonacci-generator-4886a5c87710#.qy4p75tvg) by the indefatigable Eric Elliott, I began to think I had traded one type of resource exhaustion (memory) for another (stack). However, I’ve run the Combinator with an input array of length 30 and it ran to completion: that’s 2³⁰ combinations generated (over a billion). Note that the algorithm

1. is not using tail recursion (or maybe it’s ‘split-tail’ recursion?); and
2. **yield ***, according to Eric’s article, should not be optimized as a tail recursive call in any case

Yet, it works. Proof can be found by running generated30.js in the git repository for this post.

