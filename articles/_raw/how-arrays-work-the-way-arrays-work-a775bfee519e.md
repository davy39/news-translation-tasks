---
title: An overview of how arrays work
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T03:05:06.000Z'
originalURL: https://freecodecamp.org/news/how-arrays-work-the-way-arrays-work-a775bfee519e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IAFX-G9C6sOXI-s6Q0widw.png
tags:
- name: Computer Science
  slug: computer-science
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Edison Yap

  In computer science, there is the concept of a linear data structure, which means
  that the data are structured in a linear way in which order matters. There are Arrays
  and Linked Lists, but today I’ll be talking mostly about arrays, and...'
---

By Edison Yap

In computer science, there is the concept of a **linear data structure**, which means that the data are structured in a linear way in which **order matters**. There are **Arrays** and **Linked Lists**, but today I’ll be talking mostly about arrays, and a little about linked lists.

Most object-orientated languages come with **Arrays**, whereas most _f_unctional languages come with **Linked Lists** (see why in another one of my articles, mentioned at the bottom of this article).

There’s a good reason for this differentiation which we will dive into later. For now let’s just have a quick look at the differences between the two data structures. To do this, we’ll need to take a trip down memory lane.

### Rewind Time

Objects and functions and everything that we know about computers, are fundamentally stored in bits and bytes in the computer.

In languages like Java and C, you have to explicitly declare the size of an array beforehand.

> _Hold up, but Ruby does not do that?_

In Ruby, we use `Array` for our linear data structures. We can add seemingly infinite things into a Ruby array and it would not matter as far as we are concerned.

That’s great isn’t it?! That means arrays are **infinitely** large right? And that Ruby is the superior language? Lucky us!

But not so fast. _*pops your bubble*_

There are no **infinite size arrays;** what you see in Ruby is what we call a **Dynamic Array**, and it comes with a cost.

To understand what dynamic arrays are, let’s first take a look at how arrays are represented in memory. Since MRI Ruby (Matz’ Ruby Interpreter) compiles down to C code, we’ll look at how arrays are represented in C.

### C-ing is believing

We’ll dive into a little bit of C code to help us C a little better… :)

In lower level languages like C, you have to deal with pointers and memory allocation yourself. Even if you have not dealt with C before (d_isclaimer — neither have I_), you may have C-een one of the most (in)famous examples below:

Let’s break down this bit of code:

* `malloc` doesn't have any magic meaning behind it, it literally stands for `memory allocation`
* `malloc` returns a pointer
* `malloc` takes in an argument, which is the size the memory you want the program to allocate for you.
* `100 * sizeof(int)` tells the program that we want to store 100 integers, so allocate us 100 * the size of what each integer would occupy.
* `ptr`/pointer stores reference to the memory address.

### Timmy stores luggage!

If the above example did not really make sense, try this analogy. Think of memory allocation as a luggage concierge. It works like this:

* Timmy goes to the counter, tells the concierge that he has 2 pieces of luggage, about _this_ big, and that that he’d like to store them in the storeroom.
* The concierge takes a look at the store room and go “Yes, we’ve got some room at the designated `B4` area and will allocate that space to store your luggage".
* They hand Timmy a **pick-up card** with the designated area on it, `B4` in our case.
* Timmy is happy, goes around doing whatever, and when he wants to pick-up his luggage, he goes back to the counter and shows them his **pick-up card**. “_Have you C-een my luggage?_”

In our example, Timmy’s luggage is the **data**, the **pick-up card is the pointer** (it states where Timmy’s bag is stored). The place that the concierge is storing Timmy’s luggage is the **memory block**, and the counter is the **program**.

By showing the counter (**the program**) Timmy’s card (**pointer/memory address**), Timmy can retrieve his luggage (**data**). Bonus? Because they know **exactly** where Timmy’s bag is stored — `B4`, this means that they can retrieve all Timmy's luggage relatively quickly!

Also, ever wondered why you access elements in array with **index**, like so?

This is because the array holds the references to the memory block, and the index is telling it the **offset**.

An analogy for that is if I ask you to look for Timmy in a queue of 20 people, you would logically have to ask each of them if they were Timmy. But, if I told you Timmy is the 6th (**index**) from the first person (**your original pointer**), you know exactly where to look.

Retrieving elements in arrays is fast exactly because of this — the program doesn’t have to look through all 100 elements to find what you’re looking for. If you’ve got the index, it just has to add the offset to the original memory address, and the droid that you were looking for will be right there!

### What are dynamic arrays then?

