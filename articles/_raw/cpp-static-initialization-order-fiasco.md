---
title: What is the Static Initialization Order Fiasco in C++? [Solved]
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2023-12-06T23:11:52.000Z'
originalURL: https://freecodecamp.org/news/cpp-static-initialization-order-fiasco
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/StaticCover.jpg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "In this article, I'll be covering a subtle but egregious problem that can\
  \ occur in C++ programs. This problem is popularly called the 'Static Initialization\
  \ Order Fiasco'. \nI'll first go over what the problem is, then go onto some solutions\
  \ and explo..."
---

In this article, I'll be covering a subtle but egregious problem that can occur in C++ programs. This problem is popularly called the 'Static Initialization Order Fiasco'. 

I'll first go over what the problem is, then go onto some solutions and explore how they work. Let's get started. 

This is what we'll cover:

<ul>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#whatisthestaticinitializationorderfiascoinc">What is the 'Static Initialization Order Fiasco' in C++ ?</a></li>
     <li><a href="#solutionstothestaticdeinitializationorderproblem">Solutions to the static de-initialization order problem</a>
          <li><a href="#constructonfirstuseidiom">Construct on first use idiom</a></li>
    <li><a href="#niftycountersolution">Nifty Counter Solution</a></li>
    </li>
	<li><a href="#summary"> Summary</a></li>
</ul>

##Prerequisites

