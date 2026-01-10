---
title: The Great Programming Jargon Bake-off
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-20T16:29:43.000Z'
originalURL: https://freecodecamp.org/news/programming-mental-models-47ccc65eb334
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d55K-aHn7CPPe-M83e_n5g.jpeg
tags:
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Preethi Kasireddy

  Imperative vs. Declarative. Pure vs. Impure. Static vs. Dynamic.

  Terminology like this is sprinkled throughout programming blog posts, conference
  talks, papers, and text books.

  But don’t be turned off by this jargon. Let’s jump r...'
---

By Preethi Kasireddy

Imperative vs. Declarative. Pure vs. Impure. Static vs. Dynamic.

Terminology like this is sprinkled throughout programming blog posts, conference talks, papers, and text books.

But don’t be turned off by this jargon. Let’s jump right in and break some of these concepts down, so you can understand what all these developers around you are talking about.

### Static vs. Dynamic Typing

This is about when a type information is acquired — either at compile time or at runtime.

You can use this type information to detect type errors. A type error is when a value is not of the expected type.

#### Static Type Checking

The process of verifying the type safety of a program based on analysis of a program’s source code. In other words, type checking happens at compile time, allowing type errors to be detected sooner.

![Image](https://cdn-media-1.freecodecamp.org/images/GD1KhgaCFzdaiATtb-MnKj3L-ZXUiIoydrc8)

#### Dynamic Type Checking

The process of verifying the type safety of a program at runtime. With dynamic type checking, type errors occur at runtime.

![Image](https://cdn-media-1.freecodecamp.org/images/r0NYTBqJGSc8XLHqK8Et-rMW0tkOd3VI7I5u)

### Strong vs. Weak typing

It’s important to note strong vs. weak typing doesn’t have a universally-agreed-upon technical meaning. For example, even though Java is statically typed, every time you use reflection or a cast, you’re deferring the type check to run time.

Similarly, most strongly-typed languages will still automatically convert between integers and floats. Hence, you should avoid using these terms because calling a type system “strong” or “weak” by itself does not communicate very much.

#### Strongly Typed

In a strongly typed language, the type of a construct does not change — an `int` is always an `int`, and trying to use it as a `string` will result in an error.

![Image](https://cdn-media-1.freecodecamp.org/images/qQuFtQHI0nVeCYYPFiwmtPXD0I0VtUfQS3VH)

#### Weakly typed

Weak typing means that the type of a construct can change depending on context. For example, in a weakly-typed language, the string “123” may be treated as the number 123 if you add another number to it.

It generally means the type system can be subverted (invalidating any guarantees) because you can cast a value of one type to another.

![Image](https://cdn-media-1.freecodecamp.org/images/iKBgNAycyEVpLytn2tivoY3U0wN-osYulEJr)

### Mutable vs. Immutable data

#### Immutable data

When an object is not modifiable after it has been created, you can say it’s “immutable” which is a fancy word for “unchangable.” This means you’ll instead allocate a new value for every change.

![Image](https://cdn-media-1.freecodecamp.org/images/D3tF-qLMqDUXzFdHRRXy9jZm5ZrZ-DJVxi-p)

#### Mutable data

When you can modify an object after its creation, it’s “mutable.” When you have a reference to a mutable object, for instance, the contents of the object can change.

![Image](https://cdn-media-1.freecodecamp.org/images/lKF181TAlPPvUz0ln8VLksubyCYCbs8ocB73)

### Pure vs. Impure functions

#### Pure functions

A pure function has two qualities:

1. It relies only on the input provided — and not on any external state that may change during its evaluation or in between calls.
2. It doesn’t cause any semantically observable side effects, such as modifying a global object or a parameter passed by reference.

![Image](https://cdn-media-1.freecodecamp.org/images/ir5sDGMoxckbC-wpR8JikApucz6DLkkPzGZx)

#### Impure functions

Any function that does not meet those two requirements for a pure function is “impure.”

![Image](https://cdn-media-1.freecodecamp.org/images/J02vTF9q3BE9lIYoi2jV1QbJAqjRcMZJBw8L)

### Lazy Evaluation vs. Eager Evaluation

#### Lazy evaluation

Lazy evaluation does not evaluate function arguments unless their values are required to evaluate the function call itself.

In other words, expressions are only evaluated when evaluating another expression which are dependent on the current expression.

Laziness allows programs to calculate data structures that are potentially _infinite_ without crashing.

![Image](https://cdn-media-1.freecodecamp.org/images/uxczq1DSf-SYP34fDk02eeBqbbEFaqwsUwP0)

#### Eager evaluation

Eager evaluation — also known as strict evaluation — always fully evaluates function arguments before invoking the function. In other words, an expression is evaluated as soon as it is bound to a variable.

![Image](https://cdn-media-1.freecodecamp.org/images/SHUGZI2HS4n8mSPAWoUfWySxt8D4X0N5CXu-)

### Declarative vs. Imperative

#### Declarative programming

Declarative programs express a set of operations without revealing how they’re implemented, or how data flows through them. They focus on “what” the program should accomplish (by using expressions to describe the logic) rather than “how” the program should achieve the result.

One example of declarative programming is SQL. SQL queries are composed of statements that describe what the outcome of a query should look like, while abstracting over the internal process for how the data is retrieved:

```
SELECT EMP_ID, FIRST_NAME, LAST_NAMEFROM EMPLOYEESWHERE CITY = ‘SAN FRANCISCO’ORDER BY EMP_ID;
```

Here’s an example of declarative code:

![Image](https://cdn-media-1.freecodecamp.org/images/KJkzhjbfo5EYE2flsvDS9gT0JqAIcKcfklcA)

#### Imperative programming

Imperative programming focuses on describing how a program should achieve a result by using statements that specify control flow or state changes. It uses a sequence of statements to compute a result.

Here’s an example of imperative code:

![Image](https://cdn-media-1.freecodecamp.org/images/nWC5LzuByaWllxXsVXJS1pcYokOWlKxkZor2)

### Stateful vs. Stateless

A state is a sequence of values calculated progressively, which contains the intermediate results of a computation.

#### Stateful

Stateful programs have some mechanism to keep track of and update state. They have some memory of the past, and remember previous transactions that may affect the current transaction.

![Image](https://cdn-media-1.freecodecamp.org/images/2MCDlKSDdS9imKRxHECiksWO2jjxjeV1ndVB)

#### Stateless

Stateless programs, on the other hand, doesn’t keep track of state. There’s no memory of the past. Every transaction is performed as if it were being done for the very first time. Stateless programs will give the same response to the same request, function, or method call — every single time.

![Image](https://cdn-media-1.freecodecamp.org/images/O4aqQxCiZF-tsYmo4yl34wrLs8wGOsWODvy3)

### Functional vs. Object-Oriented

#### Functional

Functional programming is a paradigm that places a major emphasis on the use of functions. The goal of functional programming is to use functions to abstract control flows and operations on data, and to avoid side effects.

So functional programming uses pure functions and avoids mutable data, which in turn provides _referential transparency._

A function has referential transparency when you can freely replace an expression with its value and not change the behavior of the program. Said a bit differently: for a given input, it always returns the same results.

Some examples languages that emphasize functional programming include Haskell, Lisp, Clojure, and Elm. But you can use functional programming concepts in most languages, including JavaScript.

#### Object Oriented

The Object Oriented programming paradigm places major emphasis on the use of objects. This results in programs that are made out of objects that interact with one another. These objects can contain data (in the form of fields or attributes) and behavior (in the form of methods).

It’s a style of partitioning (or encapsulating) the state of a program via objects to make analyzing the effect of changes tractable [1].

Moreoever, object-oriented programs uses inheritance and/or composition as their main mechanisms for code reuse. Inheritance means that a new class can be defined in terms of existing classes by specifying just how the new class is different. It represents an “is-a” relationship (e.g. a Bird class which extends an Animal class). Composition, on the other hand, is when classes contain instances of other classes that implement the desired functionality. It represents a “has a” relationship (e.g. a Bird class has an instance of a Wing class as it’s member).

Polymorphism is also an important mechanism for code reuse in object oriented programming. It’s when a language can process objects differently depending on their data type or class.

Some examples languages that emphasize object oriented programming include Java, C++, Ruby. Again, you can apply these concepts in most languages, including JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/N8MHF9tH7WY137DollJShA9icCiaduLFJS9O)

### Deterministic vs. Nondeterministic

#### Deterministic

Deterministic programs always return the same result any time they’re called with a specific set of input values and the same given state.

![Image](https://cdn-media-1.freecodecamp.org/images/QZcUv8Ergv0DU4N3SSrR6SFbajhNRXzagcTr)

#### Nondeterministic

Nondeterministic programs may return different results each time they’re called, even with the same specific set of input values and initial state.

Nondeterminism is a property of any concurrent system — that is, any system where multiple tasks can happen at the same time by running on different threads. A concurrent algorithm that is mutating state might perform differently on each time, depending upon which thread the scheduler decides to execute.

For example:

```
declare Xthread X=1 endthread X=2 end
```

The execution order of the two threads is not fixed. We don’t know whether X will be bound to 1 or 2. The system will choose during the program’s execution, and it’s free to choose which thread to execute first.

Another example of non-determinism:

![Image](https://cdn-media-1.freecodecamp.org/images/V0yGj2uPPh5HUKf25kTgQiGZwLG8eAsRjkXM)

### Phew! We’re done.

As always, your feedback and input is really important to me. I read and consider every single comment, so please don’t shy away from responding!

Finally, you can also check out the [Prezi presentation](http://prezi.com/fftgbgltl-6u/?utm_campaign=share&utm_medium=copy&rc=ex0share) I built for this article.

[1] Thank you to [Kent Beck](https://www.freecodecamp.org/news/programming-mental-models-47ccc65eb334/undefined) for his input on this.

