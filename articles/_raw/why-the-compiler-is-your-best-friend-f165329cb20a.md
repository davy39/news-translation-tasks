---
title: Why the compiler is your best friend
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T18:18:14.000Z'
originalURL: https://freecodecamp.org/news/why-the-compiler-is-your-best-friend-f165329cb20a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C9CScad4P6wtLj8H_3AhqA.jpeg
tags:
- name: Game Development
  slug: game-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Richard Taylor

  Between projects I spent time researching the root causes of high-cost bugs in large
  game teams. The findings lead us to question basic C++ language features and patterns.
  This post covers obfuscation issues from a technical leaders...'
---

By Richard Taylor

Between projects I spent time researching the root causes of high-cost bugs in large game teams. The findings lead us to question basic C++ language features and patterns. This post covers obfuscation issues from a technical leadership POV. The background research to these ideas is covered in [“How to write fewer bugs”](https://medium.freecodecamp.org/how-to-write-fewer-bugs-tips-for-game-developers-82e3d742f6f7).

### Coding Tenets

What do your team’s Coding Standards look like? Maybe they are based on a common or open standard? Maybe they define camelCase variable names for readability? Maybe they define source code doxy-mentation formatting for maintenance? Maybe none of this matters? Do they actually help? Do you have fewer bugs or less misunderstanding? Your coding standards might tick all of your OCD coding boxes but do they actually help the team function in a demonstrably better way?

When I wrote the coding standard for Onrush we had a clean sheet. No prior code to worry about. The standard did not include anything about where our brackets should be. Nothing about camelCase or underscore naming conventions. Nothing about documentation formatting. In fact, we didn’t even call it a coding standard. We sat down and we discuss what we really cared about in our code. We wanted higher quality. For us and our games, this meant more time on iteration, less time on rectification. Higher performance and lower bug count.

> We wrote our **Coding Tenets**. _The coding principals we care most deeply about._

The Coding Tenets contained statements like: Compile times and link times are a function of code quality. Write assertive code and not defensive code. Overloading is obfuscation. Name functions and classes so that high-level code reads like pseudocode. Given readable code documentation is largely useless. Document concepts, ideas and reasoning, do not document the code. The compiler is a tool for validating assumptions.

We allowed people to have their own coding style as long as it didn’t contradict any of the Coding Tenets. This resulted in a code base that was highly uniform in functional approach and flexible in styling. This flexible styling didn’t matter. It didn’t affect readability or understanding because the core tenets underpinned everything.

If you haven’t tried, stop writing Physics::Simulation.Update(dt) and start writing updateThePhysicsSimulationForThisTimeStep(dt). When I started writing descriptive function names I started thinking about the data and the transformations being applied. The former is obtusely object oriented. The latter is choosing a function name which describes operations and data names which describe information. Aim for high-level code which clearly describes the functional operations. That clearly shows the data dependencies. Aim for high-level code which does not need documentation.

### The compiler is a tool for verifying assumptions

_When coding C++ the compiler is my best friend. She scrutinises every line of code. She encodes my thoughts into executable code. She shows me my assumptions and misunderstandings. She lays out my human shortcomings. But, the compiler is not a mind reader. She does not possess psychic powers. Only unwavering diligence to produce correct code._

The compiler applies the strict rules of the C++ language to verify the correctness of my code. Although in this respect the C++ language is not exact. C++ has many ways to be inexact. Many ways to ask the compiler to make assumptions. If I have learnt one thing over the years it is this: making assumptions will always get you into trouble.

As C++ continues to grow and bloat to the size of a dwarf star, it easy to overlook the fundamentals. Are these basic programming concepts working for or against your team? The examples and comments below are specifically about C++ but apply to many modern languages.

### The <true> cost of Polymorphism

So let’s start at the beginning with polymorphism. Introduced in 1983 when ‘C with classes’ was renamed to C++. Polymorphism allows many function or methods to have the same name. The compiler will select the correct function using the types of the parameters. There is however a fundamental issue here. When is it ever good to have different things with the same name?

Consider this typical C++ 101 example where we have variants of a FileWrite function or method.

```h
// Simple polymorphic file write functions for int, short and char 

bool FileWrite(int i);
bool FileWrite(short f);
bool FileWrite(char c);
```

This seems convenient. I just call FileWrite with any type and the compiler will sort it out. The compiler has perfect knowledge of the code and will pick the functions needed to compile without errors. The process is deterministic and foolproof.

Unfortunately not. The compiler may have perfect knowledge of the code, but the compiler has zero knowledge of intent. I am telling the compiler to assume the code I type correctly implements my intent. Now I know for a fact that I am not always correct, 20 years of programming has taught me this. With this convenience, I have lost an important opportunity for the compiler to find errors in my code and this will eventually lead to a difficult to find runtime error.

As a Technical Director or Technical Lead, my primary concern is getting the programming team to work efficiently together. The larger the team the harder a problem this becomes. Here is a typical development situation using the simple code above.

```h
// Simple example structure with three int members.

struct Brain 
{
 int humor;
 int intelligence;
 int empathy;
}
```

ai_brain.cpp:

```h

// Example usecase using polymorphic file functions 

void SaveGame(Brain& brain) 
{
  FileWrite(brain.humor);
  FileWrite(brain.intelligence);
  FileWrite(brain.empathy);
}

void LoadGame(Brain& brain) 
{
  FileRead(brain.humor);
  FileRead(brain.intelligence);
  FileRead(brain.empathy);
}
```



Ok still C++ 101. In the programming team, Tom is working on the AI and Jerry is working on the Save Game. Everyone on the team is busy working for the next milestone build. Suddenly the game is crashing during the Loading Phase and the team a blocked. The milestone is looming and everyone looks at Jerry to fix the crash.

The problem is Jerry has not submitted code today. Jerry starts to investigate the problem. Source control shows that no changes have been made to the Save Game module files today. The debugger shows the crash in the Pickup code. Another search of the SCM shows no changes in the Pickup module today. The input file stream for the saved game data appears to be corrupt. Jerry sighs and takes a sip of coffee and continues to investigate.

After some time the Jerry finds the change which caused the problems in the AI code and goes to talk to Tom.

```h
// Breaking changes causing **action at a distance**

struct Brain 
{
<< old
  int humor;
  int intelligence;
  int empathy;
>>> new
  short humor;
  short intelligence;
  short empathy;
=====
}
```

Jerry explains to Tom that the change above caused the game to crash creating pickups! The change in the size of the members caused the input stream to become misaligned. The first code to fatal error due to bad data was the Pickup module.

It turnouts out that Tom did get a once only crash in the Loading phase. Tom deleted the save game and the errors when away. As Tom was not working anywhere near the loading code he assumed it was a pre-existing error and continued to work. Tom fully tested his code before submitting and all test passed.

### **How could this situation have been avoided?**

> Polymorphism enables “Action At A Distance” in code.

In the simple example above the compiler started generating different executable code in the LoadGame and SaveGame functions. The code in the LoadGame and SaveGame functions has not changed. None of the code in the Save Game module has changed. The code change in the AI module caused the code in the LoadGame function to mean something different. Then the compiler silently compiled the new LoadGame and SaveGame code without error. The code is technically correct but no longer satisfies the original intent.

**Consider this alternative.**

```h
// Strong naming and type safe file write functions

bool FileWriteInt(int i);
bool FileWriteShort(float s);
bool FileWriteChar(char c);
```

```h
// Example usecase using strong name and typesafe functions

void SaveGame(Brain& brain) 
{
  FileWriteInt(brain.humor);
  FileWriteInt(brain.intelligence);
  FileWriteInt(brain.empathy);
}
```

In this example, the data to be written is explicitly defined by the code. There are no assumptions to be filled in by the compiler. If the types passed to the function are incorrect the compiler will generate an error.

> We have changed an intermittent data dependent runtime error into a 100% repeatable compile time error.

Now let’s re-evaluating our scenario with the new code. Tom makes his changes to ai/brain.h and the code fails to compile. It is immediately obvious to Tom that his changes have caused the error. Tom is able to fix the code before submitting the changes. The compiler now discovers the error at compilation, rather than QA or the team finding the bug later.

You may be asking why this is an issue? And this deserves an explication.

### Scale

As a single developer in my own project, I have a thorough and in-depth understanding of my code. I can test and iterate with low cost. This simple example of polymorphism shows convenience with very low cost of errors.

My career as a game developer has been in large teams. When I was at university my lecturers taught OOP, Polymorphism and other clever programming tricks.

When I was a junior programmer I would write an overloaded method like above. The tricks are useful to me and I am going to use them in my code. As a senior programmer, I became responsible for bugs in my code. I am more aware of the time cost of maintaining code.

As a Technical Lead, I am responsible for bugs in other people’s code. I am involved in planning other people’s work and time estimates to make my team the best. As a Technical Director, I am responsible for the efficiency of the whole programming team. I want the team producing features NOT fixing bugs.

In a large game development team of 25, 50, 100 or more programmers, knowledge of the entire code base will vary. I know my code in detail. I know the rest of the code with varying certainty or rather, uncertainty. In a large programming team, I must write code making assumptions to the best of my knowledge. In a larger project, I **will** make more mistakes than in my own solo project and the cost of these mistakes will be higher.

In the example with Tom and Jerry, Jerry’s choice of polymorphic overloading made it really easy for Tom to introduce a bug. This bug prevented over half the development team from working for nearly 4 hours. In a team of 100 developers this is approximately 200 hours of lost work. That is equivalent to one person working full time for 5 weeks! The convenience of polymorphism to save a small amount of developer effort is completely disproportionate to the impact of the _action at a distance_ bugs that can be introduced.

To be clear the fault lies with Jerry for making an interface which has a high probability of being used incorrectly. When Tom submitted his changes all tests passed. Tom has done a reasonable amount of testing and has other tasks to move on to. Tom fell into the hole, he did not dig the hole.

### Scopes and Namespace

Namespaces were introduced in “The Annotated C++ Reference Manual” — 1990 book. Although not widely implemented until around 1995.

Previously all named objects in a program where globally unique. This caused problems when sharing code between different projects. If names in the shared code clash with the host application then something would have to be renamed. In a large project this could have a significant time impact.

Namespaces which scope the application from external libraries are completely valid and a sensible development choice.

There is however a tendency for programmers to use excessive namespacing within a project codebase.

> Within a project namespaces enable both

> — multiple names for the same object.

> — multiple objects with the same name.

By project codebase I mean specifically the code typed for that project by the team. Not any 3rd party libraries or code from other distinct teams in the same company.

Multiple aliases for the same object makes the code harder to read. Multiple objects with the same name increase assumptions. We are again asking the compiler to assume intent and select the ‘correct’ function or variable. Again as team sizes grow the probability of assumptions leading to errors increases and in large teams there is likely a high cost of failure.

The pattern of excessive namespaces is easy to fall into. STL and popular libraries such as Boot are heavily namespaced. These projects are heavily namespaced because in reality they are collections of micro projects into a single library. In these cases namespaces are being used as designed to isolate code from different contributors where refactoring global names would be unnecessarily difficult to orchestrate.

However, this pattern is so pervasive that it is commonly copied by developers inside their own code. When writing new code ensuring unique names is easy, the compiler will immediately tell you there is a problem. Inside the team’s codebase, unique naming is good because it avoids assumptions. Using namespaces within the team’s own code creates avoidable assumptions. Which enables the compiler to choose the _correct_ class, function or variable but with the wrong intent/outcome.

> math::fast::fpow(2,10)

> math::emulation::fpow(2,10)

When using namespaces there are multiple ways to reference the function and there is the possibility of several functions with the same name.

> fpow(2,10)

When reading code, the programmer needs to make an assumption about which specific fpow() function the author intended to be called and which specific fpow() function the compiler will actually choose. There will be no compile-time error if the generated code does not match the intent. These errors will need to be discovered at runtime.

This increases cognitive load. I now need to mentally track the current namespaces which apply to any given block of code. This is a problem which does not scale well with large teams and large code bases.

> MathEmuFpow(2,10)

> MathFastFpow(2,10)

There is only one way to refer to each of these Fpow functions. No matter where I am in the code, these functions all always have the same unique name. This makes the code easier to read and understand by reducing cognitive load on the programmer. I know the intent of the author and I know the code the compiler will generate.

Namespaces have valid _use cases_ for containing external code which you will not need to modify and in many cases not be able to modify. As such I will always put my projects inside a containing namespace. This is a courtesy to other teams and programmers who might need use this code in the future. Within projects, namespaces enable poor naming and assumptions and should be used sparingly.

### Auto

The C++11 standard introduced auto along with a host of other convenience features. Unfortunately auto is _yet another compiler assumption_ feature that tells the compiler to assume the code I have written is correct. The compiler must now choose whatever types allow the code to compile. The problem with this is still, I make mistakes.

Auto takes the above issues of polymorphic functions and applies this to variables. For polymorphic functions, the compiler can only choose between functions with matching names. Using auto asks the compiler to select ANY type which will make the code compile!

> Auto allows you to write code without understanding the data types.

> Auto enables action at a distance for variables.

The most common reason I hear for using auto in C++ is to make the code simpler and easier to read. Long complex STL type names are often given as justification for using auto. It is common to typedef long STL type names into convenient shorthand names. Why not skip this step and use auto?

Making the code simpler is flawed as a supporting argument. Complexity always leads to more complexity. If another system is complicated and difficult to understand, this complexity is not removed by using auto. Using auto is masking the complexity by making shorthand assumptions. (The only way to tackle complexity leaking out of APIs is to refactor the API.)

If I **do not** know the type auto will resolve to, then I am not considering all the possible failure cases. If I **do** know the type auto will resolve to, then I should use that type instead. Using the specific type better encodes my intent. If the compiler gives me an error, then I have learnt that my assumptions about the types being used are incorrect. Using the specific type also protects the code from later refactoring and action at a distance.

The cost of using auto in a personal project is probably zero. The cost of using auto in a large development team is potentially large and disproportionate to any benefits.

### The Compiler is my Friend

The compiler is my friend and ally in asserting my assumptions during development. Bugs found by the compiler must by definition be fixed before submitting changes.

> By designing my code to generate compiler errors when used incorrectly, I am helping the other programmers on my team.

This fits how we programmers work. I type some code and then hit compile in a short and fast iteration loop. I might even be using an IDE which continuously compiles in the background while I type. If the compiler finds my error quickly after typing, the cost to fix is nearly zero.

Large game development teams scale up the impact of bugs. If a team of hundreds cannot work, dev hours are lost at a truly frightening pace. Large game development projects will usually have large QA teams to find bugs. This introduces significant time delays and costs to bug discovery, fix and verification once the bug has been submitted into the build.

As a Technical Director, I must put a cost on the shorthand convenience of polymorphic functions, namespace, auto and other basic language convenience functionality. Comparing that to the impact and cost of extra bugs from unchecked assumptions.

At university I was taught that the compiler is a tool for translating source code into executable machine code. For a long time in my programming career I focused on the tech and the optimisation. I thought I knew how to use the compiler to generate the best code, but I was missing the bigger picture.

Writing source code which uses the compiler to validate the author’s intent is every bit as important as generating optimal executable code.

> The compiler is actually a tool for translating intent into executable machine code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C9CScad4P6wtLj8H_3AhqA.jpeg)

