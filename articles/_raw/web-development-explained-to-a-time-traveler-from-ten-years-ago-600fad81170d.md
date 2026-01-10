---
title: Web development explained to a time traveler from ten years ago
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-16T12:15:54.000Z'
originalURL: https://freecodecamp.org/news/web-development-explained-to-a-time-traveler-from-ten-years-ago-600fad81170d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1IogdXEkHf5_6iQlULXD7g.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ivan Zarea

  Hello friend! I hope you like this new world of ours. It’s a lot different than
  the world of 2007. Quick tip: if you just got a mortgage, go back and cancel it.
  Trust me.

  I’m glad that you’re still interested in computers! Today we have...'
---

By Ivan Zarea

Hello friend! I hope you like this new world of ours. It’s a lot different than the world of 2007. Quick tip: if you just got a mortgage, go back and cancel it. Trust me.

I’m glad that you’re still interested in computers! Today we have many more of them than we did 10 years ago, and that comes with new challenges. We wear computers on our wrists and faces, keep them in our pockets, and have them in our fridges and kettles. The cars are driving themselves pretty well, and we’ve taught programs to be better than humans at pretty much every game out there — except maybe drinking.

### (Web) Apps

You might have seen the release of the iPhone just before you stepped into the time booth. Apple is the biggest and richest tech company, mostly due to the iPhone and its operating system, iOS. Google has this competing thing called Android, and Microsoft tried to get a slice of the ever-growing pie with Windows Phone. It didn’t work out.

