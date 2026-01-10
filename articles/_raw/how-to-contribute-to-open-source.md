---
title: How to Contribute to Open Source Projects – Non-Technical Things You Should
  Know
subtitle: ''
author: Ayu Adiati
co_authors: []
series: null
date: '2023-09-14T17:34:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-contribute-to-open-source
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/How-to-Contribute-to-Open-Source-Projects-Non-Technical-Things-You-Should-Know--1-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: null
seo_desc: 'I''ve contributed to open-source projects for a few years and learned a
  lot from the process. These experiences allowed me to look closer at the open source
  flow, from the technical, such as Git and GitHub, to the non-technical aspects.

  Although they ...'
---

I've contributed to open-source projects for a few years and learned a lot from the process. These experiences allowed me to look closer at the open source flow, from the technical, such as Git and GitHub, to the non-technical aspects.

Although they are as important as the technical sides, the non-technical ones often get overlooked. In this article, I will share the essential non-technical things you should know when contributing to open source projects. 

## What are the Important Files in a Repository?

In this section, we'll talk about some of the important files you'll likely come across when contributing to an open source project.

### The `README.md` File

When you're interested in contributing to an open-source project, you should always read the `README.md` file — commonly called README — to familiarize yourself with the project.

The `README.md` file is the face of the project, containing everything essential. You'll usually find most, if not all, of these sections in a README:

* The project's description.
* The technology used for the project.
* Instructions on how to install, run, and use the project.
* The project's license.
* The code of conduct.
* How to contribute to the project.
* The expected communication style (through issue and pull request comments, GitHub discussion, chat service apps such as Slack or Discord, and so on).

### **The** `CONTRIBUTING.md` File

Next, you must know the rules to follow in order to contribute to a project. The procedures and requirements for contributing may differ between projects. For example, in some projects, you're required to comment on an issue before it gets assigned to you, while others allow you to assign an issue to yourself.

The `CONTRIBUTING.md` file serves as a contribution guide. It explains the community's rules and expectations from their contributors, from creating an issue to creating a pull request.

In most cases, you'll find a contribution section in the README. But if it's not included in the README, you can find it in a file named `CONTRIBUTING.md` or anything similar.

### The `LICENSE` File

You can't just assume that all projects on GitHub are open-source and that their codebase is freely available.

> "In most jurisdictions, any code or content is automatically copyrighted by the author, with all rights reserved, unless otherwise stated." (Source: [Open source licenses: What, which, and why](https://arstechnica.com/gadgets/2020/02/how-to-choose-an-open-source-license/))

"All rights reserved" means that no one may use, modify, or redistribute anything in the project unless the owner gives you permission to. If you ignore it, they can legally sue you. So, a project on GitHub is only open source if they have a license that specifies that.

You'd usually find a license section on the README, in the "About" section of a repository. It is found in a file called `LICENSE`.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/repo-about-section-github-1.png)
_An MIT license in the "About" section on the right sidebar of a repository on GitHub_

### The `CODE_OF_CONDUCT.md` File

You should habitually read the community's Code of Conduct (COC). The COC is the house rule of the community. It is there for a reason: to maintain a safe, welcoming space for contributors. Following the COC will prevent you from getting banned from the community and the project.

You can find the COC in a file called `CODE_OF_CONDUCT.md`, in the "About" section on of the repository. Most times, it's also included in the README and contributing guide.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/code-of-conduct-on-github.png)
_Code of Conduct in the "About" section on the right sidebar of a repository on GitHub_

## **Ethics in Open Source**

### Check for Duplication

Let's say you install and run a project on your local machine and encounter a bug. Or you read through the docs and find a missing step. You might want to raise an issue to address it.

Before doing so, you must check if a similar (open and closed) issue or pull request has been raised to avoid duplication. Enter possible keywords in the search bar on top of the issue or pull request page on GitHub to check for possible duplication.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/search-bar-github.png)
_Search bar on top of the issue or pull request page on GitHub_

For example:

```text
is:issue is:open docs 
```

```text
is:pull request is:closed button 
```

Checking for duplicates will help prevent your issue or pull request from getting turned down by maintainers.

### Ask for Permission before Working on an Issue

One of the essential ethics in open source is asking for the maintainer's permission to work on an issue unless stated otherwise in the contribution guide. Asking for permission helps the maintainers in controlling and avoiding duplicate pull requests.

You only want to work on changes and create a pull request after you get the green light from a maintainer. If you ignore this part and go ahead to work on the changes, your pull request will likely be ignored or turned down. This is because the issue may have been assigned to someone else already, or the issue may not be their priority at that moment. 

Either way, it would be a loss for you. So, what should you do when asking for permission?

#### 1. Check if the issue has already been assigned

You can see if an issue has been assigned by looking at the "Assignee" column when you open the issue tab in the GitHub repository or on the right sidebar when you open the issue.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/issue-tab-github-01-3.png)
_Assignee column on the issues page on GitHub_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/issue-right-sidebar-01-3.png)
_Assignees section on the right sidebar of the issue page on GitHub_

#### 2. Check the comment threads

You also want to make sure that someone has not already asked the maintainers to assign the issue to them. If they haven't gotten any response, then the maintainers have probably not seen the comment. You should also check other information in the threads to understand more about the issue.

#### 3. Leave a comment to request for an issue you want to work on

You can say, "Hi, I want to work on this issue. Can you assign it to me?" Or, "I see this issue has been assigned, but I haven't seen any activity here in a while. If you still need help, can I work on this?"

