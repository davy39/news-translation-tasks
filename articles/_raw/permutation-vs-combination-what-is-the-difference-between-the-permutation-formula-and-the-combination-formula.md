---
title: 'Permutation vs Combination: What is the Difference Between the Permutation
  Formula and the Combination Formula?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T21:46:28.000Z'
originalURL: https://freecodecamp.org/news/permutation-vs-combination-what-is-the-difference-between-the-permutation-formula-and-the-combination-formula
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e91740569d1a4ca3dca.jpg
tags:
- name: algorithms
  slug: algorithms
- name: beginners guide
  slug: beginners-guide
- name: combinatorics
  slug: combinatorics
- name: education
  slug: education
- name: Math
  slug: math
seo_title: null
seo_desc: "By Neil Kakkar\nHere's the short version.\nLet's take ringing bells in\
  \ a church as an example. \nA permutation is an ordering of the bells. You're figuring\
  \ out the best order to ring them in.\nA combination is the choice of bells. You're\
  \ choosing the bel..."
---

By Neil Kakkar

Here's the short version.

Let's take ringing bells in a church as an example. 

A permutation is an ordering of the bells. You're figuring out the best order to ring them in.

A combination is the choice of bells. You're choosing the bells to ring. If you have too many bells, you'd first choose them, and then think about ordering them.

This gives rise to the familiar identity: `(n P r) = (n C r) * r!`

The way to order `r` items out of `n` is to first choose `r` items out of `n`, and then order the `r` items (`r!` )

And, this means `(n P r) = n! / (n-r)!` and `(n C r) = n! / ( (n-r)! * r! )` 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/ncr.jpg)

**But do you want to know how to remember this forever?**

I'm a big fan of [first principles thinking](https://neilkakkar.com/A-framework-for-First-Principles-Thinking.html). To understand a problem, get to the core of it, and reason up from there.

Not doing this is usually the source of confusion: if I don't understand how things work, I don't know where to hang the concepts. My mental framework isn't complete, so I decide to just remember it.

As you can imagine, this isn't ideal. So, from time to time, I indulge myself in an exercise of deriving things from the source, and building intuition for how things work.

This time around, we're building intuition for permutations and combinations.

For example, do you know why the formula for a combination is (n C r)? Where did this come from? And why are factorials used here?

Let's begin at the source. Factorials, Permutations, and Combinations were born out of mathematicians playing together, much like how Steve Jobs and Steve Wozniak founded Apple playing together in their garage.

