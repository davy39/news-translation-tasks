---
title: GSoC 2023 Guide – How to Prepare for Google Summer of Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-16T17:04:36.000Z'
originalURL: https://freecodecamp.org/news/google-summer-of-code-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-prateek-katyal-2763246.jpg
tags:
- name: gsoc
  slug: gsoc
- name: open source
  slug: open-source
seo_title: null
seo_desc: "By Abhisman Sarkar\nGoogle Summer of Code is an open source program that\
  \ is managed by Google's Open Source team. \nThey invite developers to spend their\
  \ summer contributing to the source code for various different organisations taking\
  \ part in the prog..."
---

By Abhisman Sarkar

[Google Summer of Code](https://summerofcode.withgoogle.com/) is an open source program that is managed by Google's Open Source team. 

They invite developers to spend their summer contributing to the source code for various different organisations taking part in the program. 

There are many organisations that list their project ideas for participants to choose from. Last year, in the [2022 season](https://summerofcode.withgoogle.com/archive/2022/organizations), a whopping 202 different organisations took part in the program and the program ended with around 1166 projects being completed. 

Think about the sheer amount of code that was written and how much open source organisations and users in general benefited from it. You can learn more about last season [here](https://opensource.googleblog.com/2022/12/gsoc-2022-its-wrap.html).

I was among those contributors, writing code for the [TUF](https://theupdateframework.io/) project. My work involved introducing backwards compatibility to TUF's Python client so that downloading metadata adhering to different tuf versions could be easily managed. 

I am writing this tutorial to teach you about GSoC and how you can increase your chances of getting selected into the program. I'll also go over how it'll benefit you both from a learning and a career perspective. I hope it will get you inspired enough to contribute to open-source and apply for GSoC, even if you've never done that before.

# GSoC Timeline

GSoC follows a similar timeline every year. You can find the page for the 2023 session [here](https://developers.google.com/open-source/gsoc/timeline). 

The page pretty much explains all you'll need to know, and you can find the precise dates for each announcement. But still, I'll share my tips on how to prepare for each step of the journey and the best courses of action to take along the way.

The first 3 announcements are org-specific. Meaning, you don't have to worry about them since they are dates for organisations to apply to have their projects included as part of the GSoC program.

## List of Accepted Mentoring Organizations Published:

Once the orgs get announced, start going through the list and take a look at the project ideas that seem interesting to you. 

Don't target too many orgs. Try to go for a maximum of 2 or 3 project ideas within the same org. This makes you drive your efforts towards participating in that org and that really boosts your chances of getting selected. 

Targeting too many orgs divides up your efforts and it may result in you not getting admitted into the program. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-137.png)
_Org search page_

Filter through the orgs by entering your preferred programming language/org name/topic in the search bar. Once you open up an org's page, you'll be able to find the technologies and topics mentioned. Let's take a look at CNCF's page:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-161.png)
_CNCF GSoC page_

Here you can see all the different technologies and topics. Don't be discouraged if you don't know all of the tools, since those lists are for all the project ideas mentioned under the org (so there's a high chance that your particular project won't require all of them). Plus since the program is a learning experience, you'll be learning those topics yourself.

Click on the **Ideas List** next, and you'll be taken to a page that will show you all the different project ideas under that org. This is where you get to read through the description for each project and look at the tech stack for each one. 

You might find the **Difficulty** label under your project, but don't get disheartened if a project you find interesting is labelled hard. You can always learn on the go and implement what you learn. Chances are that you'll have to work a bit harder, but that's ok. 

Also under the project idea, you'll find the upstream repository and/or the upstream issue's page. Check it out and start reading the repository docs and all the other info.

Now you might be thinking – where would you go if you had any questions? Go back to the org's page on the GSoC website and you'll find links for the organisation's mailing list, public Slack channel, and Twitter among various other links.

If you can't find this info there, then go to the repository's page and you'll probably find links for the communication channels in the Readme file there.

After joining the public channel, introduce yourself over there and express your excitement to contribute to the project.

When you're asking questions, here are some thing to keep in mind. First of all, make sure you do your research by searching about your question online and then asking your question saying: "Hey, I have this problem. I did x research about this and came up with y answer though I think it may not be correct. I'd appreciate it if someone could help me, thanks." 

Phrasing your question like this shows to other people that you've thought about your question and tried searching about it online and you haven't just given up and not thought about the problem. People are then more likely to help you. 

Many times, if your question is a pretty common one, you'll get the actual answer online. Also, with the proliferation of AI tools, there's a pretty high chance that you'll find what you need. If not, go ahead and ask your question. 

Also, always try **not** to personally message someone. Ask your questions in the public channels. This way you have many people looking at your problem and so the chances of you receiving help increases. Personally messaging someone doesn't always guarantee a response since they're probably busy with their own work. So you asking a question with no one else to answer adds onto that work.

## GSoC Contributor Application Period Begins:

As a contributor, you'll have to form a proposal for your particular project idea within a deadline. 

For the 2023 session, contributor proposals start getting accepted from the 20th of March until the deadline on the 4th of April. Start working on your proposals beforehand and don't wait until the submission deadline. 

Here are a few tips from my side:

### Start the review process early

It's totally fine to ask your mentor to review your first draft of the proposal – but try to start the review process as early as possible. Implement your mentor's suggestions and then ask for reviews again. 

While doing that, be respectful of their time. They might not always be available, and in that case, try to get feedback from other maintainers working on the project. 

Always keep in mind that the maintainers are people who have a seperate work-life and that they're working on the project in their own free time. 

### Create a timeline

A good proposal is an important aspect of the selection process. [This page](https://google.github.io/gsocguides/student/writing-a-proposal#submit-a-proposal-early) has some good info regarding the subtopics you should mention. 

Make sure that you formulate a proper Timeline (Deliverable section) since that shows the mentor and maintainers that you've really thought about the project and how you aim to solve it. The actual dates of when you would implement something don't really matter – it's more about how you've thought about solving the project. 

Personally speaking, creating a timeline made a big impact on my selection process since my mentor mentioned multiple times that she liked the way I had thought about implementing the project. 

This really goes to shows that you've thought about the problem hard enough to come up with an approach toward solving it.

### Contribute to the project's repository

Contribute and work on issues in the project repository. They don't need to be big changes, but make sure they aren't only trivial ones either (like fixing grammar, deleting files, and so on). 

As you start contributing, start from easy issues and keep ramping up as you keep getting the grasp of the project. If you're someone who's new to all this then understand that the first step is usually the hardest and the upcoming ones are comparetively less difficult. 

When formulating your proposal, be sure to mention these prior contributions as they help make your proposal much more impactful. They also show your mentor that you are someone who has been contributing to the project.

### Talk about past experience

Include a passage about your past work experience and achievements (Biographical Information section). Mention work for which you have evidence as that helps add value to your proposal. Include any past open-source or hackathon or application building experience. 

Try to rank these experiences in order of relevance to the project and try not to overfill this section if you have too many. Keep it to a max of 8-10.

In addition to all these points, I suggest you to go through the page mentioned above and study the remaining points to get a good idea of what you should be mentioning in your proposal.

Once you're done formulating a proposal, create your own GSoC account and go to your contributor page. There you'll find the link to select the project you'll be working on and the link for submitting the proposal.

 In all, focus on 3 major key points while applying:

1. Have good code contributions to the project repository
2. Have a high-quality and well-reviewed proposal
3. Be active in the community by engaging with other contributors and participants

There were a few changes that got implemented in the 2022 session which are here to stay. They are:

* **Flexible project timing.** You could take anywhere from 10 to 22 weeks to complete your project. Extend your deadline if you feel that the 12 week period is not enough, but make sure to communicate with your mentor about this.

* **Choice of time commitment.** You'll have a choice between either a medium or long project.

* **Open to all.** GSoC as a program was open only to students until its 2021 season. But ever since the 2022 season, the program has started accepting everyone, student or not. Anyone looking to get into this program can get started.

The application deadline for the 2023 season is on the 4th of April, and you'll be hearing back on the 4th of May. 

I know, a month seems like a long time and you'll probably be getting anxious as the result date approaches. I know I was. If you do get selected, congratulations to you and your hard work. 

But if you don't, don't get disappointed since you've probably learnt so much about open-source through the process. And now you can work towards submitting your application for other open-source mentorship programs. [This](https://github.com/deepanshu1422/List-Of-Open-Source-Internships-Programs) page has some great info about all the other programs.

## Why You Should Do GSoC

So far, we've talked about the timeline and how to prepare your proposal. Now let's talk about the why. 

Why should you be interested in this program and in open source in general? Let's start by talking about open source.

### Why Open Source?

Working on **Open Source software** is a great way to help the broader community by contributing to projects that are used by millions of people around the world. The work that you put in helps improve software that is an important part of many large scale systems. 

Also the fact that almost all open source software is free makes it way for everyone to use it in their daily lives, be it large organizations or an everyday user. So devoting time from your busy life to work on OSS is a great and commendable feat. 

All of this sounds awesome, but **how does contributing to open source help you sustain yourself**? Working on open source allows you to obtain industry level experience. You'll learn what it's like to actually work on large projects. 

Being a contributor myself, I've had the pleasure of getting to know so much about how to actually work on changes. There are many factors that come in to play such as downloading the source code, adding changes to the code, running tests, testing out the changes manually by building a binary, pushing the changes, and so on. So much to learn.

Being a college student myself, I didn't have to wait for a job to learn about the industry. All I had to do was work hard and contribute to open source projects. 

Here are some excerpts from The Linux Foundation's [10th Annual Open Source Jobs Report](https://www.linuxfoundation.org/research/the-10th-annual-open-source-jobs-report) that might inspire you:

> According to 93% of the hiring managers surveyed, open source talent is increasingly difficult to find. As a result, companies are now turning towards training their staff in new cloud automation, orchestration, and developer productivity tools to close that gap as much as possible

> The vast majority of employers (93%) report difficulty finding sufficient talent with open source skills. This trend is not going away with nearly half (46%) of employers planning to increase their open source hiring in the next six months, and 73% of open source professionals stating it would be easy to find a new role should they choose to move on.

The report goes on to talk about how companies are willing to offer greater compensation to open source professionals and how financial incentives are making a much bigger difference. I'd recommend you to read and download the report to get a much more detailed description. 

All in all, open source is a great way for you to learn and obtain real world knowledge and also provide you with skills that will help you to get an edge in this competitive job market.

### How Does GSoC Help?

We talked about the benefits of open source and how it helps you learn a lot of real world skills. Now the question arises – how does GSoC play a role in this? 

Working on a repository and contributing code is great, but it can seem really daunting. Under a mentorship program like GSoC, you get to work on a project idea with the help of a guide who's an experienced mentor. They'll help you throughout the entire process. This over a period of 3 months or more really boosts your skills and makes you a much better developer than you were previously.

You'll develop a lot of new skills all while learning to code in a team. Your code contribution helps the project grow, too, since you'll be working on implementing various important features. This benefits both the project and the open source community in general. 

When I was participating in GSoC, I learned a lot about collaboration, good code practices, working with Git and so much about testing. I got to understand async practices and how to communicate my developments with my team, even if we were time zones apart. 

I was responsible for the code that I put in and delivering the work that was expected of mel. I believe that this really helped me to grow as a person and become a better developer. 

I also got to learn so much about what it actually was to work in a real life project and gain so much industry level experience from such talented professionals. This became an experience that I will always cherish.

Through this program you get introduced to the world of open source and get to meet and network with amazing developers who are going the extra mile to keep open source software free and available to all. You're introduced to a wonderful community of like-minded and passionate developers who are extremely welcoming and are willing to help other budding developers.

You also get sponsored while you work on writing code for such organisations which I believe is a great plus point too. All of this makes contributing to Open Source via GSoC an amazing learning experience which I believe every developer should get to enjoy.

### Thanks for reading!

That's it for now! If you've decided to apply for GSoC, good luck. I hope you enjoy the process, learn a lot, and have fun contributing to open source.


