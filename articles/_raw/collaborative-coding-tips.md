---
title: What is Collaborative Coding? Pair Programming, Mob Programming, and How it
  All Works
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-02T20:13:44.000Z'
originalURL: https://freecodecamp.org/news/collaborative-coding-tips
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/collaborative-coding-tips.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: pair programming
  slug: pair-programming
- name: teamwork
  slug: teamwork
seo_title: null
seo_desc: "By Andrej Kovacevic\nCoding can be challenging, but it can become a lot\
  \ easier if you have the right strategies and tools. \nAfter all, as noted software\
  \ engineer and writer Joel Spolsky says, \"it is harder to read code than to write\
  \ it.\"\nOne way to ma..."
---

By Andrej Kovacevic

Coding can be challenging, but it can become a lot easier if you have the right strategies and tools. 

After all, as noted software engineer and writer [Joel Spolsky](http://blogs.perl.org/users/buddy_burden/2013/12/perl-and-me-part-4-a-worthy-program-exceedingly-well-read.html#note1) says, "it is harder to read code than to write it."

One way to make your development projects more successful is with collaborative coding. This refers to the process of working on the code with a team or with another developer. In a project that uses collaborative coding, each team member helps build the code and checks it for bugs or errors.

Working in pairs or teams helps finished code contain [fewer mistakes](https://www.freecodecamp.org/news/how-to-be-a-team-player-in-the-tech-world-c78aa9f4e898/) and bugs, and this results in better code quality and projects being completed more quickly.

It also enables faster debugging and greater project resiliency, as this setup makes it easier for other developers to take over in case one of the developers has to leave the project.

But collaborative coding won't produce all of these benefits by default. Making them happen comes down to how you implement your collaborative development strategy and how you execute it. Here are four points to consider when doing so.

## You Need a Secure Development Process

Although having multiple sets of eyes checking a project's code should produce a net benefit for the code's security — it can also introduce a new type of vulnerability into the mix. This is because sharing code through a collaboration platform creates the possibility of a data breach.

Humans, after all, are the weakest link in the cybersecurity chain. So, the larger the team, the greater the odds that someone will make an unforced security error during development. 

And things like exposed or stolen login credentials can endanger a project — especially one that is designed to handle sensitive information like banking and personal details.

This means that project managers must choose a collaboration platform that's built with security in mind. Some collaborative coding platforms already have built-in security features, but others do not. And different types of coding projects will call for different feature sets, so there's no one-size-fits-all solution.

There are plenty of collaborative coding platforms that may fit the bill, however. [Teletype](https://teletype.atom.io/), for example, comes with end-to-end encryption and the option to use self-destructing messages. 

Another popular option is [Brackets](https://brackets.io/), which comes with data protection when interacting with third-party plugins and has a mechanism for preventing unapproved access and privilege escalation.

Some teams or developers might use established collaboration platforms not specifically designed for coding. Microsoft Teams, for instance, can facilitate casual coding collaboration. And although it's not an inherently insecure system, it has weaknesses that developers can address with an additional [Microsoft Teams Security](https://www.avanan.com/teams-security) solution.

These solutions include features like malware protection, URL protection, access control over confidential data, compliance tools, and security alerts – which all improve platform security significantly. 

Regardless of the platform you choose, though, it is important to use security tools or to install third-party security solutions that ensure the best possible security for your project.

## Choose the Right Platform for the Job

It's also important to recognize that security isn't the only consideration when you're choosing a collaborative coding platform. 

It's also critical to choose one that will provide every team member with the tools and resources necessary to do their job. The right platform should meet the following criteria:

### It's made for a specific programming language or ecosystem

There are many benefits in using a platform that is created for a specific programming language. First, it most likely has all of the tools necessary to efficiently work on a project in a particular language. And it won't have unnecessary features added to cater to other requirements and preferences.

A language-specific platform is also designed with best practices in mind for developers working with particular languages or frameworks. So, for example, when working with dynamic programming languages such as Go, Ruby, and Python, it is preferable to use a platform like [Cloud9](https://aws.amazon.com/cloud9/).

### It's fast to setup

Ideally, everyone involved should already be familiar with the collaborative coding platform that you'll use. But if this isn't the case, it's important to choose one that is easy to learn with minimal to no configuration involved. 

A platform that requires IDE, server, terminal, codebase, and library configuration along with other setup procedures is not the most suitable option for live coding between pairs or teams of developers.

### It should have a customizable user interface

Programming is a heavily detail-driven job and developers tend to have their own preferences when it comes to the user interface so they can work easily and conveniently. 

Forcing everyone to use a platform they are not comfortable with is not a good way to proceed with collaborative coding. So it helps to have the option to modify the UI or dashboard to some extent.

The bottom line is that the collaborative coding platform should be easy to use for everyone. Developers may be highly skilled people, but not everyone is a master of everything. Those who are collaborating should agree on a platform and working arrangement that works for everyone.

## Define Clear Team Roles at the Outset

We can categorize collaborative coding into three general setups: 

* pair programming
* mob programming, and 
* code sharing. 

And understanding the inner workings of each of these setups is important, as different coding projects require different setups. 

But it's equally important to understand the roles of the team members in each setup and to define them before beginning to code.

As the phrase suggests, [pair programming](https://www.freecodecamp.org/news/things-ive-learned-from-pair-programming-interviews-35a4db7d7443/) involves two participants. Usually, one serves as the driver and the other acts as the navigator. The driver writes the code while the navigator reviews the output. 

In this setup, the driver is responsible for the tactical aspects of the job while the navigator sets the strategic direction of the code. The two may then switch their roles to have a more thorough look at what they have produced.

[Mob programming](https://searchsoftwarequality.techtarget.com/definition/mob-programming) is similar to pair programming but involves more than two people. To avoid making it a chaotic or disorganized arrangement, it is also important to have the driver-navigator role assignments. 

It is slightly more complicated, though, because there are more than two developers who have to agree on how to assign the driver-navigator roles. This means that clear communication and mutual respect are crucial.

The code-sharing setup does not require a driver-navigator dynamic. Instead, the collaborating developers only share their respective code to allow each other to review, modify, debug, or add to each other's code. 

This is the type of collaboration that open source developers tend to rely on because it allows newcomers to participate at will and existing developers to pause their work whenever they need to.

The participants here may work on the code together in real-time or asynchronously. What's important is that they have a reliable system for version control. 

That's where version control systems like [Git](https://git-scm.com/) excel. They help teams to avoid doing duplicate work and make sure that all developers are reviewing, revising, or adding to the latest version of the code at all times.

## Create Skill Balanced Teams for Best Results

While some would consider collaborative coding as an [opportunity to learn](https://www.smashingmagazine.com/2020/04/collaborative-coding-ultimate-career-hack/) from more experienced and proficient coders, that doesn't mean every collaborative project is conducive to that. 

This is because for certain types of projects, having too much of a disparity in the skill level of team members can grind the whole project to a halt.

This is a problem that feeds one of the biggest criticisms of collaborative coding as a development method. When team members must contribute as equals but lack the skills to keep up, progress stalls. When time is of the essence, creating a skill-balanced team is the only option.

That said, collaborative coding can be an opportunity for collaborative learning, but only when deadlines aren't involved. In that scenario, team members can take their time to learn from the work of their more experienced peers. And in the end, everyone benefits from the experience.

But if the goal is to make the project a collaborative learning endeavor, it is important to make that clear from the get-go. Otherwise, the more experienced developers could feel like they've been duped into providing training instead of getting the project done. And that never ends well.

## Conclusion

The advantages of collaborative coding are undeniable — but there are drawbacks to consider too. 

So, before deciding to go into the collaborative route, it is important to carefully scrutinize the pros and cons as they relate to a specific project. 

And for developers who wish to try their hand at collaborative coding, it's a good idea to get familiar with the popular tools and platforms used for such projects beforehand. That way, both the project planners and team members will get the most out of the collaborative process — but without encountering some of the issues that it can entail.

_Featured photo by snowing 12 - stock.adobe.com_

