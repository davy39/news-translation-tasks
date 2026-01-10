---
title: 'How looking back can help us move forward: a retrospective on software gems
  and fads'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-30T18:30:49.000Z'
originalURL: https://freecodecamp.org/news/software-fads-and-gems
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/hidden-gem.jpg
tags:
- name: asyncio
  slug: asyncio
- name: Bitcoin
  slug: bitcoin
- name: formats
  slug: formats
- name: NoSQL
  slug: nosql
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Pakal de Bonchamp

  Maybe one of the most important qualities of a developer is the ability to pick
  the right tool for the right job, without hopping onto bandwagons or reinventing
  the wheel. This might require a bit of technology analysis, but even...'
---

By Pakal de Bonchamp

Maybe one of the most important qualities of a developer is the ability to pick the right tool for the right job, without hopping onto bandwagons or [reinventing the wheel](https://en.wikipedia.org/wiki/Not_invented_here). This might require a bit of technology analysis, but even more, a touch of critical thinking.

Here is a review of a few exaggerated trends and underrated niceties, in different areas of the marvelous world of computer science: **databases, asynchronicity, cryptocurrency, and data formats**. I won't touch on the subject of REST webservices, which I already [ranted about at great length](https://www.freecodecamp.org/news/rest-is-the-new-soap-97ff6c09896d/). 

_As usual, your feedback is more than welcome if any factual errors slipped into this (not entirely unbiased) article._

## Databases: NoSQL & ZODB

Few moments, in the history of computer science, were as ironically lit as the arrival of No-SQL databases, around 2009. A tidal wave struck the shores of backend development and system administration: SQL databases were too rigid, too slow, too hard to replicate. 

So new projects massively ditched them in favor of key-value stores like Redis, document-oriented databases like MongoDB/CouchDB, or graph-oriented databases like Neo4j. And we must acknowledge one thing: these new databases shone in benchmarks; they shone about as much.... as would shine any SQL database dropping all its [ACID constraints](https://www.geeksforgeeks.org/acid-properties-in-dbms/) and query language flexibility.

But the horizon was grim for numerous programmers. They learned, the hard way, that data persistence was not a minor concern. And that they needed, for example, to explicitly activate "Write Concerns" in MongoDB, to ensure that data would not get lost before reaching disk oxide. 

They learned that "eventual consistency" was a pretty word for "temporary inconsistency", opening the door to nasty, silent, hard-to-reproduce bugs in production. And that transactions - and their implicit locking - were precious features, and that mimicking them by hand, with awkward flags stuffed into documents, was all but easy and robust. 

And they learned that data schemas, and referential integrity, were more than welcome to prevent databases from becoming heaps of incoherent objects. And that the lack of advanced indexing capabilities (on multiple keys, on deep document fields) in key-value stores could become quite embarrassing.

 Thus, people began reinventing SQL features on top of NoSQL databases, by mimicking data schemas, foreign keys, advanced aggregation, in language-specific "ORM" libraries (mongoengine, mongoid, mongomapper...). In this context, this "Object-Relational Mapper" acronym should have, by itself, been a hint that something had gone wild. 

There was something surreal in watching NoSQL databases, which were honed for specific use cases (highly replicated or heterogeneous data, [capped-size collections](https://docs.mongodb.com/manual/core/capped-collections/) or [TTLs](https://docs.mongodb.com/manual/tutorial/expire-data/), pub/sub systems...), be used just to store a bunch of same-shape objects in a single server instance. 

A standard SQL database would completely have done the job, and offered many more tooling options and plugins (different storage engines, Percona toolkit scripts, IDEs like HeidiSql or Mysql Workbench, DB schema migration processes integrated into web frameworks...). Even if it meant stuffing extra unstructured data into a serialized Text Field (or, nowadays, dedicated [PostgreSQL Json Fields](https://www.postgresql.org/docs/current/datatype-json.html)).

With time, NoSQL databases themselves improved a lot, among other things by borrowing features from the SQL world. But reinventing SQL is not an easy task. Relational databases deal with query language parsing, character sets and collations, data aggregation and conversion, transactions and isolation levels, views and query caches, triggers, embedded procedures, [GIS](http://wiki.gis.com/wiki/index.php/Geographic_information_system), fine-grained permissions, replication and clustering... complex and sensitive features, driven by hundreds of settings spread on multiple levels (per database, per table, per connection). 

So despite their great progress (multi-document transactions, better data aggregation, stored JavaScript functions, pluggable storage, role-based access control in MongoDB), NoSQL DBs still have trouble challenging major SQL databases, purely feature-wise. 

Luckily, most projects only need a tiny subset of these SQL database features: a few schema validations, a few proper indices, and business can get rolling; so for teams lacking SQL expertise, the relative simplicity of many NoSQL DBs could indeed be, to be honest, a relevant factor.

The wave seems to have faded by now, and projects seem more inclined to combine different databases according to actual needs. They thus separate user accounts, job queues and similar caches, logging and stats data... each into the most relevant storage.

All these cited NoSQL databases, and their countless alternatives, are shining in their intended use cases. But I'd like to mention a too-little-known, too-little-used gem of the Python ecosystem. Have you already wanted to persist your data in a really, reaaaalllly easy way? Then I forward you to the [ZODB](http://www.zodb.org/en/latest/). You open it like a dictionary, you push whatever data you want into it, you commit the transaction, and you're good to go. 

*Example of simple local ZODB instance:*

```python
from ZODB import FileStorage, DB
import transaction

storage = FileStorage.FileStorage('mydatabase.fs')
root = DB(storage).open().root()
print("ROOT:", root)
root['employees'] = ['Mary', 'Jo', 'Bob']
transaction.commit()
```

Graphs of data are handled gracefully (no recursion error), objects are lazily loaded on access, special "bucket tree" types are provided to browse huge amounts of data while keeping memory low, and several storage backends exist, including [relstorage](https://relstorage.readthedocs.io/en/latest/install.html) which leverages the power of SQL databases. Perfect, isn't it?

Alright, I'm lying, there are a few gotchas. There is no built-in indexing system (one must use Zcatalog or the likes instead). Using dedicated "persistent" types is highly advised, to automatically detect and persist mutations of objects. The overall tooling is quite limited compared to mainstream databases. And the concurrency model based on "optimistic locking" might force you, under heavy load, to retry an operation several times until it manages to get applied. 

The extreme amount of integration with the Python language has an additional drawback: if you introduce breaking changes into your data model, your database might not load anymore, so you must handle schema migrations carefully. 

But context is everything: ZODB is not meant for long term and interoperable data persistence, but for effortless storage of (possibly very heterogeneous) python objects. It can make long-running scripts able to resume after interruption, it can store player data of online game sessions... if you really want to store blog articles or personal accounts in ZODB, you had better limit yourself to native python types, and implement your own sanity checks.  But whatever happens, do not use a very limited [stdlib shelf](https://docs.python.org/3.7/library/shelve.html), if you can have a nifty ZODB under the hand to store your work-in-progress data.

## Asynchronicity: Asyncio, Trio and Green Threads

There has been an immemorial challenge between synchronous and asynchronous programming models, in all IO-bound programs. Kernels have provided asynchronous modes for disk operations, with more or less success (_overlapped_ non-blocking IO on Windows, limited _io_submit_() API on Linux...). 

Networking code has made the issue still more acute, with the need for huge numbers of long-term connections, each performing only minor CPU operations. 

Some languages, like Erland, confronted this by being asynchronous from the start, and letting different tasks communicate by message passing (a.k.a [Actor Model](https://en.wikipedia.org/wiki/Actor_model)).

In other languages, several design patterns emerged to tackle the problem:

* callbacks
* async/await syntax
* lightweight threads

Callbacks were previously the major solution in mainstream frameworks. For example in jQuery or Twisted, the developer would provide callables as arguments or as instance methods, and these would be called on IO completion/cancellation, in a pattern called [Inversion of Control](https://en.wikipedia.org/wiki/Inversion_of_control). It works, for sure, but it makes program flows quite hard to predict and debug, hence the term "callback soup" often used in this context.

For the last few years, the [async/await](https://docs.python.org/3/library/asyncio-task.html) syntax has become highly trendy, especially in the Python world. But there is a problem: like Inversion of Control, it's a whole new way of programming, almost a new language. The vast amount of packages currently available, made of modules, classes and methods, just does NOT work with async/await. 

Any IO, any expensive operation, hidden deep inside a subdependency, could ruin your day. So we're currently gazing at thousands of great modules being happily reimplemented, with a whole new world of bugs and missing features.

Is it all worth it? Python developers have massively jumped onto the train of the [asyncio](https://docs.python.org/3/library/asyncio.html) package, which has become part of the stdlib. But this technology has scary issues, like the difficulty of socket backpressure, the fragile handling of exceptions and ctrl-C, the unsafe cancellation of (leaking) tasks, and the steep learning curve of an API full of gotchas and redundant concepts. Other frameworks like Trio/Curio, seemed [much more careful on these subjects](https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/). 

If we have to recode tons of existing libraries, why base new versions on an engine that some developers have - not without arguments - called a [dumpster fire of bad design](https://veriny.tf/asyncio-a-dumpster-fire-of-bad-design/)? But the [network effect](https://en.wikipedia.org/wiki/Network_effect) is huge in such cases, and alternative async/await-based frameworks will have a hard time challenging the standard.

And what about the third pattern quoted above, lightweight threads? Long before this async/await trend, Python developers thought: we already have some perfectly fine synchronous business code, so let's change the way it is run, not the way it is written. Thus appeared lightweight threads, or "greenlets". They work like a bunch of tiny tasks scheduled on top of a few native threads, tasks which yield control to each other only when they block on IO or explicitly do so; and with much greater performance than native threads, in terms of memory usage and switching delay. 

In the end, this system can quickly boost about any existing codebase so that it supports thousands of long-term concurrent tasks. And this is not an isolated mad experiment: Python lightweight threads have originally been used in Eve Online game (via Stackless Python), and have since successfully been ported to CPython (Gevent, Eventlet...) and PyPy. And they have actually [existed for a long time](https://en.wikipedia.org/wiki/Green_threads) in lots of programming languages, under different names (green processes, green threads, fibers...).

The drawbacks of this system?

* Libraries must play nice with green threads, by yielding control instead of blocking on IOs, and launching green threads instead of native threads. In python, main libraries (socket, time.sleep(), threading) are forcibly made green-friendly via monkey-patching; but compiled extensions must be especially checked, since they can bypass these patches and block on their own system calls.
* No heavy computation, or otherwise time-consuming tasks, must be performed, else all other tasks get impacted by the delay. For such needs, just delegate work to a pool of [native threads](http://www.gevent.org/api/gevent.threadpool.html) (or a [celery](http://www.celeryproject.org/)-like worker queue).

As we see, these drawbacks are similar to those of async/await, except that you almost don't have to touch the original, synchronous code. An "except" which can mean months or years of work avoided ; your CTO and CEO should be highly pleased about this.

Now, you'll sometimes hear strange rationalizations from people who ditched lightweight threads in favor of a whole async/await reimplementation. Something in the lines of "_Explicit is better than implicit, and all these awaits show me exactly where my code could switch context, whereas green threads might switch discreetly if a third-party function performs any kind of IO or explicit switch_".

But the thing is...

FIRST, why do you need to know at which points exactly the program will switch to another task? For all the past years, with native (preemptive) thread, a switch could happen anywhere, anytime, even right in a middle of a simple increment. 

But we learned to deal with this invisible threat properly, by protecting critical sections with locks and other synchronization primitives (Recursive Locks, Event, Condition, Semaphore...), keeping a proper order when nesting locks, and using thread-safe data structures (Queues and the likes) which handle concurrency for us. 

Green threads are a middle ground between (implicit) preemptive threads and (explicit) async/await, but all of these technologies had better stick to the good old way of protecting concurrent operations. 

Locks can be dangerous when misused (especially since most implementations stall, instead of detecting deadlock and reporting them as exceptions), but they are cheap and robust. What is the point of attempting to do lock-less concurrency, by checking the position of each potentially switch-triggering calls, when you could anytime have to add a new operation (even a simple logging output) in the middle of your carefully crafted lock-less sequence, and thus ruin its safety?

*This naive code shows how a recently added call to log_counter_value() breaks an otherwise safe asynchronous code.*

```python 

async def increment_counter(counter):
     current = counter.current_value
     await log_counter_value(current)  # Unwanted context switch happens here
     counter.current_value = current + 1
```

SECOND, do you really have to deal with synchronization? In the web world especially, where HTTP requests are not supposed to interact, we want parallelization, not concurrency. Persistent data (and transactions) are supposed to be handled by external databases and caches, not in process memory heap. 

So usual thread-safety good practices (using thread-safe initialization of the process via locks, read-only structures for global data, and read-write data only local to stack frames) are enough to make the whole system "thread/greenlet/asynctask safe". 

If one day you need to implement highly concurrent algorithms inside a process, you'll choose the best tool for that, but no need for hammer-building factories if all you have to do is thrust one nail.

## Money: Bitcoins & Alternatives

Let's ponder for a moment. What are the biggest challenges of our 21st century? Climate change? Tax evasion? Legitimacy of state power? So candid minds could think that energetic sobriety, financial traceability, and (really) democratic organizations, would be goals to pursue.

But a group of smart hackers decided that current moneys were a major issue, and came up with Bitcoins: energy-devouring "proof of work" system, easy anonymity of money holders, and fuzzy (for the least) governance.

With such adequation between needs and demand, it's no wonder that Bitcoins became what they became: a product of (almost) pure speculation, praised by [ransomwares](https://cointelegraph.com/news/research-suggests-russian-based-hackers-behind-ryuk-ransomwares-25-million-gains) and miscellaneous mafias, mass-mined by factories of graphics cards, with an especially high appetite for [being stolen](https://cryptosec.info/exchange-hacks/) (or lost). 

This money, and its soon-emerged siblings, have a history already full of bewildering moments, with accidental chain splits, [soft forks](https://en.bitcoin.it/wiki/Softfork) blocked for [political reasons](https://en.bitcoin.it/wiki/Segregated_Witness), [hard forks](https://en.wikipedia.org/wiki/List_of_bitcoin_forks) quite arbitrarily decided by miscellaneous people (or forced by [cyber attacks](https://news.bitcoin.com/verge-is-forced-to-fork-after-suffering-a-51-attack/)), and endless battles between different currencies, or different versions of the same currency (Bitcoin Core, Cash, Gold, SV...). Algorithms (cryptography, consensus, transaction code...) were praised as the foundations of a bullet-proof and self-governing system, but some actors had to [hack their own users](https://www.coindesk.com/crypto-developer-komodo-hacks-wallet-users-to-foil-13-million-hack) to protect them from theft, while even the so glorified "smart contracts" showed loads of [scary security weaknesses](https://blog.sigmaprime.io/solidity-security.html#), and [not as many use cases](https://www.coindesk.com/three-smart-contract-misconceptions) as some expected.

Let's make it clear: the blockchain, a public ledger based on Merkle trees, is far from a bad idea. But when decisions are not based on the needs of society, and carefulness regarding bugs, but on ideology and greed, the outcome can be predicted. And the decline in hype is proportional to unduly invested hopes.

What is the "better" counterpart of Bitcoin, Ethereum, and the like? Lots of alternative cryptocurrencies exist, with lighter forms of authorization, with different crypto algorithms, with different privacy settings, with different adoption rates too... But if you ask me, what we would really need is "**an easily traceable money for State finances and NGOs**"; a public ledger designed so that any citizen could easily audit how public money is used, from the moment it's gathered via taxes and donations, to the moment it gets back into private circuits by paying goods or employee salaries. _Does anything like this exist yet, anyone? Couldn't find it..._

One could also mention non-cryptographic but _local_ moneys (ex. the "[Gonette](https://translate.google.com/translate?sl=fr&tl=en&u=http%3A%2F%2Fwww.lagonette.org%2F)" in Lyon, France), kept on parity with national moneys, which have the advantage of favoring local businesses and thus lowering the collateral damages of international trade.

## Data Formats: Text and Binary

A witty passerby once defined XML as "_the readability of binary data with the efficiency of text_". Indeed XML parsers tend to be sluggish, and to clutter memory (when in DOM mode), compared to binary data loaders; and editing XML configurations and documents by hand is not the best user experience one might have.

We easily understand why XML, as a metalanguage allowing to create new tags and properties for all kinds of uses, needs to be so verbose. But why such enthusiasm for text-based formats, when the goal is to transmit information between servers using well-defined data types ?

Parsing HTTP payloads into an internal representation, and then parsing, for example, its JSON body, ends up adding significant overhead to webservice requests. For what gain ? Binary formats like [Bson](http://bsonspec.org/) would make the serialization/deserialization much more performant; and semantically equivalent text formats could be used for debugging (auto-converted by web browser dev tools, Wireshark, CURL and the likes), and for manually crafting test payloads.

For sure, handling these dual representations of the same data would add a bit of complexity to the system, but in an era when startups love exposing webservices to thousands simultaneous clients, the performance boost can be real, with not so much effort. 

## Conclusion

What's the moral of all this? Always the same, "_use the right tool for the right job, and beware of irrational fads_". It can take lots of reading before one has a sufficient depth of view, on a specific matter, to take educated decisions; but this investment quickly pays off. 

Guessing how well a framework will be supported on the long-term, or which protocol/format will win a standardization war, is a different problem, but at least we can have our opinions firmly founded, when it comes to purely technical aspects, and this is Gold.


