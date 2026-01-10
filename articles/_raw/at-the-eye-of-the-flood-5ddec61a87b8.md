---
title: 'At the eye of the storm: how I helped save people during the disastrous Kerala
  floods'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T13:46:23.000Z'
originalURL: https://freecodecamp.org/news/at-the-eye-of-the-flood-5ddec61a87b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WhQOyjS8Ez_-53GLWVHs6Q.jpeg
tags:
- name: community
  slug: community
- name: 'Kerala '
  slug: kerala
- name: Life lessons
  slug: life-lessons
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Biswaz

  This my perspective on the worst natural calamity experienced by the state of Kerala,
  and how I was able to help build the foundation upon which a great community was
  built. It was a humbling and also challenging experience at the same time...'
---

By Biswaz

This my perspective on the worst natural calamity experienced by the state of Kerala, and how I was able to help build the foundation upon which a great community was built. It was a humbling and also challenging experience at the same time.

Disclaimer: I’ve done my best to cross check the data in this post. But I do not make any guarantees about the completeness, reliability and accuracy of this information.

#### 11th August, 2018

I returned to my home in Palakkad from my college hostel. Palakkad, along with many other districts of Kerala, had just witnessed one of the worst floods in its history. But that was just the start of it. Little did I know what was about to come.

The All Kerala Student Congress, an event organised by IEEE Kerala Section, was cancelled. The Whatsapp group had some discussions regarding what we could do to help the people affected by the flood. As a result, we decided to build a website. I started to the work on a Django app.

Mr Muralidaran Manningal, from SEMT, who also has a presence in IEEE, gave out the requirements for the basic version of the site. At that time the requirements were simple:

1. There would be a form where the people or camps could specify their needs, like water, medicines etc.

2. There would be a contact form listing the info of 2 or 3 people from each district who would coordinate the efforts.

3. Any volunteer who would like to help should be able to view all the items that are needed at various places close to them.

4. The needs that have been taken care of should be marked as complete so that there won’t be too much overlap

I delivered the site by midnight that day. I remember posting the screenshot of my shell as my WhatsApp status just to look cool.

