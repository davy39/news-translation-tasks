---
title: Mistakes Your Team Might Be Making When Writing User Stories - and How to Fix
  Them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-12T17:20:09.000Z'
originalURL: https://freecodecamp.org/news/user-story-mistakes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b15740569d1a4ca2997.jpg
tags:
- name: agile development
  slug: agile-development
- name: user story
  slug: user-story
seo_title: null
seo_desc: 'By Vikash Koushik

  There''s a lot of information out there on how to write user stories and why it''s
  important. And yet, many of us make mistakes that cost us a lot.

  There are many who even prefer an alternative method. (Here’s another one.) And
  it''s o...'
---

By Vikash Koushik

There's a lot of information out there on [how to write user stories](https://zepel.io/agile/user-stories/) and why it's important. And yet, many of us make mistakes that cost us a lot.

There are many who even prefer an [alternative method](https://jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27?ref=hackernoon.com). ([Here’s another one](https://dev.to/redfred7/enough-with-the-user-stories-already-2a8a?ref=hackernoon.com).) And it's often because they're frustrated by poorly written user stories. 

As much as it's important to know how to write good user stories, it's equally important to know how to NOT write one. 

Today, many software teams want to adopt agile processes. They want to put the user in the center of their product development process while building products. And it makes perfect sense. After all, you are building the product for your users, right?

A lot of times when writing user stories we think we are writing from the user’s perspective, but we end up skewing it with our biases and knowledge. And a lot of times, these mistakes are interlinked and only get worse with time.

In this article I will talk about some of the common mistakes teams make when writing user stories.

## User stories that are too broad

When user stories are too broad, crucial information regarding the expected action and the need can get missed. If there are a lot of “_ands_” or “_ors_” or "_thats_" in your team’s user stories, it is good indication that it is too broad and you should consider re-writing it. 

Also, there’s a very good chance that your too broadly written user story is actually an [epic](https://www.agilealliance.org/glossary/epic?ref=hackernoon.com).

An example of a broad user story might look like this:

“_As a user, I would like to continue reading the article later when I’m on my way home, without needing to sign up and find the exact spot where I left off._”

In this case you can see the user story is trying to achieve two things — not needing to sign up and not having to find where they stopped reading. Instead of trying to cram everything into a single user story, consider breaking it down into multiple user stories.

Here's how it may look after it is broken down:

"_As a user, I would like to continue reading the article later without having to sign up_"

"_As a user, I want to continue reading from where I left off, so that I don't have to find the last paragraph I finished reading_"

## User stories that are too fine

When user stories are broken down into too much detail, you begin talking about how you are going to implement it. This removes the focus from the user and leads to poor communication of expectations within the team.

Here's an example of a user story that is defined too fine that it talks about implementation details.

“_Define a scalable, relational database structure so that I can use it to implement any possible future use case._”

What business value does a great relational database have if the end user cannot use it? Besides, this user story is written from the business' perspective and not from the user's perspective. When you begin to include the implementation details, user stories no longer are written from the user's perspective.

## User stories that aren't negotiable

User stories are not meant to be specific, precise descriptions of a feature. And therefore, they must not be fixed in stone.

Here's an example of a non-negotiable user story: "_As a user, I want to have a clear all button in the notifications tab, so I can remove old notifications_"

You can clearly see, the user wants to be able to remove old notifications. While having a "clear all" button is one solution, you can still automatically clear the notification after it's read too!

Here’s a classic scenario to help you identify if your user stories are too rigid: 

Sometimes a user story may have been written in a particular way, and your team finds it hard to implement because there’s an easier alternative. 

In cases like these, the team should be willing to compromise on the approach provided it doesn’t hurt the value a user derives.

## User stories that are reiterated in acceptance criteria

Far too many times I notice the acceptance criteria repeating the user story, just in different words. 

Here's how it looks:

**User story:** "_As a user, I want to add pop-up forms to my blog, so I can capture the visitor's email id before they leave the site_"

**Acceptance criteria:** "_Given a reader visits a blog, when they try to leave, then the pop-up form should come asking them to subscribe to the blog_"

Acceptance criteria should communicate the conditions that need to be met for the story to be marked as completed. This ensures that you gather feedback, help the team plan, and track their work. It makes the user story richer, more precise, and more easily testable. And more importantly, it aligns your team on what they're expected to deliver.

Here's a better example:

**For the user story:** "_As a user, I want to receive notifications when others add comments so that I am up-to-date._"

**Acceptance criteria:** "_Given I have the app open when I am writing on the doc then the bell icon should update to show unread notifications with count_"

## User stories that have an undefined user

It can feel silly to mention the user persona in every user story over and over and over. However, it can add a tremendous amount of value in terms of the outcome. 

This is particularly important if your product has more than one user persona. There will, of course, be features that’ll get built specific to different personas. If you want your team to be more aligned on the outcome you are expecting out of them, they need to know who the end users are and what benefit they’ll get out of the feature.

If you're looking for an example for this, nearly all examples I provided above are great ones of how not to do. Don't worry, it was intentional so I can talk about this. :)

Every time you write a user story that begins with "_As a user..._" or "_As a visitor..._" or "_As a reader..._", you're leaving room for ambiguity. Clearly defining who that person is will go a long way in giving your team the context they require.

At [Zepel](https://zepel.io/), we recommend writing the persona instead of user/visitor/reader. This means, your user story will look like this:

"_As a writer, I want to receive notification when others add comments within the Google Docs app, so I don't have to refresh the page every now-and-then_"

## User stories with poor context

Far too many times, we end up writing user stories just for the sake of it. After a certain point, nearly every user story starts to look the same.

Here's an example: "_As a content manager, I want a text editor so that I can edit text._"

All this tells your team is that you want them to build a text editor and nothing else. If you’ve been writing down a bunch of user stories for a while, it’s best to take a break and revisit it with a fresh perspective.

Sometimes, even after a break, you might not be able to come up with something more meaningful. This can be a good indicator that you need to talk to your users more and understand their needs better. There’s really no point trying to squeeze it out of your brain.

## Conclusion

Although using a user story template can be useful, it is never as simple as completing a fill-in-the-blanks form in your agile tool.

Because one mistake while writing user stories often leads to a series of other mistakes as a by-product. And even if you do manage to write user stories properly, it’s only the beginning. You should still enable your to team to analyze the stories — from a technical point of view — to help them estimate and create the necessary next steps.