* A basic understanding of C++: For readers not familiar with C++, [Learn C++ Programming for Beginners – Free 31-Hour Course](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/) is a helpful resource
* In particular, an understanding of [storage classes](https://learn.microsoft.com/en-us/cpp/cpp/storage-classes-cpp?view=msvc-170) in C++ will be helpful.

##What is the 'Static Initialization Order Fiasco' in C++ ?

The C++ standard states: 

> _"The order in which static objects are initialized across different translation units is [undefined](https://en.cppreference.com/w/cpp/language/siof) or ambiguous_."

A translation unit is just a way of saying a file that is fed into the compiler. It's a C++ source file with all the code from the headers included in it. 

One thing to note though, for later in the article: static objects in the same translation unit are constructed in order of declaration and destructed in the reverse order.

So, how is this a problem?

It can be a problem in the following situation:

Let's say there are 2 static objects in 2 different files. `File1.cpp` has a static object of type class A – `aObj` . `File2.cpp` has a static object of type class B – `bObj`. The static object in `File1.cpp` is visible to `File2.cpp` since it declares `aObj` as `extern` in `File1.h`.

```cpp

// Static initialization order problem
// File1.h
class A {
....
  void doSomething() {
    ...
  } 
}
extern A aObj;

//File1.cpp


static A aObj;

// File2.cpp

class B {
B() {
 aObj.doSomething();// Not okay! aObj may not have been constructed
}
....
}

static B bObj;

```

In this program, it is possible that the object `aObj` in File1.cpp gets initialized before `bObj` in File2.cpp. That is all good since in that case, the constructor for `bObj` runs after `aObj` has been constructed. It is safe to call call methods on `aObj`.

But it is also possible that the object `bObj` in File2.cpp gets initialized before `aObj` in File1.cpp. In that case, _the constructor of_ `bObj` _calls_ `doSomething()` _on_ `aObj` _which has not been constructed!_ The memory has been allocated for `aObj`, but it hasn't been constructed. This could lead to unintended behavior / a corrupt program.

So this is what the static initialization order fiasco is all about. 

But we're not done: the other problem is the **static de-initialization order fiasco**! This is pretty much the same problem, just applied to the order of de-initialization of static objects. 

The C++ standard doesn't specify the order in which static objects get de-initialized as well. So it is possible that static object `aObj` gets destroyed before `bObj`. This is a problem if `bObj`'s destructor uses or references `aObj`. 

This is illustrated in the code snippet below – it is pretty much the same as the example above, just that its the de-initialization order which is dangerous this time:

```cpp
// Static de-initialization order problem
// File1.h
class A {
....
  void doSomething() {
    ...
  } 
}
extern A aObj;

//File1.cpp

static A aObj;

// File2.cpp

class B {
B() {}
~B() {
 aObj.doSomething(); // Not okay! aObj may have already been destructed!
}
....
}

static B bObj;

```

**Note:** These problems are only applicable to objects with _static_ storage scope. They won't occur if `bObj` was a variable with automatic storage scope. In that case, the C++ standard guarantees that `aObj` is constructed before `bObj` and destructed after it.

**Another note:** These problems also do not occur in C programs. Why is that so? Well in C, there's no concept of constructors and destructors. Static objects are completely defined during compile time.

## How to Solve the Static De-initialization Order Problem

Now that it is clear what the problem is, I will discuss some solutions. There are multiple ways of solving this problem – each with its tradeoffs. Let's take a look.

###Construct on first use idiom:

This idiom tries to make sure that there is always a fully constructed object whenever the static object in question is used. Following the examples in the previous section, we can do this by replacing all references to `aObj` by a function call `aObj()` which returns a reference to an object of type `A`. 

In code it looks like this:

```cpp
// Static initialization order problem
// File1.h
class A {
....
  void doSomething() {
    ...
  } 
};

A& aObj();

//File1.cpp

A& aObj() {
  static A *aObj = new A();
  return *aObj; 
}

// File2.cpp

class B {
 B() {
   /*
    * Okay since calling aObj() gaurantees that
    * static A *aObj = new A(); ran
    */
   aObj().doSomething();  
  }
  ....
};

static B bObj;

```

`bObj` can safely assume that calling aObj() returns a fully constructed `aObj` since this line:

```cpp
static A *aObj = new A();
```

would have run on the function call and will give it a fully constructed object. Also, since the program never calls delete on `aObj`, it is never destructed so it is also safe to use `aObj` in `bObj`'s destructor. 

But this does mean that the memory allocated for `aObj` always stays alive and valid throughout the lifetime of the program. And this may or may not be a problem (it does get reclaimed by the OS after the program exits, of course).

So, in which situation is this solution not great? In the case that `aObj`'s destructor does something desirable. For example: when `aObj` gets destructed – it writes to a log file / does something else that has some side effects.

Now you may ask, okay, why don't just I replace the static pointer in the `aObj()` function call with a static `aObj` object?

```cpp
A& aObj() {
  static A aObj;
  return aObj; 
}

```

That still ensures that `aObj` has been fully constructed by the time the function is called right? Right. But it does not save us from the static de-initialization order problem. It is still possible that `aObj`'s destructor runs before `bObj` 's destructor.

There is an interesting trick that solves both of these problems: The Nifty Counter Idiom.

###Nifty Counter Solution

Reference: this resource on the [Nifty counter idiom](https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms/Nifty_Counter#:~:text=The%20%22nifty%20counter%22%20or%20%22,the%20initialization%20of%20static%20objects.&text=The%20header%20file%20of%20the,called%20on%20the%20Stream%20object.) presents the idea behind this idiom. Let's examine it.

The idea is to ensure that:

1. The static object being used gets constructed before any other static object in the translation unit that it is being used in.
2. The static object being used gets destructed after any other static object in the translation unit that it is being used in.

```cpp
// File1.h
#pragma once

struct A {
  A();
  ~A();
};
extern A& aObj;

static struct AInitializer {
  AInitializer ();
  ~AInitializer ();
} aInitializer; // static initializer for every translation unit that aObj is used in

```

```cpp
// File1.cpp
#include "File1.h"

#include <new>         // Used for placement new
#include <type_traits> // Used for aligned_storage

static int niftyCounter; // this is zero initialized at load time

/*
 * Memory for the static object aObj - memory itself is valid throughout the
 * the lifetime of the program.
 */
static typename std::aligned_storage<sizeof (A), alignof (A)>::type
  aObjBuf; 

A& aObj = reinterpret_cast<A&> (aObj);

A::A ()
{
  // Construct A
}
A::~A ()
{
  /*
   * Destruct A: with possible side effects
   * like writing to a file.
   */
} 

AInitializer::AInitializer ()
{
  if (niftyCounter++ == 0) {
    new (&aObj) A (); // use placement new operator
  }
}

AInitializer::~AInitializer ()
{
  if (--niftyCounter == 0) {
    (&aObj)->~A(); // run the destructor
  }
}

```

Let's try to understand what this code does.

First, in the header file, `File1.h` has the definition of `class A` first. After that, is have the definition of a class called `AInitializer`. 

There is also a static object **defined** in the header file of type `AInitializer`. This makes sure that the constructor for `AInitializer` runs before the constructor for any other static object in the translation unit that `File1.h` is included in (of course you have to include File1.h before any other static object's definition in source files). 

Remember: _static objects in the same translation unit are constructed in order of declaration and destructed in the reverse order_.

So now that `AInitializer` is constructed before any other static objects in a translation unit, how can we use this to our advantage? `aObj` can be constructed in the constructor of `AInitializer`! Which is what is happening in the lines below:

```cpp
AInitializer::AInitializer ()
{
  if (nifty_counter++ == 0) {
    new (&aObj) A (); // use placement new
  }
}

```

Note that the [placement new](https://en.cppreference.com/w/cpp/language/new) operator is being used here instead of the `new` operator to construct `aObj`. Let's see what would happen if we used `new` instead. The code would look like this:

```cpp
A& aObj;
A *aObjp = nullptr;

AInitializer::AInitializer ()
{
  if (nifty_counter++ == 0) {
    aObjp = new A (); 
    aObj = *aObjp; // Not okay! Cannot re-assign a reference
  }
}

```

This doesn't work since a reference needs to be defined and declared at the same time. That is precisely why the placement `new` operator needs to be used.

```cpp
static typename std::aligned_storage<sizeof (A), alignof (A)>::type
  aObjBuf; 

A& aObj = reinterpret_cast<A&> (aObj)
```

This allocates memory to fit an object of type `A` and later assigns that to the reference. Now all that's left to be done is to actually _construct_ the object in `AInitializer`'s constructor – which is what is done with the placement new operator.

Another question that may arise in your mind: here, there is a static object `aObjBuf`. But isn't that subject to the same de-initialization order problem that we talked about in the second part of the Construct _on first use_ idiom? 

The answer is that the memory for `aObjBuf` stays alive and valid until the program is alive. Nothing happens in the construction of the memory. So it's valid to this.

This approach also makes sure that the static de-initialization order problem isn't hit, since the last `AInitializer` object destructed will call the destructor of `aObj`. That is guaranteed to run after any static objects in other translation units run, since within the particular translation unit, the static object `aInitializer` is declared before any other static object using `aObj`. This means it will get destructed in the reverse order – that is after the destructor for any other static objects have run.

There are some caveats here: this solution isn't the easiest to understand and implement. This is also not thread safe. You can find more information in the article on Nifty counters presented in the The C/C++ Users Journal, May, 1999 [here](http://www.petebecker.com/js/js199905.html).

##Summary

Using statically initialized objects in C++ is tricky and should be done with care. Fortunately, there are multiple solutions and ways to get around the problem. 

In this article, we covered some common solutions: the 'Construct on first use' idiom and the 'Nifty counter solution', along with their merits and challenges.

Hope you enjoyed this article!

