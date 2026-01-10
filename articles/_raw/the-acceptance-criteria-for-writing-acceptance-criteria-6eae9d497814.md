---
title: The Acceptance Criteria for Writing Acceptance Criteria
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-06T18:25:31.000Z'
originalURL: https://freecodecamp.org/news/the-acceptance-criteria-for-writing-acceptance-criteria-6eae9d497814
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eRFNul714YcZ-LcdQARm2Q.jpeg
tags:
- name: agile
  slug: agile
- name: kanban
  slug: kanban
- name: project management
  slug: project-management
- name: Scrum
  slug: scrum
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Elijah Valenciano

  Many development teams are too familiar with the frustrations of unsatisfactory
  acceptance criteria or even the lack of criteria itself. Defining no requirements
  is like preparing for battle without a plan of action — the team ha...'
---

By Elijah Valenciano

Many development teams are too familiar with the frustrations of unsatisfactory acceptance criteria or even the lack of criteria itself. Defining no requirements is like preparing for battle without a plan of action — the team has taken more steps toward failure than success. I offer specific suggestions in crafting acceptance criteria that can improve any agile process.

First, let’s quickly define acceptance criteria.

> Acceptance criteria are the “conditions that a software product must satisfy to be accepted by a user, customer or other stakeholders.” (Microsoft Press)

Easy enough, right? Not quite. At this point, I would ask myself if this is where my definition of acceptance criteria stops. In addition to the definition above, any product owner should have answers ready for the following questions:

> What do these conditions look like? Who creates these conditions? How many conditions should there be? How are outcomes measured?

Generally, acceptance criteria are initiated by the product owner or stakeholder. They are written prior to any development of the feature. Their role is to provide guidelines for a business or user-centered perspective.

**However, writing the criteria is not solely the responsibility of the product owner. Acceptance criteria should be developed as a joint effort between the development team and the product owner.**

Crafting these criteria together helps the development team understand the desire featured. It also helps the product owner catch missing details. Additionally, the owner gains a better understanding of feasibility, complexity, and scope.

![Image](https://cdn-media-1.freecodecamp.org/images/Hzk0Rmb3UArySx-mxJXWBxlajmYZiNQ9rTyr)
_Image by [Maryna Z. &amp; Dmiriy G](https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important" rel="noopener" target="_blank" title=")._

### Formatting acceptance criteria

Criteria can be written in a variety of formats. Most teams lean towards two specific types: **rule-oriented** or **scenario-oriented**.

Rule-oriented requirements are straight-forward. They list out observable outcomes. “Display statement balance upon successful authentication.”

On the other hand, scenario-oriented criteria tend to follow the “Given…When…Then…” template. This was derived from behavior-driven-development (BDD). This requirement outlines the expected observable result. This occurs _when_ a particular action is executed _given_ some context.

### **3 characteristics of effective acceptance criteria**

#### **1. Testable with clearly defined pass/fail results**

Have testable criteria. This allows testers to properly confirm that all of the desired conditions have been fulfilled. If criteria were not testable, then there would be no way for verification. These criteria should either be met or not met. A developer should know the point in which the criterion has been achieved. Any ambiguity may prolong effort on the story.

For example, an acceptance criterion states “increase the number of entries available in a drop-down menu”. The developer would have no idea how many new entries to add and may take the liberty to assume a number based on his experience with the product. Likewise, a manual tester may take the same liberty and assume a different definition of increase. This results in a confusion that will circle back to the product owner.

#### 2. Unambiguous and concise

This is where writing acceptance criteria become an art. Academic essays stress the importance of clarity and succinctness. Similarly, writing acceptance criteria mandates the same level of organization and care.

Similar to writing a literary piece, the audience must be kept in mind. Those reading the acceptance criteria must understand what is written. Otherwise, those words are completely useless. If they are long-winded and filled with jargon, then the main points of the outlined conditions may not come across. Many people can overlook essential details in a sea of words when pressed for time. Even when not pressed for time, many people can easily gloss over long blurbs.

Instead of putting the blame on others’ lack of careful reading, one can proactively present acceptance criteria that are easy to read, straight to the point, and devoid of superfluous details.

#### 3. Establish shared understanding

This is probably the most important characteristic and the one most taken for granted. If all the members of the team are not on the same page, then process and productivity become jeopardized. Having the development team review acceptance criteria before moving forward with the story minimizes confusion. Clarifications should be made about the criteria, and the criteria should be updated accordingly.

I’ve had experiences where all team members have been part of writing acceptance criteria. It allowed everyone to understand all parts of the story. It also provided opportunities for team members to chime in with questions and ideas. However, such a process might not always be ideal, especially for larger teams.

Nevertheless, it is important that each member can read the acceptance criteria. From there each member should gain an understanding of how to bring the story into completion. Regardless of whether it be in development or testing.

![Image](https://cdn-media-1.freecodecamp.org/images/-ZwiZDhnjvum-WpwyTy2etTL1X1OY2zbOWPm)

### **When too much is an issue**

We’ve already explored the danger of unclear acceptance criteria. This results in the risk of introducing extraneous features into a story. However, the surprising opposite case can also exist: acceptance criteria may become too detailed.

> **“Acceptance Criteria should state intent, not a solution” (**Segue Technologies**)**

Provide a blueprint of “what” (intention) instead of “how” (implementation). Otherwise, the development team may be robbed of the opportunity to explore different ways to solve the problem. On those lines, better implementations may be thought up after the initial thoughts on a solution.

**Once you’ve written your acceptance criteria, you may ask yourself, “How many is too many?”**  
I’ve seen stories that range from zero acceptance criteria to more than fifteen (or at least it felt like that).

As a rule of thumb, I personally like to see three to eight acceptance criteria per story. However, towards the upper end of that limit, around five or more acceptance criteria, I would check manageability. I would carefully check to see that the story couldn’t be broken up into smaller, more manageable stories.

Others would disagree and argue that eight would already be too many. However, I like to lean towards providing as much “what” detail as I can without sacrificing conciseness.

### **Now what?**

**Ok, I lied.** I did not provide an exhaustive list of acceptance criteria for writing acceptance criteria. The desired characteristics such as conciseness, clarity, and comprehension are subjective. I intended them to be.

**I believe that there is no “correct” format to writing acceptance criteria. Their correctness is measured by the effectiveness in one’s team.**

I highly recommend on initially using a template. They have provided many teams with a solid and safe structure that promotes good acceptance criteria writing. However, do not let that structure stop you from advancing into ideas that may promote efficiency and efficacy.

If you are a product owner or client writing acceptance criteria, I challenge you to ask your development team for feedback on the current acceptance criteria. With a bit of care, practice, and organization, crafting effective acceptance criteria becomes a powerful tool in improving the workflow of any team.

### More to read

* [https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important](https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important) — by Maryna Z. and Dmiriy G.
* [https://www.leadingagile.com/2014/09/acceptance-criteria/](https://www.leadingagile.com/2014/09/acceptance-criteria/) by Steve Povilaitis
* [https://www.seguetech.com/what-characteristics-make-good-agile-acceptance-criteria/](https://www.seguetech.com/what-characteristics-make-good-agile-acceptance-criteria/) by Segue Technologies
* [http://agileforgrowth.com/blog/acceptance-criteria-checklist/](http://agileforgrowth.com/blog/acceptance-criteria-checklist/) — by Kamlesh Ravlani

