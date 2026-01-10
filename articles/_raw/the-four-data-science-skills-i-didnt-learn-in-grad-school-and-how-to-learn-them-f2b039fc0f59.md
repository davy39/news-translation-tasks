---
title: The four data science skills I didn’t learn in grad school (and how to learn
  them!)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-09T08:15:46.000Z'
originalURL: https://freecodecamp.org/news/the-four-data-science-skills-i-didnt-learn-in-grad-school-and-how-to-learn-them-f2b039fc0f59
coverImage: https://cdn-media-1.freecodecamp.org/images/1*blP7oR05ndTi_p8155W0Kg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rachael Tatman

  Before I get to the meat of this post, I want to make one thing super clear: you
  do not need a graduate degree to be a data scientist. Unless you’re doing cutting-edge
  machine learning research (which, let’s be honest, doesn’t descr...'
---

By Rachael Tatman

Before I get to the meat of this post, I want to make one thing super clear: you do _not_ need a graduate degree to be a data scientist. Unless you’re doing cutting-edge machine learning research (which, let’s be honest, doesn’t describe 99.9% of data scientists — including me!), a degree in how to do research just isn’t necessary. Anyone who tells you differently is trying to sell you something — probably a data science graduate degree.

That said, I did learn a lot of valuable skills in grad school. I learned how to deal with messy data, ask good questions, determine which statistical tool to use in a specific situation, write code for statistical computing and machine learning and, last but not least, clearly communicate technical concepts.

These are all skills that every data scientist needs. What they are not is the _only_ skills a data scientist needs. Two of the roughest parts of the transition from grad school to industry for me were 1) identifying the skillsets I was missing and 2) figuring the best way for me to get up to speed on them.

Fortunately, if you’re in the same place I was, I’ve got you covered. Without further ado, here are four data science skills I didn’t learn in grad school, along with some practical tips on how you can learn them.

### SQL

