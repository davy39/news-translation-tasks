---
title: The Best JavaScript Meme I've Ever Seen, Explained in detail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-30T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/explaining-the-best-javascript-meme-i-have-ever-seen
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/cover-photo.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yazeed Bzadough

  TLDR: Coerce yourself to use triple equals.

  I unintentionally found this JavaScript meme on Reddit, and it''s the best one I''ve
  ever seen.


  You can verify this meme''s accuracy by running each code snippet in Developer Tools.
  The res...'
---

By Yazeed Bzadough

### TLDR: Coerce yourself to use triple equals.

I unintentionally found this JavaScript meme on Reddit, and it's the best one I've ever seen.

![best-js-meme-to-date-2](https://www.freecodecamp.org/news/content/images/2019/07/best-js-meme-to-date-2.png)

You can verify this meme's accuracy by running each code snippet in Developer Tools. The result isn't surprising, but still kind of disappointing.

Of course this little experiment lead me to wonder...

## Why Does This Happen?
![why-does-this-happen](https://www.freecodecamp.org/news/content/images/2019/07/why-does-this-happen.png)

With experience, I've learned to embrace JavaScript's smooth sides while bewaring its prickly pines. Nonetheless, this corner case's details still nicked me.

It's just as Kyle Simpson says...
> "I don’t think anyone ever really knows JS, not completely anyway."

When these cases pop up, it's best to consult the source–the [official ECMAScript specification](http://ecma-international.org/ecma-262/) that JavaScript is built from.

With the spec in hand, let's deeply understand what's going on here.

## Panel 1 - Introducing Coercion
![panel-1-1](https://www.freecodecamp.org/news/content/images/2019/07/panel-1-1.png)

If you run `0 == "0"` in your developer console, why does it return `true`?

`0` is a number, and `"0"` is a string, they should never be the same! Most programming languages respect that. `0 == "0"` in Java, for example, returns this:

```
error: incomparable types: int and String
```

This makes perfect sense. If you want to compare an int and String in Java, you must first convert them to the same type.

But this is JavaScript, y'all!
![this-is-javascript](https://www.freecodecamp.org/news/content/images/2019/07/this-is-javascript.jpeg)

When you compare two values via `==`, one of the values may undergo _coercion_.

> Coercion–**Automatically** changing a value from one type to another.

_**Automatically**_ is the key word here. Instead of you _explicitly_ converting your types, JavaScript does it for you behind the scenes.

![scumbag-javascript](https://www.freecodecamp.org/news/content/images/2019/07/scumbag-javascript.jpeg)

This is convenient if you're purposely exploiting it, but potentially harmful if you're unaware of its implications.

Here's the official [ECMAScript Language Specification](https://www.ecma-international.org/ecma-262/5.1/#sec-11.9.3) on that. I'll paraphrase the relevant part:

> If x is Number and y is String, return x == ToNumber(y)

So for our case of `0 == "0"`:
> Since 0 is Number and "0" is String, return 0 == ToNumber("0")

Our string `"0"` has been secretly converted to `0`, and now we have a match!

```js
0 == "0" // true
// The second 0 became a number!
// so 0 equals 0 is true....
```

![that-string-secretly-became-a-number](https://www.freecodecamp.org/news/content/images/2019/07/that-string-secretly-became-a-number.jpeg)

Weird right? Well get used to it, we're not even halfway done.

## Panel 2 - Arrays Get Coerced Too
![panel-2](https://www.freecodecamp.org/news/content/images/2019/07/panel-2.png)

This nonsense isn't limited to primitives like strings, numbers, or booleans. Here's our next comparison:

```js
0 == [] // true
// What happened...?
```

Coercion again! I'll paraphrase the spec's relevant part:
> If x is String or Number and y is Object, return x == ToPrimitive(y)

Three things here:

### 1. Yes, arrays are objects
![arrays-are-objects](https://www.freecodecamp.org/news/content/images/2019/07/arrays-are-objects.jpg)

Sorry to break it you.

### 2. Empty array becomes empty string
Again [according to the spec](https://www.ecma-international.org/ecma-262/5.1/#sec-8.12.8), JS first looks for an object's `toString` method to coerce it.

In the case of arrays, `toString` joins all of its elements and returns them as a string.

```js
[1, 2, 3].toString() // "1,2,3"
['hello', 'world'].toString() // "hello,world"
```

Since our array's empty, we have nothing to join! Therefore...
```js
[].toString() // ""
```

![empty-array-coerces-to-empty-string-1](https://www.freecodecamp.org/news/content/images/2019/07/empty-array-coerces-to-empty-string-1.jpeg)

The spec's `ToPrimitive` turns this empty array into an empty string. References are [here](https://www.ecma-international.org/ecma-262/5.1/#sec-9.1) and [here](https://www.ecma-international.org/ecma-262/5.1/#sec-8.12.8) for your convenience (or confusion).

### 3. Empty string then becomes 0
![empty-strings-become-0](https://www.freecodecamp.org/news/content/images/2019/07/empty-strings-become-0.jpeg)

You can't make this stuff up. Now that we've coerced the array to `""`, we're back to the first algorithm...

> If x is Number and y is String, return x == ToNumber(y)

So for `0 == ""`
> Since 0 is Number and "" is String, return 0 == ToNumber("")

`ToNumber("")` returns 0.

Therefore, `0 == 0` once again...

![coercion-every-time-2](https://www.freecodecamp.org/news/content/images/2019/07/coercion-every-time-2.jpeg)

## Panel 3 - Quick Recap
![panel-3-1](https://www.freecodecamp.org/news/content/images/2019/07/panel-3-1.png)

### This is true
```js
0 == "0" // true
```

Because coercion turns this into `0 == ToNumber("0")`.

### This is true
```js
0 == [] // true
```

Because coercion runs twice:
1. `ToPrimitive([])` gives empty string
2. Then `ToNumber("")` gives 0.

So then tell me...according to the above rules, what should this return?
```js
"0" == []
```

## Panel 4 - FALSE!
![panel-4-1](https://www.freecodecamp.org/news/content/images/2019/07/panel-4-1.png)

FALSE! Correct.

This part makes sense if you understood the rules.

Here's our comparison:
```js
"0" == [] // false
```

Referencing the spec once again:
> If x is String or Number and y is Object, return x == ToPrimitive(y)

That means...
> Since "0" is String and [] is Object, return x == ToPrimitive([])

`ToPrimitive([])` returns empty string. The comparison has now become

```js
"0" == ""
```

`"0"` and `""` are both strings, so JavaScript says _no more coercion needed_. This is why we get `false`.

## Conclusion
![just-use-triple-equals](https://www.freecodecamp.org/news/content/images/2019/07/just-use-triple-equals.jpeg)

Use triple equals and sleep soundly at night.

```js
0 === "0" // false
0 === [] // false
"0" === [] // false
```

It avoids coercion entirely, so I guess it's more efficient too!

But the performance increase is almost meaningless. The real win is the increased confidence you'll have in your code, making that extra keystroke totally worth it.

## Want Free Coaching?
If you'd like to schedule a **free** 15-30 minute call to discuss Front-End development questions regarding code, interviews, career, or anything else [follow me on Twitter and DM me](https://twitter.com/yazeedBee).

After that if you enjoy our first meeting, we can discuss an ongoing coaching relationship that'll help you reach your Front-End development goals!

## Thanks for reading
For more content like this, check out <a href="https://yazeedb.com">https://yazeedb.com!</a>

Until next time!


