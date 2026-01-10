---
title: How to Handle Null References in the Latest Version of C#
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-12-11T18:16:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-null-references-in-csharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/article-null.jpg
tags:
- name: C
  slug: c
seo_title: null
seo_desc: "By Zoran Horvat\nC# 12 has just been released, and it continues the long\
  \ tradition of improvements in the safety of the language's software design and\
  \ execution. \nOne of these improvements relates to manipulating null references,\
  \ a programming concept..."
---

By Zoran Horvat

C# 12 has just been released, and it continues the long tradition of improvements in the safety of the language's software design and execution. 

One of these improvements relates to manipulating null references, a programming concept that many developers don't really love. 

Using null references in your code can cause all kinds of issues, like exceptions and a lack of information.

This article will teach you how to cope with null references in the latest version of the C# programming language and .NET. The name of the game: let no null pass unattended.

This demonstration will have several stages, each with its own small demo. If you wish to skip through, please use the table of contents below.

## Table of Contents

  1. [Prerequisites](#heading-prerequisites)
  1. [How to Use Nullable Reference Types](#heading-how-to-use-nullable-reference-types)
  1. [How to Use the `is null` and `is not null` Patterns](#heading-how-to-use-the-is-null-and-is-not-null-patterns)
  1. [How to Use `Type-Test-and-Set` Patterns](#heading-how-to-use-type-test-and-set-patterns)
  1. [How to Use `Property` Patterns](#heading-how-to-use-property-patterns)
  1. [How to Use the Null Propagation and Null Coalescing Operators](#heading-how-to-use-the-null-propagation-and-null-coalescing-operators)
  1. [How to Work with Optional Objects](#heading-how-to-work-with-optional-objects)
  1. [Final Notes](#heading-final-notes)

## Prerequisites

There are a few prerequisites you will need to meet before proceeding. I assume that you've written enough C# code to see null references in their natural habitat. And I expect you to understand that they can threaten the code's design and stability. 

This article will clarify these concepts and identify the issues and solutions using C# syntax and libraries.

If you are ready, we can get started with nullable reference types. That will allow us to set up the working environment and get up to speed for the more complex demos that will follow.

## How to Use Nullable Reference Types

Nullable reference types were introduced in C# 8 and quickly became a mainstay.

The short story is that you can either declare a reference nullable (for example, `string? s`) or non-nullable (`string s`). 

Note the plot twist: what used to be just a reference before C# 8 (`string s` was an ordinary reference to a *nullable* string) has now become something more: a reference that should never be set to null. 

That was the breaking change, maybe the first in a decade of C# syntax evolution!

The compiler will do its best to check if all the assignments to a non-nullable reference (the one without the question mark) set it to a proper object. If it finds an execution path that might set it to null, the compiler will issue a compile-time warning. This is called "definite assignment analysis," as the compiler tries to prove that each non-nullable reference is *definitely* assigned to an object.

If you have already grown accustomed to nullable reference types, I have a question: would you consider not using them today? Probably not.

Let's start with some code. Below, you see two records – one deriving from another. Record types came with C# 9. I am using them here only for brevity. Consider these two types as just the base and the derived class.

``` cs
record Person(string FirstName, string LastName);

record Celebrity(string FirstName, string LastName, string KnownFor)
    : Person(FirstName, LastName);
```

We can either instantiate a record and assign the instance to a reference, or assign a reference to null.

This is where the definite assignment analysis comes to the table. If there is a sequence of instructions in which the reference ends up being null, we must use the question mark to indicate that the reference can be null.

``` cs
Person? left = null;
Person? bob = new Person("Bob", "Coder");
Person fowler = new Celebrity("Martin", "Fowler", "famous books");
Person martin = new Celebrity("Bob", "Martin", "SOLID principles");
```

You can see that the second reference (`bob`) is assigned to a proper object but is still declared nullable. That is perfectly fine in scenarios where an object is coming from the outside, and you might not know whether it will be there or not.

Make sure you don't assign a nullable reference to a non-nullable one, though. That would cause a compile-time warning, which you can raise to the level of compile-time error if you prefer.

It is essential to understand that nullability is not the property of the type but rather a hint given to the compiler. Nullable reference types are only used during the compile-time analysis and are never stored in the compiled type itself.

One consequence is that you cannot declare a nullable type parameter in a generic type. That wouldn't make sense because the compiler has no place to put that information in the compiled type! 

But then comes a twist because we are free to indicate any reference of the generic parameter type as nullable, as in the code below. Such a reference is subject to definitive assignment analysis as any other.

``` cs
void Showcase<T>(string caption, Action<T?> action, params T?[] objects)
{
    Console.WriteLine($"Showcasing {caption}:".ToUpper());
    foreach (T obj in objects) action(obj);
    Console.WriteLine();
}
```

We have defined the utility function to showcase all situations incorporating null references in the rest of this article. As I already pointed out, it would be a compile-time error to declare this generic function as `Showcase<T?>`, while accepting a nullable `T?` in the argument list would be perfectly valid. Makes your head spin around!

An even greater mystery is to come: why not remove nullable from the argument list? What would that mean?

``` cs
void Showcase<T>(string caption, Action<T> action, params T[] objects)
{
    Console.WriteLine($"Showcasing {caption}:".ToUpper());
    foreach (T obj in objects) action(obj);
    Console.WriteLine();
}
```

That would leave it to the caller to determine nullability because – now pay attention! – a concrete generic parameter type *can* be nullable. It determines the nullability of references, which is a real thing during compilation.

I hope you have started to grasp these concepts more now. Unfortunately, it would take a lot of space to explain this concept in-depth, but I would certainly advise you to learn more about nullability of types. It is now part of C# and is here to stay.

Let me give you a quick demo showcasing the two possible choices:

``` cs
Showcase<Person?>("Nullable reference types", Console.WriteLine,
                  left, bob, fowler, martin);
Showcase<Person>("Non-nullable reference types", Console.WriteLine,
                  fowler, martin);
```

The first call above allows null references in the arguments, while the second call forces non-nullable references. So the compiler would check the references passed as arguments in that case and raise a warning if any of them is, or could be, null.

That concludes our crash course on nullable reference types in C#. We are ready to proceed with more advanced matters. 

Before that, here is the output produced by the code as we have it so far:

``` text
SHOWCASING NULLABLE REFERENCE TYPES:
                                                    <-- null is here!
Person { FirstName = Bob, LastName = Coder }
Celebrity { FirstName = Martin, LastName = Fowler, KnownFor = famous books }
Celebrity { FirstName = Bob, LastName = Martin, KnownFor = SOLID principles }

SHOWCASING NON-NULLABLE REFERENCE TYPES:
Celebrity { FirstName = Martin, LastName = Fowler, KnownFor = famous books }
Celebrity { FirstName = Bob, LastName = Martin, KnownFor = SOLID principles }

```

Pay attention to the empty line in the output. That is where we have passed null to the `Console.WriteLine`. The `WriteLine` method accepts null and treats it the same way it treats an empty string.

## How to Use the `is null` and `is not null` Patterns

Once we get nullability right, we can start doing logic around it. The simplest of all operations is asking if a reference is equal to null.

``` cs
void IsNull(Person? person)
{
    if (person is null)
        Console.WriteLine("Sad to see you leaving.");

    if (person is not null)
        Console.WriteLine($"Everybody say hello to {person}"!);
}

Showcase("is null and is not null patterns", IsNull,
         left, bob, fowler, martin);
```

The `is` operator is testing an object against a pattern. We'll meet this operator several more times in the upcoming sections. 

In this demo, you can see its simplest use: testing against the `null` pattern. There are two possibilities there, `is null` and `is not null`, with the meaning that appears to require no further explanation. Oh, but that would be a big mistake!

A corner case is covered by `is null` and `is not null` patterns, which might be the core reason for introducing these patterns in the first place. Both patterns will avoid calling any overload of the `==` and `!=` operators.

So, in theory, a class could overload the `==` and `!=` operators and, in doing so, declare that a particular object should be considered equal to a null reference. But the `is null` pattern will not call the operator overload – thus, it will flatly reject comparing that same non-null object to null.

That is a minor corner case, but it teaches how C# operates under the hood. The bottom line is: you should favor `is null` over `==`, and `is not null` over `!=` when testing for null/non-null.

Here is the printout produced when we run the function above on a few references, one of them being null.

``` text
SHOWCASING IS NULL AND IS NOT NULL PATTERNS:
Sad to see you leaving.
Everybody say hello to Person { FirstName = Bob, LastName = Coder }
Everybody say hello to Celebrity { FirstName = Martin, LastName = Fowler, KnownFor = famous books }
Everybody say hello to Celebrity { FirstName = Bob, LastName = Martin, KnownFor = SOLID principles }
```

## How to Use `Type-Test-and-Set` Patterns

The time has come to raise the bar and use some of the more complex methods of processing nullable references. We will remain with the `is` operator, but this time, we'll use its more potent form: testing type patterns.

Each reference in C# resolves into an object (or a lack of – a null), and each object we reference possesses the type descriptor. That is at the core of any object-oriented language. 

So it's pretty easy for the .NET runtime to check whether a reference is pointing to an object – and, if so, whether that object's runtime type derives from a specific type, directly or indirectly.

That was a mouthful, wasn't it? Let's split that up into bits:

  - To test whether a reference references an actual object, that is the `person is not null` pattern.
  - To add the test whether that object is assignable to a particular type, we use the type pattern instead: `person is Celebrity`.
  - Finally, to capture the reference to the desired type and use it in subsequent statements and expressions, we use the full-blown type-test-and-set expression: `person is Celebrity celeb`.

These are the three stages of extracting information from a reference, each more potent than the other. 

Without further ado, here is the method that exercises the most detailed form: testing against null and downcasting, all packed in one condensed expression:

``` cs
void TypeTestAndSet(Person? person)
{
    string report = person switch
    {
        Celebrity celebrity =>
            $"{celebrity.FirstName} {celebrity.LastName} known for {celebrity.KnownFor}",
        Person commonPerson =>
            $"{commonPerson.FirstName} {commonPerson.LastName}",
        _ => string.Empty,
    };
    if (!string.IsNullOrEmpty(report)) Console.WriteLine(report);

    if (person is Celebrity celeb) Console.WriteLine("*** Did you see a celebrity?");
}

Showcase("Type test and set patterns", TypeTestAndSet,
         left, bob, fowler, martin);
```

You may have noticed that these expressions are effectively implementing safe downcasting. Downcasting was frowned upon for decades, accused (mostly rightfully) of causing code defects and design flaws. 

But times they are a-changin'! Type test and set expressions are coming to software development from functional programming. 

This article is not a place to discuss the differences between type testing and downcasting as we knew it in object-oriented languages of the past. I strongly encourage you to learn more about this intriguing topic before judging.

``` text
SHOWCASING TYPE TEST AND SET PATTERNS:
Bob Coder
Martin Fowler known for famous books
*** Did you see a celebrity?
Bob Martin known for SOLID principles
*** Did you see a celebrity?
```

Here, you can see the output produced by the function above. As you can see, each actual type is captured correctly, creating its specific output. And the dreaded null was left out – I have indeed passed a null reference to the function at one instant but hadn't matched any of the patterns, and so was ignored.

This demo would be incomplete without one crucial note. The `switch` expression (of C# 8) is expecting patterns in order from more specific to more general ones. It would be an error to list a more specific pattern after a more general one. The general pattern would overshadow the subsequent one, never letting its right hand execute. Therefore, the `switch` expression like the one below causes a compile-time error in C#.

``` cs
person switch
{
    Person commonPerson =>
        $"{commonPerson.FirstName} {commonPerson.LastName}",
    Celebrity celebrity =>              // <-- error
        $"{celebrity.FirstName} {celebrity.LastName} known for {celebrity.KnownFor}",
    _ => string.Empty,
};
```

## How to Use `Property` Patterns

An exciting development follows if you push pattern matching even further. One specific form is the properties pattern – one aimed to match the values and attributes of properties of an object (if the object exists!).


``` cs
void PropertyPatterns(Person? person)
{
    if (person is { FirstName: "Bob"})
        Console.WriteLine($"Greet Bob, the one and only {person.FirstName} {person.LastName}!");
    else
        Console.WriteLine("Not a Bob");
}

Showcase("Property patterns", PropertyPatterns,
         left, bob, fowler, martin);
```

You don't have to specify the type if you are not interested in downcasting. It will be the type of the reference to the left of the `is` operator. 

But using the `is` operator implies a null test. Any reference passing the `is` test will be non-null and safe to check its property values on the right-hand side of the expression.

Therefore, we read this `if` instruction's condition as follows: If `person` is not null, and its property `FirstName` has a value Bob, then...

Here is the output produced when we call the function above:

``` text
SHOWCASING PROPERTY PATTERNS:
Not a Bob
Greet Bob, the one and only Bob Coder!
Not a Bob
Greet Bob, the one and only Bob Martin!
```

## How to Use the Null Propagation and Null Coalescing Operators

So far, we have been doing things to objects, which is awkward in an object-oriented design. Remember, in object-oriented programming, it is the object that exposes behavior, and, as the object's users, we only make calls to its methods.

The problems still come when the reference we expect to point to an object is nullable. Making an unguarded call on the null reference was the primary source of defects. But now, with nullable references and definite assignment checks done for us, we should be safe from the dreaded `NullReferenceExceptions`.

Consider having a method exposed by the class. We can use `ToString` as a simple example.

``` cs
record Person(string FirstName, string LastName)
{
    public override string ToString() =>
        $"{FirstName} {LastName}";
}

record Celebrity(string FirstName, string LastName, string KnownFor)
    : Person(FirstName, LastName)
{
    public override string ToString() =>
        $"{base.ToString()} known for {KnownFor}";
}
```

There is a substantial difference between calling `ToString` on `Person` and on `Person?` types. The latter one is nullable, and therefore an unguarded call might cause dereferencing a null reference, leading to a dreaded `NullReferenceException`, as you can imagine.

``` cs
Person a = ...;
Person? b = ...;

string x = a.ToString();      // safe
string y = b.ToString();      // unsafe
```

Enter the null-propagation operator (`?.`)! We can safely make an optional call to a method, provided the reference is non-null.

``` cs
Person a = ...;
Person? b = ...;

string x = a.ToString();      // safe
string? y = b?.ToString();    // safe
```

But observe the consequences. If the method returns `void`, the call will be ignored on a null reference. If the method returns a type, then the result will be the nullable version of that type. You cannot expect a string from `ToString` on a nullable reference, you see? The compiler can only promise a nullable string instead.

And what if we really wanted a string, a true one? Enter the null-coalescing operator (`??`)! We can easily convert a nullable reference to a non-nullable one by supplying a default to take when the actual value is null at run time.

``` cs
void NullPropagationAndCoalescing(Person? person)
{
    string report = person?.ToString() ?? string.Empty;
    if (!string.IsNullOrEmpty(report)) Console.WriteLine(report);
}

Showcase("Null propagation and null coalescing operators",
         NullPropagationAndCoalescing,
         left, bob, fowler, martin);
```

In this example, we make an optional call to the `ToString` method first but then short-circuit the result to an empty string if the reference were null. The result is that any null reference would produce an empty string for printout.

``` text
SHOWCASING NULL PROPAGATION AND NULL COALESCING OPERATORS:
                            <-- An empty string printed here
Bob Coder
Martin Fowler known for famous books
Bob Martin known for SOLID principles
```

## How to Work With Optional Objects

The last method of addressing nulls in this article will actually not use nulls. Another riddle! The idea is to avoid nulls altogether by modeling the objects as possibly missing. Mind the word "possibly" – that will become part of the type declaration the same way nullability was.

If you are new to optional objects, then this short explanation will be anything but sufficient to learn about them. C# has no native support for optional objects. You can choose one of the many implementations available on NuGet, the most popular one being the LanguageExt library.

``` text
dotnet add package LanguageExt.Core
```

An optional object of some type is an object that either exists or does not exist. Whichever the case, the optional object itself will always exist. Another riddle for you to solve! 

Here is how we would declare a few optional objects:

``` cs
using LanguageExt;

Option<Person>[] maybePeople = 
{
    Option<Person>.None,
    Option<Person>.Some(bob),
    Option<Person>.Some(fowler),
    Option<Person>.Some(martin),
};
```

The two shapes of an optional object are usually referred to as `None` and `Some`. The `Some` variant must contain an actual object. That completes the creation of optional objects and the code that will never have a null reference.

But what is the difference compared to nullable references? Why should we use optional objects at all?

The short story is that optional objects let us apply functions to the optional object's content – if present. The optional object will either invoke the function and pass the content to it or skip calling it altogether if there is no content.

Therefore, an optional type is a single place where that calling protocol is now implemented, the protocol in many ways equivalent to safely dereferencing nullable references.

``` cs
void Optional(Option<Person> maybePerson)
{
    string report = maybePerson.Match(
        person => person.ToString(),
        string.Empty);
    maybePerson.Do(Console.WriteLine);
}

Showcase("Optional objects", Optional, maybePeople);
```

The `Match` method covers both possibilities: It either maps the `Person` object to a string or substitutes an empty string if the person is missing. The `Do` method will only pass content to the console if content exists.

Here is the printout produced by the `Do` method:

``` text
SHOWCASING OPTIONAL OBJECTS:
Bob Coder
Martin Fowler known for famous books
Bob Martin known for SOLID principles
```

You will only see the `Some` variants printed out. The only missing object in the input array has produced no output because that optional instance has ignored the action passed to its `Do` method.

The most significant benefit of using optional objects over nullable references is their ability to apply other functions. We might already have many different classes and methods implemented in our codebase, all methods working on non-nullable references. Optional objects can bridge the gap between potentially missing objects and the common methods that are only operational when nothing is missing.

## Final Notes

In this tutorial, we started by declaring nullable objects and testing their existence using the `is` operator.

Then, we extended the example by displaying the richness of pattern-matching expressions: type test and set and property pattern expressions.

We then moved the focus from consuming objects to calling their behavior from the null-propagation operator over the null-coalescing operator, landing in the vast field of functional programming and optional objects.

I hope you enjoyed the ride. In place of farewell, I will invite you to learn more about optional objects in C# by watching my recent video [How to Avoid Null Reference Exceptions: Optional Objects in C#](https://youtu.be/8-2xr_kBRnQ).[


