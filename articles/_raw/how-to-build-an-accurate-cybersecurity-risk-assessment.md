---
title: How to Build an Accurate Cybersecurity Risk Assessment
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-05-10T19:39:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-accurate-cybersecurity-risk-assessment
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-jonathan-petersson-965879.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
seo_title: null
seo_desc: "Are you responsible for the safety and reliability of IT infrastructure\
  \ and applications? You'll absolutely need regular and accurate assessments. \n\
  Effective risk assessments are about establishing how far your organization's IT\
  \ stack can be stretche..."
---

Are you responsible for the safety and reliability of IT infrastructure and applications? You'll absolutely need regular and accurate assessments. 

Effective risk assessments are about establishing how far your organization's IT stack can be stretched before it breaks. 

From a big-picture perspective, you'll need to think about how likely you are to be hit by, say, a ransomware event that may leave your business servers unusable for a few weeks – and how much that would cost you in terms of revenue losses and mitigation costs. 

This article comes from my [Introduction to Cybersecurity course](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). If you'd like, you can follow the video version here:

%[https://www.youtube.com/watch?v=7JfuMdevhu4&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

Against that you might measure the up-front and ongoing costs associated with backups and system hardening efforts. That'll tell you how much you can actually afford, and also how urgently you should work to develop an overall defense plan.

You'll also want to get some sense of how interdependent your systems are: if, for example, your public-facing web applications were to go down, would that impact your back-end payroll and inventory systems as well? 

Do you have enough engineers available across your organization who could be pulled out of their normal work to cover for an emergency? Might you be subject to legal liabilities and expensive lawsuits as a result of an outage? 

At what point would the damage from a major outage be so great as to threaten the ongoing viability of your operations?

That last point is worth diving into a bit deeper. As it turns out, the IT admin world has developed some particularly useful metrics for measuring your organization's base needs, and anticipating the steps you'll need to take to ensure those needs are met. 

I know this list looks like a bit of an alphabet soup, but it'll be worth our time to at least briefly talk about each of these concepts.

* RPO: Recovery Point Objective
* RTO: Recovery Time Objective
* MTTR: Mean Time to Recovery
* MTBF: Mean Time Before Failure
* MTTF: Mean Time to Failure

### Recovery Point Objective (RPO)

The **recovery point objective** measures how much data loss you could sustain before full recovery becomes impossible. We're looking backwards here from the moment you restore operations. 

The point is that the world has continued spinning while your servers were sleeping. Customers were trying to access your site, but were unable to complete transactions. 

That represents a financial loss. But there might also have been existing customers who were actively using local versions of your application without realizing that the data they were generating wasn't being properly captured by your back-end.

So _you_ want to know approximately how much data and revenue would you normally process in an hour, and how many hours' worth of data and revenue you could afford to lose. With that number, you'll be in a position to figure out how quickly your response and recovery plan will need to work to be useful.

### Recovery Time Objective (RTO)

That brings us to the **recovery time objective**: how long it will take you to go from a failed state to fully restored operations. 

If your RTO estimates for a particular outage type are, say, 12 hours, but your recovery _point_ objective is only six hours, then you've got a problem. What's the use of an expensive recovery plan if you already know that your business will be dead and buried by the time it completes? 

If that's what your numbers tell you about your current expensive recovery plan, then you'd better start working on a _more_ expensive – or more efficient – recovery plan.

### Mean Time to Recovery (MTTR)

If the RTO is a way of quantifying your **target** response time for a single hypothetical disaster event, the **mean time to recovery** gives us a sense of how your technology will actually behave in the real world. 

Your MTTR might be at least partly based on the performance guaranties provided by the vendors who supply the various hardware and software components that make up your stack. But I'd guess it'll primarily depend on the performance history of your emergency teams. 

Again: an MTTR that's longer than your RPO is a signal that you need to give this some attention.

Besides those metrics, it can also be helpful to think about failure. Of course, I don't mean how nasty things might get if you're the one who lets the rasomware attack authentication through. It might not be healthy to spend too much time obsessing over that one. Rather, I mean thinking about how _often_ your systems are likely to fail.

Some failure events aren't hard to predict. You know, for instance, that you'll need to completely replace your servers running Ubuntu 20.04 by the end of its [hardware and maintenance update lifetime in April 2025](https://ubuntu.com/about/release-cycle). 

Unless, that is, you opt for an extended Security Maintenance option, in which case you'll get until April, 2030. Similarly, you can be reasonably certain that heavily-used data drives will start failing after a few years of service.

But malware events don't happen on a schedule. And, perversely, they tend to erupt on long weekends or in the middle of the night. 

Here, you'll need to work with publicly-available incident data from governments and security companies. Given how many breaches go unreported, even those numbers will probably not get you too close to the real picture.

The goal will be to estimate how long your _peer_ organizations go between major events. A "peer organization" is an organization that's largely similar to you in measures like size and industry type. In that context, the mean time _before_ failure is generally used to measure recovery times from _repairable_ failures. This can help you understand your tech stack – and particularly how each layer will work under stress within the whole.

### Mean Time to Failure (MTTF)

By contrast, the **mean time _to_ failure** focuses on _un_repairable failures that require full component or system replacement. By and large, the MTTF will be the metric that's the most interesting in the context of attack threats.

There'll obviously be some guessing with all this, but it's critically important to develop at least some informed sense of how you're likely to perform when things go crazy and how prepared you actually are to business continuity challenges.

## Wrapping Up

Having even a basic grasp of the processes and metrics behind the RPO, RTO, MTTR, MTBF, and MTTF acronyms we've discussed here should give you a decent chance at successfully fighting back against the chaos.

This article and the accompanying video are excerpted from [my](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2) **[Introduction to Cybersecurity course](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2).** And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com)

