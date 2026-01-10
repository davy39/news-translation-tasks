---
title: A comparison between Angular and React and their core languages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T22:47:25.000Z'
originalURL: https://freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2FNo1Wxk0kZX0QoH.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dler Ari

  In this article, we will compare two of the most popular web technologies in 2019,
  and also address their history, key differences, core languages recommended (TypeScript
  and JavaScript) and so forth. Overall, these technologies have made...'
---

By Dler Ari

In this article, we will compare two of the most popular web technologies in 2019, and also address their history, key differences, core languages recommended (TypeScript and JavaScript) and so forth. Overall, these technologies have made it much easier for developers to reuse, refactor, and maintain code by dividing things into modules/components.

The goal of this article is not to find the best technology, but to compare, highlight, and clarify few misconceptions. We’ll also focus on what is important instead of minor details that do not really matter in the long-term.

You should be aware that the comparison between these two technologies cannot be fully covered. Angular comes with a complete framework (MVC), while React is a fronted-library with lots of open-source packages to integrate with.

> If you want to become a better web developer, start your own business, teach others, or simply improve your development skills, subscribe to my newsletter to get latest web news and updates.

### Questions to be addressed

* What are the key differences between Angular and React?
* What makes TypeScript so special?
* How popular are these technologies?
* What is the current open-source status?
* Which technology do companies use the most?
* Do static typed languages influence code quality and development time?

Future sections will be added based on demand from the comments.

### Key comparisons

Here’s a quick side-to-side comparison between Angular (left) and React (right).

