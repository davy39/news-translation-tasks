---
title: An Overview of Erlang with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-erlang-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d15740569d1a4ca35d2.jpg
tags:
- name: Erlang
  slug: erlang
- name: Functional Programming
  slug: functional-programming
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Erlang is a functional programming language developed by Ericsson for use
  in telecom applications. Because they felt that it’s unacceptable for a telecom
  system to have any significant downtime, Erlang was built to be (among other things):


  distribut...'
---

Erlang is a functional programming language developed by Ericsson for use in telecom applications. Because they felt that it’s unacceptable for a telecom system to have any significant downtime, Erlang was built to be (among other things):

* distributed and fault-tolerant _(a piece of failing software or hardware should not bring the system down)_
* concurrent _(it can spawn many processes, each executing a small and well-defined piece of work, and isolated from one another but able to communicate via messaging)_
* hot-swappable _(code can be swapped into the system while it’s running, leading to high availability and minimal system downtime)_

### **Syntax**

Erlang makes heavy use of **recursion**. Since data is immutable in Erlang, the use of `while` and `for` loops (where a variable needs to keep changing its value) is not allowed.

Here’s an example of recursion, showing how a function repeatedly strips the first letter from the front of a name and prints it, only stopping when the last letter has been encountered.

```erlang
-module(name).

-export([print_name/1]).

print_name([RemainingLetter | []]) ->
  io:format("~c~n", [RemainingLetter]);
print_name([FirstLetter | RestOfName]) ->
  io:format("~c~n", [FirstLetter]),
  print_name(RestOfName).
```

Output:

```text
> name:print_name("Mike").
M
i
k
e
ok
```

There is also a heavy emphasis on **pattern-matching**, which frequently eliminates the need for an `if` structure or `case` statement. In the following example, there are two matches for specific names, followed by a catch-all for any other names.

```erlang
-module(greeting).

-export([say_hello/1]).

say_hello("Mary") ->
  "Welcome back Mary!";
say_hello("Tom") ->
  "Howdy Tom.";
say_hello(Name) ->
  "Hello " ++ Name ++ ".".
```

Output:

```text
> greeting:say_hello("Mary").
"Welcome back Mary!"
> greeting:say_hello("Tom").
"Howdy Tom."
> greeting:say_hello("Beth").
"Hello Beth."
```

## **Erlang Term Storage**

Erlang Term Storage, normally abbreviated as ETS, is an in-memory database built into OTP. It’s accessible within Elixir, and is a powerful alternative to solutions like Redis when your application runs on a single node.

## **Quick Start**

To create an ETS table you first need to initialize a table `tableName = :ets.new(:table_otp_name, [])`, once you have initialized a table you can: insert data, lookup values, delete data, and more.

### **ETS Demo in IEX**

```elixir
iex(1)> myETSTable = :ets.new(:my_ets_table, [])
#Reference<0.1520230345.550371329.65846>
iex(2)> :ets.insert(myETSTable, {"favoriteWebSite", "freeCodeCamp"})
true
iex(3)> :ets.insert(myETSTable, {"favoriteProgrammingLanguage", "Elixir"})
true
iex(4)> :ets.i(myETSTable)
<1   > {<<"favoriteProgrammingLanguage">>,<<"Elixir">>}
<2   > {<<"favoriteWebSite">>,<<"freeCodeCamp">>}
EOT  (q)uit (p)Digits (k)ill /Regexp -->
```

## **Persistence**

ETS Tables are not persistent and are destroyed once the process which owns it terminates. If you would like to store data persistently a traditional database and/or file-based storage is recommended.

## **Use cases**

ETS Tables are commonly used for caching data in the application, for example account data fetched from a database may be stored in an ETS Table to reduce the amount of queries to the database. Another use case is for rate limiting use of features in a web application - ETS’s fast read and write speed make it great for this. ETS Tables are a powerful tool for developing highly concurrent web applications at the lowest possible hardware cost.

### **Try it out**

There are websites where you can try running Erlang commands without having to install anything locally, like these:

* [Give it a try! (a hands-on tutorial)](http://www.tryerlang.org/)
* [TutorialsPoint CodingGround](https://www.tutorialspoint.com/compile_erlang_online.php)

If you’d like to install it on your (or a virtual) machine, you can find installation files at [Erlang.org](https://www.erlang.org/downloads) or on [Erlang Solutions](https://www.erlang-solutions.com/resources/download.html).

#### **More Information:**

* [About Erlang](https://www.erlang.org/about)
* [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))

