---
title: How to use Systems Engineering to build a successful web app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T17:47:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-systems-engineering-to-build-a-successful-web-app-6f8bda2f7fc4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f1AObOsOTggi7QhrW8Frsw.png
tags:
- name: Design
  slug: design
- name: systems-engineering
  slug: systems-engineering
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Dler Ari

  If you understand how it works, its easier to build it

  So you’ve finally completed your design in Adobe XD, Figma, Sketch or InVision,
  but still struggle with the idea of how to implement the functionality. Don’t worry,
  we’ve thought for ...'
---

By Dler Ari

#### If you understand how it works, its easier to build it

So you’ve finally completed your design in Adobe XD, Figma, Sketch or InVision, but still struggle with the idea of how to implement the functionality. Don’t worry, we’ve thought for a while that the only way to build web-apps is to begin with UI/UX design along with prototype sketches.

Luckily, it turns there are other, and better techniques we can use to describe web-apps without stressing about what positions, size, or spacing the elements on a page need.

Let me introduce you to something that has been used by companies in the aerospace, maritime, defense, automotive and telecommunication fields to gain a better understanding of how systems behave and interact. I’m not talking about X number of tips and tricks on how to improve UI/UX, but what techniques you can apply from the **Systems Engineering** (SE) arsenal to build successful web-apps.

These techniques have many benefits, but the most important one is how quickly one can express ideas and understand how things work.

By the end of this article, you’ll be able to use some of these SE techniques to build better apps.

Here are four practical and relevant SE techniques you can apply.

> If you want to become a better web developer, start your own business, teach others, or simply improve your development skills, I’ll be posting high-quality weekly tips and tricks on the latest web-languages out in the market.

### A practical example — Online learning platform

In order to make the examples intuitive and applicable, we’ll build a pretend online learning platform. A platform that allows people to publish content, the same concept as Medium, YouTube, Unsplash etc.

> Note: the idea of using these techniques is to describe it enough so that developers can easily implement these features, which means we don’t need to go into details.

Here are few nice tips to be aware of in the early stages of the app.

#### 1. Don’t start with detailed design

In early stages, most developers naturally begin with defining the solutions first, and thus get caught up with details that don’t really matter for the end-product. It leads us in the wrong direction, and we forget the true purpose of the app.

Design is important, but not something we should focus on in early stages. It’s not fixed (and changes often) — for instance the color of a button, position of the elements, font-type and so on. What doesn’t change is the web-app’s underlying behavior, such as the way a person authenticates, the way they upload something on a page, the steps to process a payment, and so forth. The fundamental parts stay the same.

#### 2. Start with the problem

Identify the problem first: the surroundings, who are the stakeholders, the behavior, and the context of the app (the scope).

We don’t build apps based on solutions, we build them because there is a problem, issue, or a challenge that needs to be resolved. In most cases, the client doesn’t care about the solution, except that it works. The solution shall be identified when the developers understand how the app behaves and interact.

The problem for example may be that the current communication platform is too slow which influences the workflow. Another problem may be that the manager does not have a clear overview of what tasks the employee work with and so on.

Keep in mind that the problem tells us that there is a need, but doesn’t provide any solutions. The problem is what triggers the development process. So begin with the problem first before starting with the solutions.

Let’s see what techniques we can use to describe our online learning platform.

### 1. Context Diagram

