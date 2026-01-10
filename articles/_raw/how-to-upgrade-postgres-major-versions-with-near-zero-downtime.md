---
title: How to Upgrade Postgres Major Versions with Near-Zero Downtime – a Practical
  Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-15T21:42:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-upgrade-postgres-major-versions-with-near-zero-downtime
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Listen-Score-loves-postgres.png
tags:
- name: database
  slug: database
- name: postgres
  slug: postgres
seo_title: null
seo_desc: "By Wenbin Fang\nIt's impossible to create zero-downtime Postgres upgrades\
  \ across major versions – right? Please, correct me if I’m wrong :) \nBut at least\
  \ we’ve found a way to get close to zero downtime.\n\nPostgreSQL Upgrades are hard!\n\
  How Retool upgrad..."
---

By Wenbin Fang

It's impossible to create zero-downtime Postgres upgrades across major versions – right? Please, correct me if I’m wrong :) 

But at least we’ve found a way to get close to zero downtime.

* [PostgreSQL Upgrades are hard!](https://andreas.scherbaum.la/blog/archives/1116-PostgreSQL-Upgrades-are-hard!.html)
* [How Retool upgraded our 4 TB main application PostgreSQL database](https://retool.com/blog/how-we-upgraded-postgresql-database/)

At [Listen Notes](https://www.listennotes.com/), we've performed Postgres major version upgrades twice since 2017, the year Listen Notes was founded. During these upgrades, we experienced zero downtime for “read” operations, and less than 1 minute downtime for “write” operations.

Let’s walk through the process we went through of upgrading Postgres at Listen Notes.

### **TL;DR**

1. Provision a new replica DB (DB_A) with the old version of Postgres.
2. Change DB hosts’ IP addresses in “/etc/hosts” of online servers to use read-only replica DB (not DB_A). By this moment, all write operations will fail.
3. Run [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html) (with “--link”) on DB_A to upgrade to the new version of Postgres, and promote DB_A to be a primary.
4. Replace all DB hosts’ IP addresses in “/etc/hosts” of online servers to use DB_A. By this moment, write operations would resume.
5. Re-provision new replica nodes with the new version of Postgres.

## How We Use Postgres in Listen Notes

Listen Notes is a popular podcast search engine. We provide a website ([ListenNotes.com](https://www.listennotes.com/)) with millions of monthly pageviews, and a solid [Podcast API](https://www.listennotes.com/api/) used by thousands of 3rd-party apps and websites.

We use Postgres as our main database, which stores all podcasts, episode metadata, and user data. 

We run a self-hosted Postgres cluster on AWS EC2, consisting of one primary (db1) for write and read operations, and two replicas (db2 & db3) for read-only operations. The database size is a bit smaller than 1TB.

### Postgres Progress

When Listen Notes was started in 2017, we ran Postgres 9.6.

[Then we upgraded to Postgres 11.0 in 2019](https://www.listennotes.fm/p/monthly-update-for-may-2019-19-05-31).

[By 2021, we were running Postgres 13.0](https://www.listennotes.fm/p/monthly-update-for-september-2021).

Generally speaking, we are not comfortable using the latest version of any infrastructure software, be it Postgres, Django, Redis, or others.

We trust the quality of Postgres, but there may be fewer documents and online discussions for the latest version, which might make troubleshooting difficult when version-specific issues occur.

Listen Notes servers that talk to Postgres DB are using hostnames like db1.internal.ln, db2.internal.ln, db3.internal.ln, and so on.

These hostnames are in “/etc/hosts,” so it’s easy to change the actual IP address while keeping the hostnames unchanged.

There are both online and offline workloads for our Postgres cluster. The online workload is to serve our website (ListenNotes.com) and API endpoints (PodcastAPI.com), which can’t have long downtime (for example, over 5 minutes).

The offline workload runs Celery tasks and other scripts that can be stopped for a relatively long time (for example, 2 hours). You can read our past blog posts to learn details of the Listen Notes architecture:

* [The boring technology behind a one-person Internet company](https://www.listennotes.com/blog/the-boring-technology-behind-a-one-person-23/)
* [Good enough engineering to start an Internet company](https://www.listennotes.com/blog/good-enough-engineering-to-start-an-internet-27/)
* [How I accidentally built a Podcast API business](https://www.listennotes.com/blog/how-i-accidentally-built-a-podcast-api-business-46/)

For upgrading Postgres across major versions, our goal is to achieve zero downtime for read operations and minimal downtime (less than 5 minutes) for write operations. This will ensure most of our users won’t be affected during the time of upgrading.

## **How to Prepare **for Postgres Upgrades****

The actual upgrade may take only 30 minutes, but we typically spend a few workdays preparing, which increases the odds of success during the upgrade.

### Prep Step 1:

We must make sure the new major version of Postgres works well with our code base. So we test the new version of Postgres on dev and staging. 

In addition to automatic unit tests, we have to manually test all major product features.

### Prep Step 2:

Online services ([ListenNotes.com](https://www.listennotes.com/) and [PodcastAPI.com](https://podcastapi.com/)) should work for most users even when Postgres write operations are disabled.

For ListenNotes.com, a majority of users are conducting “read-only” tasks, such as searching podcasts, browsing podcast details, and similar harmless actions. This means that “write” failures should affect only a tiny fraction of users.

For PodcastAPI.com, all API endpoints are read-only or offloading writes to async offline tasks, so write operations can be temporarily disabled.

We would spend some time testing on staging to make sure online services can still be functional when database writes are disabled.

### Prep Step 3:

We spend the most time _rehearsing_ the process of upgrading Postgres. Basically, we provision the entire fleet of Listen Notes and practice all necessary steps to upgrade Postgres.

We try to codify some steps in Ansible or Bash scripts to automate a bit. We document and time each step. By the time we perform it in the production environment, we know how many minutes (or even seconds) each step will take.

### Prep Step 4:

We practice how to quickly rollback to the old version of Postgres, just in case the upgrade fails and we are forced to restore a stable environment ASAP.

## **How to Upgrade **Postgres****

We typically perform the actual upgrade on a Friday night, when website and API traffic is low. Plus, we must have a good rest during the daytime, to preserve enough energy to perform such dangerous and stressful operations in production later that same evening :)

Since we’ve created a detailed TODO list in Notion during the previous few days of preparation, we carefully follow the TODO list to upgrade Postgres:

### Upgrade Step 1:

We provision a new read-only replica DB with the old version of Postgres. Let’s call it DB_A. It’ll sync data from the primary DB in real-time, and will be upgraded to the new version of Postgres first then be promoted to be primary. 

If the upgrade on DB_A fails later, we still have the option to quickly rollback and use the old primary DB instead.

### Upgrade Step 2: 

We stop all offline tasks, except for one Celery worker to handle some time sensitive async tasks, such as sending login emails. We’ll stop this Celery worker right before Step 4. 

We also take most web/API servers out of load balancer, leaving only a minimal fleet of online servers.

### Upgrade Step 3:

We change all DB hosts’ IP addresses in “/etc/hosts” on the minimal fleet of online servers (for example, web, API…) to use an old read-only DB. Let’s call it DB_B.

From this point on, all write ops should fail. This step is to make sure the future new primary DB won’t have outdated data.

### Upgrade Step 4:

We run pg_upgrade (with “--link”) on DB_A to upgrade to the new version of Postgres, and promote it to be a primary DB. From this point on, DB_A is the primary, running the new version of Postgres.

### Upgrade Step 5:

We replace all occurrences of DB_B’s IP with DB_A’s in “/etc/hosts” of the minimal fleet of online servers (for example, web, API…). By this point, DB_A is used as both primary and replica. And write ops should be good now.

### Upgrade Step 6:

We change “/etc/hosts” to use DB_A for all DB hosts (primary + replica) on all other servers and bring back offline tasks. 

From the users’ point of view, all Listen Notes services should be normal now . In fact, all API users should not experience any outage during the entire upgrade process, while a tiny portion of website users may experience errors when performing “write operations,” such as creating a podcast playlist or clip.

### **The most important step in upgrading to a new version of Postgres**

Among them all, Step 4 is the most critical. If it fails or runs too long (for example, more than 10 minutes), then we must rollback by changing “/etc/hosts” on those online servers.

From our experience, it took less than 1 minute to run Step 4. Your mileage may vary if you’ve got a bigger (or smaller) database.

After we make sure things are back to normal after Step 6, we could re-provision replica DB instances with the new version of Postgres. And eventually, we terminate old DB instances.

## Final thoughts

Sounds complex? Yeah, kind of…

Database operations in production are inherently complex and dangerous. Can’t rush the process :)

![Image](https://production.listennotes.com/web/image/747a0d713bc541d8bc063df623d35ee0.jpeg)

## **FAQs**

### Why don’t you use managed Postgres, for example Amazon RDS?

We want to have full control of key infrastructure software (for example, Postgres, Elasticsearch…), because…

1. We don’t want platform lock-in
2. We want to understand what’s going on inside the server, avoiding helplessly waiting for 3rd-party customer support teams (for example, AWS) to help solve urgent production issues inside blackboxes
3. It’s more cost-effective for us to run Postgres instances on our own — if money is not an issue (for example, raising big VC funding) or if we had less Postgres operational experience, then Amazon RDS might have been a good option to start with. Just like many things in life, we need to do things with constraints (like money, time, expertise…).

As far as I know, using a managed Postgres (like Amazon RDS) won’t remove the pain of upgrading across major versions: Google “[Amazon RDS upgrade Postgres versions with zero downtime](https://www.google.com/search?q=amazon+rds+upgrade+postgres+versions+zero+downtime)”.

### Why don’t you use 3rd-party tools to automate the process a bit (like one-button push to automate the whole thing)?

We don’t know if there are any reliable 3rd-party tools out there that are easy to use, easy to understand, safe to use… But we are open to recommendations – [wenbin@listennotes.com](mailto:wenbin@listennotes.com).

We oftentimes need to evaluate if it is worth the time and risk to learn and to use new blackbox tools in production, especially for serious DevOps tasks.

### Why don’t you use MySQL, MongoDB, or other non-Postgres databases?

When I started Listen Notes, I knew Postgres way better than MySQL and other databases, because my previous employer Nextdoor.com uses Postgres. And I know Instagram and other large scale online services also use Postgres as their main data store (at least for the first few years). 

If Postgres works well for huge online services, then it should also work for Listen Notes :) Sometimes we spend time learning new technologies to start a project, but more often we simply use technologies that we already know in order to jump-start a project faster and more efficiently.

Again, upgrading non-Postgres databases across major versions is also not easy…but here’s hoping all the above steps helped make whatever Postgres upgrade you performed a success!

_This blog post was originally published at [ListenNotes.com](https://www.listennotes.com/blog/a-practical-way-to-upgrade-postgres-major-49/)._

