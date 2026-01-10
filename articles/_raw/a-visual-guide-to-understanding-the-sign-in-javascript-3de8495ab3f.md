---
title: A Visual Guide to Understanding the “=” Sign in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T16:17:24.000Z'
originalURL: https://freecodecamp.org/news/a-visual-guide-to-understanding-the-sign-in-javascript-3de8495ab3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_LfSneHGshm2MhXImfg13w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  The assignment operator, or “=” sign, is actually very misleading for anyone that
  is learning to code for the first time.

  You are taught about the concept of the equals sign for your entire life in math
  class.

  2 x 3 = 6

  x²-4 = 0

  Th...'
---

By Kevin Kononenko

#### The assignment operator, or “=” sign, is actually very misleading for anyone that is learning to code for the first time.

You are taught about the concept of the equals sign for your entire life in math class.

_2 x 3 = 6_

_x²-4 = 0_

The things on the left side of the equation are equal in value to the things on the right side of the equation. They could be flipped at any time, and the statement would still be true.

And then JavaScript comes in like the Kool-Aid man and completely destroys this understanding.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYP5gtpVtBz9YezFdegGWw.gif)

Oh, and don’t get me started with the concept of variables. In algebra class, we are taught that variables can only be equal to numbers that satisfy the equation. For example,

_x²-4x+3 = 0_

In the equation above, _x_ can only be 1 or 3. But in JavaScript, the concept of a variable is actually quite different than what you learnt in algebra class.

This is a **huge** issue! It means that every time a newbie looks at an “=” sign when they are learning about variables, they need to repeat in their head over and over:

_It’s not what you think it means._

_It’s not what you think it means._

_It’s not what you think it means._

I wanted to create a more memorable way to explain variables than re-teaching what an “=” sign means. By the end of this tutorial, you will understand why the “=” in variable assignment is more like **a ramp that loads up a truck**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e478HxvNr4Mdtcb99r0iBw.gif)

This should create a clear guide about the purpose of variables and how to use them throughout your script.

### The Name and the Value of a Variable

**Variables are containers for carrying values within your script.** In some ways, they are the opposite of variables from algebra.

* You can always give them a new value and restart your script. There is no “permanent” equality to satisfy some condition.
* The left side of the **statement** has a completely different purpose than the right side of the statement.

Here is an example:

```
let days = 7;
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wE-bRRODuz52v_ENxM0m_A.png)

This is called **declaring** the variable. It creates a new truck called _days_ that can drive around your script and deliver its **value** OR pick up a new **value**.

* The _let_ **keyword** announces that you are creating a new variable. Or, in the analogy we are about to use, creating a new truck.
* The variable needs a unique **name**, which is _days_ here. This distinguishes this truck from all the other trucks.
* The **assignment operator**, or “=” sign, loads the **value** 7, into the truck.

It is very hard to break the habit of looking at this like it is math class all over again, so I am going to explain a little more about the different parts of the variable truck.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NaoMytaTS9UNi9vyXbU8uw.png)

This is the left side of the variable **statement**. It is not an equation! We are creating a truck with a specific name that we can use over and over again. Any time we look at the left side of the statement, we are calling in a truck with a specific name.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I_Axu1OrB9XKmNPNNokpMg.gif)

The **assignment operator** is just like the ramp of a truck. It loads up a new value. You can load up a new value pretty much any time with the _let_ **keyword**.

As a programmer, we are continuously creating new variables, loading up values and watching the changes around the script.

### Reassigning Values to Variables

So far, we can create a truck that can drive around the script and deliver its value. But what about changing the value that the truck is carrying around?

The _let_ **keyword** allows us to create **mutable** variables whose values can be changed. If we used the const keyword, it would mean that the value is **immutable** and unchangeable.

In JavaScript, unlike math, you can simply **assign** a new value to the variable. Our days variable currently stands for the 7 days in a week. But what if we wanted it to stand for the 5 weekdays? Here is the code we could use.

1. In line 2, we create the _days_ variable with a value of 7.
2. On line 4, we **re-assign** the value of the variable. It is now 5.
3. On line 6, the days truck arrives with the value of 5.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9uGxOUVl7u3xXaPKy_oyyw.gif)

In the GIF above, line 4 puts a new value in the truck that is later used in line 6.

Here is what happens in line 6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TomJtNkR39aAiAzWjzhK_A.gif)

The variable days is not “equal” to anything! It merely carries around the value that you assign to it. This is much more control than you have in math class, where you must discover the value of the variable that satisfies the equation. Now, you are in control!

### Why Do You Need Variables?

Imagine that you are building an App that tells patients when to take their medication. You need to change the number of days per week based on the medication. Here is a quick snippet.

1. In line 2, days gets loaded up with a value of 7.
2. In line 4, the value of 5 gets loaded up instead.

In lines 4 and 6, you use the **value** of the days variable. Could you hard code this by simply putting the number 7 in line 4 and the number 5 in line 6? Of course you could!

But, as your App grows, you will find that variables are helpful for 2 reasons:

1. **Instantly changing all the appropriate values at once.** Let’s say you had three medications that need to be taken for 7 days a week, and three medications that need to be taken for 5 days a week. You don’t want to constantly change the **value** of _days_ back and forth! You would instead want to use two separate variables. That gives you two separate trucks to drive values around your script.
2. **Remembering what a value stands for.** If you hard code a value, you may look back and say, why the heck is that 7? But, if you create a variable, you will remember that it stands for 7 days of the week so you can quickly change it if needed.

### Variable Names on Right Side of the Assignment Operator

So far, we have had a pretty hard rule. The name of the variable is on the left side of the **assignment operator**, while the value is on the right side.

But what if we have a situation like this?

In line 4, the variable name is on both sides of the assignment operator! This is yet another reason why it is NOT an equals sign! In fact, the relationship between the two sides of the statement stays the same.

In line 4, we load up a new value onto the _days_ variable. Here is what that looks like.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CddN2NTkrM4x5M9ad2lEyA.gif)

Notice how we start at the **assignment operator** and calculate the right side of the statement first? That is because we are **assigning** a new value to days here. We cannot touch the left side of the statement. Here is what happens next.

![Image](https://cdn-media-1.freecodecamp.org/images/1*santo6oDTf_Cns6XomXUvg.gif)

The days truck pulls up twice in this case. The first time is on the right side of the equation to deliver the old value. And the second time is on the left side of the equation to pick up the new value for _days_.

Our new **value** for the _days_ variable is 9. In our log statement on line 6, the console would log 9.

#### Call To Action

Did you enjoy this? Give it a clap so others can discover it as well. And, if you want to get notified when I release future tutorials that use analogies, sign up here:

