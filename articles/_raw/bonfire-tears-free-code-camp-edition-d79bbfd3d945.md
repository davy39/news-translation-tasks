---
title: Crying Algorithm Tears
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-26T07:06:21.000Z'
originalURL: https://freecodecamp.org/news/bonfire-tears-free-code-camp-edition-d79bbfd3d945
coverImage: https://cdn-media-1.freecodecamp.org/images/0*reQ5pMmpwq1G06h-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Women
  slug: women
- name: women in tech
  slug: women-in-tech
seo_title: null
seo_desc: 'By Tiffany White


  “Laughter and tears are both responses to frustration and exhaustion. I myself prefer
  to laugh, since there is less cleaning to do afterward.” ― Kurt Vonnegut


  There comes a point in every new programmers life when they hit a barrie...'
---

By Tiffany White

> “Laughter and tears are both responses to frustration and exhaustion. I myself prefer to laugh, since there is less cleaning to do afterward.” ― Kurt Vonnegut

There comes a point in every new programmers life when they hit a barrier, a wall, a threshold between understanding and not understanding the material at hand.

I hit that threshold yesterday.

And the day before yesterday.

In retrospect, the solution was so simple. I had the right idea several times. I got encouraged, and explained to, and guided, but it was like their words just bounced off of my skull instead of being absorbed into my grey matter.

The algorithm challenge was:

> Check if a string (first argument) ends with the given target string (second argument).

> Remember to use Read-Search-Ask if you get stuck. Write your own code.

> Here are some helpful links:

> String.substr()

The code Free Code Camp started me off with:

```
function end(str, target) { 
```

```
// “Never give up and good luck will find you.” 
```

```
// — Falcor 
```

```
return str; 
```

```
}
```

```
end(“Bastian”, “n”); 
```

#### What the Hell? Substrings?

![Image](https://cdn-media-1.freecodecamp.org/images/0*k9MyKxq8P6tLWagt.gif)

> You’ve done it before and you can do it now. See the positive possibilities. Redirect the substantial energy of your frustration and turn it into positive, effective, unstoppable determination. –Ralph Marston

I knew from looking at the failing tests that my algorithm had to handle strings of different lengths. But I kept hardcoding for just one of the test’s strings.

How do I code this thing for different string lengths? How do I get the length of a string? .length() right? YES. But _how_. Where do I put the .length()?

I had this code:

```
function end(str, target) { 
```

```
     //”Never give up and good luck will find you.” 
```

```
    // — Falcor
```

```
   //’abcdefghijklmn’.substr(0, 3)
```

```
  // ‘abc’
```

```
 //”grab 3 characters starting with the character at address number 0" ​ 
```

```
    var isEqual = str.substr(6, 1) === target.substr(0, 1); 
```

```
    return isEqual;
```

```
} ​ end(“Bastian”, “n”);
```

I found out in one of Free Code Camp’s help chat rooms that you can get to the end of a string by using a negative number. No need to keep popping off all those letters before the “n” on Bastian.

But I continued to hard code for “Bastian” and “n”.

I needed a broader approach.

I tried:

```
function end(str, target) {
```

```
​   var isEqual = str.substr(-1) === target.substr(-1); return isEqual;
```

```
} ​ end(“Bastian”, “n”);
```

But I wasn’t really making any progress. All but one of the tests were passing, and I still wasn’t really utilizing .length() to address the variance in string length.

So I tried this:

```
function end(str, target) {
```

```
    var n = target.length;     var z = str.length;     var isEqual = str.substr(-1) === target.substr(-1); return isEqual;
```

```
} ​ end(“Bastian”, “n”);
```

Same result. I knew I needed to have .length() up there. But where to go after that?

#### Aha!

![Image](https://cdn-media-1.freecodecamp.org/images/0*bGUwwQpIJYjPywvs.gif)

Finally, I had to be guided to the answer. The woman was in Britain and I am pretty sure I was keeping her awake. But together we came up with this solution:

```
// You didn't think I'd give it away, did you?
```

And finally I understood it. It took a while to get there, but when we reached the solution, I felt like a complete idiot. How could I have not understood this earlier?

I cried. I literally cried. Part of that was just me already being emotional.

The other part was me not wanting to put my fist through my MacBook Pro’s screen.

Strings are characters. Not words. And I was totally getting stuck on that.

Algorithm tears indeed.

_Originally published at [Code Newbie in Pittsburgh](http://helloburgh.me/2015/11/26/bonfire-tears-free-code-camp-edition/)._

