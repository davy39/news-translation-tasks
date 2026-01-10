---
title: What Does M Mean in Regular Expressions? M Flag for RegEx
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-26T14:31:31.000Z'
originalURL: https://freecodecamp.org/news/what-does-m-mean-in-regular-expressions-m-flag-for-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/mFlagRegex.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'In regular expressions, "m" is a flag that signifies multiple lines. So,
  it is popularly called the "multiline flag".

  In this article, I will show you what the "m" flag does and how you can use it in
  both regex engines and JavaScript.

  What Does the "...'
---

In regular expressions, "m" is a flag that signifies multiple lines. So, it is popularly called the "multiline flag".

In this article, I will show you what the "m" flag does and how you can use it in both regex engines and JavaScript.


## What Does the "m" Flag Do?
Sometimes, you want your matches not to occur only in a single line but also reach other lines below the first one. This is when the multiline flag is influential. 

Almost all the popular regex engines out there have a way you can toggle on and off the multiline flag.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-12.48.37.png)
_RegEx 101_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-12.49.25.png)
_RegExr_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-12.48.50.png)
_RegEx Tester from Dan's Tools_

## How to Use the "m" Flag in RegEx Engines
If you want your matches not to be limited to the first line while using a regex engine, all you need to do is toggle on the "m" flag.

![Screenshot-2023-04-26-at-13.04.45](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-13.04.45.png)

I have the multiline flag turned on and it’s not matching all the lines. Why that?

That’s because many times, you also have to use the global ["g"] flag with the "m" flag so you can get all the matches:
![Screenshot-2023-04-26-at-13.06.23](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-13.06.23.png)


## How to Use the "m" Flag in JavaScript Regular Expressions
Remember that to use the regular expressions flag in JavaScript, you have to specify it as the second argument of a `RegExp()` constructor. And if you are creating your Regex with slashes, the flags have to be outside of the slashes.

```js
// a flag is the second argument of a RegExp constructor
const regex1 = new RegExp('line', 'gm');

// a flag is the letter outside when you create regex with two forward slashes
const regex2 = /line/gm;
```

Here’s how I use the "m" in conjunction with the "g" flag to match multiple lines in JavaScript:

```js
const regex2 = /line/gim;

const multiLineStr = `Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7`;

console.log(regex2.test(multiLineStr)); // true

if (regex2.test(multiLineStr)) {
  console.log('There are multiple matches'); // There are multiple matches
} else {
  console.log('Found no match');
}
``` 


## Conclusion
You can now see how useful the multiline flag is in getting matches across all lines of text. 

If you found the article helpful, don’t hesitate to share it with your friends and family.

Happy coding!


