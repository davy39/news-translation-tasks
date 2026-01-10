---
title: These are the most effective microservice testing strategies, according to
  the experts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T20:15:24.000Z'
originalURL: https://freecodecamp.org/news/these-are-the-most-effective-microservice-testing-strategies-according-to-the-experts-6fb584f2edde
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OufjerPy6FKelc0l
tags:
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Jake Lumetta

  Testing microservices is hard. More specifically, end-to-end testing is hard, and
  that’s something we’ll discuss in greater detail in this article.

  But first, a quick story.

  I learned just how hard microservice testing could be when I...'
---

By Jake Lumetta

Testing microservices is hard. More specifically, end-to-end testing is hard, and that’s something we’ll discuss in greater detail in this article.

But first, a quick story.

I learned just how hard microservice testing could be when I first dove into a tech stack with seven separate microservices. Each had its own code base, dependency management, feature branches, and database schema — which also happened to have a unique set of migrations.

Talk about hectic.

The approach we took was to run everything locally. So that meant, at any given point in time when I want to run end-to-end tests, I would need to go through the following five steps for each of the seven microservices:

1. Ensure I was on the correct code branch (either master or feature_xyz)
2. Pull down the latest code for that branch
3. Ensure all dependencies were up to date
4. Run any new database migrations
5. Start the service

This was just a baseline requirement to enable tests to be run. Often times, I would forget to perform one of these steps for a service and spend 10–15 minutes debugging the issue. Once I finally had all the services happy and running, I could then begin to kick off the test suite. This experience sure made me miss the days of testing one big monolith.

So yes, I discovered that end-to-end microservice testing is hard — and gets exponentially harder with each new service you introduce. But fear not, because there are ways to make testing microservices easier. I’ve spoken to several CTOs about how they came up with their own creative ways of tackling this complex issue.

### Common microservice testing methods

#### Unit Testing