I’ve found that most graduate students who are exploring data science as a career are already familiar with R or Python (or both!). On the other hand, far fewer folks in this position know SQL. And that can be problem when you’re ready to go on the data science job market: after Python and R, [SQL is the third most widely-used tool in data science](https://www.kaggle.com/surveys/2017).

SQL (usually pronounced like “sequel”) is a programming language specifically for interacting with databases. It’s fairly rare to see it used in an academic context, but it’s ubiquitous in the industry. Fortunately, the basics are relatively easy to learn and there are a lot of educational resources out there to help you get started.

How to learn SQL:

* **Take a course**. There are a lot of online options out there, including courses by [Khan Academy](https://www.khanacademy.org/computing/computer-programming/sql), [DataCamp](https://www.datacamp.com/courses/intro-to-sql-for-data-science), [Stanford](https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/about) and [Udemy](https://www.udemy.com/introduction-to-databases-and-sql-querying/). In person courses are a bit harder to find, but if you check a local university, community college or code camp you might get lucky.
* **Develop a SQL portfolio**. Having examples of your ability to write queries on real databases is good evidence that you’re familiar with the language. One option is to write kernels (i.e. hosted R or Python notebooks) on BigQuery datasets on Kaggle. I’ve written [a quick how-to](https://www.kaggle.com/rtatman/sql-scavenger-hunt-handbook/?utm_medium=blog&utm_source=medium&utm_campaign=fcc) to get you started. (Full disclosure: I work for Kaggle. :) [HackerRank](https://www.hackerrank.com/domains/sql) and [SQLZOO](https://sqlzoo.net/) also have quite a few SQL exercises.

### Being a Generalist

Grad school is great! Your day-to-day work is expanding the borders of human knowledge, which is pretty rad. As you work through your degree, you really drill down into one specific topic, asking increasingly precise questions in a narrower and narrower domain. Eventually, you’re the most knowledgeable person on the planet about your little sub-sub-sub-niche. There’s nothing wrong with this: it’s just how scholarly inquiry works.

It is _not_ how data science works. Unless you’re very lucky and end up working on the precise thing you wrote your dissertation or thesis on, you’ll be expected to work on problems outside your field pretty much immediately. And not just things from outside your field: problems from fields you’ve never even _heard_ of. You’re going to have to get used to working on things you’re not an expert on very quickly.

Here are some ways to get better at being a generalist:

* **Read outside your discipline**. Academic disciplines tend to use a specialized set of statistical tools. In sociolinguistics, for example, we work a lot with mixed-effects regression — but there are a lot of other statistical approaches out there. Reading work in different disciplines will expose you to a wide range of different techniques and problems and help get you get comfortable jumping feet-first into a new topic.
* **Practice analyzing new types of data**. Data scientists need to work with all sorts of data. You probably already have deep experience with one type of data, but consider branching out. Have you worked with time series? Text? Images? Video? Audio? Pre-trained models? Relational databases? Figure out what the gaps there are in your knowledge and try your hand at working with some new and different sources. (Obligatory plug: [Kaggle has more than 10k public datasets](https://www.kaggle.com/datasets?utm_medium=blog&utm_source=medium&utm_campaign=fcc) from a huge variety of sources. You can also check out [Zenodo](https://zenodo.org/) or the [Dataverse project](https://dataverse.org/).)
* **Talk about technical concepts with people outside your field.** Not only will you learn a lot, you’ll also have a chance to practice explaining technical concepts to people who don’t share your specific academic background.

### Source/Version Control

This one is a little bit of a cheat for me: I actually _did_ learn source control in grad school, thanks to a [Software Carpentry workshop](https://software-carpentry.org/). It’s so, so, so valuable, though, and I know that a lot of my peers in grad school weren’t exposed to it.

Source control, also called version control, is a way to manage making changes to a single centralized document or code base. The basic idea is that you do your work on a copy of whatever-you’re-working-on, and every so often you use that copy to update the original. It’s helpful for individual projects (it lets you roll back to that one version that actually worked and figure out what you broke) and pretty much mandatory for technical collaboration.

How to learn to use version control:

* **Use version control on every single research project and paper from here on out**. I’m 100% serious. My entire dissertation was version controlled and it saved my butt so many times I lost count.
* **Use GitHub for your personal projects (if you have any) or research you can share.** This is optional, but helpful if you end up joining a team that uses GitHub. In addition, an active GitHub profile is one way to demonstrate your workflow to potential employers.

### Stopping at “Good Enough”

When you’re working in an academic setting, you really do need to make sure everything is a good as it can be. Your work is going to be closely evaluated by experts and, if it passes muster, it will be added to the scholarly literature permanently. When you’re working in an industry setting, on the other hand, it’s far better to have something useful _now_ than something very polished eventually.

One of the first new terms I learned working in an industry setting was MVP, or “Minimum Viable Product”. The idea is that you share something when it’s just good enough to satisfy some portion of the people that will interact with it. In a data science setting that means not answering every single question you could with the data, or having a model that’s less accurate than it could be with additional tuning. You may have time for deeper analysis or additional tuning later, but you should be ready to share projects the moment they get to “good enough”.

How to improve on seeing what’s good enough:

* **Work on identifying “done for now”.** The next time you work on a project, stop every so often, maybe before you wrap up every day, and think about whether you’ve already created something valuable (you probably have!). Take a minute to practice how you might describe what’s useful or interesting about what you’ve already done.
* **Consider sharing intermediate stages of your research**. If you can, consider sharing the intermediate stages of your next research project, maybe in a blog or to a lab mate. It may not be ready for the limelight, but is this piece of your analysis novel? Did you learn something worth sharing during the data collection? What have you made that’s already good enough that someone else might find it valuable?

And there you have it, four key skills that I use more-or-less every day that grad school didn’t teach me. Other data folks: feel free to chime in with necessary skills you picked up after you were finished with your degree!

