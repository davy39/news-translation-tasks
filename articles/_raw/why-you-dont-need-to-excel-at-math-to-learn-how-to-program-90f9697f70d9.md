---
title: Why you don’t need to excel at math to learn how to program
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-10T17:50:11.000Z'
originalURL: https://freecodecamp.org/news/why-you-dont-need-to-excel-at-math-to-learn-how-to-program-90f9697f70d9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*a_YBHDaex8qNOUBV.
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pau Pavón

  This is probably one of the greatest misconceptions I’ve ever heard.

  If you want to program, you must be good at math. It’s totally fake. Let me explain.

  You don’t need to excel at math to learn to code

  I started coding when I was 12 yea...'
---

By Pau Pavón

This is probably one of the greatest misconceptions I’ve ever heard.

If you want to program, you must be good at math. It’s totally fake. Let me explain.

### You don’t need to excel at math to learn to code

I started coding when I was 12 years old. The math I knew was addition, subtraction, multiplication, and division. And it was **more than enough** to get me into the programming world. Even today, I don’t use anything more complex than powers or square roots.

If you have ever programmed any line of code, you have hopefully realized it has almost nothing to do with math. If you know how to count, you are pretty much good to go.

### The origin of the myth

I believe I’ve figured out where this ‘myth’ comes from. You know those old (or not so old) movies about hackers and programmers. They often show computers with lots of 0s and 1s in a greenish font, flowing vertically along the screen? That’s binary code (and it doesn’t normally move around the screen, it’s just static text).

Computers understand binary code, but that’s not what programming languages are about. It may sound quite obvious, because if you are reading this you probably have some kind of relationship with this world. But you’d be amazed to see how many people think it’s all about binary.

![Image](https://cdn-media-1.freecodecamp.org/images/zzjUB1ePlD2vT4wPb2rx2aO4YZGyrrLmYLCX)
_When I code, my screen doesn’t look like this. Maybe I’m doing something wrong. Photo by [Unsplash](https://unsplash.com/@markusspiske?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Markus Spiske</a>on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

But besides this misconception, I think the other factor is the relation established between the words _math_ and _logic_. Programming requires logical thinking, and math also does. But golf and basketball both require a ball to be played with, and that doesn’t mean you need to know how to play basketball to take up golf.

### Making you believe what I just said

Let’s take a proper example. Imagine you want to build a function to print out the multiplication table of a number. So, for input 2, our function will return:

> 2 x 0 = 0

> 2 x 1 = 2

> 2 x 2= 4

> 2 x 3 = 6

> …

> And up to 2 x 10 = 20

You will see how little math is required to do this (even though we are calculating something ‘mathematical’). For the purpose of this example, we’ll be using JavaScript.

First, we declare the **function**. We’ll call it **_tableOf(n)_**, where _n_ is the number we want to print the table of.

```
function tableOf(n) {
```

```
//rest of the code
```

```
}
```

Pretty easy for the moment. Now we’ll implement something called a **for loop.** This is similar to a function except for the fact that, when it reaches the end, it goes back to the beginning until some condition is true

We want to print _n_ times some other value (let’s call it _i_) until that value reaches 10. We have to also take into account that _i_ should start from 0, as we want _n x 0 = 0_ to be the first line printed. The code could be as following:

```
for(i = 0; i < 11; i++) {
```

```
console.log(n, 'x', i, '=', n*i);
```

```
}
```

Let’s review what we just did. We started the for loop with _i = 0_, meaning that _i_ starts from 0 (as we wanted). Then we say i < 11, meaning that we don’t want to exit the loop unt_i_l i equals 11 or, in other words, we want the loop to continue _i_f i is less than 11. Then we _do_ i++, which means that we increase the value _o_f i by 1 every time the loop starts again (so it eventually reaches 11 and exits the loop).

Then we just output _n_ (the number we entered), ‘x’ (for the _times_ symbol), _i_(the number for which _n_ is multiplied by), ‘=’ (for the _equals_ symbol), and finally _n*i_ (the actual operation, _n times i_).

The previous code, combined:

```
function tableOf(n) {
```

```
for(i = 0; i < 11; i++) {
```

```
console.log(n, 'x', i, '=', n*i);
```

```
}
```

```
}
```

```
tableOf(2);
```

And it works. Is this difficult math? The only math we did was increasing _i_ by one (adding), and checking if _i_ was less than 11. For this concrete example, we also multiplied _n_ times _i_. **Wow**.

### The other side of the coin

Learning to code will make you better at math.

As I said before, programming requires logical thinking just as math does. While writing your programs, you’ll encounter a lot of problems that need to be solved. Most of the time with logic (but let’s be honest, sometimes trial and error works just fine).

Developing the skills to solve these problems is definitely going to help you with math — not only with the concepts, but with problem-solving. You can extend this to other disciplines as well, such as physics.

I hope this article serves to encourage people that want to give coding a try to do it. Trust me, I knew little about math and less about English, and I was still able to learn a lot. Knowledge has no limits.

