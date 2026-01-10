---
title: Why Team Culture is Critical for Successful Microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T17:21:15.000Z'
originalURL: https://freecodecamp.org/news/why-team-culture-is-critical-for-successful-microservices-2b0e24f124e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xxKgPqB6Hkmx6y3gJS8LwA.jpeg
tags:
- name: Culture
  slug: culture
- name: Microservices
  slug: microservices
- name: Productivity
  slug: productivity
- name: teamwork
  slug: teamwork
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jake Lumetta

  Developers are increasingly turning to microservices to build and modify individual
  components independently. Microservices are clearly beneficial from a technical
  standpoint, but before teams decide to implement microservices, they s...'
---

By Jake Lumetta

Developers are increasingly turning to microservices to build and modify individual components independently. Microservices are clearly beneficial from a technical standpoint, but before teams decide to implement microservices, they should consider how creating microservices will impact team culture.

This article offers advice and insights from CTO’s who have enjoyed the successes and endured the growing pains of implementing microservices, as well as guidance for how to smoothly integrate microservices into your team’s culture.

### Rule # 1: You can’t build successful microservices without a successful team culture.

Back when I was working with Java developers, I remember there being a source of tension within the camp around who got to work on the newest and meatiest features. Our engineering leadership had decided that we would exclusively use Java to build all new microservices.

There were great reasons for this decision, but — as I will explain later — such a restrictive decision came with some consequences in terms of team morale. We learned an important lesson there: to the extent possible, communicating the “why” of a technical decision to the team can go a long way towards creating a culture where people are kept in the loop.

When it comes to organizing and managing a team around microservices, it’s always challenging to balance the mood, morale, and overall culture of your team. In most cases, the leadership needs to balance the risk of team members using new technology against the needs of the client and the business itself.

This dilemma, and many others like it, has led CTOs to ask themselves questions such as: How much freedom should I give my team when it comes to adopting new technologies? And perhaps even more importantly, how can I manage the overarching culture within my camp?

#### Give every team member a chance to thrive

When the engineering leaders mentioned above decided that Java was the best technology to use when building microservices, the decision was really best for the company. Java is performant, and many of the senior people on the team we well versed with it. So that’s why we went with Java. However, not everyone on the team had experience with Java.

The problem was, our team was split into two camps: the Java guys, and the JavaScript guys. As time went by, new and exciting projects came up, and we’d always reach for Java to get the job done. Before long, there was some annoyance within the JavaScript camp that crept up.

“Why do the Java guys always get to work on the exciting new projects, while we’re left to do the mundane front-end tasks like implementing third party analytics tools? We want a big, exciting project to work on, too!”

Like most rifts, it started out small but grew worse over time.

The lesson I took from that experience was to take your team’s expertise and favored technologies into account when choosing a _de facto_ tech stack for your microservices, as well as when it comes to adjusting the level of freedom you give your team to pick and choose their tools.

Sure, you need to have some structure, but if you’re too restrictive — or worse yet, blind to the desire of people in your team to innovate with different technologies — you may have a rift of your own to manage.

So, evaluate your team closely, and come up with a plan that empowers everyone in your team. That way, every section of your team can get involved in major projects, without anyone feeling like they aren’t being given a chance to thrive.

### Technology choices: stability vs flexibility

One of the biggest issues CTOs and developers have to wrestle with is how much technological freedom to allow developers.

Let’s say you hire a new junior developer. They may be excited about some brand new fresh off the press JavaScript framework. Almost too new.

That framework, while sporting some technical breakthroughs, may not have proven itself in production environments, and it most probably doesn’t have great support available. CTOs have the hard choice between okaying that move for the good of morale and excitement within the camp — or declining it to safeguard the needs of the company, to protect the company’s bottom line, and to keep the project stable as the deadline approaches.

The right answer depends on a lot of different factors, which also means there is no right answer.

#### Technological freedom

Some CTOs and founders fully embrace technological freedom and then allow things to settle naturally on a few technologies that work well when turning to deployment.

