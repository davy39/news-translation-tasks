---
title: How to solve the Builder pattern’s boilerplate problem
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-14T16:08:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-builder-patterns-boilerplate-problem-2ea97001dbe6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*pWJ2kCkdoFaXrlK6.
tags:
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Harshdeep S Jawanda

  There is a widely-held belief that one of Java’s primary shortcomings is that writing
  “good” (idiomatic) Java requires a lot of boilerplate code. Just ask any Java practitioner.
  Nowhere is this more evident than in the Builder ...'
---

By Harshdeep S Jawanda

There is a widely-held belief that one of Java’s primary shortcomings is that writing “good” (idiomatic) Java requires a lot of boilerplate code. Just ask any Java practitioner. Nowhere is this more evident than in the [Builder pattern](http://www.informit.com/articles/article.aspx?p=1216151&seqNum=2). In this article, I present two solutions to this problem and discuss their advantages and pitfalls.

### An introduction to the builder pattern

The builder pattern is great for classes that can have complex initialization. It typically consists of setting values for multiple variables, some of which may be required with the rest being optional. Using [static factory methods](http://www.informit.com/articles/article.aspx?p=1216151&seqNum=1) or constructors can lead to the **telescoping constructor pattern**, described by [Joshua Block](https://twitter.com/joshbloch) (“Effective Java author, API Designer, Swell guy,” as his Twitter says) like this:

> …in which you provide a constructor with only the required parameters, another with a single optional parameter, a third with two optional parameters, and so on, culminating in a constructor with all the optional parameters.

Even if there are only five required parameters, but all are of the same **type**, a developer can easily make a mistake with the ordering of the parameters being passed in. This can result in subtle, often hard-to-find bugs.

The builder pattern offers an elegant solution to all these issues. Further, this pattern can help the developer ensure that all the pre-conditions of the object are satisfied **before** constructing the object. This guarantees that the constructed object is in a consistent state.

All these rosy advantages aside, actually writing a builder can be quite a tedious and repetitive task. “So what!?” you say, “At least I am getting all these advantages!” Sure you are…but come back and talk to me when you’re writing your **tenth** builder on the same project.

So let’s look at some other options.

### Doing it Dynamically: Lombok

[Lombok](https://projectlombok.org) is a tool/library well-known to many Java developers (though not enough, IMHO). According to its website, it “is a Java library that automatically plugs into your editor and build tools, spicing up your java.” [Lombok adds so many features through dynamic code generation](https://projectlombok.org/features/all) that they simply cannot be covered here. We’ll focus on the `[@Builder](https://projectlombok.org/features/Builder)` annotation.

The `@Builder` annotation — as the name suggests — can be used to generate a builder for any POJO. It can be used by placing it on the class, on a constructor, or on a static method ([see the documentation](https://projectlombok.org/features/Builder) for details). Just place the annotation on the `Person` class:

And by the magic of Lombok, a `PersonBuilder` class is automatically generated instantaneously. We can now instantiate a `Person` object using the builder pattern:

```
Person.builder().firstName("Adam").lastName("Savage")    .city("San Francisco").jobTitle("TV Personality").build();
```

Placing the `@Builder` annotation on the `Person` class

1. creates a `PersonBuilder` class with [fluent setters](https://en.wikipedia.org/wiki/Fluent_interface) for all the properties of `Person` class and a `build()` method to construct a `Person` object using the values set, and,
2. adds a `public static builder()` method to the `Person` class that returns a new instance of `PersonBuilder`.

Placing the `@Builder` annotation on a constructor or static method does the same things as above, but generates setters only for the parameters listed in the constructor/static method.

Adding the `@NonNull` annotation to a field of the `Person` class makes it a **required** parameter. Not setting its value using `PersonBuilder`’s corresponding setter method will throw a `NullPointerException` when the `build()` method is called.

The beauty of Lombok is that none of this generated code is visible in the source file (though Eclipse will show the generated class(es), methods, and fields in the Outline view), leaving it very clean and tidy. The developer only needs to focus on the important parts of a POJO, not the tedious nuts-and-bolts of its (often) mundane implementation. Make any change in the POJO, and Lombok immediately updates/generates the relevant code.

#### Lombok’s Shortcomings

Despite all this magical goodness, Lombok isn’t perfect.

The biggest shortcoming of generating builders through Lombok is that if you require validation more complex than a non-null check in your builder, you’re out of luck. You can [delombok](https://projectlombok.org/features/delombok), copy over the code, and modify it by hand, but that’s quite tedious and negates all the convenience of using Lombok in the first place.

[Assigning default values to a POJO’s fields](https://reinhard.codes/2016/07/13/using-lomboks-builder-annotation-with-default-values/) used to be very tedious:

1. Write the skeleton of the correctly-named builder class.
2. Write the corresponding/correctly-named field and set it to the default value.

However, assigning default values has become easier since v1.16.16 of Lombok by using the `@Builder.Default` annotation:

Another shortcoming — though not everybody will agree with this — is that the null-checking (whether a **required** value has been set) and NPE-throwing is done **in the constructor** of the POJO, not **before** constructing the POJO. I prefer to not construct a POJO at all if its pre-conditions aren’t being satisfied.

A more general issue with Lombok is that it doesn’t play well with IDE refactoring tools. Consider the following (admittedly silly) code:

If we were to rename `Person` class to `HumanBeing`, the corresponding builder’s generated name would become `HumanBeingBuilder`. But the IDE’s refactoring tools will fail to update `PersonBuilder` above to `HumanBeingBuilder` (at least in Eclipse :-) ).

There is, however, a simple workaround for this issue: just use the `Builder` annotation’s `builderClassName` option to set a fixed name for the builder class: `@Builder(builderClassName = "Builder")` . Then all references to the builder class will become `Person.Builder`, which will be correctly changed by refactoring to `HumanBeing.Builder`.

### Doing it Statically: Eclipse Spark Plugin

The [Eclipse Spark plugin](https://marketplace.eclipse.org/content/spark-builder-generator) allows you to generate builder code for a POJO by clicking a single button in the toolbar: it’s that simple! Clicking on the button will (optionally) show you the list of fields to choose from to use in the builder. The code is generated right in front of your eyes and is readable in the file.

Generating a builder with the Spark plugin makes the `Person` class look like this:

Now that the entire generated code is right in front of you, you can customise it (or not!) to your heart’s content. But this is not even the best part of the Spark story.

Spark also lets you generate [staged builders](http://blog.crisp.se/2013/10/09/perlundholm/another-builder-pattern-for-java): your eyes light up with joy the first time you use a staged builder and your IDE offers exactly the correct auto-complete suggestions! Explaining staged builders is beyond the scope of this article, so read the article linked above to know more.

None of Lombok’s shortcomings mentioned above apply to the Spark plugin.

#### Spark Plugin’s Shortcomings

When all is said and done, using the Spark plugin does produce a lot of visible code. Even though you may not have had to write it by hand, it does increase the **visual weight** of the source file, and makes it seem big and complicated. Many developers may not like that vs. Lombok.

Another issue is that Spark is a one-trick pony: generating builders is all it can do — compare that to [all the things Lombok can do](https://projectlombok.org/features/all).

### So Which is it?

The tool you should be using depends on your unique situation and your preferences. I will continue to prefer Lombok in the vast majority of cases, switching to Spark whenever I require fine-grained control.

Which would you choose?

### Last but Not the Least…

If you found this article helpful, please don’t forget to clap ;-)!

Constructive discussions and corrections are most welcome.

