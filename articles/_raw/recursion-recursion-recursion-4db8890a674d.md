---
title: Recursion, Recursion, Recursion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-27T07:51:06.000Z'
originalURL: https://freecodecamp.org/news/recursion-recursion-recursion-4db8890a674d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3E0JXxCCMTTKYtlmwONWbA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Michael Olorunnisola

  Before I tell you what recursion is, you should read this article:

  Recursion, Recursion, Recursion_Before I tell you what recursion is, you should
  read this article:_medium.freecodecamp.com

  Give yourself a pat on the back if y...'
---

By Michael Olorunnisola

Before I tell you what recursion is, you should read this article:

[**Recursion, Recursion, Recursion**](https://medium.freecodecamp.com/recursion-recursion-recursion-4db8890a674d)  
[_Before I tell you what recursion is, you should read this article:_medium.freecodecamp.com](https://medium.freecodecamp.com/recursion-recursion-recursion-4db8890a674d)

Give yourself a pat on the back if you didn’t fall for that one. If you did, no worries — you now know what recursion is!

> People often joke that in order to understand recursion, you must first understand recursion. — John D. Cook

When I first started coding, I thought about recursion all the time. I used to think of it as some magic spell, or some higher order technique that only the best of the best developers used to solve the hardest problems.

As it turns out, it’s not magic at all. But good developers do understand it. And great developers understand when it’s best to use it.

So what exactly is recursion?

Have you ever practiced something over and over again until the point where you “got it down?” Then you’ve preformed a recursive act.

Plainly speaking, you executed a task or series of steps repeatedly until you reached some desired goal. That, my friends, is the essence of recursion.

In code speak, a recursive function is a function which calls itself.

Before we jump into any code, let’s walk through a basic example to understand the structure of recursive functions. Since the piano is near and dear to my heart, we will make a function called practicePiano.

Every time this function is called with a person, that person will practice the piano. Since I don’t spend enough time practicing right now, I should get a little practice in.

```
practicePiano(person){  practiceScales(person);    practiceChords(person);}
```

```
practicePiano('Michael');
```

I’ve called the function above once, so I was able to get one session in, but I definitely need more than one to really get better.

```
practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');...
```

This is great and all, but it breaks one of programming’s greatest tenets: Don’t Repeat Yourself (DRY).

I was able to get more practice sessions in, but every time I want to practice more, I have to add another call to practicePiano.

One way we can solve this problem is by calling the function within itself, so every time I practicePiano, I practice more:

```
practicePiano(person){  practiceScales(person);    practiceChords(person);
```

```
//Recursive magic here!
```

```
  practicePiano(person);}
```

```
//Now we only need one of these!
```

```
practicePiano('Michael');
```

This is awesome! I only have to call it once. The only problem is, once I call this function… I never stop practicing. I never stop until it is literally impossible for me to practice anymore.

```
//Our code above would behave as follows:
```

```
  practiceScales('Michael');    practiceChords('Michael');
```

```
//Recursive Call
```

```
  practiceScales('Michael');    practiceChords('Michael');
```

```
//Recursive Call
```

```
  practiceScales('Michael');    practiceChords('Michael');
```

```
//Recursive Call
```

```
//..till I can't physically practice anymore
```

When your computer reaches a similar point where it’s unable to continue it usually returns this error:

```
RangeError: Maximum call stack size exceeded
```

That is the equivalent of your computer saying, “I’ve run out of space, and had to close up shop.” It has recorded each function call in memory in a stack. But since the calls never stop, the stack gets completely filled and the computer is forced to stop. (This is where the name for the popular website, Stack Overflow, comes from.)

So going back to my never ending piano practice, how can we keep my hands from falling off?

This is where we see the importance of a term you may have heard before: **the base case**.

In recursive functions the base case is the goal you are trying to achieve or the task you are looking to complete. The base case’s job is to tell your function when it should stop.

In our analogy, that goal can be practicing until I’m tired.

```
practicePiano(person){   if (tired(person)){ //When I am finally tired    console.log("Guess you can take a break now...");    return ;  //This will return out of the function and stop the recursive call  }
```

```
  practiceScales(person);    practiceChords(person);
```

```
//Recursive magic here!
```

```
  practicePiano(person);}
```

```
//Now when we call this here...I'll only practice over and over again until I'm tired
```

```
practicePiano('Michael');
```

This is where most developers run into problems. Although our current piano practice analogy is a simplification, it drives home an extremely important point: what if I never got tired of practicing? Then the base case we wrote would not resolve our “Maximum call stack size exceeded” error.

Before we jump straight into coding, it’s important to take the time to reflect on all the possible situations that can — and should — stop our recursive calls.

As a developer, you’ll write complex algorithms, which may take variable inputs and use recursion to achieve some goal.

You may develop a base case or multiple base cases that you believe will be reached by your recursive call. But that may not always be the case.

Consider the case of my cyborg counterpart:

```
practicePiano(person){   if (tired(person)){    console.log("Guess you can take a break now...");    return ;    }
```

```
 if (handsFallOff(person)){   console.log("Go see a doctor about that");    return ; }
```

```
  practiceScales(person);    practiceChords(person);
```

```
  practicePiano(person);}
```

```
practicePiano('Cyborg-Michael'); 
```

```
//Cyborg-Michael never gets tired//Nor do his hands ever fall off//Back to being stuck practicing forever...
```

Given this, it’s important to always make sure you are thorough in developing your base case(s) and certain your function behaves in a way that a base case will always be reached.

In our example, a logical base case would be being able to play some piece like Beethoven’s 5th.

Refactoring our code, we now have:

```
practicePiano(person, song){   if (tired(person)){    console.log("Guess you can take a break now...");    return ;    }
```

```
 if (handsFallOff(person)){   console.log("Go see a doctor about that");    return ; }
```

```
 if (song(person)){   console.log("Great Job! Time to learn this on the guitar!");    return ; }
```

```
  practiceScales(person);    practiceChords(person);
```

```
  practicePiano(person, song);}
```

```
practicePiano('Cyborg Michael', BeethovenFifth); 
```

```
//The Cyborg version of me never gets tired//Nor do my hands ever fall off//But, being a cyborg...I can learn Beethoven's 5th pretty quickly
```

This is the power of recursive solutions. With a few lines of code, I’m able to achieve some task, for which I may not know how many steps it may take. I may need 100 practice session, whereas my cyborg self will only need 5, but this solution will still work for the both of us.

So to recap, just remember the following:

1. Recursion allows you to easily repeat a task to accomplish some goal.
2. The base case(s) should be thorough enough to allow your recursive function to actually reach a conclusion (and not run forever).
3. Recursion helps you keep your code DRY (again, you’ll hear this acronym a lot, so remember that it stands for “Don’t repeat yourself” —oops, I just did!)

### More recursion to come

We’ll go more in-depth into recursion in my upcoming series on data structures. During this deep dive, we’ll get a look into how you can start to use [time complexity analysis](https://medium.freecodecamp.com/time-is-complex-but-priceless-f0abd015063c#.huo7yk6wy) and recursion in your everyday code. We’ll also work through various looping methods to understand why it may be better to use one over the other.

As an aside, one of the topics we didn’t get a chance to cover here are [factorial](https://en.wikipedia.org/wiki/Factorial) problems. Factorial problems are where you find recursive solutions applied most often as they require recursively iterating some defined number of times. You can find more specifics regarding solving factorial problems in this [awesome article](https://www.sitepoint.com/recursion-functional-javascript/) by SitePoint.

Here are some additional resources to help out:

[**Khan Academy on Recursion**](https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion)   
[_Learn for free about math, art, computer programming, economics, physics, chemistry, biology, medicine, finance…_www.khanacademy.org](https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion)[**SparkNotes: What is Recursion?: What is Recursion?**](http://www.sparknotes.com/cs/recursion/whatisrecursion/section1.rhtml)  
[_A summary of What is Recursion? in 's What is Recursion?. Learn exactly what happened in this chapter, scene, or…_www.sparknotes.com](http://www.sparknotes.com/cs/recursion/whatisrecursion/section1.rhtml)[**mybrainishuge/recursion-prompts**](https://github.com/mybrainishuge/recursion-prompts)  
[_recursion-prompts - Repository of prompts to be solved using recursion_github.com](https://github.com/mybrainishuge/recursion-prompts)

Also, thanks to [Yara Tercero](https://yctercero.github.io/) for helping edit this.

