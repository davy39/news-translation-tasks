---
title: How to make your code reviews fun (and not dreadful)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T21:31:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-code-reviews-fun-and-not-dreadful-daf4dbabc428
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ypd0z4OhOmegm-WHyGHgxg.jpeg
tags:
- name: code review
  slug: code-review
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: workflow
  slug: workflow
seo_title: null
seo_desc: 'By Eumir Gaspar

  I’ve done my fair share of code reviews. By fair share, I mean a lot. Have you ever
  done a code review of an epic feature? I have. It was not a great experience, because
  by the time the 100th file was to be reviewed, I was already fat...'
---

By Eumir Gaspar

I’ve done my fair share of code reviews. By fair share, I mean a lot. Have you ever done a code review of an epic feature? I have. It was not a great experience, because by the time the 100th file was to be reviewed, I was already fatigued looking at code. I was so close to just going “Yup, looks good to me” and then giving my approval.

But that’s not how code reviews work. Once you’ve started, you’ve got to stick to it and finish it until the end. Sure, you can take breaks, but then you start loosing the context and have to start all over again, like this:

![Image](https://cdn-media-1.freecodecamp.org/images/Ck2NsPyZNpjQBRFLQWbadZTPrPhDcpRlsHmf)
_[Cartoon by Jason Heeris](http://heeris.id.au/2013/this-is-why-you-shouldnt-interrupt-a-programmer/" rel="noopener" target="_blank" title=")_

I digress, though. The pain is not what I’m supposed to talk about.

So how do we make it, say, less dreadful? First, even before making the pull request, and even before we started coding, we should make it a point to break down features into nice small pieces. Development and deployments become quicker, as it’s always easier to deploy a mini-feature than an epic one. This makes code reviews easier and faster to perform since the changes are fairly small.

Great! I hope you liked my article. Let’s all go home…

Wait, **stop**!

That was about how to make it less dreadful, but how about making it fun?

### Using memes in code reviews

_Disclaimer: the following are my own thoughts and not of my employer._

I just wanted to get that out of the way, because this can potentially be a controversial topic. Anyway, we make our code reviews lighthearted by adding [memes](http://knowyourmeme.com/memes/memes).

I can hear your eye roll from here! Hear me out though. [What better explanation than to link to someone else who gladly explained it already](https://medium.com/@adamkoszary/look-at-this-absolute-unit-763207207917)?

It is tone that helps make it fun for both the reviewer and the person whose code is being reviewed. One example would be the very first “staple” in my `image wallet`. I noticed that [Rubocop](https://github.com/bbatsov/rubocop) was missing some double spaces in our files, so when someone submitted a pull request with a bunch of extra white space, it was a no-brainer to give them a [doge](http://knowyourmeme.com/memes/doge).

![Image](https://cdn-media-1.freecodecamp.org/images/nUXPIWCWtNzEIkdH5dS1SlOncwX-6gBtsJPD)
_wow. much whitespace. such line breaks._

It was a simple image, and yet the message was very effective. I remember people laughing when they saw it. People didn’t want to get “doged” so everyone was more vigilant in their extra whitespace.

It was easier to open up finder, drag the doge to a comment, and post, instead of just typing the plain old `Please remove the extra whitespace` in the pull request (PR), especially if there were multiple doges.

### Couldn’t it backfire?

It totally could. I’m not saying everyone should follow our team. It really depends on the team’s personality. Ours has an average age of six years my junior, which means most can relate to memes. It would be a different story if your team has an average age of forty (unless of course, they were denizens of 4chan or are up to date with the latest memes!).

You know your teammates best, really. After a few months of being with each other (especially since we were pairing almost 100% of the time), we kind of had a feel of each other’s humor, so to speak. This made us comfortable in seeing memes in our PRs and just having a laugh about it (while fixing the issue, of course).

### What benefits do you get from memes?

Well, one benefit is that it makes reviewing faster (at least for me). The person who also submitted the PR actually understands what they need to do faster. Instead of reading a few words, you see an image — and we all know images speak louder than words. Here are a few examples from my `personal image wallet™` :

![Image](https://cdn-media-1.freecodecamp.org/images/tuGwZyZ1KP1QO56Z8-iljQ007ufkOL9CH1Dw)
_Delete this line!_

When I bring out an image for the first time, I add a description / explanation on what they need to do / fix. The above basically says remove the above “legacy” code. Delete it. Destroy it!

![Image](https://cdn-media-1.freecodecamp.org/images/14sYrRTvkQ9BvRGHs5tuzXnjREEkGbGVlsjH)
_Mmmmm pretzels_

This is specific to Ruby - the `[pretzel dot](http://mitrev.net/ruby/2015/11/13/the-operator-in-ruby/)` operator is basically a short cut for a `try-catch`. I just highlight the snippet that needs a pretzel and paste this image. Quick and easy!

![Image](https://cdn-media-1.freecodecamp.org/images/qwqPKNzCHncJC19pqxJBbTXM5VQHkiMG4HdF)
_AH-AH-AH!_

![Image](https://cdn-media-1.freecodecamp.org/images/jvIFwOePL9nOau1UebnU77DdUKD6o9aH83SD)
_It actual does bother me (the cold)_

These two I just use interchangeably and again, MOSTLY in Ruby where we always add the `# frozen_string_literal: true` magic comment at the top of the file. With [Rubocop](https://github.com/bbatsov/rubocop) at the helm, though, we have seen less and less of Elsa and Mr. Freeze. They also show up for any constant that needs freezing.

![Image](https://cdn-media-1.freecodecamp.org/images/-XyiIVBrpiNFAIK7GWNWqoJA3G0u5alKu4yJ)
_Love this GIF_

This is pretty straightforward (I hope). When colleagues see this, it is a sign they had a typo. I usually highlight the typo as well so it’s quick and easy to see (and fix).

These are just a few of them. Remember though, too much of something is **usually** not a good thing. So just take care when you add your memes. It is also best not to add too many memes, as sometimes it can get distracting. Finding the right balance of tone and just sending the message across as quickly as possible is the best way of wrapping up a pull request.

### That’s all, folks

In conclusion, it really is up to you if you want to have fun, or just stay serious and professional at work. Some may think memes are unprofessional — and sure, in formal work stuff they may be. One can argue that a pull request can be or is a formal work-related thing, but I think it only applies if you use it for documentation or reviews. Otherwise, I think it is “free speech” (yep, pulled that card!) and should just be taken as it is.

For me, it conveys what I want to say: remove extra whitespace, fix spelling, freeze a constant, or remove a line or lines of code. I don’t have to type much, my colleague doesn’t have to read a bunch of words against another bunch of words, and it lightens up the mood a bit. Everybody wins! With that, I’ll end this with another one of my images:

![Image](https://cdn-media-1.freecodecamp.org/images/JTYj7y9qsEpADLb-u20Z7dagkFmAO2KgIuA8)
_I WONDER_

