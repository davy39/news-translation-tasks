---
title: The power of the developer community
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T20:28:11.000Z'
originalURL: https://freecodecamp.org/news/the-power-of-the-developer-community-2b6e713fc9ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*39yXxTeKLonaag8vJfjg1Q.png
tags:
- name: Blogging
  slug: blogging
- name: community
  slug: community
- name: Devops
  slug: devops
- name: Inspiration
  slug: inspiration
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Joel Speed

  In the autumn of 2014, I started my adventure into the world of DevOps. Having just
  started my degree, I found a society at the university that was in desperate need
  of some IT love. My home for the next three years was at Warwick Stude...'
---

By Joel Speed

In the autumn of 2014, I started my adventure into the world of DevOps. Having just started my degree, I found a society at the university that was in desperate need of some IT love. My home for the next three years was at [Warwick Student Cinema](https://warwick.film/).

![Image](https://cdn-media-1.freecodecamp.org/images/BufmiJ4tdnK0rolaro76iqb6Cq2n41YlrSBz)

Over the course of my degree, I tore every part of the cinema’s infrastructure apart and rebuilt it from scratch (not all single-handed, mind). Being on a tight budget, approximately £0 annually, the cinema’s infrastructure consisted of a number of hand-me-down machines that the university no longer required and a couple of [1U](https://en.wikipedia.org/wiki/1U) Dell pizza boxes they bought as a one-off expense. On this, they hosted their public facing website, as well as a number of internal sites crucial to the running of the cinema.

The most important of these sites was known as EPOS. It was a PHP monolith, intertwined with the main public website that was written about 10 years prior by a handful of enthusiastic students and had been passed over year on year to the next IT officer in line.

This EPOS site was used to sell tickets for the cinema’s screenings approximately 7 times a week. At each screening, over a 30-minute window, we could sell up to 300 tickets. But, more often than not, the site would fall over and our duty managers would have to resort to using raffle tickets to count our attendees. Sadly, the systems had no redundancy, nothing horizontally scaled, and honestly, no one quite knew how anything pieced together.

I’d like to think that by the time I handed the IT Officer hat over to my successor, the infrastructure was in a better state. All of the Linux workloads had been migrated to Docker containers, running on a [Swarm](https://docs.docker.com/engine/swarm/). The container’s Dockerfiles were under source control, with automated builds and deploys using Jenkins.

We now understood the role of each part of the infrastructure, we could see in code what was running and where. The monolith could now horizontally scale and its up-time had greatly increased. I felt like myself and the few colleagues who helped me during this period had really made a difference to the systems we maintained.

### Nice story Joel, but what has this got to do with community?

None of what I’ve described above I could have done alone. I’m no genius. I didn’t just instantly know how to write a Dockerfile, or how to set up a Docker Swarm. The redundant firewalls I set up with complicated policy-based routing and [VRRP](https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol) on their internal and external interfaces, it wasn’t guesswork. I barely knew what Linux was when I started university!

Everything I did, everything I learned during this period, came from the internet, the community. I spent countless hours on Google — going from tutorials on topics such as how to generate a [CSR](https://en.wikipedia.org/wiki/Certificate_signing_request) to StackOverflow questions which matched the error string I had just encountered. I trawled support forums for [pfSense](https://www.pfsense.org/) as I tried to work out how to get traffic routing between multiple [VLANs](https://en.wikipedia.org/wiki/Virtual_LAN). And I read articles on best practices for reducing single points of failures. All of the answers I found, everything I read, had been contributed by people in their spare time.

The community inspired me. There were so many people out there who were willing to give up their time, to share their expertise, to help people by writing, maintaining and responding to issues on open source projects. I feel like I learned so much over the three year period and I genuinely believe I wouldn’t be in my current role without all this. I feel indebted to the community for helping me to get to where I am today.

### So the community got you where you are today?

That’s exactly what I’m saying! Without the time and effort that countless members of the community spent on their blogs and tutorials, I would not have managed most of the projects I took on at the cinema, nor would I have learned so much!

It got me thinking. I wanted to be able to give back, take what I had learned and become an active member of the community. If these people were helping me so much, could I possibly help them and repay the favor?

I came to the conclusion that I might be doing some interesting things at the cinema. Perhaps I had spent enough time learning from others that now I could start contributing back to the community. I bought myself a [personal domain](https://joelspeed.co.uk/) and decided that I would start blogging, with the hope that someday people might find my ramblings useful.

This didn’t go quite as planned. It took me a full 3 years from purchasing my domain to actually putting a blog up on it. I’m fortunate that my company, [Pusher](https://pusher.com/), is supportive of my wanting to write and to give back to the community. In March of this year, I managed to write my first blog post and have now been published on [The New Stack](https://thenewstack.io/kubernetes-single-sign-one-less-identity/), and [InfoQ](https://www.infoq.com/articles/tips-running-scalable-workloads-kubernetes). I’ve spoken at 2 meetups and I’ve been pushing to open-source a bunch of projects I’ve worked on since I joined Pusher. Five have been shared so far!

What I have come to realize over the last year is that it’s not as hard to contribute to the community as I thought it would be, and that actually, I have been working on some interesting stuff. I’ve had a number of people reach out to me, talk to me after talks, asking me questions or for more detail on the work I’ve done. A couple of times people have just told me they’ve read my work and used it as a guideline for their own projects. I’m glad I have managed to help these people and started to help others as many others helped me.

### Why Open Source your work?

The projects we’ve open sourced at Pusher aren’t particularly big and they give us no competitive advantage over any of our competitors. They are related to our Kubernetes infrastructure. Where we couldn’t find an existing solution in the community, we wrote the tools we needed, and now we are sharing them so that other people, trying to solve the same problems, need not spend their time writing their own version.

Perhaps you’ve worked on something that is similar, is it open source? Could it be? I would like to encourage you to share it if you can.

### My plea

If you got this far, thank you, I have a favor to ask. Whether you’re a developer or an accountant, whether you work in PR or in Sales, you will know something that someone else doesn’t. You will be an expert at something even if you don’t know that you are. Have a think on that and then put pen to paper (or digital equivalent).

Write an article and share your experience. Write an article and help someone learn, and further themselves. Help them understand something they’ve been trying to wrap their head around for days. Write an article and, like so many did for me, inspire someone.

