---
title: 'When to use TypeScript: a detailed guide through common scenarios'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T17:23:29.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-typescript-a-detailed-guide-through-common-scenarios-b0a57e57905
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ygOV4sntqZDN8t7u9n-MGw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: software design
  slug: software-design
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Khalil Stemmler

  Strap yourself in. In this guide, we compare when it’s absolutely vital to be using
  TypeScript, the strictly-typed programming language, and when it makes sense to
  stick to vanilla JavaScript

  Have you heard of that little programmi...'
---

By Khalil Stemmler

_Strap yourself in. In this guide, we compare when it’s absolutely vital to be using TypeScript, the strictly-typed programming language, and when it makes sense to stick to vanilla JavaScript_

Have you heard of that little programming language called **TypeScript**? You know, the one that Microsoft made? The one that’s kinda [blowing up](https://redmonk.com/sogrady/2019/03/20/language-rankings-1-19)?

Maybe you were like me, a true JavaScript purist. I was doing _just fine_ building things with React and Node without types. Prop types and [Joi validation](https://github.com/hapijs/joi) have been treating me just nicely, thank you.

Maybe you caved at some point and gave it a shot. Started playing with it. Maybe you hated it because it reminded you of Java. Maybe you got annoyed with how you couldn’t be super productive right away.

These were some of **my own initial sentiments** when I first started with TypeScript.

I certainly didn’t see the benefit… up until I started experiencing some really annoying stuff. Things like builds not failing when they should, buggy code and typos finding their way into production code somehow in addition to finding it increasingly challenging to express my designs in a really clean object-oriented way.

9 months later into using TypeScript, I’ve built new features in Angular apps for clients, I began compiling [Univjobs](https://univjobs.ca)'s React / Redux front-end with TypeScript and ported all of our backend services to TypeScript from vanilla Node.js, refactoring mass amounts of code along the way.

In this article, we’ll take a look at some of the most common scenarios and identify when it might be vital to use TypeScript, and when we could probably just do without it and stick to _vanilla_ JS.

### Why this discussion matters today more than ever

I’ve come to the very important conclusion that depending on your situation, context, project, skill level, and other factors, that it’s actually **dangerous** for your project to **NOT** be using TypeScript today.

The front-end space, for one, is getting more and more complex. Certain features that were once considered bleeding-edge, are now very much standard user experience assumptions.

For example, it’s almost always expected that your app is still going to work offline in some capacity. And when users ARE online, it’s also usually expected that they’re going to get real-time notifications without having to refresh the page.

These are some pretty steep (but definitely not unrealistic in 2019) demands.

Before we dive into different scenarios, we should actually talk about the three categories of really hard software problems to be solved.

### 3 Categories of Hard Software Problems

Generally speaking, there are three of these. The Performant System Problem, the Embedded System Problem, and the Complex Domain Problem.

#### 1. The Performant System Problem

Let’s talk about Twitter for a sec.

Twitter is actually a really simple concept.

You sign up, you make tweets, you like other people’s tweets and that’s pretty much it.

If Twitter is that simple, why couldn’t someone else do it?

It’s apparent that the real challenge for Twitter is not actually so much as **what it does**, but it’s **how it’s able to do what it does**.

Twitter has the unique challenge of serving requests from approximately **500 million users every single day**.

The hard problem that Twitter solves is actually a _performance problem_.

When the challenge is performance, whether or not we use a strictly typed language is much less important.

#### 2. The Embedded System Problem

An embedded system is a combination of computer hardware and software, with the purpose of enabling control over the mechanical or electrical aspects of a system.

Most systems we use today are built on a very complex layer of code that, if not initially written in, compiles down to C or C++ usually.

Coding in these languages is not for the faint of heart.

In C, there is no such thing as objects; and we as humans like objects because we can easily understand them. C is procedural and this makes the code that we have to write in this language more challenging to keep clean. These problems also require knowledge of the lower-level details.

C++ does make life a whole lot better because it has object orientation, but the challenge is still fundamentally interacting with lower-level hardware details.

Because we don’t really have that much of a choice on the languages we use for these problems, so it’s irrelevant to consider TypeScript here.

#### 3. The Complex Domain Problem

For some problems, that challenge is less about scaling in terms of handling more requests, but scaling in terms of **the codebase’s size**.

Enterprise companies have **complex real-life problems** to be solved. In these companies, the biggest engineering challenges are usually:

* Being able to **logically** (domains) separate parts of that monolith into smaller apps. And then, **physically** (microservices for bounded contexts) splitting them up so that teams can be assigned to maintain them
* Handling integration and synchronization between these apps
* Modeling the domain concepts and actually solving the problems of the domain
* Creating a _ubiquitous_ (all-encompassing) language to be shared by developers and domain experts
* Not getting lost in the mass amounts of code written and slowing down to the point where it becomes impossible to add new features without breaking existing ones

I’ve essentially described the types of problems that [Domain-Driven Design](https://khalilstemmler.com/articles/domain-driven-design-intro/) solves. For these types of projects, you wouldn’t even think about not using a strictly-typed language like TypeScript.

#### Object-oriented JavaScript

For **Complex Domain** problems, if you don’t choose TypeScript and instead, choose JavaScript, it will require some extra effort to be successful. Not only will you have to be **extra comfortable** with your object modeling abilities in vanilla JavaScript, but you’ll also have to know how to utilize the 4 principles of object-oriented programming (encapsulation, abstraction, inheritance, and polymorphism).

This can be **hard to do**. JavaScript doesn’t naturally come with concepts of interfaces and abstract classes.

“Interface Segregation” from the SOLID design principles isn’t easily achievable with vanilla JavaScript.

Using JavaScript alone would also require a certain level of discipline as a developer in order to keep the code clean, and this is vital once the codebase is sufficiently large. You’re also left to ensure that your team shares the same discipline, experience and knowledge level on how to implement common design patterns in JavaScript. If not, you’ll need to guide them.

In Domain-Driven projects like this, the strong benefit from using a strictly typed language is **_less_** about expressing **_what can be done_**, but more about using encapsulation and information hiding **to reduce the surface area of bugs** by limiting what domain objects are **_actually allowed to do_**.

We can live without this on the front-end, but it’s a **hard language requirement for the** **backend** in my books. It’s also the reason why I moved my Node.js backend services to TypeScript.

There’s a reason why TypeScript is called “**JavaScript that scales**”.

Out of all three categories of hard software problems, only the Complex Domain Problem is the one where TypeScript is an absolute necessity.

Besides this, there are other factors that might determine when it’s best to use TypeScript for your JavaScript project.

### Code size

Code size usually ties back to the **Complex Domain Problem**, where a large codebase means a complex domain, but that’s not always the case.

When the amount of code a project has gets to a certain size, it becomes **harder** to keep track of everything that exists and becomes **easier** to end up re-implementing something already coded.

**Duplication is the enemy to well-designed and stable software.**

This is especially heightened when new developers start coding on an already large codebase.

Visual Studio Code’s autocompletion and Intellisense helps to navigate through huge projects. It works really well with TypeScript, but it’s somewhat limited with JavaScript.

For projects that I know will stay simple and small, or if I know that it will be thrown away eventually, I would be less pressed to recommend TypeScript as a necessity.

### Production software vs. pet projects

**Production software** is code that you care about or code that you’ll get in trouble for if it doesn’t work. This is also code that you’ve written tests for. The general rule of thumb is that “if you care about the code, you need to have unit tests for it”.

If you don’t care, don’t have tests.

**Pet projects** are self-explanatory. Do whatever you like. You have no professional commitment to uphold any standards of craftsmanship whatsoever.

Go on and make things! Make small things, make big things.

Maybe someday you’ll experience the pain when your pet project turns into your main project which turns into production software, which is buggy because it didn’t have tests or types ? not like I’ve been there or anything…

#### Lack of Unit Tests

It’s not always possible to have tests for everything, because, well — **life**.

In that case, I’d say that if you don’t have Unit Tests, the next best thing you could have is compile-time checking with TypeScript. After that, if you’re using React, the next best is thing is to use runtime checking with Prop types.

However, compile-time checking is **not a substitute** for having unit tests. The good thing is that unit tests can be written in any language — so the argument for TypeScript here is irrelevant. What’s important is that tests are written and we are confident about our code.

### Startups

Definitely use whatever helps you be most productive.

At this time, the language you choose matters a lot less.

The most important thing for you to do is to **validate your product**.

Choosing a language (Java, for example) or a tool (like Kubernetes) that you heard would help you scale in the future (while being totally unfamiliar with it) may or may not be the best option in the case of a startup.

Depending on how early you are, the most important thing for you to do is to be productive.

In Paul Graham’s famous article, [The Python Paradox](http://www.paulgraham.com/pypar.html), his main point is that startup engineers should just use the technology that maximizes their productivity.

Overall, in this case, use whatever you’re most comfortable with: types or no types. You can always refactor towards a better design once you know you’ve built something people actually want.

### Working on Teams

Depending on the size of your team and the frameworks you’re using, using TypeScript might be a make or break kind-of-thing.

#### Large teams

When teams are sufficiently large (because the problems are sufficiently large), it’s a good reason to use an opinionated framework, like Angular for the front-end, and TypeScript for the backend.

The reason why using an opinionated framework is beneficial is because you limit the number of possible ways for people to accomplish something. In Angular, there’s pretty much one main way to add a Route Guard, use Dependency Injection, hook up Routing, Lazy-Loading, and Reactive Forms.

The huge benefit here is that the API is well specified.

With TypeScript, we also save massive amounts of time and make communication efficient.

The ability to quickly determine the required arguments and its return type for any method, or the ability to explicitly describe program intent through public, private, and protected variables alone is incredibly useful.

Yes, some of this is possible with JavaScript, but it’s hacky.

#### Communicating patterns & implementing design principles

Not only that, but **design patterns**, the solutions to commonly occurring problems in software, are more easily communicated through explicit strictly-typed languages.

Here’s a JavaScript example of a common pattern. See if you can identify what it is.

```js

class AudioDevice {
  constructor () {
    this.isPlaying = false;
    this.currentTrack = null;
  }

  play (track) {
    this.currentTrack = track;
    this.isPlaying = true;
    this.handlePlayCurrentAudioTrack();
  }

  handlePlayCurrentAudioTrack () {
    throw new Error(`Subclasss responsibility error`)
  }
}

class Boombox extends AudioDevice {
  constructor () {
    super()
  }

  handlePlayCurrentAudioTrack () {
    // Play through the boombox speakers
  }
}

class IPod extends AudioDevice {
  constructor () {
    super()
  }

  handlePlayCurrentAudioTrack () {
    // Ensure headphones are plugged in
    // Play through the ipod
  }
}

const AudioDeviceType = {
  Boombox: 'Boombox',
  IPod: 'Ipod'
}

const AudioDeviceFactory = {
  create: (deviceType) => {
    switch (deviceType) {
      case AudioDeviceType.Boombox:
        return new Boombox();
      case AudioDeviceType.IPod:
        return new IPod();
      default:
        return null;
    }
  } 
}

const boombox = AudioDeviceFactory
  .create(AudioDeviceType.Boombox);

const ipod = AudioDeviceFactory
  .create(AudioDeviceType.IPod);
```

If you guessed **Factory Pattern**, you’re right. Depending on your familiarity with the pattern, it might not have been that obvious to you.

Let’s look at it in TypeScript now. Look at how much more intent we can signify about **AudioDevice** in TypeScript.

```js
abstract class AudioDevice {
  protected isPlaying: boolean = false;
  protected currentTrack: ITrack = null;

  constructor () {
  }

  play (track: ITrack) : void {
    this.currentTrack = track;
    this.isPlaying = true;
    this.handlePlayCurrentAudioTrack();
  }

  abstract handlePlayCurrentAudioTrack () : void;
}
```

**Immediate improvements**

* We know the class is abstract **right away**. We needed to sniff around in the JavaScript example.
* **AudioDevice** can be instantiated in the JavaScript example. This is bad, we intended **AudioDevice** to be an abstract class. And abstract classes shouldn’t be able to be instantiated, they’re only meant to be subclassed and implemented by [concrete classes](https://khalilstemmler.com/wiki/concrete-class/). This limitation is set in place correctly in the TypeScript example.
* We’ve signaled the scope of the variables.
* In this example, **currentTrack** refers to an interface. As per the [Dependency Inversion](https://khalilstemmler.com/wiki/dependency-inversion/) **design principle,** we should always depend on abstractions, not concretions. This isn’t possible in the JavaScript implementation.
* We’ve also signaled that any subclasses of **AudioDevice** will need to implement the **handlePlayCurrentAudioTrack** themselves. In the JavaScript example, we exposed the possibility for someone to introduce runtime errors trying to execute the method from either the illegal abstract class or the non-complete concrete class implementation.

Takeaway: If you work on a large team and you need to minimize the potential ways someone could misuse your code, TypeScript is a good way to help fix that.

### Smaller teams & coding styles

Smaller teams are a lot easier to manage coding styles and communication. Paired with linting tools, frequent discussions about how things will get done and pre-commit hooks, I think small teams can be really successful without TypeScript.

I think that success is an equation involving the size of the codebase and the size of the team.

**As the codebase grows**, the team might find that they need to rely on some help from the language itself to remember where things are and how they should be.

**As the team grows**, they might find they need more rules and restrictions to keep the style consistent and prevent duplicate code.

### Frameworks

#### React & Angular

Much of what draws me and other developers to React is the ability to write code however you want and in an elegant/clever way.

It’s true that React makes you a better JavaScript developer because it forces you to approach problems differently, it forces you to be aware of how **this binding** in JavaScript works and enables you to compose large components out of small ones.

React also allows you to have a bit of your own style. And because of the number of ways I can implement any given task, I will most often write vanilla React.js apps when:

* the codebase is small
* it’s just me coding it

And I will compile it with TypeScript when:

* more than 3 people are coding it, or
* the codebase is expected to be very large

I will also optionally use Angular for the same reason I will compile React with TypeScript.

### Conclusion

In conclusion, these are my personal opinions on when TypeScript is absolutely necessary and I welcome you to disagree with any of it.

This is what has worked for me in the past when deciding whether or not to use TypeScript. However, today, since I’ve seen the light, it’s not much more effort for me to use TypeScript over vanilla JavaScript as I’m equally comfortable with both and would prefer the type safety.

My final points here are:

#### You can always gradually start using TypeScript

Start gradually by adding TypeScript and ts-node to your package.json and utilizing the **allowjs: true**, option in your tsconfig file.

This is how I migrated all of my Node.js apps over time to TypeScript.

#### Compile time errors are better than runtime ones

You can’t argue with that. If catching bugs in production code is especially important to you, TypeScript will help you minimize a lot of these.

#### If you are in a position to learn it, learn it. It does wonders for your software design skills

Depending on where you are in your life and your career, you might not have the time to learn it. If you do have the time, I’d recommend you start learning it and start learning about **SOLID design principles** and **software design patterns**. This is the **fastest way to level up as a Junior Developer** in my honest opinion.

I hope this article was useful to you! Are you considering using TypeScript on your next project? Let me know if you agree/disagree in the comments.

#### [Learn Enterprise TypeScript & JavaScript](https://khalilstemler.com)

Essential software development patterns, principles, and tutorials with modern JavaScript and TypeScript.

> Originally published [April 6th](http://khalilstemmler.com) @ [**khalilstemmler.com**](https://khalilstemmler.com)**.**

