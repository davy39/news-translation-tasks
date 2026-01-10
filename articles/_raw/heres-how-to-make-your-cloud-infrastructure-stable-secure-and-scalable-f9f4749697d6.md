---
title: Here’s how to make your cloud infrastructure stable, secure, and scalable.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-22T08:57:18.000Z'
originalURL: https://freecodecamp.org/news/heres-how-to-make-your-cloud-infrastructure-stable-secure-and-scalable-f9f4749697d6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eQuZJgwAnOfLXTag0G2NHA.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ben Sears

  Startup DevOps is hard

  There are a lot of things to worry about as a startup. Marketing, product development,
  keeping your team together. Everything tends to take the “Minimum viable” pattern
  of getting the bare minimum up so you don’t c...'
---

By Ben Sears

### Startup DevOps is hard

There are a lot of things to worry about as a startup. Marketing, product development, keeping your team together. Everything tends to take the “Minimum viable” pattern of getting the bare minimum up so you don’t crash and burn.

As an enterprise cloud architect, I know first hand how much work can be done in the field of DevOps. As a startup founder, I also know how little time you have to spend on things — it’s more like you have to spend time on all the things at once.

Cloud Infrastructure unfortunately also tends to follow this rule, and all the “best practices” in the field tend to follow patterns that require a large amount of time investment, something startups definitely don’t have.

With this guide, I hope to give you an overview of what a “minimum viable cloud infrastructure” can look like, with a focus on stability, security, and scalability.

### Stability ?

When looking at the stability of your cloud infrastructure, there are a few key points to focus on when developing minimum viable cloud infrastructure. Restoring from catastrophic failure, automatic restart, and making sure there are enough resources available. If you focus on these three things, you should be in a pretty good place in terms of your uptime.

