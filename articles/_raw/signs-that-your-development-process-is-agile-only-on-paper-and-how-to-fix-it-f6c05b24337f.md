---
title: Signs that your development process is Agile only on paper — and how to fix
  it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T21:24:37.000Z'
originalURL: https://freecodecamp.org/news/signs-that-your-development-process-is-agile-only-on-paper-and-how-to-fix-it-f6c05b24337f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6IeFjtwx0cPgTRjcS_vS6w.jpeg
tags:
- name: agile
  slug: agile
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Geshan Manandhar

  Agility comes with practice, not putting big words on paper. Using Jira does not
  make your software development process agile. Saying we do “scrum” is not being
  agile.

  Being agile is having an agile mindset and putting it into pra...'
---

By Geshan Manandhar

Agility comes with practice, not putting big words on paper. Using Jira does not make your software development process agile. Saying we do “scrum” is not being agile.

Being agile is having an agile mindset and putting it into practice every day. It is about thinking about the value you deliver to the customer and how to do it better.

This post will unveil five signs your practice isn’t really agile, and how to solve these issues. The signs and solutions will concern multiple roles like Product Manager, Software engineer, and so on.

![Image](https://cdn-media-1.freecodecamp.org/images/QsoP-waDxNwWENV8yaNFopJLAAHUEZvEdBg5)
_Agile board image from [Unsplash](https://unsplash.com/photos/zoCDWPuiRuA" rel="noopener" target="_blank" title=")_

### TLDR;

* If you are writing documents > 5 pages you can improve.
* There should be a clear definition of Ready for development and Done.
* Story/Issue should be based on value delivered to the customer, not only the technical aspect.
* Releasing a new version of software once a month and saying we are agile should be a crime.
* Not caring about the team is not doing agile right.

Now let’s go through these signs that explain why paper boat agile practices will not work and how to fix them.

### Documents that are longer than 5 pages

There will be big features (epics) and they have to be explained. This does not give you a license to write 50 page documents. If a document is longer than 5 pages many team members will not read it. Accept this fact.

> _One beautiful Monday morning you get a memo of 30 pages text about the new feature the business wants us to develop. Will you read it thoroughly? The answer is No._

You might skim through it to make it through the meeting and that’s about it. Documents become obsolete fast. When requirements change, no one bothers to update documentation.

#### Solution

Write documents that are less than or equal to 5 pages. Make it concise and precise. Start creating visual aids for the process to explain it. Create mock-ups, and use tools like [Balsamiq](https://balsamiq.com/). Express the requirements in a way that is understood by everyone with less or no reading involved. Then as need dictates, create a UI design and discuss. After that implement it in code.

### Unclear definition of Ready for development and Done

A clear definition of ready for development and done are crucial for team success. Not having these or having unclear ones will hamper the team’s performance.

> _A software engineer should be clear about when the story is ready to be picked up for development. Same goes for done._

Is it ready for development when the story is created but the description does not exist? Is it done as soon as I deploy it to production and move my task to the “done” column? If there is confusion like this, it is an issue that needs to be addressed.

#### Solution

Have a clear point by point “Definition of Ready” and “Definition of Done”. This will help you measure and improve the team’s performance. It will also help everyone involved to understand the meaning of these things the same way.

### Stories based on the technical aspects, not the value to the customer

Agile software development is always about delivering value to the customer. Value in the form of working software, not a pile of documents.

Say that there is a story like “As a customer service manager I need to know who created a refund so that I can track and audit refunds in future”. This task might entail adding a “created_by” field in the refunds table for instance. But this should not result in having a “story” that says “Add created_by field in the refunds table”. Of course, it can be a task/sub-task as part of the main story. The main story delivers value, but this database task is something that aids the process.

![Image](https://cdn-media-1.freecodecamp.org/images/bEDuLU1nTvT3YZAeZaxaIVHshWGUXbVjNg5X)
_A story has value and points, tasks are part of a story._

#### Solution

Have clear definitions and boundaries of Epic, Story, and task. Each story should deliver some value to the customer (as in the above picture). If you are following Scrum you will have story points too for things like team velocity. Technical tasks are required. Still, only the right sum of technical tasks delivers value to the customer.

> _The main thing here is “always focus on the value being delivered to the customer”._

### Releasing a new version of software once a month

The first thing to consider here is:

> _Deployment is a technical task and releasing a new software version is a business activity._

[Deployment is not a release](https://geshan.com.np/blog/2018/10/deployment-is-not-release/). If you are not able to make that distinction there is something that needs to be fixed. On top of it, if you hardly release one new version each month, you are doing agile wrong. [Release early release often](https://en.wikipedia.org/wiki/Release_early,_release_often) is an excellent philosophy for getting feedback early. With early feedback, you can make a new set of changes in the next release to make the software better.

This might not apply for the mobile applications as they can have a long vendor approval process. For web applications, deploying and releasing multiple times a day should be a norm.

#### Solution

Build a culture and technical process that allows you to deploy and/or release to production multiple times a day.

> _Enforce good code quality and excellent software engineering practices. Follow tried and tested best practices like code reviews, automated testing, CI/CD, [logging](https://geshan.com.np/blog/2015/08/importance-of-logging-in-your-applications/), monitoring, and [automated deployment](https://geshan.com.np/blog/2015/08/the-best-automated-deployment-tool-the-one-that-fits-your-needs/)._

Call it DevOps, SRE or Platforms engineering — whatever you want. But do it and deploy without fear whenever you want.

### Not being careful about team motivation

Software development is a team sport. If one player is hurt the team covers for that player. If one team member lacks some skills, the team covers and helps teach that skill to the team member. A self-organizing team that reflects on how to make the process better is at the heart of agile.

> _Team motivation and happy team members are essential to high productivity._

If you are being treated like story executors with no voice and no room for improvement, it is a big bad sign.

#### Solution

Build a culture of continuous improvement. Reflect on things that have been done and how the process can be enhanced. For instance, if doing 60% new features and 40% bugs did not work well, find a better ratio. Do team activities and things that uplift the team spirit.

### Conclusion

Being agile on paper and being agile in practice are two different things. Don’t let your agile software process be like waterfall model with the so-called agile skin. Be agile and fix these signs to have high team output with fantastic performance.

> _Agile should be implemented to solve people and communication problems which results in stabilizing the technical issues._

_You can read more of my blog posts at [geshan.com.np](https://geshan.com.np/blog/2018/11/5-signs-that-reveal-your-software-development-process-is-agile-only-on-paper-and-solutions-for-them/)._

