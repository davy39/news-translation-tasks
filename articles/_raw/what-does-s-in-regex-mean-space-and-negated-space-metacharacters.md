---
title: What does S in Regex Mean? Space and Negated Space Metacharacters
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-07T14:09:22.000Z'
originalURL: https://freecodecamp.org/news/what-does-s-in-regex-mean-space-and-negated-space-metacharacters
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--3-.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: "In regular expressions, “S” is a metacharacter that represents space. \n\
  The small letter “s” metacharacter stands for space, and the capital letter “S”\
  \ stands for non-space. That's how the pattern for most metacharacters works. \n\
  For instance, the smal..."
---

In regular expressions, “S” is a metacharacter that represents space. 

The small letter “s” metacharacter stands for space, and the capital letter “S” stands for non-space. That's how the pattern for most metacharacters works. 

For instance, the small letter “d” is the metacharacter for a digit, and the capital letter “D” is the non-digit.

In this article, we'll look at those two variations of the “S” character in RegEx, what they do, and their usage in both RegEx engines and programming.


## What We'll Cover
- [How Do I Make Metacharacters Work?](#heading-how-do-i-make-metacharacters-work)
- [What Does the “S” Metacharacter Do?](#heading-what-does-the-s-metacharacter-do)
- [Examples of “S” Metacharacter Usage](#examplesofsmetacharacterusage)
- [Conclusion](#heading-conclusion)


## How Do I Make Metacharacters Work? 
To make metacharacters work, you need to escape them. 

The reason is that if you only type the “S”, “s”, or “D” metacharacter into a RegEx engine or while writing RegEx in a programming language, it gets interpreted as that letter. 

So, to make metacharacters work in RegEx, you need to escape them with a backslash (`\`).

In the example below, I was able to match the space characters because I escaped the `s`:
![Screenshot-2023-03-07-at-10.18.37](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.18.37.png)

For the example below, I was able to match the numbers because I escaped the `d`:
![Screenshot-2023-03-07-at-10.20.50](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.20.50.png)

## What Does the “S” Metacharacter Do?
As I mentioned earlier, the “S” metacharacter has two forms –  the small letter “s” and the capital letter “S”. 

When it’s in the small letter, it matches all space characters, such as the spacebar, tab, and carriage return.

And when it’s in the capital letter, it matches all non-space characters such as numbers, symbols, and letters. 

Each of the space characters also has their respective metacharacters:

* `\t` for tab
* `\r` for carriage return
* `\n` for a new line


## Examples of How to Use The “S” Metacharacter
You can match all non-space characters with an escaped capital letter “S”:
![Screenshot-2023-03-07-at-10.36.55](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.36.55.png)

You can match all space characters with an escaped  lowercase letter “s”:
![Screenshot-2023-03-07-at-10.18.37-1](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.18.37-1.png)

The `\s` and `\S` metacharacters work fine in any language that supports RegEx. 

Here’s an example in JavaScript:
```js
let regex1 = /\S/g;
let regex2 = /\s/g;

let str1 = 'Allofthesearenonsspacecharacters';
let str2 = `spacebar 
tab 
newLine

`;

console.log(regex1.test(str1)); //true
console.log(regex2.test(str2)); // true
```


## Conclusion
This article showed you what the “S” character means and does in RegEx. 

We looked at how it works (it needs escaping to work), its two forms, and how it works in RegEx engines and JavaScript.

Thank you for reading. Happy coding! 


