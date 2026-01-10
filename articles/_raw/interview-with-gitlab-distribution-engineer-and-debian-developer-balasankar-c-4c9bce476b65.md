---
title: Interview with Gitlab Distribution Engineer and Debian Developer Balasankar
  C
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T15:07:46.000Z'
originalURL: https://freecodecamp.org/news/interview-with-gitlab-distribution-engineer-and-debian-developer-balasankar-c-4c9bce476b65
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pRc4d0i80Mipj_THsM4J0Q.jpeg
tags:
- name: jobs
  slug: jobs
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kurian Benoy

  This is another chapter of the series where we interview amazing people who work
  in the Open source World.


  Balasankar C

  Balasankar (Balu) C is an active Free and Open Source (FOSS) contributor. He has
  been contributing to various FOS...'
---

By Kurian Benoy

This is another chapter of the series where we interview amazing people who work in the Open source World.

![Image](https://cdn-media-1.freecodecamp.org/images/RlZqjT0QqJ9ZxQGUEfS-ZxW9tDovly4L3jYF)
_Balasankar C_

**Balasankar (Balu) C** is an active Free and Open Source (FOSS) contributor. He has been contributing to various FOSS organisations like [Debian](https://wiki.debian.org/Balasankar%20C), [Gnome](https://www.gnome.org/), [Firefox](https://mozillians.org/en-US/u/balasankarc/), [Swathanthra Malayalam Computing](https://smc.org.in/), Diaspora, and [WikiGrandhashala](https://ml.wikisource.org/wiki/%E0%B4%AA%E0%B5%8D%E0%B4%B0%E0%B4%A7%E0%B4%BE%E0%B4%A8_%E0%B4%A4%E0%B4%BE%E0%B5%BE) for the past 9 years. He is involved in contributions ranging from language computing to software packaging and software development. He is a Debian Developer, Gnome foundation member and Mozillian. Apart from his day job at Gitlab, he contributes most of his time to open source projects.

#### About the Series:

I have been contributing to many Open source projects in organisations like CloudCV and FOSSASIA. It has been a wonderful learning experience for me personally and I’ve met a lot of amazing mentors.

The main aim of this interview series is to motivate more people to contribute to FOSS projects after hearing these stories. I hope you might see some patterns from these amazing people that get you motivated to contribute to Open source projects. As Mario Behling, co-founder FOSSASIA says: just contribute, and opportunities will fly towards you.

So without further adieu, here’s the transcript of the interview.

**Kurian Benoy:** Hello Balu, Thank you for taking the time to do this interview after your amazing talk at Facebook Developer Circle, Kochi.

**Balasankar C:** No problem. It’s a pleasure to be part of this series.

**Kurian Benoy:** What’s the difference between open source and free-software? Some say it’s just politics and that beginners shouldn’t care about it. What do you feel?

**Balasankar C:** Consider a yellow pencil being placed here. You may say it’s a sharp pencil, considering its functionality. Nithin may say it’s a yellow pencil, considering its appearance. When you think about open source software and free software, this is exactly the difference. Both free software and open source software are based on the four freedoms.

Free software philosophy gives importance to freedom. Open source considers it as a development methodology, where multiple people share and look at the code. This way, bugs can easily be fixed. As Linus Torvalds quotes: “With enough eyeballs, all the bugs are shallow”.

Open source methodology says, by providing these freedoms, the product itself gets better. Open source gives emphasis on collaborative development, and when multiple people with differing expertise and diversity look at the code, it forms a great product at the end.

![Image](https://cdn-media-1.freecodecamp.org/images/EwwwJc4zHsntE2dpS1d3fyZiBdPi8fu3b6hw)
_Four freedoms [source:Slideshare]_

Free software considers itself as an extension of the society. If you look at how the world has progressed, you can see that it has been through sharing of natural resources, knowledge, techniques, etc.

When you are coding, more than often you are extending upon, or basing your work on existing knowledge. Access to this knowledge was available to you because its original creators didn’t put barriers in your way. So, ethically, you locking down your creation, thus preventing others from making better stuff out of it, is simply wrong.

Imagine, if you bought a bicycle and the company tells you that you can’t pedal your bicycle backwards or that you can’t change the color of your cycle, it seems illogical. Because you have a sense of ownership over the bicycle and hence know that you have the freedom to work on your cycle without restrictions from the company. Similarly, in the case of Software, it’s your right to understand how it works. So saying that you can’t modify a software you have bought is illogical.

To answer your question, no, beginners shouldn’t be concerned about this. I respect Stallman and understand his vision. Open source didn’t make any mistakes. His politics and philosophy about working is necessary and our society is actually built on a sharing culture. Our end goal is still a free software world and we should care about the philosophy. Yet we need to take baby steps and work towards this goal. Such a compromise made to work is open source software. As a beginner, you needn’t be concerned about terms like Free Software, FOSS nor FLOSS. As a beginner, understand that freedom matters and all this is based on the four freedoms.

In the initial years of my free software journey, I was an adamant Free Software advocate, and was very vocal about the term Open Source. But, my views have changed from the experience I gained during the journey, and I have different opinions about the entire situation.

So, a beginner need not be concerned about getting it right from the beginning itself. You gain this knowledge as you talk with others and work on projects. What is important is that you contribute to projects.

**Kurian Benoy:** What are best practices to start contributing to an Open source organization?

**Balasankar C:** The way you contribute to various open-source projects depends on the type of project and also style of how an Organization functions. What I am going to say is a general workflow on how to contribute:

* Read the contributors’ guide and the README of the projects.
* Check the issue list of the project.
* Read Code styles and the code guidelines to be followed. For example, please don’t leave your code un-indented. ?
* Read the source code of the project, which can often be found in GitLab or GitHub.
* Attempt to solve the issue. If you can’t, try joining IRC/Gitter rooms related to the project, or any other developer forums. Never hesitate to ask questions.
* Open a pull request.
* If you find a problem, go on and send an e-mail or interact on forums like Gitter. Start a good conversation with a contributor.
* Keep contributing to the project. Contributions can be anything like fixing bugs, documentation, localisation of a particular service, or code contributions.

**Kurian Benoy:** What do you think about Open-source incentives like Hacktoberfest and others? Beyond getting T-shirt’s what should people focus on with these programs? Will merely a Hacktoberfest make an Open source contributor?

**Balasankar C:** The whole idea of Hacktoberfest, according to me, is good and getting a T-shirt is a great motivation to many. Getting a T-shirt is never a problem. After all, companies like to hand you freebies. What matters, is what you have done after the Hacktoberfest. Have you followed up on your pending PRs which are in the feedback phase? Are you still continuing to contribute to Open source? These are the real questions. If the only thing you’ve got out of the Hacktoberfest was a T-shirt, then your T-Shirt becomes pointless.

Essentially, if you didn’t find any passion contributing to FOSS projects, any idea of what the project is about, you essentially wasted your time (the project maintainers at least got a contribution/fix from you. ?

The important thing, according to me, is how working on the project inspired you. If it got you curious about fixing the problem you were working on, or got you interested in learning more about the project, it was time well spent. One regular example where I don’t see this happen is Google Summer of Code. Most of the time, participants stop contributing to the project after GSoC, and this often gets raised as a concern - “Are people in GSoC only for money?”

So, getting a T-Shirt is fun. It is not a taboo. But, it becomes worthy if it got you on a path of contribution.

Other than getting swag, one reason people do this is to claim themselves as “open source contributors”. What is funny is, most of them don’t realize that it doesn’t take that much to do a proper, continuous contribution to FOSS projects. Basic English learning, and a curiosity to learn and you can be a very successful contributor, and will not have to depend on any gimmicks.

If your thought process is “People in industry are excited to hire open source people, so having all these feathers on my hat would be awesome”, there is a slight problem there. Yes, FOSS contributors have a good opportunity in the industry. But, when it comes to hiring, it is not that difficult to check if you are a proper contributor or not - whether you are a good fit for the company or not. And companies often do that check. ?

**Kurian Benoy:** What’s the difference between [GitHub](https://github.com/) and [GitLab](https://about.gitlab.com/). Why should we use GitLab?

**Balasankar C:** I will start off by saying good things about GitHub. GitHub has been here for about 12 years and many of the major FOSS projects use GitHub for code hosting. GitHub popularized collaborative development and has helped open source methodology very much.

However, I find GitLab to be superior, from both philosophical and practical points of view. Philosophically, even though GitHub has contributed quite a lot to FOSS, their core code base is still proprietary. Whereas, GitLab has most of its code base released under MIT license, and even the proprietary parts of the code base is “source available” (meaning you can read the code and even clone the repo. You just can’t violate the license).

![Image](https://cdn-media-1.freecodecamp.org/images/lupAIH2SAYOtXNR7f5wR7cOQzOfBuv3NfJKZ)

From the practical point of view, as a user, I find GitLab to have a much larger collection of features compared to GitHub. Features like Continuous Integration and Continuous Deployment (CI/CD) support for all static site generators in GitLab Pages etc are features that will be useful to many users.

I consider GitHub mainly as a “code sharing platform with review ability”, whereas GitLab covers the entire DevOps lifecycle.

Now, diving a bit into the features of GitLab, I mentioned above it covers the entire DevOps lifecycle. It means, from having an idea and discussing it with your peers, to implementing that code in an IDE to deploying the code to different environments and monitoring those deployments, GitLab provides you tools to do all of this - in the same interface. So, unlike other solutions where you have to jump between multiple services to perform all this, you can just use GitLab.

I mentioned GitLab has a proprietary part too. This mostly involves features that make sense to bigger companies (say, with more that 250 employees) - features like Epics, or Roadmaps, or multiple group issue boards, etc.

Most of the code that a regular user or even a SME needs is available as Free Software. For just this reason, I consider GitLab to have a more friendly approach and commitment towards Free Software.

**Kurian Benoy:** We absolutely love [Debian](https://www.debian.org/)! What do you think is the future of Debian?

**Balasankar C:** The future of Debian depends on the future of Linux. If the question is about the Debian packages (with Snaps and Flatpaks and Docker containers here), I don’t think any drastic change will happen anytime soon. We are talking about a huge repository with about 70,000 packages.

How the technical stack around Debian (packages, build tools, workflows etc.) changes will depend on its derivatives also, mainly Ubuntu. Whatever problems I have with Ubuntu, there is no denying the fact that Ubuntu stands top as the most used GNU/Linux distribution. So, how that company drives the project forwards will have a serious impact on both Debian and other derivative projects.

In my opinion, just how RedHat made “Enterprise Linux” a thing, Ubuntu introduced GNU/Linux to home users. Whether it be by their marketing skills, or design decisions, they made a serious impact on the popularity of GNU/Linux.

Personally, I think Debian as an OS badly needs some marketing. I don’t mean we will die without that, but I think it will surely help. I haven’t seen Debian doing any sort of proper publicity efforts, or attempts to make it more popular among home users. It is a huge hit among system administrators, because of its legendary stability, so that position in the market is secure. But if we were to expand the horizons, we will have to think differently.

**Kurian Benoy:** What do you think about Open source Licenses like MIT and GPLv3?

**Balasankar C:** This relates to something I mentioned earlier. I consider a society where all software is Free to be a glorious end goal - something, as FOSS evangelists, we all should be working for and strive to achieve. And GPL is the best option in such a society.

However, to reach that end goal, we have to travel quite a bit, and try to make all sectors understand the cause. This definitely includes industry. It is not a surprise that GPL is not a favorite of industry, because it automatically makes any associated code to be released under GPL (except the cases under mere aggregation, which lets you embed a binary of a GPL licensed software with another software without releasing the whole under GPL license). Industry, by its very nature, has a for-profit mindset, and are wary of anything that can affect that profit. So, “releasing everything you make so that others can modify it and distribute it themselves” is a bit scary for them. Whether they are right or wrong is another discussion, but the fact is that such an issue exists.

Permissive licenses, in my opinion, cater to this issue. They, while ensuring the immediate user gets all four freedoms, don’t put further restrictions on the developer. I consider them to be a necessary compromise in the current socio-economic situation. The main advantage I see is that, it resulted in companies using FOSS projects and releasing most of their libraries under these licenses - thus making them Free Software. So, in totality, it resulted in more free software in the world. Yes, it is not ideal, but it is unavoidable.

(Personally, I recently started licensing all my personal code under both a copyleft and MIT license. I tell my users that I prefer if they used the copyleft license and contributed to the cause, but I leave the decision to the users.)

**Kurian Benoy:** What’s difference between FOSS Enthusiasts and ordinary people who graduate from college?

**Balasankar C:** This is a question I usually get - as a student why should I contribute to FOSS. From my personal experience, I can guarantee you something. While attending a campus placement interview, if you are a FOSS contributor, you are by default above all of your peers. It is because being a FOSS contributor gives you some specific, and unique skills, that all employers want.

* **_A mindset to fix problems_** - You contributed to a FOSS project not because someone forced you or not because you were promised anything. You did it because you were curious about a problem, or an issue, and had a mentality to sit down, spend some time and fix the problem. It doesn’t matter if the fix was just a spelling mistake or a 100 line code implementing a major feature. What matters is that there was a problem and you put in the effort to solve that problem, mainly because you had a passion to do so. Employers love those with passion, because it is that passion that drives innovation and brings in efficiency.
* **_Coding Etiquette_** _-_ While contributing to a FOSS project, often the people you interact with are people who have been doing this for quite some time. And that experience will be reflected in their feedback to you, and eventually on the work you do. For example, a university training its students on proper coding practices or giving coding guidelines is a rare sight in India. But, industry expects programmers to follow standard guidelines, proper styles, etc. They often bridge this gap by providing a training course to new hires. But, if you are a FOSS contributor, chances that you already know about all this is pretty high, which makes the job of an employer easier.
* **_Teamwork and tools_** _-_ Just like coding standards, something else you get familiar while contributing to a FOSS project is teamwork. Most of the FOSS projects involve contributors from all over the world, and it is with this diverse workforce you are regularly communicating and interacting. There is no better opportunity to understand how to work well with a team.

**Kurian Benoy:** Thank you so much for doing this interview.

![Image](https://cdn-media-1.freecodecamp.org/images/vp42eRhSpUgXWEiyGo1nxr5z9Ec2MaIcqvO4)
_Me interviewing Balasankar C (source: Nikhil Vasanth)_

**Thank you for exploring this interview along with me.** If you found it resourceful, appreciation in the **form of claps, shares would be really appreciated!**

Also your feedback helps [me](https://twitter.com/kurianbenoy2) to better improve this series in the future, so do comment about the same if any. Until the next Open Source Hero we interview, goodbye and keep on contributing to Open source!

