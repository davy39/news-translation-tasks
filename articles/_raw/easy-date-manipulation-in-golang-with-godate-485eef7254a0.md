---
title: Easy date manipulation in Golang with Godate
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T16:31:17.000Z'
originalURL: https://freecodecamp.org/news/easy-date-manipulation-in-golang-with-godate-485eef7254a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6iBVfeqbc8V9MEuhlYOTdQ.jpeg
tags:
- name: coding
  slug: coding
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kofo Okesola

  I have always been and always will be a fan of Carbon and how easy it is to get
  date manipulation done so efficiently. Being a fan of Carbon and also being a fan
  of Golang I thought why not write a library called godate. It will do fo...'
---

By Kofo Okesola

I have always been and always will be a fan of [Carbon](https://carbon.nesbot.com/) and how easy it is to get date manipulation done so efficiently. Being a fan of Carbon and also being a fan of Golang I thought why not write a [library called godate](https://github.com/kofoworola/godate). It will do for golang what carbon does for Php, and in this article I will explain how to use it.

### Package Breakdown

The package is mostly a `GoDate` struct with its available helper methods, which acts as a wrapper to a `Time` struct. It also includes some functions for initializing, e.g. `Now` `Tomorrow`.

### Usage

#### Installation

```
go get github.com/kofoworola/godate
```

It also supports [go’s new module system](https://github.com/golang/go/wiki/Modules). You can simply import it into your project and run. Go will attempt to install the latest version of the package, which is v1.2.0 as of the time of writing this.

#### Usage

Create a new GoDate struct with any of the methods currently available

Note the difference in Timezone, which is why I recommend creating a GoDate struct with a `time.Location` object passed.

Once you have a struct you can easily chain methods on the struct to achieve your result like so:

### Available Methods

#### Compare

The available compare methods are `IsBefore` , `IsBefore` and `IsWeekend` . The method names explain what they do:

#### Difference

The most important Difference methods are highlighted below. Although there are more methods included that are also used in the logic of these:

The `Difference` methods that take another `goDate` as a parameter calculates the difference as `methodOwner — parameter` . A negative difference means the parameter occurs after the `methodOwner`.

#### String Formatting

These are the current available String formatting methods. You can also [format](https://yourbasic.org/golang/format-parse-string-time-date-example/)(you might want to read that if you’re new to dates in golang) this your way by calling the `Format()` method

#### Helper

Some of the extra helper methods and their outputs are listed below:

Note the `EndOfWeek` and `StartOfWeek` methods use `time.Sunday` as the default start of the week. This behavior can be changed for the current godate struct by calling `now.SetFirstDay(time.Monday)` .

### Conclusion

The package is far from complete (and probably never will be). The aim is to provide a robust date handling API similar to and even better (someone’s ambitious here…) than [Carbon](https://carbon.nesbot.com). So you Go lovers out there like me should make it rain PRs on the [repo](https://github.com/kofoworola/godate) (and stars :)

