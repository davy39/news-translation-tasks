---
title: 'Moving away from magic — or: why I don’t want to use Laravel anymore'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T22:34:12.000Z'
originalURL: https://freecodecamp.org/news/moving-away-from-magic-or-why-i-dont-want-to-use-laravel-anymore-2ce098c979bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C547D5BdRsA6qdzFz-5GgA.jpeg
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Niklas Schöllhorn

  It is time for a change in the tools that I use. And I’ll tell you why!

  First of all, I want to make sure that you know about my intentions. I am not trying
  to rant about Laravel or why other frameworks might be better.

  This arti...'
---

By Niklas Schöllhorn

_It is time for a change in the tools that I use. And I’ll tell you why!_

First of all, I want to make sure that you know about my intentions. I am not trying to rant about Laravel or why other frameworks might be better.

This article is very subjective. I’ll give you my thoughts and try to get you to rethink your framework choices as well. And when you stick with Laravel after reassessing, that’s fine. I have no intention to convert people away from Laravel to other frameworks or languages. But it is important to look closer and to make sure you know **what** you are using and **why** you are using it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C547D5BdRsA6qdzFz-5GgA.jpeg)
_Drowning because of too much magic. Photo by [Unsplash](https://unsplash.com/photos/PC_lbSSxCZE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Kristopher Roller</a> on <a href="https://unsplash.com/search/photos/magic?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Intro

I’ve worked with Laravel for about 2 years now. I always enjoyed how easy it was to spin up an application and get going in minutes. It provides so many useful tools out of the box. The console commands support you in every aspect during coding. They generate classes, scaffolding for authentication and much more.

But the deeper you go and the bigger the projects become, the more complicated the development with Laravel will get. Or, let me rephrase it: the better other tools will do the job. I’m not even saying it’s only Laravel’s fault. It’s also partly due to PHP not being very well designed.

Now, let’s start!

### Eloquent ORM

If you’ve already worked with Laravel, you surely know about Eloquent. It’s the ORM that’s shipped with a default installation. It comes with a lot of neat features. But its design makes your application needlessly complex and prevents the IDE from correctly analyzing your code.

This is partly due to the **Active Record ORM** pattern that’s being used and partly due to the fact that Eloquent wants to save the developer from having to write more code. To do that, it lets the developer stuff a lot into the model that doesn’t belong there.

Sounds like good intentions, but I started to dislike this more and more.

Let’s have a look at an example:

The first thing you see is that there are **no properties** on the model. This seems irrelevant but for me, it makes quite a difference. Everything is injected “magically” into the class by reading the table metadata. Of course, your IDE does not understand that without help. And you get no chance to name your properties differently from your columns.

Now check out the scope method. For Laravel users, it’s pretty clear what it does. If you call this method, it scopes the underlying SQL query by adding the given WHERE clause.

You can see, it is not static. That would mean that this method operates on a specific object of the class. But in this case, **it does not**. A scope is called on a query builder. It has **nothing** to do with the model object itself. I’ll explain that after you see how you usually call those scopes:

You’re calling a static method `popular()` that nobody ever defined. But since Laravel defines a `__call()` and `__callStatic()` method, it gets handled through them. [Those methods forward the call to a query builder.](https://github.com/laravel/framework/blob/5.7/src/Illuminate/Database/Eloquent/Model.php#L1610)

This is not only something that your IDE doesn’t understand. It makes refactoring harder, might confuse new developers, and [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) gets harder as well.

In addition, when putting such methods on your model, you are violating the S of [SOLID](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf). In case you are not familiar with that, SOLID is an acronym that stands for:

* **S**ingle Responsibility Principle
* **O**pen/Closed Principle
* **L**iskov Subsitution Principle
* **I**nterface Segregation Principle
* **D**ependency Inversion Principle

When you use Eloquent, your models have multiple responsibilities. It holds the data from your database, which is what models usually do, but it also has filtering logic, maybe sorting and even more in it. You don’t want that.

### Global Helpers

Laravel comes with quite a few global helper functions. They seem very handy and yes, they _are_ handy.

You just have to know that you sacrifice your independence for that handiness and your global namespace gets polluted. It rarely leads to conflicts, but avoiding that altogether should be preferred.

Let’s look at a few examples. Here’s a list of three helper methods that we have but don’t need since there are better alternatives:

* `app_path()` — why? If you need the path of the app, ask the app object. You get it by type hinting.
* `app()` — huh? We don’t need this method. We can inject the app instance!
* `collect()` — This creates a new instance of the Collection class. We can just new an object up by ourselves.

One more concrete example:

We are using Laravel’s global `request()` helper to retrieve the POST data and put it in our model as the attributes.

Instead of using the global helper, we could type hint a `Request` object as a parameter in the controller method. The dispatcher in Laravel knows how to provide us with the needed object. It will call our method with it and we don’t have to call a helper.

And we can take this a step further to decouple even more. Laravel is [PSR-7](https://www.php-fig.org/psr/psr-7/) compliant. So, instead of type hinting the Request object, you could also type hint `ServerRequestInterface`. That allows you to replace the whole framework with anything that’s PSR-7 compliant. Everything in this method will continue to work. This would fail if you’re still be using the helper methods. The new framework wouldn’t come with the helper method and therefore, you’d have to rewrite that part of your code.

You rarely switch the whole framework, but [there are people who do.](https://dannyvankooten.com/from-go-back-to-php-again/) And even if _you_ might never switch, it is still important for interoperability. Being able to inject dependencies and have a concise data flow instead of resolving and requesting dependencies and data inside out is the way to go. It makes testing, refactoring, and nearly everything easier when you get a grip of it.

I was happy when I read that with Laravel 5.8 [the string and array helpers get removed from the core and put into a separate package.](https://laravel-news.com/laravel-5-8-deprecates-string-and-array-helpers) This is a good first step. But the documentation should start to discourage usage of **all** helper functions.

### Facades

The arguments from the last part come into play here as well. Facades seem to be a nice tool to quickly access some methods that are not really static. But they tie you into the framework once again. You use them to manually resolve dependencies instead of instructing the environment to provide them.

The same goes for the complexity by passing everything through the magic methods.

Since we were talking about IDE support, I know some of you might direct me to the [IDE helper package](https://github.com/barryvdh/laravel-ide-helper) from barryvdh. You don’t need to. I already know this package. But why is it even needed? Because some design decisions in Laravel are just not good. There are frameworks where you don’t need that. Take Symfony for example. No need for IDE helper files, because it’s well designed and implemented.

Instead of facades, we could use dependency injection again as we did in the previous example. We’d have a real object and could call real methods on it. Much better.

I will once again give you an example:

We could easily clean this up. Let’s tell Laravel to inject a `ResponseFactory` and pass us the current request:

We have now successfully eliminated the use of facades from our controller. The code still looks clean and compact, if not even better than before. And since our controllers always extend the general `Controller` class, we could take everything a step further by moving the response factory to that parent class. We need it in all other controller classes anyways.

I heard that some people provide “too many constructor parameters” as an argument against injecting everything. But I don’t agree with that. It’s only hiding the dependencies and thus complexity in the first place. If you don’t like having 10 to 20 arguments in your constructor, you are right.

The solution isn’t magic though. Needing that many dependencies in a single class means that this class most likely has too many responsibilities. Instead of hiding that complexity, refactor that class. Split it up into new ones and improve on your application architecture.

Fun fact: there’s a real design pattern called “facade pattern”, introduced in the Gang of Four’s book. But it has a completely different meaning. Laravel’s facades are essentially **static service locators**. The naming just doesn’t convey that. Same naming for different things also makes discussions about architecture in projects harder, because the other party might expect something completely different behind that name.

### Conclusion

Let’s come to an end. I might write a follow-up soon about which technologies I prefer to use nowadays. But for the moment, let me sum up what we’ve learned:

Laravel’s approach to making everything as easy as possible is good. But it’s hard to get along when your apps become more advanced. I prefer awesome IDE support, stronger typing, real objects, and good engineering. I might even go back to Laravel when I want to write a smaller app.

A lot of my points are not only Laravel’s fault. I could swap the parts I don’t like, for example the ORM. But instead, I’ll just switch the toolkit, where the defaults fit my needs better. I see no point in using a framework where I have to spend more time in avoiding traps it sets for bad engineering than in developing my app. Other frameworks and tools come with better designed defaults and less magic.

So for now, I’ll say goodbye to Laravel.

Thank you for your time. I’d appreciate a nice discussion in the comments and I am of course open for your questions and suggestions.

P.S.: Special thanks to [Marco Pivetta](https://www.freecodecamp.org/news/moving-away-from-magic-or-why-i-dont-want-to-use-laravel-anymore-2ce098c979bd/undefined) for proof reading and additional input!

_Edit March 1st, 2019:_  
Since my article was posted on Reddit, I have created a Reddit account to answer a few comments. My account is not the one the article was posted from, but this one: [https://reddit.com/u/nschoellhorn](https://reddit.com/u/nschoellhorn)

_Edit March 13th, 2019:_  
If you read this far, you can as well check out my [Twitter profile](https://twitter.com/nschoellhorn). Thank you for your continued interest in this topic! I am always open to productive discussions, so please feel free to get in contact, either here or on Twitter.