![Image](https://cdn-media-1.freecodecamp.org/images/1*w9DLq-pSxDGabNxUzawN_w.png)
_Angular and React_

One thing that is really great about React in terms of performance is the Virtual DOM, which you’ve probably heard about a couple of times. If not, don’t worry, I’ll explain it!

**Problem**  
Let’s say you want to update a user’s birth date within a block of HTML tags.

**Virtual DOM**  
It only updates the part that is required by seeing the differences between the previous and current HTML version. Its a similar approach to how GitHub operates when detecting changes in the file.

**Regular DOM**  
It will update the whole tree structure of HTML tags until it reaches the birth date.

#### Why does it matter?

It may not matter for the problem described above. However, if we deal with 20–30 asynchronous data requests on the same page (and for every page request we replace the whole HTML block), it will influence performance as well as user-experience.

Need more context? Check out [Dace](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/undefined)’s [article!](https://medium.com/@hidace/understanding-reacts-virtual-dom-vs-the-real-dom-68ae29039951)

But first, back to the beginning…

### History

We’ll need to know a bit of history (context) because it provides insight into how things may shape up in the future.

> _I will not go into the details of what exactly happened between Angular and AngularJS, and I’m sure there are lots of resources available that [cover it](https://www.angularjswiki.com/angularjs/history-of-angularjs/). But in short, Google replaced AngularJS with Angular, and JavaScript with TypeScript._

Alright, so back in the days with ES4/ES5, the learning-curve for JavaScript was really high. If you came from the world of Java, C# or C++, a world of object-oriented programming (OOP), then learning JavaScript was simply not that intuitive. In other words, it was a pain in the ass.

It’s not because the language was poorly written, but because it has a different purpose. It was built to handle the asynchronous nature of the web, such as user interaction, event-binding, transitions/animations, and so forth. It’s a different animal with different instincts.

### Popularity

As Google Trends reveal, Angular and React are two of the most popular web technologies in 2019.

Angular has more search hits than React, however it does not necessarily mean that one is better than the other. But this indicates what people find interesting, whatever the reason may be. It’s important to be aware that people may mix between keywords such as AngularJS or Angular, and thus lead to higher search hits.

One thing is for sure — both technologies are growing, and the future looks bright. That means you don’t have to worry if one technology will fail, and leave you behind.

It’s important that we do not neglect history in terms of what happened between AngularJS and Angular, because history is a form of indication on what may happen in the future. But if you have some experience with Angular and AngularJS, then you’ll most likely see why the decisions was made for the better. Just to mention, such things can happen to any frameworks out there, including React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QHPY_nB9Gvx0pNNPtPqUiQ.png)
_Google Trends Angular vs React_

#### Open-source

React has over 100,000 stars, along with 1200 contributors and close to 300 issues waiting to be resolved.

React has an a time-to-market advantage, since it was released 3 years prior to Angular. And that means it has faced lots real-world problems, gone through critical tests, and overall has developed into an adaptable and flexible fronted-library which many love.

When it comes to Angular, at first glance, we can clearly see that Angular has 6 times more issues than React (not good). However, we must not forget that Angular is a much larger framework, and also has fewer developers using it (currently) because it was released in 2016.

![Image](https://cdn-media-1.freecodecamp.org/images/1*peSbHEIzoh41XzjjEcyaOQ.png)
_Angular and React — Github popularity_

> Stats taken from [Angular](https://github.com/angular/angular) and [Reacts](https://github.com/facebook/react) GitHub page.

### What companies are using

React was initially developed at Facebook for Facebook to optimize and ease the development of components. An article written by [Chris Cordle](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/undefined) points out that React has a higher usage at Facebook than Angular has at Google.

So who uses which technology?

#### [# React](https://github.com/facebook/react/wiki/Sites-Using-React)

* Facebook
* AirBnb
* Uber
* Netflix
* Instagram
* Whatsapp
* Dropbox

#### [# Angular](https://www.madewithangular.com/categories/angular)

* Eat24
* CVS shop
* onefootball
* Google Express
* NBA
* Delta
* wix.com

> _If you know of any large (well-known) companies using Angular, please share with a link._

### TypeScript and JavaScript (ES6+)

As I mentioned, it can be misleading to only compare Angular and React without focusing on the core language each one has emphasizes (according to their docs).

> Note! The aim this section is not to decide whether we’ll choose Angular or React. But clarify few misconceptions between statically- vs dynamically-typed languages that has been going on for a while, backed with research.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VgrihKGD-D8TdfX1CTAB-A.png)
_TypeScript (left) vs JavaScript (right)_

In terms of user base, JavaScript is superior. But TypeScript is rapidly increasing, so who knows what 10–15 years will bring.

#### TypeScript popularity in the past 5 years

![Image](https://cdn-media-1.freecodecamp.org/images/1*cRXezTFmwhdPEmXX7eMCQA.png)
_Google Trends — TypeScript popularity_

#### JavaScript popularity in the past 5 years

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ga66wSTNP6w1MT6JRbfYjA.png)
_Google Trends —JavaScript popularity_

#### JavaScript vs TypeScript popularity in the past 5 years

![Image](https://cdn-media-1.freecodecamp.org/images/1*axNBATWdEu5lNC9zcL2Fug.png)
_Google trends — TypeScript and JavaScript popularity_

TypeScript was initially developed by Microsoft to make JavaScript easier (in other words, to make ES5 easier). It was released in October 2012. And it is simply a transpiler that compiles TypeScript to JavaScript code, which also means you can write ES5 code in a TypeScript file. TypeScript is referred to as a superset of JavaScript.

In general, TypeScript provides a smooth transition for programmers with an object-oriented programming (OOP) background. It is important to notice that TypeScript was released in the period of ES5, and during that time, ES5 was not a class-based OOP language.

In short, the closest you could come to classes and objects back then was through prototype inheritance. And as we know, this was a difficult transition for most developers with an OOP background. So the ideal decision was of course choosing something you felt comfortable and familiar with, which was likely TypeScript.

However, in the past years, JavaScript has evolved and implemented lots of great changes such as modules, classes, spread operators, arrow functions, template literals and so on. Overall, it allows developers to write declarative code, while supporting the characteristics of a true OOP language (that is, including class-based structure).

#### Statically and Dynamically-typed languages

A statically typed language basically means that you can define the variable type (string, number, or array etc). You may ask why this is important. Here’s a real world analogy I’ve setup (creativity at its best).

Let’s say you want to refuel your car with gas. One thing that is important is to fuel with the right gas — petrol or diesel. And if you don’t know, you may need to buy a new car.

Of course, the severity is not like that with coding, however, in some cases it may be. Think about it. If you work with a large application, you would like to know the argument and property type that is passed, otherwise you may break the code.

Alright, so if you are still confused what statically typed means, check this out:

#### Static typed property

![Image](https://cdn-media-1.freecodecamp.org/images/1*mY3mIKr4VVX2Dfdd44klqA.png)
_Static typed property comparison between JavaScript and TypeScript_

#### Static typed argument

![Image](https://cdn-media-1.freecodecamp.org/images/1*wp-KxiqHmsplvH9R9jf84g.png)
_Static typed argument comparison between JavaScript and TypeScript_

I’ve learned that lots of people believe that a statically typed language means reliable code, and is most often used as a winning argument over dynamically typed languages. And frankly, it is quite difficult to disprove this statement because it fundamentally relies on the development environment, the programmers experience and of course the project requirements.

Luckily, [research](https://courses.cs.washington.edu/courses/cse590n/10au/hanenberg-oopsla2010.pdf) (tl;dr [video](https://vimeo.com/74354480)) has taken this seriously, and put this myth to test with 49 subjects.

#### The observations from the research are:

* Statically typed language require more time due to fixing typo errors
* Dynamically typed language is readable and easier to write (declarative code)

![Image](https://cdn-media-1.freecodecamp.org/images/1*bshGBQgntp2lz78ZZENNLA.png)

Figure 5 shows that, on average, developers reduce their development time by a factor of two when writing a dynamically typed language.

If you want to dig deeper into this topic, I suggest reading this article by [Eric Elliott](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/undefined) which states that you may not need TypeScript (or statically typed languages).

#### What to choose

So the question is not only about what Angular or React offers, but also about what core language you should invest time on. And it does not really matter as long you choose something that fits your requirements and complexity.

If you are not a fan of types, then there is nothing standing in your way of writing ES6 code in TypeScript. It’s just that if you need it, then it is there.

But if you build a fairly large front-end application with Angular dealing with many HTTP requests, then having types really helps with questions such as “What type of object is this, what fields can I use, and what type is this field etc”. It works great for collaboration and clarifying small things.

Here is a simple class-object comparison between TS and JS (ES6).

![Image](https://cdn-media-1.freecodecamp.org/images/1*hlNk4pSA_NOAyUclRxAkFw.png)
_TypeScript_

![Image](https://cdn-media-1.freecodecamp.org/images/1*AqwhtWGVeDmOqf_J0_vCGg.png)
_JavaScript (ES6)_

#### IMO

Statically typed feels structured, secure, readable, and easy to collaborate with others (prevents people from passing unexpected values). However, when working with dynamically typed, I have the flexibility and creativity to focus more on creating than thinking to much about types, interfaces and generics and so forth.

And from the past web-apps I’ve built, I haven’t really had any large issues with not having static typed. It does not mean I don’t like it — I just that I don’t need it, but maybe I do in the future.

Here’s an update — currently I’m working with a couple of Microsoft developers to build an application using Angular framework. The reason we’ve selected Angular is because most of the packages are already defined, and the documentation for everything is in one place. It also emphasizes on TypeScript, which is a perfect choice because the majority of devs have already lots of experience with object-oriented programming.

On the other hand, I’ve seen similar apps we are working with built with React. So in general, both are powerful tools, and mostly rely on how you setup the architecture.

### Takeaway notes

* TypeScript is simply a transpiler, it can be used with React or any other JS frameworks
* React handles memory-management efficiently (virtual DOM)
* React uses JavaScript (ES6), a recognized web-language since 1995
* Angular uses TypeScript, released in 2012
* Statically typed language is great, but its not a must
* Dynamically typed languages require less time to write and more flexibility to use creativity
* Learning statically-typed language may be a challenge, especially if you’ve only been working with dynamically typed languages
* ES6 has implemented lots of great features such as modules, classes, spread operator, arrow functions, template literals that allows you to write less, cleaner and more structured code (syntactic sugar)
* TS is simply ES6+ with types and much more

### Conclusion

The framework/component-library you choose may influence how much time you spend programming and your budget. If you have a team with C#, Java or C++ developers, then I would probably go for Angular, since TypeScript shares many similarities with these languages.

The best recommendation I can offer is to setup a basic application both in Angular and React, and then evaluate the language and work flow before you make a decision.

As previously mentioned, both technologies have their own set of advantages and similarities, and it really boils down to **what type of requirements the application offers, the complexity and level of experience the developers have.**

Here are a few articles I’ve written about the web-ecosystem along with personal programming tips and tricks.

* [A chaotic mind leads to chaotic code](https://medium.freecodecamp.org/a-chaotic-mind-leads-to-chaotic-code-e7d6962777c0)
* [Developers that constantly want to learn new things](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4)
* [A practical guide to ES6 modules](https://medium.freecodecamp.org/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [Learn these core Web Concepts](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)
* [Boost your skills with these important JavaScript methods](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [Program faster by creating custom bash commands](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

You can find me on Medium where I publish on a weekly basis. Or you can follow me on [Twitter](http://twitter.com/dleroari), where I post relevant web development tips and tricks along with personal stories.

_P.S. If you enjoyed this article and want more, please clap ❤ and share with friends that may need it, it’s good karma._

