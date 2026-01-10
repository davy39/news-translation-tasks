---
title: What is Agile and How You Can Become an Epic Storyteller
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-05-12T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-agile-and-how-youcan-become-an-epic-storyteller
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/intro-to-agile-1.jpg
tags:
- name: Software Requirements
  slug: software-requirements
- name: agile
  slug: agile
- name: agile development
  slug: agile-development
- name: 'development process '
  slug: development-process
- name: project management
  slug: project-management
- name: Scrum
  slug: scrum
- name: software
  slug: software
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: Running a team of developers is hard. Trying to coordinate a mountain of
  work while keeping everyone productive is a challenge itself. But on top of that,
  you have to keep open communications with a client. How can we use agile to relieve
  some of tho...
---

Running a team of developers is hard. Trying to coordinate a mountain of work while keeping everyone productive is a challenge itself. But on top of that, you have to keep open communications with a client. How can we use agile to relieve some of those pain points?

* [What is agile?](#heading-what-is-agile)
* [What are some concepts you should know?](#heading-what-are-some-concepts-you-should-know)
* [Stories](#heading-stories)
* [Epics](#heading-epics)
* [Sprints](#heading-sprints)

%[https://www.youtube.com/watch?v=1GPYnoG_nkE]

## What is agile?

Agile is a software development methodology that stems from the idea of breaking up large amounts of work into smaller pieces. This gives product managers, developers, and any stakeholder a better understanding of the work.

Historically, software development was a slow process where major changes to requirements could put large strains on teams. 

When following the agile methodology, the smaller chunks of work help teams become more flexible, and dare I say _agile_. And in the process it helps them deliver features faster and respond to changes quicker.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-project-board.jpg)
_Example Jira project board from [atlassian.com/software/jira](https://www.atlassian.com/software/jira)_

These ideas have been broken up into different frameworks of approaching this methodology. Two of the common ones are [Scrum](https://www.scrum.org/resources/what-is-scrum) and [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)). 

For this walkthrough, most of these concepts follow along the Scrum framework, but there are certainly concepts that apply to both and others.

## What are some concepts you should know?

I'd argue half of being productive as a developer in an agile world is simply understanding the terms. Typically the project manager runs the show, so if you can be on the same page with what they're talking about, it will make the process a lot easier.

There are books, courses, and certifications based around learning the nuances of the agile methodology. I'm not going to go deep into some of the philosophical aspects or some of the deeper parts, but I'm going to cover a good set of key concepts that will help you hit the ground running when you start your new job with an agile team.

## Stories

A story is typically the smallest defined piece of work. This usually comes in the form of a new ticket that you create in the project tool you're using whether it's [Jira](https://www.atlassian.com/software/jira) or even [Github Issues](https://help.github.com/en/github/managing-your-work-on-github/about-issues).

### Expressing stories

When working on a project, you'll probably run into a variety of ways people express stories. But a good guideline is to work through the concept of the word "story" itself and explain the work that needs to be done in that way.

For instance, if you would like to provide the ability for the people who use your website to share a blog post on Twitter, you may want to write the story as: As a reader, I want to share the post I just read to Twitter.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-story-summary.jpg)
_Creating a new story in Jira_

Using that pattern of "as a [person], I want to [action]" helps provide context as what state somebody may be in when visiting their site and what they're trying to achieve. This can be particularly helpful if you're developing features for people who are logged in that are different from guests.

### Details and requirements

While the title of a story is an important representation of the work, you'll also want to provide additional specifics. 

At a minimum, that should be done by adding a thorough description and a set of acceptance criteria that can help give the developer context and requirements. Depending on the team, this can also include tools like tags or categorizations that make it easier for the team to visualize groups of work.

Providing a strong set of requirements helps both the developer working on the story and the person reviewing it have a measurement to determine if it's actually complete. Without it, everyone's just guessing.

A good way to phrase these are: verify [requirement]. Back to my example of sharing a post on Twitter, maybe some of the requirements to that story would be:

* Verify when clicking the share button a new tweet is created
* Verify the tweet includes a link to the current blog post

### Amount of work or level of difficulty

Each story is represented by a number of points. Those points are a way to express how much effort a team of developers expects one story to be. That effort can mean a variety of things though whether it's simply how difficult the team expects the work to be or the amount of risk or uncertainty a particular story has.

One way teams represent this is with the [fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number), where the amount of points can be 1, 2, 3, 5, 8, etc. Where a negligible text update might be 1 point, adding a new form to a page could be 3 points.

Typically you'll want to avoid pointing stories too high, as you get above 5 points, there's more than likely a way you can break up the work to make it more manageable. While you could easily create a massive 13 point story to accomplish all aspects of a feature, it usually makes sense to tackle the work in smaller, more focused chunks.

Either way, these points all add up together to give your team a rough estimate of how much work a group of stories would take to complete.

## Epics

While stories have a goal of defining a bite-sized piece of work, epics are a way to group those pieces of work together to represent a feature.

### Defining stories as a feature

A good way to explain this is with another example. If you're working on an application that requires the integration of authentication, you may want to create a new epic simply called "Authentication". 

Inside that epic, you could find stories like:

* As a guest, I want to sign into the application with my email address
* As an authenticated user, I want to change my password
* As the security team, I want to prevent spam and abuse of user authentication

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-epic-authentication.jpg)
_Example of an Authentication epic in Jira_

With your epic defined, you're giving your team a path to calling a feature complete while also understanding the entire scope of that work. This is important when it comes to planning out the work to be done.

Defining your stories in your epic gives you a sense of how much work something takes, but it doesn't help you figure out how long it would take, which is where sprints come in.

## Sprints

Sprints are a way of planning out how the work will actually get done. While similar to epics in that they are a way to group chunks of work, sprints typically represent a period of time in which a particular chunk of work will be done.

### Time per sprint

A common way of defining a sprint is two weeks of work. During those two weeks, your team will have a particular velocity, or average amount of work you can complete, for an individual sprint. This velocity is represented by a number of points that is a sum of the average velocity of each of the developers working on that sprint.

### Points per sprint

Though many fiercely argue you shouldn't use time to represent that velocity, points will roughly translates to an average amount of time of work for each developer. While 1 point for an experienced developer could be 1 hour, that same 1 point could mean 3 hours for a less experienced developer.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-project-roadmaps.jpg)
_Example project roadmap from [atlassian.com/software/jira](https://www.atlassian.com/software/jira)_

But once you have this number of points that your team averages in a sprint, you'll know how many story points you can expect to plan to be completed. This planning goes sprint to sprint as you spread out a group of stories or an epic so you can predict when a feature will be complete.

## How agile fits with your team

Try to remember that the Agile methodology through Scrum, Kanban, or any other framework is just that – a framework. While it's probably a good idea to follow the process when you first start out, listen to your team and try to mold it to your own experiences.

Each team works a little bit differently and forcing a process onto that team can cause more harm than good, but there will always be a learning curve for any process. Fight the eye rolls until everyone gets the hang of it and have frequent retrospectives to see what works and what doesn't.

At the end of the day, the processes your team follows should mostly be invisible, working for you instead of against you. Find what works best for your team and share your experiences for others to learn!

## What's your teams process?

[Share with me on Twitter!](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

