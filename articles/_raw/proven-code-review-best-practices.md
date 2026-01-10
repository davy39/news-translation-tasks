---
title: Proven Code Review Best Practices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-24T07:39:00.000Z'
originalURL: https://freecodecamp.org/news/proven-code-review-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Code-Review-Best-Practice-2.png
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

  What are the code review best practices companies such as Microsoft follow to  ensure
  great code review feedback? How do you stay productive while doing code reviews?
  Learn proven code review best practices from Microsoft in this ...'
---

By Michaela Greiler

What are the code review best practices companies such as Microsoft follow to  ensure [great code review feedback](https://www.michaelagreiler.com/great-code-review-feedback/)? How do you [stay productive](https://www.michaelagreiler.com/developer-productivity/) while doing code reviews? Learn proven code review best practices from Microsoft in this article.

The benefits of code reviews rise and fall with the value of the code review feedback. If done correctly, code reviews can help to ensure a high-quality code base. However, if teams are not aware of and do not follow code review best practices, developers may experience several [code review pitfalls](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/). In the worst case, [reviewing code can slow your team down](https://www.michaelagreiler.com/wp-content/uploads/2019/02/Code-Reviews-Do-Not-Find-Bugs.-How-the-Current-Code-Review-Best-Practice-Slows-Us-Down.pdf).

I have been researching and working with teams at Microsoft for several years. Through [several large scale-studies](https://www.michaelagreiler.com/publications/), we discovered a number of code review best practices that help teams stay productive and [boost their code review value](https://www.michaelagreiler.com/great-code-review-feedback/). But first, let’s start at the beginning. What does code review look like?

### A typical code review process

A [typical tool-based code review process](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/) starts when the engineer prepares the code for review. Then, she selects relevant reviewers for the code change. The reviewers are notified and give feedback on the code. The code review author works on the feedback until all parties are satisfied. Then, the code is checked into the common code base.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZOAaTZc1Z6XEK3Ri)

_A typical tool-based code review_

To ensure that this process is smooth and does not become a nightmare, it is important to [understand code review pitfalls](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/) and which code review best practices you can follow to overcome those.

The main code review pitfalls are:

* not getting useful feedback,
* not having enough time to do code reviews,
* code reviews taking too long causing long waiting times.

The code review best practices I present below help counteract those pitfalls, by making the job of the reviewers as easy as possible. They also help the reviewer to focus on providing valuable feedback.

### Code review best practices for code authors

In a code review, there are two different stakeholders: the code author who asks for feedback and the code reviewers, who look through the code change and provide the feedback. As a code review starts with the author, I explain the code review best practices for code authors first.

For my e-mail subscribers, I prepared an **exclusive code review e-book** including a checklist with all code review best practices. I also added additional bonus insights. You can request the [Code Review e-Book here](https://www.michaelagreiler.com/code-review-e-book/).

### Read through the change carefully

The first code review best practice is to read carefully through the code change before submitting the code for review. There is nothing worse than asking several developers to look through the code and give feedback on issues you could have fixed yourself.

This wastes everyone’s time and it might make you look bad. For future code reviews, developers may also be reluctant to review your code.

So, ensure you use a code review tool or a diff tool that can highlight what changed between this and the previous version. Because the code is presented in a different way and changed code passages are highlighted, it makes it easier for you to review your code yourself before sending it out.

Often you will see changes that you actually forgot you made or missing issues highlighted you should fix before asking somebody to review.

[The best time to fix issues is before the code is sent out for review. (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=The%20best%20time%20to%20fix%20issues%20is%20before%20the%20code%20is%20sent%20out%20for%20review.%20&via=mgreiler&related=mgreiler)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dvvMg-MkjhWYFzbM-Rpekw.jpeg)

_Thoroughly look through your code before submitting for review (Photo by [Marten Newhall](https://unsplash.com/photos/uAFjFsMS3YY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/magnifier?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

### Aim for small, incremental changes

As a developer, you should always strive for small, incremental and coherent changes. This best practice helps when working with code revision tools, such as git or SVN.

Small, incremental code changes are also a crucial code review best practice as other developers must be able to understand your code change in a small amount of time.

_10 lines of code = 10 issues._

_500 lines of code = “looks fine.”_

_Code reviews._

_- I Am Devloper (@iamdevloper)_ [_November 5, 2013_](https://twitter.com/iamdevloper/status/397664295875805184?ref_src=twsrc%5Etfw)

If several changes with different purpose happen within one code review [the task of code reviewing becomes more difficult](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/). This also decreases the ability of code reviewers to spot problems with the code. In several studies, we see that the value of the code review feedback decreases with the size of the change under review.

On the other hand, you also want to make sure the changes are coherent. Rarely code changes are too small to be sent out. It happens, but, not that often.

[The quality and value of code review feedback decrease with the size of the change. (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=The%20quality%20and%20value%20of%20code%20review%20feedback%20decrease%20with%20the%20size%20of%20the%20change.%20&via=mgreiler&related=mgreiler)

### Cluster related changes

Another code review best practice is to cluster related code changed. Imagine you plan to add some new functionality, fix a bug in another function, and refactor a class. Then, each of those changes should be a separate code review. This way, you ensure the purpose of the code change is clear to the reviewers. A clear purpose makes the reviewing job much easier and increases the feedback value.

### Describe the purpose and motivation of the change

One way to make sure you invest your time right during code review preparation is to write a description of what this code change is all about. With a small note, you help the code reviewers to understand the purpose of the code change and also why you changed it. This code review best practice speeds up code review time, increases the quality and value of the feedback, and improves code review participation rates.

![Image](https://cdn-media-1.freecodecamp.org/images/0*f-R3JWukTtkMA20T)

_Code reviewing isn’t a puzzle. Help reviewers focus on key issues by describing the code change. (Photo by [Hans-Peter Gauster](https://unsplash.com/photos/3y1zF4hIPCg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/puzzle?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

Code reviewing isn’t a puzzle. Help reviewers focus on key issues by describing the code change. (Click to tweet).

Interestingly, in our studies, we observed that developers really appreciate code change description. They actually wish that more people would write descriptions. On the other hand, we saw that the same developers did not always include descriptions themselves.

One reason for this is that when you write the code yourself, you are so involved with the code that you think it is self-explanatory. Fact is, it is not.

And if you do not help the reviewers to understand the code, [they will not be able to provide valuable feedback](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/).

So, write the note, even if it just says: “Updated the API endpoint to be compliant with security regulations”.

How much easier did the job of reviewing the code just get with this note? Remember, code reviewing isn’t a puzzle!

[Even if the code change seems trivial to you, add a description, so reviewers know what to expect (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Even%20if%20the%20code%20change%20seems%20trivial%20to%20you%2C%20add%20a%20description%2C%20so%20reviewers%20know%20what%20to%20expect.&via=mgreiler&related=mgreiler)

### Run tests before submitting a code review

Yes, take the time to run the tests for your code change. Testing isn’t only a best engineering practice, but it’s also a code review best practice. Because testing your code ensures that the code actually works before you ask for feedback.

In addition, it shows that you respect the time of the code reviewers. It is not only embarrassing to send out code that obviously (as the tests show) is not working as expected, it also kills everyone’s productivity. So, run the tests first!

### Automate what can be automated

As one of the main pitfalls for code reviews is taking too long, you better follow the code review practices of automating what can be automated.

Use style checkers, syntax checkers and other automated tools like static analysis tools to help improve the code. This way, you make sure that code reviewers can really concentrate on giving valuable feedback and do not need to use their time to comment on issues that can be found automatically.

### Skip unnecessary reviews

You read that right. Some reviews can be skipped. Obviously, it depends on your organizational policies, but if they permit it, you might consider skipping code reviews.

But stop before heading out and telling your team you need no code reviews anymore. Skipping code reviews is only advisable for trivial changes that do not change the logic such as commenting, formatting issues, renaming of local variable or stylistic fixes.

[Skipping unnecessary code reviews boosts your productivity. Click to tweet.](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Skipping%20unnecessary%20code%20reviews%20boosts%20your%20productivity.&via=mgreiler&related=mgreiler)

### Do not select too many reviewers

You should select the right number of reviewers for your code change. If now numbers above 4 people come to your mind, I’d like you to stop right there. Because adding too many developers on code reviews does more harm than good.

One problem is that if you add too many developers, each one of them feels less responsible to give feedback. Another issue is that adding more people than necessary decreases your team’s productivity.

Some studies suggest the code review best practice of adding only two active reviewers.

For some code changes, you want additional experts like security experts or developers from other teams to look through the code. But, more often than not, two active reviewers are just fine.

Many code review tools allow notifying developers without making them mandatory reviewers. This ensures that they stay in the loop and are aware of what is happening, but removes the obligation for them to comment on your code.

### Add experienced reviewers to get insightful feedback

Studies have shown that the most insightful feedback comes from reviewers that have worked on the code you are going to change before. They are the ones that give the most insightful feedback.

How often a reviewer has already reviewed code influences the ability to give useful feedback. Similar, experienced and senior developers tend to give better code review feedback.

But, be mindful about the workload of senior engineers, as they tend to be added as reviewers a lot.

[Developers that changed or reviewed pieces of the code before, give the most valuable code review feedback. (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Developers%20that%20changed%20or%20reviewed%20pieces%20of%20the%20code%20before%2C%20give%20the%20most%20valuable%20code%20review%20feedback.&via=mgreiler&related=mgreiler)

### Add junior developers to let them learn

One of the code review goals is training and learning, so do not forget to include junior developers. Consider adding reviewers that are not familiar with the code base, but that would benefit from the knowledge to allow knowledge dissemination.

### Notify people that benefit from this review

For some people, like project managers or team leads, receiving notification about code reviews (without being actually required to do the code review) is beneficial. But, you have to take a conscious decision on whom you gonna notify. Not everybody really cares or should care about your code review.

### Don’t notify too many people

Do not add everybody on the notification list. Only add people who actually benefit from the information that a code review is in the process.

I have seen teams, where each team member was added to each of the code review of the extended team by default (+70 people). This practice is like adding nobody to the list. Or in the worst case, you have several of your engineers spending their time looking through hundreds of code reviews to figure out if it’s relevant for them.

### Give reviewers a heads-up before the review

A really effective code review best practice is to let your co-workers know ahead of time that they will receive a code review soon. This code review best practice reduces turn-around times substantially.

So, let them know a code review is coming their way as soon as possible.

[Giving people a heads-up that a code review is on its way can speed up review time. (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Giving%20people%20a%20heads-up%20that%20a%20code%20review%20is%20on%20its%20way%20can%20speed%20up%20review%20time.%20&via=mgreiler&related=mgreiler)

### Be open to suggested changes

Receiving unexpected comments or feedback might make you tense and defensive. Try to prepare yourself mentally and work on your ability to be open to suggestions and different viewpoints. Always start with the assumption that the reviewer had the best intention.

If some feedback made you uncomfortable try to sort things out as soon as possible. Sometimes it is a good idea to have more personal face-to-face conversations to resolve some issues.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oWg1z_ShPb7yfPB1G7VzSg.jpeg)

_Don’t be defensive if confronted with unexpected feedback. (Photo by [Sweet Ice Cream Photography](https://unsplash.com/photos/2VwP6rUzZQ0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/danger?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

### Show respect and gratitude to the reviewers

Code reviews rise and fall with the team’s feedback culture. As a code author, show gratitude and value the received feedback. Make sure to carefully consider the reviewers’ feedback and communicate throughout the feedback cycle.

Tell the reviewers which actions you took and which decisions you made because of the received feedback in a respectful manner.

[Code review rises and falls with the quality of the team’s feedback culture. (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Code%20review%20rises%20and%20falls%20with%20the%20quality%20of%20the%20team%27s%20feedback%20culture.&via=mgreiler&related=mgreiler)

But, creating a great feedback culture is a two-way street. Naturally, code reviewers influence the culture a lot. So let us look closely at the code review best practices for code reviewers.

### Code Review Best Practices for Code Reviewers

Being asked to give feedback on a code review is an honor, so you want to make sure you know [how to give valuable code review feedback](https://www.michaelagreiler.com/great-code-review-feedback/).

During code reviews, you can not only demonstrate your skills and knowledge but also mentor other developers and contribute to the team’s success. Nothing worth than investing time in [code reviews and not getting valuable feedback](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/).

### Give respectful and constructive feedback

Even though it reads like a no-brainer, code reviews do put the code author in a vulnerable position, so you must be considerate of that.   
Your job is it to give constructive and valuable feedback but also to do so in a respectful manner.

Especially using code review tooling, please reflect on how and what kind of feedback you give. It is just so easy to hurt someone feelings — especially in written form. Too often time pressure might make you give a sloppy answer that can be misinterpreted.

### Go and talk in person if necessary

Code review tools and chat-tools allow us to communicate with our peers in an asynchronous and effortless way. But, there are quite a few situations where a proper human interaction, either face to face or via voice/video cannot be bet.

Complex issues, for example, can be much more efficient and positively resolved once you hop over to your colleague or call her and discuss it personally. The same holds true for contentious issues or sensitive matters.

Maybe it is a better strategy to write a private email or seek a personal discussion with the code author if you think you might hurt some feelings are make the engineer lose the face. So, whenever you face a complex issue or might hurt some feelings, rethink your communication channels and act accordingly.

### Ensure traceability for decisions

Even though less traceable conversations, such as face to face or video calls can make a big difference for team dynamics, it is important to document the discussion. Especially the code review outcome should be tracked for future reference by using traceable tools such as the code review tool.

The code review tool is the right communication channel for all simple matters, as it allows the whole team to follow along, and enables to look-up decisions and understand code development after the fact.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b9Y7gwaQTuwuJHHn0WnitQ.jpeg)

_Leaving traces about your decisions and changes helps to understand code evolvement (Photo by [Marten Bjork](https://unsplash.com/photos/GM9Xpgb0g98?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/trace?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

### Always explain why you rejected a change

Let’s be honest. Having a code change rejected isn’t something the code author will enjoy. So, it is important that you are thoughtful and explain your rejection in a polite, constructive and friendly way.

Explaining the reasons behind your decision does not only help the code author to learn and grow but also helps the author to understand your viewpoint. It also promotes an ongoing dialog with the author.

Tell the code author exactly what she has to do to get the change accepted.

[If you have to reject a code change, explain exactly what has to happen that the change can be approved. (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=If%20you%20have%20to%20reject%20a%20code%20change%2C%20explain%20exactly%20what%20has%20to%20happen%20that%20the%20change%20can%20be%20approved.&via=mgreiler&related=mgreiler)

### Code review best practices for boosting productivity

Some of the biggest challenges during code reviews, for both the code author and the code reviewer are time constraints.

As a reviewer, you might find it challenging to take time out of your daily tasks to review the code of your peers. But, code reviews can be very beneficial to you and the team if done in the right way.

### Integrate code review into your daily routine

Structure your day-to-day business in a way that you set dedicated time aside just for doing code reviews. For example, plan to work on code reviews every day from 11 to 12 AM.

This way you make sure you can account the time for code reviews, and also make it an anticipated activity for you and your team. This schedule will come in handy every time you have a reflection on your work progress or an evaluation of your work.

### Reduce task switching as it kills productivity

[Switching from one task to another is costly](https://www.michaelagreiler.com/developer-productivity/). Knowing you do not stop whatever you do every time a code review comes along your way ensures you can work more focused.

Which time slots work depends on your workload, the number of code reviews you have to perform as well as on the time those reviews normally come in. In some settings, your team benefits from two (shorter) scheduled reviewing times, such as in the morning and before you leave the office. This way, your peers do not have to wait for your feedback too long.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQJJWck316aARPb0jFk97w.png)

_Task switching kills productivity (Photo by [Tim Gouw](https://unsplash.com/photos/1K9T5YiZ2WU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/problem?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

[Task switching kills productivity. So have dedicated code review times.](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=%20Task%20switching%20kills%20productivity.%20So%20have%20dedicated%20code%20review%20times.%20%23codereview%20&via=mgreiler&related=mgreiler) [#codereview](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=%20Task%20switching%20kills%20productivity.%20So%20have%20dedicated%20code%20review%20times.%20%23codereview%20&via=mgreiler&related=mgreiler) [(Click to tweet)](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=%20Task%20switching%20kills%20productivity.%20So%20have%20dedicated%20code%20review%20times.%20%23codereview%20&via=mgreiler&related=mgreiler)

### Give feedback in a timely manner

It is not advisable to jump right into a code review, whenever the notifications pop up, because of context switching costs. Still, it has several advantages for you and the code author to review the code in a timely matter.

Giving feedback as soon as possible ensures that the code author is not blocked by waiting for feedback. Also, if the author has to wait too long, it becomes harder for her or him to remember the changes and incorporate the feedback. Remember long waiting times are a number one [code review pitfall](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/).

Being one of the first reviewers (especially if there are quite a few) also ensures your effort looking through the code [actually adds value](https://www.michaelagreiler.com/great-code-review-feedback/). If you are the fifth person inspecting the code, chances are you are not going to add new insights anymore. If that happens frequently, you should implement the code review best practice for selecting fewer reviewers.

### Review frequently not in a big bang fashion

Research shows that you can give better quality feedback if you review frequently and therefore less changes at a time. That means that you do not wait until several code reviews pile up to look through them in one go. Instead, you stick to your schedule and review one code review (or even parts of one if it is a larger code review) at a time.

If code reviews are generally too large and take too long, you can suggest the code review best practices for small, incremental and coherent changes to the code review authors.

[Give better quality feedback to code reviews by not letting them pile up. (Click to tweet).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Give%20better%20quality%20feedback%20to%20code%20reviews%20by%20not%20letting%20them%20pile%20up.&via=mgreiler&related=mgreiler)

### Focus on core issues, less nit-picking

Your goal as a reviewer should be to help with core issues, such as bugs, architectural problems, structural problems or problems that will lead to maintainability issues.

Obviously, if you see typos, badly named variables or styling issues, you might also point that out. Still, this is not your main tasks and, understandably, over [discussing minor issues isn’t valuable to code authors.](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/)

### Use a review checklists

Another code review best practice is to use a systematic approach for code reviews. A code review checklist can speed-up and improve your code review performance. Instead of making one from scratch, download a ready-made list and customize it to fit your team’s practices and your needs. Be sure to look for a checklist that is tailored towards your technology stack. 

### Code review best practices checklist

Now you know all the code review best practices to make the most out of code reviews. If you enjoyed this post, consider subscribing to my email list.

I prepared an exclusive [Code Review e-Book](https://www.michaelagreiler.com/code-review-e-book/) for my e-mail subscribers to help you remember the code review best practices. I also added other great insights and summaries about code reviews. Get the 12 page insights to code reviews now. Not a subscriber yet? Just sign-up.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HBwTGSldWHSf2u7yZ-8X1A.jpeg)

## Want more on Code Reviews?

Check out [proven code review best practices](https://www.michaelagreiler.com/code-review-best-practices/), learn about which [code review pitfalls](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/) you should avoid, and also how to [boost your code review value with great feedback](https://www.michaelagreiler.com/great-code-review-feedback/).

To **stay in the loop** and never miss a blog post, **sign-up** to my email list and get the **exclusive code review e-book.** You can request the [Code Review e-Book here](https://www.michaelagreiler.com/code-review-e-book/).

### You find me on Twitter

[Let's connect on Twitter](https://twitter.com/mgreiler) to discuss software engineering topics and code reviews there.

---

_Originally published at_ [_https://www.michaelagreiler.com_](https://www.michaelagreiler.com/code-review-best-practices/) _on May 2, 2019._

