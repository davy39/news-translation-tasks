---
title: What is Primitive Obsession?
subtitle: ''
author: Daniel Asaboro
co_authors: []
series: null
date: '2024-07-23T22:03:40.000Z'
originalURL: https://freecodecamp.org/news/what-is-primitive-obsession
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-23-at-08.25.18.png
tags:
- name: clean code
  slug: clean-code
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'In a statically-typed language like Java, C#, Go, Typescript, or even Dart,
  how do you represent an email address? Okay, what about a password? A phone number?
  Zip code? Home address? Alright, what about a unique ID?

  If your answer to all or most of ...'
---

In a statically-typed language like Java, C#, Go, Typescript, or even Dart, how do you represent an email address? Okay, what about a password? A phone number? Zip code? Home address? Alright, what about a unique ID?

If your answer to all or most of these is a string, then you are suffering from what Software Development experts call "**Primitive Obsession**".

While primitives like `int`, `char`, `byte`, `short`, `long`, `float`, `double`, `boolean`, `strings`, and so on are the basic built-in building blocks of any programming language, Primitive Obsession is when your code relies too much on them to represent otherwise more complex concepts.

Experts say it's a code smell. This is because Primitive Obsession can lead to a range of problems including lack of validation, poor readability, code duplication, and difficulty in refactoring. This article will help you resolve this issue.

## What You'll Learn in this Article

This tutorial, while quite short, is designed to help you understand and address the issue of primitive obsession in your code. So when you are done reading, you should be able to:

1. Identify what's so bad about Primitive Obsession and associated drawbacks.
    
2. Design better software and implement data structures that enhance code correctness, maintainability, and future-proof your software against potential issues.
    
3. Improve Data Safety, and Security, and reduce the likelihood of runtime errors and unexpected behavior by using more robust data representations.
    

## Prerequisites: What You Need to Know

1. Familiarity with OOP principles like classes, objects, encapsulation, inheritance, and polymorphism will be beneficial when designing custom data structures.
    
2. Proficiency in statically-typed languages like Java, C#, Go, TypeScript, and Dart where variable types are declared at compile time.
    

It's fine if you're not familiar with these concepts – there are many resources available online and in textbooks to help you get started. But this tutorial assumes a basic grasp of these foundations and builds upon them to address the issue of primitive obsession.

## What's Bad about Primitive Obsession?

Primitive obsession is problematic for several reasons:

1. Weak type checking
    
2. Limited built-in functionality for specific data types
    
3. Reduced maintainability and loss of domain knowledge
    

Let's take a look at each issue in detail:

### 1\. Primitives offer weak type checking

Beyond efficient memory allocation, or wasteful compute time in deciphering what type a value is, one of the benefits of statically type language is that it lets the compiler help you catch potential type mismatches at compile time. This can help prevent runtime errors caused by using the wrong data type.

The compiler would scream at you if you did this:

```dart
String phoneNumber = "+1-555-229-1234";
int zipCode = 101257;

zipCode = phoneNumber; // throws an error
```

What if you did this?

```dart
String phoneNumber = "+1-555-229-1234";
String zipCode = "1000 AP"

zipCode = phoneNumber; //works fine
```

It will compile and do nothing!

Why?

**Because a string will always be a string.**

The compiler cannot differentiate whether the string value you pass represents a user password or an email address. Consequently, it cannot prevent you from mistakenly assigning a variable to the wrong field leading to runtime errors and unexpected behaviour.

### 2\. Limited built-in functionality for specific data types.

When you rely heavily on primitives, you often need to write additional code to perform tasks such as email address validation or phone number formatting. And that's not a problem really.

The real problem is the repetitive and scattered nature of these implementations. This doesn't just increase the risk of errors but it also makes the code harder to maintain and refactor.

### 3\. Reduced Maintainability and Loss of Domain Knowledge

Scattering business rules and logic across the codebase makes it harder to maintain and evolve the software. When primitives are used extensively, it can be challenging to understand the purpose and constraints of the data they represent.

Encapsulating this logic within dedicated types helps preserve domain knowledge and makes the code more intuitive for future developers.

For instance, you might need to block certain email addresses due to fraud or restrict specific zip codes, areas, or companies. When you use primitives, this important context is not evident, leading to potential errors and increased maintenance burden.

## How to Break Away from Primitive Obsession

### 1\. Watch out for variables with special validation logic.

Take Phone Numbers, for example. In Nigeria, where I'm from, all phone numbers are eleven digits long and start with a zero. The second digit is usually a "*7*" , "*8*", or "9" which helps identify the telecom operator. Any other number is invalid.

The same can be said for a Website URL. It could very well be represented by a string. But a URL has more information and specific properties compared to a string (for example, the scheme, query parameters, and protocol). And each part has a different validation method.

### 2\. Watch out for variables with special comparison rules

Beyond simple equality checks (==), if you find yourself implementing custom comparison logic for a variable without encapsulating it in a class, it's a red flag.

For instance, comparing email addresses often involves more than a simple equality check. You might need to perform case-insensitive matching, strip out whitespace, or handle variations in formatting to accurately identify matching emails such as + sign in email addresses for people who want to game your ssytem.

daniel@example.com is the same email address as daniel+dev@example.com. Emails sent to the latter will be received on the former.

### 3\. Watch out for variables with special formatting rules

Any variable that requires specific formatting or parsing to extract meaningful information is a candidate for a richer representation.

**Currency values** are a good example of this. Different regions use different formatting rules – some use commas and some use decimal points. It's the same case with a date of birth or anything that requires some data.

Identifying and resolving primitive obsession is a continuous process.

You won't be able to catch all instances at once, especially those that are uncommon and unique to your business domain. That's perfectly fine – that's how it should be.

Instead of panicking or giving up, gradually refactor your code to incorporate these changes. This approach is key to making your code future-proof and maintainable.

## You Don't See it Until You Are Shown

Primitive obsession hides in plain sight. And that's a significant issue because, unlike static errors, linters won't flag them and neither will your program crash as a result.

It often takes a mentor, a code review, or an "aha" moment to realize that these repetitive checks and rules scattered throughout your codebase can be centralized into their own dedicated types. This recognition is the first step toward more robust, readable, and maintainable code.

So stay open-minded, engage with others, read code from different sources, and contribute to open-source projects. That's how you learn. Ultimately, it's all about one thing: encapsulation – grouping data and the methods that operate on it in one location for maintainability.

## Credits and resources:

1. [A Code Smell that Hurts People the Most](https://medium.com/the-sixt-india-blog/primitive-obsession-code-smell-that-hurt-people-the-most-5cbdd70496e9) by Arpit Jain.
    
2. [Signs and Symptoms of Primitive Obsession](https://refactoring.guru/smells/primitive-obsession) by Refactoring Guru.
    
3. [How to Fix Primitive Obsession](https://hackernoon.com/what-is-primitive-obsession-and-how-can-we-fix-it-wh2f33ki) by Sam Walpole on Hackernoon.
