---
title: I tried Pandora’s brilliant method for feature prioritization. Here’s what
  I learned.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-20T16:27:30.000Z'
originalURL: https://freecodecamp.org/news/i-tried-pandoras-brilliant-method-for-feature-prioritization-c5fb586ad317
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8s-VzNIcca2gZ3JNLseODw.jpeg
tags: []
seo_title: null
seo_desc: 'By Josh Temple

  How Pandora’s method and a $3 pack of sticky notes made stakeholder management a
  breeze.


  Sticky notes: $3. Stakeholder buy-in? Priceless.

  Army of one

  Like many data professionals at small and mid-size companies, I’m a data team of
  one...'
---

By Josh Temple

#### How Pandora’s method and a $3 pack of sticky notes made stakeholder management a breeze.

![Image](https://cdn-media-1.freecodecamp.org/images/9ExPNpdhUc77MfTrKEDoUIem-zZNS5w8k9Na)
_Sticky notes: $3. Stakeholder buy-in? Priceless._

#### Army of one

Like many data professionals at small and mid-size companies, I’m a data team of one at [Milk Bar](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities). As the first data hire, I’ve had the rather terrifying privilege of building our data stack from the ground up. I’ve spent the first few months of my time here building data loaders, modeling our data in BigQuery and [dbt](https://www.getdbt.com/), and deploying and training our teams on [Looker](https://looker.com/). Now that our data stack is functional, it’s time to plan for next quarter.

The value of business intelligence and analytics is quickly becoming apparent at [Milk Bar](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities), and more people are coming to me with feature requests. My backlog is filling up faster than I can knock out features, and I need to be sure that the projects I tackle next quarter are truly essential to the business. I read about Pandora’s product prioritization process a few months ago and I thought it was brilliant, especially for small, resource-strapped teams, so I decided to give it a try.

#### The Pandora method

The credit for this system goes to [Tom Conrad](https://www.linkedin.com/in/tomconrad/), 10-year CTO at Pandora, who developed the approach. I encourage you to read [this article](https://firstround.com/review/This-Product-Prioritization-System-Nabbed-Pandora-More-Than-70-Million-Active-Monthly-Users-with-Just-40-Engineers/) from First Round Review, which describes Pandora’s process in detail, but I’ll summarize it here:

1. The team leader collects ideas for features that are “no-brainers” from across the company. These aren’t supposed to be flashy, R&D-esque projects — they’re supposed to be ideas that the company would be _stupid_ not to tackle during the next quarter.
2. Each idea is condensed into a single slide that describes the impact to the business and how success will be measured.
3. Each idea is also assigned a dollar-amount cost based on the estimated amount of engineering time required to build it. Pandora decided that $5 would be equal to one month of one engineer’s time. Since my team is much smaller, my cost ratio was $5 for one day of my core development time.
4. The team leader holds a meeting with relevant decision makers. Conrad recommends that you choose leaders who aren’t too tied to one function and understand company-wide priorities, like the CEO and CFO.
5. The team leader talks through each feature and answers questions, then tapes a printout of each slide to the wall. The team leader divides the total “budget” of the team’s time among the decision makers in the form of sticky notes — each sticky note representing $5.
6. During the first round, the decision makers vote by placing their $5 sticky notes on the feature slides they want to see funded. Afterwards, they can discuss, negotiate, and shift their dollars around in the second round.
7. After some shuffling, the features that remain funded are the features the engineering team is responsible for building the following quarter.

The method is similar to [capacity-based planning](https://www.mountaingoatsoftware.com/blog/capacity-driven-sprint-planning) and borrows from Agile principles like [story points](https://www.atlassian.com/agile/project-management/estimation) and weight. It’s meant to solve the fundamental problem that technology teams are often asked to build many more features than they have time for. Capacity-based planning isn’t a new concept, but this method is special because it forces stakeholders with competing priorities to align on the set of features that is best for the whole business.

#### What I expected and hoped to happen

To use this method at [Milk Bar](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities), I needed to determine my total available budget for feature development. Historically, I’ve spent about 20% of my time working on ad-hoc requests, 20% on infrastructure and reliability upgrades, and 60% on core development. With 61 working days in the first quarter of 2019, this meant I would have about 37 days for core development. Using my cost ratio of $5 per day of core development, I calculated a total budget of $185.

I collected about 15 data product feature requests from across the company and from my backlog. These ranged from simple dashboard build-outs ($5, or one day of my time) to entirely new data sources that required extensive ETL and modeling ($65, or almost three weeks of my time). The total cost of all the features was well over $400, more than _double_ my amount of core development time for next quarter. This really drove the point home for me. I hate saying no, but I definitely **did not have enough time to build everything I was being asked to build**, even if I wanted to! I hoped that clearly showing this gap between demand and capacity would give me ammunition to ask for additional headcount for my team.

Next, I pared down each feature request into a concise slide describing the impact to the business and metrics for success. I don’t think there’s a particular way to do this, but it’s important that the slide is succinct enough to understand quickly when your decision makers need to read through 50 of them. Here’s an example of one of our feature slides:

![Image](https://cdn-media-1.freecodecamp.org/images/df1OonSQ7kTtQvFR4K1nk70OinHHWE1xAB2X)
_An example of a feature slide for a product performance dashboard._

After compiling all of the feature slides, I realized that the most likely outcome was that the decision-making team would coalesce around a few high-impact, high-cost features. I’ll call these foundational data features. They are projects like new API integrations or data sources, new Looker explores, and other similarly complex builds. I figured our decision-making team would end up leaving many of the medium-cost feature requests that I considered “nice-to-haves” unfunded.

I knew I wouldn’t be able to build out the foundational data features without having to say no to quite a few of the smaller feature requests, and I hoped this process would help our decision-making team arrive at that realization on their own. It would be easier for everyone to decide together than to have to tell some of our leaders that their needs were less important than the needs of another team.

#### The outcome

I met with our team leads, our strategy manager, and our COO for about an hour. I presented each feature slide and answered questions about a feature’s importance or why it was priced a certain way. Reminding everyone that the purpose was to select the features that were best for [_Milk Bar_](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities) _as a whole_, I turned them loose to discuss, negotiate, and spend their budget. Having our COO and strategy manager in the room certainly helped, because they weren’t tied to a function and were able to mediate and settle disagreements about priorities.

After the dust settled, **only 5 of the 15 original features remained funded.** I thought this was stunning, since the team leads that I work with had strongly advocated for each feature in our individual meetings.

[Conrad summarizes](https://firstround.com/review/This-Product-Prioritization-System-Nabbed-Pandora-More-Than-70-Million-Active-Monthly-Users-with-Just-40-Engineers/) my thoughts on the outcome…

> This is incredible, because someone very smart at one point thought, “We would be absolutely stupid not to do this thing.” But really, when viewed in context of all the opportunities for the business, half of the things people thought were important immediately fall away.

**That was exactly what happened.**

Our team of decision makers aligned on a few of the highest-impact features, choosing not to fund some of the smaller, “nice-to-have” projects that had been suggested. Some of the features didn’t receive a single vote.

This was a perfect opportunity for me to mention that we would have nearly double the capacity for new features if we were willing to hire another data engineer. After going through the difficult process of cutting features that still felt important, our leaders clearly understood the need for additional headcount and even asked me to push up my hiring timeline. I can’t think of a better way to ask for more resources.

Overall, in my first experience with this method, I observed some significant benefits…

* All my stakeholders have a **clear understanding of what I’m working on** next quarter, how time-consuming each project is, and the priority of every project relative to the others.
* **We only picked things that _really, really_ needed to be done.** Stakeholders were willing to accept the status quo where it was sufficient to save budget for the features they didn’t want to live without.
* I gained **more support for hiring** more data engineers and analysts.
* **Stakeholders saw how important their needs were** relative to other needs across the company. They were willing to cede features that were more specific to their teams in favor of higher-impact features.
* Saying no to a feature request can sometimes make a stakeholder feel that they aren’t valued. In this case, **everyone enjoyed the process.** It was time-efficient and fun. Someone said the idea was “genius,” and our COO told me it was an “excellent meeting and a brilliant approach.”

#### Advice for adopting this approach

I would absolutely recommend this method, and I can’t wait to do it again at the end of next quarter. Here are my recommendations for using this method.

* **Planning is key.** Take your time meeting with your stakeholders and learning about the features they want. You want to form a complete picture of what your stakeholders need from you over the next quarter, and it’s better to ask them than to guess.
* **Be ready to explain each feature concisely.** You need to be able to understand the motivation and planned execution of each feature well enough to describe it quickly and clearly. It’s worth practicing describing each feature slide in less than a minute before your final decision meeting.
* **Be ready to explain why some features were more expensive than others.** Some of our team leaders were initially frustrated to see that features they asked for cost more than their entire allocated budget. Make sure you can justify the cost with a legitimate estimate of work and can explain your estimate.
* **Keep it light but stand your ground.** As the facilitator, try to keep the atmosphere fun and help to diffusion tension or disagreements when they arise. At the same time, be firm with your estimates of work. Ultimately, you only have so many hours in the day, so don’t be afraid to remind your stakeholders that you can’t create more time. If they push back, you have an excellent opportunity to propose additional headcount for your team.

If you use the Pandora method already, are interested in giving it a try, or have suggestions about how to improve this process, please let me know in the comments!

_If you enjoyed this article, please give it some claps (on a scale of 1–50) below! Follow me [here](https://medium.com/@josh.temple) for more content about data engineering and analytics in small to mid-size companies._

