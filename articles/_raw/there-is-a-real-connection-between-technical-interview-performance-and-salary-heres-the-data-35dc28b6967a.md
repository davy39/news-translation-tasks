---
title: There is a real connection between technical interview performance and salary.
  Here’s the data.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T15:43:04.000Z'
originalURL: https://freecodecamp.org/news/there-is-a-real-connection-between-technical-interview-performance-and-salary-heres-the-data-35dc28b6967a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e1hE-C-WLWb7IcgPu_iulQ.png
tags:
- name: interview
  slug: interview
- name: research
  slug: research
- name: salary
  slug: salary
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cat Hicks

  At the end of the day, money is a huge driver for the decisions we make about what
  jobs to go after. In the past, we’ve written about how to negotiate your salary,
  and there are a lot of labor statistics and reports out there looking at ...'
---

By Cat Hicks

At the end of the day, money is a huge driver for the decisions we make about what jobs to go after. In the past, we’ve written about [how to negotiate your salary](http://blog.interviewing.io/exactly-what-to-say-when-recruiters-ask-you-to-name-the-first-number/), and there are a lot of [labor statistics](https://www.bls.gov/opub/btn/volume-7/high-tech-industries-an-analysis-of-employment-wages-and-output.htm) and reports out there looking at salaries in the tech industry as a whole. But as with many things in eng hiring, there’s very little concrete data on whether technical interview performance plays a role in compensation offers.

So we set out to gather the data and asked our users who had gone on to successfully get jobs after using our platform to share their salary info. With our unique dataset of real coding interviews, we could ask questions like:

* **Does interview performance matter when it comes to compensation packages?**
* **Do engineers who prioritize other parts of a role over compensation (e.g. values alignment) end up with lower salaries?**
* **What else seems to matter in getting a higher salary?**

To be clear, this is an exploration of past average interview performance and its connection with current salary, versus looking at how someone did in an interview and then what salary they got when they took that specific job. In other words, we haven’t paired job interviews with the salary for that same job. We believe that looking at these more general measures is more informative than trying to match single interviews and job offers, given [how volatile individual interview performance can be](http://blog.interviewing.io/after-a-lot-more-data-technical-interview-performance-really-is-kind-of-arbitrary/). But our interviewing platform allowed us to look at performance across multiple interviews for respondents, which gave us more stability and more data.

### The setup

On the interviewing.io platform, people can practice technical interviews online and anonymously, with real engineers on the other side.

When an interviewer and an interviewee match on our platform, they meet in a collaborative coding environment with voice, text chat, and a whiteboard and jump right into a technical question. Check out our [recordings](https://interviewing.io/recordings/) page to see this process in action.

Interview questions on the platform tend to fall into the category of what you’d encounter at a phone screen for a back-end software engineering role, and interviewers typically come from top companies like Google, Facebook, Dropbox, Airbnb, and more.

After every interview, interviewers rate interviewees on a few different dimensions: technical skills, communication skills, and problem solving skills. These each get rated on a scale of 1 to 4, where 1 is “poor” and 4 is “amazing!”. On our platform, a score of 3 or above has generally meant that the person was good enough to move forward. You can see what our feedback form looks like below:

![Image](https://cdn-media-1.freecodecamp.org/images/MookWFvqheOI-cFDaIb3qAxXoD4rtgkY7Kj8)

With this in mind, we surveyed interviewing.io users about their current roles, including salary, bonuses, and how satisfied they felt in their job. We then tied their comp back to how they did in interviews on our platform.

We ended up with responses from [494 engineers](http://blog.interviewing.io/#perfcomp-fn1), and because compensation packages are so complex and vary from company to company, we analyzed the data in several different ways, looking at annual salary numbers, bonuses, and equity. Then we tied compensation data to performance in technical interviews to see whether it matters, and if so, how much.

### The results

We looked at the relationships between interview performance (technical skills, communication ability, and problem solving ability) and the following: base salary, bonuses, and equity. In all cases, we corrected for location (being in the Bay Area means a higher salary) and experience (senior engineers make senior salaries), and where we could, we corrected for company size (bigger companies can generally pay bigger salaries).

The mean yearly salary for all survey participants was around $130k, and 57% of them reported a yearly bonus. For that group, the average yearly bonus was $20k. For people who reported a dollar amount for equity, the average was $54k. Below is the distribution of experience level/seniority of survey respondents.

![Image](https://cdn-media-1.freecodecamp.org/images/il3CxfIfbXk45uSD5Mm75KZhzP4wPcRnqI7M)

### Here’s what we found.

Better technical skills correlate with higher compensation

As probably comes as no surprise, people who score higher on technical skills during interviews do make more money. First, let’s look at base salary. [[2](http://blog.interviewing.io/#perfcomp-fn2)]

![Image](https://cdn-media-1.freecodecamp.org/images/x0SWlVnwkoF52Aucdj-wbeRiZ8xVeCbxHoEd)

Bonuses, too, correlate with technical skills, with an additional point in performance potentially worth about 10k. [[3](http://blog.interviewing.io/#perfcomp-fn3)]

![Image](https://cdn-media-1.freecodecamp.org/images/vezSelskCD7svFMEEMd0-3jHttZMOyi6VnzZ)

### The relationship between compensation and other interviewing skills

We also looked at the two other ratings that interviewers give after interviews: communication and problem solving. **Better communication scores had a small but statistically significant correlation with salaries** (r = .15, p < .01), but we found no significant relationships for problem solving scores.

![Image](https://cdn-media-1.freecodecamp.org/images/wWh1gmABIkUHXlBOmJzJJ4X6aIRA9rMKWFyb)

We also didn’t see a relationship between either communication ability or problem solving ability when it came to bonuses.

The non-relationships didn’t surprise us too much, to be honest, because with a relatively small sample size it’s notoriously difficult to get subcomponents of ratings to show a relationship to something distal and complicated like salaries. It’s very possible these relationships do exist, and with many determiners besides actual interview performance, like seniority and market salary norms, we’d like to repeat this survey at a bigger scale to inform this question.

### What else?

We asked engineers whether they felt satisfied with their role, and found that engineers who felt satisfied earned an average $14k more than engineers who felt dissatisfied. [[4](http://blog.interviewing.io/#perfcomp-fn4)]

We also looked at people’s perceptions of their own performance. [In a previous post](http://blog.interviewing.io/impostor-syndrome-strikes-men-just-as-hard-as-women-and-other-findings-from-thousands-of-technical-interviews/), we explored how people rated their own technical performance after an interview compared to how the interviewer rated them, and found that even experienced engineers aren’t great at guessing how they did.

For this project, **we were curious about whether overconfident engineers might net higher salaries** (perhaps they negotiate harder!). So we also looked at people who rated their performance higher than their actual interview score — **but found no difference in their compensation packages.**

Another thing we were curious about was whether people who valued money over other factors while making a job decision would have higher salaries. So we asked people to rank the most important variables in their job decisions. 32% of respondents said that a compensation package was the most important part of their decision; the next highest response was “matches my interests and values.”

But these questions didn’t have any predictive value for the actual salary amount: **people who said money matters the most didn’t have significantly different salaries from people who said money matters the least.**

It’s possible that with salaries being impacted by so many outside factors, like location and role type, candidates don’t truly have a lot of negotiating power over that salary number.

We looked at equity as well, and the average reported equity package size was 54k. We did not find any significant association between interview performance and reported equity packages. That said, enormous amounts of research have documented various salary gaps based on gender, race, and other important sociocultural and demographic factors, and we hope to repeat this analysis when we have more data.

### What do these findings mean for you?

Interview performance doesn’t just get you in the door or not: it can have a demonstrable connection to your eventual compensation. For instance, **doing just a point better in your technical interview could be worth 10k or more, and with bonus, it could add 20k to your annual comp.**

Given how much technical interview performance matters, we’d be remiss if we didn’t suggest [signing up for free, anonymous mock interviews](https://interviewing.io/signup) on our platform. So, please go do that.

And, if you’re curious about what [our salary survey](https://interviewingio.wufoo.com/forms/salary-survey) looked like or want to participate and contribute to v2 of this post, please do so too!

_Want to become awesome at technical interviews and land your next job in the process? [Join interviewing.io](http://www.interviewing.io)!_

[_Cat Hicks_](https://www.drcathicks.com/)_, the author of this guest post, is a researcher and data scientist with a focus on learning. She consults in research, has published empirical research on learning environments, and has led research on the cognitive work of engineering teams at Google and Travr.se. She holds a PhD in Psychology from UC San Diego._

