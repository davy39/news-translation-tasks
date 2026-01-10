---
title: Why explicit semicolons are important in JavaScript
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2019-02-03T20:55:20.000Z'
originalURL: https://freecodecamp.org/news/codebyte-why-are-explicit-semicolons-important-in-javascript-49550bea0b82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zX_jJO9HQX5r3WQzQe6xNQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'I am in "Effective JavaScript" training at @PayPalEng by Douglas Crockford
  and cannot express what an enlightening experience it has been! I realized today
  why using explicit semi-colons is so important in JS. Will share my insights soon.
  #javascript...'
---

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I am in &quot;Effective JavaScript&quot; training at <a href="https://twitter.com/PayPalEng?ref_src=twsrc%5Etfw">@PayPalEng</a> by Douglas Crockford and cannot express what an enlightening experience it has been! I realized today why using explicit semi-colons is so important in JS. Will share my insights soon. <a href="https://twitter.com/hashtag/javascript?src=hash&amp;ref_src=twsrc%5Etfw">#javascript</a> <a href="https://twitter.com/hashtag/webdevelopment?src=hash&amp;ref_src=twsrc%5Etfw">#webdevelopment</a> <a href="https://twitter.com/hashtag/PayPal?src=hash&amp;ref_src=twsrc%5Etfw">#PayPal</a></p>&mdash; Shruti Kapoor (@shrutikapoor08) <a href="https://twitter.com/shrutikapoor08/status/1067685062806630400?ref_src=twsrc%5Etfw">November 28, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


#### Gotchas where automatic semicolon insertion can lead to bugs

I took Effective JavaScript training by [Douglas Crockford](http://crockford.com) a few months ago. One thing that stuck with me since then is the importance of using explicit semicolons in JavaScript. For a while, I have been lazily avoiding writing the `;` and assuming the parser will do my job correctly for me. In this post, I want to present some examples that changed my mindset.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zX_jJO9HQX5r3WQzQe6xNQ.png)

### Example 1

What do you expect the output of this to be?

```javascript
const test = () => {
 return 
 {
  ok : true
 }
}
console.log(test())
```

You would expect the output of this to be an `object` with a property `ok` set to `true`. But instead, the output is `undefined`. This is so because since the curly brace starts on a new line, automatic semicolon completion changes the above code to this:

```javascript
const test = () => {
 return;
 {
  ok : true
 }
}
```

**Fix**: Use curly braces on the right of return and explicit semicolons:

```javascript
const test = () => {
 return {
  ok : true
 }
};
```

### Example 2

```javascript
const a = 1
const b = 2
(a+b).toString()
```

What do you think happens in the above code? We get an error `Uncaught ReferenceError: b is not defined.` This is because the parenthesis on the third line is interpreted as a function argument. This code is converted to this:

```javascript
const a = 1;
const b = 2(a+b).toString();
```

> In the circumstance that an assignment statement must begin with a left parenthesis, it is a good idea for the programmer to provide an explicit semicolon at the end of the preceding statement rather than to rely on automatic semicolon insertion.  
>   
> — ECMA-International.org

I have learned to be careful when using automatic semi-colon insertion.

### Further Reading —

1. [Automatic semicolon insertion rules](http://www.ecma-international.org/ecma-262/5.1/#sec-7.9)
2. [Blog post by Bradley Braithwaite inspired by the same lecture](http://www.bradoncode.com/blog/2015/08/26/javascript-semi-colon-insertion/)

### Did you learn something new? Have comments? Know a DevJoke? [Tweet me @shrutikapoor08](https://twitter.com/shrutikapoor08)



<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;I always tell women: when you get to the top, get back in the elevator and bring a woman up with you&quot; - Eunice Kennedy Shriver. Words of wisdom. <a href="https://twitter.com/hashtag/fempire?src=hash&amp;ref_src=twsrc%5Etfw">#fempire</a> <a href="https://twitter.com/hashtag/womenintech?src=hash&amp;ref_src=twsrc%5Etfw">#womenintech</a> <a href="https://twitter.com/hashtag/womenleaders?src=hash&amp;ref_src=twsrc%5Etfw">#womenleaders</a></p>&mdash; Shruti Kapoor (@shrutikapoor08) <a href="https://twitter.com/shrutikapoor08/status/1086029796100923397?ref_src=twsrc%5Etfw">January 17, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



