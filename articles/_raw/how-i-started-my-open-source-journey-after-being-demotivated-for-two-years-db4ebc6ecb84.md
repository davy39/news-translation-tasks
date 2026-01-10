---
title: How I started my open source journey after being demotivated for two years
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T00:00:53.000Z'
originalURL: https://freecodecamp.org/news/how-i-started-my-open-source-journey-after-being-demotivated-for-two-years-db4ebc6ecb84
coverImage: https://cdn-media-1.freecodecamp.org/images/0*goprda8-nuOX0ezK
tags:
- name: JavaScript
  slug: javascript
- name: Mozilla
  slug: mozilla
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Hemakshi Sachdev


  Contributing to open source is very difficult. The people who do are experts with
  years of experience and we are just beginners — it’s not meant for us.


  Those were the exact words of my friends when I first asked them about what...'
---

By Hemakshi Sachdev

> Contributing to open source is very difficult. The people who do are experts with years of experience and we are just beginners — it’s not meant for us.

Those were the exact words of my friends when I first asked them about what open source and Google Summer of Code were and how we could contribute to them. The inferiority complex inside me (or I should say the superiority I gave to them for being a little more into coding than I was) made me believe their words for two long years. So I had totally abandoned the thought of ever contributing to open source.

But today, here I am with 12 PRs submitted successfully and 3 under review to organisations like Mozilla, freeCodeCamp and Gatsbyjs. And guess what? I’m still in college and have almost zero experience working in any organisation or company!

So, if you are someone who thinks open source is not meant for you just like I used to, then just STOP!

How did it all start?

### A Little Background About Me ??

My coding journey started three years back when I learnt how to code in the C Programming Language. Since then, I have learnt C++, Algorithms & Data Structures, and solved hundreds of algorithmic and logical problems on multiple sites like CodeChef, SPOJ, HackerRank & Codeforces.

Later, I moved on to learn web development from [freeCodeCamp](https://www.freecodecamp.org/). I liked its curriculum and most importantly their projects. But the best thing was their free and open community who were always ready to help you out. A lot of people helped me clear my doubts on the forum or the Gitter chatroom and the responses were always encouraging.

I literally felt that I owed the community and always kept looking for people to whom I could provide some help. To be honest, it always felt great whenever I helped someone with their questions and problems on the freeCodeCamp chat room. After a year, the thought of contributing to open source again came in my mind. I discussed my wish to contribute with those same friends, but all I got were those same words as before. I let that thought go away for the second time.

### That Little Spark Of Self-Belief & Courage?

After successfully completing my internship and securing a job, I was totally free in my senior year of my undergrad. The thought of Google Summer of Code again stumbled into my mind. As it was probably my last chance of getting into GSoC, and I didn’t want to have any regrets after leaving college and before getting into the real world, I finally said this to myself:

> Let’s just give it a shot. Worst comes to worst I might fail but at least I will know that I tried! I do not want to let go of an opportunity just because one person said to me that I can’t do it!

I googled everything about open source, what organisations to start with, how to find something to contribute to, every single thing!

Finally, I decided to go with Mozilla as it was the most beginner-friendly organisation. As Mozilla is a very large organisation, it has quite a lot of products under it, and again that big question came up: which product should I go with?

With the help of their [introduction page](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Introduction) and learning about my own interests, I went with Firefox DevTools. Why DevTools? Because for me, there’s nothing better than helping other people learn, improve and grow. And the fact that something developed or implemented by me would help others learn was the best feeling I could ever think of.

### The Real Struggle Begins ?

I’ll be honest here, before starting out everything looked intimidating. But once it’s all done you start finding that everything is a piece of cake. The first and most important step is getting and building code. Almost all organisations have a very detailed step-by-step guide for this. I struggled a lot in getting the code. Firefox’s codebase is H U G E! And thanks to the slow internet connection which made it worse. After three days of struggle, I was finally able to get the code and was able to build Firefox locally by carefully following the steps as mentioned in the docs.

Now that I had got it all working, the next step was to actually get something to work on! I went through all the `[good-first-bugs](https://bugs.firefox-dev.tools/?easy&tool=all)` and commented on the ones I found interesting by introducing myself and showing interest in solving the issue. I got myself assigned to one of them.

Every mentor knows that we are new to open source. Finding that one place where we have to make changes is like finding a needle in a haystack. So they guide us to the code files and sometimes even the line numbers where we have to analyse the issue and make the requested changes. And even if they don’t, you have every right to ask them and they will help you happily.

For the next 10 days, all I did was study the code, debug, build, run and analyse…but, I couldn't get to any solution or conclusions! ? Finally, I decided to go with all my analysis and results and ask my mentor for help. Sometimes you have to ask for help because without doing so you cannot move forward! The whole code is new to you and no one is expected to understand it in a couple of days.

My mentor realized that it was not a `good-first-bugs` kind of issue and solved it himself. To be honest, that was a little depressing. But my mentor gave me another issue to solve which was comparatively quite easy and I finally did it after a day or two of analysis! Yes, I was finally able to submit my first patch (PR)! But getting it landed was really not that easy, so many minor mistakes and ESLint errors that were literally frustrating. Finally, after 3 to 4 rounds of reviews, my patch landed! Yay! ?

After submitting my first patch, I quickly started looking for more issues to solve. I kept solving a few more `good-first-bugs` but soon I realized that I want to solve issues that involved more than just making minor changes and were something more complex. I was also still not sure of my interests and so wanted to explore a few more organisations. So I solved a few issues on Mozilla’s Taskclusters, freeCodeCamp and Gatsbyjs as well. But very soon I realised that Firefox DevTools was the one I enjoyed working with the most ? and continued contributing to it.

This is how the process of contributing to open source looks like:

1. Get an issue to work on.
2. Study the codebase and understand what needs to be done.
3. Code. Ask questions. Commit.
4. Submit a patch.
5. Resolve review comments and make the patch land.
6. Go back to step 1.

### Final Notes

To all the people who are reading this, I hope I was able to motivate you and make you realize that you are fit to contribute to open source — because the truth is you are! In fact, it’s not even necessary to know a particular programming language, as you can always help with the documentation or you can report detailed bugs and can always learn things along the way.

Yes, I know that we might not be making any big contributions to the codebase or not starting any big open source projects, but these little contributions are also as equally important as the larger ones. And it’s rightly said that _little drops of water make a mighty ocean_. You never know when your one little contribution may turn out to be so helpful for others and one day you might also end up with this:

![Image](https://cdn-media-1.freecodecamp.org/images/Bgl9xDj3ta2X2NQEmDYCuyDiopyE4AgMVo18)

Yes! I got recognized by Firefox DevTools for one of my contributions.✨ Here’s the [tweet](https://twitter.com/FirefoxDevTools/status/1116361470500057088).

So to all the open source beginners or the ones wanting to start with open source, I just wanna say this: forget what others think and believe and only remember what you want to do. You are capable, and that’s all that matters in the end. Just take that first step fearlessly and the world will guide you further — or I should say the mentors will guide you further. ?

Lastly, I would love to thank all my mentors and open source maintainers who helped in my journey and will do so in the future. A special thanks to [Jan Honza Odvarko](https://github.com/janodvarko) and [Nicolas Chevobbe](https://github.com/nchevobbe) for helping me, answering and clarifying all my doubts and questions, and showing so much patience while mentoring me. **Thank you so much! ❤️**

Anyone who needs help with starting out with either open source or programming, don’t hesitate and drop me a mail at sachdev.hemakshi[at]gmail[dot]com. I love getting emails ?.

Thank you to the freeCodeCamp team for publishing this article. ?

