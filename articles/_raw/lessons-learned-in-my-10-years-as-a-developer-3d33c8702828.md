---
title: Lessons learned in my 10+ years as a developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T17:08:23.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-in-my-10-years-as-a-developer-3d33c8702828
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_6Q3e7_NMGteVQbGbKEZy5g.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Huseyin Polat Yuruk

  12 months.

  That’s the time we wasted while rewriting our software from scratch.

  Twelve long months in the software market.

  Without innovation.

  Without moving forward.

  Really, I cannot stop asking this question to myself.


  What ...'
---

By Huseyin Polat Yuruk

### 12 months.

That’s the time we wasted while rewriting our software from scratch.

Twelve long months in the software market.

Without innovation.

Without moving forward.

Really, I cannot stop asking this question to myself.

> What could we achieve in this fast-moving world in 12 months?

_“Tuesday, January 20, 2015, 5:10 PM, AntiMalware product is finally going its first public beta.”_

After hours without sleeping, the first release note that would give a start to our new journey was published on the website.

I was working for one of the small cybersecurity companies which provides security software for end users and enterprise companies. Our software protects users against malware. It cleans their computer if they get infected. Our AntiMalware was one of them.

The first beta version’s feedbacks and impressions were promising. We were four developers, working on that product and constantly fixing bugs, iterating new versions by improving the product.

#### **First stable version**

After two months working on bug fixing, improving and coding, we released the first stable version of AntiMalware.

What were users saying?

Most of our users’ feedbacks were great, and they liked the product. This was keeping our team motivated. We were actively working on the product to improve our core features.

#### **The airplane is taking off.**

2016–2017.

Our golden years before the big storm.

AntiMalware was living its best times. It was becoming our flagship product. Users were recommending it to their friends. Every blog and forums related to security were recommending our software. It was the first option when it comes to rescuing infected users.

Downloads, installations, sales.

Every metric was going up, the user base was growing quickly over months. Founders were happy, the team as well. This was the big success the company was looking for. Everyone thought: “_We did it! Like other big companies, we thought we created our own success story.”_

#### **New opportunities (at least we thought like that): Entering the enterprise market**

The company decided to enter the enterprise arena. We were building a new team for the corporate product. The product owner of AntiMalware was leaving the team. Our CTO was taking responsibility and becoming the new owner. (Big mistake. I will explain why).

Some developers were leaving the company, but it was OK. We were handling everything well and AntiMalware was still the best option in the market.

#### **Good days were behind. Let’s face reality.**

As I told you, our CTO was handling everything about AntiMalware. He was the main developer, constantly releasing new updates and improving the product’s capability. However, because of his position, he had to handle other company stuff also.

Sure, in the beginning, everything was going well. As in every development process, in our case also, we had to keep maintaining and improving our software.

As we should have expected (clearly we didn’t), somehow, the development process started slowing down.

The days when we were releasing new updates were behind. At that moment we were living the reality of late updates and soon no updates at all. This bugged me a lot and one day I asked our CTO:

> “What is wrong with this product?  
> Why do updates take too much time and development is slowing down?”

He took a deep breath and started talking:

_“The code base is really complicated. It is not structured well and it is not loosely coupled. The architecture was designed in a totally wrong way. The UI and core logic interfere with each other. Whenever I fix a bug or change something, this affects other parts of the software. Even small changes are hard to be done. With every new update, something new comes up._

_There are some methods that take 20 parameters, they are two pages long! Can you imagine? There are many things that were supposed not to be implemented but they were implemented anyway._

_That’s why every update takes too long and I cannot implement a new feature. If we release a new update, I am scared that we might introduce new bugs and break the program’s core functionality that works well now. That’s why it is too risky for us to release a new update. We can lose our users. We can lose our product as well.”_

A burst of reality came out from his end and all of us knew it. Actually, we were expecting this answer from him.

But there was one more thing to be asked. He was leading the previous main developer who led the product for one year, so how could the code be that messed up?

_“I didn’t want to break his motivation. We had to enter the anti-malware market as fastest as possible and he was good at this. That’s why I didn’t want to stop him.”_

Basically, we sacrificed the code base to enter the market in the fastest way, but this destroyed our product’s future.

**Lesson learned**: Don’t hesitate to say “this is sh*t” if something is really sh*t. The future of your product is more important than your spaghetti code. Focus on to have a sustainable product.