![Image](https://cdn-media-1.freecodecamp.org/images/lWpOHm-nPZ5N2bTf7lgFGuLLuL56A-zWsyeT)
_Left: a hand holding an iPhone 3GS from 2008. Right: a similarly-sized hand holding a larger iPhone X from 2017. We also got to practice doing over-the-shoulder shots. Left: [BusinessInsider](https://www.imore.com/iphone-3gs" rel="noopener" target="_blank" title="">iMore</a>, right: <a href="https://www.businessinsider.nl/is-the-iphone-x-worth-1000-2017-9/?international=true&amp;r=US" rel="noopener" target="_blank" title=")_

We started calling programs **apps,** and some websites are calling themselves **web apps**. In 2008, Google released a new browser called “Chrome.” Nine years later it’s the most popular way to get on the Web.

The Chrome team invested a lot in working with JavaScript, and the code gets better every month. Web apps are written using a lot of JavaScript, and they resemble the desktop interfaces of your time.

Companies have also invested in JavaScript to make it better—it now supports classes and modules. We use languages that **compile** to JavaScript, like [TypeScript](http://www.typescriptlang.org/) (from Microsoft, they’re cool now) or [Flow](https://flow.org/).

We write a lot of JavaScript these days, since nobody supports Flash anymore. We even run JavaScript on the server, instead of Perl, using a thing called Node. It sounds easier than it is.

![Image](https://cdn-media-1.freecodecamp.org/images/RgPMXomN0HWC8N4NcZmxUtxtJRMAaX57rYVy)
_A responsive design: the same website shows differently on multiple devices. We’re still bad at it, but we have found pretty ways to show it off. Source: [10twelve](https://www.10twelve.com/squarespace-template-jasper/" rel="noopener" target="_blank" title=")._

Remember Swing, SWT and the likes of wxWidgets? We had to reinvent them for the browser world. Several new UI programming models emerged, which mostly focused on **components**.

We had to find a way to design, build, and test apps while keeping them responsive (a term we use to describe a website that doesn’t look like crap on a mobile phone). We also needed to keep it slim — not everybody has a fast connection, but everybody has a browser in their pockets.

To help with all this, there are now **component frameworks**. The term is vague, since it includes the likes of [Angular](https://angular.io/) by Google, [React](https://reactjs.org/) by Facebook, and [Vue](https://vuejs.org/) by the community. But it’s the best term we have.

By the way, I’m not sure you remember Facebook from 2007. It was getting big in the US around that time, and now it’s bigger than huge. Boasting more than a billion users, it’s also one of the largest codebases in the world.

The Facebook development team writes a lot of great code and publishes it online. They have their own conference, F8. Most big companies have their own conferences.

CSS also had to evolve, since the new apps require more intricate layouts. We don’t use tables with images anymore. Frames are gone as well. Instead, we have created new standards, like CSS Floats, Flexbox, and CSS Grid.

People had to iterate on these standards, and they’ve built libraries to make things look consistent, like [Bootstrap](http://getbootstrap.com/), [Foundation](https://foundation.zurb.com/) and many more. Similar to JavaScript, we have created languages that **compile to** CSS. They make up for some of the things that CSS misses, like variables or modules. It’s still hard.

### It’s okay to be lost

Don’t feel bad if you’re confused. The truth is that we’re all a little confused — and it’s okay to be so. There are many more developers on the planet now, and tech companies are becoming more successful. For a while we used the term “startup” to describe companies that grew quickly and didn’t know what to do. But even this term has become old.

### Data

There are more programmers, more programs, and more devices. We have more **data** now. Computers had to grow powerful enough to process it all, and we have developed several techniques to turn that data into insight.

First, we created a field called Data Science, which aims to learn about and extract information from data.

For example, a startup called Waze let people install an app on their phones that would track their movements while they were in their cars. Because many people installed the app, Waze got a lot of data about how cars move. They used it to develop programs that understood where traffic jams were.

Now, when you open Waze on your phone, you see traffic jams on the map **in real time** and choose another route.

Waze has since been bought by Google. This happens a lot with startups.

![Image](https://cdn-media-1.freecodecamp.org/images/noQhuQUHeDAJAq3VBb2QfaWnGUysmK1-IHKm)
_Somebody using Waze to get to somewhere. The other Waze users are shown as funny icons. Source: [The waze blog.](https://blog.waze.com/2014/07/waze-releases-new-version-381.html" rel="noopener" target="_blank" title=")_

There were three main challenges with Data Science — storing data, understanding data, and acting on data. We’ve improved in all of these areas. Let’s look at each one.

### Storage

We now need to store a lot more information and then find out which part is important. We needed to invent new databases. The likes of MySQL and PostgreSQL weren’t fit to store terabytes of data (we called it **Big Data**).

Big, internet-first companies typically faced these challenges, and so they were on the forefront of developing the technologies. Most of the time, technologies were first used internally and then open-sourced.

There was a movement we called NoSQL. This new class of databases took some of the conventions of traditional Relational databases and turned them around.

There’s [Hadoop](https://hadoop.apache.org/), which deals with how the data is stored on many hard computers. It defines a way of processing the data called MapReduce (inspired by a paper from Google — big companies write good scientific papers these days).

Then there’s [Cassandra](https://cassandra.apache.org/), which looks at data not as tables, but as sets of keys and columns which can be stored on different computers. It also makes sure that any of these computers can go offline without causing data loss.

And we have [MongoDB](https://www.mongodb.com/), a database that is easy to install and use for prototyping apps. In 2017, we’re treating technologies the same way we treated pop stars ten years ago — we zealously defend some of them and vehemently hate others. MongoDB — like the band Nickelback — belongs to the latter group.

### Learning

![Image](https://cdn-media-1.freecodecamp.org/images/LC1X-wryPqqiEIBv5NEO07nZufcBS1U27SjJ)
_A dog photographed through Prisma, an app that uses machine learning to make ordinary pictures look like famous works of art. No more Photoshop Plastic Wrap. Source: [cultofmac](https://www.cultofmac.com/435997/popular-prisma-app-turns-iphone-photos-into-painterly-masterpieces/" rel="noopener" target="_blank" title=")._

In the “understanding data” camp, most of the focus has been in an area called Machine Learning. There have been many new techniques, from naive classification to deep learning, that are now in every Data Scientist’s toolbox. They mostly write Python and work alongside developers to put machine learning pretty much everywhere.

For example, with the help of Data Scientists, a lot of web apps use A/B testing. This technique serves two slightly different versions of the app to different, but similar, groups of users. It is used to see which version leads quicker to our desired goal, whether that’s a sign-up or a purchase.

A lot of big companies like Airbnb (pronounced _air-bee-en-bee_), Uber, and Netflix are running hundreds and thousands of A/B tests at the same time to make sure their users get the best experience. Netflix is an app where people can binge-watch TV shows on all their devices. `¯\_(ツ)_/¯`

### Microservices and The Cloud

Companies like Netflix are enormous. Because they serve a lot of people, they have to make sure they are up and running at all times. That means they have to manage their computers pretty well. They can add hundreds of new servers when they’re needed.

This is difficult to achieve in a traditional data center, so the amazing engineers at Netflix use virtual machines. Remember Amazon Web Services, which launched back in 2006? Back then, they started offering **Elastic Cloud Compute**, known as EC2, to help people get virtual computers in Amazon’s data centers.

Today, they have almost 80 similar services, all built to help companies grow quickly. We used to have a trendy name for that — “The Cloud” — but this term is as difficult to define as NoSQL.

![Image](https://cdn-media-1.freecodecamp.org/images/bZ73QweU2qSLxOsMwHi1rkQWLG94NZUGPy-z)
_This is the list of services you can find on Amazon’s cloud. It’s still growing._

Google and Microsoft offer their own clouds, creating a market for cloud services. And when smart people compete with each other, all sorts of crazy innovation starts happening.

First of all, we started thinking more about our infrastructure as code. Previously, you had to buy a new server, plug in a keyboard, and install dependencies.

Now we use configuration management tools like [Puppet](https://puppet.com/), [Chef](https://www.chef.io/chef/), and [Ansible](https://www.ansible.com/) to automate our servers. You write actual code, in languages like Ruby, and **provision** servers based on the configurations. If a change is needed, you edit the configurations and then update the servers. No more SSH.

Then we started looking more at containers. Because it was possible to provision machines on EC2, we needed to develop on similar environments as our production ran in.

We started with virtual machines, using tools like [Vagrant](https://www.vagrantup.com/) to automate them. But then we got Linux containers and, eventually, Docker. We found a way to run Linux on our MacBooks without running a full virtual machine, sharing some of the OS-related operations.

Using Docker, we could create descriptions of systems that matched exactly what we were running on production. Developers called these descriptions **images,** and started running their apps in somewhat-virtual instances called **containers**.

![Image](https://cdn-media-1.freecodecamp.org/images/LgUIPiYN4qHutvy8AhLdZuHVA62OEQ1aAyK9)
_By the way, we like MacBooks a lot. And this is the audience of a Windows 10 launch conference. Source: [reddit](https://www.reddit.com/r/funny/comments/2t6sut/a_sea_of_macbooks_at_the_windows_10_unveiling/" rel="noopener" target="_blank" title=")_

Then cloud providers caught up to this and let us run our containers directly on their clouds. They gave us tools like [Marathon](https://mesosphere.github.io/marathon/) and [Kubernetes](https://kubernetes.io/), called **orchestration frameworks**. These frameworks let developers run apps inside containers without worrying about scaling, fault-tolerance, monitoring and discovery. The servers became disposable, and we don’t give them clever names anymore.

This also allowed developers to build small apps, called services or microservices, and then run them independently. Because these microservices have few external dependencies, we started looking into using new programming languages, like [Go](https://golang.org/) (which was created to make concurrency bearable) and Java. Yes, Java is still around and it got better.

There are also languages like [Scala](http://www.scala-lang.org/) and [Clojure](https://clojure.org/) that let us use the Java Virtual Machine and all related libraries. A website like AirBnB runs hundreds of microservices using several programming languages and databases.

Because of these microservices, we had to revisit some of our programming models. We now have much more, much smaller apps that we have to coordinate.

As a result, there are tools like [Apache Kafka](https://kafka.apache.org/), [Google PubSub](https://cloud.google.com/pubsub/), and [RabbitMQ](http://www.rabbitmq.com/) that aim to help with chatty computers that talk to each other a lot. Kafka was created by LinkedIn, a social network where people advertise their professional life. It was later open-sourced.

### The way we build our software

The extra complexity introduced by the orchestration frameworks is mostly relevant for larger teams. Remember — we currently have more people building software than ever before, and every programmer wants to ship their code right away. If you have a company with hundreds of developers working together on a website, you need to make sure they don’t have to coordinate their releases.

So we build software in small teams. The teams usually have some **DevOps** skills, and members know enough about operations to be able to deploy their software. They use some form of an Agile process, where they release software continuously in short iterations. Organizations also experiment with other forms of hierarchy, like [Squads, Chapters, Tribes, and Guilds](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/), as Spotify (that’s a new music streaming service) does.

All these projects (and many others that were mentioned before) are developed publicly by a community of people. Sometimes they’re sponsored by a company. Most of the time, development goes on a website called [GitHub](https://github.com/). There, people can talk about software, build it publicly, and approve contributions by replying with a ? emoji. An emoji is a special character we now use to express an emotion, such as approval. :-)

There are many more communities now, and they are all experimenting with ways to build software in the open. For example, a web framework called EmberJS uses a [community-driven,](https://github.com/emberjs/rfcs) 6-week release cycle. Other languages and popular open source software (like [GitLab](https://gitlab.com/gitlab-org/gitlab-ce) and [Visual Studio Code](https://github.com/Microsoft/vscode), a code editor from Microsoft) use a monthly release cycle to make sure they don’t deliver fully breaking changes. The packages break just a little every release.

Oh, and the editor wars are still there. We’re writing our code in desktop apps that run a browser that shows a text field. And it’s great. It performs pretty well (gets better with every release) and is heavily customizable. It even has some support for VIM mode!

![Image](https://cdn-media-1.freecodecamp.org/images/sfrdpq8IIO2MIBScOHWBv-QYq-Kygz5r-nAn)
_RailsGirls is an initiative that opens the world of web development to many women. Here the workshop participants in Sofia, Bulgaria give the internet a Friday Hug — a popular gesture in the Ruby community. Source: [Railsgirls](http://railsgirls.com/sofia.html" rel="noopener" target="_blank" title=")._

Conferences are held on every topic. They’re fun, and they’re everywhere. Go to one — you’ll see all sorts of people! Make some friends, goof around, get inspired, speak out. Maybe go to an [algorave](http://mixmag.net/feature/algorave) show — what they do with music, images, and code is breathtaking.

### There’s more!

There’s more people, software, and innovation out there. I hope you’re still as excited about computers — you have all the reasons to be.

Let’s go get a Club Mate and I’ll tell you about this Bitcoin thing. Also, the US has a new president now…

If you enjoyed this article, please give me some claps so more people see it. Thanks!

