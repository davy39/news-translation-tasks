---
title: The benefits of using Lodash in the Go language without reflection
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T20:14:49.000Z'
originalURL: https://freecodecamp.org/news/the-benefits-of-using-lodash-in-the-go-language-without-reflection-1d64b5115486
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TiOHph4NBWwjeVHMvREuZw.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: golang
  slug: golang
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Tal Kol

  Working with Node.js, I’ve grown to rely on Lodash as an invaluable tool. It completes
  the JavaScript standard library with a set of handy functional operators over collections.
  I can’t recall a single JavaScript project I’ve worked on in ...'
---

By Tal Kol

Working with Node.js, I’ve grown to rely on [Lodash](https://lodash.com/) as an invaluable tool. It completes the JavaScript standard library with a set of handy functional operators over collections. I can’t recall a single JavaScript project I’ve worked on in recent years that hasn’t used it.

My experience of switching to Go has been very pleasant. Go resolves many of the issues I’ve had with Node.js over the years and yet remains as productive. I’ve been sorely missing one thing though — a library like Lodash.

### What’s so great about Lodash?

JavaScript isn’t a purely functional language, and most of the code I write in JavaScript tends to be imperative. Nevertheless, some principles of functional programming (like chaining operators and immutability) come in very handy when working with collections.

Let’s say I have an array with some duplicates I want to remove. All it takes is one line with Lodash:

Let’s say that I only want to keep colors that have names that are longer than 4 letters. This takes one line as well:

And now assume I want to capitalize the first letter of every color… yep, not more than one line. I can even do all of the above together:

Lodash is probably the handiest tool for working with collections in JavaScript.

### How would you do that in Go?

Let’s start with the first task: getting a unique slice. Googling for a best practice solution in Go yields this [blog post](https://kylewbanks.com/blog/creating-unique-slices-in-go) as a first result. This is the code, credits to [Kyle Banks](https://www.freecodecamp.org/news/the-benefits-of-using-lodash-in-the-go-language-without-reflection-1d64b5115486/undefined):

You can imagine that if we had to filter and capitalize the first letter of every color as well, we would spend way too much time on the mechanics of these actions. This would be a bit exhausting. Where are my one liners?

### Libraries to the rescue

Surely, there are some libraries that do these convenient collection actions for us. Surprisingly, there aren’t many popular ones in Go. Why is that?

To make such a library useful, it would have to support many types of collections. This is because you may have a slice of strings, a slice of integers, or a slice of structs. Supporting a **generic** type of slice isn’t straightforward in Go.

In most strictly typed languages, this is achieved with a language construct called [generics](https://en.wikipedia.org/wiki/Generic_programming). Unfortunately, Go doesn’t currently [support it](https://golang.org/doc/faq#generics).

So how can we implement such a library without generics? The Go guru Rob Pike shows an example implementation of the function `filter` in this [Github repo](https://github.com/robpike/filter). Notice the heavy use of [reflection](https://github.com/robpike/filter/blob/master/reduce.go#L22). Indeed, it’s not difficult to expand this technique and implement the various Lodash utility methods. You can see an example project that tries to do exactly that [here](https://github.com/arifsetiawan/lodash-go).

### Why should we prefer to avoid reflection?

Reflection examines types in runtime. By working our way around Go’s lack of generics with reflection, we’re moving the heavy lifting of dealing with multiple collection types from compile time to run time.

Basic utility functions that work with collections should be efficient. I haven’t done proper benchmarking, but relying on reflection for such a common task feels plain wrong.

So, as a thought experiment, what can we do instead? Can we create a truly efficient implementation of Lodash in Go that will rival the plain old **for loop** approach performance-wise?

### Compile time code generation

Generating code as part of the development toolchain isn’t a foreign concept in Go. It is used by the [Protobuf compiler](https://github.com/golang/protobuf) to generate Go access methods for protocol definitions. It has even been introduced as an official Go toolchain feature with `[go generate](https://blog.golang.org/generate)` since version 1.4.

What if we wish to move the heavy lifting of dealing with generic collection types back to compile time? The best way to do this (currently) is to generate type-specific code for every one of the types we need in our project!

Consider the implementation from before of `uniq` over a `string` slice:

How would the implementation differ if we needed support for an `int` slice?

As you can see, it’s pretty much identical, except every occurrence of `string` has been replaced with `int`.

Can we do this automatically somehow?

### Lodash in Go without reflection

Let’s design our API first. We can turn for inspiration to the original [Lodash](https://lodash.com/) implementation in JavaScript. There, the library is used with the underscore character `_`. For example, `_.uniq()`.

We can pay homage by keeping the same convention. The difference is that in our case, the underscore will be followed by a type. For example, `_int.Uniq()` for integers and `_string.Uniq()` for strings. We must specify the type explicitly since we’re going to get a completely new and dedicated implementation of the entire library for the specific type we need. This will guarantee that our runtime is as efficient as possible.

Usage is very straightforward. Just import the implementation you want:

There are dozens of potential types. Does that mean that our `go-dash/slice` library has to come with every single one? Not really, as this wouldn’t be practical. We’re going to generate the required implementations dynamically at compile time!

To achieve that, we’ll introduce an interesting command line tool: `_gen`, the code generator for our Lodash library implementation (notice how it starts with underscore as well).

When `_gen` is run in the source root of any project, it goes over all the source files in the project and looks for `github.com/go-dash/slice/_TYPE` imports. In the example above, it will find one for `_string` and one for `_int`. The generator will then generate an implementation for these specific types dynamically and add it to the library found in the Go workspace under the path`$GOPATH/src/github.com/go-dash/slice`.

The implementation of `go-dash/slice` on [Github](https://github.com/go-dash/slice) is actually very lean. It only contains a templated implementation for a single generic type. The code generator relies on this template to create the specific type implementations according to your requirements when you compile your project.

### What about custom types?

Assume your project defines a custom complex type like `Person`:

It would be quite convenient if we could use our Lodash library on a `Person` slice as well. Well, this actually can work in the exact same way. Simply import an implementation of `go-dash/slice` that works on `Person` and the code generator will take care of the rest:

### A working prototype

A working proof of concept of the `go-dash/slice` library, that provides several useful functions like `uniq`, `filter` and `chain`, is available on [Github](https://github.com/go-dash/slice).

The project also includes a working [command line generator](https://github.com/go-dash/_gen).

The command line generator is conveniently installable on Mac via [Homebrew](https://brew.sh/): `brew install go-dash/tools/gen`

Going back to our first example: let’s say we have a slice of string color names which we want to keep unique and filter for colors with length longer than 4 letters. We can finally implement this in one line:

If you like this direction and want to come help port the rest of the useful Lodash functions to Go, please contribute.

### Some final thoughts about syntax

The main thing that still bothers me with our chosen syntax is that we have an import per type. Is it possible to combine them somehow to a single implementation that will route to the correct place by type?

Consider the following:

This code combines all of the implementations into a unified `Uniq` that takes `interface{}`. While it doesn’t use reflection per se, it still has a two runtime dynamic casts and the switch which will affect performance. We should probably benchmark to see how much of an impact this adds. We should also probably benchmark the reflection implementation and see if our suspicion about runtime performance was indeed grounded in the first place.

Nevertheless, this was a fun thought experiment.

**_Tal is a founder at Orbs.com — a public blockchain infrastructure for large scale consumer applications with millions of users. To learn more and read the Orbs white papers [click here](https://orbs.com/white-papers). [Follow on [Telegram](https://t.me/orbs_network), [Twitter](https://twitter.com/orbs_network), [Reddit](https://www.reddit.com/r/ORBS_Network/)]_**

**_Note: if you’re interested in blockchain — come contribute! Orbs is a fully open source project where anyone can participate._**

![Image](https://cdn-media-1.freecodecamp.org/images/JWn9bUEABxzB3UAy7kCsYdYnHPsCsH8cDevu)

