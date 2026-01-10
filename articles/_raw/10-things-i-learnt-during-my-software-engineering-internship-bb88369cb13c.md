---
title: What I learned during my software engineering internship
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T03:21:01.000Z'
originalURL: https://freecodecamp.org/news/10-things-i-learnt-during-my-software-engineering-internship-bb88369cb13c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ixrHjysR8zRWlp9gBvroYQ.jpeg
tags:
- name: internships
  slug: internships
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Carmen Chung

  As part of my coding bootcamp at Coder Academy, I was placed as a software engineering
  intern at Valiant Finance, winner of the Australian Fintech Start Up of the Year
  (2017) Award. In the four weeks I have been here, I have made more...'
---

By Carmen Chung

As part of my coding bootcamp at [Coder Academy](https://coderacademy.edu.au/), I was placed as a software engineering intern at [Valiant Finance](https://valiant.finance/), winner of the Australian [Fintech](http://fintechawards.net/) Start Up of the Year (2017) Award. In the four weeks I have been here, I have made more intellectual discoveries than I can count: all thanks to the incredible mentorship and patience of the team I have been working with.

Here are the top 10 things I learned during my internship, divided into technical and non-technical lessons.

### TECHNICAL

#### **Be meticulous**

Having been a corporate lawyer for seven years, I have always prided myself on attention to detail. But mistakes do happen.

In the third week of my internship, I hit Ctrl + F to find a word I was searching for in my file. Then I must have accidentally hit the space bar, deleting the word entirely.

To my mortification, I didn’t notice that I had done this . It was something that would not have thrown an obvious error — otherwise our tests would have picked it up. Rather, it would have gone unnoticed and “failed silently”…if it hadn’t been for the sharp eyes of our Co-Founder, Ritchie.

To avoid making my mistake, check out GitHub Desktop. It displays all the changes you’ve made to a file, and allows you to comb through line-by-line, one final time before committing. It’s easy to skip through this part. But taking the time to review your changes one last time **before you commit / push** can save you serious heart-ache — and embarrassment — at a later stage.

![Image](https://cdn-media-1.freecodecamp.org/images/GvfEtzAo27YBQbS5jspK6k9qyUOsEApsqe1n)
_Don’t be Velma!_

I can’t stress enough how important **attention to detail is**. One missing semi-colon in some languages can stop your code dead in its tracks. Other things are less insidious, but still annoying.

Even simple things like checking your company’s Git commits to see how they write them — for example, we use a specified emoticon to indicate what the commit is, capitalize the first word in the commit, use present tense, and don’t add punctuation to the end — saves you from irritating your colleagues when you stray from the path of consistency.

#### **Take notes (and study hard)**

Forget the Fountain of Knowledge.

Almost every day that I’ve been at Valiant Finance, I’ve felt like I’m drinking from a fire hose. The amount of sheer knowledge and wisdom that comes spouting out from the mouths of our Head of Engineering ([Kris Hofer](https://twitter.com/krishofer)) and our Co-Founder ([Ritchie Cotton](https://twitter.com/ritchie__c)) is enough to make anyone’s head swim. Much to my relief, these two guys are very well-structured and patient in the way they teach, so everything clicks neatly into place.

They click faster, though, if you take notes.

I have an organized notebook with headings and a Table of Contents page to help me keep track of everything I’ve learned. Bits of code that I use repeatedly are highlighted, and I have brass tabs for sections that I use frequently.

![Image](https://cdn-media-1.freecodecamp.org/images/OKEnsvJjZ4ktK7HNBURVSXJyADkEjTADEY5E)

On top of this, I have a Weekly Planner where I jot down all the tasks that we need to tackle every day, and a non-lined notebook for drawing out flowcharts — for more complicated programming logic — and wireframes.

Most importantly, I write a list of all the things that Ritchie and Kris mention that I know I will need to do more research into on my own time.

![Image](https://cdn-media-1.freecodecamp.org/images/EN6SMceBtwLodxTu8aqoch-5YzNJdTawTbiz)

#### **Don’t reinvent the wheel**

One of the things I discovered was that Ritchie had set up an incredible CSS system, with his own fully-customized stylesheets (using the [BEM method](http://getbem.com/introduction/)) — and a style guide that would make any documentation-aficionado’s heart sing.

Before I became familiar with the system, I was tempted to create certain CSS classes that I figured would be easy for me to access and apply. What I came to realize and respect was that there was basically no need for me to do so. In almost every case there was already a set of clear and flexible styles that I could switch in and out — like interchangeable Lego pieces — all at my fingertips. By creating unnecessary styling classes, I would be cluttering up a structured and clean system, making it harder for people to navigate at a later stage.

![Image](https://cdn-media-1.freecodecamp.org/images/1KtLKQWsMC21g-NpM5f4zVqAvxpvNNWnbTbh)
_If you have great Lego blocks, don’t remake them. Focus instead on making things with them._

#### **Avoid verbosity**

One of the key principles of Ruby on Rails is DRY (Don’t Repeat Yourself). It’s something that has been drilled into junior Rails developers from day one…but oh, how the struggle is real.

My fellow intern and I were tasked with creating code that would count the number of people a user had referred to the platform. For every three referrals, the user would receive $50. The logic was manageable, but what we discovered was that we had to account for one **friend** vs. **many friends** when displaying the result.

This was how our code initially came out:

```
- if @invite_count == 1
 %p
 You have invited 1 friend to be part of Valiant Finance.
 — if @invite_count > 1
 %p
 You have invited
 %strong #{@invite_count} friends
 to be part of Valiant Finance!
 
- if (@invite_count % 3) == 0 || (@invite_count % 3) == 1
 %p
 Invite another
 %strong #{3 — (@invite_count % 3)} friends
 to receive $50!
 — if (@invite_count % 3) == 2
 %p
 Invite another
 %strong friend
 to receive $50!
```

When I showed Ritchie, he told us to look into [pluralize](https://apidock.com/rails/ActionView/Helpers/TextHelper/pluralize).

Mind.   
Blown.

This was how our code came out afterwards:

```
%p You have invited #{@invite_count} #{“friend”.pluralize(@invite_count)} to be part of Valiant Finance.
 %p
 Invite another
 %strong #{3 — (@invite_count % 3)} #{“friend”.pluralize(3 — (@invite_count % 3))}
 to receive $50!
 %p
```

#### **Be aware of your programming language’s intricacies**

A number of junior web developers use certain terms interchangeably without being aware that there are — sometimes minute, sometimes not so minute! — differences between them. I’m guilty of frequently Googling the differences between `.present?`, `.exists?`, and `.any?`; and `.empty?`, `.nil?`, and `.blank?.` Made all the more cringe-worthy because `.exists?` has [actually been deprecated](https://apidock.com/rails/ActiveRecord/Base/exists%3F/class). Oops.

![Image](https://cdn-media-1.freecodecamp.org/images/fMyJ-tJVWuLl263uB8Njy7GGPo-wqOq4uInh)
_Looks like I’m not the only one who forgets this._

Sometimes the intricacies are almost unnoticeable — in the first week of my internship, I was typing `Product.all.map(&:name)`. But I was later taught that I could instead just use `Product.pluck(:name).` There **is** a difference between the two in terms of efficiency — both with respect to me actually typing it out, and in terms of search speed. For more info, take a look at this [article](https://rubyinrails.com/2014/06/05/rails-pluck-vs-select-map-collect/).

Try to figure out the various ways things can be done in your programming language — and if there is more than one way, see if you can learn the differences between them.

**Top Tip**: Asking the differences between certain functions/methods/queries is also a favorite pass time of technical interviewers, so study up.

### NON-TECHNICAL

#### **Get involved in the company**

Sounds simple, right? But when you’re juggling a lot of tasks and trying to get yourself oriented at a new company, it’s easy to forget the little things that matter to the people around you.

On our first day at the company, the other intern and I were encouraged to sign up for Twitter. On the train to work the next morning, I dutifully set up an account, and followed our company’s account, plus the accounts of a few colleagues.

Given that I already have multiple social media accounts, I was initially reluctant to add another to the mix. But it has turned out to be really beneficial.

I’ve been able to keep up-to-date on the company’s news plus the news of key partners, as well as check out interesting tweets from my colleagues. I have been tweeting posts about company events and new product features that our team has been working on. It’s an easy way to get involved, and shows that you actually care about where you work.

![Image](https://cdn-media-1.freecodecamp.org/images/mwVLN-X2SDvnji3xpv3z8EpxYtiWSR64kHPz)
_The Valiant Finance pride competing in our in-house Winter Olympics competition._

#### **Ask questions — but more importantly, listen**

Kris, our Head of Engineering, very kindly told us that “there are no stupid questions,” and that we are encouraged to ask whatever comes to mind.

I, on the other hand, firmly believe there is such thing as a stupid question. Usually those occur when you just haven’t been paying attention, or when you’re too lazy to think for yourself about what has been said. Asking questions is important, particularly when you genuinely don’t understand something. But listening to answers is even more so.

Take the time to listen to what is being said, and think about it. It’s human nature to hear the words coming out of someone else’s mouth, and start mentally preparing a response while they’re talking. Don’t do it. **Pay attention to what you’re being told.**

![Image](https://cdn-media-1.freecodecamp.org/images/bmtPk9Pbivm-7qSGtuQdaDQL9ccnsPumPvvm)
_Don’t be this little guy (unless you’re really, really cute)_

#### **Know whom to talk to**

One of the great things about this internship was that we were encouraged to reach out to members of other teams to discuss what product features they wanted, and how we could implement them. We learned to defer to their expertise in some respects, and to the judgement of our Product team in others.

For example, we were tasked with building the tabs on the broker dashboard so that the leads that have been submitted by a broker are neatly divided into Active, Inactive, and Settled. In addition, we created a referral link card — as mentioned earlier.

Both of these tasks required liaising with the Head of Third Party Partnerships so that the functionality and language of the feature was suitable for the broker audience.

![Image](https://cdn-media-1.freecodecamp.org/images/v-bU8hOaVzLyGgSnS833fOm42Pmq83VYI8Xj)
_We worked with the Head of Third Party Partnerships to produce the responsive dashboard tabs, and Refer a Broker feature_

Having said that, there were times where we were trying to build something that attracted a great deal of interest from a number of people in the company — resulting in (sometimes conflicting) input. At times like these, we would defer to our Product team leaders, who would give us guidance — and equally importantly — step in as a buffer if the noise from other teams got too loud.

Don’t be afraid to ask your supervisors for assistance in these cases — they are usually better equipped and more experienced to tell other teams that what they are asking for is u̶t̶t̶e̶r̶l̶y̶ ̶r̶i̶d̶i̶c̶u̶l̶o̶u̶s̶ going to take a while longer than expected to implement and that because it is u̶t̶t̶e̶r̶l̶y̶ ̶r̶i̶d̶i̶c̶u̶l̶o̶u̶s̶ not business critical, it will be added to the u̶t̶t̶e̶r̶l̶y̶ ̶r̶i̶d̶i̶c̶u̶l̶o̶u̶s̶ ̶l̶i̶s̶t̶ developer log list of things to do.

#### **Stay humble**

Because there are so many ways to skin a cat in the dev world, it’s easy to get caught up in a particular way of doing things, and assume that your way is better than everyone else’s way.

Don’t get me wrong — there are best practices, and there are, no doubt, good rules that each company follows in order to ensure code consistency. But don’t dismiss what others have done just because it doesn’t conform to what you’re used to. It may (or may not) be even better than your code.

![Image](https://cdn-media-1.freecodecamp.org/images/lTZTI-yEgrBVvADz7t0hRPwJqNCY6UO2jFos)
_Don’t be this guy either (unless you’re joking around)_

On that note: when you have messed up, know that it’s time to eat some humble pie.

Own up to it, apologize, learn from the mistake, and try not to let it eat at you. The last part is the hardest for me. I had nightmares for a week after the deletion mistake mentioned in the beginning.

#### **Have fun**

At Valiant Finance, we celebrate wins. We have an entire Slack channel dedicated to cheering each other on in both our professional and personal endeavors.

We do team building activities, we have soft toys and dogs in the office, and we do casual Friday night drinks.

![Image](https://cdn-media-1.freecodecamp.org/images/eC7CQ2oLtetN05tbXWDARyzdjAdEm4xn-ZPO)
_The welcome care package we were given on our first day of the internship_

It seems obvious, but people want to work around happy people. While you’re not there to make drinking buddies at your internship company (bonus points if you do though!), you want to enjoy your time there — and the company should want you to as well. The whole point of the internship is to try to see if you are a good fit for the company — and vice versa.

Try to enjoy yourself during the internship — but if what you’re working on is tedious and mundane, try to make a game out of it. I’m a seasoned connoisseur at making boring work seem fun — perhaps something I’ll dive into further in another post.

If you’re unhappy as an intern, chances are, you’ll be unhappy as a full-time employee.

And no one wants that.

Big shout out goes to Co-Founder Ritchie Cotton and Head of Engineering Kris Hofer and for their incredible patience, mentorship and knowledge throughout my internship at Valiant Finance. I never imagined learning so much in such a short period of time — or having so much fun doing it. Thank you guys.

Follow me on [Twitter](https://twitter.com/carmenhchung).