#### 4. Wait until the maintainer replies to your message

If they (the maintainer(s)) say you can have it and assign it to you, then you can start working on the issue and, in the end, create a pull request.

### What is the Good First Issue Label? 

Labels on GitHub are tags that pass information about the type or the status of an issue or a pull request. A `good-first-issue` is a label considered appropriate for beginners by the project's owner and maintainers.

I once created an issue about a broken link. I explained the bug and the steps contributors must take to resolve it.

I also mentioned that this issue is beginner-friendly, so we want to leave it for beginners who wish to contribute to the project. After passing the review from the maintainers, the issue was labeled as a `good-first-issue`.

The sad part was that people who deliberately took the issue were not beginners.

If you already have some experience, please consider leaving this label. It is meant for beginners in open source or the technology used in the project.

### Good Communication and Patience

Always use clear and polite words to communicate with maintainers and other contributors. Remember that async communication is prone to loss in translation and miscommunication.

If you need more clarification on something, ask the maintainers. Don't make assumptions. You can ask questions in the issue or pull request comments. Some communities also have a GitHub discussions board that you can find on the top bar, while some use chat service apps like Slack or Discord to share ideas and ask questions or clarifications.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/discussion-tab-github.png)
_Discussions tab on GitHub_

A maintainer may ask you to fix something in your pull request or ask for clarifications using a straightforward sentence. Short and direct messages mostly happen because they are busy. They must be fast and effective in replying to messages. Don't take it personal as this may lead to poor communication or even lead to losing your chance at contributing.

Most of the maintainers and contributors in open source are volunteers. That said, they have life and other duties outside of the project. So, when you're contributing, you need to have patience. Don't ask maintainers to immediately answer your question or merge your pull request.

### Write Issue and Pull Request in a Structured Way

Some open-source communities provide templates on GitHub for opening an issue or creating a pull request. But when they don't, consider writing them in a structured manner. It would be handy for everyone to see the details and help maintainers review and merge pull requests.

#### How to Write a GitHub Issue

Here are some things to consider when writing an issue:

**Use c**lear and descriptive title**s**: By reading a clear and descriptive title, everyone can understand the issue. For example, "fix: Link to the About page leads to 404".

**Search** for **similar issues**: Check open and closed issues to see if there is a similar or identical issue as yours. If you don't find any, then include in the description that you've checked and did not find any similar issues. This step is essential to avoid any duplication.

**Description of the issue**: Describe the issue as straightforward as possible.

**Expected behavior**: Describe the expected behavior of an issue.

**Actual behavior**: State the actual problematic behavior that causes the issue.

**Reproduce the problem**: What steps do we need to take to reproduce the problem? It would be helpful for everyone to run the same steps and test it out. Here's an example:

```markdown
1. Go to this link.
2. Click this button.
3. This is what is happening.
```

**Screenshots or screen recording**s: Provide some screenshots or screen recordings if necessary. It is usually beneficial for UI issues.

**Suggest a solution**: If you have a solution in mind, you can give a suggestion. But if you don't, it's okay too. You are not expected to have a solution when you raise an issue.

Here's an examples that uses the points listed above:

```markdown
<!-- Issue title -->
# fix: Link to the About page leads to 404

<!-- Issue body -->
## Description

When I went to the About page, I got a 404.
I have searched and didn't find any similar issues.

## Expected Behavior

We should see the About section when we go to the About page.

## Actual Behaviour

When we go to the About page, we see a 404 page.

## How to Reproduce

1. Go to the https://website.com.
2. Click the About tab.
3. You will see the 404.

## Screenshots

![404 in about page](link to the image)

## Suggestion

Fix and use the correct link to the About page.
```

#### How to Write a Pull Request

Here are some things to consider when writing a pull request:

**Use a s**hort, clear, and informative title****: For example, "fix: Link to About page".

**Use a **clear description of the fix****: For example, "This pull request fixes the link to the About page that previously led to 404."

**Link to the** related **issue**: Include the link to the related issue. For example, "Fixes #123".

**Screenshots or screen recording**s: Provide some screenshots or screen recordings that shows the issue before and after the fix if necessary.

Here's an example that uses the structure above:

```markdown
<!-- Pull request title -->
# fix: Link to About page

<!-- Pull request body -->
## Related Issue

Fixes #123

## Description

This PR fixes the link to the About page that previously led to 404.

## Screenshots

### Before

![404 in about page](link to the image)

### After

![About page](link to the image)
```

## Good to Know: Contributing to Open Source is Not All About Code

I often hear that people — especially beginners — hesitate to contribute to open source because they need more skills or time to help with code. However, contributing to an open-source project is involves more than just code.

There are many non-technical ways to contribute to a project and its community, such as:

* Opening an issue when you see a bug or room for improvement.
* Reviewing issues and pull requests.
* Improving the project's documentation.
* Answering questions.
* Throwing ideas around the project.
* Onboarding new contributors.
* Mentoring other contributors.
* Writing a blog post or creating a video about the project.
* Promoting the project on social media, and many more!

## Final Words

Contributing to open-source projects is not all about understanding Git and GitHub. Some non-technical things are important for you to know, too. I hope this article helps.😊

If you liked and enjoyed this article, please share it. You can find other works of mine on my [blog](https://adiati.com), and let's connect on [X (formerly Twitter)](https://twitter.com/@AdiatiAyu) or [LinkedIn](https://www.linkedin.com/in/adiatiayu/)!

