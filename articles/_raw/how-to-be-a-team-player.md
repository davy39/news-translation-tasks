---
title: How to Be a Team Player as a Software Engineer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-29T23:50:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-be-a-team-player
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99fd740569d1a4ca22e3.jpg
tags:
- name: 'self-improvement '
  slug: self-improvement
- name: Software Engineering
  slug: software-engineering
- name: teamwork
  slug: teamwork
seo_title: null
seo_desc: "By Moshe Siegel\nIn my first software engineering role at an eCommerce\
  \ brand, I often secretly worked on tasks outside of my core responsibilities. And\
  \ many times I felt isolated from my teammates. \nTherefore, when I was invited\
  \ to participate in a pr..."
---

By Moshe Siegel

In my first software engineering role at an eCommerce brand, I often secretly worked on tasks outside of my core responsibilities. And many times I felt isolated from my teammates. 

Therefore, when I was invited to participate in a project-based course to better my communication skills, I jumped at the opportunity. 

For the program, I was assigned to a team with two other engineers and a team lead to build a full stack application using React, Python, and Flask. Now that the course is over, I thought I'd share the lessons I learned about how to be a better team player. 

## Lesson 1: Do not underestimate a project’s potential difficulty level

Since the course was meant for entry-level engineers, I figured I would have a leg up as I already had some professional Node.js experience. Granted, our tech stack would be using a Python Flask backend, but I figured Python and Flask would not be too hard to pick up. 

On the first day of our project, we were shown what we would be building. Wow, I suddenly felt very unprepared. Our project was significantly more challenging than I had expected.

My other two teammates seemed to pick up the material easily. At the end of our first week I was our team’s least contributing member. 

I knew React quite well, so our front end was not too difficult for me. But our backend was using PostgresSQL and Python, neither of which I knew well. It quickly became clear that the tasks expected of us would be particularly challenging for someone with little Python experience.

## Lesson 2: Request feedback on work in progress

Initially, I often found myself wasting time doing unnecessary work. For instance, one time I was creating an editable user profile form, not realizing that my teammate was in the middle of building a reusable Material UI dialog component that I could have used. 

Another time I spent time reading a tutorial on how to get the identity of an authenticated user, not realizing that my teammate had already figured it out. 

Realizing how much time I was spending doing unnecessary work, I started posting in our Slack message board what I was working on and requesting feedback. My teammates were quick to respond. By having my colleagues give input on my unfinished designs, I was able to avoid duplicating work.

## Lesson 3: When pressed for time, prioritize what to avoid learning

Given that I struggled to keep up with the workload, I needed to better prioritize my time. Whenever someone created a new feature, they would create a Git Pull Request (PR) to ask for the code to be reviewed. At first, I reviewed every PR and gave each of them my full attention. However, this soon proved impractical. 

I remember spending lots of time reviewing the PR to add cookies and tokens for authentication. To do a proper review, I first read lots of background info on security issues such as cookies, local storage, and cross site scripting attacks. When I finished all that reading I read through the PR, only to find all the code made sense and there was nothing for me to comment on. 

In hindsight, given how far behind I was with my own tasks, I should have ignored much of the cookie documentation and instead done just a rapid PR review to save time. 

Gaining an in-depth knowledge of the inner workings of our cookie authentication was of little use to my overall productivity. In contrast, other PRs such as the one which set up React Context to pass state through our app directly affected nearly every feature that I worked on. 

Prioritizing gaining a deep understanding of that PR would have been a far more valuable use of my time.

## Lesson 4: Build new features by going from chunk to chunk

To get more organized, I had to learn how to skim through technical documentation. I called a senior engineering friend of mine, Sean Ellison-Chen, and asked his process for tackling a new feature that requires a technology that is brand new to him. 

He explained that he first tries to understand at most 70% of what is going on, and then immediately starts building the feature in chunks. Each chunk gets committed to git. 

For example, let’s say he needs to set up web sockets, he might set up a basic skeleton structure for web sockets, commit it to git, then work on the next chunk of setting up the correct socket events and so on. 

By working in chunks, he ensures a smooth progression from tackling the bare minimums to eventually having a fully functioning feature.

## Lesson 5: Request feedback from your team lead

Midway through the program, I received feedback from our team lead, Shums Kassam. I was told to ask for help more, to skim through documentation, and to leverage my teammates. 

I took the advice to heart and upped the amount of times I posted in our message board. I started having video calls with teammates to review features I was building. I skimmed faster through the technical documentation and avoided the less critical areas. By implementing these changes, my rate of contributions sped up.

## Lesson 6: Avoid doing a perfect job on tasks whose requirements might change

By sheer luck, I learned the importance of procrastinating on tasks whose requirements might change. 

One of my first tasks was building a front-end form that lets users change their profile info. When I submitted my code for review, I was told the form’s appearance needed to be fixed as some of the input lengths did not match. 

Normally, I would have spent the 45 minutes to fix it right then and there. But I was far behind in my contributions, so instead I just commented a “todo” about matching the input lengths and merged my code. 

A week later, a teammate pointed out it would be a better user experience to combine the separate ‘street’, ‘city’, ‘state’, and ‘country’ inputs into a single ‘address’ input. When he simplified the inputs, my commented out “todo” was no longer applicable. 

By procrastinating with working on the form, I had saved myself from doing unnecessary work.

## Lesson 7: Be comfortable submitting non-refactored code

Near the end of our project, our team was rushing to finish all our features prior to a fixed date when we would present our project to an audience. We planned to have all features submitted well in advance to give us enough time to practice and rehearse. 

But I ended up submitting my final feature with barely an hour to our demo and we had to rush to add it in. Though our presentation went well, I was troubled that I submitted the feature so late as it severely reduced our team’s ability to rehearse our demo in advance. 

In hindsight I realize that instead of submitting optimized and clean code, I could have saved at least two hours of time by simply adding comments about refactoring later.

Over the past few months, I learned many lessons about how to be a better team player. Most importantly, I learned that teamwork is a skill that can be improved just like any other.

The program I participated in was run by [Hatchways](https://hatchways.io/), a company that helps software engineers get their first jobs. At the time of this writing they service engineers and companies in North America. If you're an employer looking to hire interns or entry-level engineers see [Hatchways - Employers](https://hatchways.io/employers). 

