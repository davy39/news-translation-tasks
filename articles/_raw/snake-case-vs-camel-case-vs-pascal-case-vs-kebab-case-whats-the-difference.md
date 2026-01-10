---
title: Snake Case VS Camel Case VS Pascal Case VS Kebab Case – What's the Difference
  Between Casings?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-11-29T16:33:11.000Z'
originalURL: https://freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-olia-danilevich-4974912.jpg
tags:
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'As a software engineer, you may be familiar with the following quote by
  Leon Bambrick:


  “There are 2 hard problems in computer science: cache invalidation, naming things,
  and off-by-1 errors.”


  Indeed, naming things when programming can be challengin...'
---

As a software engineer, you may be familiar with the following quote by [Leon Bambrick](https://twitter.com/secretGeek/status/7269997868?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E7269997868%7Ctwgr%5Eb9b41e252e8f8e5c2863c7a50642e9ec2ff0fe18%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fmartinfowler.com%2Fbliki%2FTwoHardThings.html):

> “There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors.”

Indeed, naming things when programming can be challenging when you have different naming conventions available.

In this article, I will explain the differences between the most widely used case types in programming.

Here is what we will cover:

1. [Why use casings in programming?](#intro)
    1. [What is snake case?](#snake-case)
    2. [What is kebab case?](#kebab-case)
    3. [What is camel case?](#camel-case)
    4. [What is pascal case?](#pascal-case)

## Why Use Casings in Programming? <a name="intro"></a>

In programming, spaces are reserved characters.

Let's take the following example.

Say you want to create a variable in your program, and the name of the variable is more than just one word.

For your program to not crash, you cannot leave spaces between the different words when creating the variable.

For example, you cannot do the following:

```
number of donuts = 34
```

If you tried the above, you would get an error.

Most (if not all) programming languages interpret each word as a completely separate thing and a single unit.

`number`, `of`, and `donuts` are treated separately from each other because of the space character in between them. 

For your program to work correctly, you need to remove all the spaces and combine the words into a single string in a specific way. And there are a few ways available to combine them.

Specifically, there are certain naming conventions available across all programming languages, also known as:

- snake case
- kebab case
- camel case
- pascal case

When it comes to using case styles, there is no definite answer as to which one is the best. It depends.

When choosing a case style, keep in mind the best practices of the programming language you are using in your project.

And no matter which case you choose, remain consistent in your project.

It is best practice to choose one case style and stick with it. That way, your code will remain readable, easy to understand, and maintainable for yourself and other developers you may be working with on a team.

Let's see each case in more detail in the following sections.
 
### What is Snake Case? <a name="snake-case"></a>

Snake case separates each word with an underscore character (`_`).

When using snake case, all letters need to be lowercase.

Here are some examples of how you would use the snake case:

```
number_of_donuts = 34

fave_phrase = "Hello World"
```

Snake case is used for creating variable and method names.

Snake case is also a good choice for naming files, as it keeps names readable.

You will typically encounter it the most when programming in Python and not so much when programming in Java, JavaScript, or TypeScript. 

You will also come across it when working with databases, as it is used for creating table and column names.

There is also an all-caps version of the snake case where all letters are in the upper case - also known as the screaming snake case.

Here are some examples of how you would use upper case snake case:

```
NUMBER_OF_DONUTS = 34

FAVE_PHRASE = "Hello World"
```

The capitalized version is used for declaring constants in most programming languages. A constant is a data item whose value doesn't change throughout the life of a program.

### What is Kebab Case? <a name="kebab-case"></a>

The kebab case is very similar to snake case. 

The difference between snake case and kebab case is that kebab case separates each word with a dash character, `-`, instead of an underscore.

So, all words are lowercase, and each word gets separated by a dash.

The kebab case is another one of the most human-readable ways of combining multiple words into a single word.

Here are some examples of how you would use kebab case:

```
number-of-donuts = 34

fave-phrase = "Hello World"
```

You will encounter kebab cases mostly in URLs.

A URL (short for Uniform Resource Locator) is a unique address for accessing a resource on the Web.

### What is Camel Case? <a name="camel-case"></a>

When using camel case, you start by making the first word lowercase. Then, you capitalize the first letter of each word that follows. 

So, a capital letter appears at the start of the second word and at each new subsequent word that follows it.

Here are some examples of how you would use camel case:

```
numberOfDonuts = 34

favePhrase = "Hello World"
```

In the example `numberOfDonuts`, the first word `number` is lowercase. Then,  the first letter of the second word, `Of`, is capitalized, as is the first letter of the third word, `Donuts`.

You will encounter camel case in Java, JavaScript, and TypeScript for creating variable, function, and method names.


### What is Pascal Case? <a name="pascal-case"></a>

Pascal case is similar to camel case. 

The only difference between the two is that pascal case requires the first letter of the first word to also be capitalized.

So, when using pascal case, every word starts with an uppercase letter (in contrast to camel case, where the first word is in lowercase).

Here are some examples of how you would use pascal case:

```
NumberOfDonuts = 34

FavePhrase = "Hello World"
```

You will see the pascal case used for naming classes in most programming languages.

## Conclusion

Hopefully, this article helped you understand the differences between the types of casings in programming and where you will most likely encounter each one.

Thank you for reading, and happy coding!