#### **How can we fix this terrible code?**

> “We’re programmers. Programmers are, in their hearts, architects, and the first thing they want to do when they get to a site is to bulldoze the place flat and build something grand. We’re not excited by incremental renovation: tinkering, improving, planting flower beds.”  
>  — [Joel Spolsky](https://www.joelonsoftware.com/about-me/), CEO of Stackoverflow

Developers always have a tendency to throw away the code and start over. There’s a reason for that. The reason is that they think the old code is useless and a mess. But again we just think! However, when we try to find out what is the real reason behind that, we can face the fact:

_We_ _are probably wrong!_

The reason that the old code might look messy to us and that it has to be rewritten from scratch isn’t actually because of the code but rather because of a cardinal, fundamental law of programming:

**It’s harder to read code than to write it.**

This is why it is so hard to reuse code. This is why we think “_It’s a big hair mess_”. This is why our subconscious mind whispers to our ears “_Throw it away and start over_” when we read another developer’s code.

Like every developer, we fall into this trap. Just checking our messy code one time was enough to think about rewriting it from scratch.

After a series of meetings, even though our CTO was resistant to code rewriting (right behavior), he was convinced in the end and we started the rewrite.

**However, this decision didn’t last too long…**

It was a weekend. Sunday. I was drinking my morning coffee and reading some articles. Like my feed knew what to show me, I came across the most known article about rewriting the code. It was [Netscape’s rewriting story](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) written by [Joel Spolsky](https://www.joelonsoftware.com/about-me/).

Sharing this article with the rest of the AntiMalware team, including our CTO, was my immediate action after I finished reading it.

Another discussion started.

It was already hard to convince our CTO to rewrite the code but after reading that article, he changed his mind again. He did not want to execute this decision. Other team members were yelling at me:

_“Why did you send this article? We already convinced him. This product must be rewritten from scratch. This is the only way.”_

Hereby, our first attempt was finalized and we closed that rewrite topic. Our CTO believed that he could manage this crappy code and that he could release a new update. This topic was closed until harsh reality knocked us down.

**One year without any update…**

**Really, this is not a joke. This happened!**

_“Why no update?”_

_“It has been months since the last update.”_

These negative comments from our users become our reality. As a small company, we had too many products to manage, and on top of it, we entered the enterprise market which caused us to come to that point actually.

Mix all of that and you get one point: we forgot about our users.

So, imagine. We didn’t want to release a new update because we didn’t want to lose our users.

Actually, it should’ve been opposite: if we don’t release a new update we will definitely lose our users because hey we didn’t give them an update for over a year and a half.

After the reality slapped us in the face, we decided to reach back and for us, rewriting software was the only option so we did it.

**Today.**

_“Monday, 17 December 2018, 21:40. The email was prepared to be sent to our private beta group.”_

After 12 exhausting months, we completed our rewriting process. We prepared the first beta release note, just like the first day our product met the market.

Here we are again…

The rewritten version of the product is still in Beta. It has been almost one month. We are fixing bugs, listening to our users, reviewing feedbacks… As we did 4 years ago…

What have we missed during these 12 long months? Who knows what else we could have done instead of rewriting?!

Many questions can be asked at this point. All I know is that rewriting was the only option for us or we couldn’t see any other solution.

If you fall into this trap too and start thinking _“I should rewrite the software from scratch”,_ consider asking these questions that I believe every developer should ask before taking the first step to code rewriting.

### 1. Are you ready to throw away all that knowledge?

I am asking seriously! Please be honest with yourself and answer this question: Are you really ready to throw away all that knowledge, all those collected bug fixes, years of programming. This is what you expect when you throw away the code and start from scratch. When you look at code rewriting from this perspective, it’s painful, isn’t it? All those sleepless nights trying to fix bugs go through your eyes. Believe me, I know.

You had to talk to a lot of users to find the issue that caused your software not to work properly. Then you had to find this bug in your software. Then you had to reproduce the issue then find the fix, then… and so on and so on.

### 2. Can you guarantee that you are going to do a better job than you did the first time?

It’s important to keep in mind that when you start from scratch there is **no** **guarantee** that you are going to do a better job than you did the first time.

Since you chose to throw away all that knowledge, collected bug fixes, there is a high possibility that same bugs might again come up.

Probably, the rewriting team is going to be different than the team worked on the first version. So you don’t actually have “more experience”. You’re just going to make most of the old mistakes again and introduce some new problems that weren’t in the original version.

If you don’t plan well the rewriting process, there is a big risk that a new version might be worse than the original version at solving your customer’s problem. With this rewriting decision, you’re going to take this risk that can cause you to lose your customers.

### 3. Are you ready to give a gift of months/ years to your competitors?

Do you know exactly how much time do you need to rewrite your software?

It takes a lot of effort, planning, preparations. You will plan each task and sprint one by one and you will exactly know your deadline to finish this painful process. Or you will miss the deadline. Who knows? There is a high possibility that you won’t finish this process on time.

You will be in an extremely dangerous position where you will have to ship an old version of the code for months or years, completely unable to make any strategic changes or react to new features that the market demands because you don’t have shippable code.

Your customers might as well just abandon you because you don’t give anything new and you keep shipping your old product without any changes.

Did you think about this?!

### Lessons learned in rewriting software

> Rewriting a system from the ground up is essentially an admission of failure as a designer. It is making the statement, “We failed to design a maintainable system and so must start over.” — [Max Kanat-Alexander](http://www.oreillynet.com/pub/au/5113), [Code Simplicity](http://shop.oreilly.com/product/0636920022251.do)

So as other designers, we admitted that we failed to design our software and we learned a lot from that exhausting process. Here I am sharing lessons that stuck to me.

#### **Rewriting code is a developer illusion, not the solution in most cases.**

When you are in trouble with your code, it is important to diagnose what is the issue exactly. As every developer will do, your initial thought shouldn’t be rewriting. This is just an illusion. It is illusion because you are struggling to read someone else’s code and you think you would do a better job if you rewrote it from scratch. In this case, always remember the fundamental law of programming.

#### **Consider refactoring before taking a step to code rewriting**

Targeted rewrites are useful to deal with the worst offenses in your code base. Don’t do a whole rewrite if you can limit the scope and address the majority of your problems. For example, the loading of your software is so slow. But this only affects a small part of the project. These problems can be solved, one at a time, by carefully moving code, refactoring, changing interfaces. You don’t have to rewrite the whole thing.

#### **Beware. This is a longer, harder, more failure-prone path than you expect.**

There is a fact that developers usually realize it after they miss the deadline: _everything takes longer than you think._ Be very pessimistic in your estimates about the cost of a rewrite. It almost always costs more and takes longer than you would think. There will be always a lot of complexity that will make the rewriting process harder and more painful. In the end, the possibility of failure is hard to miss.

#### **Make sure the new product is better at solving user’s problem (or at least the same). Worse cannot be acceptable.**

Rewrites have no direct effects/benefits for the customer. Your users don’t care about your code. They just want to solve their own problem. That’s all. In their eyes, you are successful if your product fits in solving their problem. Otherwise, they are not using the product. They don’t care about your rewriting decision, so the rewritten version must at least work as efficiently as the old one.

#### **Keep maintaining and supporting the existing product.**

In our case, we didn’t give any update to users for one year. This is too long in the world we live in today. Our product was still good enough, but users were complaining about no updates. Never stop maintaining a system that is currently in use so that the programmers can rewrite it. During the rewriting process, the old code still needs to be maintained. Small updates and bug fixing should be given to users while you are rewriting the old code. Otherwise, you will face losing your customers.

#### **Involve users in the design process as soon as possible.**

Always show your current progress to your end users at regular intervals so that they can help you catch the worst offenses. It is important to meet your users as soon as possible. Their feedback will help you design a new product based on their needs. Don’t implement any unnecessary features. This will save you from having a complicated code base.

#### **Keep the teams working on the product synced.**

The product is not only about the programming team. Marketing, support, programming, design… Many teams work on it. Keep them synced by giving them regular updates about the rewriting process.

In our case, we have dealt with many problems. For example, the marketing team was preparing our product beta campaign and they had to know exactly what was going on the product side so that they could prepare customers for upcoming product changes. Sometimes we made some changes without informing them. And this caused them to prepare their campaign all over from scratch. Don’t spend anyone’s time inefficiently.

#### **Don’t make dramatic changes to the product.**

It is important to know your product’s weak and strong sides. Don’t change the strong sides, the ones loved by users. If users are satisfied with your UI, don’t change it. Do minimal changes and small UX improvements. When you replace your existing software with the new one, your users shouldn’t be confused with the new dramatic changes. There are many cases where users abandoned new products because they didn’t find the same functionality as the previous product provided. Don’t let the same thing happen to you.

#### **Don’t make your product depend on only one developer.**

In our case, our CTO was the responsible developer for our software. Due to his position, our product development was going slowly. Even small changes were taking several weeks, sometimes months. The point is to always keep moving. Never stop.

#### **Migrations should be slow and steady.**

Replace your original software with the new one when you are sure that the new one is ready. Do it step by step.

First, start with a small private beta group and ship your product into that group. Continuously collect feedbacks and crash reports, fix the bugs, iterate new versions and again the same thing. Follow this cycle until you ensure that your product is ready to go public beta.

When you go public beta, feedbacks are going to be your best friend again. Your first goal here should be to ensure that your product solves the users’ problems. When you are sure that you are providing the same or better functionality as old software did, replacement can take place. Release the new software for new users, and migrate your existing users to the new one.

Those are the key lessons that I learned from our rewriting process. Rewriting is almost [_never_](http://www.joelonsoftware.com/articles/fog0000000069.html) the answer. More often than not, refactoring is a better bet. I strongly advise the slow approach of using refactoring. It’s less risky and you keep your customers happy.

### When to rewrite the code

There are times when it is appropriate to do a rewrite. If I could have made a list about when to rewrite the code, this would be my list:

**Switching to another language or platform (as in our case):** The language is so old. It is hard to find a developer or you have to pay a lot of money to get one. In both cases too much effort.

**The existing codebase is not maintainable anymore (as in our case):** How do you decide your code is not maintainable? It is hard to determine but if even small changes are hard to be done, if new updates take longer than usual, if any new change affects other parts of the software and introduces new bugs, your software is unmaintainable.

**You have the resources available to both maintain the existing system and design a new system at the same time:** Never stop maintaining a system that is currently in use so that the programmers can rewrite it. Systems must always be maintained if they are in use. And remember that your personal attention is also a resource that must be taken into account here — do you have enough time available in each day to be a designer on both the new system and the old system simultaneously, if you are going to work on both?

**The developers in the team are a bottleneck for software (as in our case):** This shouldn’t be a reason to rewrite the code from scratch. You can always switch developers within the team or you can hire new developers to eliminate the bottleneck situation.

However, sometimes, as in our case, there might be times where you have to choose the rewriting option. Our software was written with old technology and our CTO was the only responsible person to develop it. We tried to find a new developer but it was hard because of the age of this coding platform. Even if we could have found a new one, it would be very expensive for us. So together with other conditions, this was in our list to decide to rewrite code.

**The software is long-lived (I’m talking like 10–20 years or more):** Maintenance becomes more and more expensive over time. This is due to the fact that the code is becoming more and more spaghetti-ish as the original architecture is sacrificed for quick maintenance patches. Also, developers for older technologies become rarer and more expensive. Finally, hardware begins to age and it gets harder and harder to find new hardware, operating systems, frameworks, etc. to run the old application on top of it. Also, businesses evolve, and most likely an older system will not be meeting the business needs of the organization.

So you have to weigh all of the ongoing maintenance cost, as well as the potential benefits of a new system, against the cost of rewriting it from scratch.

If your case fits in one or more of the above points, you may be in a situation where it is acceptable to rewrite. Otherwise, the correct thing to do is to handle the complexity of the existing system without a rewrite, by improving the system’s design in a series of simple steps.

Rewriting your code from scratch could be the single biggest mistake you make, but equally so, not-rewriting your code could lead to the same result. Here is a piece of advice. Refactoring should be the first option.

Some developers will keep believing that all systems must eventually be rewritten. Always keep in mind that this is not true. It is possible to design a system that never needs to be thrown away. There will be always a software designer around you saying “We’ll have to throw the whole thing away someday anyway”. But if software is built right to start with and then properly maintained, why would it be thrown away?

_Originally published at [huseyinpolatyuruk.com](https://huseyinpolatyuruk.com/lessons-learned-from-rewriting-code-in-my-10-years-as-a-developer/)._

**Each ? is welcomed if you enjoyed this article!**

**I write about programming, technology, AI, startups and self-growth. If you [follow me on Twitter](https://twitter.com/h_polatyuruk) I won’t waste your time with unnecessary posts. ?**

