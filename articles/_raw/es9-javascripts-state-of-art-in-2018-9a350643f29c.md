---
title: 'ES2018: Javascript''s new features in 2018'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-12T16:14:32.000Z'
originalURL: https://freecodecamp.org/news/es9-javascripts-state-of-art-in-2018-9a350643f29c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xx6p4fNNuiKZe3bHO8M-kQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Flavio H. Freitas

  Our friends from TC39 have released new updates for our beloved JavaScript language.


  If you want to follow the process of the new releases by the committee, you can
  access this link. The process of approving and making a change ...'
---

By Flavio H. Freitas

Our friends from TC39 have [released](https://www.ecma-international.org/publications/standards/Ecma-262.htm) new updates for our beloved JavaScript language.

![Image](https://cdn-media-1.freecodecamp.org/images/bocZipyVNaJoZ43Q0DuUVShsFUBtYgbmhOAH)

If you want to follow the process of the new releases by the committee, you can access this [link](https://github.com/tc39/proposals/blob/master/finished-proposals.md). The process of approving and making a change goes through five stages:

* Stage 0: Strawman — Allow input into the specification
* Stage 1: Proposal — Make the case for the addition; Describe the shape of a solution; Identify potential challenges
* Stage 2: Draft — Precisely describe the syntax and semantics using formal spec language
* Stage 3: Candidate — Indicate that further refinement will require feedback from implementations and users
* Stage 4: Finished — Indicate that the addition is ready for inclusion in the formal ECMAScript standard

More details can be seen [here](https://tc39.github.io/process-document/). If you want to learn more about the previous changes, check out [ES6](https://medium.com/@flaviohfreitas/es6-javascript-does-love-you-f36c532c87db), [ES7](https://medium.com/@flaviohfreitas/es7-a-simple-and-useful-guide-to-master-it-6aba54abb4df) and [ES8](https://medium.freecodecamp.org/es8-the-new-features-of-javascript-7506210a1a22).

So let’s see what they have added or updated in the past year:

### 1. Lots of Regex changes

We have four modifications for regex. Let’s see them:

#### `s` (`dotAll`) flag for regular expressions

While using regular expressions, you expect that the dot `.` matches a single character, but it’s not always true. One exception is with line terminator characters:

```
/hello.bye/.test('hello\nbye') // prints false
```

The solution is the new flag /s (from singleline):

```
/hello.bye/s.test('hello\nbye')  // prints true
```

#### RegExp named capture groups

This is the old way of getting the year, month, and day from a date:

```
const REGEX = /([0-9]{4})-([0-9]{2})-([0-9]{2});const results = REGEX.exec('2018-07-12');console.log(results[1]); // prints 2018console.log(results[2]); // prints 07console.log(results[3]); // prints 12
```

And if you are working with a long regex, you know how hard it is to keep track of the groups, parentheses, and the indices. With the new named capture group, it's possible to:

```
const REGEX = /(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2});const results = REGEX.exec('2018-07-12');console.log(results.groups.year);  // prints 2018console.log(results.groups.month); // prints 07console.log(results.groups.day);   // prints 12
```

#### RegExp Look behind Assertions

There are two versions of look behind assertions: positive and negative.

**a) Positive (?<**=…)

```
'$foo #foo @foo'.replace(/(?<=#)foo/g, 'XXX')// prints $foo #XXX @foo
```

This `(?<=#)fo`o/g regex says that the word must start with # and it doesn’t contribute to the overall matched string (so it won't replace the # character).

**b) Negative (?<**!…)

```
'$foo #foo @foo'.replace(/(?<!#)foo/g, 'XXX')// prints $XXX #foo @XXX
```

On the contrary, this assertion guarantees that it doesn't start with #.

#### RegExp Unicode Property Escapes

Now we can search for characters by mentioning their Unicode character property inside of `\p{}`

```
/\p{Script=Greek}/u.test('μ') // prints true
```

You can check out more of the properties by clicking [here](http://unicode.org/reports/tr18/#RL1.2).

### 2. Rest/Spread Properties

The rest operator `(...)` copies the remaining property keys that were not mentioned. Let's look at an example:

```
const values = {a: 1, b: 2, c: 3, d: 4};const {a, ...n} = values;console.log(a);   // prints 1console.log(n);   // prints {b: 2, c: 3, d: 4}
```

### 3. `Promise.prototype finally`

This new callback will always be executed, if catch was called or not.

```
fetch('http://website.com/files').then(data => data.json()).catch(err => console.error(err)).finally(() => console.log('processed!'))
```

### 4. Asynchronous Iteration

Finally!

Now we can use `await` on our loops declarations.

```
for await (const line of readLines(filePath)) {  console.log(line);}
```

And these are all the changes from this year. Let’s wait to see what they will bring us next year.

_If you enjoyed this article, be sure to like it give me a lot of claps — it means the world to the writer ? And f[ollow me](https://medium.com/@flaviohfreitas) if you want to read more articles about Culture, Technology, and Startups._

**Flávio H. de Freitas** is an Entrepreneur, Engineer, Tech lover, Dreamer and Traveler. Has worked as **CTO** in **Brazil**, **Silicon Valley and Europe**.

