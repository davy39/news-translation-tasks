---
title: Complete Guide to Agile Methodology
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T19:25:00.000Z'
originalURL: https://freecodecamp.org/news/complete-guide-to-agile-methodology
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d69740569d1a4ca37a0.jpg
tags:
- name: agile development
  slug: agile-development
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Story Points and Complexity Points

  In Scrum/Agile, the functionality of a product in development is explored by way
  of stories a user might tell about what they want from a product. A team uses Story
  Points when they estimate the amount of effort req...'
---

## **Story Points and Complexity Points**

In Scrum/Agile, the functionality of a product in development is explored by way of **stories** a user might tell about what they want from a product. A team uses **Story Points** when they estimate the amount of effort required to deliver a user story.

Notable features of story points are that they:

* represent the contributions of the whole team
* do not equate directly to time the task might take
* are a rough measure for planning purposes - similar to orders of magnitude
* are assigned in a Fibonacci-like sequence: 0, 1, 2, 3, 5, 8, 13, 20, 40, 100
* estimate the ‘size’ of stories _relative to each other_

The concept of story points can be quite elusive if you are new to Agile ways of doing things. You will find many online sources discussing story points in different ways, and it can be hard to get a clear idea of what they are and how they are used.

As you learn about the principles and terminology of practices like Scrum, the reasons for some of these properties will become apparent. The use of story points, especially in ‘ceremonies’ such as planning poker, is much easier to understand by observing or taking part than in a written explanation!

### **More Information:**

