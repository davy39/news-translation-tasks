---
title: Better Exception Handling in Java 8 Streams Using Vavr
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T18:42:01.000Z'
originalURL: https://freecodecamp.org/news/better-exception-handling-in-java-8-streams-using-vavr-6eda31285ce9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NubsZjUhLLRtGA7SkIvtjQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: Java
  slug: java
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Rajasekar Elango

  In this post, I will provide tips for better exception handling in Java 8 streams
  using the Functional Java library Vavr.

  The problem

  To illustrate with an example, let’s say we want to print the day of the week for
  a given stream...'
---

By Rajasekar Elango

In this post, I will provide tips for better exception handling in Java 8 streams using the Functional Java library [Vavr](http://www.vavr.io/).

### The problem

To illustrate with an example, let’s say we want to print the day of the week for a given stream of date strings in the format `MM/dd/YYYY`.

### Initial solution

Let’s start with an initial solution, as seen below, and iteratively improve on it.

This will output

_Huh_, if a date string is invalid, this fails at the first _DateTimeParseException_ without continuing with valid dates.

### Java 8 Optional to the rescue

We can refactor `parseDate` to return `Optional<LocalDa`te> to make it discard invalids and continue processing valid dates.

This will skip errors and converts all the valid dates.

```
WEDNESDAY Text '01-01-2015' could not be parsed at index 2 THURSDAY Text 'not a date' could not be parsed at index 0 FRIDAY
```

This is a great improvement, but the exception has to be handled within the `parseDate` method and can’t be passed back to the main method to deal with it. We can’t make the `parseDate` method throw a checked exception as the Streams API doesn’t play well with methods that throw exceptions.

### A better solution with Vavr’s Try Monad

[Vavr](http://www.vavr.io/) is a functional library for Java 8+. We will use the `Try` object from Vavr, which can be either an instance of `Success` or `Failure`. Basically [Try](http://www.javaslang.io/javaslang-docs/#_try) is a monadic container type which represents a computation that may either result in an exception, or return a successfully computed value. Here is the modified code using `Try`:

The output is

```
WEDNESDAY Failed due to Text '01-01-2015' could not be parsed at index 2 THURSDAYFailed due to Text 'not a date' could not be parsed at index 0 FRIDAY
```

Now the exception is passed back to main to deal with it. Try also has APIs to implement recovery logic or return a default value in case of error.

To demonstrate this, let’s say we also want to support `MM-dd-YYYY` as an alternate string format for dates. The below example shows how we can easily implement recovery logic.

The output shows that now the date `01-01-2015` is also successfully converted.

```
WEDNESDAY THURSDAY THURSDAY Failed due to Text 'not a date' could not be parsed at index 0 FRIDAY
```

So _Try Monad_ can be used to elegantly deal with exceptions and _fail fast_ on errors.

**_Update on 12/03/2018:_**

The code examples are updated to use [Doculet](https://doculet.net/).

_Originally published at [http://erajasekar.com/posts/better-exception-handling-java8-streams-using-javaslang/](http://erajasekar.com/posts/better-exception-handling-java8-streams-using-javaslang/)._