So I’ve told you a little about how arrays are represented in memory, but now it’s time to talk about some cons.

Remember how you have to explicitly declare the amount of memory you need? This means that the array will find a spot that will fit exactly your size. There’s no guarantee that it will be able to fit more than what you have (because the memory block right behind it might be occupied).

Back to our luggage analogy: think of it as if Timmy was to store 2 pieces of luggage, and `B4`can store exactly 2 pieces of luggage, so they allocate that to Timmy. Now for some reason Timmy wants to store _another_ piece of luggage, but `B4` can't store 3 pieces, only 2, so what do they do?

They take all of his existing luggage, move it into a new spot that can fit more than 3 pieces, and then store all of them together.

That is an expensive operation but it’s exactly how memory works too!

In Ruby, you don’t have to declare a specific size _before hand_, but that’s because Ruby handles it for you automagically through dynamic arrays.

What a dynamic array does is that if the array is nearing its full capacity, it’ll automatically declare a new, bigger array and move all existing elements into it, and the old array is then garbage collected. How much bigger? The growth factor is _usually_ 2; double the size of the current array.

**In fact, don’t take my word for it**.

Ruby has an [ObjectSpace module](https://ruby-doc.org/core-2.2.0/ObjectSpace.html) that allows us to interact with current objects living in memory. We can use this module to take a peek at the memory usage of our dynamic array — sounds exactly like what we want!

I have written a small Ruby script that calculates the growth factor of the dynamic array. Feel free to take a look at it [here](https://gist.github.com/edisonywh/c61b3ab50359e68454d87b2c13d5d1a8), and if you do, you can see that Ruby arrays have a 1.5x growth factor (that is, they make an array that’s 50% bigger on every copy).

### I know what arrays are, what are linked lists?

Keep in mind that although arrays and linked lists are both considered linear data structures, they have one big difference between them.

Elements in an array are stored literally right next to each other in memory (so we can have index for fast lookups). But nodes in linked lists have no such restriction (which is why there’s no index lookup for linked lists) — each and every item can be stored anywhere on the memory block.

It’s almost as if Timmy’s trying to store 5 pieces of luggage, and the concierge does not have a space and decides to leave them all over the place. Sounds unorganized?

Also if they are stored in different places, how do you know which bags are Timmy’s? _Hint: Just keep track of the next node/bag!_ In our case, the concierge keeps them separately but with a tag on each of them that points to the next bag.

A node in a linked list consists of two parts — the data part and a pointer to the next node. This is how they’re able to maintain the `linear` part of it -- they still have the concept of order, they just don't have to be stored in order literally!

`node = [ data | pointer ]`

For example, given the following example stored in memory:

`[C | D] [A | B] [B | C] [D | nil]`

This bits look like it’s out of order — but if I had told you that the first element is `A`, you would be able to tell me the exact order of the list:

`list = [A -> B -> C ->` D -> nil]

There’s a lot of interesting things that you can do with linked lists which I’m not going to dive into here (also a lot on Big O that I didn’t talk about). But there are already a ton of good articles out there on data structures. If you made it here, I suggest you to read from Ali’s blogpost [here](https://dev.to/aspittel/thank-u-next-an-introduction-to-linked-lists-4pph).

[**thank u, next: an introduction to linked lists**](https://dev.to/aspittel/thank-u-next-an-introduction-to-linked-lists-4pph)  
[_In this post, we are going to be talking about the linked list data structure in the language of "thank u, next" by…_dev.to](https://dev.to/aspittel/thank-u-next-an-introduction-to-linked-lists-4pph)

You can also read more about List/Cons on [Wiki here](https://en.wikipedia.org/wiki/Cons).

### Closing Note

I initially wrote this article for a slightly different topic — [[ Elixir | Why Linked Lists?]](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d), but found it took way too long to explain how arrays work before I was able to explain explore why Elixir uses linked lists. So I have separated them into two articles.

In that article, I talk about why functional languages use linked lists as their linear data structure. Do check it out!

[**[ Elixir | Why Linked Lists? ]**](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d)  
[_I've always thought data structures are cool, but you know what's cooler? Seeing them in the wild! While going through…_dev.to](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d)

### Sources

1. [https://medium.com/@rebo_dood/ruby-has-a-memory-problem-part-1-7887bbacc579](https://medium.com/@rebo_dood/ruby-has-a-memory-problem-part-1-7887bbacc579) — This is where I found out about additional `ObjectSpace` methods by requiring it

_Originally posted on [dev.to](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg)_

