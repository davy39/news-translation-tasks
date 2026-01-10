---
title: An introduction to Ruby’s *Splat and double **Splat operators
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-07T00:15:35.000Z'
originalURL: https://freecodecamp.org/news/rubys-splat-and-double-splat-operators-ceb753329a78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Cc4O2WsCRkCaFiy0u92QA.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Declan Meehan

  Have you ever wanted to define a method without knowing how many arguments it will
  take? Do you spend long restless nights wishing there was an easy way to separate
  a list into a hash? Well look no further than Ruby’s splat operators...'
---

By Declan Meehan

Have you ever wanted to define a method without knowing how many arguments it will take? Do you spend long restless nights wishing there was an easy way to separate a list into a hash? Well look no further than Ruby’s splat operators! There are so many great things you can do with these, but I’m just going to go over the basics plus a few neat tricks I’ve discovered.

### Single *Splat

The splat operator has almost endless uses. But the main idea is that whenever you don’t want to specify the number of arguments you have, you would use a splat operator. The simplest example would be something like this:

Another useful thing is that the splat operator can make an array into several arguments:

```
arr = ["first", "second", "third"]def threeargs(*arr)#makes three arguments
```

You can also use the splat operator to grab any segment of an array:

```
first, *rest, last  = ["a", "b", "c", "d"]p first # "a"p rest # ["b", "c"]p last # "d"
```

You’ll notice that the rest variable is still an array, which is super handy. And so, following the last example, you can still do things like this:

```
first, *rest, last  = ["a", "b", "c", "d"]p rest[0] # "b"
```

Those are the basics of the single splat operator, but I urge you to mess around with it more. It can do things like combine arrays, turn hashes and strings into arrays, or pull items out of an array!

### Double **Splat

The double splat operator came out back in Ruby 2.0. It’s pretty similar to the original splat with one difference: it can be used for hashes! Here’s an example for the most basic use of a double splat.

```
def doublesplat(**nums)  p **numsenddoublesplat one: 1, two: 2 # {:one=>1, :two=>2}
```

### Putting it all Together

I hope you can see that the possibilities are pretty endless with using these two together. The main thing to keep in mind is that you use splats as a parameter in a method when you are unsure of how many arguments that method will be using.

Lastly, I made a little function that shows how you can filter out any argument that is not a key value pair using both a single splat and double splat.

```
def dubSplat(a, *b, **c)  p cenddubSplat(1,2,3, 4, a: 40, b: 50)#{:a=>40, :b=>50}
```

Thanks for reading, and now try playing around with it yourself!

