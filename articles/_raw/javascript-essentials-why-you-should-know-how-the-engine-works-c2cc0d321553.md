---
title: 'JavaScript essentials: why you should know how the engine works'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-04T22:14:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-essentials-why-you-should-know-how-the-engine-works-c2cc0d321553
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SKOyguJ-AC0DmiQ8ZS0FwQ.jpeg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Rainer Hahnekamp

  This article is also available in Spanish.

  In this article, I want to explain what a software developer, who uses JavaScript
  to write applications, should know about engines so that the written code executes
  properly.

  You’ll see b...'
---

By Rainer Hahnekamp

This article is also available in [Spanish](https://www.campusmvp.es/recursos/post/fundamentos-de-javascript-por-que-deberias-saber-como-funciona-el-motor.aspx).

In this article, I want to explain what a software developer, who uses JavaScript to write applications, should know about engines so that the written code executes properly.

You’ll see below a one-liner function that returns the property lastName of the passed argument. Just by adding a single property to each object, we end up with a performance drop of more than 700%!

As I will explain in detail, JavaScript’s lack of static types drives this behaviour. Once seen as an advantage over other languages like C# or Java, it turns out to be more of a “Faustian bargain”.

### Braking at Full Speed

Usually, we don’t need to know the internals of an engine which runs our code. The browser vendors invest heavily in making the engines run code very fast.

Great!

Let the others do the heavy lifting. Why bother worrying about how the engines work?

In our code example below, we have five objects that store the first and last names of Star Wars characters. The function `getName` returns the value of lastname. We measure the total time this function takes to run 1 billion times:

```
(() => {   const han = {firstname: "Han", lastname: "Solo"};  const luke = {firstname: "Luke", lastname: "Skywalker"};  const leia = {firstname: "Leia", lastname: "Organa"};  const obi = {firstname: "Obi", lastname: "Wan"};  const yoda = {firstname: "", lastname: "Yoda"};  const people = [    han, luke, leia, obi,     yoda, luke, leia, obi   ];  const getName = (person) => person.lastname;
```

```
  console.time("engine");  for(var i = 0; i < 1000 * 1000 * 1000; i++) {     getName(people[i & 7]);   }  console.timeEnd("engine"); })();
```

On an Intel i7 4510U, the execution time is about 1.2 seconds. So far so good. We now add another property to each object and execute it again.

```
(() => {  const han = {    firstname: "Han", lastname: "Solo",     spacecraft: "Falcon"};  const luke = {    firstname: "Luke", lastname: "Skywalker",     job: "Jedi"};  const leia = {    firstname: "Leia", lastname: "Organa",     gender: "female"};  const obi = {    firstname: "Obi", lastname: "Wan",     retired: true};  const yoda = {lastname: "Yoda"};
```

```
  const people = [    han, luke, leia, obi,     yoda, luke, leia, obi];
```

```
  const getName = (person) => person.lastname;
```

```
  console.time("engine");  for(var i = 0; i < 1000 * 1000 * 1000; i++) {    getName(people[i & 7]);  }  console.timeEnd("engine");})();
```

Our execution time is now 8.5 seconds, which is about a factor of 7 slower than our first version. This feels like hitting the brakes at full speed. How could that happen?

Time to take a closer look at the engine.

### Combined Forces: Interpreter and Compiler

The engine is the part that reads and executes source code. Each major browser vendor has its own engine. Mozilla Firefox has Spidermonkey, Microsoft Edge has Chakra/ChakraCore and Apple Safari names its engine JavaScriptCore. Google Chrome uses V8, which is also the engine of Node.js.  
The release of V8 in 2008 marked a pivotal moment in the history of engines. V8 replaced the browser’s relatively slow interpretation of JavaScript.

The reason behind this massive improvement lies mainly in the combination of interpreter and compiler. Today, all four engines use this technique.  
The interpreter executes source code almost immediately. The compiler generates machine code which the user’s system executes directly.

As the compiler works on the machine code generation, it applies optimisations. Both compilation and optimisation result in faster code execution despite the extra time needed in the compile phase.

The main idea behind modern engines is to combine the best of both worlds:

* Fast application startup of the interpreter.
* Fast execution of the compiler.

![Image](https://cdn-media-1.freecodecamp.org/images/xcTig2PibioQS1T5oImy5exOvcn43uda9R42)
_A Modern Engine uses an Interpreter and a Compiler. Source: i[mgflip](https://imgflip.com/i/23g834" rel="noopener" target="_blank" title=")_

Achieving both goals starts off with the interpreter. In parallel, the engine flags frequently executed code parts as a “Hot Path” and passes them to the compiler along with contextual information gathered during execution. This process lets the compiler adapt and optimise the code for the current context.

We call the compiler’s behaviour “Just in Time” or simply JIT.  
When the engine runs well, you can imagine certain scenarios where JavaScript even outperforms C++. No wonder that most of the engine’s work goes into that “contextual optimisation”.

![Image](https://cdn-media-1.freecodecamp.org/images/bu47j9z9Dee3O3hHm51ijuARr3aUTtj4j4EH)
_Interplay between Interpreter and Compiler_

### Static Types during Runtime: Inline Caching

Inline Caching, or IC, is a major optimisation technique within JavaScript engines. The interpreter must perform a search before it can access an object’s property. That property can be part of an object’s prototype, have a getter method or even be accessible via a proxy. Searching for the property is quite expensive in terms of execution speed.

The engine assigns each object to a “type” that it generates during the runtime. V8 calls these “types”, which are not part of the ECMAScript standard, hidden classes or object shapes. For two objects to share the same object shape, both objects must have exactly the same properties in the same order. So an object`{firstname: "Han", lastname: "Solo"}` would be assigned to a different class than `{lastname: "Solo", firstname: "Han"}`.

With the help of the object shapes, the engine knows the memory location of each property. The engine hard-codes those locations into the function that accesses the property.

What Inline Caching does is eliminate lookup operations. No wonder this produces a huge performance improvement.

Coming back to our earlier example: All of the objects in the first run only had two properties, `firstname` and `lastname`, in the same order. Let’s say the internal name of this object shape is `p1`. When the compiler applies IC, it presumes that the function only get passed the object shape`p1` and returns the value of `lastname` immediately.

![Image](https://cdn-media-1.freecodecamp.org/images/o4aMw-H7fhu2dKraaGPkHqOiV0lMAJr7ks3j)
_Inline Caching in Action (Monomorphic)_

In the second run, however, we dealt with 5 different object shapes. Each object had an additional property and `yoda` was missing `firstname` entirely. What happens once we are dealing with multiple object shapes?

### Intervening Ducks or Multiple Types

Functional programming has the well-known concept of “duck typing” where good code quality calls for functions that can handle multiple types. In our case, as long as the passed object has a property lastname, everything is fine.

Inline Caching eliminates the expensive lookup for a property’s memory location. It works best when, at each property access, the object has the same object shape. This is called monomorphic IC.

If we have up to four different object shapes, we are in a polymorphic IC state. Like in monomorphic, the optimised machine code “knows” already all four locations. But it has to check to which one of the four possible object shapes the passed argument belongs. This results in a performance decrease.

Once we exceed the threshold of four, it gets dramatically worse. We are now in a so-called megamorphic IC. In this state, there is no local caching of the memory locations anymore. Instead, it has to be looked up from a global cache. This results in the extreme performance drop we have seen above.

### Polymorphic and Megamorphic in Action

Below we see a polymorphic Inline Cache with 2 different object shapes.

![Image](https://cdn-media-1.freecodecamp.org/images/lNpKqU5ShHJkat0PpKIahkpFAwPOHpCJRIiA)
_Polymorphic Inline Cache_

And the megamorphic IC from our code example with 5 different object shapes:

![Image](https://cdn-media-1.freecodecamp.org/images/cDEEsdQECGIz20LpuSYqgtUtjRCD1wD0hRPx)
_Megamorphic Inline Cache_

### JavaScript Class to the rescue

OK, so we had 5 object shapes and ran into a megamorphic IC. How can we fix this?

We have to make sure that the engine marks all 5 of our objects as the same object shape. That means the objects we create must contain all possible properties. We could use object literals, but I find JavaScript classes the better solution.

For properties that are not defined, we simply pass `null` or leave it out. The constructor makes sure that these fields are initialised with a value:

```
(() => {  class Person {    constructor({      firstname = '',      lastname = '',      spaceship = '',      job = '',      gender = '',      retired = false    } = {}) {      Object.assign(this, {        firstname,        lastname,        spaceship,        job,        gender,        retired      });    }  }
```

```
  const han = new Person({    firstname: 'Han',    lastname: 'Solo',    spaceship: 'Falcon'  });  const luke = new Person({    firstname: 'Luke',    lastname: 'Skywalker',    job: 'Jedi'  });  const leia = new Person({    firstname: 'Leia',    lastname: 'Organa',    gender: 'female'  });  const obi = new Person({    firstname: 'Obi',    lastname: 'Wan',    retired: true  });  const yoda = new Person({ lastname: 'Yoda' });  const people = [    han,    luke,    leia,    obi,    yoda,    luke,    leia,    obi  ];  const getName = person => person.lastname;  console.time('engine');  for (var i = 0; i < 1000 * 1000 * 1000; i++) {    getName(people[i & 7]);  }  console.timeEnd('engine');})();
```

When we execute this function again, we see that our execution time returns to 1.2 seconds. Job done!

### Summary

Modern JavaScript engines combine the benefits of interpreter and compiler: Fast application startup and fast code execution.

Inline Caching is a powerful optimisation technique. It works best when only a single object shape passes to the optimised function.

My drastic example showed the effects of Inline Caching’s different types and the performance penalties of megamorphic caches.

Using JavaScript classes is good practice. Static typed transpilers, like TypeScript, make monomorphic IC’s more likely.

#### Further Reading

* David Mark Clements: Performance Killers for TurboShift and Ignition: [https://github.com/davidmarkclements/v8-perf](https://github.com/davidmarkclements/v8-perf)
* Victor Felder: JavaScript Engines Hidden Classes  
[https://draft.li/blog/2016/12/22/javascript-engines-hidden-classes](https://draft.li/blog/2016/12/22/javascript-engines-hidden-classes)
* Jörg W. Mittag: Overview of JIT Compiler and Interpreter  
[https://softwareengineering.stackexchange.com/questions/246094/understanding-the-differences-traditional-interpreter-jit-compiler-jit-interp/269878#269878](https://softwareengineering.stackexchange.com/questions/246094/understanding-the-differences-traditional-interpreter-jit-compiler-jit-interp/269878#269878)
* Vyacheslav Egorov: What’s up with Monomorphism  
[http://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html](http://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html)
* WebComic explaining Google Chrome  
[https://www.google.com/googlebooks/chrome/big_00.html](https://www.google.com/googlebooks/chrome/big_00.html)
* Huiren Woo: Differences between V8 and ChakraCore  
[https://developers.redhat.com/blog/2016/05/31/javascript-engine-performance-comparison-v8-charkra-chakra-core-2/](https://developers.redhat.com/blog/2016/05/31/javascript-engine-performance-comparison-v8-charkra-chakra-core-2/)
* Seth Thompson: V8, Advanced JavaScript, & the Next Performance Frontier  
[https://www.youtube.com/watch?v=EdFDJANJJLs](https://www.youtube.com/watch?v=EdFDJANJJLs)
* Franziska Hinkelmann — Performance Profiling for V8  
[https://www.youtube.com/watch?v=j6LfSlg8Fig](https://www.youtube.com/watch?v=j6LfSlg8Fig)
* Benedikt Meurer: An Introduction to Speculative Optimization in V8  
[https://ponyfoo.com/articles/an-introduction-to-speculative-optimization-in-v8](https://ponyfoo.com/articles/an-introduction-to-speculative-optimization-in-v8)
* Mathias Bynens: JavaScript engine fundamentals: Shapes and Inline Caches  
[https://mathiasbynens.be/notes/shapes-ics](https://mathiasbynens.be/notes/shapes-ics)

