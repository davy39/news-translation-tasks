---
title: Microservices Architecture – Explained in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-23T21:52:08.000Z'
originalURL: https://freecodecamp.org/news/microservices-architecture-for-humans
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/microservices-thumbnail.png
tags:
- name: distributed systems
  slug: distributed-systems
- name: Microservices
  slug: microservices
- name: software architecture
  slug: software-architecture
seo_title: null
seo_desc: "By Charles M.\nOver the last few years, microservices have gone from an\
  \ overhyped buzzword to something you should understand as a software engineer.\
  \ \nAccording to an O'Reilly developer survey in 2020:\n\n61% of companies have\
  \ been using microservices i..."
---

By Charles M.

Over the last few years, microservices have gone from an overhyped buzzword to something you should understand as a software engineer. 

According to an [O'Reilly developer survey](https://www.oreilly.com/radar/microservices-adoption-in-2020) in 2020:

*  61% of companies have been using microservices in the last year
* 29% say at least half of their company systems are built using microservices
* 74% say their teams own the build/test/deploy phases of their applications

These numbers will only continue to increase over time as the ecosystem around microservices matures and makes adoption even easier. 

This doesn't mean you need to be an expert on microservices to get a job, but it is definitely a bonus to at least understand the basic fundamentals. 

The truth is, microservices aren't that hard to understand when you boil it down to the basics. The biggest problem is that most of the resources available are written to impress readers instead of actually educating them. 

Another reason is that there isn’t even a true concrete definition about what a microservice is. The result is that there are tons of overlapping definitions and jargon which leads to confusion for people trying to learn about microservices. 

In this article I will cut through all the chaff and focus on the core concepts of what microservices actually are. I'll use a variety of real world examples and metaphors to make abstract concepts and ideas easier to understand.

Here's what we'll cover:

* Brief history of software design
* Benefits and downsides of monoliths
* Benefits and downsides of microservices

## 4 Minute Microservice Summary

If you prefer a quick introduction to microservices, you can watch this video first:

%[https://www.youtube.com/watch?v=l4tQ66mDfxU]

## How to Understand Microservices with an Analogy of Starting Your Own Business

Let's say you are a software engineer and decide to start freelancing to earn some money. At the beginning you have a few clients and things go smoothly. You spend most of your time writing code and clients are happy.

But over time you start to slow down as the business grows. You spend more and more of your time doing customer service, answering emails, making minor changes for past customers, and other tasks that don't move the needle for you in terms of revenue.

You realize that you aren't optimizing your time as a software engineer so you hire a dedicated employee to handle customer service. 

As you continue to grow you add more employees with specialized skills. You hire a marketer to focus on attracting new customers. You add project managers, more software engineers, and eventually an HR department to help with all these employees. 

This was all necessary for your business to grow beyond what you could do by yourself as a single person, but there are of course growing pains. 

Sometimes there are miscommunications between teams or departments and clients get upset when details slip through the cracks. There is the direct cost of having to pay employee salaries, internal rivalries between teams, and numerous other issues that arise when a company grows larger.

This example is somewhat representative of how a software company might move from a monolith to a microservice type architecture. What starts out with one person doing all the work gradually becomes a collection of specialized teams working together to achieve a common goal for the company. 

This is very similar to how tech companies with monoliths have migrated to microservice architectures. While these examples aren't a perfect 1-1 match for microservices, the general problems are the same:

1. **Scaling –** Ideally you want to be able to quickly hire new employees and linearly scale how productive your company is. 
2. **Communication** - Adding more employees adds the overhead of needing to coordinate and communicate across the organization. There are numerous strategies that companies try to use to make this efficient, especially in this era of remote work. 
3. **Specialization** - Allowing certain groups in the organization to have autonomy to solve problems the most efficient way possible rather than trying to enforce a standard protocol for all situations. Certain customers might have different needs than others, so it makes sense to allow teams to have some flexibility in how they handle things.

## How to Go from a Monolith to Microservices



![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-182.png)

To understand the present it helps to understand the past. Traditionally, software was designed in a monolithic style, and everything ran together as a single application. Like everything else in life, there are some pros and cons to this style of application.

Monoliths aren't inherently bad – and many microservice advocates actually recommend starting out with a monolith and sticking with it until you start running into problems. You can then break your monolith into microservices naturally over time.

## Advantages of a Monolith Architecture

### Faster development time initially

With a small team, development speed can be extremely fast when you're just starting off. 

This is because the project is small, everybody understands the entire app, and things move smoothly. The members of the team know exactly how everything works together and can rapidly implement new features.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-153.png)

### Simple deployment

Because monoliths work as a single unit, things like testing and logging are fairly simple. It's also easier to build and deploy a single monolith compared to a bunch of separate microservices. 

## Disadvantages of a Monolith Architecture

Despite the early benefits of monoliths, as companies grow they often encounter several problems on organizational and technical levels as a result of their monolithic application.

### Tight-coupling of modules

Most companies with monolithic applications try to logically break the monolith into functional modules by use case to keep things organized. Think things like Authentication, Comments, Users, and Blog posts.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-183.png)

