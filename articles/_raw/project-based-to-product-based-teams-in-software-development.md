---
title: Project-Based Teams VS Product-Based Teams – Which is better for Building Software?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T18:09:02.000Z'
originalURL: https://freecodecamp.org/news/project-based-to-product-based-teams-in-software-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99ed740569d1a4ca2275.jpg
tags:
- name: 'Junior developer '
  slug: junior-developer
- name: product development
  slug: product-development
- name: software development
  slug: software-development
seo_title: null
seo_desc: "By Enrico Piccinin\nSuppose you have to add a new major feature to an app.\
  \ \nIs it easier to add this major feature to a relatively small app, still under\
  \ construction and not yet in production? Or is it easier on a big app that has\
  \ grown over time, wh..."
---

By Enrico Piccinin

Suppose you have to add a **new major feature** to an app. 

Is it easier to add this major feature to a **relatively small app**, still under construction and not yet in production? Or is it easier on a **big app** that has grown over time, whose overall quality is questionable, and which is already running in production serving several clients?

Well, there is no doubt. The second is a much more challenging task. 

So then why do we usually find the most experienced developers, the architects – the "cool kids" – mostly involved in working on those smaller apps, while the rest of the folks are often buried in the large projects?

## My story

Many years ago, I joined the dev team responsible for one of the core systems of a big corporation. The first position I was given was in the Application Maintenance (AM) team responsible for the legacy parts of the app. 

The reasons were simple and were shared with me: I was new to the place, and new projects were running fast. They were using leading edge technologies for which there was not much experience. So AM was the right place for me to grow without too much pressure. 

They told me that as soon as I had gathered enough knowledge and experience I would move to the Project team. This was the team developing new features with new technologies, the team of the experienced devs. 

After one year or so this actually happened, but I will never forget that supposedly not-so-stressful period of AM.

## The Project team and the AM team

All this was many years ago but, since then, I have seen the same pattern repeated many times, often in much more extreme forms. 

When you have a new initiative, you start with the Project team. The Project team develops the architecture and the features. The Project team accumulates delays with respect to a very optimistic initial plan, and then they start working extra hours, cutting corners along the way. 

Quality is often sacrificed to the altar of the Plan, tests are forgotten, and patches are added on top of patches. Developers start adding comments “To be refactored as soon as we have some time”. Technical debt is already there and it'll only grow.

Eventually the thing is brought to production and then, immediately after it goes live, the Project team starts the transition towards the AM team. 

After some overlapping period, the AM team is left sailing alone. The AM team is usually younger, less experienced, and considered not as strong as the Project team. 

But the tough part is over, the project is now live. Now it is AM time – it is easier, it has to cost less, and the company can afford a new junior team.

## One year after the go live

Fast forward, and it has been one year of intense work. Bugs have been fixed, little things have been changed, and little things have been added. 

The system has been eventually made ready to sustain a real production load and the codebase has grown. At this point the AM Team receives a request to add a new big feature. 

And we are back to the initial question. Is it easier to add the new feature now or was it easier to add a new feature when we were in project mode?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1-leZpJJQ4qsyleIHMzG7Tdg.png)

The answer is clear: the task for the AM team is much more difficult. It is true that the AM team is sitting on their experience developed over time. But at the same time the AM team needs to deal with a not-very-stable code base, avoid introducing regressions without having a decent test safety net, and devise a way to deploy a new major version without creating disruption.

Let’s say it. The AM team often faces a much tougher job than the Project team. So why, if the task of the AM team is tougher, do all the experienced developers work in the Project team (and are now somewhere else, probably doing something else cool)?

## A possible answer: the Project team needs to lay the right foundations

One reason to have the most experienced people starting a Project is that, at the beginning, we need to lay the foundations for what is to come. We need to define the architecture and make some fundamental decisions about the design of the solution, so the right experience is required.

At the same time though, at the beginning of a Project, we usually have only a limited knowledge of the problem we are called to solve. 

At the start of any significant Project there are many known unknowns and also many unknown unknowns. For this reason, the Architecture of the system always has to be considered evolutionary. We need to be aware that many crucial decisions can not be made at the beginning but have to be made when the unknowns start to reveal themselves.

Architectural decisions can rarely be decided once for all at the beginning of a project. Critical architectural questions may pop up at any time in the life of the SW system. And those critical decisions made at the start of the project may have to be overhauled later – maybe because of new requirements, maybe because of new technologies like the Cloud, maybe because they were simply the wrong ones for the problem to solve.

So yes, it is true, the Project team has to make architectural decisions. But the AM also team has to make architectural decisions, and it has to make them in a much more complex environment.

### You simply can not do the reverse

While the classical model of a strong Project team followed by a more junior AM team is not the most efficient in the medium term, the opposite is not an answer either. 

Most companies can't imagine having a junior team starting a project and then transitioning it to a more senior team for maintenance. It's just not an option.

## A case for subconsciousness

Maybe one profound reason why more senior people start new Projects with cool new technologies is that they like to start new things and play with new tech. But then over time, when the work seem to become more repetitive, they simply want to move on to other challenges.

This is good for their tech curiosity and this is good for their resume. But this is probably not good for the long term health of the SW system they are building.

## From Project team to Product team

In 2006 Werner Vogels CTO at Amazon coined the famous [“you build it, you run it”](https://queue.acm.org/detail.cfm?id=1142065) motto. It conveyed the idea that a team responsible for a Product needs to take care of it from its inception down to its run phase (where run covers both the Ops aspects as well as the evolution aspects). 

To put it simply, the same team is responsible for all phases required for a Product to be successful: design, build, run, evolve. 

This is the model adopted by the digital giants that have emerged in the last decade, from Amazon to Facebook to AirB&B. Their undisputed success is the proof that the model is the right one in the digital era.

Nowadays a growing number of people are emphasizing the need to move from a project-oriented way of organising work to a more product-oriented model. 

This is a complex transformation which involves many aspects of an organisation. But for the topic we are debating here it definitely means that we need to abandon the idea of separate Project and AM teams and create more stable Product teams. 

Product teams need to have the right mix of experienced people and more junior people who need to grow. Working together with the experienced devs, juniors gradually become experienced themselves. Controlled rotation is then possible without tampering the quality of the team.

## Conclusion

In the era we are living, the Digital era, we should be suspicious when we hear something like _“and when the Project ends we will transition to AM”_. 

This is not to say that there is no space for AM any more. There are still old legacy systems, usually serving the back office, which are egregiously doing their work, which are very stable, and which just need some Maintenance. 

But when it comes time to develop new differentiating digital capabilities we need to move away from the Project/AM model and embrace a Product oriented model. 

In this model, teams are designed to be responsible for building not only the first version of the Product they also run it. And they learn from running it while evolving it over time to make sure it remains relevant for its end users.

