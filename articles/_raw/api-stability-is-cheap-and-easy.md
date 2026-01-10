---
title: API stability is cheap and easy, with Compat Patchers!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-28T21:00:40.000Z'
originalURL: https://freecodecamp.org/news/api-stability-is-cheap-and-easy
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/windowsserver_article_012-1.jpg
tags:
- name: api
  slug: api
- name: best practices
  slug: best-practices
- name: Compatibility
  slug: compatibility
- name: patching
  slug: patching
- name: Python
  slug: python
- name: stability
  slug: stability
- name: versioning
  slug: versioning
seo_title: null
seo_desc: 'By Pakal de Bonchamp

  Why backwards compatibility matters

  (If you''re already convinced that API stability is a crucial concern, not the whim
  of a few conservative mummies, save yourself some time and rush to the following
  chapter.)


  "WE DO NOT BREAK U...'
---

By Pakal de Bonchamp

## Why backwards compatibility matters

_(If you're already convinced that API stability is a crucial concern, not the whim of a few conservative mummies, save yourself some time and rush to the following chapter.)_

> "WE DO NOT BREAK USERSPACE!"

This [famous rant of Linus Torvalds](https://lkml.org/lkml/2012/12/23/75) is, alas, more relevant than ever.

> If a change results in user programs breaking, it's a bug in the kernel. We never EVER blame the user programs. How hard can this be to understand?

> If applications didn't care about specific error values, then it wouldn't make sense to have more than one to begin with, and you shouldn't care which one that was. But since applications _do_ care, and since we _do_ have multiple error values, we stick to the old ones, unless there are some _very_ good reasons not to. And those reasons really need to be very good, and spelled out and explained.

Let's replace "kernel" by any framework/library, and "error value" by "API signature", and we get an invaluable commandment of good programming. We can live quite well with a few buglets and imperfect features, but when our applications deliver segfaults or lengthy tracebacks after a simple version upgrade, there is a problem. A real problem.

And there is a paradox here. Regarding OS distributions, drivers, libc/gtk/Qt and other low-level, statically typed libraries, we expect - and are happy to experience - painless updates, bringing only new features and bugfixes. Whereas for our high-level web frameworks, mostly coded in dynamic languages, we have become resigned to the fact that each update could become a 3-days labor of understanding breakages, finding compatible versions of dependencies, and forking or monkey-patching until test suites are green again. Logically, shouldn't it be the other way round ? Why are most 1995 win32 freewares still working, why was the x32/x64 migration so transparent for most users, if a pluggable server app released 2 years ago is broken on multiple aspects?

I'll tell you why. 

API stability was once a very praised commitment. Semantic versioning was a must-have. Projects like Qt proudly detailed the measures they took to ensure their C/C++ would evolve without breakage. Some even filled their function parameters with NULL values "reserved for future uses". And incompatible changes were only evocated when no solution could be found.

Luckily, this mindset is still valid in large areas of programming. But now a different philosophy has contaminated minds, especially in the web industry. This spartan way of thinking could be called "Walk or die", "No paradise for the weak", or "As long as I warn, I can shoot the bullet". Sometimes hiding behind cute concepts like "calendar versioning", or "evergreen applications", this way of thinking is actually crystal-clear: the most minor software upgrade may introduce breaking changes - documented or not, proudly assumed or not -  just deal with it.

Why? Why not just let aliases, adapters, and other compatibility shims, when moving modules around, when renaming objects, when changing function signatures? With the dynamic and introspective nature of most modern languages,  isn't that a breeze? Sometimes development resources are so scarce that it's already too much. But the rest of the time? My guess is that when it is not a problem of technical skill, or of laziness, it might be a cultural issue.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/meme_bill.png)

Do you know this dopamine hit you get when you tick a box in a checklist, especially the last one? This satisfaction that sometimes makes you write an already completed task _just so you can tick it_? You might get the same thrill when you brutally refactor code to a cleaner architecture, or erase compatibility shims "_as per deprecation policy_". It's the happiness rush of the duty well done, of the return to purity. 

But this precise feeling is a huge lie. A blinding self-absorption. A harmful psychological bias.

Compatibility shims are not technical debt; nor a set of warts. At the very contrary, they are invaluable assets. With these few chunks of source code, our software extends its compatibility to tens, hundreds, thousands of miscellaneous libraries and applications spread across the web, in both public and private repositories, ranging from tiny utilities to huge corporate applications. These foreign codebases, full of business logic, of money-bringing features, of highly specific code, are what make their foundations worth existing. 

But this ecosystem is of an extraordinary diversity. Some repositories get commits every day from multiple contributors, some get a mass update once in a while when their maintainers get a little spare time, and some have not been touched for years (because their creator lost interest, or just couldn't find anything to improve). Some have Tox-like multi-version testing and continuous integration, some don't even have a single unit-test. 

So what happens when developers follow this trendy "Walk or die" philosophy? The ecosystem, already heavily fragmented by language (python2vs3, ruby, go, php... just for dynamic languages), by file format and network protocol, by framework and execution style (sync vs async), gets fragmented even more. In the most silent and deadly way. Basically, if we consider the codebases depending on a framework or library (here called "the software"): 

* Repositories that haven't been updated for a few years are broken by default.
* Repositories that are actively maintained, but do not target the same software version as us, do not work either.
* Bug trackers get filled with useless "Plz add support for version X.Y.Z" or "Plz restore support for version X.Y.Z" tickets.
* Forks flourish around mildly renowned repositories ; forks which can't be merged back, since each of their modifications are highly likely to break things for other software versions ; and the subsequent improvements brought by each forker, being chained to divergent codebases, keep spreading without ever being merged back ; naturally, they get remade by several developers each on his own, since few of them take the time to review the forks graph and cherry-pick interesting commits.
* Biggest projects sometimes get nice enough to provide a compatibility matrix, or "known working sets" pinned down to their patch version number. But as soon as you have more than a few dependencies, you enter a dependency hell that no conflict resolution algorithm can tackle ; you just have to fork, fork, fork, and monkey-patch, until your dependencies find an agreement.
* Project requirements get filled with links to git repository and commit hashes; semantic-less data which will make the next upgrades still more awkwardly experimental; or which will disappear due to an unexpected "force-push".
* Without surprise, many maintainers of these pluggable apps don't want to take on them the additional burden of filling their code with special cases, to work around the breakage frenzy of the main software's developers. As a result, the dependency hell keeps expanding unrestrained.

So when proudly pluralizing the name of a submodule, when removing a purportedly little-used utility class, when making an optional argument become mandatory, we're not improving anything. We're just murdering practicality for the sake of aesthetical purity. We're recklessly destroying entire regions of the software ecosystem, turning gazillions of test suites into reddish nightmares. But we'll never know to what extent; especially if we don't check. Ignorance is bliss.

Biological ecosystems can reach down to the depth of the abyss or to other planets if they have plenty of time; when things change too quickly, it's mass extinction. Software ecosystems are no different. Enjoying the cleanliness of an API "remade from scratch" is like enjoying the microbial sterility of a forest vitrified by a nuclear blast. 

![Image](https://www.freecodecamp.org/news/content/images/2019/06/meme_cant_break_compat.png)

For sure, it's a falsehood to think that because we use some open-source software, we're entitled to getting the bugfixes and features that we request. But it's equally false to think that because the users of our framework/library are not paying clients, we owe them nothing. They trusted us, built their own code against ours, followed our conventions and best practices, when they could have chosen another language/framework/library. How can we justify trampling their own efforts, making them waste days or weeks of development, just because we suddenly felt the irrepressible urge to change a naming scheme, or drop perfectly working code? We're all interdependent in a software ecosystem, and a tiny dose of awareness, carefulness and rationality can go a long way. "_But you're never sure that a change doesn't break things_", some will shrug. Sure. No one demands perfection. But not being deliberately harmful is already a very good start. 

There is like a paternalistic mood behind some advocates of the "walk or die" approach. "_If we stick to API stability, contributors will get lazy and never update their modules, the ecosystem will rot in place instead of moving forward_". Oh damn, how dangerous it is, to do people's good against their will. If we want users to update their codebase, at the very contrary, we should start by not brutally breaking things. We should bring shiny new features, not just a gun to their head. We should let them fix mildly annoying "deprecation warnings" when they feel like and can, not **right now**. We should let them spend their time on useful contributions, not on repairing what we have broken with the planned obsolescence that we dare calling "progress". 

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Compatibility-of-Hardware-and-Software.png)

Fun facts: advertising breaking changes in release notes does not grant them legitimacy; and when a private API is so handy that it's used by multiple projects, maybe it's a sign that it should be made public and documented, not that it should be wrecked at the first impulse.

So let's carve it into the marble of our desktops: API stability is, must be, on top of our list of concerns; along with robustness and adequation with final users' needs; but infinitely above any kind of aesthetical consideration. Only with long-term compatibility may our software ecosystems grow from a short elite of continually updated applications, to a huge and diverse galaxy of modules; some last- updated yesterday, some last-updated ten years ago, but all of them **getting stuff done**. Because that what software is all about, and that's what people are being paid for, at the end of the day. Not wasting time fixing the wheel that worked yesterday, and won't tomorrow ever more, because we heard the calling of the void.

## The Compat Patcher concept

Am I asking (open source) software maintainers to make more efforts, in order to achieve this so crucial long-term API stability? Nope. I wouldn't dare. At the contrary, I ask them to be lazier. But the good, the sensible, the both self-interested and benevolent, kind of lazy.

More compatibility means less support requests, less time justifying controversial changes, and more feature/bugfix contributions from our community. More compatibility doesn't even mean more keyboard typing. Except if we're only into toy projects, we've already put compatibility shims in place for a time. Just one thing to do : **leave them be**. They don't hurt us. They don't waste disk space. They are probably worth thousands of dollars per character. Let's just avoid one savage "Removing compatibility shim XYZ" commit, and move on towards greater goals.

And if the mere view of a compatibility shim makes us vomit (a not so unusual pathology I guess), there is awesome news : with high-level languages, we don't need shims in our code anymore. We just have to embrace the concept of **Compatibility Patcher** (or "compatcher" for neologism lovers).

Wat-iz-dat ? Just a companion library, often living its own life in its own repository, which plugs itself to the real software at startup time, and restores its compatibility with a decade of its previous versions. Thus, we can keep our codebase entirely unaware of whatever a "deprecation" might be, while still keeping a symbiotic coexistence with the thousands modules living in our ecosystem.

Monkey-patching is ugly, someone said? Maybe, but never as ugly as spending hours retro-engineering a whole plugin architecture, just to realize that an additional "S" in naming conventions sufficed to ruin everything. Programming overlords might prefer to weave their code with external shims using [aspect-oriented programming](https://en.wikipedia.org/wiki/Aspect-oriented_programming), but for most of us mere mortals, simplicity and pragmatism are widely sufficient enough. Some documentation, logging, and console warnings, are "explicit" enough to make anybody keep control over the codebase.

Let's not underestimate the power of high level languages. Examples with Python. We rename a submodule? Fine, thanks to import hooks, "_from framework import oldmodule_" and "_from framework import newmodule_" will return the exact same object. We change the signature of a function ? One tiny injection later, the old set of call parameters will automatically be adapted and forwarded to the new signature. We move an entire group of utilities out of the main repository? Fine, but as long as needed, the compatibility patcher will fetch them from their new location, and inject them back where they once so nicely belonged. We rename constants, classes, functions ? Leaving an alias was only costing a single code line, now with compatibility patchers this line doesn't even have to hurt our eyes and hearts anymore.

Please notice, Compatibility Patchers act like time travelers. They work even when developers delete a function, re-add it under a different shape, then remove it again. They work even when developers recklessly modify function behaviours, for example by exchanging similar arguments in-place. So imagine when developers cooperate with this system, and nicely decouple programming concerns so that the patch is minimal!

Cherry on the cake, by separating "state of art" code and compatibility shims, Compat Patchers make it a breeze to **selectively activate compatibility sets**. Your project is brand new and only relies on bleeding edge libraries ? Fine, deactivate the whole patcher. You just need compatibility with the last two major versions of the framework? Just enable the corresponding families of shims. You need support for very old packages ? Leave the patcher configuration in maximal mode.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/unicorn-deviant.PNG)
_That feeling when all 30 dependencies work smoothly on first install_

Now comes the anxiety-provoking part : what are the downsides of Compat Patchers? Answer: up to a few seconds of delay at startup (when all shims are activated), and a few logical operations and type checks here and there at runtime. That's it. In the modern web world, where most server processes run for hours uninterrupted, process the most unoptimized (text-based) formats conceivable, and where performance depends much more on DB optimization and proper caching than on raw execution speed, it sounds like a legitimate expense, doesn't it?

_Edit_: another limitation of Compat Patchers is that they require a tiny little bit of cooperation from core developers. Indeed, we all implicitly know the rule of backwards compatibility: "**Only Add Optiona**l". Add new optional arguments, add new functions, add new modules; don't remove elements and behaviours, don't make old options mandatory. But there is an additional, golden rule: **don't ever, ever, change the semantic of things in-place**. If we change the meaning of an argument, the format of an output, the action of a callable, without any additional indicator, then setting up shims becomes (almost) unfeasible; in this case, even Compat Patchers won't be able to resolve this ambiguity, and guess the behaviour that our users were requesting when using our API. Let's blacklist forever these kinds of [brutal](https://docs.djangoproject.com/en/2.2/releases/2.2/#admin-actions-are-no-longer-collected-from-base-modeladmin-classes) and [inimical](https://serverfault.com/questions/829754/why-did-the-format-of-nginx-ssl-client-i-dn-suddenly-change) changes.

## Time for practice!

Compat patchers are not just wishful thinking. 

[Here is one](https://github.com/pakal/django-compat-patcher) for the famous Django web framework. With a few dozens of small fixers, it allows one to use pluggable apps targeting from versions 1.6 to 2.2 of the framework. And it's only a start - feature requests and comments are welcome. 

This patcher is used in production on a few sites, including the [Pychronia](https://github.com/ChrysalisTeam/pychronia) portal and its CMS/Blog ecosystem. It runs on [CompatPatcherCore](https://github.com/pakal/compat-patcher-core), a Python micro-framework for creating such companion applications in the blink of an eye (a [cookiecutter recipe](https://compat-patcher-core.readthedocs.io/en/latest/startup.html) is even included). 

Without surprise, I warmly encourage you to bootstrap a Compat Patcher for the framework/library you might maintain, unless you are one of the few valiant minds already strongly committed to API stability.

This concept should also be easy to port to Ruby, PHP, Javascript, and other high-malleability languages. With lower-level and static languages, the task might be much harder (and require macro processors and the likes), but who knows.

**So here we are. Update breakages are not a fatality. Just a bad habit that we must _break_, thanks to a little pondering and a few technical niceties. We may thus enjoy the delights of ever-growing and ever-working software ecosystems, those which do make development fun and exciting!** 

_Edit 2019/07/05: Evocate the "hard scarcity of resources" as a possible reason for lack of shims, and tweak the tone of this part._

_Edit 2019/07/14: Fix typos, and warn against in-place semantic changes._

![Image](https://www.freecodecamp.org/news/content/images/2019/06/windowsserver_article_012.jpg)

