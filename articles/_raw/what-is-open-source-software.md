---
title: What is Open Source? How to Contribute to OSS Projects
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2022-08-16T20:23:53.000Z'
originalURL: https://freecodecamp.org/news/what-is-open-source-software
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-ben-taylor-109998.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: FOSS
  slug: foss
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: null
seo_desc: "In this article, we'll talk about open source software. Open source software\
  \ is often considered free software. \nIn this article, I'll give a high-level explanation\
  \ of what open source software (OSS) really is, its advantages in the modern technologi..."
---

In this article, we'll talk about open source software. Open source software is often considered free software. 

In this article, I'll give a high-level explanation of what open source software (OSS) really is, its advantages in the modern technological world, how to use it, and some best practices to follow when using or contributing to an OSS project. 

You will learn about widely used tools and techniques like GitHub and continuous integration, as well as what license to choose and how to promote diversity in open source projects.

You will also get to make your first open source contributions if you haven't done so already.

Both maintainers and contributors to open source projects should read this article.

## Table of Contents

* [What is OSS](#heading-what-is-oss)?
* [What is Proprietary Software](#heading-what-is-proprietary-software)?
* [Open Source Governance Models](#heading-open-source-governance-models)
* [Why Use Open Source Projects (Advantages)](#heading-why-use-open-source-projects-advantages)?
* [How to Work on an OSS Project](#heading-how-to-work-on-an-oss-project)
* [How to Contribute to Open Source Projects](#heading-how-to-contribute-to-open-source-projects)
* [Helpful Contribution Tips](#heading-helpful-contribution-tips)
* [Continuous Integration and Delivery](#heading-continuous-integration-and-delivery)
* [OSS Licenses and Legal Issues](#oss-licenses-and-legal-issues)
* [How to Choose a License for Your OSS Project](#how-to-chose-a-license-for-your-oss-project)
* [How to Build Better Open Source Software Projects](#heading-how-to-build-better-open-source-software-projects)
* [Understand that Leadership is Not Control](#heading-understand-that-leadership-is-not-control)
* [Why Many OSS Projects Fail](#heading-why-many-oss-projects-fail)
* [Diversity in OSS](#heading-diversity-in-oss)
* [How to Use GitHub for Hosting OSS Projects](#heading-how-to-use-github-for-hosting-oss-projects)

# What is OSS?

OSS stands for Open Source Software. This type of software has freely accessible source code under a license that lets you examine, modify, and use that code without restriction.

# What is Proprietary Software?

As opposed to OSS, many companies use proprietary software instead. Only the owners of proprietary software have complete access to the source code. Trusted partners can inspect the code once they've signed a non-disclosure agreement.

When using proprietary software, you must agree to a license that limits your ability to share the product.

# Open Source Governance Models

Any organization that wants to succeed needs to be organized. It's important to carefully consider how the organization make decisions and who makes them. 

Establishing a Governance Model helps determine how you can accomplish this. Let's talk about some of these models now.

### Company-led Governance Model

In this model, software development and release management is handled by a single entity. 

* External contributions may or may not be requested.
* Plans and release dates may not be publicly disclosed, and unofficial conversations may not be made public.
* Software is in the open (that is, it's public) when it is released. 
* An example of this model is Android by Google.

### Benevolent Dictatorship Governance Model

In this model, one individual has a dominant influence over the software – hence the term "dictator" (but in a much more positive sense here).

* The quality and effectiveness of the project are greatly influenced by the dictator's intelligence and managerial ability
* As a project matures, the maintainer writes less code, which can cut down on discussions and speed up progress.
* An example of this type of governance is Wikipedia

### Board of Governors Governance Model (Tighter Regulation)

* All discussions are public via mailing lists, and collective choices are taken.
* The governing board decides who may contribute and whether new software is accepted.
* Releases are sometimes made less frequently, but they are carefully debugged. 
* Examples are Debian and FreeBSD

# Why Use Open Source Projects (Advantages)

There are quite a few advantages of going into open source development. Here are some of them:

* You collaborate with other contributors and often get better results
*  The source code is often more secure and higher quality 
* Using OSS best practices helps developers become better
* It reduces the development cost
* It decreases the time to market
* Customers can trust the quality because there are no secrets and they know what they are getting
* You'll have access to a vast array of inexpensive or free instructional aids for education and learning
* It's a good way to introduce beginners to the workplace

# How to Work on an OSS Project

## How to Contribute to Open Source Projects

Before contributing to open source projects, you should do some research around the project. Here are some ways to prepare:

### Investigate the project

Before you start working on a project, you'll want to learn more about it. First, you should identify and understand the project workflow and styles it uses. Second, you should figure out the scope and nature of the work that needs doing.

### Learn About its Communication Methods

Identify how the project maintainers communicate, either through study archives, a mailing list, or some online groups or chat platform.

### Figure Out How Contributions Are Submitted

Contributions to the OSS project can be in the form of a mailing list, email, or – perhaps most commonly – through the Git version control system.

### Study the Project's Previous History

Studying the history of the project is always a great idea so you know how it started and how it's been developed. Check if the project offers veteran contributors as mentors.

### Be the Janitor at First

Offer your services for testing, finding bugs, and so on before you begin to submit code. This is healthy for beginners and people new to the OSS lifestyle. It's meant to be a temporary stage.

### Understand the Project's Language

People frequently get interested in learning new programming languages by participating in open source projects that use those languages. But don't use the project as a way to **learn the language**.

Before thinking about making a software contribution, you should have some familiarity with the language. Most maintainers want qualified contributions only – they likely don't have time to teach you Python or JavaScript, for example. 

So make sure you are proficient in the programming language(s) the project uses before contributing. Don't begin learning with a project.

### Be Respectful

Being polite and respectful is an integral part in the OSS community as it involves diverse people. Always avoid flaming and trolling, as they have no place in the open source community.

### Find a Balance

Try to achieve a balance between asking for feedback and suggestions early in the process and delaying your requests too long and overloading maintainers with a bunch of work at once.

### Study and Understand the Project's Structure (DNA)

Most likely, the project already has a formal or informal leadership structure and a community-established culture.

Look into the project's purpose and the impetus behind it. Learn about how big or small the contributions typically are, how vibrant the community is, and what kind of license is being used.

## Helpful Contribution Tips

To successfully make contributions to open source projects, there are some best practices you can follow.

First, you'll want to identify the maintainers, their work, and their techniques‌‌. There are projects with a single maintainer or many maintainers for individual subsystems.‌‌ 

Maintainers have various responsibilities as well. They need to be able to understand and review all submissions and verify that they do not add unnecessary complexity or defects. They should also make sure that these changes don't conflict with existing code.

You can develop a rapport with project maintainers and help them with debugging, reviewing, and other tasks as needed.

It's also important when you're working on a project to get input early and work in the open.

Here are some other quick tips to keep in mind:

1. The project probably has a lot of history, so check to make sure your issue hasn't already been resolved or someone else hasn't submitted a pull request to fix it. Your proposal might be a dated one.
2. Don't propose a fresh idea and have someone else carry it out. This shows that you're not committed to contributing.
3. If you are uncomfortable having other people look at your work often, OSS might not be the best fit for you. However, it could be an opportunity to learn how to take feedback and constructive criticism.
4. Contribute a little bit at a time – don't make a large code dump all at once.
5. Leave your ego at the door. You will sometimes get hash reviews and you need to be able to calmly internalize the feedback.
6. Do not discriminate against others.
7. Be patient and work to develop long-term professional relationships with others in the OSS community.

## Continuous Integration and Delivery 

When you're working on an OSS project, there will probably be established guidelines for the codebase to prevent conflicts, since many contributors will be working together on it. Testing can also help make sure the code works as it should.

### What is Continuous integration?

Continuous integration techniques help ensure that testing is done often and that any issues won't go undiscovered for long. CI also helps make sure that scattered developers remain in sync, even if they're collaborating remotely all over the world.

The different stages of continuous integration are Integration, Delivery, and Deployment.

* **Continuous Delivery**: Translates to the practice of having a speedy and automatic delivery or release process once charges have been merged, and it is released to build clients.
* **Continuous Deployment**: When the product is actually released to clients

Examples of some continuous integration tools are:

* Jenkins
* CircleCI
* GitLab
* Travis

![continuous integration and delivery](https://www.freecodecamp.org/news/content/images/2022/08/cd.png)
_**Continuous integration and delivery process**. credits: [Ronak Kumar Samantray](https://substack.com/profile/2655972-ronak-kumar-samantray)_

### What Benefits Do CI/CD Have for OSS?

When a bunch of contributors are working on various aspects of a project from various perspectives and places, it must come together and not be in conflict. Additionally, fixing one issue shouldn't lead to the emergence of new issues elsewhere. 

To accomplish all this, you must use some automated testing. So when testing, you should take into account many factors, such as:

* Whether you may implement modifications that overlap at the same time.
* Whether there are any conflicts.
* If the project is still able to compile after the changes are applied.
* If you make all the necessary changes, can you ship it?
* Does it work on all possible targets?

By ensuring that testing is constant, automated, and performed regularly, any problems that arise are swiftly fixed, and developers and users remain on the same page. And **Continuous integration** makes sure that any of these issues are minimized.

## OSS Licenses an Legal issues

### What is an Open Source License?

An open-source license is a sort of license for software that permits the use, modification, and/or sharing of the source code, blueprint, or design under specific terms and conditions. 

Then end users or developers can review and modify the source code, blueprint, or design for their own use cases, curiosity, or troubleshooting requirements. Although it is not always the case, open-source licensed software is typically offered free of charge.

There are two types of software licenses that OSS projects generally use:

* **Restrictive** – the software remains open, but it has strict restrictions on any attempts to create proprietary closed goods. Changes to the code are also made available to future recipients, such as the GPL License.
* **Permissive** – these licenses don't demand updates and alterations to be publicly accessible, such as BSD and Apache fences.

Companies should consult with lawyers, either internal or external, to ensure that they do not violate copyrights and licenses when using code from open source projects. 

There are many different licenses, so be careful. But once an organization establishes proper standard operating procedures, they must follow them for every project. 

OSS Licenses help gives contributors a better idea about how to use and contribute to the source code.

### Most Common Licenses

* GNU General Public License (GPL) 
* MIT license
* Apache License 2.0
* BSD 3-Clause "New" or "Revised" license
* BSD 2-Clause "Simplified" or "FreeBSD" license
* GNU Library or "Lesser" General Public License (LGPL)
* Mozilla Public License 2.0
* Common Development and Distribution License

### How to Choose a License for Your OSS Project

This is a crucial choice that has to be carefully considered because it may be difficult or even impossible to switch to a different license later in the project's existence.

Here are some things to consider when choosing one for your project:

* If you need a simple and permissive license, the MIT License is succinct and direct. It gives users practically unlimited access to your project. Examples of projects that use the MIT License include .NET and Rails.
* If you are more concerned about sharing improvements, almost everything can be done with your project under the GNU GPLv3, with the exception of disseminating closed source versions. Examples of projects employing this license include Ansible and Bash.

Read more about choosing the best license for your project suit [here](http://oss-watch.ac.uk/apps/licdiff/) and [here](https://choosealicense.com/).

# How to Build Better Open Source Software Projects

## Understand that Leadership is not Control

An effective leader allows and encourages all participants to speak up and share their ideals while contributing. This often leads to more creative, high-quality work. So remember: loosen the reins when you can.

According to the well-known leadership paradigm known as the "Benevolent Dictator for Life" (BDFL), a project's controllers can only do so much if they take without giving back via teaching and moderating.

Also, if you're a maintainer, make sure you go through some training to learn how to be a good leader. Having a good mentor, for example, is vital in helping you acquire the information and skills required to become a good maintainer.

If the maintainer isn't helpful or supportive, new project participants will often move on to another project if they can't connect with an experienced contributor.

And finally, remember that an open-source project cannot succeed without trust. Reputations are built up over time, and new members should be cognizant of the past.

## Why Many OSS Projects Fail

Most successful open source projects started off small and grew slowly. It's often hard to predict which projects will be successful and which won't.

Some of the reasons OSS project fail are:

1. They try to do the same thing as more mature programs.
2. They don't have good leadership.
3. There's a general lack of interest in their product/service.
4. They don't have enough developers
5. They don't have the correct license.

To combat these issues, here are some things to keep in mind:

* Make sure you have good and effective leadership, because this leads to more creative, high-quality work.
* Make sure your project has a well-defined governance structure and license.
* Encourage developers working on your project by providing resources and information to help them start contributing.

## Diversity in OSS

The word "Open" in open source software (OSS) may be taken to mean a welcome, friendly environment. But this may only be a false promise if the project doesn't cultivate a welcoming atmosphere.

There are various forms of diversity, such as nationality and race, sex and gender identity, regional or geographic location, politics and belief systems, and so on.

It's important to respect and foster diversity in whatever ways you're able to do so. Some ways to foster diversity in the OSS space include:

* Respecting peoples beliefs and religions
* Not being biased against contributors for any reasons relating to race, sex, gender identity, location, beliefs, and so on.
* Valuing the contributors of all your contributors and engaging with them whenever possible.

## How to Use GitHub for Hosting OSS Projects

Before GitHub, projects needed their own servers to host repositories. They also needed developers with extensive technical skills to set up, manage, and protect the repositories' integrity.

Developers can now primarily concentrate on the code by using GitHub or other Git hosting services like GitLab or Bitbucket.

### Types of Repositories

There are two types of repositories on Git:

* **Public Repositories** that are accessible to everyone on the internet.
* **Private Repositories**, which are only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members.

### Hands-on practice using GitHub for collaboration

Now we'll go through some basic steps, which, when you get them down, will provide you with the ultimate superpower in effective collaboration.

We will understand more fully by building a name biography website. So let's dive in:

**Here's the** [**Project Repo**](https://github.com/Caesarsage/OSS-Contribution-Beginer.git) **so you can follow along.**

#### Step 1 – Fork the repository

This is to create a copy of the repository of the project in your gitHub account for more accessibility.

Then, click on the **project link above** and then fork the repository. To fork a repository, click the fork button at the top right corner of the GitHub website of the repo.

![fork repository](https://www.freecodecamp.org/news/content/images/2022/08/fork.jpg)
_fork repository_

#### Step 2 – Clone the repository 

Cloning is creating a copy of the code online (your repository) on your local computer so you can work on it from there.

Cloning the repository on your computer is sometimes referred to as using a "**local repository**".

Click the code tab on the forked project on your GitHub and then click the copy code icon as show below:

![clone repository](https://www.freecodecamp.org/news/content/images/2022/08/clone.jpg)
_clone repository_

Now let’s go to your local computer. Open your favorite code editor (mine is VSCode) and open the inbuilt terminal. Then paste the code you copied after a 'git clone' command to clone this project repository to your local computer as shown below:

```git
git clone <your-copy-code>
```

Now in your terminal, move to the generated project folder with the code below:

```git
cd OSS-Contribution-Beginer

```

#### Step 3 – Create a branch from your local repository 

Branches allow you to make changes without affecting other contributors' code and the main branch. it is always good to create your own branch when contributing to projects.

To do this is simple – just write the following code:

```git
git branch ‘name-of-the-branch-you-want

e.g git branch caesar-name
```

Then you can switch to the branch you just created:

```git
git checkout caesar-name

```

#### Step 4 – Make changes to the repository

In this scenario, our problem is to change the [README.md](http://README.md) to include your name, social media handle, and preferred emoji (you can browse how to get markdown emoji).

Scroll to the bottom of the [README.md](http://README.md) file. Add your name, social handles, and emoji to the list. Then save the changes.

#### Step 5 – ADD and COMMIT your changes

Adding and committing your changes is a way to save the changes you made into your local Git repository.

To achieve this, in your terminal run the following commands:

```git
git add .

```

Then commit the code:

```git
git commit –m “added my name bio”

```

#### Step 6 – Push it online

All we did in **step five** has been on your local computer or repository. Now it's time to push it to the original online repository on GitHub.

You can do this with the few lines of code below:

```git
git push origin –u ‘your branch name’
i.e
git push origin –u caesar-name
```

**Step 7 –  Make a pull request (PR)**

You can let people know about changes you've pushed to a branch in a GitHub repository by making a pull request.

Before your modifications are merged into the main branch, you can examine and validate the prospective changes with collaborators and the maintainer after you submit a pull request. You can even add follow-up contributions.

Go to your forked repository in GitHub online, see your resent changes that you just pushed, and click on compare and pull. Then click the create pull request button.

![pull request](https://www.freecodecamp.org/news/content/images/2022/08/github-comparepr.png)
_Pull request_

![pull request](https://www.freecodecamp.org/news/content/images/2022/08/open-a-pull-request_crop.jpg)
_pull request_

Hurray! Congratulations. 🔥💡 You've successfully made your first open source contribution.

# Summary

The open source ecosystem is a wide and interesting one, and you can benefit a lot from collaborating with others and making contributions.

In this article, you learned how open source projects work, what to consider when getting started, how to contribute, and how the different licenses work.

As always, I hope you enjoyed the article and learned something new. If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) or [Twitter](https://twitter.com/caesar_sage).

Cheers and see you in the next one! ✌️

