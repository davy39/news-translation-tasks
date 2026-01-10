---
title: 'Requirement Analysis: how to use this startup-friendly approach + a case study'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-28T17:11:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-analyze-the-requirements-of-a-new-product-a-startup-friendly-approach-and-a-case-study-833970e5c36c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*10Wu8Q4Oxj0JsvDbXGqJdw.png
tags:
- name: agile
  slug: agile
- name: Apps
  slug: apps-tag
- name: Case Study
  slug: case-study
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Turgay Çelik

  In our previous blog posts, we explained why we decided to develop the Badges App
  and how we evaluated the feasibility of our idea at OpsGenie:

  Since we found that our idea is worth developing, the next step is analyzing the
  requireme...'
---

By Turgay Çelik

In our previous blog posts, we explained why we decided to develop the [Badges App](https://engineering.opsgenie.com/badges-app-opsgenies-response-to-skill-tracking-and-management-challenges-c539feb1db9d) and how we [evaluated the feasibility](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9) of our idea at [OpsGenie](https://www.opsgenie.com):

Since we found that our idea is worth developing, the next step is analyzing the requirements.

Requirement analysis — a very well studied area of software engineering — is the process of determining user expectations for a product, or briefly defining the product scope. There are tons of available resources on requirements analysis methodologies, characteristics of good requirements and tracing requirements. Instead of repeating the literature, we are going to summarize the critical points in a startup thinking way.

We know, startup guys generally don’t like terms like “process”, “proof of concept”, “requirements”, “scope”, “schedule”, “design”, “documentation” or “maintainability”. Generally they are impatient and they just want to code and release. We accept that agility is vital in our world and we have to try, fail and recover fast. But benefiting from the heritage of the software world will help us on the way to success. The key point is keeping it agile.

Following a process is not an objective, it is a tool that helps us achieve our goals. So, let’s see how we can adopt classical approaches to our world in the context of requirements management.

[The Project Management Triangle](https://en.wikipedia.org/wiki/Project_management_triangle) is a model of the constraints of software management. Despite the fact that it is an old concept from the 1950's, I think it is still relevant.

In summary, project management triangle says that the quality of work is constrained by the project’s **budget**, **deadlines** and **features**. There is a trade-off among these three constraints to achieve the necessary project quality. So we can say that software development is a [multi-objective optimization problem](https://en.wikipedia.org/wiki/Multi-objective_optimization).

![Image](https://cdn-media-1.freecodecamp.org/images/owsDttjxHCqVOtiAj02sAeV5RQB-5K5z0FTY)
_The Project Management Triangle (Image from [Wikipedia](https://en.wikipedia.org/wiki/Project_management_triangle" rel="noopener" target="_blank" title="))_

We don’t like to constrain ourselves by classical approaches, so let’s adapt the old Project Management Triangle to the new startup world. Recall the Startup Success Factors that we mentioned at [Feasibility Analysis post](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9).

Here is how we map these success factors to the classical project management triangle:

![Image](https://cdn-media-1.freecodecamp.org/images/ztFEbFyTRgCO7ffOwMRFTvIcJtpnmcYbjh13)

As shown in the table above, all startup success factors relate to various project management triangle constraints. Since these three constraints are in a trade-off, we can say that keeping the scope neat is vital for the success of a startup.

To define a neat scope, we have to perform a good requirement analysis before starting the development. Please note that this does not mean we are going to perform a fully detailed requirement analysis just like defined in waterfall process. We are going to do it in agile way.

### Tips for Requirement Analysis

In this section, we will provide important tips that you should keep in mind:

#### Inspect Alternative/Similar Products In Depth

As always, don’t reinvent the wheel. Check what others do to meet your objectives. Even you may end up realizing that your product does not seem to have business impact that you were thinking before.

This is a good sign to pivot your idea. It may seem like a failure, but remember, **we have to fail as fast as possible**.

#### Document your requirements

You don’t have to use a requirements management tool such as [IBM Rational DOORS](https://www.ibm.com/us-en/marketplace/rational-doors). But a short, bulleted requirements document will help negotiate with the stakeholders.

#### Keep Your (Potential) Customers In the Loop

I think this is one of the most important things about requirements development. A capability that you think that is killer may not make sense to the customers.

To keep your potential customers in the loop, you have to follow an iterative approach. You can do this by shipping an initial version of your product — Minimum Viable Product (MVP) — and evolving it according to customer feedback.

For example, Amazon Web Services team utilizes this approach frequently. They ship a service with minimum capabilities and evolve it based on customer feedback.

Another approach is to develop mock applications that just provide a dummy user interface (UI) to help potential customer to understand the product features and give feedback. You can use products like [InvisionApp](https://www.invisionapp.com/) to produce these mocks.

#### Requirements Management is a Continuous Process

You don’t have to spend months for requirements analysis at the beginning of a project, and please don’t — it is not the agile way.

At the beginning, your objective is to define boundaries of the system, negotiate with the team and other stakeholders, and prepare the definition of the Minimum Viable Product. The requirements should be detailed or can even evolve during iterations of development.

#### Group your requirements

After you create a list all of your requirements, group them (divide and conquer) to form sets of related features. Grouping requirements to feature groups will ease your life during development phase and even it can help you to define [bounded contexts](https://martinfowler.com/bliki/BoundedContext.html), microservice architectures, and so on.

#### Think About UX

It is not necessary to say that User Experience (UX) is a very important factor in the success of a product anymore; today it is so obvious. But we have to still remind that User Experience is not just about fancy User Interfaces.

As the name implies, it is all about the “experience” and it is hard to improve a system’s UX after it is developed.

Think about UX starting from requirements analysis, it could even be a motivation during the feasibility analysis phase to develop a new product if available alternatives in the market lack good UX.

User Experience affects the business requirements. For example, if you are developing an e-commerce application, designing a fast responding customer support system is about improving the User Experience.

#### Be Agnostic of Implementation Technologies As Much As Possible

Of course this is not applicable if you are developing an infrastructure or a library for a specific technology :)

Don’t fall into “If all you have is a hammer, everything looks like a nail” trap. Find new tools and utilities instead of limiting product capabilities to the technologies that you are familiar with or that you enjoy playing with.

In enterprise companies, requirements analysis is generally performed by non-software engineers who are generally known as business analysts or systems engineers. This separation has some disadvantages, especially in terms of transferring requirements to development teams, but I think it also has some advantages.

In my opinion, the biggest advantage of independent analysis teams is that they are agnostic of the technologies that will be used during development.

But in the startup world, most probably as a team member (or even as a founder), you have to wear multiple hats: analyst, developer, hiring manager, or even more interesting roles that you were not imagining when you get in this path. So, if you are wearing the analyst hat at the moment, try to be agnostic of the technologies that you are planning to use during implementation.

We consistently hear expressions like “but Spring Framework does not support …” and “This causes a lot of work on the front-end” during requirement analysis.

Considering these kind of limitations at the start degrades the quality of the end product. Let’s define the ultimate capability and evolve it during development if necessary.

Ultimate capability is the final goal to reach, you can implement a more simple form of it when you start and evolve it in future versions. But knowing the point that we want to reach will help us to define our vision for the growth of the product.

For example, think about “pinch-to-zoom” capability of mobile phones. It seems like a trivial capability but it was a revolution when [Steve Jobs first demonstrated it](https://www.youtube.com/watch?v=ze559mhbrD0). If the designers of iPhone didn’t think out-of-the-box and stuck to the available technologies and methods, we would not have this great functionality today. We know that it is an exaggerated example, but the main point is, don’t let the technology you would like to use limit you, you can move to other technologies if this will help you to create a niche product.

### Requirements Analysis for Badges App

We performed requirements analysis according to the practices that we summarized above:

* We defined an initial set of requirements
* We shared the requirements with our initial customer — The OpsGenie team — and updated the requirements according to the team’s comments.
* At OpsGenie, we use Atlassian’s JIRA for issue tracking. To track the requirements, we created an issue with “New Feature” type for each requirement in JIRA.
* We grouped related requirements with [JIRA Epics](https://confluence.atlassian.com/agile/jira-agile-user-s-guide/working-with-epics). Some of our epics are User Operations, Group Operations, Badge Operations, Endorsement and 3rd Party Tool Integration.
* In further steps of development, we created detailed issues for daily tasks, as Agile practices recommend. We linked each task with one or more requirements to keep traceability of development activities with requirements.
* Each epic contains a set of requirements (such as a New Feature), Development Tasks, and Bugs.

![Image](https://cdn-media-1.freecodecamp.org/images/NV65NKbZ1GLiSwXILHrxsnRv18fgFbyX85nV)
_Tracing Requirements with Development Tasks_

Want to follow our Badges app, or better, recommend new features and help us refine it? [Join](https://community.opsgenie.com/c/badges) Badges App community!

Further reading:

[**Badges App: OpsGenie’s Response to Skill Tracking and Management Challenges**](https://engineering.opsgenie.com/badges-app-opsgenies-response-to-skill-tracking-and-management-challenges-c539feb1db9d)  
[_As we see skill tracking and management as a crucial task for the healthy growth of our company, we invested in a…_engineering.opsgenie.com](https://engineering.opsgenie.com/badges-app-opsgenies-response-to-skill-tracking-and-management-challenges-c539feb1db9d)[**How Did We Decide That Our New Product Idea Is Feasible?**](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9)  
[_So, we have a new product idea, and we think that it’d be “useful,” “great” and further, “It will make the world a…_engineering.opsgenie.com](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9)