![Image](https://cdn-media-1.freecodecamp.org/images/Lsv4j-mR-2975w3Wu2CVbNLCfxzdNuEFmZUW)

It was the birth of a historical landmark for me. That became a platform for unprecedented collaboration that happened in 14 hours. The Minimum Viable Product was launched!

![Image](https://cdn-media-1.freecodecamp.org/images/q34ydyv0UJY7KTu7ZixpHGkQ7f1o0ItEZc6v)
_The first poster shared among student communities_

#### 12th Aug, 2018

We started getting district-wide requirements. I remember that Palakkad and Ernakulam district administrations were the first to onboard the platform. IEEE initiated WhatsApp groups per district to mobilize volunteers, which later became the control centres of young, hardworking people across Kerala. At first, we had 3 POCs who were all students who would collect resources and get them to the official district collection centres.

The first request came from Pathanamthitta — for 10 litres of water.

Website slowly started to spread on social media. I remember seeing the Kerala Police, a bunch of celebrities, and finally our Chief Minister sharing the website. That was an exciting moment for a clueless B.Tech guy who still had no idea what a dramatic, horrifying, and yet thrilling experience this was about to be.

![Image](https://cdn-media-1.freecodecamp.org/images/tW9wTTTydlT6rBsi08D1-QFPfpssRdLSUjMN)

We ran on the free plan on a cloud platform called Heroku. I chose Heroku as it had a free plan to start, it was dead simple to set up, and we’d still have access to the big guns in case we needed them. But most importantly, I had deployed about 4 Heroku apps before and I was familiar with it. Eventually, we knew that we might have to pay or move to another cloud platform which was free.

There was some thought of transitioning to State Data Center from Heroku as the former was available for free to us. This was later scrapped considering the man hours that would be lost setting up on a bare Linux machine. In a mission critical scenario like this, where every minute matters, Heroku was the best choice I made. I remember that this was my slogan:

> git push heroku master

I would say it to my little brother during some of my previous projects on Heroku. And during this project I used that command often enough, due to the agile nature of the work. (Sorry CI/CD lovers, we didn’t set it up until later.)

We reached the 10K row limit on Heroku’s free tier database. That was one of the first things that worried me. A little bit of maintenance (that lasted until after 1am IST) and some shell commands later, and we were up and running thanks to AWS and its free credits — so we moved the database to AWS!

The following day, the situation became much worse. The requests from places like Ranni intensified the pressure. We had to do something…

![Image](https://cdn-media-1.freecodecamp.org/images/3KQ64QbuLUJKf040ZBZ1Sf21vBBQnhuKZLTw)
_At the time of finishing this, the site had 1.8 Crore+ total page requests and 10 Lakh+ unique visitors._

#### 16th August, 2018 onwards

### The inception of our open-source community

A WhatsApp message was circulated around this time by someone. It said we were receiving tremendous amounts of requests and needed help. It was true indeed! The community started raising issues and adding improvements. To be frank, I was terrified by the number of phone calls I got that day.

[**Hi all · Issue #92 · IEEEKeralaSection/rescuekerala**](https://github.com/IEEEKeralaSection/rescuekerala/issues/92)  
[_Hello, the number of PRs and issues just exploded. And we’re running short of time. Please list below, how us the devs…_github.com](https://github.com/IEEEKeralaSection/rescuekerala/issues/92)

The above issue on GitHub was the first thing that started out community engagement. Everything was exponentially growing (even open issues and stale PR’s).

Vignesh Hari pointed out that we’re starting to get serious stuff in our requests section:

> ഞാനും എന്റെ കൈകുഞ്ഞും അച്ഛനും അമ്മയും അമ്മാവനും അമ്മായിയും ഞങ്ങളുടെ വീട്ടിൽ അകപ്പെട്ടിരിക്കുന്നു.വീടിന്റെ താഴത്തെ നിലയിൽ മുഴുവനും വെള്ളം കയറി…റോഡ് മാർഗം രക്ഷപ്പെടാൻ പറ്റുന്നില്ല .പമ്പയാറിന് സമീപമാണ് വീട്. ജലനിരപ്പ് അപകടമാംവിധം ഉയരുന്നു.ദയവു ചെയ്ത് ആരെങ്കിലും ഞങ്ങളെ രക്ഷിക്കണം..

```
Translation: Me, my newborn, my father and mother, my uncle and my aunt are trapped in our house. The ground floor is flooded.. we cant escape via road too... Our house is near the Pamba river. Water level is increasing dangerously. Please, someone help us...
```

This was one such request. This was the moment I started to fight against my body and mind, to do the best I could. The thought of people depending upon what I coded struck me so hard that it made me do things I would never have done otherwise.

Some of us worked for 21 hours a day for 3 days straight. I’d sleep at 3 am and find myself awake at 6 without an alarm. It was like my circadian rhythm became sentient and took control of the situation. Such extraordinary efforts were made by a handful of volunteers, that I know of, and they remained unseen by the rest of the community. It took 10–12 days of non-stop work. After that things started to settle down a bit.

The community too worked nonstop during these days. There was always someone from some corner of Earth monitoring our Heroku dashboard, who would wake me up if something bad was about to happen.

Our app performed incredibly well during the peak days of the crisis 24x7. We were very careful in our development and code review — but I admit I did some stupid PR merges without a proper code review at the beginning.

![Image](https://cdn-media-1.freecodecamp.org/images/axXrpYUdRwu5uki497TflxJku6VKnjZs6sBx)

To an outsider, our Slack group may seem like a mess — different channels discussing various “gibberish”. Was productive work being done here? Yes! The best thing about the community was the beauty in the chaos. I couldn’t just manage Slack, with the kind of workload I had. Still, the community found its way. Like a structure made by an army of ants, they made amazing stuff. Devops, DataViz, analytics, all kinds of stuff happened in there.

People have asked me, how did KeralaRescue become the №1 application, even though there were many websites with similar features? It is mainly due to the official endorsement from the government. We got that only because we started very early when no one else had started working on such a website. Another reason was that it was launched very quickly. Finally, it was all about the community. It is the community that worked wonders — one built on the strength of the human soul, and its compassion to help its fellow beings.

Making it open-source was another decision that I’m very proud of. The site was open-source from Day 0.

I had read about the power of open source and how it revolutionized many similar events, but to be honest, I didn’t even think about it too much. I just pushed to Git! Because open-source is the default option configured in my brain, like many other students of Kerala. This may be because of our familiarity with stuff like Ubuntu from school. Thanks to the education department for making this happen, while many other states of India still depend on proprietary software.

Along with the open-source-y goodness, we saw the wonders that open data can accomplish. Our data was used by volunteers across the globe, for IVRs, visualization and what not. The impact of open data was visible here. One thing I wish I could go back and change was implementing proper APIs. Initiatives like [https://data.gov.in/](https://data.gov.in/) have great potential.

### The tech

As I mentioned, the database was moved to AWS, just because we had free credits on it. Later, one of the core DevOps engineers pointed out that colocating the database with the application had its advantages. So we later moved back to Heroku (and they ended up giving us free credits!).

One of the main things I had in mind was: Do not block the request-response cycle. We encountered stuff like slow API calls (for sending SMS) that block the cycle. Such calls were identified in the code review. We added a Redis Queue and that helped a lot moving forward. All CSV imports were made through the Redis Queue. It was satisfying to see RQ crunching the data, while our app dynos took care of requests.

We had an endpoint called /data which was made to populate the rescue map. The map was later removed. But /data stayed for a while. When the request data grew (to 51K finally), it started to slow down the server. We tried paginating it and later removed it. /data did a good job at the time of crisis. Making the data readily available made it easy for various groups like keralafights, saakhi and the myoperator powered call centres who prioritized the requests and channelled them to various authorities via IT Mission.

The community had multiple parallel efforts like Ushahidi and Sahana. Ushahidi’s data import was painfully slow. The existing data needed to be ported to Ushahidi if we were to be able to use it. One of the developers ended up submitting an upstream patch speeding up the process by 40%! But, we ended up not using both of them.

### Lessons for the future

Global warming and the destruction of our mountains, rivers and valleys will backfire in the near future. Unfortunately, this may not be the only natural calamity that Malayalis may experience in their lifetime.

> Those who do not read history are doomed to repeat it  
>  — George Santayana

Sustainable development should be implemented, not just remain in textbooks. I believe this is the **ONLY** form of development Kerala can have, due to our geography.

Ideally, our disaster management should utilise the power of modern tech. A ready to deploy tech solution should be always available. Efforts should be made by the government, using the existing volunteer force to transform KeralaRescue into a go-to solution for disaster management software.

The student/volunteer community is an untapped potential of Kerala. A crisis like this can summon techies from all over the world. We even had contributions from Croatia. These silent guardians will be there in the future, waiting to be called.

Our disaster management should have a technically capable team, who can handle agile workflows. A central management team plays an important role here. They should be able to provide volunteers with vision and direction.

Standards such as [SPHERE](http://www.sphereproject.org) should be enforced. Supplies tracking, damage assessment and fund utilization should be available online, as public information. Public ledgers are perfect for ensuring transparency. Public audits should be the source of truth. Getting people’s feedback should be incorporated into the software.

#### Wrapping up

Thank you Cloudflare, Slack, Heroku, AWS and Workast who helped us by giving their technology for free! And all the awesome people on Twitter, Reddit and wherever else, spreading our message.

![Image](https://cdn-media-1.freecodecamp.org/images/AqneCnDMppT-jLHN8eRLBdncwswVLfLvM-0N)

None of the contributors are mentioned here. This was a conscious decision. A [humans.txt](http://humanstxt.org/) file is the best tool for this as I may miss someone, inevitably.

This effort was made possible by the FOSS philosophy, which Kerala is indeed familiar with. I wish to see more FOSS initiatives, right from the school level. In fact, my first exposure to FOSS was Edubuntu used at all schools across Kerala and also the IT Festival organized by the government for students.

![Image](https://cdn-media-1.freecodecamp.org/images/kvOaCn6Rkxg73io5sOqmFhvecbvwjIq-xHGv)

Finally, I’d like to thank each and every human soul who helped KeralaRescue and by virtue of that, the people of Kerala. It was a privilege to work with an international team of software engineers and contributors.

Reach me at [https://biswaz.github.io](https://biswaz.github.io)

