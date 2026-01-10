---
title: Does a Computer Science degree really boost your salary? I crunched the numbers
  to find out.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T23:48:48.000Z'
originalURL: https://freecodecamp.org/news/does-an-undergrad-computer-science-education-affect-a-web-developer-s-salary-80711fff9298
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QAU9qepvrMDis8FJuX0Pdw.jpeg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Leigh Silverstein

  I was in the middle of writing an article about the correlation of specialization
  to salary in the software industry. I had worked out the theory of why and how specialization
  affects salary, and where specialization tends to occ...'
---

By Leigh Silverstein

I was in the middle of writing an article about the correlation of specialization to salary in the software industry. I had worked out the theory of why and how specialization affects salary, and where specialization tends to occur. The only thing I needed was statistical proof.

So I took the [2017 Stack Overflow Survey Data](https://insights.stackoverflow.com/survey/2017), cleaned it, and started plugging in variables from previous analyses that were [known to affect final salary](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/).

One of the trickiest part of data analysis is understanding which variables you want to test for, and which ones you don’t. That way, you can control their behavior.

For example, I could test to see whether using PHP at work increases your salary. But if I didn’t factor in the country of the respondents, I wouldn’t be able to truthfully account for the influence of PHP.

Since I was testing specialization, I needed to simplify the dataset and improve sensitivity to changes in specialization. I chose to use only professional web developers from the United States, and to account for specialization, I was looking to test the salaries of frontend and backend specialists against full-stack generalists.

I gradually added in variables: Experience, Education, Web Developer Type. The results weren’t perfect. I was expecting formal education to have a more positive influence, but I was optimistic, and I was already seeing some evidence of the advantage of specialization.

And that’s when something unexpected happened.

I am a web developer by trade, and I do full-stack development. I’ve always speculated that if I had been a little more mature, and acquired a computer science (CS) degree instead of a fine arts degree, I might be making a lot more money.

One of my younger brothers has a CS degree, and our pay appears to be on two different scales, and these scales will never meet. Everyone I meet who has an interest in programming, I always tell them that a undergraduate CS degree is worth at a minimum, a 20k pay difference in perpetuity, and I think I’m being conservative.

So you can imagine my shock when I ran the analysis for undergrads with CS degrees against everyone else. **There was no significant difference.**

“Surely I made a mistake,” I thought. The first time I ran the analysis, I had lumped CS grads in with engineers, mathematicians, and information technology graduates. Clearly CS needed to be separated into its own division.

So I ran the analysis again.

But again, there was no significant difference.

![Image](https://cdn-media-1.freecodecamp.org/images/9gus9Ht0EpJUUXSr336yImPd3Z1cC7TdDrQg)
_Linear regression on factors that affect salary for professional American web developers_

### Let me outline exactly what was going on here.

When I accounted for formal education, experience, web developer type, and undergrad major, **there was no correlation** between having a CS major — or an engineering or mathematics major — and salary.

So I started removing variables. “Maybe CS majors generally stream into the backend,” I thought. So I remove the “web developer” type. No correlation.

I removed formal education altogether. No checking for a bachelors, or a masters, or a doctoral degree. No correlation.

### I tried every combination imaginable. And I could not find a significant link between having a CS undergraduate degree and earning a higher salary.

There are several possible explanations for the lack of statistical relevance surrounding the undergraduate CS degree and salary. The first thing that comes to mind is that the data is bad. It wasn’t a proper sampling of the population, or people lied, or people didn’t complete the survey.

We know, for example, that women were misrepresented in the [initial findings](https://medium.com/@glitterwitch/stack-overflow-s-developer-survey-analysis-hurts-women-ec4d568e2352). We can also see that only a third of American professional web developer respondents actually included their salary, and from the ones that did include it, the majority were from the US $90,000 to $130,000 annual salary range.

We know that the national average salary for a web developer is [closer to $70,000](https://www.bls.gov/oes/current/oes151134.htm). So there’s a possible bias here, where people would only report their salary if they were proud of it.

So I tested this hypothesis by assigning all N/A salaries with a below average $40,000 salary. I found that it broke all of the previous correlations, and resulted in no new revelations.

Another possibility was that CS-educated undergrads stream into something other than web development, leaving the stragglers for web development. It’s a stretch, I know, but I’m really trying to get to the bottom of this.

Statistics is as much an art as a science. It’s easy enough to run regressions on data and find correlations, but sometimes it just comes down to the logic of the whole thing. In dishonest hands, statistics can be used to convey falsehoods.

> “There are three kinds of **lies**: **lies**, **damned lies, and statistics**.” — Mark Twain

Looking back at the first linear regression, I noticed a question regarding respondents who had gone to college, but hand’t earned a degree. A whopping 14% of the respondents were students who didn’t complete their degrees.

The variable was insignificant, but the estimated effect was strongly negative. What if some of the students dropping out of college and university were CS majors?

I created two interaction variables: one for CS students who completed their bachelors, and another for CS students who completed their masters. The results were significant, and highly positive. It looked like having a CS undergrad degree did indeed affect salary.

![Image](https://cdn-media-1.freecodecamp.org/images/0vl-VGnI1J3I7PYLVg6TE6FAXXNjXliZrcE5)
_Linear regression on factors that affect salary for professional American web developers with cs interaction variables_

Or did it? Look at the effects of having majored in CS and having completed a bachelors in CS. The signs are nearly equivalent. Barely a thousand points off.

Having a CS undergrad with a masters degree, on the other hand, was worth an extra $10k. **So if you’re interested in web development, and you already have a CS undergrad degree, you might want to consider doing a masters.**

So I’m almost back where I started. Having a CS degree does affect salary, but the effects are nowhere near my initial assumption of a $20,000 boost.

Instead it’s closer to $1,000 — which for most of the developers who responded to the survey with their salary means **less than a 2% difference in total income.**

Now maybe this comes as a shock to me because I’m a Canadian, and we tend to be a little more reserved when it comes to sifting through resumes. Maybe a CS degree is worth more here. And maybe it’s worth more in a lot of places in the world. But CS degrees don’t seem to affect the salaries of professional web developers in the United States.

