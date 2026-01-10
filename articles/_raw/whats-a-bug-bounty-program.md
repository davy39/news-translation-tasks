---
title: What is a Bug Bounty Program? How Bug Bounties Work and Who Should Use Them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-07T18:30:50.000Z'
originalURL: https://freecodecamp.org/news/whats-a-bug-bounty-program
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/pexels-pixabay-35804.jpg
tags:
- name: bug bounty
  slug: bug-bounty
- name: cybersecurity
  slug: cybersecurity
- name: '#infosec'
  slug: infosec
- name: penetration testing
  slug: penetration-testing
seo_title: null
seo_desc: 'By Megan Kaczanowski

  Bug bounty programs allow independent security researchers to report bugs to an
  organization and receive rewards or compensation. These bugs are usually security
  exploits and vulnerabilities, though they can also include process ...'
---

By Megan Kaczanowski

Bug bounty programs allow independent security researchers to report bugs to an organization and receive rewards or compensation. These bugs are usually security exploits and vulnerabilities, though they can also include process issues, hardware flaws, and so on.

The reports are typically made through a program run by an independent third party (like Bugcrowd or HackerOne). The organization will set up (and run) a program curated to the organization's needs. 

Programs may be private (invite-only) where reports are kept confidential to the organization or public (where anyone can sign up and join). They can take place over a set time frame or with no end date (though the second option is more common).

## Who uses bug bounty programs?