* User Stories: [freeCodeCamp](https://guide.freecodecamp.org/agile/user-stories)

## **Parallel Development**

Parallel Development stands for the development process separated into multiple branches, to provide a versatile product with stable releases and new features. In a more common straightforward software development process you have only one branch with bug fixes and improvements, alongside with new features. In parallel development multiple branches can coexist.

Usually parallel development contains a main, “master” branch which is the most stable and contains important fixes for existing code. From the main branch, more branches are created to add new “paths” to the existing code. These branches provide new features, but do not include fixes, applied in the mean time from the master branch. Clients know about these releases and have special equipment, or test machines to be able to test the new features. When QA tests are passed, side branch can be merged with the main branch to introduce new features to the release version.

## **Burndown Charts and Burnup Charts**

Burndown and burnup charts are used to measure progress of a project— usually a development sprint under the Agile methodology. Both charts visually represent work versus time.

Burndown charts show how much work is left to be done versus the amount of time remaining. The Y axis represents work left to be done— usually relating to a time estimate assigned to each task, e.g. story points— and the X axis represents time left. Two lines are used; the first— “Ideal Work Remaining Line”— represents an ideal burndown, where each day an amount of work proportional to the total amount of time is completed, resulting in a straight line. The second “Actual Work Remaining Line” is used to plot actual progress as taks move through development to a done state. An example of a burndown chart is shown below.

![alt text](https://upload.wikimedia.org/wikipedia/commons/8/8c/Burn_down_chart.png)

Many Scrum Teams use burndown charts in order to see how they are doing during the sprint. Having an even and steady burndown might be an indicator that the stories are small and manageable. If a team notices in the middle of a sprint that the “Actual Work Remaining Line” is above the “Ideal Work Remaining Line” they can make adjustments to the scope: stories can be taken out of the sprint or the scope of stories can be made smaller. Looking at the burndown during the retrospective in the end of the sprint might spark some interesting discussions and result in process improvements.

Burnup charts are very similar, but they show the work that has been completed versus the total amount of work and time remaining. Three lines are used— an ideal line, a completed work line, and a total work line. In this chart, the total work line should be somewhat steady across the top of the chart, and is a good representation of scope change. The completed work line should move steadily up towards the total work line for the amount of time in the project— its ideal trajectory is shown by the ideal line. An example is shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/ReleaseBurnup.png)

_Image courtesy of [Effective PMC](https://sites.google.com/a/effectivepmc.com/www/blog/agile/information-radiators/burn-up-chart?overridemobile=true)_

## **Design Patterns**

A design pattern is a common design solution to a common design problem. A collection of design patterns for a related field or domain is called a pattern language. Note that there are also patterns at other levels: code, concurrency, architecture, interaction design …

In software engineering, a software design pattern is a general reusable solution to a commonly occurring problem within a given context in software design. It is not a finished design that can be transformed directly into source or machine code. It is a description or template for how to solve a problem that can be used in many different situations. Design patterns are formalized best practices that the programmer can use to solve common problems when designing an application or system.

Object-oriented design patterns typically show relationships and interactions between classes or objects, without specifying the final application classes or objects that are involved. Patterns that imply mutable state may be unsuited for functional programming languages, some patterns can be rendered unnecessary in languages that have built-in support for solving the problem they are trying to solve, and object-oriented patterns are not necessarily suitable for non-object-oriented languages.

Design patterns may be viewed as a structured approach to computer programming intermediate between the levels of a programming paradigm and a concrete algorithm.

The book that popularised the field is Gang of Four’s (GoF) **Design Patterns: Elements of Reusable Object-Oriented Software** (1994). It present a series (23) of patterns for an conventional (C++) OO language classified in three types:

* **Creational** (to create objects): abstract factory, builder, factory method, prototype, singleton.
* **Structural** (to compose objects): adapter, bridge, composite, decorator, facade, flyweight, proxy.
* **Behavioral** (to communicate between objects): chain of responsibility, command, interpreter, iterator, mediator, memento, observer, state, strategy, template method, visitor.

Patterns can be used for multiple objectives (learning, communication, improving your tooling) but in agile they should be refactored from code with technical debt and not just added at the start (emergent design/architecture) as initially you don’t have enough knowledge about the (future) system that is going to evolve. Note that what requires a pattern in a language or tool may not be needed or already be part of another language or tool. A framework is a set of cooperating classes that make up a reusable design for a specific type of software and are typically pattern-heavy.

## **Task Boards and Kanban**

Kanban is an excellent method both for teams doing software development and individuals tracking their personal tasks.

Derived from the Japanese term for “signboard” or “billboard” to represent a signal, the key principal is to limit your work-in-progress (WIP) to a finite number of tasks at a given time. The amount that can be In Progress is determined by the team’s (or individual’s) constrained capacity. As one task is finished, that’s the signal for you to move another task forward into its place.

Your Kanban tasks are displayed on the Task Board in a series of columns that show the state of the tasks. In its simplest form, three columns are used

* To Do
* Doing
* Done

![Kanban Board Example](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Simple-kanban-board-.jpg/600px-Simple-kanban-board-.jpg)

_Image courtesy of [Wikipedia](https://en.wikipedia.org/wiki/Kanban_board)_

But many other columns, or states, can be added. A software team may also include Waiting to Test, Complete, or Accepted, for example.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/LeanKit-Program-Board_Drive-Agility-c-1000x547.jpg)
_A more complicated example._

_Image courtesy of [leankit](https://leankit.com/learn/kanban/kanban-board-examples-for-development-and-operations/)_

## **Integration Hell**

Integration Hell is a slang term for when all the members of a development team goes through the process of implementing their code at random times with no way to incorporate the different pieces of code into one seamless string of code. The development team will have to spend several hours or days testing and tweaking the code to get it all to work.

In practice, the longer components are developed in isolation, the more the interfaces tend to diverge from what is expected. When the components are finally integrated at the end of the project, it would take a great deal more time than allocated, often leading to deadline pressures, and difficult integration. This painful integration work at the end of the project is the eponymous hell.

Continuous Integration, the idea that a development team should use specific tools to “continuously integrate” the parts of the code they are working on multiple times a day so that the tools can match the different “chunks” of code together to integrate much more seamlessly than before.

Code Repositories, like Git (and it’s open source interface we all know and love, GitHub) allow development teams to organize their efforts so that more time can be spent coding and less time on worrying if the different parts of the code will all integrate.

[Continuous Integration](https://guide.freecodecamp.org/agile/continuous-integration/) is the Agile antidote to this problem. Integration is still painful, but doing it at least daily keeps interfaces from diverging too much.

## User Stories

According to [Mountain Goat Software](https://www.mountaingoatsoftware.com/agile/user-stories), user stories are:

> ...part of an agile approach that helps shift the focus from writing about requirements to talking about them. All agile user stories include a written sentence or two and, more importantly, a series of conversations about the desired functionality.

User stories are typically written using the following pattern:

**As a [ type of user ], I want [ some goal ] so that [ some reason or need ]**

User stories should be written in non-technical terms from the perspective of the user. The story should emphasize the need of the user, and not the how. There should be no solution provided in the user story.

One common mistake that is made when writing user stories is writing from the perspective of the developer or the solution. Be sure to state the goal and the need, and the functional requirements come later.

#### **Sizing a User Story: Epics and Smaller Stories**

An is like the headline or placeholder for user stories. Epics are typically serve as big, broad strokes, and are then broken down into several user stories.

By starting with an epic, you can plan out the functionality of the product without committing to exact details. Taking this approach gives you time to learn more about your users and how to address their needs.

When thinking about possible stories, it is also important to consider “mis-user cases” and “unhappy path” stories. How will exceptions be handled by the system? What kind of messaging will you provide back to user? How would a malicious user abuse this application function? These mal-stories can save rework and become useful test cases in QA.

## **Planning Poker**

### **Introduction**

Planning poker is an estimation and planning technique in the Agile development model. It is used to estimate the development effort required for a [user story](https://en.wikipedia.org/wiki/User_story) or a feature.

### **Process**

The planning poker is done for one user story at a time.

Each estimator holds an identical set of poker cards consisting of cards with various values. The card values are usually from the Fibonacci Sequence. The unit used for the values can be the number of days, story points, or any other kind of estimation unit agreed on by the team.

The product owner (PO) or stakeholder explains the story that is to be estimated.

The team discusses the story, asking any clarifying questions that they might have. This helps the team get a better understanding on _what_ the PO wants.

At the end of the discussion, each person first selects a card (representing their estimate for the story) without showing it to the others. Then, they reveal their cards at the same time.

If all the cards have the same value, the value becomes the estimate for the story. If there are differences, the team discusses the reasons for the values that they have chosen. It is of high value that the team members who gave the lowest and highest estimates provide justifications for their estimates.

After this discussion, the process of picking a card in private and then revealing it at the same time is repeated. This is done until there is a consensus on the estimate.

Because planning poker is a tool to moderate a _joint_ expert estimation, it leads to a better common understanding and perhaps even refinement of the feature request. It is of high value even when the team is operating in a No-Estimates mode.

A moderator should try to avoid confirmation bias.

Things worth mentioning:

* Estimations are not comparable between teams, as every team has its own scala.
* Estimations should include everything that needs to be done in order for a piece of work to be done: designing, coding, testing, communicating, code reviews (+ all possible risks)
* The value of using planning poker is in the resulting discussions, as they reveal different views on a possible implementation

## **Behavior Driven Development**

Behavior Driven Development (BDD) is a software development process that emerged from [Test Driven Development (TDD)](https://www.freecodecamp.org/news/an-introduction-to-test-driven-development-c4de6dce5c/). Behavior Driven Development combines the general techniques and principles of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software development and management teams with shared tools and a shared process to collaborate on software development. It is a software development methodology in which an application is specified and designed by describing how its behavior should appear to an outside observer.

Although BDD is principally an idea about how software development should be managed by both business interests and technical insight, the practice of BDD does assume the use of specialized software tools to support the development process.

Although these tools are often developed specifically for use in BDD projects, they can be seen as specialized forms of the tooling that supports test-driven development. The tools serve to add automation to the ubiquitous language that is a central theme of BDD.

BDD focuses on:

* Where to start in the process
* What to test and what not to test
* How much to test in one go
* What to call the tests
* How to understand why a test fails

At the heart of BDD is a rethinking of the approach to the unit testing and acceptance testing that naturally arise with these issues. For example, BDD suggests that unit test names be whole sentences starting with a conditional verb (“should” in English for example) and should be written in order of business value. Acceptance tests should be written using the standard agile framework of a user story: “As a _role_ I want _feature_ so that _benefit_”. Acceptance criteria should be written in terms of scenarios and implemented as classes: Given _initial context_, when _event occurs_, then _ensure some outcomes_.

Example

```text
Story: Returns go to stock

As a store owner
In order to keep track of stock
I want to add items back to stock when they're returned.

Scenario 1: Refunded items should be returned to stock
Given that a customer previously bought a black sweater from me
And I have three black sweaters in stock.
When he returns the black sweater for a refund
Then I should have four black sweaters in stock.

Scenario 2: Replaced items should be returned to stock
Given that a customer previously bought a blue garment from me
And I have two blue garments in stock
And three black garments in stock.
When he returns the blue garment for a replacement in black
Then I should have three blue garments in stock
And two black garments in stock.
```

Along with it are some Benefits:

1. All development work can be traced back directly to business objectives.
2. Software development meets user need. Satisfied users = good business.
3. Efficient prioritization - business-critical features are delivered first.
4. All parties have a shared understanding of the project and can be involved in the communication.
5. A shared language ensures everyone (technical or not) has thorough visibility into the project’s progression.
6. Resulting software design that matches existing and supports upcoming business needs.
7. Improved quality code reducing costs of maintenance and minimizing project risk.

## **Scrum**

Scrum is one of the methodologies under the Agile umbrella. The name is derived from a method of resuming play in the sport of rugby, in which the entire team moves together to make ground. Similarly, a scrum in Agile involves all parts of the team working on the same set of goals. In the scrum method, a prioritized list of tasks is presented to the team, and over the course of a “sprint” (usually two weeks), those tasks are completed, in order, by the team. This insures that the highest-priority tasks or deliverables are completed before time or funds run out.

### **Components of a Scrum**

Scrum is one of the methodologies under the Agile umbrella. It originates from ‘scrummage’ which is a term used in rugby to denote players huddling together to get possession of the ball. The practice revolves around

* A set of roles (delivery team, product owner, and scrum master)
* Ceremonies (sprint planning, daily standup, sprint review, sprint retrospective, and backlog grooming)
* Artifacts (product backlog, sprint backlog, product increment, and info radiators and reports).
* The main goal is to keep the team aligned on project progress to facilitate rapid iteration.
* Many organisations have opted for Scrum, because unlike the Waterfall model, it ensures a deliverable at the end of each Sprint.

### Artifacts

* Sprint: It is the time duration, mostly in weeks, for which a Team works to achieve or create a deliverable. A deliverable can defined as a piece of code of fragment of the Final Product which the team wants o achieve. Scrum advises to keep the duration of a Sprint between 2-4 weeks.
* Product Backlog: It is the list of tasks a Team is supposed to finish within the current Sprint. It is decided by the Product Owner, in agreement with the Management as well as Delivery Team.

### Roles

* Product Owner(PO): The ONLY Accountable person to the Management. PO decides what goes in or out of the Product Backlog.
* Delivery Team: They are required to work in accordance with the tasks set by their PO in the product backlog and deliver the required delivarable at the end of the sprint.
* Scrum Masters: - Scrum Master’s has to strictly adhere to Scrum Guide and make the team understand the need to adhere to Scrum guide when following Scrum. It is a Scrum Master’s job to ensure all Scrum ceremonies being conducted on time and participated by all the required people as per the scrum guide. The SM has to ensure that the Daily Scrum is conducted regularly and actively participated by the team.

## **Daily Stand-Up and Daily Scrum**

The Daily Stand-Up (DSU) or Daily Scrum meeting is one of the integral parts of scrum methodology.

As the name suggests, you hold the meeting daily, at the same time and, for a co-located team, in the same location. The meeting should be brief, finished in less than 15 minutes.

Only members of the Development team are required to attend the Daily Stand-up. Typically, the Scrum Master and Product Owners will also attend, but they are not required.

The standard agenda for each person is:

* What have you done since the last DSU
* What are you doing after this DSU
* What are the major obstacles that are stopping your progress, and where do you need help

Team members are to listen carefully to each other’s contributions and attempt to identify areas where they can assist each other’s progress. The standup meeting will also surface more lengthy topics of discussion that need to take place between different members of the team. These lengthier discussions that arise should then be halted and taken outside of the standup, involving only the relevant participants, and not the entire team.

### **Example of Stand-up Meeting**

[https://www.youtube.com/watch?v=_3VIC8u1UV8](https://www.youtube.com/watch?v=_3VIC8u1UV8)

## **Pirate Metrics**

Dave McClure identified five high-level metric categories critical to a startup’s success: Acquisition, Activation, Retention, Revenue, Referral.

He coined the term “Pirate Metrics” from the acronym for these five metric categories (AARRR).

In their book Lean Analytics, Croll and Yoskovitz interpret these metrics visually as a funnel:

![Lean Analytics Figure 5.1](https://github.com/yunChigewan/storage/blob/master/figure_5_1.jpg?raw=true)

Lean Analytics, 2013

And with more pointed explanations as a table:

![Lean Analytics Table 5.1](https://github.com/yunChigewan/storage/blob/master/table_5_1.jpg?raw=true)

Lean Analytics, 2013

## **Nonfunctional Requirements**

A non-functional requirement (NFR) is a requirement that specifies criteria that can be used to judge the operation of a system, rather than specific behaviors (a functional requirement). Non-functional requirements are often called “quality attributes”, “constraints” or “non-behavioral requirements”.

Informally, these are sometimes called the “ilities”, from attributes like stability and portability. NFRs can be divided into two main categories:

* **Execution qualities**, such as safety, security and usability, which are observable during operation (at run time).
* **Evolution qualities**, such as testability, maintainability, extensibility and scalability, which are embodied in the static structure of the system

Usually you can refine a non-functional requirement into a set of functional requirements as a way of detailing and allowing (partial) testing and validation.

### **Examples:**

* The printer should print 5 seconds after the button is pressed
* The code should be written in Java
* The UI should be easily navigable

## **Feature Based Planning**

**Feature Based Planning** is a planning methodology that can be used to decide when to release software based on the features that will be delivered to the customers, rather than an arbitrary deadline based release.

In this method of release planning, teams decide what feature/features should be prioritised. Based on the scope of these features the team can then predict when the next release can be deployed.

## **Functional Managers**

A functional manager is a person that have management authority over group of people. That authority comes from the formal position of that person in the organization (eg. director of the department, quality department manager, development team manager). Role of functional managers is different then Project Managers or ScrumMasters and is not project based.  
In more agile organizations different models exists. Functional manager often are responsible for developing people in their groups, securing budgets and time for people. However there are also some Agile company models where functions usually assigned to functional managers are distributed to other roles within organization (eg. Spotify model with Tribes, Guilds, Chapters, Squads).

Out in the traditional world of work companies organize people into a hierarchy. People with similar work roles are grouped into functional areas and led by a Functional Manager. The functional manager is generally responsible for the guidance and well-being of the employees who report directly to her.

Agile project teams will often work with functional managers who control the resources the team needs to get work done. An example would be working with a functional manager in procurement to assign a person to work with the team to procure software licenses.

## **Build Measure Learn**

The Build-Measure-Learn loop is a method used to build the right product. Coined in the “Lean Startup” book by Eric Reis, the loop enables rapid experimenting, in the sole purpose of achieving market fit. In other words, it is a powerful system to validate assumptions concerning a product you set out to deliver. Breaking down the loop, it consists of the following parts:

![build-measure-learn-loop](https://steveblank.files.wordpress.com/2015/05/ideas-build-code-measure.jpg)

### **Idea**

Each loop starts with an idea that will supply business value to some users. Such idea must be consisted of a vision for a product - which will direct you at what to build, and a metric that will point out to whether your assumptions about the business value were correct.

### **Build**

To validate your idea, you set out to build a Minimal Viable Product (MVP), combined with predefined metrics (one is preferred), whose purpose is to validate your theory, and help you decide whether you should preserve or pivot.

### **Measure**

This stage is focused on collecting data & metrics from the MVP.

### **Learn**

Next, using the data collected, a decision has to be made, whether or not your product is used by users and so you should preserve, or whether users are not interested in the product, and as such you must pivot. The learn phase is therefore ending with an idea (either how to expand the product, or how to pivot from the original product), applicable for the next Build Measure Learn loop.

## **Sprint Planning Meeting**

The Sprint Planning is facilitated by the team’s Scrum Master and consists of the Scrum Team: Development Team, Product Owner (PO) and Scrum Master (SM). It aims to plan a subset of Product Backlog items into a Sprint Backlog. The Scrum Sprint is normally started in after the Sprint Planning meeting.

### **Main part**

It is of high value for the team to part the meeting in two parts by asking this two questions:

* **What** should the team plan for the upcoming Sprint?
* **How** should the team (roughly) takle the items planned?

#### **What**

In What phase the team starts with the top of the ordered Product Backlog. The team at least implicitly estimates the items by forecasting what they could take into Sprint Backlog. If needed they could ask / discuss items with the PO, who has to be in place for this meeting.

#### **How**

In How phase the team shortly discusses every picked Sprint Backlog item with the focus on how they will takle it. SM helps the team not to deep dive into discussion and implementation details. It is very likely and good if more questions to the PO are asked or refinements to the items, or backlog is done by the team.

### **Sprint Goal / Closing**

The team should come up with a shared Sprint Goal for the Sprint to keep the focus in the Sprint time box. At the end of the Sprint Planning the team forecasts that they can achieve the Sprint Goal and complete most likely all Sprint Backlog items. The SM should prevent the team to overestimate by providing useful insights or statistics.

## **Lean Software Development**

### **Introduction**

Lean Software Development is the process of building software with the focus on using techniques which minimize extra work and wasted effort. These techniques are borrowed from the Lean manufacturing movement and applied to the context of software development.

### **Key Concepts**

There are seven principles within the methodology which include:

1. Eliminate waste
2. Amplify learning
3. Decide as late as possible
4. Deliver as fast as possible
5. Empower the team
6. Build integrity in
7. See the whole

### **Metaphors**

The act of programming is viewed as an assembly line, where every feature or bug fix is called a “change request”. This assembly line of “change requests” can then be considered as a “value stream” with the goal being to minimize the time that each “change request” is on the line prior to being delivered.

Software which is not yet delivered is considered as “inventory” since it has not yet provided value to the company or the customer. This includes any software which is partially complete. Therefore to maximize throughput it is important to deliver many small complete working pieces of software.

In order to minimize the “inventory” it is important to secede control to the “workers” who would be the software developers, as they would be best equipped to create automated processes to “mistake proof” the various parts of the assembly line.

### **References**

The original source of written documentation on the Lean techniques is the book Lean Software Development, An Agile Toolkit by Mary and Tom Poppendieck.

Additional books by the author(s) include:

* Implementing Lean Software Development: From Concept to Cash by Mary Poppendieck
* Leading Lean Software Development: Results Are not the Point by Mary Poppendieck

## **Collocation Vs Distributed**

* Co-located refers to a team that sits together; same office. Ideally, everyone sitting together in adjacent offices or an open workspace.
* Distributed team members are scattered geographically; different buildings, cities, or even countries. In case of distributed team, infrastructure should facilitate processes in order to resolve time difference and distance between team members, thus providing an efficient way of working altogether.

## **Continuous Integration**

At its most basic, continuous integration (CI) is an agile development methodology in which developers regularly merge their code directly to the main source, usually a remote `master` branch. In order to ensure that no breaking changes are introduced, a full test suite is run on every potential build to regression test the new code, i.e. test that the new code does not break existing, working features.

This approach requires good test coverage of the code base, meaning that a majority, if not all, of the code has tests which ensure its features are fully functional. Ideally continuous integration would be practiced together with full [Test-Driven Development](https://guide.freecodecamp.org/agile/test-driven-development).

### **Main Steps**

The following basic steps are necessary to do the most standard current approach to continuous integration.

1. Maintain a central repo and an active `master` branch.

There has to be a code repository for everyone to merge into and pull changes from. This can be on Github or any number of code-storage services.

1. Automate the build.

Using NPM scripts or more complex build tools like Yarn, Grunt, Webpack, or [Gulp](https://guide.freecodecamp.org/developer-tools/gulp), automate the build so that a single command can build a fully functional version of the product, ready to be deployed in a production environment. Better yet, include deployment as part of the automated build!

1. Make the build run all the tests.

In order to check that nothing in the new code breaks existing functionality, the full test suite needs to be run and the build needs to fail if any tests within it fail.

1. Everyone has to merge changes to `master` every day.
2. Every merge into `master` has to be built and fully tested.

### **Best Practices**

There are further best practices that make the best use of what CI has to offer and the challenges it presents, such as:

1. Keep the build fast, so that lots of developer time isn’t wasted waiting for a build.
2. Test the build in a full clone of the production environment.

If you have, for example, an app deployed on something like Heroku or Digital Ocean, have a separate test deployment there that you can deploy test builds to, to make sure they work not just in tests but in a real production environment. This test environment should be functionally identical to the actual production environment, in order to ensure the test is accurate.

1. Make it easy to stay up to date.

Coders should pull regularly from the `master` branch to keep integrating their code with the changes from their team. The repo should also be made available to stakeholders like product managers, company executives, or sometimes key clients, so that everyone is easily able to see progress.

1. Keep records of builds, so that everyone can see the results of any given build, whether it succeeded or failed, and who or what introduced new changes.
2. Automate deployment.

Keep your app fully up-to-date with any new changes by automating deployment in the production environment as the final stage of the build process, once all tests have passed and the test deployment in the production environment clone has succeeded.

### **CI Services**

Lots of services exists to handle the process of continuous integration for you, which can make it a lot easier to establish a solid CI pipeline, or build process. When evaluating these, take into account factors like budget, build speed, and what kind of project you’re working on. Some services, like [Travis CI](https://travis-ci.org/) offer free services for open-source projects, which can make them an easy choice for projects like that, but they might have slower builds than other services, like [Circle CI](https://circleci.com/) or [Codeship](https://codeship.com/), to name just a few.

## **Acceptance Criteria**

The User Story, as an item in your backlog, is a placeholder for a conversation. In this conversation, the Product Owner and the Delivery Team reach an understanding on the desired outcome.

The Acceptance Criteria tells the Delivery Team how the code should behave. Avoid writing the **“How”** of the User Story; keep to the **“What”**. If the team is following Test Driven Development (TDD), it may provide the framework for the automated tests. The Acceptance Criteria will be the beginnings of the test plan for the QA team.

Most importantly, if the story does not meet each of the Acceptance Criteria, then the Product Owner should not be accepting the story at the end of the iteration.

Acceptance criteria can be viewed as an instrument to protect the Delivery Team. When the Delivery Team commits to a fixed set of stories in the Sprint planning they commit to fixed set of acceptance criteria as well. This helps to avoid scope creep.

Consider the following situation: when accepting the user story the Product Owner suggests adding something that was not in the scope of the User story. In this case the Delivery team is in the position to reject this request (however small it might be) and ask the Product owner to create a new User story that can be taken care of in another Sprint.

## Code Smells

A Code Smell in computer programming is a surface indication that there might be a problem regarding your system and the quality of your code. This problem might require refactoring to be fixed.

It is important to understand that smelly code works, but is not of good quality.

#### **Examples**

1. Duplicated code - Blocks of code that have been replicated across the code base. This may indicate that you need to generalize the code into a function and call it in two places, or it may be that the way the code works in one place is completely unrelated to the way it works in another place, despite having been copied.
2. Large classes - Classes having too many lines of code. This may indicate that the class is trying to do too many things, and needs to be broken up into smaller classes.

## More info on Agile Development:

* [How to make sure your development process is actually Agile](https://www.freecodecamp.org/news/signs-that-your-development-process-is-agile-only-on-paper-and-how-to-fix-it-f6c05b24337f/)
* [How to fix tech debt](https://www.freecodecamp.org/news/give-the-gift-of-a-tech-debt-sprint-this-agile-holiday-season/)
* [Does Agile really mean what you think?](https://www.freecodecamp.org/news/you-say-your-team-is-agile-but-that-word-may-not-mean-what-you-think-6dd26eaf9b21/)


