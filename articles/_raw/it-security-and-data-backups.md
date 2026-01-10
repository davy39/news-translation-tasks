---
title: Why Backing Up Your Data Is Important for IT Security
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2021-01-06T18:55:04.000Z'
originalURL: https://freecodecamp.org/news/it-security-and-data-backups
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/backup-recovery.jpg
tags:
- name: Backup
  slug: backup
- name: cybersecurity
  slug: cybersecurity
- name: data
  slug: data
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: 'Early one recent morning my Linux workstation failed to boot. And just
  like that, all my work plans for the day ground to an immediate halt.

  This was the Linux workstation that was host to thirty years-worth of data: The
  original working drafts of al...'
---

Early one recent morning my Linux workstation failed to boot. And just like that, all my work plans for the day ground to an immediate halt.

This was the Linux workstation that was host to thirty years-worth of data: The original working drafts of all my books. The master versions of my course videos. My tax records, banking information, password vault, and the access keys to my cloud infrastructure.

Was I surprised? Not particularly. The day before I’d been struggling with a broken Python package and I knew there was a chance it wouldn’t end well the next time I fired up the machine.

Was I annoyed? Yup.

Did I break into a cold sweat, thinking about what was lost and whether I’d ever recover? Nope. That was never a concern. 

In fact, from the moment I decided that the original installation was no longer worth fighting for, it would only take an hour or so to get everything back up and running. (Not counting the time it took me to remember that a known hardware conflict required I disable a non-free Nvidia driver.)

Let me emphasise that: I erased the corrupted drive, installed a clean copy of Ubuntu Linux, and wrote fresh, reliable copies of around 20GB of data to the new installation in less than a single hour.

Besides having a fast fibre optics internet connection, what’s my secret sauce? I’m constantly backing up all my important data to multiple storage locations. When catastrophe hits, I have a solid, tested recovery protocol in place. 

For all intents and purposes, the workstation part of that protocol involves installing my OS and then, with just two or three commands, restoring all my data to its new home. From that moment, I’ll be back to work.

I’m sure this story has left you overcome with relief and warm, sympathetic feelings. But what’s it all got to do with IT security? More than you might imagine. 

The fact is that there many reasons backup discussions belong here, but if you had to limit yourself to just one, this common and timely scenario (adapted from my recent “[Linux Security Fundamentals” book from Wiley/Sybex](https://www.amazon.com/dp/1119781469)) would be it:

> _Imagine you’re responsible for the IT systems powering the municipal services for your small town. Without those computers and their data, municipal workers won’t get paid next month, the local library won’t know where any of their books are, the 911 emergency service communication system’s phones won’t ring, and the town’s information website will go offline._

> _Now imagine that one fine morning you log into the main server and you’re greeted by the cheerful news that all the data on your systems has been encrypted by a hacker from Eastern Europe and that they won’t give you the decryption key to restore your access unless you pay them a couple hundred thousand dollars’ worth of cryptocurrency. Don’t think this is realistic? Major hospitals, utilities, and entire small cities have been brought to their knees by just such attacks._

> _What are your choices?_

* _You could pay the ransom and hope the attackers keep their promise to decrypt your data. But, historically, they often haven’t. Criminals aren’t known for being honest._
* _You could try using decryption tools provided by major security companies and government agencies (like_ [_https://noransom.kaspersky.com/_](https://noransom.kaspersky.com/) _) and hope that they’ll work on your system. This is certainly a valid option, but it won’t work in all cases._
* _You could wipe your systems clean and rebuild everything from scratch. This could be hugely expensive and take months to complete._

> _But do you know how you can stop the attack cold and walk away virtually untouched? If you had complete, up-to-date backup copies of your systems (both the user data and the application systems themselves), then all you’ll need to do is rebuild from your backups._

> _Worst case, you’re down for an hour or two, and few people even notice. Even better, you could plan things really well by designing an always-running “hot” backup infrastructure that’s preconfigured to go live the minute the main system goes down. It’s known as failover, and it’s the kind of plan that can make you a big hero and earn you a big raise._

> _Still not sure what backups have to do with security?_

That Linux Security Fundamentals book also describes how to properly assemble all the parts your recovery plan will need. That’ll include a careful assessment of precisely how important your data is to both you and the organization you work for. 

Here’s how my book describes RTOs and RPOs:

> _How “quick” is quick enough and how “complete” is complete enough? That will depend on your organization’s operational needs. It’s common for administrators to measure their needs in terms of a recovery point objective (RPO) and recovery time objective (RTO). An RPO is the system state you need to be able to recover that will be current enough for your organization’s minimum requirements. So, for instance, if your recovered system will have data that includes all but the last hour preceding the crash, you’ll be able to get by. But a loss of two hours of data would be catastrophic; the financial or reputation loss you’d face would be too serious. For such an organization, you’d better make sure you have an RPO of one hour or less._

> _An RTO, on the other hand, is a measure of how soon you need to get your system back up and running at full speed before really bad things start happening to your organization._

> _By way of example, suppose your ecommerce site was offline for 12 hours. You’ll lose some business, obviously, but your business analysts tell you that anything up to 48 hours is still livable. More than 48 hours, however, and customers will assume you’re down for good and head over to the competition (which, all things being equal, will be Amazon)._

> _Therefore, when you plan your backup regimen, you’ll take both the RPO and the RTO into account. You’ll need to make sure a new backup is run within the RPO (say, one hour) and also make sure you can access your backup archives and successfully restore the data to the applications in less than the RTO (48 hours, in our example)._

Sure, RTOs and RPOs are usually applied to enterprise infrastructure workloads. But, on many levels, the underlying point can also apply to our own beloved workstations and laptops.

If you take some time now — today — to plan, create, and test your own recovery protocol, you can be sure that one day soon, you’ll thank yourself.

_You can find much more technology content by_ [_David Clinton through his website._](https://bootstrap-it.com/davidclinton) _In particular, you might enjoy his new book,_ [_Keeping Up: Backgrounders to all the big technology trends you can’t afford to ignore_](https://www.amazon.com/gp/product/B08HL9WQ1H/)_._