Just like how Apple became a full fledged profitable company, the simple factorial, `!`, became the atom of an entire field of mathematics: [combinatorics](https://en.wikipedia.org/wiki/Combinatorics).

Forget everything, let's start thinking from the bottom up.

The first known interesting use case came from Churches in the 17th century.

Have you wondered how the bells are rung in churches? There's a machine that "rings" them in order. We switched to machines because the bells are too big. Also, there are tons of bells.

How did people figure out the best sequence to ring them in? What if they wanted to switch things up? How could they find the best sound? Each bell tower had up to 16 bells!

You couldn't change how quickly you could ring a bell - the machines only rang one bell every second. The only thing you could do was [change](https://en.wikipedia.org/wiki/Change_ringing) the order of the bells. So, this challenge was about figuring out the best order. 

Could we, on the way, also find out all the possible orders? We want to know all possible orders to figure out if it's worth trying them all.

A bell ringer, [Fabian Stedman](https://en.wikipedia.org/wiki/Fabian_Stedman) took up this challenge.

He started with 2 bells. What are the different orderings he could ring these bells in?[1]

1 and 2.
or
2 and 1.

This made sense. There was no other way.

How about with 3 bells?

1, 2, and 3.  
1, 3, and 2.

Then starting with the second bell,

2, 1, and 3.  
2, 3, and 1.

Then starting with the third bell,

3, 1, and 2.  
3, 2, and 1.

Total, 6.

He then realised this was very similar to two bells!

If he fixed the first bell, then the number of ways to order the remaining two bells was *always* two. 

How many ways could he fix the first bell? Any of the 3 bells could be the one!

Okay, he went on. He then reached 5 bells.

This is when he realized doing things by hand is unwieldy. You only have so much time in the day, you've got to ring bells, you can't be stuck drawing out all the possible bells. Was there a way to figure this out quickly?

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5bells-2.jpg)

He went back to his insight.

If he had 5 bells, and he fixed the first bell, all he had to do was figure out how to order 4 bells.

For 4 bells? Well, if he had 4 bells, and he fixed the first bell, all he had to do was figure out how to order 3 bells.

And he knew how to do this!

So, ordering of 5 bells = 5 * ordering of 4 bells.

Ordering of 4 bells = 4 * ordering of 3 bells

Ordering of 3 bells = 3 * ordering of 2 bells.

.. You see the pattern, don't you?

> Fun Fact: This is the key for a programming technique called [recursion](https://en.wikipedia.org/wiki/Recursion). 

He did too. Although, it took him much longer, since no one near him had already discovered this.[2]

Thus, he figured out that the ordering of 5 bells = `5 * 4 * 3 * 2 * 1`.

This ordering formula, in 1808, came to be known as the factorial.

We think of the factorial notation as the base, but the idea existed long before it had a name. It was only when the French mathematician Christian Kramp noticed it being used in a few places that he named it the factorial.

This ordering of bells is called a permutation.

> A Permutation is an ordering of items.



When learning something, I think it helps to look at things from every different angle, to solidify understanding.

What if we tried to derive the formula above directly, without trying to reduce the problem to a smaller number of bells?  
  
We have 5 spaces, right?

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells.jpg)

How many ways can we choose the first bell? `5`, because that's the number of bells we have.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_1filled.jpg)

  
The second bell? Well, we used up one bell when we placed it in the first position, so we have 4 bells left.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_2filled.jpg)

  
The third bell? Well, we've chosen the first two, so there are only 3 bells left to choose from.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_3filled.jpg)

  
The fourth bell? Only 2 bells left, so 2 options.   
The fifth bell? Only 1 left, so 1 option.  


![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_5filled.jpg)

And there we have it, the total number of orderings is `5 * 4 * 3 * 2 * 1`

Thus, we have our first general formula. 

> The number of ways to order `N` items is `N!`


# The Permutation

Now, we're faced with a different problem. The king ordered new bells to be made for every church. Some are nice, some are okay, some will make you go deaf. But every one is unique. Each makes its own sound. A deafening bell surrounded by nice bells can sound majestic.

But, our bell tower still holds 5 bells, so we need to figure out the best ordering out of 8 bells that the skilled bell makers made.

Using the above logic, we can proceed.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesFor8Bells-1.jpg)

For the first bell, we can choose any of the 8 bells.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_1filled_8bells.jpg)

  
For the second bell, we can choose any of the remaining 7 bells... and so on.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_5filled_8bells.jpg)

  
In the end, we get `8 * 7 * 6 * 5 * 4` possible orderings of 8 bells in 5 spaces.

If you're familiar with the formula version of (n P r), which is `n! / (n-r)!`, don't worry, we'll derive that soon enough, too!

One bad way to derive it is to multiply both the numerator and denominator by 3! in our example above -

we get `8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 / 3 * 2 * 1` = ` 8! / 3!`.

But this doesn't help us understand why this formula works. Before we get there, let's have a look at choosing things, or the Combination.

# The Combination

Now that we know how to order things, we can figure out how to choose things!

Let's consider the same problem. There's a belltower with 5 bells, and you have 8 bells. However, right now, you don't want to figure out the order of bells (remember that's what a permutation is).

Instead, you want to choose the 5 best bells, and let someone else with better taste in music figure out the ordering. In effect, we're breaking the problem down into to parts: First, we figure out which bells to choose. Next, we figure out how to order the chosen bells.

How do you choose the bells? This is the "combination" from permutations and combination.

The combination is a selection. You're being selective. You're choosing 5 bells out of 8 your craftsmen have made.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/8bells_inline.jpg)

Since we know how to order bells, we're going to use this information to figure out how to choose bells. Sounds impossible? Wait till you see the beautiful math involved.

