---
title: How making delivery your focus will help you build quality applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-26T01:05:59.000Z'
originalURL: https://freecodecamp.org/news/making-delivery-the-focus-techniques-for-delivering-quality-applications-222b79d301d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B8jyD4Cli4xIFtdTD4st_g.png
tags:
- name: agile
  slug: agile
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Simon Schwartz

  I was recently asked by our company’s executive team why our team was able to develop
  improvements to our product so quickly. This blog outlines some key guidelines,
  from a technical point of view, that our team followed to x iterat...'
---

By Simon Schwartz

_I was recently asked by our company’s executive team why our team was able to develop improvements to our product so quickly. This blog outlines some key guidelines, from a technical point of view, that our team followed to x iterate our product at speed safely. I tried my darndest to stay high level in this post while still providing technical details. The techniques we talk about aren’t things that we invented._

My fellow tech comrades on the team and I saw it as our role to reduce the friction to delivering value to our users. We also aimed to maintain a high quality of the applications we were responsible for. We did a large part of this by removing, simplifying, and automating the processes around delivering updates to our production codebase.

Keep in mind there are some projects that may have inherent complexity. Some of the techniques our team used may not fit your project. From my experience, working with legacy software can make it hard or impossible to simplify certain processes truly.

### Make delivery the focus

Our team prioritized delivering frequent improvements to the production codebase above everything else. Well almost — we put things like mental health, letting people take a day off if they were sick, and being nice ahead of delivery.

**Code in production is the goal.** We made sure that all ideas, designs and feature requests had a clear path for how we were going to get it to production. One technique we used to re-enforce this was only to show working code in showcases. We banned powerpoints and design mockups. We also found this made our showcases more engaging and interesting.

**Meetings are optional.** We found that this encouraged people who called meetings to articulate the purpose and value of the meeting clearly. It was up to team members to decide if they should attend a meeting. We wanted to prevent developers from being unnecessarily interrupted. It can take upwards of 30 minutes for someone to return to a productive state after being interrupted.

