---
title: Code Calligraph VS Code Chicken Scratch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-13T12:25:06.000Z'
originalURL: https://freecodecamp.org/news/what-is-shitty-code-handwriting-ae7c00708b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D9KCF2ipzxxvUXGu1ya9GA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alex Ewerlöf

  Over the past 17 years I’ve worked on over 90 projects with many teams. But it wasn’t
  until I came across Git’s blame feature that I learned about each coder’s “handwriting.”
  This simple curiosity soon became a habit. Whenever I saw n...'
---

By Alex Ewerlöf

Over the past 17 years I’ve worked on over 90 projects with many teams. But it wasn’t until I came across Git’s `blame` feature that I learned about each coder’s “handwriting.” This simple curiosity soon became a habit. Whenever I saw new code, I tried to guess who wrote it. Then I’d verify my guess with a `git blame`.

(By the way, if you aren’t familiar with [git](https://en.wikipedia.org/wiki/Git_%28software%29) yet, it’s a popular way for developers to collaborate on code, and its “[blame](https://help.github.com/articles/using-git-blame-to-trace-changes-in-a-file/)” feature shows you who has authored a given line source code.)

After a couple of years, I started to see patterns, just like [a handwriting expert](http://www.dailymail.co.uk/sciencetech/article-2380858/What-does-handwriting-say-Study-finds-5-000-personality-traits-linked-write.html) might detect a sociopath from the way they draw their W’s. Code handwriting reveals a lot about the programmer who wrote it.

You can learn just about anything from a programmer’s code handwriting: how much experience they have, how much they care about their code’s readability (and by extension, how much they care about their teammates).

Code talks. [Bad code](https://en.wikipedia.org/wiki/Code_smell) screams! So is the code you’re reading code calligraphy or is it code chicken scratch?

A quick disclaimer: what you’re about to read is based purely on my subjective intuition. As far as I know, there haven’t been any peer-reviewed academic studies. My code handwriting analysis skills have served me well in the past, and may help you as well, but — as with anything you read on the internet — your mileage may vary.

### Insight #1: Bloated code = struggle

Usually when I discover code that has become bloated, and way larger than it needs to be, it shows a programmer who was struggling to finish a task that was beyond their abilities. They either didn’t have the knowledge or the time to finish the job properly.

In real life, people who _do_ less, tend to _talk_ more. It’s the same over in code land: those who can’t do the job elegantly tend to write a lot of code.

Unfortunately, bugs feast on code, and the more code provisions, the larger the habitat for bugs.

> “I hate code, and I want as little of it as possible in our product” — Jack Diederich

![Image](https://cdn-media-1.freecodecamp.org/images/1*geAN2yrvAR4mfd8C9Uqq6w.jpeg)

### Insight #2: Dead code = sloppiness

Ever seen huge blocks of commented code committed to the repo? Or even worse: code that doesn’t do anything special but is there for historical reasons?

Interestingly, this has a direct correlation to the messiness of the desk of the programmer who wrote it. Ever seen outdated comments or tests? Yep, you found a careless programmer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WwxpH0REH0QGkwycpDRDhQ.jpeg)

### 3. Complex code = stupidity or greed

I love this quote from [Schumacher](https://en.wikiquote.org/wiki/E._F._Schumacher):

> “Any intelligent fool can make things bigger, more complex, and more violent. It takes a touch of genius — and a lot of courage to move in the opposite direction.” — Fritz Schumacher

If you found code that is hard to follow or comprehend, rest assured that it was written either by someone who doesn't have a clue what they are doing or someone who seeks job security by taking “ownership” of that part of the code.

### Insight #4: Comments = a team player (unless…)

All high-level languages allow writing code that is readable enough that you shouldn’t need comments. But sometimes complexity is inevitable due to a lack of knowledge, time, or elegant framework.

I really love it when programmers put a link to API reference or a relevant Stack Overflow question when they realize that their peers (or their future self) will question a particular line of code.

That being said, over-using comments shows a lack of self-esteem (or as I mentioned earlier, trying to explain away “bloated code”).

### Insight #5: Names = communication skill

Variable names, function names, parameter names, class names. These are the basic level of communication to code maintainers.

If you come across single letter names (except for `i`, which is the default in `for` loops) you’ve found a programmer with lack of communication skills or empathy for others.

Unless it’s a temporary project that isn’t going to be shown to anyone else or maintained, every second put into picking a suitable name results in good karma.

And if an entity’s functionality changes, it’s important to refactor its name accordingly.

Some programmers claim that names aren’t important, since the machines don’t care. Well, unless you’re writing code literally in zeros and ones, you’re writing code for humans too!

### Insight #6: Poor readability = lack of fluency

Sometimes programmers are fluent in one language, but they try to twist and bend another language to behave like their favorite language.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IqL4tmjw8DiMvHT5Q9wGOg.jpeg)

JavaScript is one of those poor target languages.

Most back-end programmers have the luxury to pick their “mother language.” And many are brave enough to hack together a few lines of front-end code. But since the browser land is mostly JavaScript (which is a flexible language), they try to imitate what ever patterns are familiar to them from their “mother tongue.”

This is all good and well until an actual JavaScript programmer sees the code and pulls their hair out!

### Insight #7: Hacks = shallow personality or lack of discipline

Ever spent lots of time tidying up a code base only to witness your peer [pouring gasoline all over your beautiful code](http://blog.codinghorror.com/code-smells/) by using it as a platform for quick and dirty fixes?

Congratulations: you met a hacker!

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Oxwskpp6ntXreTWOflWGQ.jpeg)

Hackers are great in making quick fixes without bothering to understand the architecture holistically (usually by fussing with a debugger, or through trial and error).

So wWhat’s the catch? They fix one problem and create 10 others.

Consultants have a tendency to show this behavior (since their time is expensive, and they’re not going to live with the consequences of their changes). Besides, they can get paid to fix those 10 other problems and sow job security by making 100 new ones.

Nevertheless, I’ve witnessed internal programmers who make even the sloppiest consultants look like rock stars. Ever estimated an issue to take 8 hours, but some product manager cuts your estimate to just 1 hour? That’s usually when the hacks are born.

That being said, sometimes you need quick delivery (like during the prototyping phase in a start-up to validate the idea) and it’s accepted to cut corners due to limited resources. No one cares about a beautiful code that doesn't solve any problem. But still there’s a difference between cutting with scissor or chopping with a machete!

### Insight #8: Inconsistency = pride and fanaticism

> When in Rome, do as Romans do. — a proverb

There are so many coding conventions. It doesn't really matter which one is picked. But once your team picks some conventions, it’s crucial that they stick with them .

If contributors ignore some or all conventions, they are either hacking away or are too proud to change their style to match your code base.

Worst of all is when they push for their own conventions instead. That’s pure fanaticism. And you can be sure that the programmer is narrow minded in other matters as well.

### Insight #9 WET code = bad memory

The opposite of [Dry](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (“Don’t Repeat Yourself”) is WET (“We Enjoy Typing” or “Write Everything Twice”).

Well, bugs reproduce through a messy process called “copy” and “paste.”

There are surprisingly many types of WET code. For example:

1. A function or class that’s written twice, only with minor differences
2. A variable that holds the value of another variable
3. A set of repetitive instructions that could reside in a function

This is different from bloated code, in that rather than being merely complex or twisted, WET code is quite literally repeated.

Usually repetitive code is a sign that a programmer can’t recall (or worse, hasn’t seen) the other similar code. One of the main tasks of the human brain is to detect patterns. When a programmer is unable to spot similar code, it’s a sign of inexperience or inattention to detail.

### Insight #10. Temporary workarounds = lack of discipline

Sometimes developers will inject a quick and dirty solution as a temporary workaround, hoping that some day they’ll get around to refactoring it. This usually happens because of a close deadline or a lack of knowledge. But as we all know, temporary workarounds are there to stay.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-G0N_d5G6zCDxcExo8qafQ.jpeg)

Temporary workarounds indicate a pragmatic engineer who lacks any taste or pride in their work. They can also be a sign of low self esteem, because they don’t want to disappoint someone else (boss, customer, etc).

The only time a temporary workaround is acceptable is for a learning project or prototyping (proof of concept). And even in those cases it’s best to refactor it as soon as you know how to do it the right way.

### Insight #11: Lots of dependencies = carelessness for the future of the project

Dependencies need to be kept up to date. When a project has too many of dependencies, it’s a sign of sloppiness.

It’s hard to say what is “too much” but the rule of thumb is: if the project can easily survive without a dependency, it’s redundant.

Another measure is that if there’s no necessary requirement for the underlying problem that the dependency is solving, it’s probably unnecessary.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MfKP9AjNFtlQUdxU8_8R_g.jpeg)

### There are three motivations for unnecessary dependencies:

#### Reason #1: The developer is too eager to learn new stuff.

By importing new dependencies, they get the chance to do that learning in a real project.

Curiosity is good but there should be other platforms for learning, like side projects, short term tasks, or hackathons.

You don’t want to lose a good developer because they think they can’t grow at their job, but you don’t want them to treat your product like their pet project, either.

#### Reason #2: It’s done by an overly-ambitious junior developer.

The newcomers in any field tend to be overwhelmed by all the new buzzwords, and out of frustration or ignorance (or the recommendation of a “pro”) they may decide to “jump into the pool” and learning everything at once. Don’t let them. [Pick your technology](https://medium.com/@alexewerlof/how-i-learn-new-tech-cb79db19c818).

#### Reason #3: The developer has baggage from another job (or a side project)

They want to have an edge over their peers by bringing in something that only they know very well.

Unfortunately there’s no easy solution to this but soft skills: the team has to question the choice of every dependency, and if there’s a proper code-review and merge process in place, it makes it hard to sneak terrible code in without someone noticing it.

Sometimes the cowboy coder in question may do a massive refactoring, then put the team into a position to accept the whole change because it’s already done. Well, don’t! Ask them to break their pull request into smaller parts and be skeptical about bringing new dependencies. Yes, it’s more work but it’s gonna save much more time and energy on the long run.

Good developers care about the future of their project because they spent their most finite and precious resource to create it: their time!

![Image](https://cdn-media-1.freecodecamp.org/images/1*kco_a6noe_ekN5aRq_vPCw.jpeg)

By the way, a lot of dependencies and trendy buzzwords can also be a sign that the developer is building up a resume and already gearing up for their next job.

### Code calligraphy

Now that we’ve discussed code chicken scratch, let’s talk about the flip side: code that is an absolute pleasure to read.

Some even say “[code is poetry](https://www.smashingmagazine.com/2010/05/the-poetics-of-coding/).”

The source code for [jQuery](https://github.com/jquery/jquery) or [lodash](https://github.com/lodash/lodash) are great examples, but pretty much all popular libraries on Github that a lot of contributors will eventually converge upon beauty. This, my friends, is marvelous _code calligraphy_.

Essentially, great code is:

1. Easy to read, follow, and debug
2. Flexible, configurable, and extensible
3. Smart with resource usage
4. High performance

Note that some projects demand a different order. For example, [the Linux source code](https://github.com/torvalds/linux) might not be very easy to read because performance is more important for an operating system. Or a humble embedded IoT application may sacrifice configuration in favor of resource optimization.

Anyway, there’s much more you can find out about your peers just by analyzing their code. Code speaks louder than words! So the next time you’re reading some code, try out the `git blame` command and start recognizing code handwriting.

_⚡_️_Liked what you read? **Follow** me to be notified when I write something new._

Also you may wanna check out why [programming is the best job ever](https://medium.com/p/what-s-cool-about-being-a-programmer-5a1e58efeee6).