Let's imagine all the bells are in a line.

Before finding all the ways to choose the bells, let's focus on one way to choose bells.

One way is to choose any 5 at random. This doesn't help us solve the problem much, so let's try another way.

We put the bells in a line, and choose the first 5. This is one way to choose the bells.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/8bells_inline_choose5.jpg)

Notice that, even if we switch positions of the first 5 bells, the choice doesn't change. They're still the same one way to choose 5 unique bells.

This is true for the last three bells as well.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/8bells_inline_choose5_permute.jpg)

Now, the beautiful math trick - for this one way to choose the 5 bells, what are all the ordering of 8 bells where we choose exactly these 5 bells? From the image above, it's all the orderings of the 5 bells (`5!`) and all the orderings of the remaining three bells (`3!`).

Thus, for every single way to choose 5 bells, we have (`5! * 3!`) orderings of 8 bells.

What are the total possible orderings of 8 bells? `8!`.

Remember, for each choice of first 5 bells, we have (`5! * 3!`) orderings of 8 bells which give the same choice.

Then, if we multiply the number of ways to choose the first 5 bells with all the possible orderings of one choice, we should get the total number of orderings. 

```
Ways to choose 5 bells * orderings of one choice = Total orderings
```

So, 

```
Ways to choose 5 bells = the total possible orderings / total orderings of one choice.
```

In math, that becomes:

```
(8 C 5) = 8! / ( 5! * 3!)
```
Lo and behold, we've found an intuitive explanation for how to choose 5 things out of 8.


Now, we can generalize this. If we have N things, and we want to choose R of them, it means we draw a line at R.

Which means the remaining items will be `N-R`. So, for one choice of `R` items, we have `R! * (N-R)!` orderings which give the same `R` items.


![Image](https://www.freecodecamp.org/news/content/images/2019/12/nSpacesForBells.jpg)

For all ways to choose `R` items, we have `N! / (R! * (N-R)!)` possibilities.


> The number of ways to choose `r` items out of `n` is `(n C r) = n! / (r! * (n-r)!)`


In colloquial terms, (n C r) is also pronounced `n choose r`, which helps solidify the idea that combinations are for choosing items.

# The Permutation - revisited

With the combination done and dusted, let's come back to Part 2 of our job. Our dear friend chose the best 5 bells by figuring out all possible combinations of 5 bells.

It's our job now to find the perfect melody by figuring out the number of orderings.

But, this is the easy bit. We already know how to order 5 items. It's `5!`, and we're done.

So, to permutate (order) 5 items out of 8, we first choose 5 items, then order the 5 items.

In other words, 

```
(8 P 5) = (8 C 5) * 5!
```

And if we expand the formula, `(8 P 5) = (8! / ( 5! * 3!)) * 5!`

`(8 P 5) = 8! / 3!`.

And, we've come full circle to our original formula, derived properly.

> The number of ways to order `r` items out of `n` is `(n P r) = n! / (n-r)!`

# Difference between permutation and combination

I hope this makes the difference between permutations and combinations crystal clear.

Permutations are orderings, while combinations are choices.

To order N elements, we found two intuitive ways to figure out the answer. Both lead to the answer, `N!`.

In order to permutate 5 out of 8 elements, you first need to choose the 5 elements, then order them. You choose using `(8 C 5)`, then order the 5 using `5!`.

And the intuition for choosing `R` out of `N` is figuring out all the orderings (`N!`) and dividing by orderings where the first `R` and last `N-R` remain the same (`R!` and `(N-R)!`).

And, that's all there is to permutations and combinations.

Every advanced permutation and combination uses this as a base. Combination with replacement? Same idea. Permutation with identical items? Same idea, only the number of orderings change, since some items are identical.

If you're interested, we can go into the complex cases in another example. Let me know [on Twitter](https://twitter.com/neilkakkar).

> Check out more posts on [my blog](https://neilkakkar.com/), and join the [weekly mailing list](https://neilkakkar.com/subscribe/).

## End notes

1. This is how I imagine he figured things out. Don't take it as a lesson in history.
2. The Indians had, in the 12th century, 400 years before him.

