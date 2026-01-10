---
title: How to Improve your Debugging Skills
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-24T15:51:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-debugging-skills
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fb8cb2d49c47664ed823f4b.jpg
tags:
- name: bugs
  slug: bugs
- name: debugging
  slug: debugging
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Ogundiran Ayobami

  ‌‌Whether you are a beginner or expert software developer, you probably find bugs
  in your code.

  ‌‌We all have bugs in our applications because no one knows everything about coding,
  and we sometimes make mistakes. After all, there...'
---

By Ogundiran Ayobami

‌‌Whether you are a beginner or expert software developer, you probably find bugs in your code.

‌‌We all have bugs in our applications because no one knows everything about coding, and we sometimes make mistakes. After all, there is no way to stop being human.

‌‌Or can you show me how to develop a superpower? Ah alright then, never mind. :)

‌‌We can only study ourselves, our tools, and our bugs to find solutions that can help us be more efficient in reducing the bugs we create.

## How can we deal with bugs?

There are three major ways to deal with bugs:

1. Prebugging: the reduction of bugs before they're created
2. Debugging: identifying, fixing, and removing bugs once you find them
3. Post-debugging: expecting unexpected or unknown bugs

Let's look at each one in detail.

# What is Prebugging?

‌‌The late computer scientist [Edsger W. Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) said, 

> “If debugging is the process of removing bugs, then programming must be the process of putting them in.”

‌‌If we introduce bugs to a program through programming, that means we need to guide ourselves to reduce the number of bugs we introduce. I call this process of guiding ourselves "Prebugging".

‌‌I searched "define: debugging" on Google and the definition I saw from the Oxford Dictionary got me thinking.

‌‌This is the definition: 

> "[Debugging is] the process of identifying and removing errors from computer hardware or software."

‌‌What? Is that the only thing we do?

‌‌The definition got me thinking because I am sure a lot of software developers are proactive about debugging. They improve their tools and themselves to reduce the number of bugs they create in the first place.

Some ways we can do that:

1. Write program specs.‌‌
2. Learn to really understand the tools you use.‌
3. Learn to type accurately.‌ 
4. Familiarize yourself with error messages and their probable solutions.‌‌
5. Always make sure you have setups that are stable for most of the tools you use.‌‌

And a lot more!

‌‌The definition doesn't reflect all these aspects of debugging, and that forced me to think "Oh, no! Someone has to share all the things software developers do to reduce bugs."

‌‌Though the definition is acceptable for debugging, it downplays every other thing software developers do to reduce bug creation.‌‌ So let's go over those things now.

### 💥Learn the basic of the tools you use often

‌‌It is important to learn the basic of any tools you often use, because this helps you reduce the number of bugs you create while coding.

‌‌There is no way to avoid bug creation completely, but you can avoid creating some bugs if your knowledge of the basic of the tools you use is very sound.

‌‌For example, many JavaScript users can't remember what `splice()` returns. And some can't remember the difference between the `map()` and `forEach()` array methods.‌‌ What is the difference, anyway? Never mind! We're all guilty of it now and then.

‌‌If you are not a JavaScript user, just pick a built-in method or function from the language you use and ask yourself:

‌‌What kind of argument does this take? ‌‌What does this return? ‌‌What happens if an invalid argument is supplied?

‌‌Asking yourself the above questions about each of the built-in parts of whichever tool you use often can influence you to learn further and stay up to date.

‌‌That is how to keep yourself updated on the basics of the tools you often use especially if you don't have much time to read actively.

### 💥 Plan Before Coding

Programming can seem like a trial and error sport where you do it until you get it right.

‌‌Many beginner software developers don't truly understand the programs they are working on and some of them don't actually try to understand error messages before googling them.

Everybody now seems to feel that programming is always about _"Code, Code, code, Search, Debug"._

‌‌But it is necessary to really understand what you are doing so that you can quickly write out:

* What we expect to take as inputs as well as the structure and features of such inputs.‌‌
* What we expect to do with the inputs.‌‌ 
* What we expect to return or do in the end in relation to the inputs or other things.‌‌
* What we expect to do if the expected inputs are not given.

‌‌In short, planning the inputs, processes, and outputs of a function or program doesn't only help you reduce bugs but also helps you write efficient tests.

### 💥 Familiarize yourself with common error messages

It is often very easy to fix an error or a bug if you have familiarized yourself with that bug.

That is why it is important to take time to study some common errors and learn how to go about fixing them. Let's talk about some common errors now:

#### 1. Syntax Errors

Every programming language has its own rules, and developers are liable to violate those rules.

