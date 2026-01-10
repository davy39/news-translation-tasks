---
title: What is Reactive Programming? Beginner's Guide to Writing Reactive Code
subtitle: ''
author: Pacifique Linjanja
co_authors: []
series: null
date: '2024-03-18T09:02:54.000Z'
originalURL: https://freecodecamp.org/news/reactive-programming-beginner-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-14-at-17.29.29.png
tags:
- name: best practices
  slug: best-practices
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Welcome to your journey through the dynamic world of reactive programming!
  This fascinating paradigm is all about building responsive, resilient, and adaptable
  applications that effortlessly manage vast amounts of data almost instantly.

  Imagine writi...'
---

Welcome to your journey through the dynamic world of reactive programming! This fascinating paradigm is all about building responsive, resilient, and adaptable applications that effortlessly manage vast amounts of data almost instantly.

Imagine writing a program that needs to react instantly to changes—whether that's user inputs, messages from other systems, or live data feeds. That's where reactive programming shines, making it a cornerstone of modern software development, especially for web and mobile applications.

Let's draw a simple parallel to everyday life to bring this concept closer to home. Consider a bus station, a familiar sight where people queue up, waiting for their ride. Each bus arrival is an event, and the passengers' response—to board the bus—is an action triggered by this event. 

Reactive programming works similarly. It deals with data streams (like the schedule of arriving buses) and the propagation of change (a new bus arriving), enabling applications to respond in real-time (just as passengers react by boarding the bus). Sound familiar?

In this article, we'll dive into the essence of reactive programming, focusing on its implementation using JavaScript/TypeScript within the Node.js environment. We'll also keep an eye on a global context that applies to many programming languages and frameworks. 

We'll keep things straightforward and engaging, using simple language and practical examples. By the end of this guide, you'll have a solid foundation in reactive programming concepts and hands-on experience building a real-time notification system. 

Whether you are new to the concept or looking to refine your skills, this guide is crafted to demystify reactive programming and show you its power in action. Let's get started on this exciting journey together!

## **What We'll Cover:**

