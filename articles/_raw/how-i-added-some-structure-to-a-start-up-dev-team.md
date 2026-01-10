---
title: How I Added Some Structure to a Start-up's Development Team - And What I Learned
  from the Process
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-24T22:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-added-some-structure-to-a-start-up-dev-team
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/you-x-ventures-Oalh2MojUuk-unsplash-1.jpg
tags:
- name: agile
  slug: agile
- name: 'development process '
  slug: development-process
- name: leadership
  slug: leadership
seo_title: null
seo_desc: 'By Hughie Coles

  Until recently, I''d spent the last 4 years of my career at FinTech start-ups. I''d
  always worked for smaller companies, and being at a start-up was the next logical
  step in looking for roles where I could make the biggest difference.  ...'
---

By Hughie Coles

Until recently, I'd spent the last 4 years of my career at FinTech start-ups. I'd always worked for smaller companies, and being at a start-up was the next logical step in looking for roles where I could make the biggest difference.  

But a common problem with early-stage start-ups is that it's kind of a free-for-all in terms of how they're managed. 

These companies tend to be run by people who don't have a ton of experience running companies. And management tends to consist of founders and those who got in early, not necessarily those who excel in leadership roles. (No shade – good person + talented doesn't necessarily mean they're a good boss or leader).

During my time at one such start-up, I was promoted from senior developer to lead developer. 

The catalyst for this change was that the development team lacked leadership. The CTO had too many responsibilities, and the job of keeping the dev team engaged and productive was falling through the cracks. 

On top of this, we didn't have a project manger, and our product managers were too inexperienced to introduce any kind of structure.

This is the story of the wins and losses, and how to add process to a company that has none.

## Events leading to the change

First, a little bit of background. My previous job had been as a developer at a digital agency. This agency was a hard-core scrum shop that had trained all of their employees fairly thoroughly in scrum, and agile in general. 

So I came from an environment with a lot of process. That's partially why I left to pursue a start-up. 

About a year in, I started to notice some issues. Firstly, the developer turn-over was growing. Developers weren't feeling engaged. They were handed half-baked projects with no context on how it would aid the growth of the company, no input in the design or planning, and with nowhere near enough detail.

Then came a project that crystallized our problem. The product that I worked on had the concept of bills (payables) and invoices (receivables). We were working on a new feature that would allow users to upload an image of an invoice and have it input manually by a service. 

The problem was that the product manager kept saying "bills" instead of "invoices". There was no user story, no ticket, this was all in the mind of the product manager. Requirements were communicated verbally or in slack messages. The developer working on the project had only ever been told "bills". 

It wasn't until the CTO overheard a conversation a few days before release that we realized that we'd targeted the wrong aspect of the system. 

Luckily, bills and invoices were, for the most part, symmetrical in our system, so it wasn't much work to make the change. It just became very clear that we had a problem.

Given my background and the fact that I was one of the most senior and tenured developers at the company, it made sense for me to take the lead. 

Since I was leading the initiative, I chose to implement a scrum-type process.  In the remainder of this article, I'll outline **what** we did, **how** we did it, and **why** it was done, as well as my **learnings**.

## Getting Buy-in

I'm gonna preface this by saying that I don't like handing commandments down from on high. I feel like a leader-team relationship is a collaborative one. I may occasionally play leader because it's my nature, but it's important that ideas are discussed and that people feel their opinions are heard and valued.

The first step was to gather the developers to have a discussion.  In this initial discussion, I outlined what I felt our issues were.  This included lack of clarity on requirements, sliding deadlines, and our complete lack of a testing strategy.  The discussion validated my thoughts, because the team felt the same way.  

The rest of the meeting consisted of me outlining scrum, what elements I felt could benefit us, and what that would look like. I also discussed some things that I learned about test plans and systematic QA that I learned in my agency days.  We then went around the table, giving thoughts, asking questions, and tweaking.

I conceded that manual testing wasn't fun or ideal for the dev team, but until we could justify a full-time QA engineer, we had to do the best with what we had.

Learnings: 

* If you have a good idea, all you need is a chance to prove its worth. 
* Enlist your team to help build this together, make everyone part of the solution and they'll own it with you.

## Our Version of Scrum

After describing what a "full" scrum process would look like, I laid out to the team what the purpose of each aspect and ritual was.  I wanted to highlight where we could get the most gains. No one wanted 10 hours of meetings per sprint.  

Speaking of sprints, we decided to start with a 2 week time-box with an eye on moving it to 3 weeks if we wanted less overhead and could afford less frequent releases.

The process I put in place was as follows.

We'd have a sprint started with a 2-hour grooming/planning meeting on a Monday morning. In this planning meeting we (the dev team and the product manager) did a pass over the backlog.  This pass consisted of clarifying the story to clear up misunderstandings; estimating using story points; and prioritizing based on company road-map.  The team then picked out the amount of work we felt we could do, based on priority, and brought it into the current sprint. 

This work was a collection of user stories. The product manager would leave, and the dev team would break these stories down into tasks, get a general sense of who would work on what, and then we got to work.  This gave the product manager transparency on what we could deliver, which was sorely lacking.  It also gave the team their full workload for 2 weeks, which allowed us to plan and pace accordingly.

The next week and a half were dev days. This included peer code reviews on feature branches before they were merged. Dev hands-off was the Wednesday of the 2nd week at noon. We would then prepare the QA build, QA spreadsheet (more on this in a bit), and start manual testing.  

The idea was to finish the initial QA pass by the end of the Wednesday, and spend Thursday and Friday in a bug fix/test loop until we were satisfied with the build.  

