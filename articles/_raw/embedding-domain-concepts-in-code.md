---
title: How (and why) to embed domain concepts in code
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-11-12T07:48:19.000Z'
originalURL: https://freecodecamp.org/news/embedding-domain-concepts-in-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/2015-Gran-Paradiso-007.JPG
tags:
- name: Quality Software
  slug: quality-software
- name: Code Quality
  slug: code-quality
- name: '#Domain-Driven-Design'
  slug: domain-driven-design
- name: software design
  slug: software-design
- name: software development
  slug: software-development
seo_title: null
seo_desc: Code should clearly reflect the problem it’s solving, and thus openly expose
  that problem’s domain. Embedding domain concepts in code requires thought and skill,
  and doesn't drop out automatically from TDD. However, it is a necessary step on
  the road...
---

Code should clearly reflect the problem it’s solving, and thus openly expose that problem’s domain. Embedding domain concepts in code requires thought and skill, and doesn't drop out automatically from TDD. However, it is a necessary step on the road to writing easily understandable code.

I was at a software craftsmanship meetup recently, where we formed pairs to solve a simplified Berlin Clock Kata. A Berlin Clock displays the time using rows of flashing lights, which you can see below (although in the kata we just output a text representation, and the lights in a row are all the same colour).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/berlin-clock-2.gif)

## Initial Test Driven solution