A microservice may be smaller by definition, but with unit testing, you can go even more granular. A unit test focuses on the smallest part of a testable software to ascertain whether that component works as it should. Renowned software engineer, author, and international speaker Martin Fowler [breaks unit testing down](https://martinfowler.com/articles/microservice-testing/#testing-unit-introduction) into two categories:

1. **Sociable unit testing:** This unit testing method tests the behavior of modules by observing changes in their state.
2. **Solitary unit testing:** This method focuses on the interactions and collaborations between an object and its dependencies, which are replaced by test doubles.

While these unit testing strategies are distinct, Fowler puts forth that they aren’t competing — they can be used in tandem to solve different testing problems.

During a discussion with David Strauss, CTO of Pantheon, David told me that “the opportunity is that Microservices are very straightforward to actually do unit testing on.”

#### Integration testing

With integration tests, you’re doing what it sounds like you’re doing: testing the communication paths and interactions between components to detect issues. [According to Fowler](https://martinfowler.com/articles/microservice-testing/#testing-integration-introduction), an integration test “exercises communication paths through the subsystem to check for any incorrect assumptions each module has about how to interact with its peers.”

An integration test usually tests the interactions between the microservice and external services, like another microservice or datastore.

Pawel ​Ledwoń, Platform Lead at Pusher, informed me that his team “lean[s] towards integration testing. Unit tests are still useful for some abstractions, but for user-facing features they are difficult to mock or skip important parts of the system.”

Not everybody I spoke to was a fan of the process. Mosquera’s take on the subject of integration testing, for example, is well worth noting:

> Integration testing is very error prone and costly, in terms of man-hours. The ROI just isn’t there. Each individual integration test brings small marginal coverage of use cases.

#### End-to-end testing

Last but not least is end-to-end testing, which — as previously mentioned — can be a difficult task. That’s because it involves testing every moving part of the microservice, ensuring that it can achieve the goals you built it for.

[Fowler wrote](https://martinfowler.com/articles/microservice-testing/#testing-end-to-end-tips) the following:

> end-to-end tests may also have to account for asynchrony in the system, whether in the GUI or due to asynchronous backend processes between the services.

He goes on to explain how these factors can result in “flakiness, excessive test runtime and additional cost of maintenance of the test suite.”

The best advice I can give when it comes to end-to-end testing is to limit the amount of times you attempt it per service. A healthy balance between the other microservice testing strategies mentioned — like unit testing and integration testing — will help you weed out smaller issues.

An end-to-end test is larger by definition, takes more time, and can be far easier to get wrong. To keep your costs low and avoid time-sink, stick to end-to-end testing when all other means of testing have been exhausted, and as a final stamp of quality assurance.

### The challenges of testing microservices

Microservices (compared to a monolith) require extra steps, like managing multiple repositories and branches, each with their own database schemas. But the challenges can run deeper than that.

Here are a few key challenges associated with testing microservices:

* **Availability:** Since different teams may be managing their own microservices, securing the availability of a microservice (or, worse yet, trying to find a time when all microservices are available at once), is tough.
* **Fragmented and holistic testing:** Microservices are built to work alone, and together with other loosely coupled services. That means developers need to test every component in isolation, as well as testing everything together.
* **Knowledge gaps:** Particularly with integration testing (which we will address later in this article), whoever conducts the tests will need to have a strong understanding of each service in order to write test cases effectively.

According to Oleksiy Kovyrin, Head of Swiftype SRE at Elastic,

> One important issue we have to keep in mind while working with microservices is API stability and API versioning. To avoid breaking applications depending on a service, we need to make sure we have a solid set of integration tests for microservice APIs and, in case of a breaking change, we have to provide a backwards-compatible way for clients to migrate to a new version at their own pace to avoid large cross-service API change rollouts.

Stefan Zier, Chief Architect at Sumo Logic, also reiterated to me that microservice testing is indeed “very, very difficult.”

“Especially once you go towards more continuous deployment. We’ve invested and continue to invest fairly heavily into integration testing, unit testing, and would do a lot more if we had the people to do it,” Zier told me.

With that being said, he admitted that, at certain stages, when Sumo Logic wants to test their services holistically, “more or less [the] entire company [becomes] a quality assurance team in a sense.”

### Solution: Five microservice testing strategies for startups

Yes, testing microservices can be difficult, but [given all the benefits of microservices](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith), foregoing them because of testing challenges isn’t the right path. To tackle these challenges, I got insight from several CTOs and distilled five strategies they used to successfully approach testing microservices.

#### 1. The documentation-first strategy

Chris McFadden, VP of Engineering Sparkpost, summarized the documentation-first strategy quite nicely during our discussion:

> We follow a documentation first approach so all of our documentation is in markdown in GitHub. Our API documents are open source, so it’s all public. Then, what we’ll do is before anybody writes any API changes or either a new API or changes to an API, they will update the documentation first, have that change reviewed to make sure that it conforms with our API conventions and standards which are all documented, and make sure that there’s no breaking change introduced here. Make sure it conforms with our naming conventions and so forth as well.

If you’re willing to go one step further, you could dabble in API contract testing, which — as previously mentioned — involves writing and running tests that ensure the explicit and implicit contract of a microservice works as it should.

#### 2. The full stack in-a-box strategy

The full stack in-a-box strategy entails replicating a cloud environment locally and testing everything all in one vagrant instance (“$ vagrant up”). The problem? It’s extremely tricky, as software engineer Cindy Sridharan of Imgix explained in a [blog post](https://medium.com/@copyconstruct/testing-microservices-the-sane-way-9bb31d158c16):

> I’ve had first hand experience with this fallacy at a previous company I worked at where we tried to spin up our entire stack in a [local] vagrant box. The idea, as you might imagine, was that a simple vagrant up should enable any engineer in the company (even frontend and mobile developers) to be able to spin up the stack in its entirety on their laptops.

Sridharan goes on to detail how the company only had two microservices, a gevent based API server and some asynchronous Python background workers. A relatively simple setup, by all means.

“I remember spending my entire first week at this company trying to successfully spin up the VM locally only to run into a plethora of errors. Finally, at around 4:00pm on the Friday of my first week, I’d successfully managed to get the Vagrant setup working and had all the tests passing locally. I remember feeling incredibly exhausted,” she narrated.

In addition, Stefan Zier, Chief Architect at Sumo Logic, explained to me that — on top of being difficult to pull off — this localized testing strategy simply doesn’t scale:

“[With] a local deployment, we run most of the services there so you get a fully running system and that’s now stretching even the 16GB RAM machines quite hard. So that doesn’t really scale,” he said.

#### 3. The AWS testing strategy

This third strategy involves spinning up an Amazon Web Services (AWS) infrastructure for each engineer to deploy and run tests on. This is a more scalable approach to the full stack in-a-box strategy discussed above.

Zier called this a “personal deployment [strategy], where everyone here has their own AWS account.”

“You can push the code that’s on your laptop up into AWS in about ten minutes and just run it in like a real system,” he said.

#### 4. The shared testing instances strategy

I like to think of this fourth strategy as a hybrid between full stack in-a-box and AWS testing. That’s because it involves developers working from their own, local station, while leveraging a separate, shared instance of a microservice to point their local environment at during testing.

Steven Czerwinski, Head of Engineering, Scaylr, explained how this can work in practice:

> Some of [our] developers run a separate instance of a microservice just to be used for testing local builds. So imagine you’re a developer, you’re developing on your local workstation, and you don’t have easy way of launching the image parser. However, your local builder would just point to a test image parser that’s running in the Google infrastructure.

#### 5. The stubbed services strategy

And finally, we have the stubbed services testing strategy.

Zier laid out SumoLogic’s approach to stubbed service testing by telling me how, “stubbing let’s you write these marks or ‘stubs’ of microservices that behave as if they were the right service and they advertise themselves in our service discovery as if they were real service, but they’re just a dummy imitation,” he explained.

For example, testing a service may necessitate that the service becomes aware that a user carries out a set of tasks. With stubbed services, you can pretend that user (and his tasks) have taken place without the usual complexities that come with that. This approach is a lot more lightweight compared to running services in their totality.

### Tools to help you test microservices

Here’s a list of tools that have benefited me during my own microservice testing experiences, bolstered by some recommendations from the [pool of CTOs and senior developers](https://buttercms.com/books/microservices-for-startups/#contributors):

* [Hoverfly](https://hoverfly.io/): simulate API latency and failures.
* [Vagrant](https://www.vagrantup.com/): build and maintain portable virtual software development environments
* [VCR](https://github.com/vcr/vcr): a unit testing tool
* [Pact](https://docs.pact.io/): frameworks consumer-driven contracts testing.
* [Apiary](https://apiary.io/): API documentation tool
* [API Blueprint](https://apiblueprint.org/): design and prototype APIs
* [Swagger](https://swagger.io/): design and prototype APIs

### Microservices testing: difficult, but worth it

Testing your microservices won’t be a walk in the park, but the additional work is worth the benefits of having a microservice architecture.

Plus, the microservice testing strategies adopted by the likes of SumoLogic and Scaylr should help smooth the process out. Here’s a quick recap of those strategies:

1. The documentation-first strategy
2. The full stack in-a-box strategy
3. The AWS testing strategy
4. The shared testing instances strategy
5. The stubbed service strategy

Naturally, you may need to tweak each strategy to match your unique circumstances, but with some good old fashioned trial and error, your microservice testing strategy should come into its own.

_If you’ve enjoyed this article, please help it spread by clapping below! For more content like this, follow us on [Twitter](https://twitter.com/ButterCMS) and [subscribe](https://buttercms.com/blog/) to our blog._

_Jake Lumetta is the CEO of [ButterCMS](https://buttercms.com/), and is publishing [Microservices for Startups](https://buttercms.com/books/microservices-for-startups/)._

_And if you want to add a blog or CMS to your website without messing around with Wordpress, [you should try Butter CMS](https://buttercms.com/)._

