---
title: How To Approach Any Algorithm Interview Without Panicking
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T19:29:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-approach-any-algorithm-interview-without-panicking-b6d7ae5c050
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ltLHswL2X4LBTKWEQ2RXQw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: interview
  slug: interview
- name: jobs
  slug: jobs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sun-Li Beatteay

  Let’s be honest, algorithm problems are still very much a part of the job search.
  While there’s an ever-expanding list of companies that don’t make you jump through
  coding hoops, the average developer will encounter a live algorith...'
---

By Sun-Li Beatteay

Let’s be honest, algorithm problems are still very much a part of the job search. While there’s an [ever-expanding list of companies](https://github.com/poteto/hiring-without-whiteboards) that don’t make you jump through coding hoops, the average developer will encounter a live algorithm challenge sometime in their job hunt. Especially if you want to work for a Big Four or an established startup. So through the hoops we jump.

I don’t need to talk about how stressful technical interviews can be. I’m sure most of us know the frustration of walking out of an interview we just bombed and cycling through all the ways we could’ve turned it around. It’s not a fun feeling.

That’s why I’m writing this. For those of you who do end up in an algorithm challenge, how you approach it can make all the difference. Are you the type of person who dives in head-first and figures it out along the way? Or do you have a process you follow to break down the problem into manageable pieces? While the former method may work for some, I exercise the latter.

For me, having a set of steps to use to break a problem down is crucial. While it doesn’t guarantee me a solution or job offer, it allows me to manage my stress response. Keeping my panic at a tolerable level helps me to focus. After all, technical interviews should be about demonstrating your ability to problem solve — not your ability to handle multiple people silently judging you without passing out.

In this article, I want to show you the process I have honed through several technical screens and dozens of mock interviews. It is heavily influenced by the [Launch School’s PEDAC system](https://medium.com/launch-school/solving-coding-problems-with-pedac-29141331f93f). I use it every single time and it has served me well.

> “Fall in love with the process and the results will come.” — Eric Thomas

The best way to show my process is to demonstrate it in action. So let’s work through a problem together. And to make this as authentic as possible, I’ll pick a problem I’ve never solved before. Though you’re going to have to take my word for it.

According to [Leetcode](https://leetcode.com/), the [String to Integer](https://leetcode.com/problems/string-to-integer-atoi/) algorithm is a popular interview question. It also has the lowest completion rate of any Medium ranking problem. This should be a good challenge.

I also picked this problem as it is somewhat practical. This is an actual algorithm that has been implemented in most programming languages. Unlike many other interview challenges (looking at you [Coin Change](https://leetcode.com/problems/coin-change/)), engineers have actually used this algorithm in real life.

With that said, let’s dive in. Feel free to follow along in whatever language you want. I will use JavaScript. You can try out my approach or use your own. See if you can even solve it before I do at the end of this post. You might end up one step closer to creating our own language.

### Step 1: Rephrase the problem in your own words

![Image](https://cdn-media-1.freecodecamp.org/images/0*RLFsUv1fOvXw5omy)

For me, this is the most important step. This is my chance to ask my interviewer questions to clarify the requirements and parse out all the crucial information. Furthermore, rewriting the problem into my words gives me the chance to form a mental model and digest the problem.

For this problem, one question I would ask is whether I’m allowed to use type casting. While the description doesn’t specify it, I will only use JavaScript’s native type casting to convert one character at a time. That’s the sort of restriction I would expect to find in an actual interview.

After reading the description, these are the key details I came up with.

```
// Given a string, return its appropriate number value.
```

```
// Ignore all white-space at the beginning of the string.
```

```
// Number may begin with a negative or positive.
```

```
// All characters that come after the number should be ignored.
```

```
// String is invalid if a character that is not a white-space or sign comes before the number.
```

```
// If string does not contain any integer values, it is invalid.
```

```
// The return value for any invalid string is 0.
```

```
// Resulting integer cannot be larger than (2^31) — 1 or smaller than -(2^31).
```

Just from these requirements, I’m already starting to envision how I will create this algorithm. It will probably require some looping and quite a bit of conditional logic.

Some people would probably start coding after this step. For me, it’s still a bit too early to formulate any concrete plans — but my gears are turning.

### Step 2: Input and output types

Many people will see this as a pointless step, but I always make sure to get the inputs and outputs of the algorithm. Either as a code comment or in the corner of the whiteboard.

It serves two functions. First, it solidifies what the parameters of my function will be and what the signature will look like. Leetcode already created the function signature for me but this won’t be the case in an actual interview.

Second, I keep a reminder of the types I’ll be working with. It’s not unheard of for a candidate to fail all the test cases because they forgot to return a string and not an array. I may or may not be speaking from experience…

For our problem, the inputs and outputs are nicely defined in the title.

```
Input: stringOutput: 32-bit signed integerSignature: myAtoi(str)
```

### Step 3: Examples and Edge Cases

![Image](https://cdn-media-1.freecodecamp.org/images/0*OcGarO2HdqOSlZIB.png)

Now that I’m confident of the inputs and outputs, I want to come up with some test cases. These examples need to cover all the edge cases I can think of. I can only imagine the number of times a candidate has created a working solution, only to have the interviewer come up with an edge case they missed — causing their solution to fall apart.

It’s possible that your interviewer will provide some, but I would come up with even more — especially if they aren’t exhaustive. For example, Leetcode has given me some decent test cases.

```
In: “4193 with words”Out: 4193
```

```
In: “words and 987”Out: 0
```

```
In: “-91283472332”Out: -2147483648
```

However, these examples are missing some possibilities. What if the number starts with a `+`? Or what if multiple signs come before a number, such as `-+-50`?

Let’s make some better ones.

```
Input: “+50.890”Output: 50
```

```
Input: “ -+100”Output: 0
```

```
Input: “ !another invalid -10”Output: 0
```

### Step 4: Data Structure(s)

![Image](https://cdn-media-1.freecodecamp.org/images/0*RMV6tgCYXkYKvMMn.png)

Most, if not all, algorithm code challenges involve using a structure to keep track of your data. It’s important to consider which data structure(s) you will use as it will impact your implementation.

I know from the problem description that I will be dealing with strings and integers. But will I use another data structure to help convert from one to the other?

One issue I can already foresee is keeping track of the places of each digit (tens, hundreds, thousands, etc). Since I will not know the length of my integer beforehand, I will use an **array** to keep track of the integer characters. The array will serve as the interim placeholder for each character before they are converted into the final integer.

While there is most likely a more space efficient solution, I can optimize my solution later. Right now, I just want to go with what makes the most sense for me. It’s better to get a working naive solution than to shoot for the moon and not finish anything.

### Step 5: Pseudocode

![Image](https://cdn-media-1.freecodecamp.org/images/1*88cH0lTO7R2ypVsg0FDJsw.png)

My penultimate step is to spend some time laying out my algorithm in pseudocode. Interviewers want to see how you think and approach problems. Pseudocode is perfect for that.

An added benefit is that the interviewer will know how to assist you ahead of time. There have been times where I’ve gotten stuck on a problem only to have my interviewer provide subtle hints to keep me going. If you jump into coding without a plan, you could end up confusing both yourself and your interviewer. Do each of you a favor and create an action plan.

This is what I came up with.

```
// Start with index = 0
```

```
// While character at current index is white-space  // increment index
```

```
// Check if next character is invalid  // return 0
```

```
// Check if next character is positive or negative sign  // If negative sign, mark number as negative  // increment index
```

```
// Loop through characters starting at current index  // If current character is integer    // Unshift into front of array    // Increment index  // Else, break out of loop
```

```
// Loop through string integer array   // Cast string character into integer  // Multiply integer by (10^index) and add to return value
```

```
// If string contained negative sign, multiply result value by -1// If result value is less than min, reassign to min// If result value is greater than max, reassign to max
```

```
// return value
```

It may seem like I came up with this out of nowhere, but there was a lot of deliberation and trial-and-error behind the scenes. This is the most time-consuming step because this is where the algorithm is created.

Read over the requirements, inputs/outputs, and edge cases. Ask questions, clarify concepts, and isolate areas of uncertainty to focus on. Find the simplest solution you can think of and work from there.

Will you need a depth-first search? Sliding window? Divide and conquer? Something else?

If this is the step you struggle with the most, don’t worry. It will get easier with practice. And practice you should. A thorough algorithm design in pseudocode will make the next step fast and easy.

### Step 6: Code!

“**Finally!**” You’re probably thinking. “**That took forever!**”

Indeed, I spend a lot of time in planning mood. If an interviewer gives me 45 minutes to finish, I will spend 15–30 minutes thinking and mentally digesting.

> “Give me six hours to chop down a tree and I will spend the first four sharpening the axe.” — Abraham Lincoln

In fact, coding is the least important step for me. All the heavy lifting has already been done. Now I just need to interpret my mental model into code.

Additionally, how I code this solution in an interview setting won’t be the same as how I code it in real life. Heck, a real interview solution would look different than the answer I came up with for this article. Several factors affect how I code in an interview, such as time and responsiveness of the interviewer.

Without access to Google or sufficient time to refactor, I just want to write something that works. And there’s no guarantee I would even achieve that.

But that’s not the point of this post. Yes, it’s possible I wouldn’t have solved this question in an interview. But up until this point, I have de-structured the challenge into its key components. I know I _can_ solve it and I have put myself in the best position to do so. A good interviewer will see that.

In a technical screen or onsite, it’s not about the code. It’s how you come up with it.

If you are interested in comparing solutions, here’s the one I came up with:

This solution is not the most efficient. According to Leetcode, it only beats 25% of the other submissions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8SAs6MGc9y2xNx4j7EjJ3Q.png)

However, it would pass most technical interviews. An interviewer might ask me to optimize it for space or time, but those are things that can be included on further iterations if time permits. You don’t need to come up with them on the first try.

The point of using a process is to have a systemic approach to break down any challenge. It works whether you use in your job on a daily basis or in a technical interview. By using it in an interview, you can keep your panic at bay by focusing on the challenge and not your emotions.

If you don’t have a process, start making one. You can use [PEDAC](https://medium.com/launch-school/solving-coding-problems-with-pedac-29141331f93f) or develop your own. Just make sure it helps you create solutions in which you’re confident.

For example, you may have noticed the use of constants, helper functions, and regex in my solution. Those are all tricks I’ve picked up that help me isolate complexity in an interview. The more my code reads like English, the less confused I get when writing it, and the faster I work. It may be a bit verbose, but I like it. Do what works for you.

If there’s already a procedure you use, practice and perfect it. Don’t wait until your onsite interview to start fine-tuning. Experiment in mock interviews. [Pramp](https://www.pramp.com/#/) and [Interviewing.io](https://interviewing.io/) are perfect tools for that.

Remember, if all else fails, trust the process.

If this article has resonated with you, please leave some claps ? !

As always, happy coding!

