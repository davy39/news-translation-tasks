---
title: 'Keeping Time in C++: How to use the std::chrono API'
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2023-12-04T23:38:45.000Z'
originalURL: https://freecodecamp.org/news/cpp-std-chrono-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/ClangCover.jpg
tags:
- name: C++
  slug: c-2
- name: profiling
  slug: profiling
seo_title: null
seo_desc: "Keeping track of time is a very important aspect of computer programs.\
  \ Some common use cases are:\n\nMeasure/profile the performance of certain parts\
  \ of code.\nDo work at certain periods of time, from within a program. \nDetect\
  \ whether threads are in a d..."
---

Keeping track of time is a very important aspect of computer programs. Some common use cases are:

* Measure/profile the performance of certain parts of code.
* Do work at certain periods of time, from within a program. 
* Detect whether threads are in a deadlock / taking too long to complete an operation.
* Synchronize tasks between different components of software

and many more…

This article will guide you through how you can measure time in modern C++. 

### Prerequisites

* A basic understanding of C++: For readers not familiar with C++, [Learn C++ Programming for Beginners – Free 31-Hour Course](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/) is a helpful resource.
* A quick read through Linux time tracking infrastructure – [such as you can find here](https://man7.org/linux/man-pages/man2/gettimeofday.2.html) – will help you get familiar with the ideas presented in the article.

## Common Ways to Track Time in C++

This article covers how you can keep track of time in C++. In C, on UNIX like systems, you can use the [clock_gettime()](https://linux.die.net/man/3/clock_gettime) function to keep track of time. It returns time in a structured way through the [`timespec`](https://www.gnu.org/software/libc/manual/html_node/Time-Types.html) struct. 

The [`clock_gettime()`](https://linux.die.net/man/3/clock_gettime) /[gettimeofday](https://linux.die.net/man/2/gettimeofday) function gives us back a filled [`timespec`](https://www.gnu.org/software/libc/manual/html_node/Time-Types.html) struct which has two fields:

1. `tv_sec`, which gives us the time in seconds since the time source – CLOCK_REALTIME / CLOCK_MONOTONIC that was passed into clock_gettime. The 'type' of this field is [`time_t`](https://en.cppreference.com/w/c/chrono/time_t) which is usually an integral value.
2. `tv_nsec`, which gives the time after `tv_sec`, in nanoseconds since the time source that was specified while calling `clock_gettime()`. The type of this field is a long int.

So why is [`clock_gettime()`](https://linux.die.net/man/3/clock_gettime) not good enough? The answer is that the members of `struct timespec` can easily be passed to functions as they're really just `int`s / `float`s. They're not strongly typed. 

It's also easy to forget about the units in which they represent time while passing information around to functions. This can happen when you're dealing with projects that have thousands of lines of code.

So what's the solution?

##The std::chrono API

C++11 introduced the std::chrono API, which can help you avoid some of these problems.

There are 3 important parts of the API.

###1. `std::chrono::duration`

As its name suggests, `std::chrono::duration` is a type that represents a time interval. The official C++ reference mentions that `std::chrono::duration` is a templated type with the following signature:

```cpp
template<
    class Rep,
    class Period = std::ratio<1>
> class duration;
```

  
Here, the `Rep` template parameter represents the type that is used to count 'ticks' of time. A tick is just a unit of time which is a given fraction of a second. `Period`, the second parameter, defines what exactly that fraction is.

So, for example, if you write:

```cpp
using my_ms_type = std::chrono::duration<int, std::ratio<1, 1000>>

my_ms_type duration_ms duration = 3; // error: cannot convert from int
my_ms_type duration_ms duration_ok{3} // OK, can construct from int

```

`my_ms_type` is a type that has been defined, which counts in units of milliseconds (1/1000th of a second). This count is expressed as an integer. As you might be able to guess, the `Rep` template parameter is `int` and Period is `std::ratio<1,1000>` (which really is a way of saying 1/1000).

Now that it's clear how durations are represented, let's see what we can and cannot do with these.

If there is a function that takes in a `my_ms_type` duration and you instead try to pass in any non-`std::chrono::duration` type, you'll get a compiler error.

It is possible to implicitly convert between different types of `std::chrono::duration` as long as information isn't lost with the type of `Rep`, since the standard library can compute the relationship between two `std::chrono::duration`types. It is not possible to implicitly convert if there is a loss of information. For example:

```cpp
#include<chrono>

using namespace std::chrono;
using my_type_ms = std::chrono::duration<int, std::ratio<1, 1000>>;
using my_type_ms_f = std::chrono::duration<float, std::ratio<1, 1000>>;
using my_type_hundredth_s = std::chrono::duration<int, std::ratio<1, 100>>;
void f(my_type_ms millis) {}
int main()
{
   int duration = 2;
   my_type_ms_f duration_f{2.5};
   my_type_hundredth_s duration_compatible{100};

   f(duration); // error: could not convert 'duration' from 'int' to 'my_type_ms'

   f(duration_f) //error: since float -> int will lose information

   f(duration_compatible) // OK since no information is lost
}

```

The standard library also has some predefined `std::chrono::duration` template specializations for common time durations such as `std::chrono::duration::seconds`, `milliseconds`, `microseconds`, and so on.

You can also get the 'count' value contained in a duration by using the `count` method in a duration.

```cpp
std::chrono::seconds duration{3};
// Prints: 'Duration count: 3 seconds'
std::cout << "Duration count: " << duration.count() << " seconds";

```

Interestingly, converting from a unit with higher precision like `nanosecond` to something with a lower precision such as `millisecond` may also lead to a loss of information. For these specific cases, you need to use an _explicit cast_ for conversion. This is called `duration_cast`. For example:

```cpp
nanoseconds durationInNs = 3000000000;
seconds ms = duration_cast<seconds>(durationInNs); //OK 3s
durationInNs = 3500000000;
ms = duration_cast<nanoseconds>(durationInNs); // OK 3s - truncates down

```

Now that we know why `std::chrono::duration` is useful, let's move on. The next section explores `std::chrono::time_point`.

###2. `std::chrono::time_point`

`std::chrono::time_point` is a way of expressing a particular point in time – surprise, surprise! 

If you think about it, how can you logically define a point in time ? We need to have a reference starting point and a duration from the starting point. This is exactly what `std::chrono::time_point` does. 

The class declaration looks like this:

```cpp
template<
    class Clock,
    class Duration = typename Clock::duration
> class time_point;

```

There are two template parameters here:

The first one is `Clock` which represents a reference clock relative to which the point in time is being measured. For now, some examples of clocks are:

* `system_clock`: this represents a real-world wall clock. It's useful when you want to measure time in terms of real-world times. It's important to note that the system time can usually be changed on any system, so you shouldn't depend on this clock to calculate time periods between tasks / performance profiling.
* `steady_clock`: this represents a monotonically increasing clock. It's useful when you need stop-watch like clock accounting.

The second template parameter is `Duration` which is what we discussed in the previous section. A `time_point` needs to be associated with a `duration` type since that's what is being used to measure ticks since the 'epoch' of the `Clock`. 

Epoch is just a way of saying a reference point in time. While there's no mandate for which reference to use, Unix Time - that is, the time since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970 is a common one.

Time points based on the _same_ clock can be subtracted and not added. For example:

```cpp
auto tp1 = std::chrono::system_clock::now();
...
auto tp2 = std::chrono::system_clock::now()
auto tp3 = std::chrono::steady_clock::now();

auto diff = tp2 - tp1; // OK
auto add = tp1 + tp2; // Not Ok
auto add = tp3 - tp2; // Not Ok - based on different clocks

```

Let's now see what clocks are.

###3. Clock Types

A `Clock` is a type that ties together `std::chrono::duration` and `std::chrono::time_point`. It has a function `now()` that returns the current `time_point`. The formal requirements for a type to be a `Clock` can be found in the C++ spec [here](https://en.cppreference.com/w/cpp/named_req/Clock).

As mentioned before, `system_clock` and `steady_clock` are two popular clocks provided by the standard library. Each clock has its own associated `duration` as well.

Each `time_point` is associated with some clock, since it really has to be relative to some given reference.

Finally, let's see some examples of how you can tie together `duration`, `time_point`, and `Clock`. Let's say you want to measure the time that looping 100,000,000 times takes in nanoseconds, and you also want to print out the current wall time:

```cpp
#include <chrono>
#include <iostream>
#include <ratio>
#include <thread>
#include <ctime>

using namespace std::chrono;
constexpr size_t kIterations = 100000000;
void testFunction () {
    for (size_t i = 0; i < kIterations; i++) {
    }
}

int main()
{
    auto tStartSteady = std::chrono::steady_clock::now();
    std::time_t startWallTime = system_clock::to_time_t(system_clock::now());
    std::cout << "Time start = " << std::ctime(&startWallTime) << " \n";
    testFunction();
    auto tEndSteady = std::chrono::steady_clock::now();
    nanoseconds diff = tEndSteady - tStartSteady;
    std::time_t endWallTime = system_clock::to_time_t(system_clock::now());
    std::cout << "Time end = " << std::ctime(&endWallTime) << " \n";
    std::cout << "Time taken = " << diff.count() << " ns";
    return 0; 
}

```

The output of the program is the following:

```
Output:
// This can of course vary from system to system
Time start = Tue Nov  7 07:11:13 2023

Time end = Tue Nov  7 07:11:13 2023

Time taken = 50998885 ns

```

## Summary

This article explored various facets of the `std::chrono` API in C++. The `std::chrono` API allows C++ programmers to safely keep track of time thanks to its strongly typed system. It also helps maintain support for convenient conversions between different 'types' of time points.

  

