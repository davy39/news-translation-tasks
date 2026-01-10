---
title: 'Here’s my follow-up to REST is the new SOAP: let’s talk about the Original
  REST'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-02T18:59:55.000Z'
originalURL: https://freecodecamp.org/news/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a68QxzlHe3e3THOyKV9m8w.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: REST
  slug: rest
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pakal de Bonchamp

  I’ve read the philosophical dissertations, so you don’t have to!

  I expected my recent article (or “hipsteresque drunken rant,” as some called it),
  to get a barrage of criticism, under the motto “you haven’t understood anything
  ab...'
---

By Pakal de Bonchamp

**I’ve read the philosophical dissertations, so you don’t have to!**

I expected my [recent article](https://medium.freecodecamp.org/rest-is-the-new-soap-97ff6c09896d) (or “hipsteresque drunken rant,” as some called it), to get a barrage of criticism, under the motto “you haven’t understood anything about REST.” It indeed happened.

But it also sparked interesting debates, especially on [Reddit](https://www.reddit.com/r/javascript/comments/7k2kv2/rest_is_the_new_soap_pakal_de_bonchamp_medium/?st=jb8hbpsd&sh=1a3a371e) and on [Hacker News](https://news.ycombinator.com/item?id=15937448). It also struck a cord in numerous developers, who felt like heretics for doubting the almightiness of REST.

To quote a [particularly insightful summary](https://news.ycombinator.com/item?id=15938460) of the resentment:

> _A simple RPC API spec takes minutes to define. ‘Rest’ifying takes much longer, there are a million little gotchas, no real standard. Everyone has a different opinion of how it should be done._

> _Data is spread across verbs, urls, query params, headers, and payloads. Everyone thinks everyone else doesn’t ‘get’ REST. If you try to suggest something other than REST in the office you become the subject of a witch hunt. It really is a cargo cult of pointlessness._

> _My co-workers have spent sooo much time trying to get Swagger to generate documentation correctly as well as generate client side APIs, and there are countless gotchas we are still dealing with. It really is SOAP 2.0, when a simple JSON/RPC protocol would have done fine._

> _Don’t get me started with conflating HTTP server errors with applications errors. And trying to do action-like requests with a mindset optimized for CRUD. How much time have we wasted figuring out the ‘standard’ way to do just a login API call RESTfully._

On the opposite side, Phil Sturgeon, one of the main advocates of REST, released a [response article](https://philsturgeon.uk/api/2017/12/18/rest-confusion-explained/) (see my [quick comments here](http://disq.us/p/1oy9a9l)). I’m glad we agreed on some important points, especially that many APIs actually ought to be RPC, instead of ending as pseudo-REST patch-up jobs.

In the light of all this feedback, I’ve edited my initial essay quite a few times, and now a new article seems necessary to clarify the remaining points.

I would like to apologize in advance if the cheekiness of this post comes across as rudeness. Considering the harmfulness of the situation, I alas couldn’t content myself of a peaceful tone. No personal offense is meant in any way. So let’s get on with it.

### Several shades of REST

One difficulty of the subject is that there are several concepts behind the term “REST.”

1) The Founding Book of REST, i.e [the dissertation of Roy Fielding](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)   
2) The thousands of blogposts/podcasts of REST advocates (like Phil Sturgeon’s), disseminated on the Web, and explaining “how to do REST properly”  
3) The gazillions of (self-proclaimed) RESTful webservices, publicly or privately exposed all over the Internet

My rant was mostly dealing with **#3:** the RESTish APIs that are wasting everyone’s time, for yet-to-be-demonstrated benefits. And even after reading hundreds of comments, I have to stand my ground: these APIs that I’ve met everywhere are constantly reinventing the wheel, don’t even leverage the advantages that HTTP semantics could bring (client-side caching, content negotiation, optimistic locking…), and are a lengthy pain to integrate.

The response article by Phil Sturgeon highlighted the main reason for this epitome of pointlessness:

> “_Folks everywhere are building RESTish APIs which are basically just RPC + HTTP verbs + Pretty URLs._”

Along the way, we evoked **#2** through some quotes of REST advocates. For the rest, as far as I’ve seen, REST bloggers/podcasters have often contradicted each other. They’ve given instructions that sounded more like tastes than wisdom lessons, have evaded the most important questions, and have made a virtue of not backing, with examples and demonstrations, their most audacious arguments: _“RPC causes redundant work”_, _“REST is necessary for APIs lasting decades”_, and of course the (in)famous _“The client does not need any prior knowledge of the service in order to use it.”_

I’ve not yet crossed a simple page of prose summarizing how HATEOAS _really_ works, and what challenges it solves for us. This is a problem in itself.

About contradictions…here’s an anecdote. When I showcased a simple (and gently CRUD-oriented) API, it was just to show the abnormal number of questions that had to be answered just to RESTify it. And still, numbers of commenters felt compelled to explain, with verbose documentation, how THEY would specify this API.

It resulted in lots of similar but incompatible protocols, some weaving standards together, some reinventing carved flintstone, and some going as far as specifying a versioned MIME type per Resource endpoint (like _“application/vnd.my-rest-api.v1.account-search-result+json”_).

Phil Sturgeon also answered, in his response article, these semi-rhetorical questions. The recommendations delivered made sense and seemed “up to date.” But they directly contradicted the past or present teachings of lots of other REST proponents (as well as commenters cited above) on diverse subjects: sparse fields, compounds documents, PATCH formats, DELETE payloads, and so on.

At least all this proved a point: when things must be done quickly and consensually, REST is not the best way to go. Still, many claimed that I was attacking “misconceptions” of REST, and directed me to this or that quote from the original dissertation. This was a way of saying that the “theory” was good, even though the “practice” was flawed. “_Yeah, right, communism claims the same,_” one might argue.

![Image](https://cdn-media-1.freecodecamp.org/images/DIOnmqtsew2du2MQ-H9Rx67Y7kny0XF6oI4y)
_How *some* REST advocates view its Founding Thesis_

The debate of whether a practice is RESTful or not has become a running gag in the web development ecosystem. However, for the sake of intellectual honesty, it was actually interesting to come back to the most authoritative definition of REST™ as given by the dissertation **#1** and related articles. It’s at least to understand how this hype started, and what can be saved from it all.

I hope the summaries below will be deemed faithful enough to the originals. If not, I welcome your feedback on other “misconceptions” they might contain.

### What is the Original REST™ anyway?

Roy Fielding’s [dissertation](https://medium.com/@pakaldebonchamp/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438), published in 2000, is naturally long (180 pages), so it’s probably not widely read among web developers.

Here is a breakdown of its content. As an alternative, you can also read the Introduction and Conclusion chapters of said dissertation.

* Chapter 1 defines architecture-related terms like elements, components, properties, styles, patterns, and so on.
* Chapter 2 lists the key properties for a network-based architecture: user-perceived performance, network efficiency, scalability, modifiability, visibility, and reliability.
* Chapter 3 classifies existing architectural styles (Pipe and Filter, Cache, Client-Server, Code on Demand), and shows their pros and cons regarding the key properties above.
* Chapter 4 summarizes the requirements of the World Wide Web architecture (Low Entry Barrier, Extensibility, Distributed Hypermedia, Anarchic Scalability and so on), and explains why a dedicated architectural style is needed to guide its development, especially to evaluate proposed extensions before they are deployed.
* Chapter 5 presents the REST architectural style: the existing styles from which it derives, its architectural elements (Resources and their Identifiers, Representations, Connectors, Components, and so on), and how all this works together regarding processes and data.
* Chapter 6 gives an experience feedback of how REST was used to guide the development of Web protocol standards (URIs, HTTP and its numerous features and extensions), where it failed to be applied (cookies, mixing of different concerns in headers, user IDs in URIs, and so on), and the architectural lessons to be learned from the modern Web architecture.

![Image](https://cdn-media-1.freecodecamp.org/images/RICSoTTSIx3hE6WbMEFyh-UHXdYMFmPLLxGe)
_The book “An introduction to REST: Tome 1”_

What do we get from this dissertation, apart from the usual [REST constraints](http://whatisrest.com/rest_constraints/index)?

First, as expected from the **introduction of an “architectural style,”** it says almost nothing about HTTP methods, schemas, error handling, versioning, and all these concrete subjects which shape real-world webservices. That’s why hundreds of contradicting opinions have flowed to fill the hole, and that’s why it’s weird to sometimes hear that REST is “_precisely specified_” by this dissertation.

Second, REST was formalized to give a **theoretical backbone to the development of the World Wide Web.** It mixes lots of existing architectural styles, and inherits from their benefits and drawbacks, for the purpose of designing an **Internet-scale distributed hypermedia system**.

**And it works.**

* On the web, we are happy that all webpages speak HTTP, display themselves with a GET, and handle forms with GET or POST [Uniform Interface]
* On the web, we’re happy that our browser understands hundreds of content types (HTML, images, CSS, fonts, Javascript, RSS…), and handles them according to numerous built-in rules (caching, display, security…) [Self-Descriptive Messages]
* On the web, we’re happy to have in-browser caching, content delivery networks, and other forms of shared caches, helping to speed up loading time and absorb traffic peaks (like “Slashdot effects”). Even though a quick ctrl+F5 is sometimes needed to fix weird behaviors of webpages. [Layered System & Caching]
* On the web, we’re happy that proxies and firewalls understand web protocols, and let them flow, while blocking dubious TCP/UDP connections. [Visibility]
* On the web, we’re happy that scripts can be delivered by the server for each page, since browsers have, by themselves, no clue about how to add dynamics to provided HTML [Code-On-Demand]

One point [evoked but not detailed in the dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_5) is “**Hypermedia As The Engine Of Application State**” **(HATEOAS).** In complementary articles, Roy Fielding explained the concept of “_hypermedia controls,_” also called “_affordances:_” some kinds of glorified links, advertising to the client “what it can do next.” And he declared (a little late?) that these are not mere options, but that HATEOAS is at the very core of REST.

> When I say Hypertext, I mean … The simultaneous presentation of information and controls such that the information becomes the affordance through which the user obtains choices and selects actions. Hypertext does not need to be HTML on a browser: machines can follow links when they understand the data format and relationship types ([source](http://roy.gbiv.com/talks/200711_REST_ApacheCon.pdf)).

> _Information and actions, displayed up to a user through a self-documenting format of awesomeness, with a selection of links that turn a well-tuned client into a crawler instead of just being a CRUD exchange… well that’s the whole point of REST ([source](https://blog.apisyouwonthate.com/representing-state-in-rest-and-graphql-9194b291d127))._

> _Naturally, that is where I have to explain why “hypermedia as the engine of application state” is a REST constraint. Not an option. Not an ideal. Hypermedia is a constraint. As in, you either do it or you aren’t doing REST ([source](https://www.infoq.com/articles/roy-fielding-on-versioning/))._

> _A REST API should be entered with no prior knowledge beyond the initial URI (bookmark) and set of standardized media types that are appropriate for the intended audience (i.e., expected to be understood by any client that might use the API) ([source](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven))._

Regarding this aspect too, the Web seems RESTful. From the homepage of a website, users and webspiders are able to navigate it effortlessly, and handle related medias (images, stylesheets, scripts, and so on) that are discovered along the way. Although URLs change over time and forms are added and removed, websites don’t need version numbers, and it’s fine.

![Image](https://cdn-media-1.freecodecamp.org/images/8TXoDNwDHiJFQU4enox2C8z7PLnmBhzPlty8)
_When I realized that the main HATEOAS example was just the world wide web_

We thus see that the original REST™ is a powerful architectural style, providing big control to servers over their clients, and offering a crawlable ecosystem of editable hypermedia.

Now, what about your APIs? Do they aim at being “_Internet-scale distributed hypermedia systems,_” too?

### The hazardous and (often) unnecessary Holy Grail

You might have heard about the [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html). It evaluates the level of RESTfulness of your API, depending on whether it uses proper resources (Level 1), verbs (Level 2), and hypermedia controls (Level 3). This model might give you the feeling that some “RESTish” APIs of yours are meant to evolve on these “_steps toward the glory of REST_” (as Martin Fowler describes it). Bad news, this most probably won’t occur.

Yes, you can fake RESTfulness by mapping your server functions to Resource URLs. Yes, you can fake it further by mapping your operations to the closest HTTP verbs. But when it’s time to reach the final level, to really have a self-descriptive, crawlable, hypermedia-driven application, you’ll have to realize the harsh truth: your API is not RESTful, it has never been, and it never will be. It actually has less chances to attain “True RESTfulness” than a slug has to become a butterfly.

Remember the quotes from Roy Fielding in the previous section? His definition of REST is all about HATEOAS. But it’s an extremely ambitious statement.

It means you should forget meaningless MIME types like “text/xml” or “text/json,” and use specific content types, backed by contracts, and recognizable by API consumers. It means that unless a full-fledged RESTful protocol already exists for your precise use case, you’ll have to write RFC/IETF-style drafts to describe the semantics of your specific content types. You’ll have to design a crawler-enabled hypermedia system, and specify the meaning of its miscellaneous “affordances.” And you’ll probably have to provide client implementations to your customers, in their own programming languages, since they have other things to do than follow such herculean endeavors.

All this is huge specification and implementation work. For rather light benefits. And worrisome drawbacks.

Yes, this enables server-side developers to keep control of their URL structure without redirections (_today I’ll rename “users/” to “accounts/” — it’s smoother_), but at what cost? Unless you constantly generate new URLs to prevent it, I bet your API consumers will hardcode URLs anyway, to avoid this extra layer of complexity (recognition of affordances, URL traversal caching etc.)

Yes, this enables the server to control available actions, when the end consumer is a human. But what about User eXperience? The arbitrary showing and masking of affordances by the server is a scary concept. When a “delete” button is missing on a [SPA](https://en.wikipedia.org/wiki/Single-page_application), I want to know why. And if I ask my REST-crawler program to create “this” resource, I’d rather have him fail with a proper remote error message, than say “_sorry, couldn’t find the affordance for that._” Actions can be prevented by security rules, missing dependencies, concurrent tasks, and other issues. We have the right to know what’s going on, and “affordances,” in their current form, miss this crucial feature.

Also, what about machine-to-machine interactions? If API evolvability is key, how does the consumer program understand new fields and new affordances? Roy Fielding [answers](https://www.infoq.com/articles/roy-fielding-on-versioning/) “_That is where code-on-demand shines._” No way. No way you’re dynamically injecting your remote code into my Python program anytime soon.

After reading hundreds of pages on the REST/HATEOAS subject, I’ve rarely been so unimpressed. Reaching LEVEL 3 of RESTfulness was supposed to be an epiphany. I rather have the deep feeling that the remedy is worse than the disease.

Now, some people argue that Roy Fielding is pushing the concept too far, that “**lightweight REST**” (i.e “Richardson Maturity Level 2,” without Hypermedia Controls) is the real goal to head for.

But still, I bet you actually do not need any of this.

* You (most probably) do not want code-on-demand. You want your clients to read your specs, and call your API precisely as you (and they) intend it.
* You (most probably) do not want network-level visibility. On the contrary, you want as much TLS encryption as possible.
* You (most probably) do not want shared caches or client-side caching. On the contrary, remote caches are amongst your worst enemies. And if your API consumers are not browsers, they typically ignore caching headers anyway.
* You (most probably) can do without content negotiation, and other HTTP features more or less bundled with REST best practices (you know, for Representation versus Resource). Every up-to-date language can understand formats like Xml and Json.
* You (most probably) do not want to expose Resources for CRUD operations, and use these awkward men-in-the-middle to trigger actual operations in your applications.

All you (most probably) want is to expose a bunch of your server-side functionalities to remote browsers or servers. In a quick, elegant, robust, way.

**Your API (most probably) screams “RPC”. And in this case, not even a skyscraper-sized shoehorn will allow it to fit into the very ambitious, but rarely relevant, REST Architectural Style.**

For sure, you might need this or that property of HTTP. For example, you might want to use the GET method and different URIs for your Ajax-originated read-only operations to benefit from browser-side caching. Or you might want to expose your database as CRUD-over-HTTP to leverage generic implementations (like Active Record style clients for JsonAPI protocol).

But whatever your needs are, _life is short_. You do not need to start from an abstract “set of guidelines” like REST constraints. You had better seek a **turnkey protocol**, matching the needs you really have.

There are tons of such solutions (mostly non-RESTful), for lightweight RPC, CRUD, pub/sub, job queues, remote filesystems, data querying/filtering, high performance computing, and bi-directional messaging. Rarely, you’ll have to innovate — add new capabilities to a protocol, or use hybrid approaches. But beginning to “turn verbs into nouns” or following abstract principles as dogmas is the last thing you need to do.

Please note, by the way, that CRUD can also be done as a mere subset of RPC. Webservices are usually not coded in C language anymore, so if you see one more wanderer arguing that “_it’s awful to have to code so many boilerplate CRUD functions_”, please enlighten them with this high-technology API.

```
create(type, **params) -> id
retrieve(type, id, **params)
update(type, id, **params)
delete(type, id, **params)
```

Along your (most probably) RESTless way, you’ll meet dozens of adamant speeches, claiming that only REST can grant you scalability and longevity. There is little need to disprove what has never been proven. All I can judge, from personal experience, is that:

* A well configured database and a simple server-side cache are enough for 99% of webservices; an old wisdom says _premature optimization is the root of all evil_.
* Services evolve continuously. Whether it means a new parameter in a remote procedure or a new field in a resource representation, it doesn’t matter much. And the [API Evolution](https://blog.apisyouwonthate.com/api-versioning-has-no-right-way-f3c75457c0b7#API%20Evolution) concept is, as far as I’ve read, nothing but plain old wisdom from software development: don’t make breaking changes until absolutely needed, and use compatibility layers to help everyone move forward at a sane pace.
* Even if you design your API awkwardly, it will certainly be dead loooong before it has real compatibility issues. Maybe not because its purpose has become irrelevant, and maybe not because of crushing competitors, but likely because of changes-of-mind in your marketing department.
* With the time spent to properly integrate most REST-style APIs, one could implement several successive versions of corresponding lightweight RPC webservices. Let’s remain pragmatic.
* When a tech startup, with a life expectancy below 2 years, spends one third of its time writing REST(ish) boilerplate, its CTO might deserve to be slapped with a large trout. Good programming practices and cheap workarounds are all they need, until they reach the state where scalability becomes a matter worth thinking about and spending money on.

Most importantly, please give up this Holy Grail Quest called “HATEOAS,” unless you’re part of the few Knights in the world concerned by this Mission.

REST/HATEOS is for specific data-centric APIs: those which are naturally CRUD, those which are consumed via ActiveRecord or DataMapper patterns in your favorite languages, those which do not have tons of subtle constraints and side-effects between the fields of a model, and those meant to be explored by humans (currently the only entities in the universe able to understand what this newly appeared “_billing contact email_” field means).

Otherwise, you’ll end up with the awkwardness of RESTish APIs, but with an extra stack of complications.

![Image](https://cdn-media-1.freecodecamp.org/images/3hlZJG4kPDdGKmn7yyoOFW-Yq8V4AIVsueyM)
_When used inadequately, REST is like “Monty Python and the Holy Grail,” but with thousands of rabbits_

One relevant use case for HATEOS would be a generic “Database Admin Protocol,” allowing any server to drive a same generic Single Page Application through the structure of its (SQL or no-SQL) database: navigation between tables and record pages, autogenerated forms for each schema, dynamic create/edit/delete buttons, and so on.

In similar fashion, an API dedicated to browsing and editing documentation, or exploring/pulling/pushing a Version Control System, would lend itself well to a REST architectural style. But these are far, very far, from what most webservices are built for. And if [Github switched from REST to GraphQL](https://githubengineering.com/the-github-graphql-api/) for its API, it’s a hint that the benefits claimed by REST were just _not enough_.

### **Where did it go wrong?**

So here we are. REST/HATEOS is certainly a nicely evolved architectural style, but (imho) only relevant to a tiny fraction of use cases. And now it has spread like cancer over the ecosystem of webservices — mostly under its truncated form called “RESTish APIs” — bringing inadequacy and artificial complexity everywhere.  
   
Who is to blame for this awkward situation?

* The original dissertation, which didn’t position REST in comparison to other architectures, and remained too vague on its pros and cons?
* The REST advocates, who often lost themselves in very subjective (when not contradicting) recommendations, instead of advertising standards and explaining when (not) to use REST?
* The uncountable articles who displayed a false dilemma between SOAP and REST, thus propelling to the stars a winner by default?
* The Internet trolls who proclaimed, in about every StackOverflow thread regarding webservices design, “_Forget existing protocol XYZ, it’s an extra layer which makes stuffs unmaintainable, all you need is handmade HTTP_”?
* The buzzword lovers who imposed REST to their teams, without discussing the impacts of this architectural change, without ever asking themselves “_but why though?_”
* The silent mass of developers, who, like me, have known FOR YEARS that something was deeply wrong, but haven’t blown the whistle?

![Image](https://cdn-media-1.freecodecamp.org/images/N42-nijzWSHyLEQCHFSL7nNNQops1B0Qhj2Y)

Yup. I guess it’s a mix of all these.

The cruel irony of this story is that the [original dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/introduction.htm) itself warned about bandwagon jumping and improper architectural choices:

> “H_ow often we see software projects begin with adoption of the latest fad in architectural design, and only later discover whether or not the system requirements call for such an architecture. Design-by-buzzword is a common occurrence. […] The REST interface is designed to be efficient for large-grain hypermedia data transfer, optimizing for the common case of the Web, but resulting in an interface that is not optimal for other forms of architectural interaction._”

Some good news, however, is that REST has paved the way for other protocols, like GraphQL and HTTP2. And its use of advanced HTTP features is an inspiration for other architectures. We owe it at least that.

### What if you *really* have to RESTify?

For lots of reasons (like corporate hierarchy, or really needing CRUD with HTTP caching), you might have to go for REST. With or without HATEOAS.

In my previous article, I suggested that industrializing REST clients and servers was a problem without solution. **It turns out I was wrong**_._

Here is an non-exhaustive list of REST-related “standards”, grabbed from the inputs of various commenters. You can find a lot more on Phil Sturgeon’s new [standards.rest](http://standards.rest/) listing.

* To specify semantics of PATCH: JSON Patch, JSON Merge Patch
* To specify interface contracts: JSON Schema, API Blueprint, OpenAPI (formerly Swagger), RAML, GraphQL Types, XML Schema
* To serialize results and/or errors in responses: JSend format, RFC7807 (Problem Details for HTTP APIs), Sparse fieldsets (restricting the fields to return), Compound documents (including related resources)
* Protocols with hypermedia controls: JSON Hyper-Schema (IETF Draft), JSON Hypertext Application Language or “HAL” (IETF Draft), Json-API, OData, Mason, Hydra/JSON-LD, JSON SIREN

These are indeed quite a good number of possibilities. A combinatorial explosion of possibilities, since many of them only take care of a small portion of the protocol. These efforts at standardizing are welcome, although they are somehow late: the most RESTful ones (for hypermedia) are, nearly 18 years after Roy Fielding’s dissertation, still drafts.

![Image](https://cdn-media-1.freecodecamp.org/images/i6CBAPMfBiy4qOpl5ceeYOwH3Y8EwOuBz8bc)
_REST APIs have standards. Like phone chargers do._

**Do you know why I didn’t cite any of them in my previous rant?**

Because during all those years spent integrating the APIs of big companies (think Google, Microsoft, Oracle, Dropbox, Spotify, and others), as well as that of smaller enterprise, **NOT ONCE** have I met any of these “standards”, neither explicitly nor implicitly. Maybe it’s because I was unlucky. Maybe it’s because they are rarely used.

From my point of view, this lack of visible standardization has to do with the **original sin of the REST**: for some reason, it came with a very strong anti-standards mindset, with an obscurantist “_all you need is love and HTTP_” philosophy. So even the most talented developers felt the urge to specify their own half-baked protocol, in their corner, oblivious to thousands of others who had already done the same.

In your case, naturally, the least harm will be to use existing standards and libraries. Preferably **full-fledged protocols**, rather than LEGO-style assemblies of RFCs.

**I shall warn you, though. Here be dragons, too.**

Sometimes, the devil is in the details. An old wisdom in computer sciences states that errors shall not go silent. That’s why it’s good practice to keep the format of objects consistent: some of their fields might be nullified, but they are present at all time anyway (unless asked otherwise by the client). That’s the best way to prevent _false negatives_ (due to typos), and to avoid random breakages in strict clients if the _quantic_ property of these fields was (as often) not properly documented.

I thought that this idea naturally applied to REST representations, too. Too bad: standards like [JSON Merge Patch](https://tools.ietf.org/html/rfc7386) force you to delete remote fields instead of nullifying them. These tiny but apocalypse-triggering details are especially inappropriate in a philosophy which claims to “_help client and server evolve independently._”

Sometimes, the devil is elephant-sized. Ever heard about this OpenAPI (formerly Swagger), one of the most ambitious REST standards? The idea is to describe your API in a specification file, with endpoints and schemas, and use OpenAPI tools to industrialize the creation of both client and server. It sounds nice, doesn’t it?

Here is an [example json interface spec](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json), for the Kubernetes API. Yes, Json schemas are by nature extremely verbose.

Ok, now here is the [corresponding client implementation](https://github.com/kubernetes-incubator/client-python/tree/master/kubernetes/client) for Python.

As of today, it’s more than 90,000 lines of Python code and comments, automatically generated by OpenAPI. Not just thin wrappers, to benefit from auto-documentation tools and IDE autocompletion. 90,000 lines. More than their json interface spec. What. the. actual. heck.

![Image](https://cdn-media-1.freecodecamp.org/images/WO3MynM9YLRWzKSWHvSWxHhVRoaYJCwCkjzZ)
_When you ask OpenAPI for a catamaran_

Each language, each framework, has its own idea on how to handle OpenAPI. Some choose [hybrid (and elegantly cruft-free) approaches](http://radar.oreilly.com/2015/09/building-apis-with-swagger.html). Some generate a spec file from server code. Most generate tons of boilerplate from said spec file. Sometimes they go farther and generate tests, too.

More tooling and more code generators mean more bugs and harder learning curves… and all that for what? The Kubernetes SDK is exposed to Python as a [set of methods](https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md#documentation-for-api-endpoints). With hardcoded URLs. Again, some RPC-over-CRUD system, considered by many as state-of-the-art RESTfulness, while disregarding HATEOAS. I find all this utterly confusing, and I hope I’m not the only one.

So be especially wary about REST-related protocols and frameworks you might choose. Some are handy and efficient, but some make REST look more and more like the new SOAP.

### TL;DR

The original REST™ is like rocket engineering: exciting, but very specific, quite complex, and rather harmful unless you precisely know what you’re doing.

RESTish APIs are more affordable, but be sure that you‘ll benefit from them, since it’s rarely the case. To quote a simple rule of thumb from Phil Sturgeon:

> “_If an API is mostly actions, maybe it should be RPC. If an API is mostly CRUD and is manipulating related data, maybe it should be REST_”.

Lots of REST(ish) “standards” exist, so no need to ever specify one from scratch. But whatever your needs are, beware of buzzwords, use the right tool for the right job (REST and RPC are only two amongst hundreds), and most importantly, [KISS](https://en.wikipedia.org/wiki/KISS_principle). I bet you’d have more success using a generic JsonAPI client and validating it against a real preprod server, than spending days generating tons of boilerplate OpenAPI code — only to discover later that it doesn’t actually match the remote side because of bugs or other incompatibilities.

The same goes for other architectures, by the way: you’ll probably save time using simple JsonRPC or JsonWSP protocols, instead of generating boilerplate with gRPC, only to later realize that this shiny protocol hasn’t even specified how to report application-level errors.

### Epilogue

REST is a difficult subject to talk about. There are lots of plot holes in the founding dissertation, lots of conflicting definitions, lots of contradicting opinions on how to do this or that right, lots of unjustified hypes and disgraces, lots of (underused and partial) standards… and very few real life examples of HATEOAS APIs (most links I’ve crossed were dead, so much for the “_lasting decades_”).

But I hope that this analysis has clarified a bit the different “RESTs” people are talking about, and that it will spare you some of the obscene amount of time I had to spend just to somehow understand what the Original REST™ was meant to be.

At the very least, you now have a new weapon in your bag. The next time your boss wants you to expose some server operations as REST webservices, just ask:

**For this API, do we really need to follow a composite architectural style meant for Internet-scale distributed hypermedia systems?**

The expression on his face will be your answer.



**Please leave your comments below. And here are past comments about this article on Medium: [https://medium.com/p/21c59d243438/responses/show](https://medium.com/p/21c59d243438/responses/show)**

