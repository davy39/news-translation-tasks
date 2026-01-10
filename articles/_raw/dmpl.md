---
title: An Introduction to Task-Oriented Programming
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-23T14:54:33.000Z'
originalURL: https://freecodecamp.org/news/dmpl
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/mars.jpeg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: programming languages
  slug: programming-languages
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nishant Shukla

  Vehicles on Mars autonomously self-regulate, plan, and navigate using software packaged
  up in millions of lines of C. Now, if hardware limitations were not a concern, what
  language would you choose to write the logic, decision-flow,...'
---

By Nishant Shukla

Vehicles on Mars autonomously self-regulate, plan, and navigate using software packaged up in [millions of lines of C](https://softwareengineering.stackexchange.com/questions/159637/what-is-the-mars-curiosity-rovers-software-built-in/159638#159638). Now, if hardware limitations were not a concern, what language would you choose to write the logic, decision-flow, and reasoning for an extraterrestrial robot? 

Some prefer the brevity of Python, while others appreciate the robustness of Rust, but picking a language for a project has deep consequences. [Just ask any linguist](http://www.inf.ed.ac.uk/teaching/courses/inf1/fp/lectures/2012/lect01.pdf): 

<blockquote>
    "Language shapes the way we think, and determines what we can think about." <br/> – Benjamin Lee Whorf; pioneered linguistic relativity
</blockquote>

<blockquote>
    "The limits of my language mean the limits of my world." <br /> – Ludwig Wittgenstein; mathematician, logician, and philosopher
</blockquote>

<blockquote>
    "A language that doesn’t affect the way you think about programming, is not worth knowing." <br /> – Alan Perlis; first recipient of the Turing Award
</blockquote>
        


There's no one-size-fits-all when it comes to programming languages, so it's worth expanding our horizon by studying what's out there. 

Categorizing the thousands of programming languages that exist is no easy task, but software trends over the years have revealed two sovereign frameworks: imperative (object-oriented) and declarative (functional) languages. 

* ==**Imperative**:== The programmer defines how to perform algorithms and how memory is accessed. Examples include C++, JavaScript, and Python.


* ==**Declarative**:== The programmer defines the composition  of functions, and lets the run-time optimize algorithms. Examples include Haskell, Erlang, and OCaml.

A classic way to describe the distinction between declarative and imperative programming is that declarative languages let the programmer describe **what** to do, whereas imperative languages let the programmer define **how** to do it. 

If we extend this idea to a third type of language that lets the programmer define **why** choices are made, then we have discovered task-oriented programming languages. 

* ==**Task-oriented**:== The programmer defines desired states,  and lets the runtime resolve the composition of actions. Examples include DMPL, PDDL, and DTProbLog.

The figure below summarizes these paradigms with glorious details about how languages have influenced each other over the years. The types of languages are all over the place, and it all started less than a century ago!  

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-7.png)
_Arrows between languages represent influence. Languages are placed in columns corresponding to their primary paradigm, even though some languages are multi-paradigm. For a more robust breakdown, please see Figure 1. Genealogy of Programming Languages, from Farooq et. al. ([https://doi.org/10.1371/journal.pone.0088941](https://doi.org/10.1371/journal.pone.0088941))_

Task-oriented languages bring a new perspective to the way we think about code. In this article, we'll cover exactly what the means. 

The following section below distills what makes some languages so popular today (and why popularity may not be a good indicator for choosing one language over another). 

The subsequent section walks through implementing an algorithm in the different paradigms. 

We then conclude with a discussion on what each paradigm does exceptionally well.

## Why stick with a language?

Of the thousands of programming languages out there, you may be wondering what sets your favorite language apart from a freshly minted one. Typically, what locks developers in is a combination of the following factors:

* **APIs/frameworks:** Sometimes you just really need to use a library that's not widely available in many languages. OpenCV, for example, is a computer vision library that pairs exceptionally well with C++ or Python, but has limited support for some other languages, such as Elixir. 
* **Learning curve:** Some languages take years of study to master, such as Haskell, whereas other languages like Python let you stumble upon desired behaviors through trial and error.
* **Documentation:** Older languages, like C, typically have mature documentation due to years of refinement. However, newer languages may rapidly outgrow their original specs before they reach stability.
* **Community:** Stack Overflow, for example, gives you the peace of mind that you're not alone in solving some of your hardest programming challenges. Newer languages may not have an established community, so sometimes you're on your own.
* **Performance:** C/C++ are languages that compile to machine code and perform  certain algorithms more efficiently than higher-level interpreted languages such as JavaScript. 
* **Elegance:** If you're truly a romantic, then the syntax and philosophy of the language may play a key factor in why you've chosen to stick with a language.
* **Robustness:** Type safety, informative error messages, and intuitive memory management are all aspects of languages that relieve the programmer from worrying about anything but the task at hand.
* **Legacy:** Sometimes the argument of "it's always been done that way" tends to be reason alone to keep up a tradition. 

Indeed, imperative languages are no doubt the most popular in industry (see chart below), perhaps because those languages have successfully satisfied most of the above criteria. However, you've read up to this point in this article already, so I bet you're game to try something new.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-4.png)
_Source: [https://www.tiobe.com/tiobe-index/](https://www.tiobe.com/tiobe-index/)_

We're about to dive into a couple concrete examples, so hold on tight, buckle your seat belts, and please keep your arms within the vehicle. 

## Comparing languages

Suppose you'd like to write an algorithm for a Mars rover that intelligently sends back video recordings to mission control on Earth. There's no high speed fiber-optic connection between the planets, so the order in which videos are sent really matters.

The list of video recordings may be defined as follows:

```javascript
videos = [
    {name: "Excavation", minutes: 22, anomaly: true},
    {name: "Sky panoramic", minutes: 11, anomaly: false}
]
```

Let's say mission control is only interested in retrieving videos that run shorter than 20 minutes, so you'd like to write out an algorithm that sequences videos accordingly. In the next few sections, we'll see how different language paradigms might implement this simple task.

### Imperative implementation

If a `for` loop through the `videos` array is your first instinct, then you're thinking like an imperative programmer. For example, you may want to use an `if` statement within the loop to selectively append videos that are shorter than 20 minutes to a queue, as shown below:

```javascript

queue = []
for (var i = 0; i < videos.length; i++) {
    if (videos[i].minutes < 20) {
        queue.push(items[i])
    }
}

```

The variables `queue` and `i` are declared with initial values of `[]` and `0`, respectively. Then the rest of the code specifies _**how**_ to update the variables.

### Functional implementation

Functional programmers smirk, and present us with an elegant one-liner:

```javascript
queue = videos.filter(x => x.minutes < 20)
```

Here, `filter` is a function that reduces an array based on a predicate. The focus is no longer about how variables get updated through an algorithm, but instead about **_what_** data transformations need to occur to produce the desired result. 

### Task-oriented implementation

In task-oriented languages, you define the goal and possible actions. The goal, in our case, is to pick videos that are shorter than 20 minutes. 

One way to author goals is by listing situations in order of preference, such as `[{minutes: 10}, {minutes: 40}]`, which declares that `minutes == 10` is more favorable than `minutes == 40`. 

```javascript
preference = [{minutes: 10}, {minutes: 40}]
```

The action is to select a video from the `videos` list. We do so using the `fork` statement, which is a generalized `if` statement. Traditional `if` statements execute the first satisfying entry condition, but `fork` statements consider all satisfying entry-conditions, and choose the one that best characterizes our preferences by searching (for example depth-first search) forwards in time.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-197.png)
_A `fork` in the road. (Photo by [Jens Lelie](https://unsplash.com/@leliejens?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit))_

The programmer lists the candidate choices, and lets the run-time resolve the best possible path to take. That way, some of the cognitive-load of defining system behavior is offloaded from the programmer.

```javascript
#{model: [preference]}
fork {
    _ {
        name, minutes, anomaly = videos[0]
        print name
    }
    _ {
        name, minutes, anomaly = videos[1]
        print name
    }
}
```

The run-time of the language resolves forks by picking a candidate block that will increase the situation's utility. In this case, the run-time will select videos of shorter duration. 

## Understanding the power of each paradigm

Let's face it, in order for code to stay relevant, it needs to be continuously maintained. Refactoring, enhancing, and scaling can get a bit scary at times. That's why each of the three paradigms champion their own mechanisms for dealing with changing requirements.

**Object-oriented design** in imperative languages: Instead of directly accessing data, the programmer defines interfaces, which hide the implementation details of how the data changes. That way, you can plug and play these _objects_ with new problems, without needing to overwhelm yourself with all the minor details.

**Pure functions** in functional languages: A pure function is slightly like a look-up table (like a dictionary or map). It guarantees that no matter how the software evolves, the pure function will not accidentally update variables beyond its scope. Chaining pure functions together creates more complex functions that remain pure, letting you refactor easily without worrying about global variables.

**Tasks** in task-oriented languages: Tasks let you explain a desired behavior without needing to detail out a concrete plan. For example, defining what one may want for dinner is different from writing a recipe to outline the precise steps in the kitchen. The run-time of the language is responsible for assembling instructions that achieve the task, whereas the programmer is responsible for carefully defining the desirable states.

For instance, in our Mars rover example, let's say the requirements have changed: mission control now wants to only retrieve videos with anomalies. Consider how you would rewrite the imperative, functional, and task-oriented code. 

I'll let you think about the first two, but in task-oriented languages, simply change the goal to change program behavior: 

```javascript
preference = [{anomaly: true}, {anomaly: false}]
```

As systems mature in complexity, task-oriented languages unveil powerful abstractions that allow programmers to scale and alter the behavior of their systems more efficiently. The programmer focuses on defining the **why**, whereas the run-time composes the **how**_._ This explicit decoupling of goals from actions helps alleviate software failure due to unforeseen edge-cases. 

These task-oriented languages may one day be the de facto standard for authoring the behavior of video-game agents (NPCs), industrial robots, chat-bots, or any decision-making system. The technical maturity of programming language design hasn't even reached its adolescence – for example, compared to the history of the automobile, we haven't even made it to the Ford Model T. Now's the time for the adventurous to uncover new fundamental software principles.  

If you would like to try out [DMPL](http://w3.org/2019/11/dms), join the [W3C](https://www.w3.org/community/conv/) Conversational Interfaces Community Group, and follow [@binroot](https://twitter.com/binroot) for more announcements, news, and discussion.

