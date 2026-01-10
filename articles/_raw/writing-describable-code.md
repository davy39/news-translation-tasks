---
title: How to write easily describable code
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-10-02T20:34:23.000Z'
originalURL: https://freecodecamp.org/news/writing-describable-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/writing-describable-code.jpg
tags:
- name: Code Quality
  slug: code-quality
- name: software design
  slug: software-design
- name: software design patterns
  slug: software-design-patterns
seo_title: null
seo_desc: When code is not describable using words, most people have to do some mental
  mapping to turn it in to words. This wastes mental energy, and you run the risk
  of getting the mapping wrong. Different people will map to different words, which
  leads to co...
---

When code is not describable using words, most people have to do some mental mapping to turn it in to words. This wastes mental energy, and you run the risk of getting the mapping wrong. Different people will map to different words, which leads to confusion when discussing the code. 

This is usually a fertile breeding ground for bugs born out of miscommunication / misunderstanding, and fixing these bugs often introduces new ones, for the same reasons. In the end it becomes code that no one really understands or wants to touch.

## Example of undescribable code

It is easy to think that code is already a written language. If it looks simple, it should be easy to read, speak and listen to. However, this is not always the case.

Below is a common solution to deciding whether a year is a leap year.

```python
(divisibleBy(4) and not divisibleBy(100)) or divisibleBy(400)

```

This is not overly complicated code. It calls a functions 3 times, has 3 operators (and, or, not), and has two levels of nesting.

However, if you take a second to try and describe the algorithm in words I think you will find it to be a struggle.

Maybe “A year is leap year if it is divisible by 4 and not divisible by 100, or divisible by 400”?

The trouble with this is that the code has brackets, but the words do not. So they cannot adequately describe the condition, and whether “or divisible by 400” applies to “divisible by 4” or “not divisible by 400”. You could try some hand waving and gesturing to get around this, or vary the length of pause between the statements, but hopefully it’s obvious that there is a lot of potential for error.

## Refactoring to describable code

Instead we can start by describing the condition with words, and then make the words as clear and concise as possible. We might start with this:

“400 years is a special case. If a year is divisible by 400, then it is a leap  year. 100 years is also a special case. If a year is divisible by 100 then it isn’t a leap year, unless it is also divisble by 400, the 400 year special case takes priority. If there are no special cases, then the year is a leap year if it is divisible by 4.”

This is clear, but isn’t concise, so we would probably want to shrink it a bit:

“If a year is divisible by 400, then it is a leap year. Otherwise if it is divisible by 100 then it is a normal year, otherwise it is a leap year if it is divisible by 4.”

If we turn these words in to code, we probably get something like the following:

```python
	if divisbleBy(400):
		return LeapYear
	elif divisbleBy(100)
		return NormalYear
	elif divisbleBy(4):
		return LeapYear
	else:
		return NormalYear

```

## Conclusions

Hard to understand code is a daily occurrence for virtually all programmers. We can help ourselves and our co-workers by writing code that is easy to describe in words.

And the great thing is that doing so is actually easier than writing code any other way, as there is no mental mapping / wasted mental effort. The only “trick” is to describe the algorithm in words, and then write code to match the words.

In many organisations, the algorithm will already be described in words, as part of acceptance tests or user stories, which will improve productivity even further.