![Image](https://cdn-media-1.freecodecamp.org/images/1*f1AObOsOTggi7QhrW8Frsw.png)

#### Define the boundaries

The purpose of the context diagram is to define the boundaries within the app, or parts of the app, and provide a clear understanding of what entities it interacts with.

As shown, we can see what types of stakeholders (users) interact with the app, and the interaction types between them. Note, the names of the stakeholders are not mentioned, nor what type of database we are dealing with. We don’t want to get caught up with details which may change in the future.

#### Clarify complex apps

If you are dealing with a fairly complex app that consist of many parts, then a context diagram is a good alternative that allows you to simplify things. It’s also a good way to remind ourselves of what the purpose of the app is, and eliminate things that provide little value for the app. It’s a way to step back, and focus on what’s important.

### 2. Use Case Diagram

![Image](https://cdn-media-1.freecodecamp.org/images/1*9pm2euQHRmIO1izFgd1-uA.png)
_High-level use case diagram_

Note, we don’t mention anything about the layout, size or position of the elements. In SE it’s important that things are modular, meaning that we can change things without affecting the app — we don’t want things to be fixed and immutable.

> A developer who needs to build working software should be able to read a use case and get a good sense of what the software needs to do. [Source](http://www.gatherspace.com/static/use_case_example.html).

#### Describe the interactions

The purpose of the use case diagram is to describe how the user interacts with the web-app in a verbal way. This is a great tool for understanding what the customer needs and also what features the developer has to implement.

#### Elaborate a use case (action)

As shown above, the user is the content-producer and performs four actions. An action is a feature that needs to be implemented. The use case diagram does not describe the behavior of the app, except the interaction between the user and the app, or parts of it.

In order to describe the behavior, we can take one action, and elaborate it through diagrams such as activity, state-machine, sequence-diagrams and so forth.

For instance, we can create an activity diagram to describe the steps needed to fulfill the “upload content” action. There is an example of this in sections 3 and 4.

#### Focus on different use case scenarios

The app will most likely be used by users with different roles such as an admin, content producer, editor, analyst and so forth. And each role has a set of unique needs with different use case (interactions). It is important that we cover these interactions or else we end up with a static app customized for a specific user role.

### 3. Activity Diagram

![Image](https://cdn-media-1.freecodecamp.org/images/1*dUNAPGt-4Fn2BxRKgx8esg.png)
_Activity diagram — upload content_

#### Describe the behavior

The purpose of an activity diagram is to describe the sequence of activities necessary to fulfill a use case. The use case selected is “upload content” from the use case diagram, as shown above.

You are free to decide what use case you want to expand upon and elaborate — the point is not to make an activity diagram for every use case, but the ones that are difficult to understand or implement.

#### Describe the steps to reach the goal

It’s difficult to predict what the user does, and in what order. For that reason, an activity diagram helps us to map what activities the user performs, and also covers decisions we might not be aware of. It can also be used to describe activities from a non-user, for instance a part of the app that waits for something before it can execute. The focus is to describe the workflow.

#### Express ideas through design

When I was working in a team, a senior engineer handed me an activity diagram of a feature he wanted to be implemented. The whole development process became a lot easier because I didn’t have to guess how the app behaves, the behavior was already described through an activity diagram.

In general, it’s a great tool for expressing ideas and thoughts to people rather than just relying on verbal communication.

### 4. State-machine Diagram

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJFctGbCz-p_LVm2VmsVGA.png)
_State machine diagram — Content state_

#### Define the states

The purpose of the state machine diagram is to describe a discrete behavior of the app. The difference between an activity diagram and a state-machine diagram is that the former describes the steps to achieve something (workflow), while the latter describes how the states of an object change over its lifetime.

Both are useful techniques to describe the app’s behavior, and are helpful for clients and developers to gain common understanding of how things work.

### Final thoughts

Design is in constant motion and evolves and changes throughout the development process. As mentioned above, tackling design issues such as UI/UX and prototype sketches is important, but doesn’t really describe how the underlying parts of the app work or communicate. It also requires having educated graphical designers, and a lot of resources.

For that reason, we need something that is not design-dependent, something that doesn’t focus on minor details such as font-types, box-shadows, colors and so on.

We need Systems Engineering techniques to describe how the app behaves and interacts, to express ideas, simplify the development process, and help people with non-technical backgrounds grasp the apps behavior.

> Note, there are set of rules that should be followed when creating such diagrams, however, most people I’ve worked with do not understand or actually care about these rules. So the best tip I can give is to make sure you follow the purpose of the diagram, but don’t draw yourself into the rules such as if the line should end with an arrow head, diamond and so forth.

Here are a few other articles I’ve written about the web-ecosystem along with personal programming tips and tricks.

* [A practical guide to ES6 modules](https://medium.freecodecamp.org/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [How to perform HTTP requests using the Fetch API](https://medium.freecodecamp.org/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547)
* [A comparison between Angular and React](https://medium.freecodecamp.org/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76)
* [Boost your skills with these important JavaScript methods](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [A chaotic mind leads to chaotic code](https://medium.freecodecamp.org/a-chaotic-mind-leads-to-chaotic-code-e7d6962777c0)
* [Developers that constantly want to learn new things](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4)
* [Learn these core Web Concepts](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)
* [Program faster by creating custom bash commands](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

You can find me on Medium where I publish on a weekly basis. Or you can follow me on [Twitter](http://twitter.com/dleroari), where I post relevant web development tips and tricks.

