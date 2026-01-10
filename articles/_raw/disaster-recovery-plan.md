---
title: How to Create a Disaster Recovery Plan for your IT Team
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-05-14T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/disaster-recovery-plan
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b09740569d1a4ca2952.jpg
tags:
- name: insertone
  slug: insertone
- name: Disaster recovery
  slug: disaster-recovery
- name: incident management
  slug: incident-management
- name: RPO
  slug: rpo
seo_title: null
seo_desc: "You know the old joke: there are two kinds of companies, those that've\
  \ been hit with IT disaster, and those who don't yet realize they've been hit with\
  \ IT disaster. \nBut what they all have in common is that there are plenty more\
  \ disasters to come. So..."
---

You know the old joke: there are two kinds of companies, those that've been hit with IT disaster, and those who don't yet realize they've been hit with IT disaster. 

But what they all have in common is that there are plenty more disasters to come. So ask yourself whether you're ready for the next one.

This article, which is based on my [Pluralsight course, Linux System Maintenance and Troubleshooting](http://pluralsight.pxf.io/VMKQj), is intended to start you thinking about what building an effective protocol will take.

## What you need to have in place

It all begins with the **business continuity plan** (BCP). This is a formal plan that's meant to define the procedures an organization would use to ensure survival in the event of an emergency. 

BCPs will generally include sub-plans to secure the immediate safety of employees and customers, work to restore previously-designated critical operations as soon as possible and, eventually, to restore full normal operations. 

In addition, an effective BCP will also include two sub-plans that are specific to IT operations: the incident management protocol and disaster recovery plan.

The **disaster recovery** **plan** (DRP) aims to protect an organization's IT infrastructure in the event of a disaster. Its primary goals are to minimize damage and to restore functionality as quickly as possible. 

The reason we call this a "plan" is because it simply won't work without serious prior preparation. Infrastructure protection, threat detection, and corrective protocols are critical parts of the plan.

An **Incident Management Plan** (IMP) is meant to address the specific threat of cyber attacks against IT infrastructure. Its goals are to minimize damage and remove the threat. 

As you can easily tell, there will be some overlap between your DRP and IMP. But the key focus of disaster recovery is to get your infrastructure back on its feet, while incident management is much more closely aligned with the world of IT security.

For the rest of this short article we're going to look at what goes into creating incident management and disaster recovery plans and how to ensure that your plan is sound and should, when executed, actually work.

## Developing an Incident Management Protocol

Since incident management is going to be your first response to trouble, we'll begin there. 

The first indication that there's trouble can come from a user who notices that something's not right with the system. Or, if you've done a particularly good job configuring your infrastructure, it could also come to you in the form of an automated alert triggered by monitoring software.

When that alert comes in, it'll be the job of the technician or admin on call to decide how it's going to be handled and who has to handle it. 

Escalation can happen through a direct phone call or email, a ticket submitted through a collaboration tool like Jira, or by using a purpose-built Security Information and Event Management (SIEM) tool.

Again, though, the more smart automation you build into the process, the faster and more efficient it's likely to be. 

Whoever ends up with the ultimate responsibility will coordinate efforts to definitively diagnose and resolve the problem. Ideally, where necessary, such coordination will include admins, developers, and other key stakeholders to ensure you've got all the resources you'll need to address the problem.

When it's all over, once you've confirmed the problem is resolved, you'll want to close the incident by assessing what went wrong and what went right, how your response could have been better, and how you can rework things to reduce the risk of a repeat of the incident.

But what does all this have to do with IT administration? Well, responsible IT managers must be able to build resiliency into their infrastructure. 

That will mean spending serious time fine-tuning their software monitoring systems so they'll catch and alert you to real problems while issuing alerts for as few false positives as possible. 

And it'll probably also involve intelligently automating logging and intrusion detection systems and generally getting a good idea of how things are supposed to look.

## Developing a Disaster Recovery Plan

Disaster recovery planning requires you to:

* Define exactly what recovery means
* Identify the resources that achieving recovery will require
* Convert those observations into a formal plan format
* Communicate the plan to the players who will one day have to carry it out

What does **recovery** mean? It's when your poor, stricken infrastructure has returned to the shape it was in the moment before disaster hit. 

What you'll need to get you back to that point can be defined by establishing a **Recovery Time Objective** (RTO) and **Recovery Point Objective** (RPO) that fits your organization's needs.

A **Recovery Time Objective** represents the maximum number of minutes, hours, or days that your organization could survive an IT service outage. So your recovery plan will need to incorporate that hard deadline into its protocols.

Of course that means you'll need to have team members available to make it into the office even in the small hours of the night quickly enough to make a difference. 

But it also means, say, that if your RTO is six hours, but restoring critical data from your backups would take a minimum of eight hours just to handle the transfer, then you'll have to rethink those numbers before signing off on the plan.

A **Recovery Point Objective** is the amount of transaction data your organization could afford to lose during an outage and survive. 

To illustrate, an e-commerce website that normally processes 25 transactions each minute could, perhaps, afford to issue apologies and refunds to 30 minutes worth of angry customers wondering why their credit cards were billed but their electric train sets weren't delivered. Refunding more than 30 minutes worth, however, could deplete your financial reserves to the point that you're no longer viable.

In any case, calculating accurate and reliable RTOs and RPOs is how you set the limits within which your recovery plan will have to operate. Or, in other words, you'll have defined what recovery means.

Now what about **resources**? By which I mean the data backups and, when necessary, the physical equipment you'll need to get your application back on its feet. 

To make that work you'll have to decide on an infrastructure backup system. Whether you choose to go with incremental or differential, on-site or off-site, and single or multiple media types, you'll have to map out exactly how the recovery will go and whether or not it'll meet your RTO and RPO limits.

Of course there's no end of really bad things that can happen to make those plans utterly useless. What if your local server facility just burns down? What if it's lost to some kind of political upheaval or widespread power disruption? 

Even if you've conscientiously maintained up-to-date data backups off-site, what good will they do you if your hardware effectively no longer exists?

Thinking about all those horrors can make preparing a cloud-based backup protocol using platforms like AWS and Azure sound mighty attractive. The big public clouds have the resources to distribute their infrastructure widely enough that it's virtually impossible for the whole thing to ever go down.

So you could, for instance, maintain a reliably replicated data store on a public cloud platform that mirrors your main deployment. You could also design an infrastructure template that could be loaded up with your backup data and then launched on demand to take over in the event of an outage. Because nothing is kept running until it's actually needed, it can take a good few minutes to bring this one up to speed.

A warm standby recovery design might maintain your data running 24/7 on a minimal number of virtual servers. In an emergency, you can hit the switch and the platform's auto scaling will fire up all the instances you'll need. 

You could set the scaling to kick in when triggered by an alert from your primary system. The public cloud presents endless possibilities, but they all require planning and preparation.

A solid disaster **recovery plan** must be effectively communicated long before crunch time. Practically speaking, that means it'll all be written up, printed, and distributed to each of the key players who will carry out the plan. 

That's not to say it ends there: those players will of course have actually read the thing and, ideally, engage in realistic simulations until they're confident they can make it work under pressure.

What goes in this book?

* An enumeration of all the stuff that could go wrong and bring down your system
* An inventory of exactly what you've got running in your server room and what would be needed to replace it
* The information you'll need to access and restore backed up data
* An up-to-date contact list of the people who will be responsible for every aspect of the plan
* The exact sequence of the tasks and events that will make up the recovery

That's a lot of detail. But it's barely a drop in the bucket when compared with the total amount of preparation and plain old hard work that goes into creating a real-world recovery plan. 

But for now, the key takeaway from this module is simply to keep all this in mind. Why? Because the next time you sit down to configure a monitoring package or administration framework, you'll think about incident management protocols and disaster recovery plans and wonder how you should include them in your configuration.

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com/)._

