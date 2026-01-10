---
title: The Emoji developers use most — based on my analysis of 3.5GB of chat logs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T18:26:31.000Z'
originalURL: https://freecodecamp.org/news/and-the-most-popular-developer-emoji-is-d660a9687be7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RtN1V6RYVVbGp4s4cXjdhQ.png
tags:
- name: Data Science
  slug: data-science
- name: education
  slug: education
- name: social media
  slug: social-media
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Evaristo Caraballo

  Emoji have drastically changed the way we communicate in social media.

  There are numerous studies suggesting differences in the way people use emoji on
  different social media platforms. For example, the lists of the top emoji in...'
---

By Evaristo Caraballo

Emoji have drastically [changed the way we communicate](https://digiday.com/marketing/digiday-guide-things-emoji/) in social media.

There are [numerous studies](https://www.socialpilot.co/blog/how-to-use-emojis-to-boost-your-social-media-posts) suggesting differences in the way people use emoji on different social media platforms. For example, the lists of the top emoji in [Instagram](https://blog.hubspot.com/marketing/instagram-emojis-infographic), [Twitter](http://emojitracker.com/), or [Facebook](http://metro.co.uk/2017/07/17/facebook-reveals-which-emojis-are-sent-the-most-for-world-emoji-day-6785309/) have some similarities but also very distinctive patterns. Those differences get larger when moving down the list.

The possibility that the social platform dynamics might affect the use of emoji made me curious about how people might use them in a social platform to learn to code.

In this article, I look at how new developers use emoji, specifically in the freeCodeCamp’s Gitter Main Chat Room.

There are at least two ways to render emoji in Gitter:

* Using _aliases_ (like those listed by existing [online cheat sheets](https://gist.github.com/rxaviers/7360908)).
* Using the _UTF-8 form_ by either writing the emoji directly from your keyword or copying/pasting the character from online resources.

Both render differently in the message, the former rendering existing Gitter images and the latter rendering according to your machine setups. The first method “using aliases” is the most popular and will be the main subject of this discussion.

To give you a quick idea of what I was after, I wanted to quickly explore answers to questions like:

* Is there a distinctive pattern in the use of emoji?
* Which are the most popular emoji then?
* How many people use emoji?
* How versed are users in the emoji vocabulary?

So lets get started and answer these questions.

### Let's have some emoji-talk

After carrying out my analysis, I found out that about 23% of engaged chatters were also emoji users. I define an **engaged chatter** as a person that has sent at least 10 messages. If we instead compare engaged and non-engaged emoji users against all engaged chatters, that figure rises to 45%.

The number of emoji users might sound small compared to other platforms. However, it is important to note that:

* many users of the chat room were short lived
* there were users who preferred a conservative communication
* some users might not know the emoji aliases

In total, our emoji users rendered at least 753,000 emoji (600,000 when emoji were counted only once per message) with an average of 32 emoji for every 100 messages.

![Image](https://cdn-media-1.freecodecamp.org/images/DPL0IGIoIRdpB5vPiWKDd1uxUx8QBute-dCW)
_Depiction of a beeswarm chart with the approx date emoji were seen for the first time in the main chatroom. There were about 800 records with full data. (D3.js v4, my bl.ock)._

All in all, our emoji users showed a collective literacy of about 800 aliases, about 25% of the [full list of emoji in use](https://unicode.org/emoji/charts-11.0/full-emoji-list.html). [I sketched a beeswarm visualization](https://bl.ocks.org/evaristoc/d5531fb65c599370f777370e44f14242)? on D3.js showing that many of them were introduced for the first time in the chat room between July 2015 and July 2016 with a growth rate of 10 - 20 new emoji per week.

When taken per individual though, our emoji users managed a vocabulary of around 3 different emoji on an average. The difference was due to few users championing the usage of emoji, with one particular emoji master showing an emoji literacy of around 500 different ones. ?

### “Atypical” emoji-ing in the chatroom?

To have a better idea of how people emoji-ed in the chatroom I compared my findings against a [report](https://www.scribd.com/doc/262594751/SwiftKey-Emoji-Report) made by SwiftKey in 2015. There have been substantial updates to the emoji list since the release of the report but it appears to be the best free reference available still [in use](http://edition.cnn.com/2017/01/18/health/emoji-use-personality-traits-study/index.html). It was not possible to find the emoji categorizations used by SwiftKey though. I used the categories and subcategories given by [unicode.org](http://unicode.org/emoji/charts/emoji-list.html) as an approximation instead:

![Image](https://cdn-media-1.freecodecamp.org/images/yo3a6Y0bgEsqbRS1USdFU9Lh3JUX3mrdG9lp)
_Emoji SwiftKey's categories as a percentage of all emoji use (source: SwiftKey 2015 Report)_

I first evaluated the use of emoji at the category level and the results were very much as in the SwiftKey report. Most of the emoji posted in the freeCodeCamp chat room belonged to the “Smileys & People” category, which include faces, gestures, person-roles, body parts and hearts.

![Image](https://cdn-media-1.freecodecamp.org/images/Q8ooxx93MEYI9BOTTUlfiO8WCWkoJnoUvbjk)
_Emoji freeCodeCamp’s categories as proportions of count per message. Emoji users ❤️ "Smileys &amp; People"._

Because comparisons based on high level categorizations are usually too shallow, I tried another comparison focusing on the 25 most used emoji ever from 2015 to 2017 using their **subcategories** instead. Together those 25 emoji accounted for around 15% of all the emoji posted during that period.

The list of emoji and subcategories suggest that our emoji users might still fit well into the typical pattern of emoji users. The extensive use in the chat room of icons within the “face-positive” subcategory coincided with the use of the SwiftKey report's “happy faces”.

The same with the “face-negative” subcategory, much like the “sad faces” in the SwiftKey report. A bit apart was the use of “:trollface:”, which is an icon available in GitHub and it is usually associated with spam messages and sabotage, but also used as a joke in the freeCodeCamp chat room, probably in the same way as ? (“:poop:” or “:hankey:”), also listed in the 25 top-ever.

![Image](https://cdn-media-1.freecodecamp.org/images/dTneYIbhVEn7MRBMv7tp4bWw9D4PyiD5G2Qy)
_Two charts about the 25 most used emoji ever in the chatroom from 2015 to 2017, and their subcategories. Notice the extensive use of emoji hand gestures like ? (“:wave:”), ? (“:thumbsup:”), ☝️ (“:point_up:”), or ? (“:clap:”), but no kisses._

However it is in the extensive use of positive hand gestures and in general “body” icons where this chat room might distinguish itself from other benchmarks.

The most used gesture icons in the freeCodeCamp chat room are positive, related to welcome, support, validation, and recognition of success, which are values commonly shared in the freeCodeCamp community.

Another difference is the lesser use of icons like ♥️ “hearts” or ? “kisses”, suggesting that “s_haring affection”_ was not the main goal of this chat room. With a gender demography of a[bout 70–80% males](https://medium.freecodecamp.org/we-asked-20-000-people-who-they-are-and-how-theyre-learning-to-code-fff5d668969) that could prove even harder. This demographic might also explain some male-related icons in the top-ever, such as ? (“:gun:”).

Even though we could spot some deviations to the general pattern, it is too soon to make a definitive conclusion. In fact it is likely that the most important deviations might be found in how people used the _less-popular_ emoji.

Furthermore, it might be that the most important differences are not in terms of numbers, but _meanings_ or how the iconography might be interpreted by the group according to its context. A good example of what I refer to is the [swastika](https://en.wikipedia.org/wiki/Swastika). A well known example for emoji is the [eggplant](https://emojipedia.org/aubergine/). I wonder if from our 25 top-ever list ? (“:fire:”) wouldn’t have a distinctive meaning for this group, as a way to express “c_ommitment to a task”_. In any case, this is more a topic for those interested in social media communication and emoji, like i[n this article.](https://medium.com/@catherineannemoore/emoji-as-visual-literacy-cbebe37cb99c)

### And the winner is…

As a bonus, I scratched [a D3.js visualization of the monthly Top5 emoji](http://bl.ocks.org/evaristoc/663eca9722c37bd7c0d254edfb0c9d00). Being part of the list of the-most-counted-ever doesn't mean that the emoji reached the monthly top 5 once, or vice versa. Like the [Tour de France](http://www.letour.fr/en/), a rider could be consistently in the sixth position for the whole competition without ever winning a day and then listed in the most counted. Similarly, a rider could win a day and then stay the last the rest of the time. This is why this list looks a bit different.

So the winner of the monthly Top 5 is…

![Image](https://cdn-media-1.freecodecamp.org/images/alQ9jt2wSO6sWerf9fMs-xTKKGEBlyjqwjnH)
_Apple/iOS Picture of “Smiling Face with Open Mouth and Smiling Eyes”, its real CLRDname, or simply ? (source: h[ttp://www.iemoji.com)](http://www.iemoji.com" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/hglfKUEQtIiuQ48KrqbC9LIKKxqEXNk10tPE)
_Depiction of the visualization I made showing ? winning the first place several times month after month between 01–2015 and 11–2017. No doubt about its popularity (D3.js v4, my bl.ock)._

Frankly, I didn’t expect ? (“:smile:”) to be the most popular emoji. I thought it was ? (“:joy:”), given that Apple recently revealed it as it[s most popular during 2017.](http://fortune.com/2017/11/03/apple-most-popular-emoji/) 

The following 8 emoji also appeared in the freeCodeCamp casual chatroom. All about smiles :). Do you think you are an emoji-fan? Guess their aliases! (Observation: names/keywords can vary by platform…)

![Image](https://cdn-media-1.freecodecamp.org/images/9ytewgop1dwDkm7Mo3HDfPKmbhJW-NdbYiNW)
_Apple/iOS emoji pictures_

I used Python and the [Gitter API](https://developer.gitter.im/docs/welcome) to get the messages from the freeCodeCamp main chat room. Python libraries like [multiprocessing](https://docs.python.org/3.5/library/multiprocessing.html) and [emoji](https://github.com/carpedm20/emoji/) were used to transform the data. Part of the transformations also required data available online, for which I made customized scrapers also with Python libraries (requests, [urllib](https://docs.python.org/3/library/urllib.html), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)). To analyze the data I used plain Python and some [pandas](https://pandas.pydata.org/). Explorative visualizations were made using [matplotlib](https://matplotlib.org/) while the interactive ones where made in [D3.js](https://d3js.org/).

Versions of the code will be available on my [GitHub repository](https://github.com/evaristoc/fCC_emojis) together with a few final datasets. Regarding the raw datasets used for this project they are now available on the freeCodeCamp’s [Kaggle account](https://www.kaggle.com/free-code-camp).

The motivation of this project adheres to the mission of the freeCodeCamp’s [Open Data Initiative](https://github.com/freeCodeCamp/open-data). A big thanks to the people in the freeCodeCamp DataScience room and specially to [mstellaluna](https://github.com/mstellaluna) for her comments!

And remember, if you found the information in this article useful or you simply liked the content, don’t forget to leave some claps ? ? before you leave! Thanks and Happy Coding! ?