Many major organizations use bug bounties as a part of their security program, including AOL, Android, Apple, Digital Ocean, and Goldman Sachs. You can view a list of all the programs offered by major bug bounty providers, [Bugcrowd](https://www.bugcrowd.com/bug-bounty-list/) and [HackerOne](https://www.hackerone.com/), at these links.

## Why do companies use bug bounty programs?

Bug bounty programs give companies the ability to harness a large group of hackers in order to find bugs in their code. 

This gives them access to a larger number of hackers or testers than they would be able to access on a one-on-one basis. It can also increase the chances that bugs are found and reported to them before malicious hackers can exploit them.

It can also be a good public relations choice for a firm. As bug bounties have become more common, having a bug bounty program can signal to the public and even regulators that an organization has a mature security program. 

This trend is likely to continue, as some have started to see bug bounty programs as an industry standard which all organizations should invest in. 

## Why do researchers and hackers participate in bug bounty programs?

Finding and reporting bugs via a bug bounty program can result in both cash bonuses and recognition. In some cases, it can be a great way to show real-world experience when you're looking for a job, or can even help introduce you to folks on the security team inside an organization. 

This can be full time income for some folks, income to supplement a job, or a way to show off your skills and get a full time job. 

It can also be fun! It's a great (legal) chance to test out your skills against massive corporations and government agencies.

## What are the disadvantages of a bug bounty program for independent researchers and hackers?

A lot of hackers participate in these types of programs, and it can be difficult to make a significant amount of money on the platform. 

In order to claim the reward, the hacker needs to be the first person to submit the bug to the program. That means that in practice, you might spend weeks looking for a bug to exploit, only to be the second person to report it and make no money. 

R[oughly 97% of](https://www.cyberscoop.com/bug-bounty-pen-testing-hackerone-synack-bugcrowd/) participants on major bug bounty platforms have never sold a bug. 

In fact, a [2019 report](https://www.cyberscoop.com/bug-bounty-pen-testing-hackerone-synack-bugcrowd/) from HackerOne confirmed that out of more than 300,000 registered users, only around 2.5% received a bounty in their time on the platform. 

Essentially, most hackers aren't making much money on these platforms, and very few are making enough to replace a full time salary (plus they don't have benefits like vacation days, health insurance, and retirement planning). 

## What are the disadvantages of bug bounty programs for organizations?

These programs are only beneficial if the program results in the organization finding problems that they weren't able to find themselves (and if they can fix those problems)! 

If the organization isn't mature enough to be able to quickly remediate identified issues, a bug bounty program isn't the right choice for their organization. 

Also, any bug bounty program is likely to attract a large number of submissions, many of which may not be high-quality submissions. An organization needs to be prepared to deal with the increased volume of alerts, and the possibility of a low signal to noise ratio (essentially that it's likely that they'll receive quite a few unhelpful reports for every helpful report).

Additionally, if the program doesn't attract enough participants (or participants with the wrong skill set, and thus participants aren't able to identify any bugs), the program isn't helpful for the organization. 

The vast majority of bug bounty participants concentrate on website vulnerabilities (72%, according to HackerOn), while only a few (3.5%) opt to look for operating system vulnerabilities. 

This is likely due to the fact that hacking operating systems (like network hardware and memory) requires a significant amount of highly specialized expertise. This means that companies may see significant return on investment for bug bounties on websites, and not for other applications, particularly those which require specialized expertise.

This also means that organizations which need to examine an application or website within a specific time frame might not want to rely upon a bug bounty as there's no guarantee of when or if they receive reports.

Finally, it can be potentially risky to allow independent researchers to attempt to penetrate your network. This may result in public disclosure of bugs, causing reputation damage in the public eye (which may result in people not wanting to purchase the organizations' product or service), or disclosure of bugs to more malicious third parties, who could use this information to target the organization.

## Is a bug bounty program right for every organization?

No. An organization needs to reach a certain level of maturity in their security program before a bug bounty program can be effective. 

The biggest question an organization needs to ask is whether or not they will be able to fix any identified vulnerabilities. If they can't do so within a reasonable amount of time, a bug bounty program probably isn't a good idea. 

If the organization is struggling to implement basic patch management or they have a host of other identified problems that they are struggling to fix, then the additional volume of reports which a bug bounty program will generate is not a good idea. 

A bug bounty program becomes a good idea when there is not a backlog of identified security issues, remediation processes are in place for addressing identified issues, and the team is looking for additional reports. 

Additionally, as I mentioned earlier, while websites are usually good targets for bug bounty programs, a highly specialized target, such as network hardware or even operating systems, may not attract enough participants to be worthwhile.

Finally, the amount of money or prestige afforded by successfully submitting a report for different organizations may impact the number of participants and the number of highly skilled participants (that is, reporting a bug for Apple or Google may carry more prestige than a bug for a company which isn't as well known).

## What are the alternatives to bug bounty programs?

First, organizations should have a vulnerability disclosure program. Essentially, this provides a secure channel for researchers to contact the organization about identified security vulnerabilities, even if they do not pay the researcher. 

Having an identified point of contact can be helpful as it can immediately filter requests to the security team, rather than a communications team which may not know how seriously to treat the report. It can also encourage researchers to report vulnerabilities when found. 

Typically this also includes a framework for how to handle intake, mitigation, and any remediation measures.

Additionally, organizations may opt to hire a penetration testing firm to perform a time-limited test of specific systems or applications. The pen testers will have a curated, directed target and will produce a report at the end of the test. 

This will ensure that the company gets a team of highly skilled, trusted hackers at a known price. They can also request any specialized expertise which they need, as well as ensuring the test is private, rather than publicly accessible. 

The company may even have the testers sign non-disclosure agreements and test highly sensitive internal applications. 

However, this is typically a single event, rather than an ongoing bounty. Also, penetration testers are paid whether or not they find any vulnerabilities (whereas in a bug bounty the researchers are only paid if they successfully report a bug). 

## Which is better – bug bounty programs or hired penetration testers?

Often these two methods are not directly comparable - each has strengths and weaknesses. 

If the organization would benefit more from having more people (of varying skill levels) looking at a problem, the application isn't particularly sensitive, and it doesn't require specific expertise, a bug bounty is probably more appropriate. 

If the application is internal/sensitive, the problem requires specific expertise, or the organization needs a response within a specific time frame, a penetration test is more appropriate. 

Interested in learning more about bug bounties?

* [HackerOne has an introductory course to help folks get into bug bounties](https://www.hacker101.com/).
* Here's an interview with [Katie Moussouris, one of the biggest names in Bug Bounties](https://www.theverge.com/2020/7/7/21315870/cybersecurity-bug-bounties-commercialization-katie-moussouris-interview-vergecast-podcast).