![Image](https://cdn-media-1.freecodecamp.org/images/sHwS78xWfPUSKQ258Sz-O4cn6CzJ7fDoBltn)

#### Restoring from catastrophic failure (Automatic Backups)

You know the worse case scenario — you bricked your server and disk. The minimum viable solution to this is to have scheduled, automated backups taken so you prevent data loss.

Depending on your cloud provider, there are a few different options you can take. Snapshotting disks is generally the simplest way to do a minimum viable backup process, but more advanced (and more stable) methods include database specific backups (dumping the database) and distributed systems.

* **AWS**  
If you are using Amazon, I would recommend using CloudWatch. It lets you create scheduled jobs (such as automatic snapshots) — [See this guide](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/TakeScheduledSnapshot.html)
* **GCP**  
Google allows you to schedule snapshots as well — [See this guide](https://cloud.google.com/compute/docs/disks/create-snapshots)
* **Cloud Agnostic**  
Don’t want to lock your backup process to your cloud provider? Your most important data will be the database and any uploads that may be provided. For a database, you should look to write a script that periodically dumps the database and sends the data to a secure location (private s3 bucket, distributed file system, etc.) This will be more prone to error than a platform specific method, however, so be wary.

![Image](https://cdn-media-1.freecodecamp.org/images/bZcnQNF1mZvbaJy2ZIh7udvZA-Rq02vPEPD8)

### ? **?**Ma**ke sure to test your backup restore method or risk wh[at happened to GitLab,](https://about.gitlab.com/2017/02/01/gitlab-dot-com-database-incident/) w**here all 5 of their backup methods failed because they never tested the restoration.??

#### Automatic service restarting in case of server reboot

There are two parts to automatic restarting. One, when your app crashes, does it start up again? And two, when your server reboots, does your app start up automatically?

**Crontab** —Crontab is a useful tool that lets you schedule jobs easily. Perhaps the simplest approach to auto-start your stack is to create a crontab job that gets run on reboot — [See this guide on how to do that](https://www.cyberciti.biz/faq/linux-execute-cron-job-after-system-reboot/).

**/etc/init.d** — Most systems support init.d scripts. With init.d you can define scripts which can be started at boot and also support **stop, start, and status** commands (eg. `service start myscript`) to give you more control over your applications. It’s a bit more complex than a crontab, but it gives you more features — [See this post to set up an init.d script](https://unix.stackexchange.com/questions/20357/how-can-i-make-a-script-in-etc-init-d-start-at-boot).

If you are interested in the differences between these methods, check out [This stack exchange post](https://unix.stackexchange.com/questions/188042/running-a-script-during-booting-startup-init-d-vs-cron-reboot).

#### Automatic service restarting in case of application crash

Applications are not always stable and can be prone to crash at awkward times. A good way to maintain stability is to have a tool which can automatically restart.

* NodeJS — [Forever](https://github.com/foreverjs/forever) or [PM2](https://github.com/Unitech/pm2)
* General — [Check this post on how to restart processes using bash scripts](https://stackoverflow.com/questions/696839/how-do-i-write-a-bash-script-to-restart-a-process-if-it-dies)

#### Always ensure there are enough resources available

One of the most common reasons for server downtime is servers running out of resources. I’ve had SQL servers die from running out of disk space and production applications die from running out of memory. Setting up monitoring of resources is a good way to mitigate this risk.

* **AWS** — [CloudWatch](https://aws.amazon.com/cloudwatch/) is a good tool for monitoring. You can set up email alerts on specific events.
* **GCP** — [Stackdriver monitoring](https://cloud.google.com/monitoring/) provides similar functionality, and also integrates with messaging systems like Slack.
* **Cloud Agnostic** — Crontab is good again for this kind of task, but you will need to write a script which will check system resources and send emails when they reach your threshold.

### ??Make sure to document your auto-start method and boot scripts. Keep code in version control or you will risk trouble when it comes to scale due to mystery code you forgot about.??

### Security ?

Security is unfortunately overlooked when it comes to MVP philosophy. People just don’t see the value gained for the time investment needed. This is a form of dangerous gambling, as a security breech could cause severe loss of data, customer trust, and time. Here are some basic things you can do to get started with a security mindset.

#### SSL

Nowadays, SSL is basically a requirement for a modern SaaS app with many users refusing to use applications without https support. Tools like [Let’s Encrypt](https://letsencrypt.org/) make getting certificates easy and free.

![Image](https://cdn-media-1.freecodecamp.org/images/64MZulnr1GS6W7wXNym7C6qPZWcKOqNzBtLq)

#### Server Security

One of the most important things when it comes to security is managing servers properly. Here are a couple basic tips you should be keeping in mind.

* Databases should not be accessible to the open internet.
* Keep applications and operating system up to date. There are often security updates which protect your server from new vulnerabilities.
* Close all ports except those that are absolutely necessary.
* Do not use username/passwords — using keys is much more safe.
* Do not give people the root key when they need access to your server. Make new accounts and have them give you their public key.

#### Secret Management

API keys, credentials, configurations, and all sensitive data needs to be managed. I’m always hesitant when placing this kind of data on the cloud, not only because I don’t know what the cloud provider can look at, but also because if they get my account, all my secrets become exposed.

* Keep as many secrets local as possible.
* Don’t hardcode secrets into your application — create configuration files you can store outside of app code.
* Don’t store secrets in a public Github repo (be wary of the cloud in general).
* Avoid plaintext when storing user passwords and your own secrets

### Scalability ?

### ??In most cases when it comes to scalability, Y**o[u Aren’t going to need it (](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)when starting out).??**

If you have the time, the will, and the skills (or money), putting some effort into scalability could give you future benefits. If not, I’d recommend ignoring it and focusing on the previous two points.

Focus on delivering your product to your first 5 customers, not your first 1,000. The best you can do when it comes to building scalable infrastructure is think about design principals while building your app so it wont be too much work to get going when it’s finally time to scale. I should know — I’ve fallen for the over-engineering trap many, many times.

#### Containerization

![Image](https://cdn-media-1.freecodecamp.org/images/-lKBBoCdygIIPz263C-rOmkTkHOIKKOCcMh9)
_Tools like Docker and Kubernetes are great for scaling_

An easy win when it comes to scaling is to containerize your application. Check out Docker for a good guide. Here are some tips:

* Allow configuration of your app via environment variables. Things like database info and initial admin username/password will go a long way when it comes to building a CI/CD pipeline and automating your app deployment.
* Keep as much state out of your container as possible. This will allow for stateless deployments via tools like Kubernetes.
* Install your modules as part of the build process to reduce dependencies and image size.

#### Keep your servers’ configurations well documented

Store everything in version control: configurations, scripts, and procedures to prepare servers. This will save you when it comes to scaling. I’ve had to deal with scaling apps that require servers configured in a very particular way, and if the documentation is lacking you will be in for a hell of a time.

### Conclusion

There is a lot of work involved with standing up and maintaining cloud infrastructure. Startups have it hardest because they have no time, and often, their skillset is lacking when it comes to DevOps. What you can do is focus on the essentials. Security, Stability, and if you have the time, Scalability.

#### [ServiceBot](https://servicebot.io?ref=medium) helps you scale your SaaS by automating deployments (CI/CD), managing your subscriptions, and removing common points of friction between you and your customers. [Check it out](https://servicebot.io)

