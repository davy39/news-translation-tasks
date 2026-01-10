---
title: How to Write Commit Messages that Project Maintainers Will Appreciate
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2023-11-11T01:16:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Commit-message-post.png
tags:
- name: best practices
  slug: best-practices
- name: community
  slug: community
- name: open source
  slug: open-source
seo_title: null
seo_desc: "You know the saying “If you keep looking at the past, you’ll miss the future”?\
  \ Well in the context of coding and working with Git, that’s not the case. \nYour\
  \ commit history plays a huge role in the future of the open source projects that\
  \ you contribu..."
---

You know the saying “If you keep looking at the past, you’ll miss the future”? Well in the context of coding and working with Git, that’s not the case. 

Your commit history plays a huge role in the future of the open source projects that you contribute to, and commit messages are key to making this possible.  

What are commit messages, you may ask? These brief explanations describe the changes you made to the codebase, and they're very useful if things like bugs occur. 

Commit messages are also great checkpoints if you’re getting back to an open source project that you have not contributed to for a while and need to remember the changes you’ve made so far. 

Feeling intimidated? No worries. In this quick guide, you’ll learn how to write effective commit messages.

## What Makes a Bad Commit Message?

Like most things in life, we have to learn about what makes an unhelpful commit message before we learn how to write a good one. 

Let's look at one example:

```git
mention information

```

Even though this commit message describes the change, it does not explain **why** the change was made, which can leave maintainers feeling confused. 

It also does not state **what** kind of information was mentioned. Maintainers might be wondering "Was is it a missing code snippet?  A link to a specific section?". These are things that you want to avoid when writing commit messages. 

Now that we’ve seen the bad, let’s learn how to turn this commit message into something that maintainers can understand.

## Characteristics of a Good Commit Message

Remember how I said the earlier commit message was a bit vague? Well, here’s how we can fix it:

### Step 1 – Mention the type

This is where you specify the kind of change you’re making to the codebase. This makes it easier for maintainers and other contributors to gain a better understanding of your contribution. 

Here’s how this step would look with the sample commit:

```git
feat: mention information

```

Since the sample commit seems to focus on adding some text, I decided to go with  `feat` because it often is used to describe contributions where information or a new feature is added to an open source project.  

Here are some other common abbreviations that are used to categorize commits:

* `docs`: This is commonly used to describe revisions to current versions of or updates to an open source project's documentation.
* `fix`: This is typically used for fixing bugs in the project's codebase or small grammar errors in the project's documentation. 
* `chore`: This is often used for a contribution that make take longer that usual to finish. 

### Step 2 – Summarize the change

This is where you give an overview of the change and how you did it. This helps maintainers understand how your contribution solves the problem you’re trying to solve. 

Now it’s important to note that GitHub has a 72-character limit so you'll need to keep your description within that range. Let's look back at our example:

```git
feat: mention information
```

Remember how I said that it does not specify the typo that was fixed? Well after doing some thinking, I decided to write this:

```git
feat: mentioning Christine Peterson in the course's intro
```

That's so much better! :) Unlike before, this version of the sample commit mentions the kind of information and specifies where it was added in the project. This helps maintainers gain a better understanding of why this contribution was made. 

### Optional Step – Add a description

This is where you describe the change in more detail by mentioning why you made it. While this step is optional, consider doing this so that maintainers can get an idea of how your contribution enhances or solves an issue in their project.  

Here’s how it would look with our sample:

```git
I decided to add this information so participants get accurate information.
```

When doing the description, I decided to keep the describe short yet specific. That way, it would help maintainers understand why I made this contribution and how it enhances the project. 

Now let's put these parts altogether:

```git
feat: mentioning Christine Peterson in the course's intro

I decided to add this information so participants can get accurate information
```

Now in comparison to the original example, this commit message is more effective because it does the following:

* Specify the type commit being made 
* Describes how the contribution enhances the project
* Summarizes the change 

Looks great right? 😉

## Wrapping Up

Whether you’re a new contributor or a seasoned veteran, writing commit messages effectively is crucial to communicating your contributions to maintainers. 

If you’re looking for more ways to step up your commit message writing skills, check out [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). Also, follow me on [BioDrop](https://www.biodrop.io/CBID2) to check out my socials and other technical articles.





  


  



