---
title: How code reviews work at Microsoft
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-27T08:00:57.000Z'
originalURL: https://freecodecamp.org/news/how-code-reviews-work-at-microsoft-4ebdea0cd0c0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*GWGY5OFKBHznk598
tags:
- name: code review
  slug: code-review
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Michaela Greiler

  Have you ever wondered how one of the largest software companies world wide ensures
  high quality code through code reviewing?

  So did I. That’s why together with my colleagues at Microsoft, we investigated how
  code reviews are done...'
---

By Michaela Greiler

Have you ever wondered how one of the largest software companies world wide ensures high quality code through code reviewing?

So did I. That’s why together with [my colleagues](https://www.michaelagreiler.com/category/code-reviews/#ms-peers) at Microsoft, we investigated how code reviews are done at our company. Is it a common practice? Are developers required to do code reviews? And which tools do they use?

Let’s find out in this post, which is part of a [**larger blog post series about code reviewing**](https://www.michaelagreiler.com/code-review-blog-post-series/).

To begin with, let me give you some key information about Microsoft. [Microsoft has around 140,000 employees](https://news.microsoft.com/facts-about-microsoft/#EmploymentInfo). Approximately 44% of them, that means over 60,000 employees, are engineers. Several products such as Office, Visual Studio or Windows are developed by thousands of engineers that work on the same code base simultaneously.

I say all this to give you some context and perspective of what it means to coordinate and manage the software development process. As you can imagine, it is a non trivial task to ensure code developed by different sub teams actually works perfectly together. And code reviews play a big role at Microsoft to allow smooth collaboration at such a large scale.

### Code reviews at Microsoft are an integral part of the development process

One of the important facts when it comes to code reviews at Microsoft is that it is a highly adopted engineering practice. Thousands of engineers perceive it as a great best practice. And most high-performing teams spend a lot of time doing code reviews.

[At Microsoft, code reviewing is a highly adopted engineering practice and perceived as a great best practice. Click To Tweet](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/&text=%20At%20Microsoft%2C%20code%20reviewing%20is%20an%20highly%20adopted%20engineering%20practice%20and%20perceived%20as%20a%20great%20best%20practice.%20%20&via=mgreiler&related=mgreiler).

### Investigating code reviews at Microsoft

Because code reviews play such an important role in the Microsoft development process, it was an ideal target for us to dig deeper and really understand the benefits and drawbacks of this practice. [In a large scale study on code reviews at Microsoft,](https://www.michaelagreiler.com/wp-content/uploads/2019/03/Code-Reviewing-in-the-Trenches-Understanding-Challenges-Best-Practices-and-Tool-Needs.pdf) we interviewed, observed and surveyed more than 900 developers about their code review practices.

Our aim was to understand how exactly code reviews are done at Microsoft, which challenges developers face while doing code reviews, and to distill which best practices they develop to overcome those challenges.

### What can you learn from code review practices at Microsoft?

Most of the lessons learned are as valuable to smaller teams and organizations as they are for large teams and large organizations. In case your team does not do code reviews yet, I distilled our findings in a way that shows you the benefits of the practice. I also explain how the code review life cycle looks like so you can incorporate that practice in your own development process.

If your team already does code reviews, you can compare your practice with the code review practice at Microsoft. Does your code review lifecycle look different? In later posts, you learn from the challenges that arise doing code reviews and the best practices. With this information you can set out to see if your team already implements all the best practices I present and overcome challenges. But, let’s get started:

### How often do Microsoft engineers perform code reviews?

In this study, 36% of the developers said they perform code reviews multiple times a day. Another 39% of the developers said they do code reviews at least once per day. 12% do code reviews multiple times a week, and only 13% said they did not do a code review in the past week.

![Image](https://cdn-media-1.freecodecamp.org/images/K3jMFIgEEHEn8kADlr7CUZnBrg-4rFnFYtIj)

This means that developers at Microsoft spend a significant amount of their time on code reviews. So it is important to make sure that this time spent is worthwhile. But, which benefits does code reviewing provide?

### Which benefits does code reviewing provide?

The most important reasons developers mentioned as benefits of code reviews are to improve the code quality and to find defects in the code. Another important benefit of code reviews is knowledge transfer.

Knowledge transfer means that team members that review each others code, become familiar with a larger part of the code base. But, it also means that best practices are developed within the team. Another advantage is that new team members and junior developers can learn and improve their coding skills while reviewing or getting feedback.

If developers discuss alternative solutions during code reviews, it not only improves the code base, but has also a learning effect for all involved. Learning, mentoring and self-improvement are therefore all reasons code reviewing is perceived as such a beneficial practice at Microsoft.

![Image](https://cdn-media-1.freecodecamp.org/images/J4xPSMk926cmcD0tTDWcePiZ4aGfxMDDUQfn)

Developers do code reviews to improve the code, to find defects, but mostly to increase the knowledge transfer amongst team members and for the learning effects. [Click To Tweet](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/&text=Developers%20do%20code%20reviews%20to%20improve%20the%20code%2C%20to%20find%20defects%2C%20but%20mostly%20to%20increase%20the%20knowledge%20transfer%20amongst%20team%20members%20and%20for%20the%20learning%20effects.&via=mgreiler&related=mgreiler).

### But how does a developer typically do code reviews?

Code reviews can be performed in many ways. Sometimes, it is as informal as one developer walking over to another developer’s desk to look at some code together. Other times, teams review code together in groups. But the most likely scenario you will encounter for code reviews at Microsoft is that code reviews are done with the help of tools.

#### Code reviews at Microsoft are most often done via an internal tool

There is a wide variety of code review tools available, and at Microsoft teams are free to choose their tooling. In 2016, 89% of the developers indicate to use the CodeFlow code review tool. I will explain more about this [code review tool at Microsoft](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/#ms-tool) later. Since then, and with the rise of Git, the tooling landscape has changed. I’ll add updated numbers as soon as they become available. But, let us consider a typical review situation:

Let’s imagine a developer at Microsoft, and let us call her Rose. Rose just finished a part of a feature and now wants feedback from her peers.

#### How does Rose start a code review at Microsoft?

Well, as said, Rose is ready to get some feedback. Therefore she first prepares the code for review. This step includes that she opens the code review tool, that allows her to preview the code change. The code review tool performs some diffing tasks that help Rose to see exactly which changes she has done.

After carefully reviewing those changes, she prepares a small note that tells the reviewers what she did and why she did that. This note helps the reviewers to understand the purpose of the code change and its motivation. Now the code is ready to be sent to the reviewers.

#### How does Rose select the right code reviewers?

Many experienced developers know who should be on the code review. Nevertheless, for people new on the team, or for new areas of work the selection can be a bit more tricky. If Rose does not know whom she should add, she would either look at the team policies or ask her colleagues. She can also use a recommendation feature of the code review tool that helps select reviewers based on experience and knowledge with the code base.

#### Who are relevant reviewers?

Rose selects reviewers that she thinks can contribute their knowledge to this piece of code. The reviewers are often other developers, but can also include other stakeholders, such as dev-ops engineers, UI experts, or also managers. Some reviewers are selected for their expertise, others are selected in order to stay informed about a coming change.

![Image](https://cdn-media-1.freecodecamp.org/images/Siud62YVmYXQ1xe6xFrPMeFcZR-nkz7zrh26)

#### Rose requests feedback from her peers

Once everybody is selected, Rose sends out the code review (by pressing the send button ?). The code review tool sends notification automatically to inform everybody that a code review has been created. Notifications are sent to all reviewers. But, often additional parties, such as managers or product managers of other teams, are also added to the notification list, and are automatically informed for each review. Those notifications allow them to stay in the loop. They are not required to perform the review.

#### Receiving feedback is an iterative process

Once Rose’s colleagues have time, they will look at the code review. Each reviewer can annotate the code and add comments. Once finished commenting, the reviewer sends the annotated code back to Rose. Rose can now work on the comments and prepare a new improved version of the code.

Reviewers normally look for things like: does the code look bug free? Is there an architectural problem? Are there minor issues such as missing comments, spelling mistakes? Not all comments are equally valuable. But, there are [several best practices to boost the value of code review comments.](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/boosting-code-reviews-useful-comments)

#### Rose prepares a new improved version of the code

Rose works on the feedback by fixing and addressing the suggestions. If Rose sees that there are some misconceptions or other contentious issues, she might walk over to a colleague to discuss this in person. That’s sometimes easier and more personal than through the tooling.

Anyway, once she finished working on all the feedback, she sends a new version of the code to the reviewers. That new improved version is called a revision.

If needed, she will receive further feedback. Whether or not this cycle continues for a few times depends on the type of change and its quality. For simple and small code changes, often only one code review revision is needed. For other more complex changes or changes in problematic code, several iterations might be necessary.

It is totally normal, and partly desirable, that this code review feedback cycle sparks some discussions between the author and the code reviewers.

#### All reviewers approve and Rose checks-in the code

After this review cycle, reviewers mark the code as okay, and Rose can finally check-in the code into the common code base.

Some teams have policies that allow the developer to check-in the code before an actual review is completed. This is normally restricted to small and trivial changes, in order to allow asynchronous reviews and to speed-up development.

All steps I describe are part of a typical code review life cycle at Microsoft and are performed by all teams. Depending on the team’s policies, teams are more strict or rigorous for each of the steps.

### Not all teams are the same

As you can imagine, not all 60,000 engineers, and not all of the thousands of teams do the same. Some teams at Microsoft have additional steps or tools they require during the code review life cycle. I want to give you a short overview of some additional steps that teams add to the code review process.

### Code reviews including test results

The least what you want is to waste time by reviewing “automatic detectable” buggy code. I mean, if you could run automated tests and realize that the code does not work as expected, then, that’s what you should do: Run the tests before the review.

That’s why some teams require test results to be submitted with each code review. This way nobody can forget about running the tests. And it assures that the tests have actually run and passed for the given code change.

Other teams went even a step further and configured the code review tool in such a way that for each code review a developer submits, a build is triggered. That build contains that exact change, and also starts a series of automated tests. The results of this build and these tests are attached to the code review. Configuring it this way, ensures that the code changes have been tested with the latest code changes from the common code base.

### Code reviews including user interface

If changes affect the user interface, it is also a smart idea to require the developer to submit a screenshot. That way the code reviewer can see the effects of the code change without running the code. Second, the code reviewer can spot discrepancies when running the code on her own machine.

### Code reviews including static analysis

Static analysis tools are only as good as their configuration, but, in terms of styling issues they can save a lot of time for code reviewers. Some teams at Microsoft use automated static and dynamic analysis tools as dedicated bot-reviewers. Those bots comment on code styling and other static issues. Thus, freeing up time for human code reviewers to perform more interesting tasks.

### Microsoft’s code review tool

For many years, one of the de facto standards for code review at Microsoft was an internal tool called CodeFlow. This is a sophisticated code review tool that supports developers and guides them through all steps of a code review. CodeFlow helps during preparation of the code, automatically notifies reviewers, and has a rich commenting and discussion functionality.

CodeFlow is an UI heavy tooling, much like Word or PowerPoint, as you can see in the screenshot below.

![Image](https://cdn-media-1.freecodecamp.org/images/CnMpM1uqn911onDKhvrJ2AVuXg0lz035cMg8)

#### CodeFlow’s interface explained

You can skip this if you want, but for all interested, I am walking you through the interface of CodeFlow. Looking at the screenshot, on the left (A) you see all affected documents.

Also on the left, you see (B) the list of reviewers assigned to the review as well as their status (e.g., signed-off or pending). The active document is shown in the editor (C ). At the bottom, you see (D) a list of comments for all documents.

On the other hand, in the active document (F) is one single comment. This comment is connected to the concrete part of the code (i.e., one word in a line). Finally, at the top you see the overall status of the code review. In this case, completed. The numbers before signal the different revisions. In this review, there have been five revisions.

#### Commenting functionality

One of the nicest features of CodeFlow is its commenting functionality.

A code reviewer can select very precisely the parts of the code she wants to comment on. For example, a reviewer can even highlight just one or two characters in a line, instead of highlighting a whole row. Then, the reviewer can attach a comment to that selection.

The code author or other reviewers are notified of this comment and can start a conversation in form of a thread around this comment.

#### Discussion functionality

This commenting functionality feels like commenting on social media platforms, such as Twitter or Facebook. Therefore, the commenting experience in CodeFlow feels very natural and allows rich conversations and discussions. Another nice perk is the possibility to assign a status to each of these comment threads. The status can, for example, be “won’t fix”, “resolved” or “open”.

### Comparison between code review revisions

A helpful feature is the possibility to select two different revisions of the code review and compare the differences between that. This means that you can see exactly which changes the code review author has performed between one code review revision and another one. That’s super handy to track the progress of the review.

### Code review analytics tool

Developers spend a substantial amount of their time performing code reviews at Microsoft. To ensure this time is well spent, Microsoft has its own code review analytics platform.

This platform stores all code review data starting from the code under review, the developers involved in code reviews, to all comments of the developers. Even the code changes for each of the revisions can be traced back.

This [code review data is the base for several empirical studies](https://queue.acm.org/detail.cfm?id=3292420) on code reviews at Microsoft. It is also used by many product teams for tracking their productivity and to understand their own code review practices. Also, many of the insights I share in [this blog post series about code reviews at Microsoft](https://www.michaelagreiler.com/code-review-blog-post-series/) stem from studies and analyses that involved this code review data.

### The future of code review at Microsoft

With Micorosft’s engagement and acquisition of GitHub change was inevitable. The change is visible by the vast adoption of Git as a source control tooling within Microsoft for example. But, this also means that at Microsoft code reviewing in form of pull requests is on the rise.

I’ll definitely plan to address code reviewing using pull requests at a later time.

### Coming up next: Code review challenges

I will write about code review challenges in the next blog post. To **stay in the loop** and **follow me** on medium.

**Credit where credit is due:**

I would like to mention my wonderful colleagues at Microsoft and the University of Victoria that have been part of this study: [Chris Bird](https://www.microsoft.com/en-us/research/people/cbird/), [Jacek Czerwonka](https://www.microsoft.com/en-us/research/people/jacekcz/) and [Laura Macleod](http://lmacleod.com/) and [Margaret-Anne Storey](http://margaretstorey.com/). I loved to work with you on this ♥

_Originally published at [www.michaelagreiler.com](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/) on March 27, 2019._

