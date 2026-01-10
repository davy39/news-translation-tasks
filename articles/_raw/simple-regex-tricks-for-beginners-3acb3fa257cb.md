---
title: Simple RegEx tricks for beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T16:40:49.000Z'
originalURL: https://freecodecamp.org/news/simple-regex-tricks-for-beginners-3acb3fa257cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wUY_k-Q4q-z10Zo425qC5Q.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrei Chernikov

  Always wanted to learn Regular Expressions but got put off by their complexity?
  In this article, I will show you five easy-to-learn RegEx tricks which you can start
  using immediately in your favorite text editor.

  Text Editor Setup...'
---

By Andrei Chernikov

Always wanted to learn Regular Expressions but got put off by their complexity? In this article, I will show you five easy-to-learn RegEx tricks which you can start using immediately in your favorite text editor.

### Text Editor Setup

While almost any text editor supports Regular Expressions now, I will use Visual Studio Code for this tutorial, but you can use any editor you like. Also, note that you usually need to turn on RegEx somewhere near the search input. Here is how you do this in VS Code:

![Image](https://cdn-media-1.freecodecamp.org/images/GjEq59Gj7Io7MWY4OuayOCmqZo0f5ezXyvOS)
_You need to enable RegEx by checking this option_

### 1) `.` — Match Any Character

Let’s start simple. The dot symbol `.` matches any character:

```
b.t
```

![Image](https://cdn-media-1.freecodecamp.org/images/tMEDSKS2mHfOfqYTQP-elCZI5OnGUObC484v)

Above RegEx matches `"bot”`, `"bat”` and any other word of three characters which starts with `b` and ends in `t`. But if you want to search for the dot symbol, you need to escape it with `\`, so this RegEx will only match the exact text `"b.t"`:

```
b\.t
```

![Image](https://cdn-media-1.freecodecamp.org/images/anNgoajLGzpFhPWYRnVGlowi0bL4Z4xni59R)

### 2) .* — Match Anything

Here `.` means _“any character”_ and `*` means _“anything before this symbol repeated any number of times.”_ Together (`.*`) they mean _“any symbol any number of times.”_ You can use it, for example, to find matches starting with or ending in some text. Let’s suppose we have a javascript method with the following signature:

```
loadScript(scriptName: string, pathToFile: string)
```

And we want to find all calls of this method where`pathToFile` points to any file in the folder `“lua”` . You can use the following Regular Expression for this:

```
loadScript.*lua
```

Which means, _“match all text starting with`“loadScript”` followed by anything up to the last occurrence of `“lua”`“_

![Image](https://cdn-media-1.freecodecamp.org/images/wCWC964KLZKxEHdW0fZlr4Z-X-vdcbYX-ogk)
_`loadScript.*lua: matches everything starting with "loadScript" and ending in "lua"`_

### 3) ? — Non-Greedy Match

The `?` symbol after `.*` and some other RegEx sequences means “match as little as possible.” If you look at the previous picture, you will see that text `“lua”` is seen twice in every match, and everything up to the second `“lua”` was matched. If you wanted to match everything up to the first occurrence of `"lua"` instead, you would use the following RegEx:

```
loadScript.*?lua
```

Which means, _“match everything starting with`"loadScript"` followed by anything up to the first occurrence of `"lua"`"_

![Image](https://cdn-media-1.freecodecamp.org/images/NnHX2yevennzK3Z9ddpq1NPBsbfWnyalfFrw)
_`loadScript.*?lua: matches` everything starting with loadScript and up to the first occurrence of “lua”_

### 4) ( ) $ — Capture Groups and Backreferences

Okay, now we can match some text. But what if we want to change parts of the text we found? We often have to make use of capture groups for that.

Let’s suppose we changed our `loadScript` method and now it suddenly needs another argument inserted between its two arguments. Let’s name this new argument `id`, so the new function signature should look like this: `loadScript(scriptName, id, pathToFile)`. We can’t use normal replace feature of our text editor here, but a Regular Expression is exactly what we need.

![Image](https://cdn-media-1.freecodecamp.org/images/hRdlYnNzYuX64kcVoXrvtH2RfwaY3FzNZedD)
_loadScript\(.*?,.*?\)_

Above you can see the result of running the following Regular Expression:

```
loadScript\(.*?,.*?\)
```

Which means: _“match everything starting with `"loadScript("` followed by anything up to the first `,`, then followed by anything up to the first `)`”_

The only things which might seem strange here for you are the `\` symbols. They are used to escape brackets.

We need to escape symbols `(` and `)` because they are special characters used by RegEx to capture parts of the matched text. But we need to match actual bracket characters.

In the previous RegEx, we defined two arguments of our method call with the `.*?` symbols. Let’s make each of our arguments a separate **capture group** by adding `(` and `)` symbols around them:

```
loadScript\((.*?),(.*?)\)
```

If you run this RegEx, you will see that nothing changed. This is because it matches the same text. But now we can refer to the first argument as `$1` and to the second argument as `$2`. This is called backreference, and it will help us do what we want: add another argument in the middle of the call:

Search input:

```
loadScript\((.*?),(.*?)\)
```

Which means the same thing as the previous RegEx but maps arguments to capture groups 1 and 2 respectively.

Replace input:

```
loadScript($1,id,$2)
```

Which means _“replace every matched text with text `“loadScript(“` followed by capture group 1, `“id”`, capture group 2 and `)`”._ Note that you do not need to escape brackets in the replace input.

![Image](https://cdn-media-1.freecodecamp.org/images/w27UNrc7N2hkWAO1DmU6p0gulIYiwU-oYjpT)
_Replacement Result_

### 5) [ ] — Character Classes

You can list characters you want to match at a specific position by placing `[` and `]` symbols around these characters. For example, class `[0-9]` matches all digits from 0 to 9. You can also list all digits explicitly: `[0123456789]` — the meaning is the same. You can use dash with letters too, `[a-z]` will match any lowercase Latin character,`[A-Z]` will match any uppercase Latin character and `[a-zA-Z]` will match both.

You can also use `*` after a character class just like after `.`, which in this case means: _“match any number of occurrences of the characters in this class”_

![Image](https://cdn-media-1.freecodecamp.org/images/2aTqw0lDyht0cE1gqoF3O5eYcemyzhIBhSzU)
_expect.*to.equal\([0–9]*\): Match only those lines where we expect tested variable to equal a number_

### Last Word

You should know that there are several RegEx flavors. The one I discussed here is javascript RegEx engine. Most modern engines are similar, but there may be some differences. Usually, these differences include escape characters and backreferences marks.

I urge you to open your text editor and start using some of these tricks right now. You will see that you can now complete many refactoring tasks much faster than before. Once you are comfortable with these tricks, [you can start researching more into regular expressions](https://www.regular-expressions.info/).

**Thank you for reading my article to the end. Add claps if you found it useful and subscribe for more updates. I will publish more articles on regular expressions, javascript, and programming in general.**

