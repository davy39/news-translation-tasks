---
title: 'My first week of open source: how I got involved, and what I’ve learned'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T21:27:10.000Z'
originalURL: https://freecodecamp.org/news/the-path-of-my-first-week-of-open-source-contributions-87823aaeb872
coverImage: https://cdn-media-1.freecodecamp.org/images/0*oGS2HCMbtG_IFY3K.
tags:
- name: Life lessons
  slug: life-lessons
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Storybook
  slug: storybook
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Chak Shun Yu

  When I started to write this post, I had finished my first serious week of contributing
  to open source. I mainly contributed to the project Storybook. This post will describe
  the contributions and interactions that took place this wee...'
---

By Chak Shun Yu

When I started to write this post, I had finished my first serious week of contributing to open source. I mainly contributed to the project [Storybook](https://storybook.js.org/). This post will describe the contributions and interactions that took place this week. It will also focus on the path that led up to this week.

I want to talk about the change in mindset and motivation that (finally) got me started. I will show you what I did to get to my first contribution, and I will share what I learned from this week and my experience of everything as a whole.

While I’m aware that one week has not made me an open source expert, the stories I describe will be from my own subjective perspective. Developers trying to get into open source, like me before this week, might find some value in reading the story of someone in very similar shoes.

In this post, I won’t go over the basics about getting into open source. I will not cover how to choose a project to contribute to. Nor will I cover why, how, and what you should contribute to the project. [Open Source Guides](https://opensource.guide/how-to-contribute/) covers all these topics very well. You should definitely check it out if you’re looking for advice regarding those topics.

![Image](https://cdn-media-1.freecodecamp.org/images/KONcC2tWywcLmOrtduE4z7uJX6bD5XWC2kda)
_“A highway down a countryside with a red wheat field” by [Unsplash](https://unsplash.com/@alice_hampson?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Alice Hampson</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Motivation and Mindset

While this week has been pretty awesome and enjoyable, the journey up until this point has most definitely not been a walk on a flowery path.

Let me provide you with some context about me. I’m currently a second year MSc student in Computer Science at the Delft University of Technology. I would describe myself as a (below) average developer compared to my peers. I didn’t really start programming before I got into my Bachelors. I never found the motivation to do so outside of courses.

It has been over a year now since I first heard about the mysterious phenomenon of open-source programming from a colleague. This colleague also described all the benefits, both for personal development and for my career.

My inner developer kicked in and was like _“Oh that’s super awesome, I should do that so I can learn a lot and increase my chances for a job in the future!”_, but then my inner student kicked in and was like _“Why should I burden myself with more_ **_obligations_** _than I already have (from university) though?”_.

Fast forward a year. While I’m already improving my development skills in alternative ways, I still hadn’t touched open source in any voluntary or serious way. I expect to graduate during the Autumn of this year. Then I will get into the job market which is nothing out of the ordinary.

In these past months, however, I’ve started to take my future quite seriously. I am already exploring opportunities through career fairs, in-house days, and staying in touch with companies.

While this is great and all, there’s still one thing that I lack: **experience.** Especially in a established environment (like a company). While a part-time job on the side is _an_ option, the main thing on my mind right now is to focus on my MSc thesis and graduate. Everything else is just kinda of on the side. So, in the end, I don’t really consider a part-time job to be an option _for me_.

During these months, I’ve looked for alternative opportunities to gain experience. I have looked into hobby projects and a small programming side job at the university. Those still aren’t quite what I’m looking for.

But one day, the thought came across my mind that I could gain the experience that I was looking for through open-source contributions. Provided that I chose the projects carefully to meet my needs. Because, in the end, open-source projects are very similar to companies. The only difference is that the employees are fighting to get work, rather than to avoid it. ?

After this week, I’ve noticed how my mindset and motivation has changed compared to last year. I credit this change as the reason that I could get into open source now. The lack of motivation is the reason that I failed before.

Before, I only thought about it as a way to improve my résumé. This relates to how I initially saw it as an obligation. In the long run, that would never keep me motivated. Even worse, it would never motivate me enough to begin in the first place, which is exactly what was the case during this year.

Now, on one hand I see it as an alternative way to obtain experience in a company-like environment. But more than that, I want to enhance and develop my skills, both in programming and communication.

And that’s the main thing that keeps me going right now. I can actually motivate myself to spend time doing open-source programming. Not because then I can apply for that particular job offer. Not because I can then put it on my résumé…but because I actually **want** to become a better developer myself. It’s all for myself. That is a motivation that will most definitely not suddenly fade out or not be strong enough.

The best practical example of this in practice is the context of my first contribution. On a Thursday (the 19th of April) I was basically working at my uni job the entire day. It was a pretty early morning for my standards, starting at 10:00 which means waking up at 8:00 for me. And we didn’t finish until 18:30, which made it a pretty long day. After coming back home and finishing dinner, it was basically already 20:00. Any other day, I would’ve either fallen asleep on the couch or taken it chill the rest of the evening.

That evening, however, a [certain Github issue](https://github.com/storybooks/storybook/issues/3384#issuecomment-382812208) reached my mailbox. (I will discuss later why and how it got there ?). It caught my attention because it felt like something I could solve. I basically rushed to my laptop, and left a message on the issue that I would be willing to give it a try.

I spent a few hours working on it, before eventually hitting my friend up to play some games as usual. Even when I think back about it now, I’m still extremely surprised that I was **willing** to do more programming after such a long day for my standards. Again, I credit all this to the above stated change in mindset and motivation.

#### My Choice of Projects

As I said before, the [Open Source Guides](https://opensource.guide/how-to-contribute/) already covers a lot of the initial steps for getting into Open Source programming. They even include how to find a project to contribute to. Therefore, this section will be dedicated to my choices in projects, my preferences, and how it affected my choices.

At the moment, my main interest and the field that I’m focusing on improving the most in is web development. Especially React — it’s the library that I’ve come to love and feel most comfortable with. So naturally, I wanted to find projects that were related to web development. For me, the project being written (partially) in JavaScript was a must, while involving or being related to React was a plus.

On top of that, I wanted the project to be a slightly- to decently-established project in the community. I wanted to mimic the experience of working in a company-like environment. And being able to say that you worked on _-insert widely used library or project in the community-_ definitely sounds cool in any conversation or interview ?.

The full list of projects that I looked into consisted of projects found through [searching “React” on Github](https://github.com/search?o=desc&q=react&s=stars&type=Repositories) and ones that I knew or had heard of: [React](https://github.com/facebook/react), [Redux](https://github.com/reactjs/react-redux), [MobX](https://github.com/mobxjs/mobx), [React-Router](https://github.com/ReactTraining/react-router), [Next.js](https://github.com/zeit/next.js/), [styled-components](https://github.com/styled-components/styled-components), [Storybook](https://github.com/storybooks/storybook), [Spectrum](https://github.com/withspectrum/spectrum), and more…

In the end, I stuck to styled-components, Storybook, and Spectrum. Mainly because the other projects felt relatively abstract and more difficult to understand. These projects were very new-contributor friendly. Plus they are still widely used in the community.

Over that one week, and between these 3 projects, all but one of my contributions were towards Storybook. My first contribution was towards Storybook, and I really liked the flow of it. At that time there happened to be more issues that I felt I was capable of tackling, so I continued with it!

#### Making My First Contribution

So I’ve already talked about the context of my first contribution. I haven’t talked about the technical details of the [Pull Request (PR)](https://help.github.com/articles/about-pull-requests/), however. Or how I got to the PR in the first place, which will be the focus of this section.

The best thing that I did to increase my knowledge and understanding of all the projects was [watching all the repositories](https://help.github.com/articles/watching-and-unwatching-repositories/#watching-a-single-repository) that I was interested in. This is also the biggest recommendation that I can give to people that are new, like I am, to any open-source project. This spammed my mailbox with any activity in the projects, be it the creation of an issue or PR, or any comment in it.

Then, whenever I had some free time on my hands, I would go through all the emails. I would process the ones that I could understand. Someone made a PR and the title doesn’t sound like complete magic? Let me take a look at what they did and how. Oh, there’s a active discussion going on in this issue and it doesn’t sound overwhelming? Let’s follow that conversation as well!

The pattern here is that I tried to extract as much information and knowledge about the project by exposing myself to what others were doing. Watching the repository guaranteed that any information I was consuming would be recent.

The current problem or implementation that I was learning about was useful for the project at that point. Of course, there were scenarios where, no matter how hard I tried, I just couldn’t see myself participating meaningfully. Although this can feel very demotivating, it’s also completely normal if you think about it carefully.

In the beginning, I was archiving a lot of emails, because I just lacked the knowledge to understand the issue. Instead, I focused on the ones I could and the ones that I wasn’t sure about whether I could. No matter what the result was, I would just try to go through them and understand.

If I couldn’t, then I would know where my limitations were and still learned about the project in some way or another. If I could, then I extended my knowledge on the project as well, and I could potentially contribute to solving the issue. Of course, especially if the project was very active, it was very hard to keep up with all the emails. I just tried as much as I could afford, hoping it would help me in the long run — which it did!

At some point, someone opened an issue. The issue described some problems with the Storybook CLI during the installation process. It turned out that Storybook prefers to use yarn. However, not everybody uses yarn, and npm is still significantly used in the field.

To cover for these cases, the CLI would run the yarn — version command to check whether yarn was installed. If so, it would use it as the package manger of choice to install dependencies. The issue arose, however, when developers had both package managers installed, but mainly used npm. Storybook would then use the old version of yarn. This resulted in the issues reported by the current user.

This sounded like something that I understood and felt capable of fixing! So what did I do then? I started of with politely asking whether it was okay for me to tackle this issue.

There are several reasons that I explicitly asked this, rather than just doing it.

1. It signals than _somebody_ is working on the issue, which is great for the maintainers.
2. It clarifies that _you_ are working on it and that you claimed the issue. This is especially useful in highly active projects.
3. It makes sure that you’re not taking someone else’s issue. For various reasons, someone could be already working on it, and I personally hate taking away someone’s issue.
4. It will make sure that you’re not going to waste your time and effort on something that’s outdated, unnecessary, unwanted, or already done. If any of these are true, a maintainer will most likely let you know.
5. It never hurts to be polite and communicate ?.

After receiving a green light from a maintainer and the user that reported the issue, I went and applied a fix described in the issue. The fix itself wasn’t particularly mind blowing. Instead of checking for an installed version of yarn, it would check for the presence of a yarn.lock file instead. After some discussion on making the check slightly more elaborate and processing that feedback, they approved my changes. My PR was merged! ?

Did I feel super accomplished after this? You would expect so, but I actually felt way less excited about it than expected. Don’t get me wrong, it **did** feel satisfying to have my changes merged. It just didn’t feel like it was a super complex problem that I solved.

The real feeling of accomplishment and excitement actually came way later at unexpected moments. At multiple points in time, people would report certain problems that they had with Storybook. For me, those seemed completely unrelated to my changes. However, in at least 4 different issues, my fix was mentioned by a maintainer because it helped solve the issue at hand.

WHAT!? I ACTUALLY HELPED PEOPLE!? ? My small fix that felt like it was nothing actually helped people with their problems. The feeling of accomplishment and excitement that I had at that moment was indescribable. It exceeded any feeling that I could’ve had from solving a super complex problem of some kind. I still hold it very dear.

#### The Rest of the Week

After that moment, I felt even more motivation to keep working on issues and stuff in the project. As long as it was something that could help the users of Storybook, I was more than happy to have a go at it.

I paid more and more attention to the different activities in the repository. Whenever I found something I could do, I would politely ask whether it was okay for me to solve, and then make an attempt at solving it.

In my first week, I had opened 4 PR’s to Storybook, and all of them were accepted and merged! If you’re interested in the details on those PR’s, go ahead and [check out the GitHub tracker](https://github.com/storybooks/storybook/issues?q=author%3AKeraito+sort%3Acreated-asc).

I also want to go back briefly and further discuss the point that I made regarding watching the repositories and following all the activities in them. You might wonder whether it will pay off or be worth it for the required effort and time (which I agree is significant).

For me, the answer was a decisive yes, and this is why. My second PR had to do with a section of the codebase that I didn’t know and had never yet looked at. This, of course, was true for every part of the project as I was a new contributor. While I could find my way through the CLI code, this time it involved the actual Storybook application, which for me was on another level.

The main reason I was able to address the problem and work with the code anyway was because I went through the changes of someone else’s PR that touched upon that same part of the codebase. The style of my changes, if you compare it to the changes of that PR, were therefore very similar. But in the end, I still got the job done, and that’s all that mattered for me (and the project)!

But if I never took the time and effort to go through as much activity from the project as I could, including the work of others, I’m pretty sure I would’ve never been able to solve the issue (so quickly). So yes, if you’re serious about wanting to contribute to the project, then it’s definitely worth your time and effort.

#### What I Learned

To be honest, I haven’t really (yet) learned as much or improved as much in my programming this week as I expected. But don’t get me wrong — I’ve definitely learned some technical things, especially regarding how a significant project looks in practice.

Rather, I’ve learned a lot about working together with others. I’ve learned about communicating my thoughts and changes to the maintainers that had to review my changes. I’ve learned how to phrase my thoughts to get my ideas across.

In a way, this was the experience that I was looking for. Looking back onto this week, it has been super helpful. I’ve learned a lot, finally did something that I wanted to do for a long time, and, most important of all, **I had fun!**

#### Going Forward

Going forward after this week and beyond, I will just do as I’ve done during this first week: keep an eye out on issues and conversations, and help wherever and whenever I can.

As time progresses, I hope be able to also contribute to more complex problems. Ideally, it would be super awesome for me to be able to contribute to something larger, like an additional feature or add-on to Storybook. Nonetheless, I enjoy what I’m doing, and will definitely stick around and continuing doing so.

As a matter of fact, I’ve stuck around so long that at the time that I’m finishing this post (~5 weeks after I started writing this) I was invited by the owner of Storybook to join the GitHub organization! ? I’m super grateful for this opportunity. I will definitely to try my best to make myself more and more useful to the project! ?

#### TLDR:

* Think about what you want to accomplish with open source. If it’s not a long-term motivation, it will be hard to 1) get started and 2) keep going.
* Watch all the activity from repositories that you’re interested in and try to spend time going through them. It will considerably increase your knowledge on the project and help you contribute.
* Stay polite and have fun! ??

Thank you for reading. If you enjoyed my story, consider clapping for it a bit, sharing it with other people, or following me either here or on [Twitter](https://twitter.com/keraito) (or both ?). I will try my best to deliver similar content in the future!

If you have any feedback, either writing or content-wise, feel free to contact me in any of the described ways. I’m open to any feedback that will improve the quality and usefulness of my potential future content!

> Special thanks to [Maurício Aniche](https://www.freecodecamp.org/news/the-path-of-my-first-week-of-open-source-contributions-87823aaeb872/undefined) and [Martijn Steenbergen](https://twitter.com/mjwsteenbergen) for helping me out with this post through proofreading and feedback! Also to [Norbert de Langen](https://www.freecodecamp.org/news/the-path-of-my-first-week-of-open-source-contributions-87823aaeb872/undefined) (Storybook’s maintainer), for inviting me to the GitHub org and trying his best to involve me in the project!