“We give our team and ourselves 100% freedom in considering technology choices. We eventually identified two or three technologies not to use in the end, primarily due to not wanting to complicate our deployment story,” said [Benjamin Curtis](https://twitter.com/stympy?lang=en), Co-founder of [Honeybadger](https://www.honeybadger.io/).

“In other words, we considered introducing new languages and new approaches into our tech stack when creating our microservices, and we actually did deploy a production microservice on a different stack at one point. [While we do generally] stick with technologies that we know in order to simply our ops stack, we periodically revisit that decision to see if potential performance or reliability benefits would be gained by adopting a new technology, but so far we haven’t made a change,” Curtis continued.

When I spoke with [Stephen Blum](https://twitter.com/stephenlb), CTO at [PubNub](https://www.pubnub.com/), he too expressed a similar view in favor of welcoming pretty much any technology that cuts the mustard:

“We’re totally open with it. We want to continue to push forward with new open source technologies that are available and we only have a couple constraints with the team that are very fair: must run in container environment and it has to be cost-effective,” Blum said.

#### High-freedom, High-responsibility

Freedom comes with a caveat though: if developers enjoy the fruits of freedom of technology choices, they also need to take ownership of making sure the build works.

During my interview with [Sumo Logic](http://sumologic.com) CTO [Christian Beedgen](https://twitter.com/raychaser) and Chief Architect [Stefan Zier](https://twitter.com/stefanzier), they expanded on this topic. They added clout to the position that, if you’re going to give developers freedom to choose their technology, it has to come with a high level of responsibility attached.

“It’s really important that [whoever builds] the software takes full ownership for it. In other words, they not only build software, but they also run the software and remain responsible for the whole lifecycle,” they said.

They continued by explaining that a system that resembles a federal government system should be put into place to help keep those freedoms in check by heightening responsibility.

“[You need] a federal culture really. You’ve got to have a system where multiple, independent teams can come together towards the greater goal. That limits the independence of the units to some degree, as they have to agree that there is potentially a federal government of some sort. But within those smaller groups, they can make as many decisions on their own as they like within guidelines established on a higher level,” he said.

Decentralized, federal, or however you wish to frame it, certainly seems to be an attractive approach to structuring microservice teams. It’s an approach that gives each team and each team member the freedom they want — without giving anyone free reign to pull the entire project apart at the seams.

But not everyone agrees.

#### Restrict technology to simplify things

On the other hand, [Darby Frey](https://twitter.com/darbyfrey), Co-founder of Lead Honestly, takes a more restrictive approach to technology selection.

“At my last company, we had a lot of services and a fairly small team, and one of the main things that made it work, especially for the team size that we had, was that every app was the same. Every backend service was a Ruby app,” he explained.

Frey told me how this helped simplify the life of his team, as every service has, “the same testing framework, the same database backend, the same background job processing tool, etc. Everything was the same.”

At the same time, Frey is sympathetic to the concept of developers wanting to introduce a new language, admitting that he “loves the idea of trying new things”. However, he feels that the cons outweigh the pros.

“Having a polyglot architecture can increase the development and maintenance costs. If it’s just all the same, you can focus on business value and business features and not have to be super siloed in how your services operate. I don’t think everybody loves that decision, but at the end of the day when they have to fix something on a weekend or in the middle of the night, they appreciate it,” said Frey.

### Centralized or decentralized organization

The way your team is structured is also going to impact your microservices engineering culture — for better, or worse.

For example, it’s common for software engineers to write the code before shipping it off to the operations team, who in turn deploy it to the servers. But when things break (and things always break!), an internal conflict occurs.

Because operation engineers don’t write the code themselves, they rarely understand problems when they first arise. As a result, they have to get in touch with those who did code it — the software engineers. So, right from the get-go, you’ve got a middleman relaying a message between the problem and the team that can fix that problem.

To add an extra level of complexity, because software engineers aren’t involved with operations, they often can’t fully appreciate how their code affects the overall operation of the platform. They only come to know of any issue when operations engineers complain about it. As you can see, this is a relationship that’s destined for constant conflict.

#### Decentralized = high-responsibility

One way to attack this problem is by following the lead of Netflix and Amazon, both of which favor decentralized governance. James Lewis and Martin Fowler, two software development thought leaders, laid out their thoughts via a [lengthy blog post](https://martinfowler.com/articles/microservices.html#ProductsNotProjects). According to them, decentralized governance is the way to go when it comes to microservice team organization.

“One of the consequences of centralized governance is the tendency to standardize on single technology platforms. Experience shows that this approach is constricting — not every problem is a nail and not every solution a hammer,” the article reads.

“Perhaps the apogee of decentralized governance is the ‘build it, run it’ ethos popularized by Amazon. Teams are responsible for all aspects of the software they build including operating the software 24/7,” it continues.

Netflix, Lewis and Fowler write, is another company pushing higher levels of responsibility on development teams. They hypothesize that, because they’ll be responsible and called upon should anything go wrong later down the line, more care will be taken during the development and testing stages to ensure each microservice is in ship shape.

“These ideas are about as far away from the traditional centralized governance model as it is possible to be,” they conclude.

#### Who’s getting paged on the weekends?

When considering centralized or decentralized culture, you should think about how that impacts your team members when problems inevitably crop up at inopportune times. You see, a decentralized system implies that each decentralized team takes responsibility for one service, or one set of services. But that too creates a problem: silos.

That’s one reason why [Darby Frey](https://twitter.com/darbyfrey), the Co-founder of Lead Honestly, isn’t a proponent of the concept of decentralized governance.

“The pattern of ‘a single team is responsible for a particular service’ is something you see a lot in microservice architectures. We don’t do that, for a couple of reasons. The primary business reason is that we want teams that are responsible not for specific code but for customer-facing features. A team might be responsible for order processing, so that will touch multiple code bases but the end result for the business is that there is one team that owns the whole thing end to end so there are fewer cracks for things to fall through,” Frey explained.

The other main reason, he continued, is that developers can take more ownership of the overall project:

“They can actually think about [the project] holistically,” said Frey.

Nathan Peck, Developer Advocate for Container Services at Amazon Web Services, [explained this problem in more depth here](https://medium.com/@nathankpeck/microservice-principles-decentralized-governance-4cdbde2ff6ca). In essence, when you separate the software engineers and the operations engineers, you make life harder for your team whenever an issue arises with the code — which is bad news for end users, too.

#### Does decentralization need to lead to separation and siloization?

Peck goes on to explain that his solution lies in [DevOps](https://opensource.com/resources/devops), a model aimed at tightening the feedback loop by bringing these two teams closer together. This strengthens team culture and communication in the process. Peck describes this as the, “you build it, you run it” approach.

However, that doesn’t mean teams have to get siloed or distanced away from partaking in certain tasks, as Frey suggests might happen.

“One of the most powerful approaches to decentralized governance is to build a mindset of ‘DevOps,’” Peck wrote. “[With this approach], engineers are involved in all parts of the software pipeline: writing code, building it, deploying the resulting product, and operating and monitoring it in production. The DevOps way contrasts with the older model of separating development teams from operations teams by having development teams ship code ‘over the wall’ to operations teams who were then responsible to run it and maintain it.”

DevOps, as [Armory](http://armory.io) CTO [Isaac Mosquera](https://twitter.com/imosquera) explained, is an agile software development framework and culture that’s gaining traction thanks to — well, pretty much everything that Peck said.

Interestingly, Mosquera feels that this approach actually flies in the face of [Conway’s Law](https://en.wikipedia.org/wiki/Conway%27s_law):

> “Organizations which design systems … are constrained to produce designs which are copies of the communication structures of these organizations.” — M. Conway

“Instead of communication driving software design, now software architecture drives communication. Not only do teams operate and organize differently, but it requires a new set of tooling and process to support this type of architecture, i.e. DevOps,” Mosquera explained.

[Chris McFadden](https://twitter.com/cristoirmac), VP of Engineering at [SparkPost](https://www.sparkpost.com/), has an interesting example that might be worth following. At SparkPost, you’ll find decentralized governance — but you won’t find a one-team-per-service culture.

“The team that is developing these microservices started off as one team, but they’re now split up into three teams under the same larger group. Each team has some level of responsibility around certain domains and certain expertise, but the ownership of these services is not restricted to any one of these teams,” said McFadden.

This approach, McFadden explained, allows for any team to work on anything from new features to bug fixes to production issues relating to any of those services. There’s total flexibility, and not a silo in sight.

“It allows [the teams to be] a little more flexible both in terms of new product development as well, just because you’re not getting too restricted and that’s based on our size as a company and as an engineering team. We really need to retain some flexibility,” he continued.

However, size might matter here, as McFadden admitted that if SparkPost was a lot larger, “then it would make more sense to have a single, larger team own one of those microservices.”

“[It’s] better, I think, to have a little bit more broad responsibility for these services and it gives you a little more flexibility. At least that works for us at this time, where we are as an organization,” he said.

### A successful microservices, engineering culture is a balancing act

When it comes to technology, freedom — with responsibility — looks to be the most rewarding path. Team members with differing technological preferences will come and go, while new challenges may require you to ditch the technologies that have previously served you well. Software development is constantly in flux, and so you’ll need to continually balance the needs of your team as new devices, technologies, and clients emerge.

As for structuring your teams, a decentralized, yet un-siloed approach that leverages DevOps and instills a “you build it, you run it” mentality seems to be popular, although other schools of thought do exist. As usual, you’re going to have to experiment to see what suits your team best.

Here’s a quick recap on how to ensure your team culture meshes well with a microservices architecture:

* **Be sustainable, yet flexible**: Balance sustainability without forgetting about flexibility and the need for your team to be innovative when the right opportunity comes along. However, there’s a distinct difference of opinion over how you should achieve that balance.
* **Give equal opportunities**: Don’t favor one section of your team over another. If you’re going to impose restrictions, make sure it’s not going to fundamentally alienate team members from the get-go. Think about how your product roadmap is shaping up and forecast how it will be built and who’s going to do the work.
* **Structure your team to be agile, yet responsible**: Decentralized governance and agile development is the flavor of the day for a good reason, but don’t forget to install a sense of responsibility within each team.

_If you’ve enjoyed this article, please help it spread by clapping below! For more content like this, follow us on [Twitter](https://twitter.com/ButterCMS) and [subscribe](https://buttercms.com/blog/) to our blog._

_And if you want to add a blog or CMS to your website without messing around with Wordpress, [you should try Butter CMS](https://buttercms.com/)._ [ButterCMS](https://buttercms.com/) is a headless CMS that lets you build CMS-powered apps using any programming language including [Ruby](https://buttercms.com/ruby-cms/), [Rails](https://buttercms.com/rails-cms/), [Node.js](https://buttercms.com/nodejs-cms/), [Python](https://buttercms.com/python-cms/), [ASP.NET](https://buttercms.com/asp-net-cms/), [Flask](https://buttercms.com/flask-cms/), [Django](https://buttercms.com/django-cms/), [Go](https://buttercms.com/golang-cms/), [PHP](https://buttercms.com/php-cms/), [Laravel](https://buttercms.com/laravel-cms/), [Angular](https://buttercms.com/angular-cms/), [React](https://buttercms.com/react-cms/), [Elixir](https://buttercms.com/elixir-cms/), [Phoenix](https://buttercms.com/phoenix-cms/), [Meteor](https://buttercms.com/meteor-cms/), [Vue.js](https://buttercms.com/vuejs-cms/), and [Gatsby.js](https://buttercms.com/gatsbyjs-cms/)

