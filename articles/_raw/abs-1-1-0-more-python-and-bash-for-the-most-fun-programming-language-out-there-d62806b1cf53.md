---
title: 'ABS 1.1.0: more Python and Bash for the most fun programming language out
  there'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T22:39:34.000Z'
originalURL: https://freecodecamp.org/news/abs-1-1-0-more-python-and-bash-for-the-most-fun-programming-language-out-there-d62806b1cf53
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6mI3EvSE3oEnyo9i8g-HBw.png
tags:
- name: Bash
  slug: bash
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Alex Nadalin


  If you missed my previous post, ABS is a programming language that allows you to
  interact with the underlying system with a modern syntax. This is an example of
  it as a version of Bash built in 2019.


  In this article, I’ll discuss a ...'
---

By Alex Nadalin

> If you missed [my previous post](https://medium.freecodecamp.org/introducing-abs-a-programming-language-for-shell-scripting-dfbd737d621), ABS is a programming language that allows you to interact with the underlying system with a modern syntax. This is an example of it as a version of Bash built in 2019.

In this article, I’ll discuss a fresh new release of the [ABS programming language](https://www.abs-lang.org/), bringing more syntax you should be familiar with, inspired both by Bash and Python.

![Image](https://cdn-media-1.freecodecamp.org/images/5OAgXy5TO37WQneW-yytB9mfRRN5GgSTWQmg)

This release includes 8 new features and 2 bugfixes, so let’s discover them together!

### Better membership testing

The membership testing operator, `in`, now supports finding whether an object has a particular key as well as allowing it to find substrings in strings:

```
some in {"some": "thing"} # TRUEsome in {} # FALSE
```

```
"str" in "string" # TRUE"hello" in "string" # FALSE
```

With these changes to `in` we are now deprecating the `set.includes(member)` function:

```
"string".contains("str")[1, 2, 3].contains(2)
```

The function will keep working but, again, is deprecated. We will likely not remove it from future releases (even major ones) but…you’ve been warned!

### 1 ~ 1.1

The similarity operator, `~`, now supports numbers:

```
1 ~ 1.23 # TRUE1 ~ 0.99 # FALSE
```

Numbers will be similar if their integer conversion is the same. This is a shorthand for:

```
1.int() == 1.23.int() # TRUE1.int() ~ 0.99.int() # FALSE
```

### for .. in

We’ve made a few changes to `for .. in` to make it more useful, as you can now loop through hashes:

```
for k, v in {"some": "thing"} {    # k is some     # v is thing }
```

### More destructuring

We introduced destructuring [before ABS was stable](https://github.com/abs-lang/abs/releases/tag/preview-2), [updated it right before 1.0](https://github.com/abs-lang/abs/releases/tag/preview-3), and we’ve now expanded it to be able to destructure hashes:

```
some, thing = {"some": 1, "thing": 1}some + thing # 2
```

### Backtick commands

My _absolute_ favorite feature in this release is the ability to execute commands with the backtick shell syntax:

```
`ls -la`
```

```
# previously you could only do$(ls -la)
```

There were some limitations with the `$()` syntax (namely, a command needs to be on its own line) that are not there anymore with backticks. Now you can do things such as:

```
if `somecommand`.ok {    ...do something...}
```

```
# This is not possible, $() needs its own line$(somecommand).ok
```

The same interpolation style available with `$()` is working with backticks:

```
arg = "-la"`ls $arg`
```

### sleep(ms)

Well…every language has one!

You can now pause execution of a script by sleeping for a certain amount of milliseconds:

```
echo("This will be printed immediately")sleep(10000)echo("This will be printed in 10s")
```

### Hash builtin functions

With this release we’ve added a bunch of new built-in functionalities to hashes:

```
hash = {"a": 1, "b": 2, "c": 3}
```

```
hash.keys() # ["a", "b", "c"]hash.values() # [1, 2, 3]hash.items() # [["a", 1], ["b", 2], ["c", 3]]hash.pop(a) # hash is now {"b": 2, "c": 3}
```

### NULL comparison

In [ABS 1.0.0](https://github.com/abs-lang/abs/releases/tag/1.0.0) we introduced a bug that would make NULL comparison fail:

```
null == null # FALSE
```

In 1.2.0 we fixed it (and backported it to [1.0.2](https://github.com/abs-lang/abs/releases/tag/1.0.2)).

### Index assignments

Assigning to the index of a hash / array now works:

```
array = []array[0] = 1 # array is now [1]array[5] = 1 # array is now [1, null, null, null, null, 1]
```

```
hash = {}hash.x = 1 # hash is now {"x": 1}
```

### What are you waiting for?

```
bash <(curl https://www.abs-lang.org/installer.sh)
```

…and start scripting like it’s 2019!

PS: Again, many thanks to [Erich](https://github.com/ntwrick), who’s been helping me along the way and has become a crucial member of the team over the past few weeks. Just want to make sure his name is mentioned as most of this stuff would not have been possible without him!

PPS: [1.2.0 is already well underway](https://github.com/abs-lang/abs/milestone/9) — expect it within the next 2 to 3 weeks. We’ll be introducing extremely interesting features such as background commands and REPL history, so it’s going to be an exciting release!

_Originally published at [odino.org](https://odino.org/abs-1-dot-1-0-released-a-bit-more-of-python-and-a-bit-more-of-bash-for-the-most-programming-language-out-there/)._  
_You can follow me on [Twitter](https://twitter.com/_odino_) — rants are welcome!_ ?

