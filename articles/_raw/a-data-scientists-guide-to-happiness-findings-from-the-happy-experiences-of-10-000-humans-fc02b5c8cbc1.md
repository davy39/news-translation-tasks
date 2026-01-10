---
title: 'A Data Scientist’s Guide to Happiness: Findings From the Happy Experiences
  of 10,000+ Humans'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T22:53:44.000Z'
originalURL: https://freecodecamp.org/news/a-data-scientists-guide-to-happiness-findings-from-the-happy-experiences-of-10-000-humans-fc02b5c8cbc1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*EsFDmp-QfBLa0vBf.png
tags:
- name: Data Science
  slug: data-science
- name: Happiness
  slug: happiness
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: topic modeling
  slug: topic-modeling
seo_title: null
seo_desc: 'By Jordan Rohrlich

  Modern life throws a lot at us. We often find ourself struggling to manage anxiety,
  wrangle responsibilities, adapt to new conditions, and maintain a happy state of
  mind.

  But happiness is a noisy space these days. Self help books, ...'
---

By Jordan Rohrlich

Modern life throws a lot at us. We often find ourself struggling to manage anxiety, wrangle responsibilities, adapt to new conditions, and maintain a happy state of mind.

But happiness is a noisy space these days. Self help books, articles, blogs, and meditation apps can’t help everyone, and often increase the mental burden needed to stay content. That’s a serious problem. So, as mental health becomes increasingly vulnerable and solutions become increasingly complex, it’s important to anchor oneself to the fundamentals. **That is, we need to refocus our daily lives on the everyday things that make people happy.**

### Data

