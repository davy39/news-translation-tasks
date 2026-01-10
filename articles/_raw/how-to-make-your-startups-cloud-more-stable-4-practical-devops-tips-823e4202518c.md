---
title: 'How to make your startup’s cloud more stable: 4 practical DevOps tips'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T16:47:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-startups-cloud-more-stable-4-practical-devops-tips-823e4202518c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qi_8eBa0Xe1vniGhxkDmGA.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ben Sears

  In the startup world, there is a balancing act when it comes to where you invest
  your time. I’ve been in many situations where, due to the need to ship an MVP, DevOps
  practices take a backseat.

  I consider this to be normal and not really...'
---

By Ben Sears

In the startup world, there is a balancing act when it comes to where you invest your time. I’ve been in many situations where, due to the need to ship an MVP, DevOps practices take a backseat.

I consider this to be normal and not really a bad thing because “MVP” should be “Minimal” , and most problems that are solved by good DevOps are not problems at such a small scale.

But here are a few things that should definitely be done (or at least considered). Because there aren’t many things worse in the startup world than having your cloud infrastructure go down.

![Image](https://cdn-media-1.freecodecamp.org/images/k305qMPtQ5JQ-YTmewSKZ4QMr3yDxxi4Lhso)
_It’s hard to find time for DevOps in a startup when there’s so much else to do_

### Tip #1: Schedule Backups of your data ?

This is a must for any startup that cares about having persistent data. You need to be automatically backing up your critical data or you risk losing more than just files, you also will lose customer trust which will impact your future growth.

I generally automate two types of backup methods when starting projects

#### Database backups

This generally takes the form of a scheduled script, like a cron job which runs every night and pushes a database dump somewhere on the cloud like a private S3 bucket. You can have more fancy solutions with some backup solutions but those tend to be more enterprise focused and will cost you a lot of time and money (not startup friendly) .

![Image](https://cdn-media-1.freecodecamp.org/images/xVaOSbJdAg94fofj9T705IRPpB8xOnY5ttfH)

#### Disk snapshots

When all else fails, if you have a copy of your disk you are generally going to be safe. Most major cloud providers have solutions in place that let you take disk snapshots on a schedule of your choosing, so try and avoid writing scripts that connect directly to the cloud api since you will be responsible for maintaining them.

#### ? ?Make sure to test your backup restore method or risk wh[at happened to GitLab w](https://about.gitlab.com/2017/02/01/gitlab-dot-com-database-incident/)here all 5 of their backup methods failed because they never tested the restoration??

### Tip #2: Set up monitoring and be alerted to problems ?️

Will you know when a server goes down or an app crashes due to running out of disk space? If not, you should consider fixing that problem (it doesn’t take too much time).

The simplest way to set up monitoring would usually be a cloud provider solution like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) or [GCP Stackdriver](https://cloud.google.com/monitoring/). You can set up metrics to monitor and have different kinds of alerts in response to those events occurring within your cloud infrastructure, for example getting an email when your disk is running low.

If you don’t want to go with a provdier’s solution — there are cloud agnostic options too that can monitor your cloud. Simple solutions exist such as scheduling [shell scripts that send emails](http://www.linuxjournal.com/content/tech-tip-send-email-alert-when-your-disk-space-gets-low) to run periodically, but a more comprehensive solution that gives you a dashboard view of your system is generally better and much more scalable. Options like [Blue Medora](https://bluemedora.com/) and [Solar Winds](https://www.solarwinds.com/) exist for enterprise private cloud but most startups need to save money, meaning turning to open source solutions such as [Countly](https://count.ly/).

All in all, I would recommend going with a cloud provider based solution as those are going to be guaranteed stable, easy to set up, and, at a startup’s scale are not going to cost you much extra.

### Tip #3: Move towards a CI/CD Pipeline ?

![Image](https://cdn-media-1.freecodecamp.org/images/u3t9eAehi-11vaS36FCSnYsIYtc94mPTGuoS)

One of the common struggles I see with startups is the process of releasing code. Many haven’t yet put the time into DevOps to develop a stable release pipeline, meaning that the code that gets pushed to version control is either manually tested, built, and released, which is both error prone as well as time consuming for your development team.

#### Continuous Integration — Ensuring changes are non-breaking

The point of continuous integration is to have a pipeline that gets kicked off every time code is ready to be committed.

![Image](https://cdn-media-1.freecodecamp.org/images/M-Dh7rZOrTVvpB7ExmQgrwq971QiOmVcPv5C)
_Continuous integration protects the stability of your codebase_

1. Code is committed into version control
2. An automation system like Jenkins creates a build of the application
3. Automated Tests are performed to validate that the system still works properly
4. Once all tests pass, the code is allowed to be added to the stable codebase
5. New code is now ready for deployment (this is where continuous deployment comes into play)

#### Continuous Deployment — Automating your releases to production

Continuous deployment starts after your continuous integration pipeline has done its job of validating new code wont break your build. This generally consists of creating a new production build just like what was done in the continuous integration stage and replacing the old build (Immutable infrastructure).

Technically, you can have continuous deployment without continuous integration, but the risks of doing so are great. You would basically be pushing untested code directly to customers (?B**AD?**)

#### **Where should you start when moving towards CI/CD? — Automated Testing!**

It’s no secret, most developers do not enjoy writing tests. They tend to need constant updating as applications evolve and are a large time sink, so naturally many startups will neglect writing tests because “MVP”.

If you don’t have a comprehensive test suite I would not bother thinking about CI/CD until this is remedied. As the testing coverage improves you will start to see major efficiency gains as you see less and less bugs in production. This is the point when you should move on to the other pieces of your CI/CD pipeline.

### Tip #4: Containerize your application ?

![Image](https://cdn-media-1.freecodecamp.org/images/Rl8fBg6SSZ2ixPA3NjmdWfzYRuFgfQ9HT1AB)
_Containers make it easy to create automated builds of applications_

Don’t be afraid of containers, while the technology itself is complex and hard to understand without a fundamental knowledge of kernals, taking advantage of them and converting apps to containers is really quite trivial.

It usually takes less than an hour to put together a Dockerfile (depending on your app’s complexity) and before you know it, you can deploy your app instantly and take advantage of great systems such as Kubernetes.

Here are some benefits you can gain immediately by containerizing your application.

#### **Consistent Builds**

No more “it works on my machine” problems — If the container builds, it will run on any machine the same way.

#### **Pain-free Deployments**

You know how when you want to set up an open-source project you have to go through all kinds of manual steps, setting up databases and installing package that are required? With containers this is no longer the case, all those steps are baked into the build process and all you need to do is run a single command to start up your servers.

#### **A Vibrant Container Ecosystem**

Container platforms like Docker and Kubernetes have a very large and growing ecosystem of products and services to help you manage your applications easier. A lot of headache around things like storage, networking, and resource allocation are basically eliminated saving you time and money.

### Conclusion

Many startups don’t put much thought or time into their cloud infrastructure. This is generally due to MVP philosophy of shipping first and cleaning up technical debt afterwards.

When looking to scale up your DevOps infrastructure — consider scheduled backups, monitoring, CI/CD and containerization. These are generally easy wins and will lead to a much more stable cloud.

### Want to scale your cloud infrastructure? [ServiceBot can help](https://servicebot.io?ref=medium3).

