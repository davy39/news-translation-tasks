---
title: How JavaScript’s Asynchronous Operations Work in the Browser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-16T21:58:01.000Z'
originalURL: https://freecodecamp.org/news/javascript-asynchronous-operations-in-the-browser
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Amazing Enyichi Agu\nJavaScript is a popular programming language used\
  \ for developing interactive front-end web applications, among other things. \n\
  It's widely known for its major features: it is single-threaded, non-blocking, and\
  \ asynchronous. But ..."
---

By Amazing Enyichi Agu

JavaScript is a popular programming language used for developing interactive front-end web applications, among other things. 

It's widely known for its major features: it is _single-threaded_, _non-blocking_, and _asynchronous_. But what do these three things mean?

### What Does "Single-Threaded" Mean?

When a programming language is referred to as single-threaded, it means the language can execute only one instruction at a time. This differs from multi-threaded programming languages that run multiple instructions at once.

![Illustration depicting Single-threaded and Multi-threaded processes](https://www.freecodecamp.org/news/content/images/2023/05/single-and-multi-threads.png)
_Illustration depicting Single-threaded and Multi-threaded processes_

### What Does "Non-Blocking" Mean?

When a programming language is said to be non-blocking, it means that the language does not wait for a specific previous instruction to finish executing before it moves to the next one. This ensures that no instruction blocks or obstructs the execution of subsequent instructions. 

If a programming language is not non-blocking, it could lead to slow applications.

![Illustration of JavaScript’s non-blocking behavior](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2.png)
_Illustration of JavaScript’s non-blocking behavior_

### What Does "Asynchronous" Mean?

JavaScript is also asynchronous (async), which means that it can handle a large number of tasks at a time. This is a feature of multi-threaded programming languages, but JavaScript achieves it with a single thread.

![Illustration of the asynchronous process](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-3.png)
_Illustration of the asynchronous process_

Now, these features of JavaScript might seem contradictory. How can a language that is supposed to execute only one task at a time (Single-threaded) be able to handle a large number of tasks (asynchronous) simultaneously?

In this article, you will gain an understanding of how JavaScript manages to remain single-threaded despite executing asynchronous operations in the browser. We will also explore some concepts necessary for understanding the process.

This article assumes that you have basic knowledge of JavaScript and can apply it to Web Applications. The article covers the steps JavaScript takes to handle async operations in the browser. It does not go into detail to teach the different async functions there are, or how to write them. It only covers their process of execution in the browser.

The exciting part of all of this is that the article tells a short story, and uses this story as an analogy to explain the process. Through this unique approach, you will gain more insight into the inner workings of asynchronous operations.

Here's what we'll cover:

1. [The story that will help explain these concepts](#heading-the-story)
2. [How the JavaScript engine works](#heading-how-the-javascript-engine-works)
3. [How the call stack works](#heading-how-the-call-stack-works)
4. [Asynchronous operations and web APIs](#heading-asynchronous-operations-and-web-apis)
5. [Callbacks](#heading-callbacks)
6. [Callback queue](#heading-callback-queue)
7. [Event loops](#heading-event-loops)
8. [Conclusion](#heading-conclusion)

## The Story

This is the story of two companies. One of them is called _Lerdorf Corp_ while the other is _Eich Agency_. These two companies are Event Planning Agencies and they cater to clients who need professional event planning services.

Lerdorf Corp is a long-running and successful company. They have a lot of staff and multiple specialized departments who work together to make sure they remain profitable. These departments include Catering, Registration and Ticketing, Accounting, and more.

When Lerdorf Corp secures a contract with a client, their efficient work process kicks into gear. The company swiftly breaks down the project into manageable tasks and assigns them to the respective departments responsible for their execution. This seamless division of labor ensures that each department can focus on its specific area of expertise, working in sync to deliver results.

This operational approach Lerdorf Corp employs is similar to how [Multi-threaded Programming Languages](https://en.wikipedia.org/wiki/List_of_concurrent_and_parallel_programming_languages#Multi-threaded) function. In Multi-threaded programming, a program can be split into separate [threads](https://en.wikipedia.org/wiki/Thread_(computing)), with each executing independently of the others.

Returning to our story, let's now shift our focus to the Eich Agency. It's a small agency with limited staff. Despite their ambitious aspirations, it may seem quite laughable that they aim to compete with the well-established Lerdorf Corp.

Lerdorf Corp initially did not see them as a competition. They gave Eich Agency a month or two to move out of business. Eich Agency did not have any specialized departments. Yet, they were successfully able to execute big events, exactly the size one would think only Lerdorf Corp could pull off. Eich Agency’s client base also steadily expanded over time.

Lerdorf Corp did not understand how this could be the case. It was clear to them that Eich Agency did not have sufficient resources. They struggled to make sense of the situation and eventually held a meeting concerning the issue.

During the meeting, they decided to investigate how Eich Agency was able to execute events for clients so quickly without enough resources. Lerdorf decided to designate a capable staff member to conduct an extensive investigation of the agency and compile a comprehensive report within one week. 

After one week, the report was completed, and the executive staff at Lerdorf Corp reviewed it together.

## How the JavaScript Engine Works

With the investigation, it turned out that Eich Agency had a core team. The team received requests for planning events for clients. Now that team was responsible for most of the planning. They generated a blueprint for how an event would work out.

The Eich Agency team usually ordered the small tasks they needed to execute into a roadmap, then they'd start from the top to bottom, executing them in order. They did this because they did not have separate departments dedicated to a set of tasks like Lerdorf Corp.

JavaScript executes instructions similar to how Eich Agency does it. For a browser to interpret JavaScript code, it needs to have a [JavaScript engine](https://en.wikipedia.org/wiki/JavaScript_engine). This JavaScript engine is a software component of a modern web browser that accepts JavaScript code, analyzes it, and transforms it into instructions the device will understand. The JavaScript engine can be likened to the core team of Eich Agency.

![JavaScript Engine inside the Runtime](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-1.png)
_JavaScript Engine inside the Runtime_

The JavaScript runtime is the environment that contains all the resources necessary for the execution of a JavaScript program. It includes the JavaScript Engine but also includes other things we will look at.

Different browsers today use different JavaScript engines. For example, the Chrome Browser uses the [V8 Engine from Google](https://v8.dev/), Firefox uses one called [Spidermonkey](https://spidermonkey.dev/), and Opera Browser previously used the [Carakan](https://dev.opera.com/blog/carakan/) engine, before switching to V8.

These engines have individual differences, but their jobs still remain the same. They process JavaScript Code.

## How the Call Stack Works

As the staff of Lerdorf Corp reviewed the report, they made an intriguing discovery. Eich Agency, upon finalizing the sequence of preparatory tasks for an upcoming event, would display the list on their board. With this order in place, the core team knew what task to start with and what to continue with.

The board Eich Agency uses to publicly list the order of tasks is similar to the Call Stack in the JavaScript Engine. The call stack is a component of a JavaScript Engine that keeps track of all the functions the program executes. It is a [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) data structure that operates with two key operations.

These operations are:

* Push: This operation adds or pushes a new function onto the top of the stack. The stack can only add new entries to the top.
* Pop: This operation removes or pops a new function off of the top of the stack. The Stack can only remove new entries from the top.

**Last In First Out (LIFO)** is a term that summarizes how the call stack works. The last operation that went in is the first operation that will leave the stack.

![Simple Illustration of the Call Stack](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--1-.png)
_Simple Illustration of the Call Stack_

After the JavaScript Engine receives JavaScript code, it parses the code and places the first function it encounters on the call stack. If, while executing that function, the JavaScript engine notices that it calls other functions, then those functions are stacked on top of the call stack. This is very important for functions nested in other functions as well as recursive functions.

The call stack makes it possible to track the current and future running functions essential for the execution of a program. For the stack to pop off a function, the engine must have finished interpreting and running that function. If not, it remains there. A peek at the JavaScript call stack during the execution of a program shows the current state of the program.

For example, consider these JavaScript instructions.

```javascript
function greeting() {
	console.log("Hello World")
}

function run() {
	greeting()
}

run()

```

Upon execution of the code, the call stack can look something like this:

![The Call Stack while monitoring functions](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--2-.png)
_The Call Stack while monitoring functions_

To recap, whenever the JavaScript engine receives code, it parses it and uses a call stack to monitor the execution of these instructions. This is similar to the way Eich Agency displays the order of tasks they need to accomplish.

## Asynchronous Operations and Web APIs

The way the Eich Agency core team ordered the tasks they wanted to execute was not strange to Lerdorf Corp at all. They themselves as a company employed a similar strategy when they wanted to work for clients, but there were some distinctions.

In Lerdorf, whenever they got a contract, the first thing they did was break the task into a few smaller chunks. After they broke it down, they sent those chunks to different departments they had. They had a lot of departments and the process was faster if those departments started working on the tasks independently.

Lerdorf Corp already had each individual department with their own board similar to the one Eich Agency used. The departments used it to keep track of the tasks to accomplish. 

Relating it to JavaScript terms, they had many “call stacks” that operated independently. Meanwhile, the Eich Agency had only one “call stack”.

This revelation puzzled the Lerdorf Corp team more. How then did Eich Agency manage to host large events properly if they pretty much had just a single department? This was the question on everyone’s mind.

Upon further review of the report, the Lerdorf team made a shocking discovery. They discovered that the core team at Eich Agency did not actually do all the work themselves. They did not have a Catering or Audio-Visual department, while these were departments Lerdorf Corp had.

But based on the contracts Eich Agency secured, they were typically expected to provide these services. When drafting their lists of tasks, they included the provision of these services, even though the agency could not provide them in-house.

Here's what they did instead: while executing their tasks, whenever Eich Agency encountered a task they could not immediately execute, they took action. They contacted a different company offering that specific service and requested help. After contacting the company, they returned to their order of tasks.

If, while following their list of tasks, they encountered another assignment that they couldn't perform, they repeated the process. They would find a separate service provider, discuss their needs with them, and request the required service.

Relating this to JavaScript, even though JavaScript is single-threaded, it is also asynchronous. In asynchronous programming, a language can execute multiple tasks simultaneously. Just like Eich Agency, whenever JavaScript encounters asynchronous instructions like requests to third-party sites, or timer-based actions, it seeks assistance. 

To achieve this, JavaScript uses the browser’s provided **Web Application Programming Interfaces (Web APIs).**

One very important reason for writing asynchronous code is to prevent a scenario where a particular running function ends up blocking the rest of the code. If this happens, it can cause undesirable user experiences and make our software inefficient.

The Web APIs are a set of functions provided by the browser that the JavaScript engine can utilize. They include examples such as Document Object Model (DOM) manipulation methods, `fetch`, `setInterval`, `setTimeout`, promises, async-await functions, and more.

![The JavaScript Engine interacting with the Web API](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--3-.png)
_The JavaScript Engine interacting with the Web APIs_

### Callbacks

Let us briefly go back to the story of Lerdorf Corp and Eich Agency. Recall that Eich Agency contracted service providers and requested their assistance, and then continued with their order of execution.

Whenever any of the external service providers called back the agency to deliver a response, such as notifying the completion of a request, the agency would later act upon this new information. 

Lerdorf Corp discovered that even though the external providers handled and completed many services, the agency's core team still needed to take further action.

For example, let's say the core team of Eich Agency had requested a catering service provider to supply a certain quantity of snacks and drinks. The core team would still be responsible for collecting the snacks from the caterers and incorporating them into their inventory of items for the event. In this scenario, the snacks would join other items that Eich Agency had prepared for the event.

This is similar to how JavaScript works in the browser. Asynchronous operations provide a response after being processed using Web APIs. The purpose of writing an asynchronous function is to utilize the function's output for subsequent operations. We refer to the functions that rely on the response from asynchronous operations as callback functions.

A callback function is a function that is passed as an argument to a parent function, which the parent function needs to invoke after completing its process. In JavaScript, asynchronous operations utilize callbacks to further process the responses they receive from Web APIs.

The example below is an asynchronous operation with a callback function.

```javascript
button.addEventListener('click', function () {
	console.log('I was clicked!')
})
```

Now whenever the user clicks on the button, it triggers the callback function to fire. But the callback cannot happen unless the parent function calls or invokes it, which is dependent on the user's action.

You can also observe the use of callback functions with the **`fetch`** API.

```javascript
fetch("<https://jsonplaceholder.typicode.com/users>")
.then((response) => response.json())
.then((response) => console.log(response))
```

In this example, the **`then`** method of the **`fetch`** object accepts an arrow function as an argument. The execution of this function is dependent on the response received from the fetch request, making it a callback function. 

Also, in the second **`then`** method, you can see the usage of another callback. This is because the first callback returns another asynchronous function, necessitating the use of a callback.

To recap, a callback function is passed in as an argument to an asynchronous function and only runs when the asynchronous operation has been completed. This is similar to how Eich Agency only executes some tasks when their third-party vendors have called them back.

### Callback Queue

Continuing their examination of Eich Agency’s execution process, the Lerdorf Corp team also discovered that Eich Agency often received multiple “call-backs” from the vendors they contacted. Each of these responses needed some action from the Eich Agency team.

Eich Agency streamlined its process further by keeping a separate list. This was a list where, whenever a vendor sent them a response they were supposed to act on, they would put that action inside the list. 

This is what they did for every “call-back” they got. Eich Agency eventually ended up with a queue of extra tasks to perform but in a list separate from the one up on their board.

That list is similar to the Callback Queue in the browser’s JavaScript Runtime. The callback queue is a software mechanism that stores callback functions to be run after the Web APIs have processed asynchronous functions. It uses the [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) data structure which works with the **First In First Out (FIFO)** approach. This means that the first callback added to that queue is going to be the first callback to leave.

![JavaScript Runtime showing the Callback Queue](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--4-.png)
_JavaScript Runtime showing the Callback Queue_

### Event Loops

Eich Agency implemented one final step to make sure everything went well between them and their clients. They would wait until they completed the tasks on their initial board before addressing the queue of extra tasks.

Eich Agency designated a member of their core team to manage the queue of tasks. This team member would await the completion of the regular tasks by other team members. Once the initial tasks were cleared, the assigned team member would select the first item from the queue of extra tasks and display it on the board.

The core team would proceed to complete the assigned task, such as receiving the snack supplies from the vendors. Once accomplished, the team member responsible for managing the extra tasks would select the next item and add it to the board. The core team would then work towards achieving this task, and the process would repeat in a loop until all the items on the queue of extra tasks were exhausted.

The team member in charge of the extra tasks can be likened to the event loop in the browser’s JavaScript Runtime. The event loop is a loop that continuously checks if the call stack is empty. When the call stack is not empty, it allows the ongoing process to continue. But when the call stack becomes empty, the event loop fetches the task at the top of the callback queue and adds it to the call stack.

The event loop runs continuously as long as the program is running, always performing its function until the callback queue is completely empty. This is why the JavaScript Engine executes callbacks only after everything in the call stack has been processed.

For example, consider this code snippet.

```javascript
console.log('A')
setTimeout(() => console.log('B'), 0)
console.log('C')

// A
// C
// B

```

It ends up logging A and C before B, even though the timeout was for 0 seconds. The reason for this is that the callback in `setTimeout` waited in the callback queue (`setTimeout` uses the Web API). The JavaScript Engine had to finish handling synchronous functions before handling the asynchronous ones. It needed the help of the event loop to send the callback function to the call stack.

![The Event Loop in the JavaScript Runtime](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--5-.png)
_The Event Loop in the JavaScript Runtime_

To complete the story, after Lerdorf Corp understood how Eich Agency operated, they were impressed. They admired the way Eich Agency utilized its resources, but they immediately saw that it posed a threat to them and could potentially impact their business negatively.

Later on though, Lerdorf Corp realized that their client base differed from that of Eich Agency. While Eich Agency excelled in planning social events, Lerdorf Corp specialized in working with companies and organizing corporate events. There was no need for them to feel threatened by Eich Agency’s success. :)

## Conclusion

In this article, you have learned various important concepts that illustrate the asynchronous nature of JavaScript. 

We began by discussing the three fundamental characteristics of JavaScript – that it's single-threaded, that it's non-blocking, and that it's asynchronous – and acknowledged that they may initially appear contradictory. After that, we clarified this apparent misconception by explaining the details.

You learned some concepts like the JavaScript engine in the browser, the call stack, callbacks, the callback queue, and the event loop.

Additionally, we used a story as an analogy to enhance your understanding of these concepts further. With this, you should have gained a solid understanding of how asynchronous operations function in the browser.

