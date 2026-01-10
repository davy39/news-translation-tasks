---
title: Why I’m not using your GitHub repository
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T16:25:39.000Z'
originalURL: https://freecodecamp.org/news/why-im-not-using-your-github-repository-2dff6c7ac7cf
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OqUuHr4YvJjeGWDn
tags:
- name: GitHub
  slug: github
- name: learning
  slug: learning
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sam Westreich, PhD

  As a bioinformatician, I reside in an interesting middle ground between developers
  and end users. My background training is in biology, not computer science.

  But in recent years, biology has moved closer to computer science. Man...'
---

By Sam Westreich, PhD

As a bioinformatician, I reside in an interesting middle ground between developers and end users. My background training is in biology, not computer science.

But in recent years, biology has moved closer to computer science. Many types of biological data are too big to analyze by hand and must be processed using computers. The ever-decreasing cost of genome sequencing has introduced vast amounts of sequence data. All this data needs to be assembled, compared, searched, and annotated.

More and more, biologists need computers.

More specifically, biologists need computer programs. Look, if I’ve got a bunch of sequence data from a microbiome that I want to match up to the different species of origin, I’m not going to sit down and build my own aligner tool from scratch. I’m going to grab an off-the-digital-shelf tool that’s been used before, pray that it is fairly straightforward to install, and plug it in.

In graduate school, I made a mistake. I allowed the fast pace of the computer world to seduce me. “No more multi-week experiments at the lab bench!” I declared to myself. “I’m going to dive headlong into the computer side of biology and become a bridge between both worlds — a _bioinformatician_!”

In theory, a bioinformatician analyzes data gathered by biologists, discovering new conclusions and forging new connections.

In practice, a bioinformatician installs a lot of programs and curses the developers who created them.

I’ve given up on many programs — some of which, I assume, are very good programs — because of nonsensical instructions, bad code, or horrible documentation.

It’s gotten to the point where I can glance at a GitHub repository and get a good sense of how I’ll feel about your tool.

Some repos instil confidence. Others fill me with dread.

Sometimes, I find one so bad that I refuse to even attempt to install the tool (unless it’s demanded by my boss).

Here are the biggest issues I see, and how to avoid them.

### Reason 1: No documentation

