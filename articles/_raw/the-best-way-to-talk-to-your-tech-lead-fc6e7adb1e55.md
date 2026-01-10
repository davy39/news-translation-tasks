---
title: How to talk to your tech lead and fix your communication glitches
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-30T18:06:58.000Z'
originalURL: https://freecodecamp.org/news/the-best-way-to-talk-to-your-tech-lead-fc6e7adb1e55
coverImage: https://cdn-media-1.freecodecamp.org/images/1*By6rwJTTUNUXSsm0iTEZaw.jpeg
tags:
- name: leadership
  slug: leadership
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Greg Sabo

  Here’s where you messed up.

  Your tech lead told you to build out a new API endpoint for an upcoming feature.
  It was supposed to be simple: just return a list of the current user’s email addresses.

  You start with the usual boilerplate. Yo...'
---

By Greg Sabo

Here’s where you messed up.

Your tech lead told you to build out a new API endpoint for an upcoming feature. It was supposed to be simple: just return a list of the current user’s email addresses.

You start with the usual boilerplate. You register the new endpoint. You associate it with a controller. You add an explanatory comment.

Then you discover that the query is impossible. The user’s email addresses all live on different database shards.

The footlights flip on. The curtain rises. This is your time to be a software superstar! You’ll use your hard work and creativity to find a solution to this unique problem.

You begin building a denormalized table to keep the data local to the user’s shard, as well as a wrapping layer to keep the copies in sync. Your solution is scalable and performant. Look at you go!

Here’s the problem. You didn’t talk to your tech lead. From their perspective, they gave you a simple thing to work on, and it’s taking you three times longer than expected. It doesn’t matter if you’re creating the perfect architecture. You’ve eroded trust in your relationship with your team lead.

The best engineers can create elegant systems, but they also talk to their tech leads the right way. Here’s what I recommend.

### 1. During meetings, focus on how you’re tackling what’s going wrong

It’s time for the standup. What are you going to say to your team and your teach lead?

“I’ve made some progress on this thing yesterday. I ran into some test failures, and I’m fixing them now. I hope to ship this today.”

That was a status update. And it was pointless.

Status updates are communications that have no response other than “OK, sounds good.” Why spend the time giving these in-person updates then?

The whole point of holding standups is to encourage team members to unblock one another. The traditional three questions are:

```
1. What did you finish yesterday?2. What will you finish today?3. What's blocking you?
```

People often focus on the first two and omit the final thing entirely. But it’s the most important!

People often interpret “What’s blocking you” as “What’s completely stopping you from working?” That’s why I prefer the question “What’s your red flag?” instead.

A red flag is **anything** that’s going to slow you down. Here are some examples of red flags:

* “I’m not sure how to get started on the test for this.”
* “I need to figure out what the mobile team needs me to do here.”
* “I need to refactor this component to get this to work.”

None of these are things that are completely stopping you from working. But they are going to take up a considerable portion of your time.

This is what your tech lead wants to hear. It’s their best opportunity to do their job, to help speed you up and come up with solutions to your trickiest problems.

An important note about red flags: you should always maintain clear **responsibility** for your project as you state your red flag. You shouldn’t be in the habit of using red flags as an excuse for not getting your work done.

Most people want to sound impressive during their standup. They want to say, “Look at all this stuff I got done yesterday! Look at how awesome I am.” Resist that temptation, and instead focus on how you can accelerate the work ahead.

### 2. Between meetings, communicate proactively

When you’re working as a team lead or tech lead, you have this constant paranoia that your team is completely stuck and you don’t know it.

You come into your team’s work pod, and everyone’s at their desk. But what are they doing? Are they making good progress? Are they spending their time implementing something the completely wrong way? It’s hard to tell.

And of course, the tech lead absolutely must have a trusting relationship with their team. They can’t let this paranoia control their behavior at all times. So they end up not asking.

This is your opportunity to meet one of your tech lead’s needs. You should proactively communicate about what you’re doing at least twice per day.

What do I mean by proactive communication? I mean any conversation that’s initiated by you. Check-ins started by your tech lead and scheduled meetings don’t count as proactive.

Examples of ways to kick of proactive communication:

* Sending a Slack message
* Commenting on an Asana task that they’re following
* Catching them as they come back to their desk

Proactive communication sometimes takes the form of [asking for help](https://hackernoon.com/how-awesome-engineers-ask-for-help-93bcb2c7dbb7). “I can’t get this module to import and I don’t know what’s wrong. Can you help?” These are opportunities for the tech lead to do their job, and if you’re truly blocked then it’s time well spent.

The other form proactive communication can take is a checkpoint. Something like, “I’m working on this feature, and I’m finding that I’ll need to hoist this state up all the way to the root component for it to work. Let me know if you want to discuss this.” This is a great way to surface potential architectural disagreements. Stop waiting for code review before talking about this stuff, seriously.

Proactive communication seems easy. In practice everyone hesitates before “bothering” someone else with this kind of communication. Try adding a daily task to your to-do list to proactively communicate, and you’ll see what I mean.

Like all communication patterns, it’s worth your time to have an open discussion with your tech lead on their preferences. Do they hate Slack? How many status updates per day is too many? Did your communication over the past week benefit the team or not?

### 3. During technical discussions, repeat and summarize

It’s important that you and your tech lead have at least some alignment around the technical decisions you’re making. Your opportunity for making this alignment happen is technical conversations.

Technical conversations might look like your tech lead sitting down with you to kick off a new project. Your tech lead has some initial thoughts on how it could be implemented, and they’re sharing them with you.

Often, your tech lead might have more historical context than you on the system that’s changing. So they’ll probably say at least one thing that makes you go “huh?”

Your tech lead knows this. But they don’t know which things they’re saying are going to make you go “huh?” unless you actually say “huh?”

Always clarify both what you **do** and **don’t** find confusing. Rather than saying “I’m lost,” clarify “I understand X, but I don’t understand Y.”

Ultimately, you want your tech lead to walk away from the conversation with a lot of confidence that you heard and understood what they had to say. A lot of people try to achieve this by smiling and nodding. That has the opposite effect.

Instead of smiling and nodding when you understand, **repeat and summarize** what you heard.

For example:

> “Got it. What I’m hearing is, I should calculate this value on the server to reduce roundtrips, and send it down to the client during page load.”

This pretty much proves to your tech lead that you were listening to them. And it actually forces you to listen better.

When trying this out, you’re going to resist at first. It kind of feels like you’re being bossy and interruptive. It also kind of feels like you’re just patronizingly copying what they say.

Don’t let that stop you. Think about how the tech lead will feel. I can tell you that it’s a real relief to see the other person take the initiative to repeat and summarize.

These summaries are usually action items. Your next step should be to write them down somewhere. Put them somewhere that your tech lead can see them and provide corrections if you’re wrong.

### Be a super collaborator

Tech leads want to work with engineers who take responsibility. This can be hard to do on a technical level if you’re not familiar with the systems that you’re working with.

But what you **can** take responsibility for is how you **communicate** about your work. Think about how you can shift your communication patterns with your tech lead, and you’ll easily discover powerful new habits to build.

#### If you’re passionate about helping teams collaborate effectively, you should [work with me at Asana](https://asana.com/jobs/engineering?utm_source=medium&utm_medium=blog&utm_content=talk-to-tech-lead).