‌‌Programming languages are strict about their rules and they will throw errors whenever those rules are violated. 

Imagine, for example, that you omit the parentheses of a function or method like this:

`function {}`

An error will be thrown.

Familiarizing yourself with the error message of a syntax error and how to fix it will give you an edge while debugging it.

Personally, I have noticed that most syntax errors always mention some keywords that help you figure out the part of your code that is faulty.

```
let school = { 
name: "Harvard", 
location: "Heaven On Earth", admit: function() { return "weeew! You are admitted" } 
} 
console.log(school.names); // undefined
```

The "undefined" that's returned tells us whether the object or property we are accessing is not available. We can figure out where the problem is if we pay keen attention to the error message.

‌‌Now, let's take the example a bit further. 

`console.log(school.locations.address);` // Uncaught TypeError: Cannot read property 'address' of undefined.

‌‌If we pay close attention to the error message, we can easily figure out where the bug is.

‌‌From the error message above, "Cannot read property 'address' of undefined" means that address is a property and a property is known to be in an object (in JavaScript). But in this case, the object is said to be "undefined".

‌‌The more you code the more you get better at avoiding syntax errors. You can also simply use code editors, linters, or IDEs that highlight syntax errors. Using these tools can help you a lot.

**You can check out these code linters to see which one works best for your use case:**

