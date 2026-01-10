---
title: Why you should use column-indentation to improve your code’s readability
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T04:43:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-columnize-your-code-to-improve-readability-f1364e2e77ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EWTTZDqP8okovm5BF4QPFA.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Leonardo Carreiro

  I think that the most important aspect of programming is the readability of the
  source code that you write or maintain. This involves many things, from the syntax
  of the programming language, to the variable names, comments, and ...'
---

By Leonardo Carreiro

I think that the most important aspect of programming is the readability of the source code that you write or maintain. This involves many things, from the syntax of the programming language, to the variable names, comments, and indentation. Here I discuss the last one of these, **indentation**.

It’s not about indentation size, or the choice between tabs and spaces, or if it should be required in a language such as Python. A lot of people like to use a maximum line length for each line of code, usually 80 or 120 characters. With this idea, there is no maximum length, and sometimes you’ll need to use the horizontal scrollbar. But don’t freak out, it is not for the whole code — it’s just for some parts of it.

### Four examples of improvements using code indentation

#### First example

Take a look at this code:

The readability is not so good, and you could end up with something like this to avoid the mess:

And your seven lines have turned into almost 40 lines. This with just three or four properties per object. If it was eight properties, it would become 70 lines.

The idea that I’m talking about is to use something like this (I call it “column- indented” code):

#### Second example

It’s not just for object literals. It can be used for any piece of code that is a group of similar lines. This process can be quick. You can copy the first line, paste it, and then overwrite the changing pieces in each line.

It can be used in JS `import` too. Compare these two versions:

These thirteen imports are alphabetically ordered by the path. All of them are from the `vs` folder — five from `vs/base` and eight from `vs/platform`.

You can’t see that without moving your eyes back and forth across each line. Doing this is annoying. Of course, you don’t need to make statistics about how your files are importing others. But at some time you will read this code to see if you imported something from the correct file, or if a file was already imported.

Now see how it looks when the same code is column-indented:

Doesn’t that make it a little better?

#### Third example

In this example, we have a method declaration from TypeScript compiler:

Again, you can see the difference between the lines more easily. It helps you to read all the five lines at the same time, spending way less effort. And, if you need to add a parameter in each of these 5 lines, you can do it just one time, using the [multiline cursor](https://stackoverflow.com/a/30039968) in almost all code editors.

#### Fourth example

Here is the final example, with the original and comparison together:

**Pros**:

* Your code looks cleaner.
* Your code has improved readability
* You may be able to reduce the number of lines in your code

**Cons**:

* The auto-formatting option of code editors can interfere with the layout
* When adding one line to a block of lines, sometimes you have to change all the other lines
* It can be time-consuming to write code

### What tools can help to achieve this?

I did indentation this way, manually, for some time. It’s boring, but once you start doing it, you can’t stop. You look at your code, all those repeated lines that could be column-indented to be more readable, and you can’t go on without doing it. It’s addictive.

I use Visual Studio and Visual Studio Code, so I tried to find an extension or plugin that helps achieve this. I didn’t find any. So in November 2017 I started to create my own extension for Visual Studio Code and named it [Smart Column Indenter](https://marketplace.visualstudio.com/items?itemName=lmcarreiro.vscode-smart-column-indenter).

I published a first **usable** version in the same month. Take a look at how it works:

![Image](https://cdn-media-1.freecodecamp.org/images/1*gIMmQyMNnEpLgqAUcDTOUA.gif)
_“Smart Column Indenter” for Visual Studio Code_

There are areas where the extension could be improved. Currently, it only works with `*.ts`, `*.js` and `*.json` files. I think that it could help with XML and HTML files too, like column-indenting the same attributes of repeated tags, or different tags that are repeated in a group of lines.

Once the code is selected for column-indentation, the algorithm works in three steps:

1. Lexical analysis (or tokenization) of the code. I installed the [TypeScript npm package](https://www.npmjs.com/package/typescript) as a dependency and used the Compiler API to avoid reinventing the wheel here.
2. Execute the [Longest Common Subsequence (LCS)](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) algorithm passing each line of code as a sequence of tokens. This is the hard part. A lot of references on the internet talk about the LCS for just two sequences as input, which is easily solved with **dynamic programming**. As we usually want to column-indent more than two lines of code, the problem becomes finding the longest common sequence (LCS) of multiple strings. [This is a NP-hard problem](http://ieeexplore.ieee.org/document/5530316/?reload=true). As this is a generic problem, I created a separated npm package ([multiple-lcs](https://www.npmjs.com/package/multiple-lcs)) with a basic implementation to accomplish this. It isn’t the best solution in some cases, but it is workable.
3. Rewrite the code to column-indent the tokens that appear in the LCS. Each token in the LCS is placed in a new column.

For some types of tokens, such as strings or variables names, the type name is used instead the content in the LCS algorithm. The result is a larger sub-sequence.

I put all the logic in a separate npm package ([smart-column-indenter](https://www.npmjs.com/package/smart-column-indenter)). If you want to create an extension or plugin like this for another JavaScript-based IDE, you can use this package.

My initial reason to create this solution was proof-of-concept. I would like to know what other programmers think about my solution. **If you liked it, please clap**.

If you have constructive criticism, or know of other tools that do the same thing, please leave a comment. This is an [article that I found useful](http://www.draconianoverlord.com/2016/09/16/one-true-way-of-indenting.html).

Thanks for reading.

**Update (2018–03–29):** After it was published a few days ago, I got a lot of feedback, most of them are negatives, but thank you all anyway, it’s good to know why a lot of people don’t like it. I found out later that people usually call it “code alignment”, you won’t find anything about “column indentation”, so if you want to search more about this, search for “code alignment” instead. I did it, and I found an interesting [blog post from Terence Eden’s Blog](https://shkspr.mobi/blog/2014/11/why-i-vertically-align-my-code-and-you-should-too/), as most of the negative comments are about issues with VCS merges, history and dirty diffs, I’ll copy his conclusion: “If our tools make understanding those ideas more difficult, it’s the tools which need to change — not us.”

**Update (2018–05–03):** As if someone at GitHub team had read the negative comments about code alignment here, [now you can ignore white spaces in code review](https://blog.github.com/2018-05-01-ignore-white-space-in-code-review/).

**Update (2018–05–20):** If you use Visual Studio (not Code), [Shadman Kudchikar](https://www.freecodecamp.org/news/how-to-columnize-your-code-to-improve-readability-f1364e2e77ba/undefined) made a similar extension, you can read about it [here](https://medium.com/@kudchikarsk/sharp-column-indenter-visual-studio-extension-d167aaddf11f) or download it [here](https://marketplace.visualstudio.com/items?itemName=kudchikarsk.sharp-column-indenter).

### Factoid

We have now 22" screens with 1920x1080 resolution. There is no reason to limit yourself to 80 characters per line, although you need to decide on the maximum limit. The origin of this 80-characters limit is:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UV-JCMR337fEAsvCF2eVuw.jpeg)
_[More than one person has wondered this](https://softwareengineering.stackexchange.com/a/148678" rel="noopener" target="_blank" title=")._

