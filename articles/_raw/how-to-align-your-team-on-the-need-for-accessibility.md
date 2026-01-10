---
title: How to get your team on board with accessibility
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T21:40:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-align-your-team-on-the-need-for-accessibility
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/keyboard-1.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: presentation
  slug: presentation
- name: progressive web app
  slug: progressive-web-app
- name: teamwork
  slug: teamwork
seo_title: null
seo_desc: 'By James Y Rauhut

  We all learn about web accessibility at different points in our career. That means
  a lot of time you are not on the same page as your teammates. I had the privilege
  a couple of months ago to speak at Pingboard about accessibility. O...'
---

By James Y Rauhut

We all learn about web accessibility at different points in our career. That means a lot of time you are not on the same page as your teammates. I had the privilege a couple of months ago to speak at [Pingboard](http://pingboard.com/) about accessibility. Our goal was to get the whole team at the same knowledge starting point. If we all have a basic understanding of whom web accessibility affects and how it affects them, we can ship better experiences.

You probably find yourself in the same opportunity at your company to present on accessibility. So I would like to do two things to help: I am going to [give you my presentation](https://drive.google.com/file/d/1W62aya8uk0LgMPyMUBSIAJVOQBewmiKd/view?usp=sharing) as a starting point and walk you through the points I like to touch on.

> You probably find yourself in the same opportunity at your company to present on accessibility. …I am going to [give you my presentation](https://drive.google.com/file/d/1W62aya8uk0LgMPyMUBSIAJVOQBewmiKd/view?usp=sharing) as a starting point and walk you through the points I like to touch on.

# **Remind the team that you are talking about real people.**

When we read accessibility documentation, it is easy to forget the human element. It makes sense because you are reading technical docs meant to influence code. It is great to start with this shared definition:

**_A person with a disability:_** _A person who has a physical or mental impairment that substantially limits one or more major life activity._

We use this to establish friendly dialog. People do not want to be called “disabled”. They want to be called their name. We also need to clarify how wide of a range disabilities can be. Try expanding past assumptions early on with these points:

* Some disabilities come at birth, some come later.
* Some disabilities are permanent, some are temporary.
* Some disabilities always affect, some come and go.
* Some disabilities are visible, some are invisible.

# **Go over some disability categories with emotional experiences and quick tips.**

Now that we have established that we are talking about people, it is time to talk about their experiences. I like to mix this section with quick tips for common disability categories. Remind your audience that there are way more disabilities than you are covering. They are difficult to categorize, which is why the technical documentation focuses on the solutions.

Something you will notice about the presentation is that there is a lot of video and audio. I find it more effective to have those with disabilities speak more than me about the issue. The multimedia in the presentation makes it possible for those people to not even have to be there.

### Visual

%[https://www.youtube.com/watch?v=UzffnbBex6c]

I love to share this video of Tommy Edison using a screenreader because he keeps things lighthearted, but also goes through the whole process of sending an email. After the video, you can point out that fellow Mac users can try their screenreader with `CMD + F5` at anytime.

Quick tips:

* People with dyslexia prefer to override font settings.
* People with low vision need to be able to zoom correctly.
* People with color blindness need an overall color contrast ratio of 4.5:1. Text 19px or larger can have a ratio of 3:1.
* People with color blindness need labels and patterns for differentiations.

### Auditory and Seizure

Auditory disabilities are easier to talk about with digital product teams. Remind your team that all audio should be paired with visual cues and captions. Encourage the team to do content audits to check all videos for closed captioning.

Strobing, flickering, and flashing can trigger seizures. Other triggers include animations longer than 250ms, parallax, and images moving under text.

### Motor

%[https://youtu.be/yx7hdQqf8lE?t=253]

There are two demos I like to show teammates when it comes to motor disabilities. The first is hidden inside a longer video. A fellow named Gordin Richins shows what it is like to use a mouth stick. It is an older video, but I try to point out that new technologies can be more expensive.

The second video is a wholesome video of an eye tracking product. These are great because they can provide mouse capabilities to those with motor disabilities. However, we should still make all experiences keyboard accessible to be safe.

%[https://www.youtube.com/watch?v=FEQv7buTNxw]

### Cognitive

Cognitive disabilities can be difficult to convey. For this last category, I stuck with quick tips to keep the presentation alternative between facts and emotion. Here are the quick tips I share:

* For memory, keep processes short and remind users of context as much as possible.
* For problem-solving, error messages should be as explanatory as possible.
* For attention, use visual cues to highlight the most important points or sections of content.
* For reading, linguistic, and verbal comprehension, provide supplemental media that helps processes.

# **Emphasize how common disabilities actually are.**

Did you know that one out of five people in the US have at least a one disability? ([source](https://www.census.gov/newsroom/releases/archives/miscellaneous/cb12-134.html)) It may not seem like that in the workplace, but we should consider why. This is the point of the presentation when people should understand invisible disabilities. Invisible disabilities can be hidden from the naked eye. Here is a great interview where Carly Medosch talks about working with an invisible disability:

[**NPR: People with 'Invisible Disabilities' Fight for Understanding**](https://www.npr.org/2015/03/08/391517412/people-with-invisible-disabilities-fight-for-understanding)

This story is a great transition to a big question: What can we as enterprise software teams do to help those with disabilities?

Well, 79% of people of a working age in the US have employment. Only 41% of people of a working age in the US that have disabilities have employment. ([source](https://www.census.gov/newsroom/releases/archives/miscellaneous/cb12-134.html)) If more jobs were accessible, that gap would close. This means that we as enterprise software teams can make it our mission to close the gap!

# **End with the legal risk for those that need extrinsic motivation.**

It may not feel great, but some people may still need more reasoning about why the team should work towards accessible experiences. This is why I like to close the presentation on the legal implications of accessibility.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-13-at-3.45.32-PM.png)
_ADA Title 3 lawsuits in federal court: 2722 in 2013, 4436 in 2014, 4789 in 2015, 6601 in 2016, 7663 in 2017, 10163 in 2018. https://www.adatitleiii.com/2019/01/number-of-ada-title-iii-lawsuits-filed-in-2018-tops-10000/_

In 1990, the Americans with Disabilities Act was signed. This provides those with disabilities the same protection that’s given in the Civil Rights Act of 1964. Section 508 says digital experiences in government departments and agencies have accessibility requirements.

Lawsuits continue to grow saying that the ADA also covers digital experiences from any company. Over 10,000 lawsuits were filed in 2018 alone. In fact, one of those [cases is headed towards supreme court](https://www.cnbc.com/2019/07/25/dominos-asks-supreme-court-to-say-disability-protections-dont-apply-online.html).

# Be a part of the good fight.

Are you considering presenting to your team on web accessibility? You really should. You don’t have to be an expert and it’s okay if not everyone listens to you. Every effort to make the web a more friendly place is worth it.

I hope these resources helped you shape a future presentation. Please steal everything from me (but keep the citations).

If you appreciate this, please consider voting for my SXSW talk idea. I want to teach product managers, designers, and everyone else about progressive web apps. The cool thing about PWAs, is that a lot of accessibility criteria is baked in! If you wanna learn more, check out the video below.

[Please take minute to vote for my talk and share it with others.](https://panelpicker.sxsw.com/vote/95517)

%[https://www.youtube.com/watch?v=aRwfB7Iiaqo]

Got any other good resources for accessibility presentations? Please share them in the comments or tweet me them at [@seejamescode](http://twitter.com/seejamescode). I will retweet the best ones!

