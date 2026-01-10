---
title: The easy way to get TypeScript interfaces from C#, Java, or Python code in
  any IDE
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-19T16:13:52.000Z'
originalURL: https://freecodecamp.org/news/the-easy-way-to-get-typescript-interfaces-from-c-java-or-python-code-in-any-ide-c3acac1e366a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wTwVD_QDNfAW4BgqrXhVBA.png
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Leonardo Carreiro

  Who has never experienced the situation where you have to fix a bug and at the end
  you find out that the error on the server was a missing field coming from a HTTP
  request? Or an error on the client, where your Javascript code wa...'
---

By Leonardo Carreiro

Who has never experienced the situation where you have to fix a bug and at the end you find out that the error on the server was a missing field coming from a HTTP request? Or an error on the client, where your Javascript code was trying to access a field that doesn’t exist on the data that came in an HTTP response from the server? A lot of times, these problems are caused just by a different name for this field between the code on the client and the server.

### The problem

Everyone who works both on the back-end and front-end of a web application has to query and process data on the server-side and then return these data to be consumed by the client-side of the application. No matter how many layers your architecture is divided into, you always will have the edge between the server and the client, where the HTTP requests and responses carry on the data between those two sides in both directions.

And this is not just about the bugs with different names — no one can remember the entire data structure of all the entities of the application. When you are writing code, it’s common to type a `.` (or `-&`gt; `or` [“). If you don’t write a wrong name there, you stop and ask yourself “What the heck was the name of that field?”. After you spend some time trying to remember, you give up and choose the most boring path. You take your mouse and start looking for the file where you define all those fields that you need to access.

> The boring part of writing code is when you cannot figure out by yourself what is the right code that you need to write.

Sometimes it doesn’t hurt to just google it and you find a Stack Overflow answer with the code there, ready to be copied. But when you have to search for this answer inside your project, a big project, where the code that defines the data structure that you have to access is in a file that wasn’t written by you…the time you spend on this path can be one or two orders of magnitude bigger than the time spent just writing the right name.

### TypeScript to the rescue

When we used to write just plain old Javascript, we didn’t have an option to avoid this boring path in these situations. But then, at the end of 2012, [Anders Hejlsberg](https://twitter.com/ahejlsberg) (the father of the C# language) and his team created TypeScript. Their mission was to make it easier to create large Javascript projects that scale.

The funny part is that, while this new language was a **superset** of Javascript, its objective was to allow you to do only a **subset** of things that you used to do with Javascript. It **added new features** like classes, enums, interfaces, parameter types, and return types.

But it also **removed possibilities**, even things that weren’t too bad, like passing a number as a parameter to `document.getElementById()`, and using the `*` operator with a number and a numeric string as operands. You cannot count with implicit type conversions anymore, you have to be explicit and use `.toString()` or `parseInt(str)` when you do want a type conversion. But the best thing that you can’t do anymore **is to access a field that doesn’t exist in an object.**

So, when a problem is resolved, a new one often takes its place. And here the new problem was the duplication of code. People started replacing the DRY principle (Don’t Repeat Yourself) by the WET principle (Write Everything Twice).

It is a good practice to use different classes in different layers, for different purposes, but it is not the case here. If you have three layers (A -> B -> C), you shouldn’t have specific data structure**s for each** layer (one for A, one for B and one for C), but rather for **each edge between those** layers (one between A and B and another between B and C). Here, unless your back-end is a Node.js application, we have to duplicate these data structure declarations because we are in the edge between two different programming languages.

To avoid writing everything twice, we are left with just one option…

### Code Generation

One day I was working on a .NET project with Entity Framework. It had a model diagram in a .edmx file, and if I changed this file, I had to select an option to generate the classes for POCO entities (Plain Old CLR Objects).

This code generation was done by T4, a template engine of Visual Studio that worked with a .tt file as a template for a C# class. It ran the code that reads the .edmx model file and outputs the classes in .cs files. After remembering that, I thought that it could be a solution to generate TypeScript interfaces and I started trying to make it work.

First, I tried to write my own template. When I worked with this and the Entity Framework, I never had to change the .tt template. Then I found out that Visual Studio didn’t support syntax highlighting in .tt files — it was like programming in notepad but worse.

Besides having C# code of the generation logic, I also had mixed with it the TypeScript code that had to be generated, like [this](https://gist.github.com/robfe/4583549). I installed a Visual Studio extension to get syntax support, but the extension defined syntax colors only for the light theme of Visual Studio, and I use the dark one. The light theme syntax colors on the dark theme was unreadable, so I had to change my Visual Studio theme too.

Now with syntax highlighting it was all good. It was time to start writing some code. I searched on google for a working example. My idea was to change it for my needs after I got it working, but… IT DIDN’T WORK!

```
System.IO.FileNotFoundException: Could not load file or assembly 'System.Runtime, Version=4.2.1.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a' or one of its dependencies. The system cannot find the file specified.
```

I tried a lot of “working” examples found searching on google, but none of them worked. I thought that maybe the problem was not with Visual Studio or with the T4 Engine — maybe the problem was me, using it wrong.

Then google got me on this [issue](https://github.com/dotnet/core/issues/2000) in the .NET Core repository and I found that it didn’t work with ASP.NET Core projects. But this error was a common error in the .NET world, so I figured I could try to make a workaround for it. I searched for that 4.2.1.0 version of the System.Runtime.dll, I found it, and I tried to put it in some different directories to see if Visual Studio could find it…but nothing worked.

Finally, I used Process Explorer to see which version of System.Runtime Visual Studio had loaded, and it was version 4.0.0.0. I tried to use a `bindingRedirect` to force it to use the same version (as I described [here](https://github.com/dotnet/core/issues/2000#issuecomment-456413662)), and it worked! I could not believe that I would not have to duplicate and manually sync my data structures between the server and client anymore.

I started to thing about it more, and another thought was bothering me…

### Was it worth it?

I work for a big oil company, with a lot of legacy applications. A friend had to work with a virtual machine because the app he was debugging sometimes only worked in Windows XP. Another app that I had to work on one day only worked with Visual Studio 2010. Another that used Code Contracts only worked with Visual Studio 2013 because the Code Contracts extension didn’t work in Visual Studio 2015 or 2017.

Since 2012 when I started working there until the beginning of 2019, I never had the chance to develop a new application. All my work always was with others developers’ messes. Last year I started to study more about software architecture, and I read the Uncle Bob’s “Clean Architecture” book.

Now that I started this new year with this opportunity, for the first time in this company I am creating a web application from scratch and I want to do a good job. I choose ASP.NET Core for my back-end, React for the front-end, and it will be one of the first apps in this company to run in a Docker container in our new Kubernetes cluster.

Another poor developer will have to work on this project in the future, with my code and all my mess, and I don’t want them to have to deal with bad code. I want all developers after me to want to work on this project. This will not happen if they have to lose a day of work just to get the generation of client code from back-end data structures working. They would then hate me (and some of them would already hate me for putting TypeScript code in a project when TypeScript was still in version 0.9).

> When we write code that isn’t ours, we have the responsibility to make it easy for other people to work on it.

After thought about that, I came to a conclusion:

> **We should avoid dependencies on anything that cannot be handled by the package manager of the technology of choice.**

In this case, besides dependencies on Visual Studio and Windows, I would make the project depend on a bug fix that would need to be fixed by Microsoft (and [it seems that it doesn’t have any priority](https://developercommunity.visualstudio.com/content/problem/358905/filenotfoundexception-systemruntime-version4210-wh.html)). So it’s best to duplicate this code and manually sync it than put a dependency on this T4 engine.

I choose to use .NET Core, but if some developer in the future wants to work on this project using Linux, I can’t stop them.

### The final solution (TL;DR)

Duplicate code is bad, but dependency on third party tools is worse. So, what can we do to avoid duplication of data structures and not depend on any specific IDE / plugin / extension / tool for development?

It took me some time to realize that the only tool that I needed was there all this time, inside the language runtime: **Reflection**.

I realized I could write some code that runs on the startup of my back-end ASP.NET Core app only in development mode. This code could use reflection to read the metadata about names and types of all the data structures that I wanted to generate TypeScript interfaces. I just needed to map C# primitives to TypeScript primitives, write the .d.ts TypeScript definitions in a specific folder, and I’d be done.

Every time I changed some data structure in the back-end, it would override the interfaces definitions inside a .d.ts files when I ran the code to test it. When I got to the part of writing the client code to use the data structure that changed, the interfaces would already be updated.

This approach can be used by projects in .NET, Java, Python, and any other language that has support for code reflection, without adding a dependency on any IDE / plugin / extension / tool.

I wrote a simple example using C# with ASP.NET Core and published it on GitHub [here](https://github.com/lmcarreiro/cs2ts-example). It just takes from all classes that inherit `Microsoft.AspNetCore.Mvc.ControllerBase` and all types from parameters and returns types of public methods that have `HttpGet` or `HttpPost` attributes.

Here is what the generated interfaces look like:

![Image](https://cdn-media-1.freecodecamp.org/images/-4fmTbfc18e-s41lvRdt0smq-f78Dma1Hrws)
_C# classes (left) vs TypeScript interfaces (right)_

#### You can generate other types of code too

I used it to generate interfaces and enums for data structures only, but think about the code below:

![Image](https://cdn-media-1.freecodecamp.org/images/87YihvvupEwjtjXBcRj6Gpr-2oCQVRHVbp7s)
_TypeScript code of an example API that could be generated automatically_

It’s much less of a pain to keep this code in sync with all the possible MVC controllers and actions than it was to keep the data structures in sync. But do I need to write this code by hand? Couldn’t it be generated too?

I can’t generate C# interfaces from C# concrete implementations, because I need the code to compile and run before I can use reflection to generate it. But with client code that needs to be kept in sync with server code, I can generate it. This way of code generation can be used beyond the data structure interfaces.

#### If you don’t like TypeScript…

It doesn’t need to be written with TypeScript. If you don’t like TypeScript and prefer to use plain Javascript, you can write your .js files and use TypeScript just as a tool (if you use Visual Studio Code you are already using it). That way, you can generate helper functions that convert your data structures to the same structures. It seems weird, but it would help the TypeScript Language Service to analyse your code and tell Visual Studio Code with fields that exist in each object, so it could help you to write your code.

![Image](https://cdn-media-1.freecodecamp.org/images/FBWck84VzHqiE5gidEkthJ9eO-K86D6iIOP2)
_Using typing information with plain Javascript_

### Conclusion

We, as developers, have a responsibility to other developers that will have to work on our code. Don’t leave a mess for them to clean up, because they won’t (or at least they won’t want to!). They will likely only make it worse for the next one.

You should avoid at all costs any development and runtime dependencies that cannot be handled by the package manager. Don’t make your project the one that others developers will hate working on.

Thanks for reading!

PS 1: This [repository with my code](https://github.com/lmcarreiro/cs2ts-example) is just an example. The code that converts C# classes into TypeScript interfaces there is not good. You can do a lot better, and maybe we already have some NuGet package that do this.

PS 2: I love TypeScript. If you love TypeScript too, you may want to take a look at these links, from before it was announced by Microsoft in 2012:

* [**What’s Microsoft’s father of C#’s next trick?** Microsoft Technical Fellow Anders Hejlsberg is working on something to do with JavaScript tools. Here are a few clues about his latest project.](https://www.zdnet.com/article/whats-microsofts-father-of-cs-next-trick/)
* [A HackerNews discussion: **“Anders Hejlsberg Is Right: You Cannot Maintain Large Programs In JavaScript”**](https://news.ycombinator.com/item?id=4067696)
* [A Channel9 video: **“Anders Hejlsberg: Introducing TypeScript”**](https://channel9.msdn.com/posts/Anders-Hejlsberg-Introducing-TypeScript)