![Image](https://cdn-media-1.freecodecamp.org/images/1zjiS85MIpXdcMtpIlG0S-y71a8qsl74iaFH)
_No one knows how to use your program unless you write it out for them. Photo by [Beatriz Pérez Moya](https://unsplash.com/@beatriz_perez?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")._

I’ve seen every variation of documentation:

* Documentation written in the Readme.
* A “quick how-to” in the Readme, with detailed information in a separate PDF or Word document.
* A link to a GitHub wiki.
* A link to an external site, with documentation written there.
* A link to an external site, where there’s another link to download a PDF. (Why not just put the PDF in the repo?)
* Worst of all… **no documentation.**

Yes, I know that writing documentation is awful. I’ve built pipelines and tools, and I’ve forced myself to write documentation. I’ve forgotten about edge cases and the particulars of commands, and have sometimes received embarrassing reminders from users.

If you build a tool and make it public, your documentation should include, at minimum:

1. The requirements and dependencies to use your tool. This includes both hardware requirements (RAM and disk size) and software requirements (operating system, other programs).
2. How to install your tool.
3. What your tool does.
4. How to make your tool do those things, with example commands.

I also highly recommend that you include:

1. A ‘frequently asked questions’ section.
2. Tests — this includes test data and the exact commands that should be used on that test data (to the level where the commands should be copy/pasted onto the command line).
3. Examples of output.
4. A license.
5. Screenshots, if applicable.
6. Acknowledgements, whether you’re open to pull requests, and contact information, so users can report issues.

Bad or incomplete documentation is the number one reason I stop using a tool. You know how your tool works, but no one else does — don’t force people to figure it out. Give clear and easy instructions.

### Reason 2: Dependency hell

![Image](https://cdn-media-1.freecodecamp.org/images/FDURQPsceanAj4o0NmU9zlxk3jSqxqlwirie)
_“Each of these is a dependency. Be sure to unpack them all in the right order!” Photo by [chuttersnap](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")._

I once found a tool (a pipeline for DNA sequence annotation) that had six dependencies.

“That’s not the worst,” I thought to myself. “I can handle installing six dependencies to use this tool.”

Unfortunately, most of those dependencies had other dependencies. And those had even more dependencies, including some that refused to play nicely with each other.

By the time I gave up on that original tool, I’d come across nineteen different dependencies that I’d need to install, specifically to use this single pipeline. _Nineteen_!

It’s great that there are plenty of useful tools out there that can serve as the building blocks for more complex programs. It’s much better to use an already existing, already recognized dependency than it is to reinvent the wheel and do it all yourself.

But if you take this route, please find an easier way for me to install the dependencies for your tool.

Give me an install script that I can run to get all dependencies — this works especially well if I need a half-dozen Python or R packages. If possible, give me an archive of the dependency, so I don’t need to go and hunt it down (assuming that the license for the dependency permits this level of redistribution).

Don’t trap me in dependency hell — or if you do, be prepared to see many users give up on using your program. No one wants to spend time in hell.

### Reason 3: Abandonment issues

![Image](https://cdn-media-1.freecodecamp.org/images/KhyADvIhU0dygAeG6bMFeH4ECrYEia3ciQ8v)
_“No one’s made updates to this repo for a long, long time.” Photo by [Nathan Wright](https://unsplash.com/@cozmicphotos?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")._

When a GitHub project is new and fresh, there are no issues. It’s new, it’s clean, and no one’s stumbled across the bugs yet.

Over the next couple of weeks to months, as users find the program and test it out, they will raise issues. Thankfully, GitHub has a page on each repository dedicated to logging these issues. It’s called “Issues.”

Here, on this page, users comment that they get an error message when they try various tasks. Sometimes, it’s an out-of-date dependency. Sometimes, it’s a typo in the code. Sometimes, it’s user error — they have the wrong version of another tool, their inputs are in the wrong format, or they’re using illegal options and not reading the help messages.

On the surface, this is a great feature. But this Issues page can also be a warning — or a deterrent.

An Issues page can throw up one of two red flags — or a green flag:

* Red flag 1: There are no issues. There have never been any issues. **No one has ever used this tool, and it’s abandoned and gathering dust.**
* Red flag 2: There are several open issues, mostly about errors, with no resolution from the repo owner. **This tool is abandoned and broken and the owner doesn’t care.**
* Green flag: There are very few open issues, most of which are tagged as enhancements — but lots of closed issues. **The owner is actively fixing errors, helping users, and plans to add more features.**

Because I’ve published programs on GitHub, I know that maintaining them isn’t fun. It’s fun to create something new. It’s not fun to troubleshoot strange error messages and obtuse use cases. It’s not fun to pour back over pages of old code and figure out why a super-specific condition leads to failure.

But the best programs (and the most trustworthy GitHub repos) come from creators who are willing to do the boring, dull work. That includes fixing issues and providing support for users.

And if other questions are being answered, I feel more confident that my own problems will be addressed, and I’ll be able to confidently use the tool for my own purposes.

### Sell me on your program

![Image](https://cdn-media-1.freecodecamp.org/images/8EDMTIs25bBgemnT6mDTYz25kR-hn81Wk3yP)

Like it or not, your GitHub repository is often the ‘face’ of your program. Your repo needs to sell your program as easy to install, easy to run, and easy to understand.

A great GitHub repo is a beautiful thing. As a semi-skilled user, I love when a readme file tells me exactly what commands to install the tool, how to use it, and how to troubleshoot the most common issues. A detailed and straightforward manual puts a smile on my face. A one-step dependency install script makes me breathe a sigh of relief. Indications that you’re supporting your tool and fixing bugs causes my chest to fill with confidence.

Let me use your tool.

Let me cite your work and sing your praises to my colleagues.

Let me respect you and the great program you’ve built.

Avoid these issues — and avoid these errors in your next public-facing GitHub repository.

_Sam Westreich is a microbiome scientist working in Silicon Valley, and has spent years immersing himself in science and the nerdiest of pursuits. He blogs about science, biology, microbes and microbiomes, and his thoughts on graduate school and finding success._

