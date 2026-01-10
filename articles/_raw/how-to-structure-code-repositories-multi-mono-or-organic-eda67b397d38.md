---
title: 'How to Structure Code Repositories: Multi, Mono, or Organic?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T11:26:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-structure-code-repositories-multi-mono-or-organic-eda67b397d38
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bk93-RBsMVGgEhYozK2SgQ.jpeg
tags:
- name: engineering
  slug: engineering
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Chetan Sharma

  The newest debate in town is whether you should keep your services in a single repository
  or multiple small repositories.

  The idea of multiple small repositories is that code for each of your app’s micro
  service is kept in a reposito...'
---

By Chetan Sharma

The newest debate in town is whether you should keep your services in a single repository or multiple small repositories.

The idea of multiple small repositories is that code for each of your app’s micro service is kept in a repository of its own. With a mono-repo, you keep the all the code in a single repository and deploy the code as microservices.

So which should you use? Being too rigid about any one approach — without considering the purpose and uses of each approach — can lead to negative outcomes in the long run. If you’re aware of when to use each, it can increase your productivity and improve your project.

### To bend the rules, we need to first understand why they exist.

A common recommendation is to have an independent repository for every app/service. But why? Because, by having one repository for each micro-service, we gain:

* **Freedom** to write code differently and independently of all other services.
* **Velocity** in making code changes while fixing bugs, making updates, testing and deploying. Since changes only have to be tested in a single repository, deployment of the code is faster and more reliable.
* **Separation of code** as independent units, which prevents bug leakages and performance bottlenecks between services.
* **Clear ownership** of each repository and service, which is especially helpful for large teams.

### But why did the need for mono-repos arise?

Clearly, the multi-repo approach has its benefits. But it also comes with its own challenges, especially in projects with a large number of microservices that use the same frameworks, language, tech stacks etc.

A few of these challenges are:

* **Enforcing standards and best practices** across all repositories. With a multi-repo, changes in code standards and best practices need to be replicated across repositories. With a mono-repo, all the changes can be done in one place.
* The effort of **maintaining shared or common components**. Security patches, version upgrades and bug fixes involve making sure that these changes are made across all repositories and that they work seamlessly everywhere. (On a side note, the repeated code in each service also bloats its size.) In a mono-repo, we can make updates in one place, saving both time and headaches.
* **End-to-end testing** in tandem with closely related or dependent services right from the developer’s machine. By having all the code in one place, we ease the process of starting up all the related services and running end-to-end tests.
* **On-premise deployments** of code for other businesses. By deploying a mono-repo as microservices, we save time and reduce the redundant effort of bootstrapping each repository.

Clearly, there are advantages and disadvantages to both approaches, and each approach will have its own benefits under different circumstances.

Therefore, we have adopted the approach of remaining flexible and using both multi-repos and mono-repos, but only after completely understanding why we have chosen to use each for each service. This has led us to have multiple repos containing several microservices, segregated in a way that has made:

* Maintenance and updates both easy and fast.
* Locating the code to debug or change much more structured.
* Onboarding new teammates easier.

### How we decide what type of repository to use

The following considerations have helped us decide when to use mono-repos vs. multi-repos.

#### 1. Think about the code that will serve as the foundation of the service.

> _Begin by identifying any similarities in code, maintenance, and updates. If multiple repositories have identical code, it would be better to club them in a single repository._

The freedom to write code differently and independently in a service is one of the benefits of multiple small repositories. But often services will have a lot of identical scaffolds if they use the same language, framework, logging, bootstrap scripts, middle-wares, etc. Reusing these shared scaffolds saves time.

For example, [Collect](http://socialcops.com/collect) — our primary data collection tool — has multiple micro-services built on an identical framework. These services are built on [Node.js](https://nodejs.org/en/), [Express](https://expressjs.com/) and [Parse Server](https://parseplatform.org/). They share a lot of libraries like [Winston](https://github.com/winstonjs/winston), [Mongoose](https://mongoosejs.com/) and other third-party integrations. Earlier, when each of these services had a repository of its own, updating or fixing a bug in any of these shared modules meant updating and testing each repository separately. This was slow and cumbersome.

However, when we clubbed them together in a mono-repo, testing and updating the shared modules became easier and faster. Applying security patches and enforcing standards became easier since developers can do all the changes in once place.

The potential risk of a mono-repo is that a developer can reuse code originally written for an unrelated module. When the two modules share code, then change in this common code can lead to bugs. If these bugs go unchecked, they can affect the CI/CD (Continuous Integration and Delivery) pipelines of unrelated micro-services. To avoid such issues, it is important to have a strong testing suite in place.

#### 2. Check whether you have any modules that are very distinct from the rest.

> _Are you developing a module that demands a very different technology, language, framework or persistence? Then separating it out into a separate repository will be better._

In Collect, there are services that handle processing of events in bulk. They maintain queues, execute custom scripts and have a completely different error-handling mechanism. These services are written in Python, and quite often they need to do CPU-intensive tasks.

So when we were thinking about restructuring the code for Collect, keeping these services in a separate repo came across as self evident. These services were very different from Collect’s main repository (described above). While the main repository was for user-facing requests, this repo was all about background tasks and executions. Also, the change management in these services was going to be different and isolated from the main repository.

Thinking about the code maintenance and how it is going to evolve over time led us to club these services in a separate repository. By doing that, we were able to put up a completely different change management system, which turned out to be very helpful and more productive.

#### 3. Consider the uncertainty and therefore the frequency of changes a service might go through.

When you start working on something that is highly uncertain (either in terms of the scope of the problem or the implementation itself), then having a different repository can give you with the velocity and freedom you need to test things.

For example, say that you want to test a new way of processing images to identify objects. You want to dabble with machine learning, but you are still unsure how it will evolve or if the problem statement will change dramatically. In this case, it would be clearly better to have a separate repository and then get to a point of certainty. Conversely, if you think that the API has reached stability and will remain unchanged for a large amount of time, you can take a call to merge it with one of your main repositories.

The blog was originally published on [blog.socialcops.com.](https://blog.socialcops.com/) The above is how we handle our repository decisions. I hope it can help you in thinking from first principles if you approach this problem. Do [subscribe](https://share.hsforms.com/1Ag85PQHyTgCzyx00Col3Sw1d0o3) to our newsletter for more updates from [SocialCops](http://www.socialcops.com) Engineering and Data Science Team.