The problem is that this requires extreme engineering discipline to maintain long term. Established rules often get thrown out the window when a deadline approaches. This results in shortcuts being taken during a crunch and tangled interconnected code that accumulates as technical debt over time.

> Real world example - Trying to stay disciplined with monoliths is a lot like sticking to an exercise routine or diet. Many people get excited and can stay disciplined with their diet for a few weeks, but eventually life gets in the way and you revert back to your normal routine.   
>   
> Trying to enforce loose coupling with monoliths is like that – there's just too much temptation to cut corners when you get in a time crunch.

### Onboarding new hires becomes hard

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-154.png)

For new hires, becoming productive often takes much longer because they need to learn how all the interconnected pieces of the monolith work together before they can risk modifying any single part of the application. 

It's not unheard of for new hires to say it takes months for them to truly feel comfortable with a massive code base. And there's always the underlying fear that any time you push new code it might blow up the entire app.

> Real world comparison - Training somebody to do a single task like hammer nails vs training somebody to do every single possible task on a construction site.   
>   
> Having to teach a new hire absolutely everything about the entire job increases the cost of hiring new employees.

### Conflicting resource requirements

In a monolith, different modules might have different hardware requirements. Some tasks might be CPU-heavy calculations, others might require a lot of RAM. 

But because the entire application has to run on the same server, you can't use the type of hardware specialized for a certain task. 

> Real world example - Certain types of vehicles are better suited for certain tasks.   
>   
> If you are going on a road trip, a car with great fuel economy would be the best choice so you save money on gas. If you are moving into a new apartment, it would be good to have a vehicle with more space for storage so you don't have to make as many trips. 

### A single bug can take down the entire app 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-186.png)

Because the application is deployed as a single unit, that means that any team can accidentally create a bug that takes down the entire monolith.

> Real world example - To prevent a single leak from sinking an entire ship, bulkheads are used to seal off sections if they start to flood.   
>   
> Microservices work in a similar way – each service is deployed independently from others, which can reduce the chances of a bug taking down the entire app.

### Limits experimentation

When building a monolith, you are pretty much stuck using the ecosystem of the programming language the monolith was written in. A simple example would be the tradeoffs of low level programming languages and higher level programming languages. 

With a microservice architecture, if a certain service is struggling to scale, you have the option to rewrite it in a higher performance language like C++ or Go. 

For other services where performance isn't a huge factor, you can improve development speed by using higher level languages like Python or JavaScript.

A monolith architecture can also blind a team from seeing alternative ways to solve a problem. When you only have a hammer, everything looks like a nail.

> Real world comparison - Pizza is great, but you probably wouldn't want to eat pizza every meal for the rest of your life.   
>   
> Plus in some situations it would also just be inconvenient to cook and eat pizza rather than something else. Sometimes it would be nice to just grab a quick snack or eat something a little healthier.

### Deployments can become slow 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/slow-deployment-drawing.PNG)

One of the strengths of the monolith listed above can eventually become a weakness. The fact the entire app is deployed together can become a problem for massive monoliths because it can result in taking a long time to deploy the entire service. This reduces how fast a team can iterate and make changes to the app. 

Each time they make even a minor change they are forced to wait for the app to build and deploy for testing.

> Real world example- Your dream is to make the world's best cookies. The fastest way to accomplish this goal would be to test as many batches of cookies as possible while gradually changing and improving the recipe until it was perfect.   
>   
> Now imagine you only have 1 oven. The rate at which you can test out different cookie recipes is much slower compared to having 10 ovens.

## Advantages of Microservices

So now that you know the pros and cons of the monolith architecture style, let's examine microservices.

### Development Speed Improves

Because you are no longer deploying a monolith, teams are able to move faster when it comes to adding features. Teams can have independent release schedules and don't have to worry about coordinating with other teams as much. 

As long as the external interface that other microservices use to interact with the team's service stays the same, a development team could completely rewrite the system in another programming language if they wanted.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-184.png)

Another benefit of each service being deployed independently is that builds are faster due to each build being smaller. This means that iteration time is also improved just due to builds being faster.