1. [Understanding Streams and Observables](#heading-understanding-streams-and-observables)
2. [Reactive Programming in JavaScript/TypeScript and Beyond](#heading-reactive-programming-in-javascripttypescript-and-beyond)
3. [How to Build a Real-Time Notification System with Node.js](#heading-how-to-build-a-real-time-notification-system-with-nodejs)  
– [Introduction to the Notification System](#heading-introduction-to-the-notification-system)  
– [Project Setup: Getting Started with Node.js and TypeScript](#heading-project-setup-getting-started-with-nodejs-and-typescript)  
– [How to Implement the Core Features](#heading-how-to-implement-the-core-features-building-a-real-time-notification-system)
4. [Best Practices and Common Pitfalls](#heading-best-practices-and-common-pitfalls)
5. [Conclusion](#heading-conclusion)
6. [Resources](#heading-resources)

## Understanding Streams and Observables

Let's dive into the heart of reactive programming: streams and observables. These concepts are the building blocks of reactive applications, enabling them to process data dynamically and reactively. To understand their significance, let's revisit our bus station analogy.

Imagine the bus station being equipped with a digital display showing real-time updates of bus arrivals, departures, and delays. This display is constantly receiving data about buses - this flow of information is what we call a "stream." Each piece of new data (like the arrival of a bus) can be seen as an "event" in this stream.

### Streams: The Flow of Data

In programming, a stream is a sequence of ongoing data made available over time. Streams can be anything: mouse movements, keystrokes, tweets, or even real-time stock market updates. They're not so different from the bus station's digital display, which receives a continuous flow of information about buses.

In short, a stream is a collection of values pushed over time, the interval between two different values can be controlled (scheduled streams) or random (we never know when someone will send us a message right?). 

Streams can emit three different things: a value (of some type), an error, or a "completed" signal. Let’s think of a notification system, for example. On one end we have a client (mobile app, web app, and so on) that has subscribed to a WhatsApp group. Whenever there is a new message in that group, the application will react by sending a push notification to the user–but we never know when those messages are coming.

Figure 1 below shows an illustration of what can be considered as a stream. After some time, the value can change, notifying every client that subscribed to the stream that a new value is available. It gives clients the possibility to unsubscribe at any time they want.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Guessing-game-Page-4.drawio--1-.png)
_Figure 1: Illustration of what is a stream, subscription, and unsubscription_

As you can see from the image above, from the moment a client unsubscribes, they stop getting new values from the stream.

### Observables: Reacting to Data

An observable is a type of stream that you can observe, enabling you to listen for and react to incoming data. 

To illustrate, consider the digital display at a bus station as the stream. As you eagerly wait and watch for information about your bus's arrival, you are akin to an observable. When your bus's arrival is displayed (an event), you react by preparing to board it.

Observables are characterized by the following three aspects:

1. **Data Lifecycle:** An observable is a primitive type that can contain zero or multiple values. These values are pushed over any duration, determining the lifecycle of the stream.
2. **Cancellable:** Observables can be cancelled at any time. By informing the producer that you no longer require updates, you can cancel a subscription to an observable.
3. **Lazy Evaluation:** Observables are lazy, meaning that they do not perform any actions until you subscribe to them. Similarly, they cease operations when unsubscribed. This stands in contrast to Promises, which are eager and must be settled each time they are invoked before further processing occurs.

### Why Streams and Observables are Important

Streams and observables are crucial in reactive programming because they allow applications to handle data that changes over time—just like the constantly updating information on the bus station display. 

They make it possible for apps to react instantly to new data, from a user clicking a button to receiving messages from a web service.

### Operators

Streams alone are useful, as they allow multiple Observers to subscribe to it for their updates. Things start to get more enjoyable when you want to manipulate a stream. Streams can be transformed and even combined, using operators.

RxJS itself for example contain hundreds of operators inspired by some well-known JavaScript's arrays’ methods like map, filter, reduce, etc.

Operators are simply functions that take an observable and return an observable with some operation applied to it. 

Let's look at two essential operations: **mapping and filtering**. Take a look at the following animation:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/map-filter-stream-e0e9503b758fe89104ae60e0ecd48995.gif)
_Figure 2: operators on an observable - [source](https://reactive.how/filter)_

In _Figure 2_ above, for the `map` operator, when the input observable emits a value, it is being processed by the `isEven` function and the resulting value is emitted as a value for the output observable. 

For the `filter` operator, when the input stream emits a value, it is given to the same function, which emits a value for the output observable when it fulfills the condition. Otherwise, it is ignored. The input is an observable, and the operator returns another observable.

## Reactive Programming in JavaScript/TypeScript and Beyond

In the world of JavaScript and TypeScript, particularly in the Node.js environment, streams and observables are crafted with both grace and effectiveness.

Node.js offers built-in support for streams, enabling powerful data handling capabilities for server-side applications. Also, libraries and frameworks built on top of the reactive programming paradigm, such as RxJS for JavaScript/TypeScript, provide developers with powerful tools to create reactive applications.

RxJS, for instance, is a library specifically designed for reactive programming in JavaScript/TypeScript. It provides a vast collection of operators to create, combine, and manipulate observables. With RxJS, developers can handle complex data flow scenarios with ease, thanks to its intuitive API and extensive operator set.

But reactive programming is not limited to JavaScript/TypeScript and Node.js. Many other programming languages have their own implementations of reactive programming paradigms and libraries.

For example, languages like Java have RxJava, Kotlin has RxKotlin, and Swift has RxSwift. These libraries offer similar functionalities to RxJS but are tailored to their respective language ecosystems.

Regardless of the programming language you're using, the principles of reactive programming remain applicable. Whether you're working in JavaScript, Java, Kotlin, Swift, or any other language, you can leverage reactive programming to build responsive, scalable, and maintainable applications. 

The concepts of streams, observables, and operators transcend language barriers, providing developers with a powerful toolkit for handling asynchronous data flows and creating dynamic user experiences.

## Putting It All Together

Imagine we're developing a feature for our bus station app that notifies users when their bus is approaching. Using RxJS, we can create an observable that represents the stream of bus arrival data. Each time a bus's status is updated—say, when it's 10 minutes away—the observable emits an event. Our app can subscribe to these events (observe them) and react by sending a notification to the user: "Your bus is on its way!"

This scenario showcases the power of reactive programming with streams and observables. Not only does it allow for real-time responsiveness, but it also simplifies the handling of asynchronous data flows, making our code cleaner and more intuitive.

This fundamental understanding of streams and observables is your first step into the world of reactive programming. As we move forward, remember the bus station's digital display and how it continuously updates. Our applications, much like an attentive traveler, has to be ready to respond to these updates as efficiently as possible. 

With RxJS and the concepts of streams and observables, we're equipped to tackle these challenges head-on, creating applications that not only meet but exceed user expectations in terms of responsiveness and performance.

Engaging with these concepts is not just about understanding theory – it's about seeing the immense potential they unlock for developing dynamic, user-centric applications. As we dive deeper into practical examples, keep the bus station analogy in mind—it will help you grasp the more complex aspects of reactive programming in a relatable and straightforward way.

## How to Build a Real-Time Notification System with Node.js

In this section, we'll embark on a journey to create a real-time notification system using Node.js. Imagine a scenario where users of a web application need to receive instant updates on various events, such as new messages, notifications, or system alerts. 

Our goal is to build a robust and efficient system that delivers these notifications seamlessly in real-time.

### Introduction to the Notification System

Before diving into the technical implementation, let's envision how our real-time notification system will function. Users will interact with the system through a web interface, where they'll be able to subscribe to different types of notifications based on their preferences.

These notifications could include new messages in a chat room, updates on shared documents, or alerts for important system events. We will try to keep it very simple, since the goal is really getting started with the paradigm.

### Key Interactions with the System

1. **User Subscription:** Users will have the option to subscribe to specific types of notifications, tailoring their experience to their preferences and needs.
2. **Real-Time Delivery:** Once subscribed, users will receive notifications instantly as they occur, ensuring timely communication and responsiveness.
3. **Actionable Notifications:** Notifications will be actionable, allowing users to interact with them directly from the interface. For example, clicking on a notification might open the corresponding chat room or document.

With this vision in mind, let's proceed to set up our Node.js project and lay the foundation for our real-time notification system. We'll start by configuring the project environment and installing the necessary dependencies, including RxJS, to power our reactive programming implementation.

### Project Setup: Getting Started with Node.js and TypeScript

Before we can dive into implementing our real-time notification system, we need to set up our Node.js project environment. This involves configuring TypeScript for enhanced type checking and enabling RxJS to harness the power of reactive programming. 

Let's walk through the steps to get our project up and running:

#### Step #1 – Initialize a New Node.js Project

Start by creating a new directory for your project and navigate into it:

```bash
$ mkdir real-time-notification-system
$ cd real-time-notification-system

```

Next, initialize a new Node.js project using npm or yarn:

```bash
$ npm init -y

```

or

```bash
$ yarn init -y
```

#### Step #2 – Install Dependencies

Now, let's install the necessary dependencies for our project. We'll need TypeScript for type checking and compilation, as well as RxJS for reactive programming:

```bash
$ npm install typescript rxjs

```

or

```bash
$ yarn add typescript rxjs

```

#### Step #3 – Configure TypeScript

Create a **`tsconfig.json`** file in the root of your project to configure TypeScript:

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "CommonJS",
    "outDir": "./dist",
    "strict": true},
  "include": ["src/**/*"]
}

```

This configuration sets the compilation target to ESNext, enables strict type checking, and specifies the output directory for compiled TypeScript files.

#### Step #4 – Set Up Project Structure

Create a **`src`** directory to store your TypeScript source files:

```bash
$ mkdir src

```

Your project structure should now look like this:

```markdown
real-time-notification-system/
├── src/
├── node_modules/
├── package.json
└── tsconfig.json

```

Now, create a sample TypeScript file in the **`src`** directory to verify that TypeScript is working correctly:

```tsx
// src/index.ts
const message: string = 'Hello, world!';
console.log(message);

```

To run the file, you can either use Node, or any other JS runtime like Bun, using the following command:

```bash
# make sure bun is installed with bun -v command
# then run
$ bun run src/index.ts

```

Make sure you get the “Hello, world” in the console before you proceed to the next step

#### Step #5 – Compile TypeScript

Compile your TypeScript code by running:

```bash
# then compile the project 
$ npx tsc
```

This will generate JavaScript files in the **`dist`** directory according to the configuration specified in **`tsconfig.json`**.

With our project set up and TypeScript configured, we're ready to start implementing the core features of our real-time notification system. 

Let's move on to creating observables, applying operators, and handling real-time notifications in our application.

### How to Implement the Core Features: Building a Real-Time Notification System

Now, let's dive into implementing the core features of our real-time notification system. We'll create observables to represent different types of events, apply operators to filter and transform these event streams, and finally subscribe to these observables to handle real-time notifications effectively.

#### How to Create Observables – Modeling Event Streams

In our notification system, we'll have various event streams representing different types of notifications. These could include new messages, user mentions, system alerts, and more.

Remember, everything can be observable, as this is very important when building reactive programs. Using RxJS ([https://rxjs.dev/guide/overview](https://rxjs.dev/guide/overview)), you can manipulate any kind of stream in an observable way.

Before we get started, let’s see what I mean by that.

Given a button listening to a click event, JavaScript you can capture the event like this:

```tsx
<button id='btn'>Click Me</button>

// in js file
const btn = document.getElementById("btn");
btn.addEventListener("click", (event) => {
  console.log('Button clicked');
});
```

While this works perfectly fine, it’s not reactive. What if you want to combine the click event with another event, such as a timer or an HTTP request? This is where reactive programming comes in.

With reactive programming, you can treat all of these events as streams of data and combine them in a declarative and composable way. 

Imagine a scenario where we need to print a message when two click events that happen in within a 5 seconds interval, or print a message with an array of positions the mouse occupied on the browser between two click events. Or to print a message when the user clicks on the button and the enter keyword within a 2 seconds interval. 

All these scenarios are possible with usual imperative programming but may require more tricky code, and thinking reactively may become a must. 

Let's try to build the first scenario in a usual way, then we 'll see how reactive programming can help us to make it more readable and maintainable.

```tsx
const btn = document.getElementById("btn");

let clickCount = 0;
let lastClickTime = 0;

btn.addEventListener("click", (event) => {
  clickCount++;
  if (clickCount === 1) {
    lastClickTime = new Date().getTime();
  } else if (clickCount === 2) {
    if (new Date().getTime() - lastClickTime < 5000) {
      console.log('Two clicks in less than 5 seconds');
    }
    clickCount = 0;
  }
});

```

Now let's see how we can achieve the same result using a reactive programming approach with `rxjs` in the following code snippet:

```tsx
import { fromEvent } from 'rxjs';
import { buffer, debounceTime, filter } from 'rxjs/operators';

const btn = document.getElementById("btn");
const btnClick$ = fromEvent(btn, 'click');
btnClick$.pipe(
  buffer(btnClick$.pipe(debounceTime(5000))),
  filter(clickArray => clickArray.length === 2)
).subscribe(() => {
  console.log('Two clicks in less than 5 seconds');
});

```

In the code above, we used the `fromEvent` function from `rxjs` ([https://rxjs.dev/api/index/function/fromEventPattern](https://rxjs.dev/api/index/function/fromEventPattern)) to create an observable from the click event on the button. We then used the `buffer` and `debounceTime` operators to buffer the click events and filter out the ones that occurred within 5 seconds. 

This allowed us to easily handle the scenario of two clicks occurring within 5 seconds, all in a declarative and composable way. The `$` symbol is a common notation to identify a stream, while fully optional, you may need to use it when working on a collaborative project, since it’s very common to see it.

As you can see, the reactive programming approach is much more declarative and composable, maybe not intuitive when using it the first time, but making it easier to understand and maintain. This is a very basic example, but it shows the power of reactive programming when dealing with complex event combinations. 

Reactive programming allows you to treat all events as streams of data and manipulate them in a declarative and composable way, making it easier to handle complex scenarios and maintainable code.

**⚒️ Hands on exercise:** To get more familiar, try to build the second scenario using both ways and see how you can do some complex event management using very few lines of code

Now that you have an idea of how you can turn almost anything to an observable, let’s get our hands dirty and code our sample notification system. This will be a very basic example, the goal is to show how you can benefit from reactive programming when dealing with a complex combination of events or a stream of intensive data in your future applications.

Let's start by creating observables to represent these event streams:

```tsx
// src/observables.ts
import { Observable } from 'rxjs';

// Observable for new messages
export const newMessage$ = new Observable<string>((subscriber) => {
  // Simulate receiving new messages
  setInterval(() => {
    subscriber.next('New message received');
  }, 3000);
});

// Observable for user mentions
export const userMentions$ = new Observable<string>((subscriber) => {
  // Simulate user mentions
  setInterval(() => {
    subscriber.next('You were mentioned in a message');
  }, 5000);
});

// Observable for system alerts
export const systemAlerts$ = new Observable<string>((subscriber) => {
  // Simulate system alerts
  setInterval(() => {
    subscriber.next('System alert: Server down');
  }, 10000);
});

```

In the code above, we have created three observables using the `Observable` class from `rxjs` ([https://rxjs.dev/guide/observable](https://rxjs.dev/guide/observable)): `newMessage$`, `userMentions$`, and `systemAlerts$`. 

Each of these observables emit a new value at different intervals. The `newMessage$` observable emits a new message every 3 seconds, the `userMentions$` observable emits a new message every 5 seconds, and the `systemAlerts$` observable emits a new message every 10 seconds. Now that we have our observables set up, we can subscribe to them and handle the emitted values in our application.

#### How to Apply Operators – Transforming Event Streams

Next, let's apply operators to filter and transform our event streams to generate actionable notifications. We'll use operators like **`filter`**, **`map`**, and **`merge`** to process incoming data streams and generate meaningful notifications:

```tsx
// src/operators.ts
import { newMessage$, userMentions$, systemAlerts$ } from './observables';
import { merge, map, filter } from 'rxjs';

// Combine multiple event streams into one
export const combinedNotifications$ = merge(
  newMessage$.pipe(map(message => `New message: ${message}`)),
  userMentions$.pipe(map(mention => `You were mentioned: ${mention}`)),
  systemAlerts$.pipe(map(alert => `System alert: ${alert}`))
);

// Filter notifications based on user preferences
export const filteredNotifications$ = combinedNotifications$.pipe(
  filter(notification => notification.startsWith('New message'))
);

```

In the code above, we have created three observables: `newMessage$`, `userMentions$`, and `systemAlerts$`. Each of these observables emit a new value at different intervals. The `newMessage$` observable emits a new message every 3 seconds, the `userMentions$` observable emits a new message every 5 seconds, and the `systemAlerts$` observable emits a new message every 10 seconds.

#### How to Handle Real-Time Notifications – Subscribing to Observables

Finally, let's subscribe to our observables to handle real-time notifications in our application. We'll subscribe to the combined notifications stream and display notifications to the user in a simulated client interface:

```tsx
// src/index.ts
import { combinedNotifications$, filteredNotifications$ } from './operators';

// Subscribe to combined notifications and display them in the UI
combinedNotifications$.subscribe(notification => {
  // Simulate displaying notifications in the UI
  console.log('Displaying notification:', notification);
});

// Subscribe to filtered notifications based on user preferences
filteredNotifications$.subscribe(notification => {
  // Simulate displaying filtered notifications in the UI
  console.log('Displaying filtered notification:', notification);
});

```

In the code snippet above, we have created two observables: `combinedNotifications$` and `filteredNotifications$`. The first one combines multiple event streams into one using the merge operator. The second one filters notifications based on user preferences using the filter operator. We then subscribe to these observables and display the notifications in the UI.

Let’s test things out again using `bun`:

```bash
$ bun run src/index.ts

```

You should have the following output:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-14-at-16.02.15.png)
_Figure 3: terminal output when running the project_

As you can see, the notifications are being displayed in the UI as expected, and they keep coming in as new events are emitted, untill the program is stopped. 

Another way to stop getting notifications is to unsubscribe from the observables, adding a condition that will execute the following block:

```tsx
combinedNotifications$.unsubscribe();

```

⚒️  **Over to you:**  
Feel free to interact with the code and explore how observables and operators work together to handle real-time notifications effectively. Experiment with different event streams and filters to tailor the notifications to your preferences, making sure you get to use as more RxJS operators as possible. As you code along, consider real-world use cases and how this notification system can be applied to various applications.

You can find the full source code for this article at the following GitHub repo: [https://github.com/pacyL2K19/rx-programming-real-time-sample](https://github.com/pacyL2K19/rx-programming-real-time-sample). Kindly leave a star if you find it helpful.

## Best Practices and Common Pitfalls

Reactive programming is a powerful paradigm, but it comes with its own set of best practices and potential pitfalls. 

Let's explore some key considerations when working with reactive programming in real-world applications:

### Best Practices:

Here are are some of the best practices you need to follow when building application in a reactive way:

* **Declarative and Composable:** Leverage the declarative and composable nature of reactive programming to handle complex event streams and data flows. Use operators to transform and combine observables in a clear and maintainable way.
* **Error Handling:** Implement robust error handling mechanisms to manage exceptions or failures in your event streams. Use operators like `catchError` ([https://rxjs.dev/api/operators/catchError](https://rxjs.dev/api/operators/catchError)) or `retryWhen` ([https://rxjs.dev/api/index/function/retryWhen](https://rxjs.dev/api/index/function/retryWhen)) to handle errors gracefully.
* **Memory Management:** Be mindful of memory management when working with observables. Unsubscribe from observables when they are no longer needed to avoid memory leaks and unnecessary resource consumption.
* **Testing:** Write comprehensive unit tests for your observables and operators to ensure they behave as expected. Use testing libraries like `Jest` or `Mocha` to test your reactive code.

### Common Pitfalls:

* **Overusing Operators:** Avoid overusing operators, especially in complex event streams. While managing complex data/event streams can lead to using more than one operator, an overuse of operators can lead to code that is difficult to understand and maintain, always seek for an optimal use of operators.
* **Complexity:** Be cautious of overly complex event streams and data flows. Strive to keep your reactive codebase simple and intuitive to avoid confusion and bugs.
* **Performance:** Keep an eye on performance when working with reactive programming. Intensive data processing and complex event combinations can impact performance if not managed carefully, especially knowing when to subscribe and when to unsubscribe from observables, making sure the resources are used optimally.

By following best practices and being aware of common pitfalls, you can harness the full potential of reactive programming while ensuring the maintainability and performance of your applications.

## Conclusion

Reactive programming is a transformative paradigm that empowers developers to build responsive, scalable, and efficient applications. By leveraging the principles of streams, observables, and operators, developers can handle complex data flows and asynchronous operations with ease. 

Whether you're building real-time dashboards, IoT applications, or financial trading platforms, reactive programming provides a versatile and powerful toolkit for handling dynamic data streams. As you continue your journey with reactive programming, remember the core concepts of streams and observables.

Embrace the declarative and composable nature of reactive programming, and explore the vast array of operators available to transform and combine observables. By doing so, you'll unlock the full potential of reactive programming and create applications that meet the demands of modern software development.

### Resources

* [Reactive programming and its effect on performance and the development process](https://lup.lub.lu.se/luur/download?func=downloadFile&recordOId=8932146&fileOId=8932147) By Gustav Hochbergs
* [The introduction to Reactive Programming you've been missing](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) By André Staltz
* [The fight for performance](https://devm.io/java/the-fight-for-performance-157515) By Arne Limburg
* [Introduction to reactive programming](https://developer.ibm.com/series/learning-path-introduction-to-reactive-systems/) by IBM