At this point, the build would be handed off to the CTO for a final code review, and it would be deployed the following Tuesday. Issues found in the code review would be fixed and tested on the Monday if needed.

Friday afternoon we would have a blameless retrospective/postmortem. Here we laid things bare. It's important to acknowledge what went poorly, and to address the cause(s) so that we could avoid it in the future. 

All of the developers (including myself) learned a lot through this process. I feel like we're all better off after having gone through it. I actually overheard the CEO suggest doing blameless postmortems a few weeks after we started doing them on the dev team. It was nice to see that our ideas were catching on. 

This was one of the big wins. We learned why a feature was needed, what the intention behind it was, and all of the details and expectations.

Learnings:

* Split and join meetings based on your team's needs.  Don't do things "just because"
* Share your progress outside your department.  Sometimes your ideas can provide benefits outside of your team.

## A Testing Framework That You Can Believe In

This company had never had a formal testing process. This meant no test plan, no peer testing, just a developer verifying that it worked, and it going to production.  

In my experience, developers are as good at testing as they are at estimating, so we needed to change that. We had a good suite of automated tests (unit and integration), but no end-to-end tests. I also prefer to have some exploratory testing as well. In the past, I've seen it uncover weird behaviors that automated testing can miss.  

We set up a google doc with all of the tickets (including links to the user stories) in the first column, and all of the developer names (and the PM) in the first row. The idea was that every ticket had to have 2 X's, both from people who didn't work on the feature. This divide and conquer strategy allowed us to test very thoroughly in a fairly short amount of time. 

Learnings: 

* Lean hard on automated testing.  It's reliable and finds many classes of bugs with no manual time.
* Test with a plan.  You're going to waste a lot of time just wandering.  A systematic approach can make manual testing more efficient.

## Success

What was the result? I don't have exact numbers, but the defect rate plummeted. There were no longer rushed hot fixes to production. The work promised was delivered. Features were being released on time. 

We were moving faster than ever, and the developers were happier. We were working as a team instead of in silos, we all knew each others' features intimately because we all went through the user stories and estimated together. There was no more of this "oh, I can't touch feature X, I didn't work on it" siloing stuff. 

One dev who was planning on leaving stopped looking. It was great.

Learnings:

* Keep adjusting your process based on results.  It's an ongoing process.
* Sometimes people don't want to leave a company, they want to leave a situation.

## An Abrupt End

But nothing gold can stay :) Ok, that's a bit dramatic. While the dev team was gelling, increasing our velocity, and building more camaraderie, management was going in a different direction. 

The CEO had done a ton of reading and decided that OKRs were what was gonna get the company to the next level. Unfortunately, it was decided that OKRs would go down to the individual level, meaning that the team would no longer be pooling work, breaking it down and tackling it together. Instead, each developer would work out (or in practice, given) a set of KRs, and they alone would be responsible for delivering on them.  

We were back to silos. The development team pushed back, we tried to compromise, to stop OKRs at the team level, but it was no use. The dream was dead. Yes, again with the drama, but it was a little sad. 

This change coincided with a slight change in power structure, my title as lead developer became little more than a platitude, "leadership" said some very unkind things to the development team (somewhere along the lines of "get on board or get out"), which led to half the dev team, including myself, leaving within a month.

Learnings:

* Good ideas don't always win out.  Even in a situation like this, you can learn a lot.
* Recognize when you can no longer make a difference. 

## Mistakes Were Made

Given the way that last paragraph ended, you may thing that I was about to enumerate the mistakes that the company made. But I'm not going to do that. 

It's been about a year since I left, and in that time I've learned a thing or two. There were some serious gaps in the process that we'd created. These were things that I just didn't really understand or know about at the time. It was due to my shortcomings, but we all get better every day. 

In hindsight, here are some major things I'd missed:

### We weren't measuring.  

How do you know you've done it right if you didn't take measurements before and after? We had no telemetry, very little alerting, and frankly, if a feature had negative impact, we didn't know about it.

### Too much manual testing, not embracing automation.  

What we were really missing was a nice suite of automated E2E tests. We started working on these near the end, but we didn't prioritize them enough. Many of the errors we found during manual testing could have been caught during some acceptance tests using cucumber, or some E2E selenium tests.

### Big bang releases.  

I know a common part of scrum for many companies is the idea that all of the sprint work is demoed and released together. 

The problem with this is two-fold. Firstly, at a start-up you need to move quicker. You need to beat others to the punch and get value out to customers and feedback from customers as quickly as possible. And the tighter that feedback look is, the better.  

Therefore, multiple releases per sprint would have been better. It's more difficult to coordinate testing and QA, but it's still better to release quickly and often. 

Secondly, the larger the release, the more risk is involved. Releasing smaller chunks means that fewer changes are released at one time. If there's any issue, it's easier to identify and fix, and a rollback won't affect other, correctly functioning features.  

So I've learned that releasing in verticals that are as small as possible is the safest, least coupled way of releasing software.

## Conclusion

For all of the missteps and the unfortunate ending, I feel like the experience was a success. I learned what it meant to guide a team of developers through a process, to take feedback and apply it, and to try and discard ideas that, even though they are "supposed to be there", just didn't fit our team.  

It's important to cater your process to your team and organization. You have to add enough process to guide, but not so much to hinder. It taught me how to implement process, to push ideas forward, to help others be heard, and how to lead from within a team.  

Although it ended poorly, it was a big step forward in my career, and really solidified my ability and desire to lead.

You can find more of my articles on my [medium blog](https://medium.com/@hughie.coles).








