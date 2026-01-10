---
title: 'DevRel Down the Stack: Containers, Kubernetes and DevOps Engineers'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-18T10:30:00.000Z'
originalURL: https://freecodecamp.org/news/devrel-down-the-stack-containers-kubernetes-and-devops-engineers
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/marek-devrel-banner.jpg
tags:
- name: containers
  slug: containers
- name: developer-advocacy
  slug: developer-advocacy
- name: developer relations
  slug: developer-relations
- name: Kubernetes
  slug: kubernetes
- name: Swift
  slug: swift
- name: Swift Programming
  slug: swift-programming
seo_title: null
seo_desc: 'By David Nugent

  IBM’s $34B acquisition of Red Hat closed last week, underscoring the huge and growing
  importance of  hybrid cloud infrastructure. My colleague Marek Sadowski has become
  a  subject matter expert in containers, Kubernetes and server-sid...'
---

By David Nugent

IBM’s [$34B acquisition of Red Hat](https://newsroom.ibm.com/2019-07-09-IBM-Closes-Landmark-Acquisition-of-Red-Hat-for-34-Billion-Defines-Open-Hybrid-Cloud-Future) closed last week, underscoring the huge and growing importance of  hybrid cloud infrastructure. My colleague Marek Sadowski has become a  subject matter expert in containers, Kubernetes and server-side Swift,  although he started out as a full stack developer advocate, a robotics  startup founder and an entrepreneur.

![Marek lecturing](https://res.cloudinary.com/practicaldev/image/fetch/s--LGWhCAWn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/gr6qrvfie9qrbx21gy4o.jpg)

Marek has 20 years of enterprise consulting experience throughout the  USA, Europe, Japan, Middle East and Africa, and he pioneered in  research on VR goggles for the virtual reality system to control robots  on Mars during his time at NASA. After founding a robotics startup,  Marek came to work at IBM. I talked to him about his experience in  DevOps advocacy.

## Table of Contents

* How DevOps advocacy different from API/app advocacy?
* How do you focus on the DevRel community?
* What have you changed when moving to DevOps DevRel?
* How do you get developers to see Swift as server-side?
* How did you get into DevRel?

![Marek lecturing](https://res.cloudinary.com/practicaldev/image/fetch/s--OCVtuwPo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/x0ccbjsy1k941giianl7.jpg)

### Q: One of your focus areas in DevRel is containers. How is advocating  for a DevOps technology different than advocating for an API or  application?

Good question. When working with containers, engineers think more in  terms of the plumbing and ideas of DevOps and the ease of expanding your  infrastructure footprint. In contrast, when you talk about APIs, you  try to make application development the center of gravity for the  discussion.

When discussing APIs with developers, you talk about how one could -- in a robust way -- consume the API. Let’s take the [IBM Watson API](https://ibm.biz/BdzKG5) as an example: our team will talk about how you can create and run SDKs  for developers to consume APIs in their own language, for example,  Swift (for mobile) or Java (for enterprise.) You’d look at the consumer  of your API and discuss how you can produce the API, protect yourself  and do the billing.

Getting back to containers: when discussing container technology, you speak more about _plumbing_ of the cloud. How do you manage containers? Expand them? Manage their workloads? Deliver and test new versions?

It quickly becomes apparent that these are two separate concepts.  Containerization deals with how your backend is working and proper  maintenance of your application, which attracts people from a DevOps  background. When you talk about APIs, that’s a completely different  story. Your thought paradigm changes to the point of view of the  consumer: How does the consumer find the API? How can developers consume  the API?

I speak at conferences on both subjects areas. I’ve found that people  who develop applications are more interested in the look and feel and  developer experience of the application, whereas with containers it’s  more about backend, load balancing, and seeing issues from a system  administrator’s perspective.

### Q: Many people are familiar with DevRel with a focus on software  engineers, but DevOps is a different community entirely. How do you  focus on that community?

There is a division — everybody is interested in new things like  Kubernetes and Docker, but not too many will want to perfect their  skills to the point that it’s their daily job. So many developers want  to know how to spin up a container and a service inside the container,  put it in their resume and be done with it. Developers may be interested  because it’s fashionable or it’s a buzzword. However, you can find a  lot of people who are running services in containers and have specific  questions: sysadmins who want to monitor containers and assure security,  load balancing, and other aspects of administration. It’s a completely  different audience from developers who consume APIs and create a cool  web application. They are two different communities, and you have to  give each community different content.

For example, in a hackathon it’s very difficult to create large  deployments in containers. It’s an optimization of development and  operations more than application coding.

![The IBM SF City Team staffing a booth](https://res.cloudinary.com/practicaldev/image/fetch/s--eA1r0etR--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/9sh0o5no0f09pjbj31qk.jpg)

### Q: How have you had to change your approach to DevRel when moving to DevOps advocacy?

Previously when I ran workshops focused on application developers,  they’ll usually have a few goals: understand our API, consume data from  API endpoints and create a simple “Hello World” types of applications.  Developers in these workshops will ask questions about high-level ways  of architecting applications, e.g. with Watson, in mobile applications  or web applications, or a chain of processes.

On the contrary, when I speak about DevOps and containers, developers  in the audience want to spin up the services, see how they scale up and  scale down, investigate how the services behaving when something is  failing and how to ameliorate security issues. It’s a completely  different approach. They are not interested in building something new,  they want to perfect their approach to deployment.

An analogy I can give to people new to this field: it’s like inviting  a painter and a plumber to a party. They both do similar things, yet  the painter wants to make a painting that you can hang on the wall, and  the plumber will rarely speak about the type of piping he’s using inside  your walls. Both are doing something in your house, but the painter is  thinking about the people they will attract and the paint (our APIs) to  ensure a pleasant viewing experience, while the plumber just wants to  get the job done and never touch it again. The plumbers want to make  changes as rarely as possible and focus on stability, the painter wants  to create more new paintings. They have different approaches based on  their different goals.

### Q: You also give talks on Swift, specifically on the server side. Most  people know Swift from the iOS development side, but why is it useful  on the server? How do you get developers to think of it as a server  language?

Server-side Swift is a relatively new development. I compare the  current state of server-side Swift to where Java was twenty-four years  ago. In 1996 I started writing a server-side application using Java --  it was a novel concept at that time! The same thing is happening now  with Swift, as developers are moving the Swift language to the server.  There are a lot of reasons why; one of the simplest is that you write in  the same language on the server as you do for your mobile app, and in  that way you can use the same data constructs, thought processes and  personnel resources on both systems. You don’t need different systems or  frameworks to talk to the database or the cloud.

Every mobile app nowadays asks you to connect to the internet for AI,  messaging and social media. Even simple games allow you to exchange  information or have a conversation with people all over the world. If  your app and back-end are written in one language like Swift, it makes  these data exchanges simple and transparent.

Some people are saying _Swift is a fashionable language to learn_.  Since you have the option to write apps in Java or JavaScript, you can  also write them in Swift. Swift has now been open-sourced by Apple,  similar to the way Sun opened up Java. You can now write applications in  the cloud or on any platform. For example, OpenWhisk allows you to  write event-based Swift functions in the cloud without any DevOps code.

With Swift, developers are attracted to the beauty of the language  and the ability to write one language from mobile to cloud to make your  application better and easier to maintain. You can enjoy writing in your  language of choice and expand the capabilities of the environment you  love. If you are an iOS developer, maybe you can become a full-stack  developer, and developers love the story that they can become something  more and participate in the full stack development process.

![Marek](https://res.cloudinary.com/practicaldev/image/fetch/s--SlcpOzfS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/chlb5mirpmyo4jher7bp.jpg)

### Q: How did you get into developer relations?

I had just come to the United States from Poland as the founder of a  startup, and the purpose of the move was to expand my company. They say  that 99% of startups don’t succeed right away, and founders often need  to bootstrap while in an existing job. I was told that working in the  cloud is the key factor in a lot of industries, but I had little  exposure to those technologies. On the other hand, I had built up skills  talking to investors, and as an entrepreneur, I was able to understand  what was important to startups. I also had a robust background in Java  development and different IT technologies — I had a career as an  architect supporting banks and other enterprises EMEA as a Java  professional, demonstrating systems to customers.

There was an opening for a mobile-first developer advocate, and  despite having no mobile or cloud experience, I convinced the  interviewer that I was the perfect candidate due to my ease of speaking  with developers and presenting technical subjects in an accessible  manner. I enjoy explaining complex topics in a simple way through demos  and example projects.

My hiring manager asked me to build a small mobile app as an employment test, which connected to [IBM Cloud](https://ibm.biz/BdzKGU) to exchange information between the user and a backend. I enjoyed the  task and found I was good at it! After two years, I migrated to more  cloud technologies and more and more IBM APIs. Eventually I started to  find interest in Kubernetes and containers, and I realized containers  are a field with amazing growth potential.

I must say, the thing that attracted me the most to DevRel was the  opportunity to learn and convey new technologies to developers out  there, and use my talent for explaining complex things in a  straightforward manner.

![Marek snowboarding](https://res.cloudinary.com/practicaldev/image/fetch/s--q3yO1Vrc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/eccad3abeiluyjgz8i8b.jpg)

###   [](https://dev.to/drnugent/devrel-down-the-stack-containers-kubernetes-and-talking-to-devops-engineers-hm7#next-steps)    Next Steps:

* [Follow Marek on Twitter](https://twitter.com/blumareks)
* See Marek speak at an upcoming [IBM Developer SF Meetup](https://www.meetup.com/IBM-Developer-SF-Bay-Area-Meetup)