> Real world example - When you buy food from a restaurant you don't really care if anything changed behind the scenes as long as the food tastes good.   
>   
> Maybe they got new ovens or fryers, but as long as the food tastes the same you don't worry about it. As an external consumer the only thing that matters is the end product.

### Faster onboarding for new hires

New employees can learn a single system to start and begin contributing. Over time they can continue learning more about the entire application but that isn't necessary right away.

> Real world example - The assembly line revolutionized production by breaking things down. Instead of each employee having to know how to create an entire product from scratch, they just needed to learn the single part they worked on. This cut down on training time for new employees and allowed better scale.

### Fault Tolerance

While microservices often do depend on each other to complete tasks, a properly designed microservice architecture will have built-in redundancy and fail safes to prevent failure of the entire system if another service goes down. 

Often this involves retrying requests with an increasing wait period between requests or a default fallback value to return if the service isn't available.

> Real world example - If Netflix's recommendation service breaks, it doesn't make sense to return a complete failure message to users.   
>   
> Instead Netflix could just return a default set of popular movies and in the background keep retrying the recommendation service until it is able to return the user's customized recommendations.

### Flexible Scalability

Because each service is deployed independently you can also replicate and scale each service on its own. With a monolith the company would be forced to scale the entire application, despite only a single feature getting more traffic than usual. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-185.png)

With a microservice architecture, a company can specifically scale only the service that needs to handle more traffic, which is more efficient and can save money because it reduces wasted resources. 

> Real world example- Let's consider something like Cyber Monday for Amazon, way more orders than usual will be placed but most people probably already selected what they wanted and put it in their cart.   
>   
> So while the Orders Service will be getting way more traffic than usual, things like the Search Service and other features might be around normal usage rates. 

This is especially useful if a service is particularly heavy for a certain resource and can use specialized hardware for that task. 

If a service needs a ton of CPU resources but not much RAM, the company can save money by not using general purpose servers. A company using a pure monolith has no choice but to scale using "jack of all trades" type servers.

## Disadvantages of Microservices

Microservices are far from perfect. Shifting from monolith to microservices eliminates some problems while creating new ones.

### Overall Complexity

While each individual service is easier to understand, the entire system itself is complicated. This additional complexity led to the rise of tools like Docker and Kubernetes to abstract away as much of it as possible. 

The goal of these tools is to allow software engineers to not worry about anything other than building features like they normally would, without worrying about how it all works behind the scenes.

### Communication

One of the biggest issues with microservices is figuring out how they communicate with each other. 

A single external request from a user might require several services working together to fulfill that request. Let's use placing an order online as an example of how this might work:

* User places order in app
* Load balancer forwards request to services that are available to process the request
* Shopping cart service gives list of items in the order
* Inventory service confirms that items are in stock
* Shipping service calculates estimated cost and delivery time
* Payment service confirms that customer's payment is valid
* Recommendation service uses items ordered to generate new recommendations for the customer in the future
* Review service schedules an email to ask the customer to leave a review

At any of the above stages a single service failing could result in the entire order process failing or annoyance for the user, which would quickly make for some angry customers. 

Handling how all these services interact and deal with partial failures is a huge challenge with microservice architectures.

### Handling Data

One of the most difficult challenges with microservices is how to handle requests that span multiple services and require making updates to data. 

What happens if a request fails part way through the sequence with data updated in one service but not the rest? You don't want to bill a user but then have them not receive what they paid for because the service was down.

In a monolith you can rely on ACID transactions to rollback a database change if something goes wrong. With microservices there is much more complexity involved with what are known as distributed transactions across services.

### Development environment

Most tools were designed with monoliths in mind and development in general becomes more difficult with a microservice architecture. 

Testing requires being able to simulate interactions with other services, Debugging is more difficult because things are no longer happening inside a single process, and logging must be done across multiple services.

Even something simple like trying to track why a blog is loading slowly is more difficult than you might expect. 

Let's say you notice on your analytics that all of a sudden it's taking 5 seconds for pages to load on your blog. With a monolith it would be pretty easy to track down the problem, but with a microservice architecture you need specialized tools to track external requests as they are processed by different services.

## Conclusion

Hopefully this article gave you a decent understanding of the what and why of microservices and an intuitive understanding of how they work, even if you don't understand all the technical details under the hood.

If you are interested in seeing future videos and articles on microservices be sure to [subscribe on YouTube](https://www.youtube.com/channel/UCzYV9nBadlQdBMPP2ZuDvKA) or [follow on Twitter](https://twitter.com/Ren_Engineer) so you don't miss anything.