Most pairs used inside out TDD, and there were a lot of solutions that looked something like this (complete [code available on GitHub](https://github.com/ceddlyburge/berlin-clock-initial-tdd-solution/blob/master/BerlinClock.py)).

```python
def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

	return [
		seconds_row_lights(seconds % 2)
		, five_hours_row_lights(hours)
		, single_hours_row_lights(hours % 5)
		, five_minutes_row_lights(minutes)
		, single_minutes_row_lights(minutes % 5)
	]

def five_hours_row_lights(hours):
    lights_on = hours // 5
    lights_in_row = 4
    return lights_for_row("R", lights_on, lights_in_row)
	
# ...

```

This type of solution drops out naturally from applying inside out TDD to the problem. You write some tests for the seconds row, then some tests for the five hours row, and so on, and then you put it all together and do some refactoring. This solution does expose some of the domain concepts at a glance:

* There are 5 rows
* There is one second row, 2 hour rows and 2 minute rows

Some more concepts are available after a bit of digging, but aren't immediately obvious. The rows are made up of lights that can be on (or presumably off), and that the number of lights on is an indication of the time.

However there are some big parts of the problem that are not exposed. And since I haven't yet explained it, you probably don't know exactly how the Berlin Clock works yet.

## Elevate the concepts

To improve this we can bring some of the details that are buried in the helper functions (such as `get_five_hours`) closer to the top of the file. This brings you to something like the following (complete [code available on GitHub](https://github.com/ceddlyburge/berlin-clock-elevated-concepts/blob/master/BerlinClock.py)), although the downside is that it breaks nearly all of the tests. Solutions like this are rarer on GitHub, but do exist.

```python
def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

	single_seconds = seconds_row_lights(seconds % 2)
    five_hours = row_lights(
		light_colour="R",
		lights_on=hours // 5,
		lights_in_row=4)
    single_hours = row_lights(
		light_colour="R",
		lights_on=hours % 5,
		lights_in_row=4)
    five_minutes = row_lights(
		light_colour="Y",
		lights_on=minutes // 5,
		lights_in_row=11)
    single_minutes = row_lights(
		light_colour="Y",
		lights_on=minutes % 5,
		lights_in_row=4)

	return [
		single_seconds,
		five_hours,
		single_hours,
		five_minutes,
		single_minutes
	]

# ...

```

This improves the concepts that are now exposed at a glance:

* There are 5 rows
* The seconds row is a special case
* There are 2 hour rows and 2 minute rows
* The rows use different colour lights
* The rows have a different number of lights

This is pretty good, and is already better that most of the solutions out there. However, it's still a bit mysterious how the rows are related to each other (there are 2 rows to display the hours and the minutes, so presumably these are linked). It's also not obvious what amount of time each light represents.

## Name implicit concepts

At the moment some of the concepts (such as the amount of time each light represents) are implicit in the code. Making these explicit, and naming them, forces us to understand them and to embed that understanding in the code.

In order to make the amount of time each light represents explicit, it seems like it would be sensible to pass a `time_per_light` value to `row_lights`. This means we have to push the calculation of `lights_on` down into `row_lights`.

This in turn makes it obvious that there are two kinds of rows: one related to the quotient (`\\`) of the time value, and one related to the remainder / modulus (`%`). If we look at the quotient case, we see that the 2nd parameter to the operation is the `time_per_light`, which is 5 in both cases (5 hours in one case and 5 minutes in the other).

This allows us to write these rows like this:

```python
five_hour_row = row_lights(
	time_per_light=5,
	value=hours, 
	light_colour="R",
	lights_in_row=4)

```

If we now turn our attention to the remainder case, we realise that `time_per_light` is always singular (one hour or one minute), as it is filling in the gaps in the quotient case. 

For example, the five hours row can represent 0, 5, 10, 15, or 20 hours, but nothing in between. In order to represent any hour, there must be another row to represent +1, +2, +3 and +4. This means that this row must have exactly 4 lights, and that each light must represent 1 hour.

This implies that the remainder case is dependent on the quotient one, which most people would describe as a parent / child relationship.

With this knowledge in hand, we can now create a function for the child remainder rows, and the solution now looks like this (complete [code on GitHub](https://github.com/ceddlyburge/berlin-clock)):

```python
def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

	return [
		seconds_row_lights(
			seconds % 2),
		parent_row_lights(
			time_per_light=5,
			value=hours, 
			light_colour="R",
			lights_in_row=4),
		child_remainder_row_lights(
			parent_time_per_light=5,
			value=hours,
			light_colour="R"),
		parent_row_lights(
			time_per_light=5,
			value=minutes, 
			light_colour="Y",
			lights_in_row=11),
		child_remainder_row_lights(
			parent_time_per_light=5,
			light_colour="Y",
			value=minutes)
	]

# ...

```

A quick glance at this code now reveals nearly all the domain concepts

* The first row represents the seconds and is a special case
* On the second row each "R" light represents 5 hours
* The third row shows the remainder from the second
* On the fourth row each "Y" light represents 5 hours
* The fifth row shows the remainder from the fourth

This took something thinking about, which will have cost us some time / money. But we increased our understanding of the problem while we did it, and most importantly we embedded that knowledge in to the code. This means that the next person to read the code will not have to do this, which will save some time / money. Since we spend about 10 times longer reading code than we do writing it, this is probably a worthwhile endeavour.

Embedding this understanding has also made it harder for future programmers to make mistakes. For example, the concept of parent / child rows didn't exist in earlier examples, and it would be easy to mismatch them. Now the concept is plain to see, and the values are mostly worked out for you. It is also easier to refactor to support new clock variants, for example where lights in the first hours row represent 6 hours.

## How far should you take it?

There are things we can do to take this further. For example the `parent_time_per_light` of a child row must match the `time_per_light` of its parent, and there is nothing enforcing this. There is also a relationship between `time_per_light` and `lights_in_row` for the parent rows, and again it is not enforced. 

However, at the moment we are only required to support one clock variant, so these probably aren't worth doing. When a change is required for the code, we should refactor so that the change is easy (which might be hard) and then make the easy change.

## Conclusions

Embedding domain concepts in code requires thought and skill, and TDD won't necessarily do it for you. It takes longer than a naive solution, but makes the code easier to understand, and will very likely save time in the medium term. Time is money, and finding the right balance of spending time now versus saving time later is also an important skill for a professional programmer to have. 

