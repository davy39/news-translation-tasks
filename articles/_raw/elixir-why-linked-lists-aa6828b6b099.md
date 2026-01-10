---
title: Why Elixir uses linked lists
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T03:12:13.000Z'
originalURL: https://freecodecamp.org/news/elixir-why-linked-lists-aa6828b6b099
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L8v2RUaCgJ2O1YiWqQTGwQ.png
tags:
- name: Computer Science
  slug: computer-science
- name: Elixir
  slug: elixir
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Edison Yap

  I’ve always thought data structures are cool, but you know what’s cooler? Seeing
  them in the wild!

  While going through Elixir’s docs, I saw that Elixir uses linked lists under the
  hood for their linear data structures. I thought this wa...'
---

By Edison Yap

I’ve always thought data structures are cool, but you know what’s cooler? Seeing them in the wild!

While going through Elixir’s docs, I saw that Elixir uses linked lists under the hood for their linear data structures. I thought this was cool, but something struck me; I understood arrays and linked lists, but I had no idea how they related to programming languages. It’s bothered me ever since, and I _needed_ to find out _why_ linked lists were used…hence this article!

So back to the article: from what I’ve found so far, there are three reasons as to why Elixir does this (and I could be totally wrong, feel free to correct me!). Let’s go through one by one:

### Immutable Data

In Elixir (most functional languages actually), data are immutable. This is an important first step to understanding why linked lists are used, so let’s explore this.

> _Immutable means that once data is declared, it_ cannot _be mutated/changed anymore._

Assuming you know how arrays work under the hood (check out [my other article](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg) if you want a refresher), let’s take a look at what happens if we try to implement immutability with an array!

An array is defined as a continuous block of memory. The problem with this is that an array of 5 elements is still just ONE array, and when we are adding/deleting an element, we are MUTATING it. How can we use immutability with arrays then? It’s not impossible, but let’s look at why that’s not practical.

If we want to enforce true immutability in arrays, this means that we need to make a full copy of the old array every time we want to add/delete in the array.

Which means, if you have an array of size 5, if you want to add a new item to the array, your memory usage is instantly doubled (because you need to keep the old array as is, and you also need to make a new array of the same elements). And that’s just space complexity — there’s also time complexity that we need to think about!

A linked list doesn’t have the same constraints, as the nodes are all stored separately in memory, which means we don’t really need to worry about space/time complexity while adding/deleting nodes in the list.

This gives us our first reason as to why it uses a list, however that’s not the whole story. Here’s where recursive structural/tail sharing jumps in and everything starts making sense.

### Recursive structure

Did you notice that linked lists are recursive by definition?

For example, `A -> B ->` C -> D is a linked list, b`ut so is B` -&`gt; C` -> D, C -> D and so on, and each link_ed_ list is just a sub structure of another linked list!

Well that wasn’t very exciting on its own, but this is vital to the next piece of puzzle!

> Fun Fact: The recursive nature coupled with the fact that data has to be immutable (so you can’t have a loop counter) is why functional languages are usually associated with recursion — they kinda have to!

### Structural/Tail Sharing

So, we know linked lists are recursive in nature. Combined with the immutable nature of the language, we know that the data can never change.

This is interesting, because now we can confidently say that `A -> B ->` C -> D is a different l`ist from B` -> C -> D (even though one recursively contains the other one). Because we have that guarantee (along with the fact that a list CAN'T change), we don't have to define the same d**ata twice, and we can reuse existin**g linked lists! **This is called Str**uctural sharing.

Awesome isn’t it? Let’s look at an example.

e.g:

Now we have THREE different lists! `list`, `list_one` and `list_two`, but all of them share the same reference (the tail) and the only difference between them is the head pointer.

This means that there will be a total of 6 elements in memory. Adding to list has low memory cost, while retaining the immutability that we desire.

Reusable baby!

![Image](https://cdn-media-1.freecodecamp.org/images/1*b31hiO4ynbDLRrXWEFF4aQ.png)

If you want to read a little more, you can look into [Trie trees](https://en.wikipedia.org/wiki/Trie) which have the exact same concepts of sharing datas/prefixes!

### Garbage Collection & Caching?

These two I’m not quite sure about, but I’ve heard that linked lists are good for GCs and that tail sharing makes a good candidate for locality of reference/caching (I don’t get how, because they aren’t stored in the same places). Would appreciate if someone wants to chime in!

### Closing Note

Side note: in actuality, it’s not as much about Elixir since it compiles down to Erlang. But it’s also not much about Erlang, because all functional programming does pretty much same thing…but this is what prompted my curiosity, hence the ties to Elixir.

While writing this article, I found that I had to write in depth on how arrays work before I was able to dive into the Elixir part, so I’ve published that as [another article over here](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg) instead. Do read that to gain a better understanding on what the tradeoff is!

[**How arrays work the way arrays work**](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg)  
[_In computer science, there is the concept of linear data structure, which means that the datas are structured in a…_dev.to](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg)

I also did not really talk about Big O notation, because I felt it might add unnecessary reading _time_ and _complexity_ to the article, but it’s pretty vital and fundamental to computer science, so I suggest you brush up a little on it.

If you’re a podcast kind-of person, there’s the [BaseCS](https://www.codenewbie.org/basecs) by CodeNewbie, co-hosted by Vaidehi Joshi and Saron.

If you want to read though, Vaidehi Joshi’s blogpost version (which is what inspired the podcast, I believe) is great too on [BaseCS Medium](https://medium.com/basecs).

As for video, [MyCodeSchool](https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P) is beyond amazing and is practically where I learned everything that I know now, highly recommended!

Other than that, hope you all enjoyed the article as much as I enjoyed writing it!

### Sources

[https://elixir-lang.org/getting-started/basic-types.html#linked-lists](https://elixir-lang.org/getting-started/basic-types.html#linked-lists) — The piece that prompted this article

_Originally posted on [dev.to](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d)_

