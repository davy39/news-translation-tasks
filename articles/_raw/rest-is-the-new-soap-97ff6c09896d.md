---
title: REST is the new SOAP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-15T20:32:11.000Z'
originalURL: https://freecodecamp.org/news/rest-is-the-new-soap-97ff6c09896d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VlkAg8dodbaaKp-Po7DrAA.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pakal de Bonchamp

  Written by Pascal Chambon, reviewed by Raphaël Gomès

  Update: this article mostly deals with the RESTish ecosystem, which now constitutes
  a major part of webservices. For more in-depth analysis of the original REST, and
  of HATEOAS...'
---

By Pakal de Bonchamp

_Written by Pascal Chambon, reviewed by Raphaël Gomès_

**_Update_**_: this article mostly deals with the RESTish ecosystem, which now constitutes a major part of webservices. For more in-depth analysis of the original REST, and of HATEOAS, see my [follow-up article](https://medium.com/@pakaldebonchamp/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438)._

### Introduction

Some years ago, I developed a new information system in a big telecom company. We had to communicate with an increasing number of web services, exposed by older systems or by business partners.

Needless to say, we had our fair share of [SOAP](https://en.wikipedia.org/wiki/SOAP) Hell. Abstruse [WSDLs](https://en.wikipedia.org/wiki/Web_Services_Description_Language), incompatible libraries, weird bugs… So whenever we could, we advocated — and used — simple Remote Procedure Call protocols: XMLRPC or JSONRPC.

Our first servers and clients for these protocols were pretty basic, limited, fragile. But gradually, we improved them; and with a few hundreds lines of additional code, we achieved the dream: support for different dialects (such as Apache-specific XMLRPC extensions), built-in conversion between python exceptions and hierarchical error codes, separate handling of functional and technical errors, auto-retries for the latter, relevant logging and stats before/after requests, thorough validation of input data…

Now we were able to robustly connect to any such API, with just a few lines of code.

Now we were able to expose any set of functions to a wide audience, to servers and to web browsers, with a few decorators and doc updates.

And when it came to communicating between our different applications (microservice-style), it was a job for our system administrator; software-side, it was almost transparent.

![Image](https://cdn-media-1.freecodecamp.org/images/U8IwqOXGlnAp-z3A25ZgRz3Gm2PUjlduG1-c)
_Developer resting after a tough 30mn spent integrating an RPC API._

**Then came REST.**   
**REpresentational State Transfer.**

A wave of renewal shook the foundations of inter-services communication.

RPC was dead, the future was RESTful: resources living each on its own URL, and manipulated exclusively through HTTP protocol.

From then on, every API we had to expose or consume became a new challenge; not to say a testimony to insanity.

### What’s the problem with REST?

A short example is worth a long talk. Here is a small API, with data types removed for readability.

```
createAccount(username, contact_email, password) -> account_id
addSubscription(account_id, subscription_type) -> subscription_id
sendActivationReminderEmail(account_id) -> null
cancelSubscription(subscription_id, reason, immediate=True) -> null
getAccountDetails(account_id) -> {full data tree}
```

Just add a properly documented hierarchy of exceptions (InvalidParameterError, MissingParameterError, WorkflowError…), with subclasses to identify important cases (eg. AlreadyExistingUsernameError), and you’re good to go.

This API is easy to understand, easy to use, and robust. It is backed by a precise state machine, but the restricted set of available operations keeps users away from nonsensical interactions (like changing the creation date of an Account).

**Estimated time to expose this API as a simple RPC service: a few hours.**

Ok, now time to go the RESTful way.

No more standards, no more precise specifications. Just a vague “RESTful philosophy”, prone to endless metaphysical debates, and as many ugly workarounds.

How do you map the precise functions above, to a handful of CRUD operations? Is sending the activation reminder email an update on a “must_send_activation_reminder_email” attribute? Or the creation of a “activation_reminder_email resource”? Is it sensible to use DELETE for cancelSubscription() if the subscription remains alive during a grace period, and may be resurrected during that time? How do you split the data tree of getAccountDetails() between endpoints, to respect the data model of REST?

What URL endpoint do you assign to each of your “resources”? Yeah it’s easy, but it has to be done anyway.

How do you express the diversity of error conditions, using the very limited bunch of HTTP codes?

What serialization formats, which specific dialects do you use for input and output payloads?

How exactly do you scatter these simple signatures between HTTP method, URL, query string, payload, headers, and status code?

And you’re gone for hours, reinventing the wheel. Not even a tailored, smart wheel. A broken and fragile wheel, requiring tons of documentation to be understood, and violating specifications without even knowing it.

![Image](https://cdn-media-1.freecodecamp.org/images/0bAxdhnQJw0WseQEmDT9Km9hn2Nj2VfsWJzb)

**How come REST means so much WORK?**   
_This is both a paradox, and a shameless pun._

Let’s dive further into the artificial problems born from this design philosophy.

_BEWARE : through this document, you’ll encounter lots of semi-rhetorical technical questions. Do not misunderstand them, they DO NOT mean that RESTish webservices can’t solve these problems. They just mean that users have an extra burden of decisions to take, of extensions to integrate, of custom workarounds to apply, and this is a problem in itself._

### The joy of REST verbs

Rest is not CRUD, its advocates will ensure that you don’t mix up these two. Yet minutes later they will rejoice that HTTP methods have well defined semantics to create (POST), retrieve (GET), update (PUT/PATCH) and delete (DELETE) resources.

They’ll delight in professing that these few “verbs”are enough to express any operation. Well, of course they are; the same way that a handful of verbs would be enough to express any concept in English: “Today I updated my CarDriverSeat with my body, and created an EngineIgnition, but the FuelTank deleted itself”; being possible doesn’t make it any less awkward. Unless you’re an admirator of the [Toki Pona](https://en.wikipedia.org/wiki/Toki_Pona) language.

If the point is to be minimalist, at least let it be done right. Do you know why PUT, PATCH, and DELETE have never been implemented in web browser forms? Because they are useless and harmful. We can just use GET for read and POST for write. Or POST exclusively, when HTTP-level caching is unwanted. Other methods will at best get in your way, at worst ruin your day.

You want to use PUT to update your resource? OK, but some Holy Specifications state that the data input has to be equivalent to the representation received via a GET. So what do you do with the numerous read-only parameters returned by GET (creation time, last update time, server-generated token…)? You omit them and violate the PUT principles? You include them anyway, and expect an “HTTP 409 Conflict” if they don’t match server-side values (forcing you to then issue a GET...)? You give them random values and expect servers to ignore them (the joy of silent errors)? Pick your poison, REST clearly has no clue what a read-only attribute it, and this won’t be fixed anytime soon. Meanwhile, a GET is dangerously supposed to return the password (or credit card number) which was sent in a previous POST/PUT; good luck dealing with such write-only parameters too.

Did I forget to mention that PUT also brings dangerous race conditions, where several clients will override each other’s changes, whereas they just wanted to update different fields?

You want to use PATCH to update your resource? Nice, but like 99% of people using this verb, you’ll just send a subset of resource fields in your request payload, hoping that the server properly understands the operation intended (and all its possible side effects); lots of resource parameters are deeply linked or mutually exclusive(ex. it’s either credit card OR paypal token, in a user’s billing info), but RESTful design hides this important information too. Anyway, you’d violate specs once more: PATCH is not supposed to just send a bunch of fields to be overridden. Instead, you’re supposed to provide a “set of instructions” to be applied on the resources. So here you go again, take your paperboard and your coffee mug, you’ll have to decide how to express these instructions. Often with handcrafted specifications, since Not-Invented-Here Syndrome is a de-facto standard in the REST world. (Edit: REST advocates have backpedaled on this subject, with [Json Merge Patch](https://tools.ietf.org/html/rfc7386), an alternative to formats like [Json Patch](https://tools.ietf.org/html/rfc6902))

You want to DELETE resources? OK, but I hope you don’t need to provide substantial context data; like a PDF scan of the termination request from the user. DELETE prohibits having a payload. A constraint that REST architects often dismiss, since most webservers don’t enforce this rule on the requests they receive. How compatible, anyway, would be a DELETE request with 2 MBs of base64 query string attached? (Edit: the [RFC 2616](https://tools.ietf.org/html/rfc2616#section-4.3), indicating that payloads without semantics should be ignored, is now obsolete)

![Image](https://cdn-media-1.freecodecamp.org/images/Kh0pTcWKoXqHlue3kdqTPNk9HhwjzDoe4kFQ)

REST aficionados easily profess that “people are doing it wrong” and their APIs are “actually not RESTful”. For example, lots of developers use PUT to create a resource directly on its final URL (_/myresourcebase/myresourceid_), whereas the “good way” (edit: according to many) of doing it is to POST on a parent URL (_/myresourcebase_), and let the server indicate, with an HTTP “Location” header, the new resource’s URL (edit: it’s not an HTTP redirection though). The good news is: it doesn’t matter. These rigorous principles are like Big Endian vs Little Endian, they occupy philosophers for hours, but have very little impact on real life problems, i.e “getting stuff done”.

By the way… handcrafting URLs is always great fun. Do you know how many implementations properly urlencode() identifiers while building REST urls? Not that many. Get ready for nasty breakages and SSRF/CSRF attacks.

![Image](https://cdn-media-1.freecodecamp.org/images/3cj3Mv2d3PmHunKtUoRheSjqK4ALGsJXAEud)
_When you forget to urlencode usernames in 1 of your 30 handcrafted URLs._

### The joy of REST error handling

About every coder is able to make a “nominal case” work. Error handling is one of these features which will decide if your code is robust software, or a huge pile of matchsticks.

HTTP provides a list of error codes out-of-the-box. Great, let’s see that.

Using “HTTP 404 Not Found” to notify about an unexisting resource sounds RESTful as heck, doesn’t it? Too bad: your nginx was misconfigured for 1 hour, so your API consumers got only 404 errors and purged hundreds of accounts, thinking they were deleted….

![Image](https://cdn-media-1.freecodecamp.org/images/E7ViySx5TgWjpOm4ajHxsAhkfRY58Sz1IQW5)
_Our customers, after we deleted their gigabytes of kitten images by error._

Using “HTTP 401 Unauthorized” when a user doesn’t have access credentials to a third-party service sounds acceptable, doesn’t it? However, if an ajax call in your Safari browser gets this error code, it _might_ startle your end customer with a very unexpected password prompt [it did, years ago, YMMV].

HTTP existed long before “RESTful webservices”, and the web ecosystem is filled with assumptions about the meaning of its error codes. Using them to transport application errors is like using milk bottles to dispose of toxic waste: inevitably, one day, there will be trouble.

Some standard HTTP error codes are specific to Webdav, others to Microsoft, and the few remaining have definitions so fuzzy that they are of no help. In the end, like most REST users, you’ll probably use random HTTP codes, like “HTTP 418 I’m a teapot” or unassigned numbers, to express your application-specific exceptions. Or you’ll shamelessly return “HTTP 400 Bad Request” for all functional errors, and then invent your own clunky error format, with booleans, integer codes, slugs, and translated messages stuffed into an arbitrary payload. Or you’ll give up altogether on proper error handling; you’ll just return a plain message, in natural language, and hope that the caller will be a human able to analyze the problem, and take action. Good luck interacting with such APIs from an autonomous program.

### The joy of REST concepts

REST has made a career out of boasting about concepts that any service architect in his right mind already respects, or about principles that it doesn’t even follow. Here are some excerpts, grabbed from top-ranked webpages.

_REST is a client-server architecture. The client and the server both have a different set of concerns._ What a scoop in the software world.

_REST provides a uniform interface between components._ Well, like any other protocol does, when it’s enforced as the _lingua franca_ of a whole ecosystem of services.

_REST is a layered system. Individual components cannot see beyond the immediate layer with which they are interacting._ It sounds like a natural consequence of any well designed, loosely coupled architecture; amazing.

Rest is awesome, because it is STATELESS. Yes there is probably a huge database behind the webservice, but it doesn’t remember the state of the client. Or, well, yes, actually it remember its authentication session, its access permissions… but it’s stateless, nonetheless. Or more precisely, just as stateless as any HTTP-based protocol, like simple RPC mentioned previously.

![Image](https://cdn-media-1.freecodecamp.org/images/kRhdDUN-QCazUckRJuN8D4cKsB7zNS0mcWbp)

With REST, you can leverage the power of HTTP CACHING! Well here is at last one concluding point: a GET request and its cache-control headers are indeed friendly with web caches. That being said, aren’t local caches (Memcached etc.) enough for 99% of web services? Out-of-control caches are dangerous beasts; how many people want to expose their APIs in clear text, so that a Varnish or a Proxy on the road may keep delivering outdated content, long after a resource has been updated or deleted? Maybe even delivering it “forever”, if a configuration mistake once occurred? A system must be secure by default. I perfectly admit that some heavily loaded systems want to benefit from HTTP caching, but it costs much less to expose a few GET endpoints for heavy read-only interactions, than to switch all operations to REST and its dubious error handling.

_Thanks to all this, REST has HIGH PERFORMANCE_! Are we sure of that? Any API designer knows it: locally, we want fine-grained APIs, to be able to do whatever we want; and remotely, we want coarse-grained APIs, to limit the impact of network round-trips. Here is again a domain in which REST fails miserably. The split of data between “resources”, each instance on its own endpoint, naturally leads to the N+1 Query problem. To get a user’s full data (account, subscriptions, billing information…), you have to issue as many HTTP requests; and you can’t parallelize them, since you don’t know in advance the unique IDs of related resources. This, plus the inability to fetch only part of resource objects, naturally creates nasty bottlenecks (edit: yes, you can stuff extensions like Compound/Partial Documents into your setup to help with that)..

_REST offers better compatibility._ How so? Why do so many REST webservices have “/v2/” or “/v3/” in their base URLs then? Backwards and forward compatible APIs are not hard to achieve, with high level languages, as long as simple rules are followed when adding/deprecating parameters. As far as I know, REST doesn’t bring anything new on the subject.

_REST is SIMPLE, everyone knows HTTP!_ Well, everyone knows pebbles too, yet people are happy to have better blocks when building their house. The same way XML is a meta-language, HTTP is a meta-protocol. To have a real application protocol (like “dialects” are to XML), you’ll need to specify lots of things; and you’ll end up with Yet Another RPC Protocol, as if there were not enough already.

_REST is so easy, it can be queried from any shell, with CURL!_ OK, actually, every HTTP-based protocol can be queried with CURL. Even SOAP. Issuing a GET is particularly straightforward, for sure, but good luck writing json or xml POST payloads by hand; people usually use fixture files, or, much more handy, full-fledged API clients instantiated directly in the command line interface of their favorite language.

_“The client does not need any prior knowledge of the service in order to use it”_. This is by far my favourite quote. I’ve found it numerous times, under different forms, especially when the buzzword [HATEOAS](https://fr.wikipedia.org/wiki/HATEOAS) lurked around; sometimes with some careful (but insufficient) “except” phrases following. Still, I don’t know in which fantasy world these people live, but in this one, a client program is not a colony of ants; it doesn’t browse remote APIs randomly, and then decide how to best handle them, based on pattern recognition or black magic. Quite the opposite; the client has strong expectations on what it means, to PUT this one field to this one URL with this one value, and the server had better respect the semantic which was agreed upon during integration, else all hell might break loose.

![Image](https://cdn-media-1.freecodecamp.org/images/34MrY7lPN5IORJltxiixXPAQaJPXy6efQRNa)
_When you ask how HATEOAS is supposed to work._

### How to do REST right and quick?

Forget about the “right” part. REST is like a religion, no mere mortal will ever grasp the extent of its genius, nor “do it right”.

So the real question is: if you’re forced to expose or consume webservices in a kinda-RESTful way, how to rush through this job, and switch to more constructive tasks _asap_?

**_Update_**_: it turns out that there are actually lots of “standards” and industrialization efforts for REST, although I had never encountered them personnally (maybe because few people use them?). More information in my [follow-up article](https://medium.com/@pakaldebonchamp/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438)._

#### How to industrialize server-side exposure?

Each web framework has its own way of defining URL endpoint. So expect some big dependencies, or a good layer of handwritten boilerplate, to plug your existing API onto your favorite server as a set of REST endpoint.

Libraries like Django-Rest-Framework automate the creation of REST APIs, by acting as data-centric wrappers above SQL/noSQL schemas. If you just want to make “CRUD over HTTP”, you could be fine with them. But if you want to expose common “do-this-for-me” APIs, with workflows, constraints, complex data impacts and such, you’ll have a hard time bending any REST framework to fit your needs.

Be prepared to connect, one by one, each HTTP method of each endpoint, to the corresponding method call; with a fair share of handmade exception handling, to translate passing-through exceptions into corresponding error codes and payloads.

#### How to industrialize client-side integration?

From experience, my guess is: you don’t.

For each API integration, you’ll have to browse lengthy docs, and follow detailed recipes on how each of the N possible operations has to be performed.

You’ll have to craft URLs by hand, write serializers and deserializers, and learn how to workaround the ambiguities of the API. Expect quite some trial-and-error before you tame the beast.

Do you know how webservices providers make up for this, and ease adoption?

Simple, they write their own official client implementations.

FOR. EVERY. MAJOR. LANGUAGE. AND. PLATFORM.

I’ve recently dealt with a subscription management system. They provide clients for PHP, Ruby, Python, .NET, iOS, Android, Java… plus some external contributions for Go and NodeJS.

Each client lives in its own Github repository. Each with its own big list of commits, bug tracking tickets, and pull requests. Each with its own usage examples. Each with its own awkward architecture, somewhere between ActiveRecord and RPC proxy.

This is astounding. How much time is spent developing such weird wrappers, instead of improving the real, the valuable, the getting-stuff-done, webservice?

![Image](https://cdn-media-1.freecodecamp.org/images/6e6uGUi7IVtFgglB6VlN3m6Kq5ohKtztGVet)
_Sisyphus developing Yet Another Client for his API._

### **Conclusion**

For decades, about every programming language has functioned with the same workflow: sending inputs to a callable, and getting results or errors as output. This worked well. Quite well.

With Rest, this has turned into an insane work of mapping apples to oranges, and praising HTTP specifications to better violate them minutes later.

In an era where [MICROSERVICES](https://en.wikipedia.org/wiki/Microservices) are more and more common, how come such an easy task — linking libraries over networks — remains so artificially crafty and cumbersome?

I don’t doubt that some smart people out there will provide cases where REST shines; they’ll showcase their homemade REST-based protocol, allowing to discover and do CRUD operation on arbitrary object trees, thanks to hyperlinks; they’ll explain how the REST design is so brilliant, that I’ve just not read enough articles and dissertations about its concepts.

I don’t care. Trees are recognized by their own fruits. What took me a few hours of coding and worked very robustly, with simple RPC, now takes weeks and can’t stop inventing new ways of failing or breaking expectations. Development has been replaced by tinkering.

Almost-transparent remote procedure call was what 99% people really needed, and existing protocols, as imperfect as they were, did the job just fine. This mass monomania for the lowest common denominator of the web, HTTP, has mainly resulted in a huge waste of time and grey matter.

**REST promised simplicity and delivered complexity.**  
**REST promised robustness and delivered fragility.**  
**REST promised interoperability and delivered heterogeneity.**  
**REST is the new SOAP.**

### Epilogue

The future could be bright. There are still tons of excellent protocols available, in binary or text format, with or without schema, some leveraging the new abilities of HTTP2… so let’s move on, people. We can’t forever remain in the Stone Age of Webservices.

_Edit_: many people asked for these alternative protocols, the subject would deserve its own story, but one could have a look at XMLRPC and JSONRPC (simple but quite relevant), or JSONWSP (includes schemas), or language-specific layers like Pyro or RMI when for internal use, or new kids in the block like GraphQL and gRPC for public APIs…

![Image](https://cdn-media-1.freecodecamp.org/images/L5hrdnm4vPQK-RaCYSy4z49vFhqYeUdsZom3)
_“Always finish a rant on a positive note”, momma said._

Edited on December 12, 2017:

* normalize section titles
* remove some typos
* rectify improper “HTTP redirection” wording after POST operations
* add suggestions of alternative protocols

Edited on December 28, 2017:

* fix mixup between “HTTP methods” and “REST verbs”

Edited on January 7, 2018

* fix ambiguous wordings

Edited on January 19, 2018

* fix wrong wording on “PUT vs GET” remarks
* precise the notion of “real APIs” (non-CRUD)
* mention risk of overrides with PUT
* update paragraphs on PATCH and DELETE troubles

Edited on January 19, 2018

* fix wording around Not-Invented-Here Syndrome

Edited on February 2, 2018

* add links to follow-up article on The Original REST, in “introduction” and “how to industrialize” chapters

Edited on April 14, 2019

* add clarification about “semi-rhetorical question”, and hints about extensions like compound/partial documents

Edited on July 6, 2019

* fix typos and French links

**Please leave your comments below. And here are past comments about this article on Medium: [https://medium.com/p/97ff6c09896d/responses/show](https://medium.com/p/97ff6c09896d/responses/show)**


