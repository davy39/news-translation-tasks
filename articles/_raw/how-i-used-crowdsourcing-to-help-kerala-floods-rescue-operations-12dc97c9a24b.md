---
title: How I used crowdsourcing to help Kerala floods rescue operations.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-04T19:05:43.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-crowdsourcing-to-help-kerala-floods-rescue-operations-12dc97c9a24b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wWP9CgjPGVglqTU2Arh3Tw.jpeg
tags:
- name: crowdsourcing
  slug: crowdsourcing
- name: Disaster Response
  slug: disaster-response
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Arnav Bansal

  Overnight, I made a website that let people discover urgent requests


  In August 2018, floods decimated the state of Kerala. One-sixth of its population
  was directly affected. The state incurred property damage worth $3B.

  I’m Arnav, an...'
---

By Arnav Bansal

#### Overnight, I made a website that let people discover urgent requests

![Image](https://cdn-media-1.freecodecamp.org/images/RTrVKBeZKPcQc5wSd9JCvUgKBNGrPVSM2yut)

In August 2018, [floods](https://youtu.be/hzDDYwwDJ1E?t=23s) decimated the state of Kerala. One-sixth of its population was directly affected. The state incurred property damage worth $3B.

I’m [Arnav](https://twitter.com/itsarnavb), an 18-year-old from Bangalore who finished school this March. As the floods were happening, I came across the [Kerala Rescue Project](https://github.com/IEEEKeralaSection/rescuekerala/). This was a movement of volunteer developers solving tech challenges associated with the Kerala Floods using the web.

The [website](https://keralarescue.in) provided important services. It collected help requests from victims. It helped volunteers and rescuers locate them, and find relief camps. It provided visualizations for disaster response forces.

As I explored the project on GitHub and Slack, I found a specific problem I felt I could solve.

### Too many requests

Following a massive once-in-100-years flood, there were a large number of requests for help.

I watched new requests arrive every time I refreshed an API endpoint on the rescue website. When I first discovered it, I spent nearly half an hour just reading through people’s requests.

They were distressing. Requests about old people, sick and injured people, pregnant women, and infants. Some reporting buildings on the verge of collapse or flood waters rising. Some were from people living elsewhere, unable to reach relatives in Kerala.

**But the distressing ones were amidst a sea of requests that didn’t seem to be immediate or had little data.**

And those were just the ones in English. I couldn’t read requests written in Malayalam (the language of Kerala).

That led me to wonder: how were requests being prioritized? I asked around. Sure enough, people remarked that this was a real issue.

### Making sense of the data

I thought of two approaches to figuring out the urgency of requests.

#### Natural Language Processing (NLP)

Words like ‘Urgent’, ‘Infant’, ‘Pregnant’, or ‘Trapped’ indicated urgency, and could be used to classify requests.

But the data had several problems: requests were in English and Malayalam. And sometimes, Malayalam was written with in the English alphabet.

Many were written in a hurry.

Some suggested translating requests to English first, before applying NLP. But translation is lossy, and I was certain that this wouldn’t work.

And finally, I felt that urgency was largely contextual. Would NLP handle it well? Existing sentiment analysis can tell you if the text is positive, negative, happy or sad. But it doesn’t measure urgency.

And there wasn’t time to develop a new model. Especially, given the language problem.

#### Crowdsourcing

I was certain that people would volunteer some time to identify urgent requests.

They’d make sense of information suggesting urgency that computers aren’t good at.

I imagined a website that’d fetch and show requests from the rescue website. Volunteers would rate urgency on a scale that went from _not urgent_ to _critical (_values 0 to 3), with an option for spam (–1). They could skip requests if they didn’t know the language.

So I got to work.

### Implementation

I first thought about building the crowdsourcing feature into keralarescue.in

The project was open source. Many were building separate-but-linked tools into the same platform. It made sense for me to build right into it.

But I had some worries:

1. I wasn’t certain whether the idea would work. I didn’t want to leave dead-weight on the platform that many depended upon.
2. The platform was written in Django, using PostgreSQL. I’ve little familiarity with those, and I didn’t want to experiment-learn.
3. The review system would get in the way of iterating quick.

So I decided to create my tool independent of the main platform.

If it worked, I’d get them to merge my data. If it failed? Eh.

#### Midnight oil

It was already around 1 AM. I set a goal to have my site up within five hours, so it’d be ready when people woke up.

My idea was to use the API endpoint from keralarescue.in to display help requests. Of course, I cached it at my end, so as not to burden the main website.

I began developing the platform. I started by creating data models. Then, I worked on functions and API endpoints. Finally, I started work on the front end. My stack included Firebase and VueJS, for quick prototyping reasons.

I planned to use [Wilson confidence intervals](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval) to evaluate scores. (Used for the [confidence sort on Reddit](https://medium.com/hacking-and-gonzo/how-reddit-ranking-algorithms-work-ef111e33d0d9)) They’re an improvement over simple averages, as they account for the number of ratings.

But I was in a hurry, so I decided to implement this later. Without data, this wasn’t of much use.

‘Simplicity’ is a cliche. But I found that it works. Things seemed to improve when I cut out complexity. I wrote simple data models. I dropped reCAPTCHA and authentication, making the assumption that I wouldn’t attract malicious users.

By around 8 AM, my prototype was ready. And I was ready to drop asleep. I posted a link on GitHub, and went to bed just as the first pageview rolled in on Google Analytics.

I had no trouble falling asleep.

### Getting people on board

I had users.

When I woke at noon, I checked analytics before anything else. ~30 visits. And I had two users currently online. From the state of Kerala. _Woah_.

The feedback was positive. And I’d gathered quite a bit of data. I continued to improve my platform over the day.

* **I dropped the spam option.** I learnt that people weren’t sure which requests were spam. Many were missing information. Those could be completely valid requests from people in a hurry, or people who weren’t good with tech.
* **I implemented the Wilson score.** I created an API endpoint that returned the confidence value between 0 and 1 based on all user ratings collected so far. The idea was to get keralarescue.in to use this endpoint to update its dataset periodically. The value could be used to sort, and find the most urgent requests
* **I added a page to display urgent requests.** I wanted to make this tool useful as soon as possible.

At about 4 PM, I decided to announce it on Slack and Github.

This turned out to be an inflection point, and for the next few hours, the site had 20–30 users online. They were from all over India, and also the US. The users from Kerala continued to work late into the night, sorting requests at 2 AM.

I noticed that people were slower at rating requests than I’d anticipated.

The next evening, I would learn why.

#### The triage group

By the next day, I’d finished most dev work. Lots of people started contacting me. They liked my project — especially the simple interface.

In the evening, I received a DM on Twitter from someone named Nishanth, asking if my website could be used to **triage** requests. We got on a call, and I described how crowds could help determine the urgency of requests.

He added me to a hundred-member group on WhatsApp. It turns out, these great folks had been using my website in a completely different way.

They were actively calling up requesters, and getting updates on their situation. They were rating urgency based not on the text content, but from **actually conversing with affected people**. _WOAH._

I realized that my database contained more valuable information than I’d thought. We were directly helping volunteers reach victims. Messages thanking me for my work were rolling into my phone.

### Losing the data source

Back in the main project, people were gearing up for a big event. The government of Kerala was going to announce the rescue website publicly. Heavy traffic was to be expected.

The main website was providing a lot of functionality. Heat maps of requests, donations, relief camps, volunteer coordination, announcements, you get the gist.

I’ve developed serious respect for the dev-ops team, because as the traffic hit the site, they worked overnight to scale it.

All seemed to be working, except for one thing: **they took down the API endpoint I was dependent upon.**

Now, I knew that the endpoint I was using was not going to scale. It returned all requests at once. Towards the end of its life, it was returning a 10 MB dataset. It was made for development, and not production use.

Fortunately, my site already had a caching mechanism, so it remained operational.

I got into contact with the team. They were building an alternative. But they had lots left to build, so I tried not to push.

My site continued to run without issue, and the triage groups (there were multiple by this point) continued to operate, albeit without new data.

### New features?

At this point, I started thinking about ways to improve.

The immediate problem was the influx of large amounts of new data when the alternative route became available. And what other improvements could I make?

I thought through some features.

* **Cohorts based on time**: Assign a certain percentage of users to handle the newest requests exclusively. Likewise, assign users to sections of older requests.
* [**Bloom filters**](https://www.jasondavies.com/bloomfilter/)**:** They are a space efficient way to test set membership. I could use bloom filters for so many things: ensure we exhausted all requests, and limit repeat visits.
* **Status updates**: I could build a feature for people to update the status of requests. It was a trivial build, and people were asking for it. But people working on the main platform told me that they were building one already.
* **Websockets:** I could stream new requests to the website in real time as they arrived. Combined with status updates and time cohorts, we’d get detailed information about requests as soon as they arrived.

I had a lot of competing ideas, and I wasn’t sure what could be implemented in time to be useful.

### Wrap-up

The API endpoint returned the next day. It was paginated now, returning 300 requests at a time. I quickly wrote a script to download and maintain a local cache using the new API.

The number of calls and messages I was receiving reached a new high. Having never been employed before, this was new terrain. Devs working on the main platform were contacting me. They were working on integrating the crowdsourced data — both the urgency ratings, and the status updates that we were collecting.

As the day ended, the folks on the triage groups felt a shift.

Most victims they were calling reported being rescued recently. It turns out, the rescue missions on the ground had kicked in.

This was great news. At about 5 AM, I got on a call with Nishanth. He was in touch with government officials overseeing rescue operations. We packaged data from the website and spreadsheets, and handed it over.

As I write this, flood victims have been rescued and transported to relief camps. There are new challenges involving logistics between camps and aid arriving from around the country.

### Lessons

* **Simplicity**: Many people messaged me that they liked my site. I’m no designer, but my decision to keep UX simple helped people get on board quicker.
* **Computing is cheap:** All of this was hosted on Google Cloud Platform. It cost me less than a dollar, covered within my free tier credits. If I had known how cheap it would be, I’d have built an application heavy on the backend.
* **Pivoting**: I wish I’d completely pivoted to a detailed triage platform. The volunteers came up with a makeshift solution, but in hindsight, I would rather have shipped the platform with those features.
* **Networks are important**: People wanted to help. The initial group of 30 grew over two days to a group of 230, as people called upon their friends and acquaintances. Folks joined in from Kerala, the rest of India, and from around the world.

I’ve met many amazing people. I’ve learnt a lot, technical and otherwise. Through all this, the most incredible feeling was that of being on the same page as thousands of other people.

If my work merits an article, the project I was a part of deserves a book.

As for me, I’m getting in contact with people involved in disaster response to learn from their experience and expertise.

A bit more about me: I’m on a gap year to delve into crypto economics. I picked up web development skills back in 10th grade, while hosting a hackathon at school.

I’m considering developing a project based on this, but with many other insights that my friends and I have had since.

* _Ann Thomas, a volunteer from the triage groups, wrote about her experience [here](https://mommysuitup.blogspot.com/2018/08/my-tryst-with-triage.html)_
* _Thanks to Dr. Harikrishnan, Dr. Nishanth, Ajit Chandran, Prasad Pillai, who helped organize the triage groups_

