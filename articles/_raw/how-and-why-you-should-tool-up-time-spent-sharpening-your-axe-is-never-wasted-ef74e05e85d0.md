---
title: 'How and why you should tool-up: time spent sharpening your axe is never wasted'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-20T16:56:37.000Z'
originalURL: https://freecodecamp.org/news/how-and-why-you-should-tool-up-time-spent-sharpening-your-axe-is-never-wasted-ef74e05e85d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sT3OymCpylqi6csy.
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Harshdeep S Jawanda

  There is this old anecdote about two friends who went to the forest to chop up some
  firewood for their homes. The first friend kept at it without a break for four hours,
  whereas the other friend would rest for 5 minutes or so e...'
---

By Harshdeep S Jawanda

There is this old anecdote about two friends who went to the forest to chop up some firewood for their homes. The first friend kept at it without a break for four hours, whereas the other friend would rest for 5 minutes or so every hour. When they were done the first friend was surprised to see that the other’s woodpile was much larger than his.

Incredulous, he asked, “How did you chop more wood than me!? I worked continuously while you took so many breaks.”

His friend replied, “While resting, I would sharpen my axe, so that I could chop up wood more efficiently the rest of the time.”

That’s what I mean by “Tool-Up!”: equipping yourself with the right tools to make you more productive while ensuring higher quality work output.

What follows is aimed at developers, and uses Java to illustrate examples. But **the general advice applies to everybody**.

### Be smart

The example above is not to meant to send you running to your keyboard to start banging out utility classes/libraries that will supposedly help you out. Not at all! Be smart about what exactly it is that you need. Maximize the Return On your (time) Investment (ROI). An important part of being smart means that you…

#### Prefer pre-built solutions to rolling out your own

For developers, the right tool is often a library that provides you with the required functionality. Whether it is the `Optional<`;T> class of the Guava library (for use in pre-Java 8 code) o`r its ImmutableL`ist<T> implementation, these tools have been developed to cover many use cases. They also typically have many generations of evolution behind them, and have been thoroughly tested, both by developers and by users. As such they offer the benefits of good design and mature implementations.

Remember: don’t re-invent the wheel!

#### Use your tools consistently

If you use a tool or technique, try to use it consistently throughout your work as much as you’re able. This will help reduce the mental load of having to do a **context switch** between different paradigms and situations.

Often this means refactoring legacy code. In such situations, you should seriously consider scheduling time for it. If time is a limiting factor — as it often is — try to prioritize high-impact parts of your codebase.

### When it’s time to do it yourself

The stage will likely come (as it almost invariably does) that pre-built solutions are not good enough, or they fail to fill some of the very specific gaps you need filled. Don’t feel pressured to create humongous, perfectly-designed, everything-and-the-kitchen-sink libraries. **Start small**. Create **a solution that’s just enough** for your current needs. Perhaps instead of creating a library, think only about creating a utility class, and then take things from there.

#### A little can go a long way

You’ll be surprised by how much utility and convenience even 3–4 lines of ordinary code can deliver.

There were a number of places in my code where I had to get specific values from specific indices in `List`s. What’s more simple than:

```
Object listValue = myList.get(index)
```

Right? Not so fast! That simple line of code can potentially throw two different exceptions (can you figure out which ones and why?). Ok, so you wrap your code with some `try-catch` goodness and now you’re done, right? What value are you going to assign to `listValue` in case of an exception? Your code now begins to look something like:

```
Object listValue = null; // default value assignmenttry {    listValue = myList.get(index);} catch (Exception e) {    // Do nothing (if that is what you want to do)}
```

Simple, straightforward code — but it’s not exactly a pretty sight or very convenient. Not to mention that similar fragments will be littered all over your code. Sooner or later you will also forget to cater for all eventualities. And then: **boom!!**

Compare that to:

```
Object listValue = Lists.get(myList, index, null);
```

where the `Lists` utility class contains the following convenience method:

```
public static <T> T get(List<T> list, int position, T defaultValue) {    if (null != list && position >= 0 && position < list.size())        return list.get(position);    return defaultValue;}
```

It’s an extremely simple method, yet very useful (for a specific use case).

Of course, this may not be exactly what you need. You could also argue that instead of throwing an `ArrayIndexOutOfBounds` exception, this code hides incorrect indices and could lead to insidious errors, and that’s why you don’t find code like this in general-purpose libraries (where failing early is a virtue)…That’s all valid, but that is also why I wrote this particular utility method for **my use case.**

This illustrates my point: beyond the point you can/will/should write utility code for your specific use cases, just be aware of potential pitfalls, if any.

### Look for repeating patterns

As I mentioned before, there’s no need to rush into anything. A good and easy way to identify scenarios where a higher level of abstraction would be useful is to look for things that are:

* cumbersome
* have repeated usage
* are error-prone

Let this be your guide. Basically, **look for repeating patterns** in your code or your actions to get the most bang for your buck.

As you start to improve the most obvious scenarios, other — often higher-level — patterns will begin to emerge. Things that did not seem so inconvenient before will suddenly start looking unweildy/error-prone in comparison. That will automatically guide you towards the next tool/abstraction you should develop.

Rinse, repeat.

### Don’t Force It

Let your tool usage/adoption grow organically as you deal with your pain points and bottlenecks (Agile mindset?). Don’t set a hard-coded limit of X hours spent per week to satisfy some externally-imposed metric of what constitutes “good practice.”

**Forced tool usage can sometimes be counter-productive:** you’ll get much better results when you and your people **feel the need for improvement**. The motivation level and the perception of reward (when the improvement happens) is just so much higher.

### Last but definitely not least…

Practice continuous learning and self-improvement.

These are the two most important tools you can equip yourself with. Once you inculcate these habits, they will have the longest-lasting impact on your life and career.

### Finally…

If you found this article helpful, please don’t forget to clap ;-)!

Constructive discussions and corrections are most welcome.