**Spend time solving user problems, not technology problems.** We wanted to avoid spending countless hours discussing what technology to use or building our own technology. We used [AWS Lambda](https://aws.amazon.com/lambda/) so we didn’t have to think about servers and scaling. We used [Create React App](https://github.com/facebook/create-react-app) so we didn’t have to worry about build configuration for our front end app. We made early tech decisions and stuck to them.

#### ? W**_hat we tried to avoid._**

* We avoided spending weeks building our own tooling or frameworks when we could re-use them from elsewhere.
* We avoided adding unnecessarily complex processes or ceremonies to the team. This included convoluted kanban boards or agile processes that weren’t benefiting us.
* We avoided spending weeks designing, building and supporting features that had **no proof** they would be useful to our users. Our design team did a great job of designing features based on user feedback and analytics.

### Make deployments a non-event

Having a rapid release cycle meant we could get new features out to our users as soon as they were ready. We also recovered from bugs and outages much quicker. A major challenge of high-frequency deployments is moving at pace without introducing bugs. Automating this process is critical as it vastly reduces the time and effort it takes to deploy updates.

**Automate the deployment.** Rapid delivery requires the deployment process to be as frictionless as possible. Luckily nowadays we have many tools that can automate the entire deployment process. I recommend tools such as [CircleCI](https://circleci.com/) and [TravisCI](https://travis-ci.org/). Our setup was when the new code was added to the release branch, the code was automatically deployed by our deployment tool.

**Write (and automate) tests**. When deploying code changes automatically, it is critical to understand the impacts the changes will have and to stop deployments that introduce bugs or regressions. This means we needed to write tests that confirm the code is functioning as expected.

Whenever we integrate new code to a release branch, the CI tool automatically runs our test suite. Any failures in the test suite will cancel the deployment process. Developers would also run this test suite locally to confirm everything worked before pushing changes. Automated testing is also much quicker, less cumbersome and less prone to human error than manual testing.

Delivering at speed doesn’t work if all new code needs to be manually tested by a human for an hour. As a team, we agreed that we would write tests for all the code we wrote. For cases where it wasn’t practical to write tests, we would need to give a reason. Any time we fixed a bug, we would also write a test that covered the bug. We made sure that we had tests for common user interactions and journeys (integration tests). As well as tests for the individual functions that made up our applications(unit tests).

![Image](https://cdn-media-1.freecodecamp.org/images/XaSYwzsMVr3-wvoSTa6b1-Zm2vwr5aY-OJtL)
_One of our automated test suits running built with [Cypress](https://www.cypress.io/" rel="noopener" target="_blank" title="). We simulate different actions our users may do and verified the correct data and user interface would be displayed. We can automatically run dozens of scenarios very quickly which would otherwise take hours if run manually._

**Small frequent updates.** Updating our codebase in small increments increased the rate we delivered improvements to our users. Small updates are easier to integrate into the codebase. Our code review process became more rigorous. It was easier and quicker for developers to review small pull requests. It is much easier to identify issues and impacts of new code because the surface area of the code was so small.

One technique we found useful was moving the design quality assurance(QA) audit process to the pull request level. This made the QA process more focused and quicker as opposed to when it carried out every few days on a large set of multiple changes. As a team, we made an agreement that we would keep PRs small.

We also agreed that we would review PRs within half a day. If we weren’t able to review within that time frame, we needed to let the author know.

#### ? W**_hat we tried to avoid._**

* We avoided manually doing tasks that we could otherwise automate.
* We avoided risks associated with deploying a large amount of code all at once. It’s not uncommon to deploy code that has bugs that are not picked up or bugs that only surface when the code runs at scale. The larger the surface area of our deployments, the larger the impact these issues will have.

### Make changing code simple and safe

> “To me, there is only one definition of well designed code. Well designed code is code that is easy to change” — Dave Thomas

Having the ability to deploy code changes on demand is pointless if changing the code is hard and time-consuming. Writing code that is easy to understand and update helps us iterate at speed. As a technical team, we kept each other accountable through our code review process to ensure we were writing code as clearly and simply as possible.

**Write modular and reusable code.** Functions are the building blocks of our applications. These functions should be small, decoupled and have a single purpose. This makes it easier for developers to follow and understand the logic of the application. It’s easier to repurpose existing functions to reduce the amount of code written. Changing functions is much safer because the surface area of function is so small. The effects of the change are easier to understand. As a team, we would carefully review each others pull requests and give feedback to help each other write the best code we could.

**Write code for humans.** There are two primary users of the code we write: computers who run the code and humans who read and change the code. Most developers are pretty good at writing code for computers. If your code runs or complies without bugs — it means you did a good job writing code for the computer. Some developers forget about writing code for humans. If the code is hard to understand it will take longer for developers to understand and update the code. We focused on making it clear the purpose, outputs, and inputs of each function.

The inputs and outputs of functions were made clear with the type system. We used the inbuilt type system when using Go, and Flow when using JavaScript.

We chose descriptive names for our variables. This made it clearer what data the variable held or what function is performed.

```
// Both these functions do the same thing
```

```
function a(arr) {  return arr.filter(it => it.age < 30)}
```

```
function getUsersUnder30(userList) {  return userList.filter(user => user.age < 30)}
```

**Write testable code.** Whenever we change the code we need to be sure our changes have not regressed the previous functionality of the code. This is one of the great benefits of having tests. It adds a level of safety to making code changes. We made our lives easier by writing code in a way that made it simple to write tests for. A technique for writing code that is easy to test, is to use _pure functions_.

A pure function is a function that given the same inputs, will always return the same outputs. These functions are super simple to test. If you are interested in learning more about pure functions [Eric Elliot](https://medium.com/@_ericelliott) has [a fantastic article describing pure functions](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976).

Unfortunately, you cannot write a function as a pure function if it has _side effects_. A side effect is something that operates outside of the scope of its function. This could be operations such as writing a file or sending an API request. Side effects can be tricky to test at the unit level, so these were separated from our pure functions.

#### ? W**_hat we tried to avoid._**

* We avoided wasting time manually testing scenarios that we could automate.
* We avoided compromising code quality for speed. Compromising code quality for speed is redundant. Not only are you more likely to introduce bugs, but you are also creating a codebase that will eventually be very hard to change and debug. This will significantly slow down your ability to deliver new features and bug fixes.

Thanks for reading!

