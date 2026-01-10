---
title: How to Improve Your Debugging Skills
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T17:17:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-debugging-skills-abb5b363bdb8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*akKmLhkA0fJ__-hb3Bp8WA.jpeg
tags:
- name: careers
  slug: careers
- name: Computer Science
  slug: computer-science
- name: debugging
  slug: debugging
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Nick Karnik

  All of us write code that breaks at some point. That is part of the development
  process. When you run into an error, you may feel that you don’t know what to do.
  However, even the most seasoned developers introduce errors and bugs that...'
---

By Nick Karnik

All of us write code that breaks at some point. That is part of the development process. When you run into an error, you may feel that you don’t know what to do. However, even the most seasoned developers introduce errors and bugs that break their code. We are humans after all.

The important thing is to learn from these mistakes and avoid repeating them by developing techniques to improve your programming and debugging skills. Errors are primarily logical or syntactical. Some of them manifest via exceptions or crashes while others may only be observed when using the software.

### Here are some of the mistakes that developers make

#### Failure to Log Messages

One of the most unhelpful scenarios you can run into is when your program crashes and there are no error messages to indicate what went wrong. The first step is to identify if the program is crashing on start or during runtime. You can accomplish this by printing a simple log message to the terminal at the beginning of your code.

If you don’t see your log message, your program is most likely crashing while loading and it is possibly a dependency or build related issue.

If you see your message, you need to narrow down to the general vicinity of the crash. The best way is to strategically place some log messages throughout your program depending upon how much information you have about the execution path by the time it crashes. Then, all you have to do is see which messages are printed.

#### Failing to Read Error Messages

Exception messages on the front-end are usually displayed on the UI or developer console. Sometimes these messages are visible in the backend through the terminal or via log files. Regardless of where these errors occur, new developers are intimidated by them and fail to take the time to read them.

This is the number one reason why debugging takes longer for many developers. The first thing you should do is take the time to read the error message in front of you, let it sink in, and process it thoroughly.

#### Failing to Read System Log Files

Some programs generate log files or write to the system event log. There is often useful information in these logs. Even if it doesn’t tell you exactly what is wrong, there might be a warning or error message or even a success message providing a hint about what happened before the error occurred.

#### Failing to Write Trace Logs

Tracing is following your program flow and data. Writing trace messages throughout your program helps simplify the debugging process. Trace Logs are an easy way to keep track of program execution throughout the runtime of your application.

#### Failing to Make Incremental Changes, Build Them, and Test Them

Many developers write big chunks of code before building and testing it. The time to find bugs increases proportional to the amount of code that was changed. You should strive to make incremental changes, build them, and test them as frequently as possible. This will ensure that you don’t end up in a situation where a lot of code was written before you discover your program doesn’t work.

Often, I will even refactor my code to simplify what I’ve written.

#### Failing to Write Test Automation

Unit-tests and end-to-end test automation allow you to catch potential errors as they happen. One of the reasons why existing code breaks is that developers refactor their code when they have low test coverage, which means all changes are not tested automatically.

#### Failing to Use the Method of Elimination

If you’re unable to identify the root cause of your issue, you need to use the method of elimination. You can comment out new blocks of code to see if the errors stop. Eliminating blocks of code will help you get closer to diagnosing the issue.

You can form a certain hypothesis and try to prove or disprove it. Many times a simple assumption can prevent you from finding bugs.

#### Copying and Pasting from StackOverflow

Often developers copy and paste code from stack overflow without understanding what it does. This has so many adverse effects. First, it is important that you pay attention to what goes into your application.

More often than I’d like, when I write a question on StackOverflow and think about how to effectively articulate it, I end up answering my own question!

Similarly, sometimes when I talk to other members of the team, I end up answering my own question. This happens because it forces you to think about your solution.

#### Failing to Solve their Problem Again

One of the most successful debugging techniques I have found is to try to walk through your solution over and over again and in some cases try to re-implement certain functionality from scratch. This forces you to find potential issues by recreating your implementation.

#### Failing to Backtrack

Normally, if you can isolate the symptoms to a specific area, you can start to walk up the call-stack to verify all variables and expected values. This can quickly lead you to uncover parts of your program where things are behaving unexpectedly.

#### Failing to Learn the Debugger

Finally, the single best investment you can make in yourself is to learn to use a debugger. All IDE’s come with powerful debuggers. They follow the same basic concepts. They allow you to programmatically stop the execution of your application, either on start or in a specific part of the program flow.

There are also a ton of debugging tools that can aid in this process.

If this article was helpful, ??? and Fol[low me on Twitter.](https://twitter.com/intent/follow?screen_name=theoutlander)

[**GitHub Extensions to Boost Your Productivity**](https://medium.freecodecamp.org/github-extensions-to-boost-your-productivity-4692ad2b1796)  
[_Here are GitHub Extensions that I use. They will enable you to improve your productivity on GitHub. Please share your…_medium.freecodecamp.org](https://medium.freecodecamp.org/github-extensions-to-boost-your-productivity-4692ad2b1796)

