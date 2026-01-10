---
title: A look at the Optional datatype in Java and some anti-patterns when using it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T09:04:42.000Z'
originalURL: https://freecodecamp.org/news/optional-in-java-and-anti-patterns-using-it-7d87038362ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UEpbSnAgz65SLvAbvR3nbA.jpeg
tags:
- name: clean code
  slug: clean-code
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Mervyn McCreight

  by Mervyn McCreight and Mehmet Emin Tok


  Overview

  In this article, we are going to talk about experiences we gathered while working
  with Java’s Optional-datatype, which has been introduced with Java 8. During our
  daily business, w...'
---

By Mervyn McCreight

_by_ [Mervyn McCreight](https://www.freecodecamp.org/news/optional-in-java-and-anti-patterns-using-it-7d87038362ba/undefined) _and_ [Mehmet Emin Tok](https://www.freecodecamp.org/news/optional-in-java-and-anti-patterns-using-it-7d87038362ba/undefined)

![Image](https://cdn-media-1.freecodecamp.org/images/K2LKxHKECSsGZxGXipMfxYpRKElJA1Lp1Goj)

#### Overview

In this article, we are going to talk about experiences we gathered while working with Java’s _Optional_-datatype, which has been introduced with Java 8. During our daily business, we encountered some _“anti-patterns”_ we wanted to share. Our experience was that if you strictly avoid having those patterns in your code, chances are high that you will come to a cleaner solution.

#### Optional — the Java way to explicitly express the possible absence of a value

The purpose of _Optional_ is to express the potential absence of a value with a data-type instead of having the implicit possibility to have an absent value just because _null-reference_ exists in Java.

If you take a look at other programming languages, which do not have a _null-value_, they describe the potential absence of a value through data-types. In Haskell, for example, it is done using [Maybe](https://hackage.haskell.org/package/base-4.11.1.0/docs/Data-Maybe.html), which in my opinion has proven to be an effective way to handle a possible “no-value”.

```
data Maybe a = Just a              | Nothing
```

The code-snippet above shows the definition of [Maybe](https://hackage.haskell.org/package/base-4.11.1.0/docs/Data-Maybe.html) in Haskell. As you can see, _Maybe a_ is parametrized by the type-variable _a_, which means that you can use it with any type you want to. Declaring the possibility of an absent value using a data-type, e.g. in a function, forces you as a user of the function to think about both possible results of an invocation of the function — the case where there actually is something meaningful present and the case where it is not.

Before _Optional_ was introduced into Java, the “java-way” to go if you wanted to describe the nothing was the _null-reference_, which can be assigned to any type. Because everything can be null, it gets obfuscated if something is intended to be null (e.g. if you want something to either represent a value or nothing) or not (e.g. if something _can_ be null, because everything can be null in Java, but in the flow of the application, it should not be null at any time).

If you want to specify that something can explicitly be nothing with a certain semantic behind it, the definition looks the same, like if you expect something to be present all the time. The inventor of the null-reference [_Sir Tony Hoare_](https://en.wikipedia.org/wiki/Tony_Hoare) even apologized for the introduction of the null-reference.

> I call it my billion-dollar mistake…At that time, I was designing the first comprehensive type system for references in an object-oriented language. My goal was to ensure that all use of references should be absolutely safe, with checking performed automatically by the compiler. But I couldn’t resist the temptation to put in a null reference, simply because it was so easy to implement. This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage in the last forty years. (Tony Hoare, 2009 — [QCon London](https://qconlondon.com/))

To overcome this problematic situation, developers invented many methods like annotations _(Nullable, NotNull),_ naming-conventions (e.g. prefixing a method with _find_ instead of _get_) or just using code-comments to hint that a method may intentionally return _null_ and the invoker should care about this case. A good example for this is the _get-function_ of the map-interface of Java.

```
public V get(Object key);
```

The definition above visualizes the problem. Just by the implicit possibility that everything can be a _null-reference_, you can not communicate the option that the result of this function can be _nothing_ using the signature of the method. If a user of this function looks at its definition, they do not stand a chance to know this method could return a _null-reference_ by intention — because it could be the case that no mapping to the provided key exists in the map-instance. And this is exactly what the documentation of this method tells you:

> Returns the value to which the specified key is mapped, or `null` if this map contains no mapping for the key.

The only chance to know this is by looking deeper into the documentation. And you have to remember — not all code is well documented like this. Imagine you have platform-internal code in your project, which does not have any comments, but surprises you with returning a _null-reference_ somewhere deep down its call-stack. And this is where expressing the potential absence of a value with a data-type shines.

```
public Optional<V> get(Object key);
```

If you take a look at the type-signature above, it is clearly communicated that this method MAY return nothing — it even forces you to deal with this case, because it is expressed with a special data-type.

So having _Optional_ in Java is nice, but we encounter some pitfalls if you use _Optional_ in your code. Otherwise the usage of _Optional_ might make your code even less readable and intuitive (long story short — less clean). The following parts will cover some patterns we found out to be some sort of “anti-patterns” for Java’s _Optional_.

#### Optional in Collections or Streams

A pattern we encountered in code we worked with is having empty optionals stored in a collection or as an intermediate state inside a stream. Typically this was followed by filtering out the empty optionals and even followed by invoking _Optional::get_, because you do not really need to have a collection of optionals. The following code example shows a very simplified case of the described situation.

```
private Optional<IdEnum> findValue(String id) {   return EnumSet.allOf(IdEnum.class).stream()      .filter(idEnum -> idEnum.name().equals(id)      .findFirst();};
```

```
(...)
```

```
List<String> identifiers = (...)
```

```
List<IdEnum> mapped = identifiers.stream()   .map(id -> findValue(id))   .filter(Optional::isPresent)   .map(Optional::get)   .collect(Collectors.toList());
```

As you can see, even in this simplified case it becomes hard to understand what the intention of this code is. You have to take a look at the findValue-method to get the intention of it all. And now imagine the findValue-method to be more complex than mapping a string representation to its enumeration-typed value.

There also is an interesting read about why you should avoid having _null_ in a collection [[UsingAndAvoidingNullExplained](https://github.com/google/guava/wiki/UsingAndAvoidingNullExplained)]. In general you do not really need to have an empty optional in a collection. This is because an empty optional is the representation for “nothing”. Imagine having a List with three items in it and they are all empty optionals. In most scenarios an empty list would be semantically equivalent.

So what can we do about it? In most cases the plan to _filter first before mapping_ leads to more readable code, since it was directly stating what you want to achieve, instead of hiding it behind a chain of _maybe mapping_, _filtering and then mapping_.

```
private boolean isIdEnum(String id) {   return Stream.of(IdEnum.values())      .map(IdEnum::name)      .anyMatch(name -> name.equals(id));};
```

```
(...)
```

```
List<String> identifiers = (...)
```

```
List<IdEnum> mapped = identifiers.stream()   .filter(this::isIdEnum)   .map(IdEnum::valueOf)   .collect(Collectors.toList());
```

If you imagine the _isEnum-method_ to be owned by the IdEnum itself, it would become even clearer. But for the sake of having a readable code example it is not in the example. But just by reading the above example, you can easily understand what is going on, even without really having to jump into the referenced _isIdEnum-method_.

So, long story short — if you do not need the absence of a value expressed in a list, you do not need Optional — you just need its content, so optional is obsolete inside collections.

#### Optional in method parameters

Another pattern we encountered, especially when code is getting migrated from the “old-fashioned” way of using a _null-reference_ to using the _optional-type,_ is having optional-typed parameters in function-definitions. This typically happens if you find a function that does null-checks on its parameters and applies different behaviour then — which, in my opinion, was bad-practice before anyways.

```
void addAndUpdate(Something value) {    if (value != null) {      somethingStore.add(value);   }    updateSomething();}
```

If you “naively” refactor this method to make use of the optional-type, you might end up with a result like this, using an optional-typed parameter.

```
void addAndUpdate(Optional<Something> maybeValue) {   if (maybeValue.isPresent()) {      somethingStore.add(maybeValue.get());   }   updateSomething();}
```

In my opinion, having an optional-typed parameter in a function shows a design-flaw in every case. You either way have some decision to make if you do something with the parameter if it is there, or you do something else if it is not — and this flow is hidden inside the function. In an example like above, it is clearer to split the function into two functions and conditionally call them (which would also happen to fit to the “one intention per function”-principle).

```
private void addSomething(Something value) {   somethingStore.add(value);}
```

```
(...)
```

```
// somewhere, where the function would have been calledOptional.ofNullable(somethingOrNull).ifPresent(this::addSomething);updateSomething();
```

In my experience, if I ever encountered examples like above in real code, it always was worth refactoring “‘till the end”, which means that I do not have functions or methods with optional-typed parameters. I ended up with a much cleaner code-flow, which was much easier to read and maintain.

Speaking of which — in my opinion a function or method with an optional parameter does not even make sense. I can have one version with and one version without the parameter, and decide in the point of invocation what to do, instead of deciding it hidden in some complex function. So to me, this was an anti-pattern before (having a parameter that can **intentionally** be null, and is handled differently if it is) and stays an anti-pattern now (having an **optional-typed** parameter).

#### Optional::isPresent followed by Optional::get

The old way of thinking in Java to do null-safe programming is to apply null-checks on values where you are not sure if they actually hold a value or are referencing to a _null-reference_.

```
if (value != null) {   doSomething(value);}
```

To have an explicit expression of the possibility that _value_ can actually be either something or nothing, one might want to refactor this code so you have an optional-typed version of value.

```
Optional<Value> maybeValue = Optional.ofNullable(value);
```

```
if (maybeValue.isPresent()) {   doSomething(maybeValue.get());}
```

The example above shows the “naive” version of the refactoring, which I encountered quite often in several code examples. This pattern of _isPresent_ followed by a _get_ might be caused by the old null-check pattern leading one in that direction. Having written so many null-checks has somehow trained us to automatically think in this pattern. But _Optional_ is designed to be used in another way to reach more readable code. The same semantics can simply be achieved using _ifPresent_ in a more readable way.

```
Optional<Value> maybeValue = Optional.ofNullable(value);maybeValue.ifPresent(this::doSomething);
```

“But what if I want to do something else instead, if the value is not present” might be something you think right now. Since Java-9 _Optional_ comes with a solution for this popular case.

```
Optional.ofNullable(valueOrNull)    .ifPresentOrElse(        this::doSomethingWithPresentValue,        this::doSomethingElse    );
```

Given the above possibilities, to achieve the typical use-cases of a null-check **without** using _isPresent_ followed by a _get_ makes this pattern sort of a anti-pattern. _Optional_ is per API designed to be used in another way which in my opinion is more readable.

#### Complex calculations, object-instantiation or state-mutation in orElse

The Optional-API of Java comes with the ability to get a guaranteed value out of an optional. This is done with _orElse_ which gives you the opportunity to define a default value to fall back to, if the optional you are trying to unpack is actually empty. This is useful every time you want to specify a default behaviour for something that _can_ be there, but does not have to be done.

```
// maybeNumber represents an Optional containing an int or not.int numberOr42 = maybeNumber.orElse(42);
```

This basic example illustrates the usage of _orElse_. At this point you are guaranteed to either get the number you have put into the optional or you get the default value of 42. Simple as that.

But a meaningful default value does not always have to be a simple constant value. Sometimes a meaningful default value may need to be computed in a complex and/or time-consuming way. This would lead you to extract this complex calculation into a function and pass it to orElse as a parameter like this.

```
int numberOrDefault = maybeNumber.orElse(complexCalculation());
```

Now you either get the number or the calculated default value. Looks good. Or does it? Now you have to remember that Java is passing parameters to a function by the concept of **call by value**. One consequence of this is that in the given example the function _complexCalculation_ will **always** be evaluated, even if orElse will not be called.

Now imagine this _complexCalculation_ is really complex and therefore time-consuming. It would **always** get evaluated. This would cause performance issues. Another point is, if you are handling more complex objects as integer values here, this would also be a **waste of memory** here, because you would always create an instance of the default value. Needed or not.

But because we are in the context of Java, this does not end here. Imagine you do not have a time-consuming but a state-changing function and would want to invoke it in the case where the Optional is actually empty.

```
int numberOrDefault = maybeNumber.orElse(stateChangingStuff());
```

This is actually an even more dangerous example. Remember — like this the function will **always** be evaluated, needed or not. This would mean you are always mutating the state, even if you actually would not want to do this. My personal opinion about this is to avoid having state mutation in functions like this at all cost.

To have the ability to deal with issues like described, the Optional-API provides an alternative way of defining a fallback using _orElseGet_. This function actually takes a _supplier_ that will be invoked to generate the default value.

```
// without method referenceint numberOrDefault = maybeNumber.orElseGet(() -> complex());
```

```
// with method referenceint numberOrDefault = maybeNumber.orElseGet(Something::complex);
```

Like this the supplier, which actually generates the default value by invoking _complex_ will only be executed when _orElseGet_ actually gets called — which is if the optional is empty. Like this _complex_ is **not** getting invoked when it is not needed. No complex calculation is done without actually using its result.

A general rule for when to use _orElse_ and when to use _orElseGet_ can be:  
If you fulfill **all three criteria**

1. a simple default value that is not hard to calculate (like a constant)
2. a not too memory consuming default value
3. a non-state-mutating default value function

then use _orElse_.   
Otherwise use _orElseGet_.

#### Conclusion (TL;DR)

* Use Optional to communicate an intended possible absence of a value (e.g. the return value of a function).
* Avoid having Optionals in collections or streams. Just fill them with the present values directly.
* Avoid having Optionals as parameters of functions.
* Avoid Optional::isPresent followed by Optional::get.
* Avoid complex or state changing calculations in orElse. Use orElseGet for that.

#### Feedback & Questions

What is your experience so far with using Java Optional? Feel free to share your experiences and discuss the points we brought up in the comment section.

