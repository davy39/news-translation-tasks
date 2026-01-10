---
title: Sacrificial Architecture – How to Make Tough Decisions to Abandon and Rebuild
  Systems
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-24T19:02:30.000Z'
originalURL: https://freecodecamp.org/news/sacrificial-architecture-make-tough-decisions-to-abandon-and-rebuild-systems
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-wendelin-jacober-1411400.jpg
tags:
- name: Clean Architecture
  slug: clean-architecture
- name: clean code
  slug: clean-code
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: "By Nahla Davies\nWhen you're working with an application, sometimes it\
  \ no longer makes sense to try to continue and improve what already exists. Instead,\
  \ you need to rethink, restructure, and rebuild. \nMaking the decision to give up\
  \ all the work you a..."
---

By Nahla Davies

When you're working with an application, sometimes it no longer makes sense to try to continue and improve what already exists. Instead, you need to rethink, restructure, and rebuild. 

Making the decision to give up all the work you and others have put into the existing system is a difficult choice for many developers. Still, dogged devotion to existing code in the face of disruption is a disservice to developers and users alike.

The effects of any large-scale alterations to a system reach far beyond the development world. Wholesale system replacements are rarely invisible, which also makes life difficult for salespeople and marketers. They're the ones who have to explain to customers why such a drastic change happened. 

But this does not make the changes any less necessary.

As with so many other things in life, just because a choice is difficult and painful does not mean it is wrong. Evolution can be a violent process. But failure to adapt leads to extinction. 

When fish crawled out of the sea millions of years ago, they didn’t continue to improve on fins and gills. Entirely new systems were necessary for motion and breathing. It doesn’t mean that fins and gills weren’t valuable or that their design was flawed. Indeed, their designs fit perfectly with their intended purposes. But the purpose became irrelevant, and so they were no longer suitable in their current environment. 

When the time comes (and it will), you must step back and take an objective look at the situation. Will another tweak to that fin work? Or will it just highlight how poorly adapted it is to current needs?

## Intelligent Design Choice or Inevitable Reaction?

Much of the discussion on sacrificial architecture revolves around whether it should be a proactive development process as opposed to a last-ditch reactionary decision. 

Should developers intentionally build systems with limited lifetimes? Or should they build for the long run and make large-scale changes only if absolutely necessary?

According to Martin Fowler, who [introduced sacrificial architecture seven years ago](https://www.infoq.com/news/2014/11/sacrificial-architecture/), building it into the design process can be a good idea:

> _“So what does it mean to deliberately choose a sacrificial architecture? Essentially it means accepting now that, in a few years’ time, you'll (hopefully) need to throw away what you're currently building._   
>   
> _This can mean accepting limits to the cross-functional needs of what you're putting together. It can mean thinking now about things that can make it easier to replace when the time comes - software designers rarely think about how to design their creation to support its graceful replacement. It also means recognizing that software that's thrown away in a relatively short time can still deliver plenty of value.”_

Intentional sacrifice can also be useful when considering new features or applications as a way to limit overall development effort. 

Using sacrificial architecture for proof-of-concept systems can move the development process more quickly towards a launchable implementation. As noted in [the Open Group Agile Architecture Framework](https://pubs.opengroup.org/architecture/o-aaf/snapshot/Agile_Architecture_Framework.html):

> _“When the goal is to get rapid market feedback experimenting with an MVP, sacrificial architecture is an option to consider as it would not be worth spending too much time designing an architecture that would have to change should the product owner decide to pivot.”_

This is not to say that proactively using sacrificial architecture will eliminate the need for reactive sacrifices. There are always going to be changes and disruptions that you and your team will not anticipate. And disruptions often lead to sacrifices and evolutions. 

Just consider how the COVID pandemic crisis disrupted so many aspects of everyday life, from how employees work to [how schools teach our children](https://www.freecodecamp.org/news/disrupting-the-status-quo-of-traditional-learning-ef83c694cfd7/).

There are many less drastic examples as well. One side effect of the COVID crisis was the rapid acceleration of e-commerce business and online transactions. 

But the industry had to adapt to rising consumer concerns about data privacy. All online businesses rely on software with crucial features such as online invoicing and payments. But application providers and payment processors had to rapidly adapt existing systems to ensure compliance with new standards like the Payment Card Data Security Standard (PCI-DSS) and the European Union General Data Protection Regulation (GDPR). 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-179.png)
_[Image Source](https://interestingengineering.com/best-youtube-channels-for-coding-and-programming)_

In the same way, code can become obsolete or fail to accomplish its intended purposes. There are times when disruptions in coding practices or programming language capabilities mean that you need to make large-scale changes. 

Just consider eBay, which has changed its underlying programming language twice since its founding in 1995. Why? Because the capabilities of the abandoned languages failed to meet eBay’s needs and requirements as the business grew.

## How to Anticipate the Sacrifice

Developers cannot possibly build to avoid the need for replacements altogether, and they shouldn’t focus on doing so. There are, however, steps you can take to plan for obsolescence.

### Build with replacement in mind

As Fowler stated, you can build code with the idea that it will require replacement in a few years. Outdated code will eventually become susceptible to malicious viruses that could result in browser hijacking or system slowdowns. 

This means that you need to consider in advance the code’s limitations, including performance and scalability, and other characteristics.

### Minimize sacrifice through modularity

As a general rule, it is easier to replace smaller pieces of code than it is to replace an entire structure. 

Just as you don’t need to spend the time and money to replace your entire roof if a shingle gets blown off, there is no need to completely rewrite the code for a system if revising one module will do. 

So building modular code results in an architecture [that is easier for developers](https://stackoverflow.blog/2021/03/08/infrastructure-as-code-create-and-configure-infrastructure-elements-in-seconds/) to modify as needed.

But modularity is not always an effective solution, and you should be aware of the limits of your code. Sometimes, replacing too many pieces can weaken a structure or make it unstable. 

In the same way, the more modules you replace in your existing code, the more opportunities there are for problems with the operation of the code as a whole. That is the dividing line between continued piece-by-piece updating and wholesale replacement.

### Maintain quality standards

Even when you intentionally decide to build code knowing you will sacrifice it in the near future, you should always continjue to strive to meet or exceed company quality standards. After all, the sacrificial architecture will still probably be in production. 

Needs may also change, eliminating the reasons that you planned to retire the code in the first place. Poorly designed or implemented code also [makes developers’ lives more difficult](https://www.freecodecamp.org/news/clean-coding-for-beginners/) when modifying the code. 

Poor documentation and code structure also hinder your ability to understand the connections between pieces of code, making replacements and updates more challenging. 

Poorly designed code can [also be a significant security risk](https://hostingdata.co.uk/online-privacy-guide/), perhaps allowing hackers to access private data that companies have invested so much to protect.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-180.png)
_[Image Source](https://www.altexsoft.com/blog/business/technical-documentation-in-software-development-types-best-practices-and-tools/)_

Quality is a mantra that must always be front-of-mind, even for disposable code.

## Sacrificing for the Greater Good

While it may sound trite to quote this common saying, sacrificing your code may indeed be for the greater good of your systems and your company in the long run. 

Judicious, proactive use of sacrificial architectures can help reduce time to market for new features. And, it can minimize how much effort it takes when an unplanned, large-scale replacement inevitably occurs.