[ESLint](https://eslint.org/docs/user-guide/getting-started) for JavaScript

[PyLint](https://www.pylint.org/) for Python

[Checkstyle](https://github.com/checkstyle/checkstyle) for Java

[PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) for PHP

Also, most of the popular code editors like VSCode can be configured to use the code linters above.

#### 2. Logic/Semantic Errors

Logic errors are very tricky to deal with because they always seem like there is no error – but you still don't get the expected result.

For example, a simple way to confirm this kind of error is to check the code below in the browser's console.

‌`prompt("enter number") + 3;`

You may expect a number as an output, but it will return a string. In short, you will not get the expected result.

Planning before coding and understanding the basics of the programming language you use can help you deal with logical errors – provided you understand the program requirements given to you.

#### 3. Compilation Errors

Your program may not compile because you might have violated some rules the compiler expect you to stick to. So, the program you are working on may not compile.

For example, writing a string without the usual quotes, as in `const name = Ayobami`, will lead to a compilation error because a string must be quoted. So, the code will not compile.

‌‌This is similar to syntax errors, and the more you code, the more you get better at dealing with compilation errors.

You can be more effective and reduce these errors by compiling or testing your code often.

#### 4. Resource Errors

Sometimes, your program may exceed its memory limit or use up the available resources. That may lead your application to go out of service or malfunction.

The code below is a real-world example of code that leads to resource errors.

```javascript
function factorial(num) {
  var result = 1;
  for(var i = num; i > 0; i--){
    result = num * factorial(num-1);
  }
  return result;
}

factorial(5);
factorial(10);
factorial(20);
factorial(0);

```

The function `factorial()` crashes or slows down the browser because the ‌‌stack space, that is the memory the browser allocates to the function call chain, is used up. The error, in this case, is a resource error because it occurs as a result of using up the allocated memory (resources).

#### 5. Interface Errors

‌‌Sometimes we design program APIs to be used in certain ways but users use the programs differently and cause errors. Such errors are referred to as interface errors.

‌‌For example, let's say that the method `go(string)` expects a string but we call it with a number instead. That will lead to an error if the creator of the program doesn't expect and manage how the program should respond in such a case.

‌‌Most things in software follow standards. If your defined standards are not followed, you need to provide your users with error messages or guides to help them figure out they are using the application wrongly.

Documenting your APIs can help a lot in this case.

### 💥 Makes sure your setups are suitable for your tools

It is important to have a setup that is suitable for your tools. Sometimes, your OS may not be compatible with your applications – maybe because it requires a newer version of the OS or it requires a certain software.

For example, WampServer may not run properly on Windows OS if some Microsoft VC runtimes are missing on the computer. Similar things can also happen with Linux and macOS.

You just have to be sure your setup is suitable for whatever you do.

### 💥 Be deterministic about the functions of your program

> ‌‌"In mathematics, computer science and physics, a deterministic system is a system in which no‌‌ randomness is involved in the development of future states of the system.  
>   
> A deterministic‌‌ model will thus always produce the same output from a given starting condition or initial state." - [Source](https://en.m.wikipedia.org/wiki/Deterministic_system)

‌‌Then, the question is, how do we make a deterministic program? ‌‌You have to be certain about the type of data that's acceptable in your program and reject any data that doesn't fit in.

‌‌In short, you need to take the expected data and reject unexpected data or notify your users about expected data.

### 💥 Don't use it if you don't understand It

‌‌One of the best ways to reduce the creation of bugs is to only use approaches, methods, and classes you understand. If you have to use any approach or style you don't understand, research it and be sure of what you are about to do before doing it.

‌‌It is easy to introduce unnecessary bugs to your application whenever you make use of things you don't understand.

### 💥 Learn to type accurately

Typing accurately is underrated, because programming is more about thinking than typing. But being accurate while typing may help you reduce some syntactic errors, type errors, or typos.

Many programming bugs are caused by simple typographical errors. Your ability to type accurately gives you an edge in reducing bugs.

### 💥 Watch fellow developers while debugging

‌‌Another interesting way to improve your debugging skills is to watch fellow developers while they are debugging. It helps to see different debugging methods, especially through their lenses.

‌‌There will always be tools or approaches we don't know about or use for debugging.‌‌ Watching others gives us the chance to discover the tools or approaches we may not be aware of.

Or even if you are aware of those different approaches, you might not know why or how to use them.

‌‌Watching others can influence us to revisit these approaches and tools that may eventually improve our debugging skills.

# What is Debugging?

Debugging is at the core of programming, because it takes up the largest percentage of your time while coding.

There are three major phases involved in debugging:

1. Finding bugs.
2. Analyzing and understanding why bugs occur.
3. Fixing or removing bugs.

### How to find bugs

Finding bugs starts with understanding the error messages you see.

It goes without saying that an error message is a pointer to a bug. If you understand the error message, you can track down the location of the bug with precision.

But some errors can be tiring because they may not have explicit error messages. We just may not get an expected result.

To find bugs, you need to:

* Be clear about your expectations.
* Check the results you get.
* Compare your expectations and the actual result to see what is missing.

You can use a debugger or other useful tools to find those errors fast.

You can then check different parts of your code against your assumptions and perform trial and error to find the bug.

### How to Understand Why Bugs Occur

‌‌After finding a bug, you need to figure out why the code is behaving the way it does. Doing this helps you build an efficient system.

‌‌Instead many developers will just google and use the answers they get directly from StackOverflow.

‌‌That is fine in certain circumstances, but it is better to understand the cause of a bug and why the solution works.

‌‌Understanding the cause of a bug is an important step on the path to fixing it or removing the bug.

### How to Fix or Remove Bugs

‌‌After finding and understanding the cause of a bug, we have to fix that bug. Sometimes, once you understand what the bug is, you'll simply find a solution without stress.

‌‌However, there are times when our understanding yields no solution no matter how hard we try.

‌‌Instead of wasting time, it is okay to Google the error message or whatever you feel is appropriate.

‌‌You can also ask another person because others tend to see things differently. They are neutral and that neutrality does help in fixing some bugs.

‌‌So, Google it!

‌‌Ask questions on StackOverflow, Twitter, or wherever you're connected to other developers.

‌‌It's okay! We all do those things a million times.

‌‌Fixing a worrisome bug always brings about great excitement. But don't get caught up too much in the excitement, as fixing a bug may cause another bug. So first make sure you have not introduced another issue to the program. That is why automated tests are important.

# What is Post-debugging?

"Post-debugging" is about anticipating unexpected bugs in programs you've already written.

It refers to all the mechanisms you might use to ensure that unknown bugs are easily tracked down or managed before they harm the system or company.

The question now is how do you do that? Well, with an error tracking system.

You should have an error tracking system in production so that you can easily discover bugs as they emerge after pushing your application to production.

There are a lot of error trackers out there and they are just a bit of googling away. But here are a few you can check out:

* www.sentry.io
* www.honeybadger.io
* www.pypi.org
* www.airbrake.io
* www.logrocket.com

There are so many error trackers out there, you'll just have to research to discover what is best for you.

## Conclusion

Debugging is a major skill that all software developers must cultivate. It is at the core of coding, and if you do it well, it can make you a better developer.

To be great at debugging, you must learn as much as you can about various debugging methods, many of which I've discussed here in this article.

It is time to be a great software developer and debugging can help you along the line.

Now, you only need to put everything into practice to be great at debugging and your software development skills will not be the same again. 

## About the author

**[Ayobami](https://twitter.com/codingnninja)** loves writing history with software development and is currently helping those who are struggling to understand and build projects with JavaScript through **[You Too Can Code](https://bit.ly/3o3TMyg)**.

