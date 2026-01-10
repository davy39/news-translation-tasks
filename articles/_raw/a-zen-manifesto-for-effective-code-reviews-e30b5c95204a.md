---
title: A zen manifesto for effective code reviews
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T20:30:34.000Z'
originalURL: https://freecodecamp.org/news/a-zen-manifesto-for-effective-code-reviews-e30b5c95204a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Pt73-k3YNsgjnOP8
tags:
- name: code review
  slug: code-review
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: teamwork
  slug: teamwork
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jean-Charles Fabre

  When you are coding, interruptions really suck.

  You are in the zone, flying high, killing it. And BAM… meeting, standup, insert
  interruption… Great!

  In that context, code reviews can be perceived as another hurdle to productivit...'
---

By Jean-Charles Fabre

When you are coding, interruptions **really** suck.

You are in the zone, flying high, killing it. And BAM… meeting, standup, *insert interruption*… Great!

In that context, code reviews can be perceived as another hurdle to productivity.

And frankly I can relate to that.

#### Code reviews are hard.

Not only do you need to stop what you are currently doing, you also need to immerse yourself into somebody else’s code. It takes _a lot_ of energy just to switch your focus.

#### Code reviews are time consuming.

According to [Slack Overflow’s 2019 survey](https://insights.stackoverflow.com/survey/2019#development-practices), 56.4% of developers spend 4 hours or more per week performing code reviews. And it can represent up to 20% of a developer’s week!

#### Code reviews are frustrating.

As a submitter, it can be frustrating to get your pull request rejected, to wait hours if not days for a review. As a reviewer, code reviews can feel like an obstacle to a good productive day.

Yes, code reviews can sometimes be hard, time consuming and frustrating.

But they’re also a good way to **share knowledge, prevent bugs, and reinforce your company’s culture** among other things.

What follows is a manifesto for submitters and reviewers to bring back peace of mind into code reviews. ?

### A Submitter’s Manifesto

As a submitter, here’s what you can do to increase your chances of getting your pull requests approved in a timely manner.

#### Submit when you’re done.

It sounds obvious, I know. But the thing is — most of the time if the machine doesn’t work, it’s not because it’s broken… it’s because it’s not plugged in!

Very small details can make a big difference on how your work is perceived. And you don’t want your colleagues to feel they are investing time and effort into reviewing work in progress code.

> Me: “It was just a missing </div>!”

> You: “Yeah I know, but the whole thing didn’t work and it took me 20 minutes to spot it.”

So here’s what you can do:

* **Self-test your code.** Include WIP in title or label if you’re not done yet.
* **Self-review your code.** Use the diff report of your code editor or versioning tool to catch mistakes.
* **Make sure the tests of your CI are green** before assigning a reviewer, this will save them time.

![Image](https://cdn-media-1.freecodecamp.org/images/5O1kil0Dxt4qNqUrwFEx6sfPRoyjWHqdD7df)
_Don’t be this guy, obviously ? (G[iphy)](https://giphy.com/" rel="noopener" target="_blank" title=")_

#### Make smaller pull requests

I get it, it’s a big, important and complex feature and you might be tempted to submit a long pull request. Yet, most of the time, you are better off submitting smaller pull requests.

Code reviews take energy. Big code reviews even more. Don’t impose on your team a **developer vs food** challenge every time they review your code.

Be nice, cut it in smaller chunks. You are also doing yourself a favor:

* **You’ll get more qualitative feedback.** The longer a pull requests the fewer qualitative feedback per line of code you’ll receive. Keep your pull request small (not too small either) and you’ll increase your chances of getting great feedback on it.
* **You’ll get them approved faster.** It’s a win-win, by breaking down your work into smaller pull requests, you increase your chances of getting them approved faster.

![Image](https://cdn-media-1.freecodecamp.org/images/irUe6ZKsZwrWHJwrIqGsymee1oo2cq0mMEBs)
_LGTM ?_

_For the nerds out there, here’s a [study](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) conducted on a Cisco programming team. It shows that after 400 LoC the ability to find defects diminishes pretty dramatically._ ?

The next principle helps with keeping pull requests size under control.

#### Narrow the scope

The scope of your pull request should be **simple, unique and well-defined.** That might be a feature, a user-story or a bug fix.

![Image](https://cdn-media-1.freecodecamp.org/images/hVle2Ce9EvgyfDMvplMuSbg3FpXTF9CN55-j)
_Making the world a better place, one LoC at a time ?_

One way to think about it is that reviewers have a **limited number of “attention credits”** (like everybody). Every time they focus on something, they use 1 credit. What happens when they have 0 left?

> LGTM ?

Do what you can to reduce the noise around your work. Be mindful of the reviewer’s attention span.

For instance, **avoid void changes** (like skipping lines). They don’t add any value and complicate the code review.

Similarly, if your pull request changes the _behavior_, don’t include changes to _formatting_. Conversely, if your pull request changes _formatting_, don’t include changes that affect the _behavior_. They might be overlooked by the reviewer.

#### Give context

Think about your pull request as documentation for new comers. Guide the reader with context.

Start with a **self-explanatory title.**

![Image](https://cdn-media-1.freecodecamp.org/images/-rZMLs8GynJOJMIB2C1ZTf1sa22RdiccZaw2)
_Good title taken from the xg2xg repo ?_

Then**, write a clear description** to explain what you are doing and why are you doing it. What is the purpose of this pull request? Why is this change necessary? How did you approach this problem?

![Image](https://cdn-media-1.freecodecamp.org/images/QfB-BL9MLi1SnpFMByRDtEoGcLsnhYqAbtUZ)
_Good example of explaining why the change is necessary taken from react repo_

The description is also is great place to **point out unresolved issues and open questions.** Reviewers might have suggestions to unblock you.

Are you working on a visible part of the product? **Screenshots** can help get your point across faster.

* Show before/after differences.
* Use colored arrows.
* Add screen recordings if you feel like it :)

![Image](https://cdn-media-1.freecodecamp.org/images/BMOl9N0I3lUy6RFHW6koF-AHvUaS3zj8ZJzz)
_From react repository_

Finally, write **information signs** along the way to guide the reviewer through your reasoning.

Keep a clean commit history to make it easier for the reviewer to follow your step. Use comments to point out alternatives you explored.

![Image](https://cdn-media-1.freecodecamp.org/images/parB1wMVMrNCIoUjqixRqCHHJ08HMuE2FEb8)
_Good comment example from Lodash_

#### Welcome feedback ?

Rejection hurts.

Truth be told, **code rejection hurts even more.**

![Image](https://cdn-media-1.freecodecamp.org/images/Hw2grLkrNu8rHBcUJxqHt9v71eUAPRVwiBnn)
_I’m seeing this a lot!_

It’s alright. Don’t take it personally.

Comments and suggestions are an opportunity to learn and become a better software engineer ?

### A Reviewer’s Manifesto

Congrats on making it this far! Now let’s look at a few principles that might help you become a better reviewer ?

#### Adopt the right mindset

There is no scenario where a team can benefit from a reviewer being mean or patronising. **Be** **kind**. Period.

![Image](https://cdn-media-1.freecodecamp.org/images/xLy0yeaSYmd9HAUIDvcN892VA7ehvPvD4b5p)
_What are you trying to say my friend? ([Giphy](https://giphy.com/" rel="noopener" target="_blank" title="))_

Want to make code reviews more exciting?

Look for something you can **learn** from this review. A new library, a new method, a new concept, a simpler way to do things. What piece of knowledge will you extract from it?

If you are the more experienced developer, is there something you can **share**? How can you use this review to transfer knowledge to the submitter? How can you help them become a better software engineer?

![Image](https://cdn-media-1.freecodecamp.org/images/CA98J-KCq3p77rFiVmv4W5ojoQnUnBEvgNOn)
_Thanks for the tip mate! ?_

### How to actually do a code review

#### **What to review**

What am I even supposed to look for? Without clear guidance on what and how to review, it’s easy to get lost. Here is what you can do.

First off, **check the purpose**. Is this code accomplishing what it is meant to do? Are there parts of the new code that are not clear to you? Ask clarifying questions. The code is easily testable? Test it. There’s no need to go beyond if this square is not checked.

Ok now that the code works, time to focus on the **implementation**.

Think about how you would have approached this problem. Would you have done it differently? Is there potential for refactoring or abstraction? Is this re-inventing the wheel? Is this using standard code patterns?

#### **What to not review**

Because a piece of code has room for improvement, it doesn’t always mean it needs to be improved.

At the end of the day, code reviews are a tradeoff between **quality** and **velocity** and depending on the scope and stage of the project it might make sense to let a few things behind.

Similarly, you shouldn’t be doing things that can be automated. Let your favorite linter hunt for the missing semicolons and extra indentation. No need for an endless debate on tabs vs spaces.

Finally, don’t increase the scope of the pull request. If you think of new things that need to be done, create a new pull request /task for that matter.

#### Review in a timely manner

There are at least 3 good reasons to review pull requests in **hours rather than days.**

* The submitter can move to the next task quicker
* It reduces context switching cost
* It reduces the risk of merge conflicts between branches.

![Image](https://cdn-media-1.freecodecamp.org/images/XVktldbIDiDVoWG2GCGSIo4ppuEMv49qFU5m)
_Opened 6 years ago. Be right back ?_

**Disclaimer:** I just released [GitRise](https://www.gitrise.com/), a tool that helps teams using GitHub & Slack review pull requests faster. I do think it can help with this one :)

### How to give feedback in a code review?

When giving a feedback, the form matters as much as the substance.

Did you know that in written communication, **neutral content looks more negative than it actually is?** Beware of this bias and include emojis when needed to get the tone right in your comments.

Also, most of the time, even if you are pretty sure that there is a better way to do something, you are better off **asking a question rather than requesting a change**. Plus, questions sound less aggressive.

![Image](https://cdn-media-1.freecodecamp.org/images/YDgB2aLyBwOvo21kVLfvYdlKdlTioV1UUP4a)
_Example from ember.js repo_

**Finally, reward when things are done right.** Code reviews are also a great place to give kudos to colleagues for doing a good job. Be creative and fun :)

? Congrats on reaching the end of this blog post!

? Thanks a lot for reading and let me know if you have any comments!

? I **just released G[itRise,](https://www.gitrise.com/) a tool that creates pull requests reminders for teams using Slack & GitHub. G**ive it a try if you want. Looking forward to your feedback.