This research dives into a handy dataset that can help shed some light on the fundamentals of happiness. [HappyDB](https://github.com/rit-public/HappyDB) is a set of 100,000+ happy experiences gathered through Amazon Mechanical Turk from March to June of 2017. It contains the experiences and demographics from tens of thousands of contributors around the world. Interestingly, some basic text analysis methods can help us learn a lot from this data.

By understanding the emotional intensity and keyword patterns drawn from these happy experiences, HappyDB teaches us two valuable lessons.

You can check out the code for yourself on [GitHub](https://github.com/jrohrlich/DSGuideToHappy).

### 1. Happiness is not conditional on demographics.

This one is counterintuitive.

Most of us experience a “grass is always greener” effect with respect to happiness. Young people anticipate a happy career and family later on in life. Older folks reminisce about a time when they were young and adventurous. Bachelors yearn for companionship. Couples hope for children.

And, despite knowing this, we all think someone else is happier, or some other stage of our life will bring us more joy. Let’s take a look at the data.

[Sentiment analysis](https://web.stanford.edu/class/cs124/lec/sentiment.pdf) weighs the emotional intensity of text. Using an R package called “Syuzhet,” I measured the sentiment of these happy experiences to determine how their intensities vary. This created a spectrum of happy experiences that could be broken down by specific demographic groups:

![Image](https://cdn-media-1.freecodecamp.org/images/vtSR9KdR4zPHMmWcHn7v1MPvZ640dX8VRe6M)
_Sentiment of Happy Experiences (by gender, family status)_

![Image](https://cdn-media-1.freecodecamp.org/images/dBKgVGpc2rWvemRIUZryNLznFVUVlxWVRHuK)
_Sentiment of Happy Experiences (by age group)_

Somewhat surprisingly, there’s little change in the spread of happy experiences across these gender, family, and age demographic groups. Here are the highlights:

* Overall, the experiences are definitely positive. But the bottom quartile does have negative sentiment (some happy things poetically arise from discomfort and tragedy)
* The distributions have high-end tails and fairly limited lower bounds — some experiences are extremely positive, and few are strikingly negative
* Self-identifying females have slightly higher sentiment scores than men for most of their experiences (a 0.05–0.1 point difference)
* Married parents have slightly higher sentiment scores than bachelors and childless couples for most of their experiences (a 0.05–0.1 point difference)
* The quartiles of happy experiences (25th, 50th, and 75th percentiles) across age groups are virtually identical

**In sum,** **there is no significant difference in the range of happy experiences reported by different demographics.** Although women and parents tend to have marginally more happy experiences to record, the differences on the sentiment scale can’t be taken seriously — they correspond to a fraction of a fraction of a single happy word per experience recorded. That’s a minuscule difference.

This dataset, however, does not include any data fields for race, socioeconomic status, or other identity positions that may materially influence daily experiences. Future happiness research should inspect these relationships closely.

### 2. Happiness is determined by specific types of experiences.

It’s easy to think of happiness as a mysterious, ethereal substance that penetrates our experiences in uninterpretable ways. This view espouses a metaphysical understanding of happiness as something beyond human comprehension.

But that’s not very helpful, especially for people who rely on happy and meaningful experiences as the lifeline of their mental health.

Enter Topic Modeling. This method of text analysis (explained [here](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/); I use R’s “Mallet” package) provides a constructive approach to explaining what HappyDB’s 10,000+ participants find to be happy experiences.

By segmenting the dataset into documents of each respondent’s experiences, then running an LDA topic model to identify groups of commonly occurring keywords, we can begin to isolate distinct types of experiences that bring us happiness. The topics and related keywords can be seen below, in no particular order:

![Image](https://cdn-media-1.freecodecamp.org/images/bSlgdQrleybiwhVeNzAzevuLqtRXteuIFEpQ)
_Topic Model Output from 100,922 Happy Experiences_

#### **Time with Family**

Seems like a no-brainer. Words like “daughter,” “son,” “husband,” “baby,” “wife,” and “time” seem to show that lots of people reflect very positively on experiences that involve their loved ones. These experiences often involve the most commonplace of settings and derive happiness simply from company and affection.

Try spending more time with loved ones: call your mom, go to your kid’s soccer game. It may pay off more than you think.

#### **Getting Paid**

Although people don’t like thinking that money relates to happiness, their experiences sure say the opposite. Getting a paycheck, clearing a credit card balance, or giving money to a friend can make people really happy. And the sense of accomplishment and economic security that comes with would definitely explain why.

#### **Food**

People love eating. Cooking a favorite meal, eating out with friends, or gorging on a pint of iced cream in front of the TV can all make someone happy. Good food with friends should definitely play a part in any happy lifestyle.

#### **Sleep Time**

Surprisingly, people document lots of happy experiences around sleep: cuddling up in bed, going to sleep with a furry friend, waking up to a promising new day, and so on. There’s lots to be happy about, if one takes a moment to reflect at night after a productive day, or in the motivated morning before something exciting.

#### **Games and Competition**

Humans are competitive. They love playing video games, watching sports, and doing other things that stoke their biological instinct to dominate. Play a board game with some friends or get excited about your home sports team. Chances are you’ll be happy you did.

#### **Achievement and Education**

After weeks of work, it feels great to finish big enterprises. Finishing a class, graduating from school, or launching a project can all seriously lift a person’s mood. But finishing big undertakings requires a few to start, so go out and start something new! Learning and doing are rewarded handsomely.

#### **Celebrating and Birthdays**

Obviously, celebrations make people happy (think birthdays, anniversaries, and friendsgivings). People enjoy finding a reason — however important or silly — to meet up with loved ones, get happy about an occasion, and do something to break up a dull weekly routine.

#### **Mental Balance and Introspection**

The act of tuning into one’s mental state seems to provide a lot of happiness in and of itself. Thinking introspectively about one’s wellbeing, head space, and happiness seem to have positive effects on those very things! Try meditating, reflecting on happy experiences, or just being aware of your mental state — it may be the very thing to help boost it.

#### **Spending**

Satisfying our material desires, of course, brings lots of people happiness. Finding good deals, finally buying that car or home, and getting something nice for oneself or a loved one all create some sort of happiness. Enjoy responsibly.

#### **Weekend Trips**

People like being off work, but enjoy it dramatically more if enjoyed in good company, while doing something different. Go on a trip somewhere, have an outing nearby, or find another novel excuse for spending time with others in new scenery. The data says you certainly won’t regret it.

#### **Reading and Music**

Whether bundling up at home with a new book or discovering a song on the bus ride home, lots of people get happy through the simple act of reading or listening. Taking an hour before bed to read something new or skim through Discover Weekly is probably worth the time investment.

#### **Decisions**

Decisions also clock in as a big happiness generating activity. It’s exciting to spend time thinking about a big change, decide to do something new, and tell people about it. It leaves a lingering mood boost for lots of folks, too. So make a change you’ve been meaning to for a while; and commit to it!

### Wrapping up

These twelve categories of experience represent the foundations of daily happiness for tens of thousands of people. Given that humans are more alike than we often give them credit for, the same can likely be said about you.

This method, like any, is imperfect. Some demographics contribute more heavily than others, which may throw curious words into some topics, or may bias the topics that are represented in the model. Textual data is messy and people also don’t think about happiness in crisply defined categories of experience.

But, using these two lessons as a basic structure for understanding positivity in our everyday lives, I think it can help remind us that happiness is never so far off as we may think.

We already know many of these happy topics to be true on some level. But we rarely recognize the power that they have on our mood, and so don’t structure them into our everyday lives as readily as we should.

These categories are empirically-certified mood boosters. They’re happiness slam dunks.

So we should take what we can get. Throw out the self-help handbooks and focus on real happy experiences. You may like what you find.

_If you found this article helpful, share it with a friend or give some claps ?._

See the code for yourself on [GitHub](https://github.com/jrohrlich/DSGuideToHappy)!

