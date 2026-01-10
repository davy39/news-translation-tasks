---
title: Introducing ABS, a programming language for shell scripting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T17:33:17.000Z'
originalURL: https://freecodecamp.org/news/introducing-abs-a-programming-language-for-shell-scripting-dfbd737d621
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_BSX61CxShyqW7oT7Kgc8Q.jpeg
tags:
- name: Bash
  slug: bash
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alex Nadalin

  Over the past few days I took some time to work on a project I had in mind for ages,
  a scripting alternative to Bash: let me introduce you to the ABS programming language.


  Why

  Let me keep this brief: we all love shell programming — a...'
---

By Alex Nadalin

Over the past few days I took some time to work on a project I had in mind for ages, a scripting alternative to Bash: let me introduce you to the [ABS programming language](https://www.abs-lang.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/SEQ45gplyveMOk8nKiL8d-w5azHRSEjtC7-8)

### Why

Let me keep this brief: we all love shell programming — automating repetitive tasks without too much effort.

We might probably agree that shell programming is also kind of nuts in terms of syntax:

```
if [ -z $STRING ]; then    ...fi
```

Like, ehm, _what the hell? fi? -z? brackets?_

Fighting with Bash, or the common shell programming language, can get intense from time to time. Writing code such as:

```
if (this == that) {    parts = this.split("/").filter(...).map(...)}
```

will bring tears to your eyes if you’re using the shell.

Now, you can do similar things with any mainstream programming languages (the example above is valid JavasScript): what these languages are not great at is their integration with the underlying system — a [shell is simply much more coincise / powerful](https://stackoverflow.com/questions/796319/strengths-of-shell-scripting-compared-to-python) from that perspective.

Imagine you could run code like:

```
host = $(hostname)
```

```
if (host == "johns_computer") {    ...}
```

Well, you don’t have to “imagine” no more: ABS is a language that combines quick and simple system commands with a more elegant syntax.

Think of it as the best thing since candy, only to remember this is the definition ABS’ author gave you. But seriously, it’s pretty darn convenient.

Don’t believe me? Read on!

### Examples

I’m a firm believer in the “_show me the code!_” mantra, so let’s quickly get to it. Running shell commands is extremely easy in ABS:

```
# Get the content of your hostfile$(cat /etc/hosts)
```

and pipes work too:

```
# Check if a domain is in your hostfile$(cat /etc/hosts | grep domain.com | wc -l)
```

At this point we can just capture the output of our command and script over it:

```
# Check if a domain is in your hostfilematches = $(cat /etc/hosts | grep domain.com | wc -l)
```

```
# If so, print an awesome stringif matches.int() > 0 {  echo("We got ya!")}
```

It won’t happen, but let’s say that _an error_ happens:

```
# Check if a domain is in your hostfilematches = $(cat /etc/hosts | grep domain.com | wc -l)
```

```
if !matches.ok {    echo("How do you even...")}
```

```
# If so, print an awesome stringif matches.int() > 0 {  echo("We got ya!")}
```

We could make this a bit more general:

```
$ cat script.abs# Usage $ abs script.abs domain.com# Check if a domain is in your hostfiledomain = arg(2)matches = $(cat /etc/hosts | grep $domain | wc -l)
```

```
if !matches.ok {    echo("How do you even...")}
```

```
# If so, print an awesome stringif matches.int() > 0 {  echo("We got %s!", domain)}
```

Now, strings are fairly boring, so we can try something more fun:

```
# Say we're getting some JSON from a commandx = $(echo '{"some": {"dope": "json"}}')x.json().some.dope # "json"
```

```
# Arrays, you say?tz = $(cat /etc/timezone) # "Asia/Dubai"parts = tz.split("/") # ["Asia", "Dubai"]
```

```
# You better destructure the hell out of that![continent, city] = tz.split("/")
```

…and so on. There are loads of “regular” things you can do with ABS, so I won’t focus much on those — let me show you the weirder parts instead:

```
# Avoiding the bug that happened because# we forgot to compare strings case-insensitively"HELLO" ~ "hello" # true
```

```
# Just range1..3 # [1, 2, 3]
```

```
# Combined comparison operator (thanks Ruby!)5 <=> 5 # 05 <=> 6 # -16 <=> 5 # 1
```

```
# Classic short-circuiting1 && 2 # 21 || 2 # 1
```

You can skim through the whole [documentation](https://www.abs-lang.org/introduction/why-another-scripting-language) within 15 minutes: ABS’ aim is not to be a general-purpose, feature-loaded language, so the surface isn’t that wide. In addition, if you’ve worked with languages such as JavaScript, Python or Ruby you won’t have troubles getting used to ABS.

### What’s going to happen now?

You can head over to [ABS’ website](https://www.abs-lang.org/), and learn more about the language. The brave ones will instead make a trip to [ABS’s github repo](https://github.com/abs-lang/abs) and [download a release](https://github.com/abs-lang/abs/releases) to install it locally.

The braver ones will just:

```
bash <(curl https://www.abs-lang.org/installer.sh)
```

_(you might need to sudo right before that)_

Which one will you be?

![Image](https://cdn-media-1.freecodecamp.org/images/964Hq52XCeztEs5UKsPayCvFgCTtLfD1pcRZ)
_Photo by [Unsplash](https://unsplash.com/photos/XMFZqrGyV-Q?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Fabian Grohs</a> on <a href="https://unsplash.com/search/photos/programming?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

_Originally published at [odino.org](https://odino.org/introducing-abs-a-programming-language-for-shell-scripting/) (25th December 2018)._  
_You can follow me on [Twitter](https://twitter.com/_odino_) — rants are welcome!_ ?

