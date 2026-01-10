---
title: 'Ordering Take Out: How to Eat a Scary Monolith'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T22:45:34.000Z'
originalURL: https://freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6fjILAnGqbbPAvkPfZOzvg.jpeg
tags:
- name: Microservices
  slug: microservices
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alan Ridlehoover

  Martin Fowler said:


  Almost all the successful microservice stories have started with a monolith that
  got too big and was broken up.


  You can add our story to that list.

  My team and I just built a new messaging service. It replace...'
---

By Alan Ridlehoover

Martin Fowler [said](https://www.martinfowler.com/bliki/MonolithFirst.html):

> Almost all the successful microservice stories have started with a monolith that got too big and was broken up.

You can add our story to that list.

My team and I just built a new messaging service. It replaced an aging subsystem in our primary application. We modeled the new service on real-life concepts. This simplified the data model considerably, unlocking new features that would have been a challenge to build in with the old data model.

Along the way, we learned a few things which we’d like to share…

![Image](https://cdn-media-1.freecodecamp.org/images/MaXabuxVfnzuqOetILf5NhS1fmlts8AbyCLo)

### Our worst-case, most pessimistic estimate was wildly optimistic

Our most conservative guess for how long it would take to complete the project was three months. It took ten.

To be fair, we estimated that the entire team would take three months to complete the work. But, in reality, we took on several projects at once. We continued ongoing maintenance of the legacy subsystem, and even added new features. So, given less than half the resources, the original estimate should have been longer.

That said, we did underestimate the work. We underestimated the work related to disentangling the subsystem from the monolith. We started out searching for references to classes owned by the subsystem. We ended up looking at SQL queries that referenced the underlying database tables. That’s how tightly coupled the subsystem was to the rest of the application.

**Lesson learned:** Pay attention to _all_ the integration points. There are likely more than you think.

![Image](https://cdn-media-1.freecodecamp.org/images/jcZnblemwjZBQ2trF9dpJWd5haPFYbphLrow)

### Build a moat around the subsystem in the monolith

In _Domain Driven Design,_ Eric Evans describes a pattern called the Anti-Corruption Layer. This layer is a wall between two subsystems. Neither subsystem talks to the other directly. They both talk to the wall. Following this pattern prevents the subsystems from bleeding into one another.

For us, other subsystems had metastasized into ours. We needed a way of disconnecting them without modifying their functionality. We looked to the Anti-Corruption Layer for inspiration.

Our solution: we wrapped a façade layer around our subsystem within the monolith. This placed a moat around the subsystem, preventing access except through defined interfaces. It also allowed us to integration test the calls to the façade. We kept those tests passing throughout, even after cutting over to the new service.

As mentioned above, this was by far the most difficult piece of extracting the service. Pulling half of a raw SQL query behind a façade is hard work:

First, you have to understand the entire query, some of which were hundreds of lines long. Next, you extract the bits of the query that access the old subsystem. And, then, you convert them into the new data model. You extend the new service to support this new query. Finally, you integrate the results with the remainder of the original SQL query. If you do it right, the calling code never knows the difference.

**Lesson learned:** When constructing an application, it is important to maintain boundaries. Encapsulation is important. That point is obvious outside the monolith. But, it is even more important _inside_ the monolith. It’s the only way to keep the system pliable, so you can make room for new features through refactoring.

![Image](https://cdn-media-1.freecodecamp.org/images/rAlpgJ4-e13zDCzGJAFxfRsqwjneOWivEEuN)

### Run both systems in parallel

We ran both systems in parallel for months while we worked toward feature parity. We could do this because we created the façade mentioned above. We sent requests to the façade through both the legacy subsystem and the new service. Comparing the results enabled us to find (and fix) data inconsistencies. It also gave us a real-world stress test against live production data.

**Lesson learned:** We found most of our bugs this way. There’s no substitute for production workloads. We admit that this increased development costs. But, finding the bugs before we put the system in production was worth every penny.

![Image](https://cdn-media-1.freecodecamp.org/images/oBKskiY3Cni6yDQfCtAj50HcvrzKg7riCrdz)

### Use feature flags to stage rollout

A feature flag is a boolean value that enables a feature when on, and disables the feature when turned off. Typical feature flag systems allow you to turn the flag on for subsets of your users. This allows you to roll out functionality gradually, rather than all at once.

Our implementation used four separate flags:

* One flag controlled whether to write to the new system. This allowed us to run the systems in parallel. We turned this flag on very early in the process, giving us the benefits described above.
* Another flag controlled whether to read data from the new service. This way we could test the functionality before enabling it globally.
* The last two flags controlled which system could access our third-party email providers. One flag turned off the legacy subsystem. The other turned on the new service. We separated these flags so we could turn both systems off at the same time, in the event of a major problem. (We did not end up exercising this functionality. But we’re still glad we built it.)

Finally, using feature flags allowed us to roll out the new service to one customer at a time. This reduced risk and prevented undue disruptions to the business.

**Lesson learned:** Use separate feature flags for writing to and reading from a service. This allows you to begin running the service in parallel with the legacy system. And, in our case, adding the extra flags to prevent duplicate emails from being sent was critical.

![Image](https://cdn-media-1.freecodecamp.org/images/z5ciHTnv-lW9AORCgzx9pdiHcubvX9EAsiNV)

### Add logging, exception handling & monitoring early

One of the first things we built inside the new service was a logger. Next, we added exception handling. This turned out to be crucial when debugging the system. We found it especially useful across the service boundary.

We added monitoring later to give us a window into our data import process. Adding it was easy because of our centralized logger.

**Lesson learned:** Centralize your logging and exception handling, and build it early. You’ll thank yourself later.

![Image](https://cdn-media-1.freecodecamp.org/images/HZWJyhA6TsmtkdSHRcIoVRO6vnzzIxSLwG6V)

### Expect issues migrating your data

We decided to port our data into the new service, so there would be one system of record. We did this by sending messages to the new service, thus testing the interface under heavy load.

The vast majority of the data migrated correctly. But there were many valid edge cases. Each time we would figure out one of the edge cases, we would adjust the migration and run it again.

In the end, we had about 700 records (out of 1.2M) left over that we could not explain. The vast majority were several years old. This data did not fit any of the corner cases we’d identified and resolved. After spending a couple of days on it, we decided to mark the records as “failed” and move on.

**Lesson learned:** Production data is sloppy. Most of it will look correct. Some of it will not. The older the data, the harder it is to migrate. Records will be missing. Foreign keys won’t exist. Just roll with it. Make the best, most user friendly decisions you can.

![Image](https://cdn-media-1.freecodecamp.org/images/4etUQXX-ktD33z-PoW3dgJgYmjwibMCn2ZAP)

### Use deterministic UUIDs and idempotent migrations

When you have two different systems running in parallel, you need a shared id space. Any UUID will do. But we chose to use deterministic UUIDs to support idempotent migrations. To generate a deterministic UUID, you provide a namespace and some unique attribute. Given the same data, the algorithm always produces the same UUID.

In our case, the façade in the main application generates the deterministic UUIDs. Then it sends the UUID to the service for storage. Inside the service, we indexed that field to prevent duplicates. This makes idempotency possible.

**Lesson learned:** Your production data will be unpredictable. As you resolve corner cases, you will need to run your migrations over and over. Using deterministic UUIDs makes this possible.

![Image](https://cdn-media-1.freecodecamp.org/images/RaN-4SHUcVD7X8ohmabLvlA933hVU6J6mBvB)

### Use queues

Introducing a new service means introducing another point of failure. We wanted to protect ourselves from minor service outages. So, we decided to communicate with the service via a queue. By using a robust queue, we achieved a bit of fault tolerance should the service ever go down. We also chose a FIFO queue to guarantee the order of operations. This prevents an update from preceding a create, or following a delete. This also allowed us to speed up our data import process by scaling horizontally.

**Lesson learned:** There are several advantages to using a robust queue. Fault tolerance lends peace of mind. And, horizontal scaling enables you to keep up with demand.

![Image](https://cdn-media-1.freecodecamp.org/images/3PnX0cTLctAh7DBHQoyxPycmOExnNxZga7zq)

### Use circuit breakers

Reading data asynchronously via a queue requires the caller to understand asynchronous callbacks. JavaScript is, of course, quite good at this. But, Ruby is not. And, in this case, it is the monolith calling the service via a queue.

Consider a request from the front-end to fetch some data. The monolith would receive that request and place a message on a queue along with a correlation id. The service would then reply (on a different queue) with the results and the same correlation id. But, the worker that processes the response would not have a handle on the request. So, now you’d need to push the data to the front-end (most likely using sockets).

In other words, we would have had to rewrite our front-end to receive data via sockets. f. Unfortunately, we did not have time to rebuild the front-end of our application to work this way. So, we chose to use HTTP for read operations. This worked well, until it didn’t.

During testing, a bug in the deployment process took the new service down. This prevented the monolith from loading in our staging environment. Why? Because we were bootstrapping data from the service when we loaded the first page. Since the service was down, the requests were all timing out. The solution was to use the circuit breaker pattern.

Circuit breakers wrap calls to external services. If the call works, nothing happens. But if the call fails with certain exceptions (like a time out or a server error), the circuit breaker trips. While tripped, the circuit breaker won’t call the service. Instead, it returns a hard-coded return value like `nil` or `[]` or `{}` during a cool down period. Once the cool down expires, the circuit breaker starts calling the service again. If it’s back up, great! If not, the circuit breaker trips again.

**Lesson learned:** If you must use HTTP, protect the broader system from service outages. Circuit breakers are one mechanism for doing this.

![Image](https://cdn-media-1.freecodecamp.org/images/mTAX0RC7RdFhjIeyJmJoAROtssQliybEWTll)

### Executive Sponsorship

The success of long term projects often comes down to executive sponsorship. We were fortunate that both our VP of Product and our VP of Engineering were on board with our plans. They put a great deal of trust in us. And when the project began to look bigger than we’d planned, they stood by us. We could not have completed our work without their support.

Why were our executive sponsors willing to go to bat for us? Several reasons. But one of the most important is that we were open and honest in our communications with them. They knew where the project was and they knew what we needed to do.

**Lesson learned:** When embarking on a long-term, high risk project, make sure you have the support of your leadership. Make sure they understand the benefits as well as the risks. And, communicate continuously. It builds trust, which you’ll need if you’re going to succeed.

### What would we do differently?

We thought we did our due diligence before proposing the project. We found every reference to the models used in the subsystem. But we did not search for direct references to the underlying table names in raw SQL statements. That was an oversight. We will definitely do that next time.

If we could go back in time, we would isolate the old subsystem _within_ the monolith. Encapsulating the subsystem would simplify the extraction process. In fact, it may even have made it unnecessary, since we could have be able to refactor in place.

### So, would we do it again?

It was a long journey, for sure. Extricating our subsystem from the monolith was more difficult that we predicted due to some truly epic coupling. We did the decoupling work out of necessity. It was not enjoyable. It felt like a chore.

But, working with the new service is a dream. The code is very well factored. We have super high test coverage. And, we have well defined domain logic that corresponds to specific use cases. So, we can tell what the application does by looking at a single class. This means that extending the service is as simple as adding another domain class and tests for it.

But, would we do it again?

As engineers? We would definitely do it again. The project led to large improvements in developer productivity and happiness. The trade-off was worth it for us in job satisfaction alone. In fact, we already see opportunities for extracting several small services.

As an organization? We are very happy with the results we achieved. Customers are happy we’re shipping long-requested features we were unable to ship before. Management is happy that there have been no production issues. And, the team is thrilled to be free of the monolith.

That said, this project was a significant investment for us at our stage. We will need to see a strong return before taking on another large scale bet on service extractions.

A version of this article was first published on [SourceCode](https://sourcecode.entelo.com/), our blog about engineering in the recruiting industry.

I’d like to thank [Fito von Zastrow](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined), [Jason Rosendale](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined), [Ryan A Booth](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined), and [Cole Goeppinger](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined), all of whom made invaluable contributions to this article.

And, thank you! You win a prize for reading this far. Mention this article to me IRL for a free sticker!

