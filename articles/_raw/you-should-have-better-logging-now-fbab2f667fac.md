---
title: An introduction to logging for programmers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-27T09:30:50.000Z'
originalURL: https://freecodecamp.org/news/you-should-have-better-logging-now-fbab2f667fac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0syxG6pVAgyWwItiegWS8g.jpeg
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Stefanos Vardalos

  There is a part of software development that not all developers take very seriously.
  That part is proper logging and everyone who has lost countless hours during debugging
  knows exactly what I mean.

  Useful logs can provide the de...'
---

By Stefanos Vardalos

There is a part of software development that not all developers take very seriously. That part is proper logging and everyone who has lost countless hours during debugging knows exactly what I mean.

Useful logs can provide the developer ( especially when someone has to debug/maintain someone else’s code ) with tremendous help when trying to understand what the code actually does. Some developers say that stack trace is all someone should ever need but, that could not be further from the truth. Stack traces are great and can tell you where and what went wrong, but they can’t tell you how you got there in the first place. Surely you can follow execution through break points but, going in blind will make the whole process a lot more time-consuming than it actually should, and could be.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fyh4F1gDByMdWYn4u8Gjlw.png)
_Not very helpful_

That is the _diagnostic_ part of logging, the most important one and basically the one that developers could understand easier, as it is more part of their daily work routine. There is another part which is called _audit_ logging. Where the diagnostic logging takes care of recording the events that happen during runtime ( method calls, input/outputs, HTTP calls, SQL executions ), the audit logging is responsible for recording more abstract, business logic events. Such events can be user actions (adding/editing/removal of content, transactions, access data) or other things that have either managerial value or, more importantly, legal value.

In the back end world, there have been some great logging frameworks to choose from as the need for those arose a lot earlier. For example in Java, you can take a pick between Java’s own logging engine, java.util.logging or some great external frameworks like Logback or the most popular Log4j.  
In the front end world, things haven’t gotten that far yet, but there are options that can help you do the extra mile ( and of course get rid of trivial console.log messages ). Two such Javascript libraries for the front end are the minimal but powerful loglevel and the browser-bunyan, a port of the awesome node.js logging module for the browser. Some features are common between those frameworks but there are unique ones which should guide the developer to choose which one he needs. The use of those can be shown with some examples.

> Manifesto: Server logs should be structured. JSON’s a good format. Let’s do that.

As original [Bunyan](https://github.com/trentm/node-bunyan)’s manifesto goes, logs should be structured and easily indexed, filtered, searched. This awesome framework produces logs in JSON format which then can be easily consumed by other services for further processing.

Apart from the JSON exporting capability, [Bunyan](https://github.com/philmander/browser-bunyan) has the concept of child loggers, which can be used to create different loggers for different components of the application. That gives great flexibility as to what fields and extra info you want to include in specific parts of your application only. Bunyan also incorporates streams, which are the ‘output’ settings of its loggers. You can create multiple streams and assign one ore more to each logger and each stream can have different settings like the minimum level of logs to record ( acceptable levels of Bunyan are fatal/error/warn/info/debug/trace ) or output method ( in the browser there are only console related options but, in a Node environment you can do other things like write logs to a specific file ).

> This is a barebones reliable everyday logging library. It does not do fancy things, it does not let you reconfigure appenders or add complex log filtering rules or boil tea (more’s the pity), but it does have the all core functionality that you actually use

With quite a modest statement, [loglevel](http://pimterry.github.io/loglevel/) presents itself a minimal logging framework that adds just the bare minimum that most applications need. It adds some proper level-based logging ( trace/debug/info/warn/error ) and filtering as to what is the minimum level to be displayed on the console.

The power of this framework is its simplicity, as it is dead easy to incorporate it into your project and start using it, replacing the console.log() for ever. Furthermore, loglevel has one more hidden gem, its extensibility, as there are various plugins written for it, that provide extra features for those who want them, like [prefixing messages](https://github.com/kutuluk/loglevel-plugin-prefix).

Whichever framework you choose in the end for your JavaScript Application, you will save for sure a lot of hours of work during debugging and will make your application more future-proof.

