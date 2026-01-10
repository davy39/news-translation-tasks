---
title: The boring technology behind a one-person Internet company
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-10T21:51:00.000Z'
originalURL: https://freecodecamp.org/news/the-boring-technology-behind-a-one-person-internet-company
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_83ZzjS6ZhVWvZdnoozElOw.png
tags:
- name: actor model
  slug: actor-model
- name: Entrepreneurship
  slug: entrepreneurship
- name: podcast
  slug: podcast
- name: 'solopreneur '
  slug: solopreneur
- name: Startups
  slug: startups
seo_title: null
seo_desc: 'By Wenbin Fang

  Listen Notes is a podcast search engine and database. The technology behind Listen
  Notes is actually very very boring. No AI, no deep learning, no blockchain. “Any
  man who must say I am using AI is not using True AI” :)

  After reading t...'
---

By Wenbin Fang

[Listen Notes](https://www.listennotes.com/) is a podcast search engine and database. The technology behind Listen Notes is actually very very boring. No AI, no deep learning, no blockchain. [“Any man who must say I am using AI is not using True AI”](https://www.youtube.com/watch?v=4sJY7BTIuPY) :)

After reading this post, you should be able to replicate what I build for Listen Notes or easily do something similar. You don’t need to hire a lot of engineers. Remember, [when Instagram raised $57.5M and got acquired by Facebook for $1B](https://www.crunchbase.com/organization/instagram#section-funding-rounds), they had only [13 employees](https://www.businessinsider.com/instagram-employees-and-investors-2012-4) — not all of them were engineers. The Instagram story happened in early 2012. It’s 2019 now, it’s more possible than ever to build something meaningful with a tiny engineering team — even one person.

If you haven’t used Listen Notes yet , try it now:

[https://www.listennotes.com/](https://www.listennotes.com/)

### Overview

Let’s start with requirements or features of this Listen Notes project.

Listen Notes provides two things to end users:

* A website [ListenNotes.com](https://www.listennotes.com/) for podcast listeners. It provides a search engine, a podcast database, [Listen Later](https://www.listennotes.com/listen/?s=nav) playlists, [Listen Clips](https://www.listennotes.com/clips/?s=nav) that allows you to cut a segment of any podcast episode, and [Listen Alerts](https://www.listennotes.com/alerts) that notifies you when a specified keyword is mentioned in new podcasts on the Internet.
* [Podcast Search & Directory APIs](https://www.listennotes.com/api/) for developers. We need to track the API usage, get money from paid users, do customer support, and more.

I run everything on AWS. There are 20 production servers (as of May 5, 2019):

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1__HqlSoEW7JEDVnJ9rFSj7w.png)
_The servers that run Listen Notes_

You can easily guess what does each server do from the hostname.

* **production-web** serves web traffics for [ListenNotes.com](https://www.listennotes.com/).
* **production-api** serves api traffics. We run two versions of API (as of May 4, 2019), thus v1api (the legacy version) and v2api (the new version).
* **production-db** runs PostgreSQL (primary and replica)
* **production-es** runs an Elasticsearch cluster.
* **production-worker** runs offline processing tasks to keep the podcast database always up-to-date and to provide some magical things (e.g., search result ranking, episode/podcast recommendations…).
* **production-lb** is the load balancer. I also run Redis & RabbitMQ on this server, for convenience. I know this is not ideal. But I’m not a perfect person :)
* **production-pangu** is the production-like server that I sometimes run one-off scripts and test changes. What’s the meaning of “[pangu](https://en.wikipedia.org/wiki/Pangu)”?

Most of these servers can be horizontally scaled. That’s why I name them _production-something1_, _production-something2_… It could be very easy to add _production-something3_ and _production-something4_ to the fleet.

### Backend

The entire backend is written in Django / Python3. The operating system of choice is Ubuntu.

I use [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) to serve web traffics. I put [NGINX](https://www.nginx.com/) in front of uWSGI processes, which also serves as load balancer.

The main data store is [PostgreSQL](https://www.postgresql.org/), which I’ve got a lot of development & operational experience over many years — battle tested technology is good, so I can sleep well at night. [Redis](https://redis.io/) is used for various purposes (e.g., caching, stats,…). It’s not hard to guess that [Elasticsearch](https://www.elastic.co/) is used somewhere. Yes, I use Elasticsearch to index podcasts & episodes and to serve search queries, just like [most](https://medium.com/netflix-techblog/tagged/elasticsearch) [boring](https://engineeringblog.yelp.com/2017/06/moving-yelps-core-business-search-to-elasticsearch.html) [companies](https://eng.uber.com/tag/elasticsearch/).

[Celery](http://www.celeryproject.org/) is used for offline processing. And [Celery Beat](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html) is for scheduling tasks, which is like Cron jobs but a bit nicer. If in the future Listen Notes gains traction and Celery & Beat cause some scaling issues, I probably will switch to the two projects I did for my previous employer: [ndkale](https://github.com/Nextdoor/ndkale) and [ndscheduler](https://github.com/Nextdoor/ndscheduler).

[Supervisord](http://supervisord.org/) is used for process management on every server.

Wait, how about Docker / Kubernetes / serverless? Nope. As you gain experience, you know when not to over-engineer. I actually did some early Docker work for my previous employer back in 2014, which was good for a mid-sized billion-dollar startup but may be overkill for a one-person tiny startup.

### Frontend

The web frontend is primarily built with [React](https://reactjs.org/) + [Redux](https://redux.js.org/) + [Webpack](https://webpack.js.org/) + [ES](https://en.wikipedia.org/wiki/ECMAScript). This is pretty standard nowadays. When deploying to production, JS bundles would be uploaded to [Amazon S3](https://aws.amazon.com/s3/) and served via [CloudFront](https://aws.amazon.com/cloudfront/).

On [ListenNotes.com](https://www.listennotes.com/), most web pages are half server-side rendered ([Django template](https://docs.djangoproject.com/en/2.0/topics/templates/)) and half client-side rendered ([React](https://reactjs.org/)). The server-side rendered part provides a boilerplate of a web page, and the client-side rendered part is basically an interactive web app. But a few web pages are rendered entirely via server side, because of my laziness to make things perfect & some potential SEO goodies.

#### Audio player

I use a heavily modified version of [react-media-player](https://github.com/souporserious/react-media-player) to build the audio player on ListenNotes.com, which is used in several places, including [Listen Notes Website](https://www.listennotes.com/p/321dd0ce5b974079bd3fc8d65d132912/), [Twitter embedded player](https://twitter.com/ListenHistoryFM/status/955913550605688832), and embedded player on 3rd party websites:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_R9SqwWtGOKvL0MqOBvsMrA.png)
_Embedded player on 3rd party websites_

### Podcast API

We provide a simple and reliable [podcast API](https://www.listennotes.com/api/) to developers. Building the API is similar to building [the website](https://www.listennotes.com/). I use the same Django/Python stack for the backend, and ReactJs for the frontend (e.g., API dashboard, documentation…).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_6s_rx2FAKEJiHy7K6gEwdA.png)
_Listen API dashboard_

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_dYUinicZH-m6HZPpE1MXBg.png)
_Listen API documentation_

For the API, we need to track how many requests a user use in current billing cycle, and charge $$$ at the end of a billing cycle. It’s not hard to imagine that Redis is heavily used here :)

### DevOps

#### Machine provisioning & code deployment

I use [Ansible](http://docs.ansible.com/) for machine provisioning. Basically, I wrote a bunch of yaml files to specify what type of servers need to have what configuration files & what software. I can spin up a server with all correct configuration files & all software installed with one button push. This is the directory structure of those Ansible yaml files:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_oql35nt1Iak2FzniugFPSw.png)
_I could’ve done a better job in naming things. But again, it’s good enough for now._

I also use Ansible to deploy code to production. Basically, I have a wrapper script _deploy.sh_ that is run on macOS:

> _./deploy.sh production HEAD web_

The deploy.sh script takes three arguments:

* **Environment**: production or staging.
* **Version of the listennotes repo**: HEAD means “just deploy the latest version”. If a SHA of a git commit is specified, then it’ll deploy a specific version of code — this is particularly useful when I need to rollback from a bad deployment.
* **What kind of servers**: web, worker, api, or all. I don’t have to deploy to all servers all at once. Sometimes I make changes on Javascript code, then I just need to deploy to web, without touching api or worker.

The deployment process is mostly orchestrated by Ansible yaml files, and of course, it’s dead simple:

* **On my Macbook Pro**, if it’s to deploy to web servers, then build Javascript bundles and upload to S3.
* **On the target servers**, git clone the listennotes repo to a timestamp-named folder, check out the specific version, and pip install new Python dependencies if any.
* **On the target servers**, switch symlink to the above timestamp-named folder and restart servers via supervisorctl.

As you can see, I don’t use those fancy CI tools. Just dead simple things that actually work.

#### Monitoring & alerting

I use [Datadog](https://www.datadoghq.com/) for monitoring & alerting. I’ve got some high level metrics in a simple dashboard. Whatever I do here is to boost my confidence when I am messing around the production servers.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_nrvlxilaFwNJtZDeGt01fQ.png)
_Datadog dashboard for Listen Notes, as of Dec 2017._

I connect [Datadog](https://www.datadoghq.com/) to PagerDuty. If something goes wrong, [PagerDuty](https://www.pagerduty.com/) will send me alerts via phone call & SMS.

I also use [Rollbar](https://rollbar.com/) to keep an eye on the health of Django code, which will catch unexpected exceptions and notify me via email & Slack as well.

I use [Slack](https://slack.com/) a lot. Yes, this is a one-person company, so I don’t use Slack for communicating with human beings. I use Slack to monitor interesting application-level events. In addition to integrating Datadog and Rollbar with Slack, I also use [Slack incoming webhooks](https://api.slack.com/incoming-webhooks) in Listen Notes backend code to notify me whenever a user signs up or performs some interesting actions (e.g., adding or deleting things). This is a very common practice in tech companies. When you read some books about Amazon or PayPal’s early history, you’ll know that both companies had similar notification mechanism: whenever a user signed up, there would be a “ding” sound to notify everyone in the office.

Since launched in early 2017, Listen Notes hasn’t got any big outage (> 5 minutes) except for [this one](https://broadcast.listennotes.com/postmortem-on-apr-22-2018-outage-e5a87723d003). I’m always very careful & practical in these operational stuffs. The web servers are significantly over-provisioned, just in case there’s some huge spike due to press events or whatever.

### Development

I work in a [WeWork](https://refer.wework.com/i/WenbinFang) coworking space in San Francisco. Some people may wonder why not just work from home or from some random coffee shops. Well, I value productivity a lot and I’m willing to invest money in productivity. I don’t believe piling time helps software development (or any soft of knowledge/creativity work). It’s rare that I work over 8 hours in a day (Sorry, [996 people](https://www.nytimes.com/2019/04/29/technology/china-996-jack-ma.html)). I want to make every minute count. Thus, a nice & relatively expensive private office is what I need :) Instead of optimizing for spending more time & saving money, I optimize for spending less time & making money :)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_LqJym-17rqU-vyNzanCiVA.jpeg)
_My office at WeWork_

I’m using a MacBook Pro. I run the (almost) identical infrastructure inside [Vagrant](https://www.vagrantup.com/) + [VirtualBox](https://www.virtualbox.org/wiki/Downloads). I use the same set of Ansible yaml files as described above to provision the development environment inside Vagrant.

I subscribe to the [monolithic repo](https://danluu.com/monorepo/) philosophy. So there’s one and only one listennotes repo, containing DevOps scripts, frontend & backend code. This listennotes repo is hosted as a GitHub private repo. I do all development work on the main branch. I rarely use feature branches.

I write code and run the dev servers (Django runserver & webpack dev server) by using [PyCharm](https://www.jetbrains.com/pycharm/). Yea, I know, it’s boring. After all, it’s not Visual Studio Code or Atom or whatever cool IDEs. But PyCharm works just fine for me. I’m old school.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_0qlv-bne1Ld2wuUxCeDFwQ.png)
_My PyCharm_

### Miscellaneous

There are a bunch of useful tools & services that I use to build Listen Notes as a product and a company:

* [iTerm2](https://www.iterm2.com/) and [tmux](https://github.com/tmux/tmux/wiki) for the terminal stuffs.
* [Notion](https://www.notion.so/?r=d1e4526dd2924f4796cd10235cbe132e) for TODO lists, wiki, taking notes, design documents…
* [G Suite](https://gsuite.google.com/) for @listennotes.com email account, calendar, and other Google services.
* [MailChimp](http://www.mailchimp.com/monkey-rewards/?utm_source=freemium_newsletter&utm_medium=email&utm_campaign=monkey_rewards&aid=da29e56f1e479faf6b4ef3f72&afl=1) for sending the [monthly email newsletter](https://us16.campaign-archive.com/home/?u=da29e56f1e479faf6b4ef3f72&id=ba72067923).
* [Amazon SES](https://aws.amazon.com/ses/) for sending transactional & some marketing emails.
* [Gusto](https://gusto.com/r/wenbin) to pay myself and contractors who are not from Upwork.
* [Upwork](https://www.upwork.com/) to find contractors.
* [Google Ads Manager](https://admanager.google.com/home/) to mange direct sales ads and track performance.
* [Carbon Ads](https://www.carbonads.net/) and [BuySellAds](https://www.buysellads.com/) for fallback ads.
* [Cloudflare](https://www.cloudflare.com/) for DNS management, CDN, and firewall.
* [Zapier](https://zapier.com/) and [Trello](https://trello.com/) to streamline the [podcaster interview](https://www.listennotes.com/interviews/) workflow.
* [Medium](https://broadcast.listennotes.com/) for the company blog (obviously).
* [Godaddy](https://www.godaddy.com/) and [Namecheap](https://www.namecheap.com/) for domain names.
* [Stripe](https://stripe.com/) for getting money from users (primarily for [API](https://www.listennotes.com/api/)).
* [Google speech-to-text API](https://cloud.google.com/speech-to-text/) to transcribe episodes.
* [Kaiser Permanente](https://healthy.kaiserpermanente.org/) for health insurance.
* [Stripe Atlas](https://atlas.stripe.com/) to incorporate Listen Notes, Inc.
* [Clerky](https://www.clerky.com/) to generate legal documents for fund raising (SAFE) and hiring contractors who are not from Upwork.
* [Quickbooks](https://www.referquickbooks.com/s/Wenbin) for bookkeeping.
* [1password](https://1password.com/) to manage login credentials for tons of services.
* [Brex](http://brex.com/signup?rc=oPLQ0ZQ) for charge card — you can get incremental $5000 AWS credits, which can be applied on top of the AWS credits from WeWork or Stripe Atlas.
* [Bonvoy Business Amex Card](http://refer.amex.us/WENBIFIUoH?XLINK=MYCP) — You can earn Marriott Bonvoy points for luxury hotels and flights. It’s the best credit card points for traveling :)
* [Capital One Spark](https://www.capitalone.com/small-business-bank/) for checking account.

### Keep calm and carry on…

As you can see, we are living in a wonderful age to start a company. There are so many off-the-shelf tools and services that save us time & money and increase our productivity. It’s more possible than ever to build something useful to the world with a tiny team (or just one person), using simple & boring technology.

As time goes, companies become smaller and smaller. You don’t need to hire tons of full-time employees. You can hire services (SaaS) and on-demand contractors to get things done.

Most of time, the biggest obstacle of building & shipping things is over thinking. What if this, what if that. Boy, you are not important at all. Everyone is busy in their own life. No one cares about you and the things you build, until you prove that you are worth other people’s attention. Even you screw up the initial product launch, few people will notice. [Think big, start small, act fast](https://hackernoon.com/think-big-start-small-act-fast-6fdab1f771ea). It’s absolutely okay to use the boring technology and start something simple (even ugly), as long as you actually solve problems.

%[https://twitter.com/wenbinf/status/1082725746160746496?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1082725746160746496&ref_url=https%3A%2F%2Fbroadcast.listennotes.com%2Fmedia%2F622ba96d011f0ebfd9712504b7e353c3%3FpostId%3D56697c2e347b]

There are so many [cargo-cult](http://stevemcconnell.com/articles/cargo-cult-software-engineering/)-type people now. Ignore the noises. Keep calm and carry on.

---

If you haven’t used Listen Notes yet , try it now:

[https://www.listennotes.com/](https://www.listennotes.com/)


