---
title: How I analyzed the data from my FitBit to improve my overall health
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T21:34:54.000Z'
originalURL: https://freecodecamp.org/news/how-i-analyzed-the-data-from-my-fitbit-to-improve-my-overall-health-a2e36426d8f9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tFLhws9xNR64HVbz
tags:
- name: Data Science
  slug: data-science
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Yash Soni

  It turns out that data can keep you healthy


  _Photo Credit: [Unsplash](https://unsplash.com/@franki?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Franki Chamaki on <a href="https://unsplash.com?utm_source...'
---

By Yash Soni

#### It turns out that data can keep you healthy

![Image](https://cdn-media-1.freecodecamp.org/images/QZMrnNh5FJCEunBOXlCOllbiiZIZRaub1Kfq)
_Photo Credit: [Unsplash](https://unsplash.com/@franki?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Franki Chamaki</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Physical activity trackers have become a multimillion-dollar product category. I have had my fair share of fancy trackers, starting early from [Nike Fuelband](https://www.wareable.com/fitness-trackers/not-so-happy-birthday-nike-fuelband-2351) and then [MI activity band](https://www.mi.com/in/miband/). Personally, I couldn’t adopt any of them very well and eventually, they all ended up being a fancy digital watch which needed a re-charge every few days in order for them to tell the correct time.

And then, a few months back, I was gifted a [Fitbit Versa](https://www.fitbit.com/versa) by a friend of mine. Something clicked. Why?

A lot had happened since I gave up the idea of health bands being effective. When I received this gift, I was at a stage where I was glued to a chair and my laptop. As a result, I had a severe problem of back pain and postural imbalance. The wrongdoing of many years could not be fixed in just days or weeks. Fighting an arduous battle against sitting, which is now considered by many as the [new ‘smoking’](https://www.startstanding.org/sitting-new-smoking/), I became mindful about my posture and the idea of maintaining an active lifestyle.

So, I thought of giving Fitbit a clean slate and tried it for a week. The Fitbit app did a pretty good job of capturing and showcasing the data in a consumable format.

![Image](https://cdn-media-1.freecodecamp.org/images/OW8rJRXNpRL94YLQyv3H9J3fn6sSmrgCZuRd)

![Image](https://cdn-media-1.freecodecamp.org/images/W3lmQTP1gQr6BMKZolZng8t-jm6BUuYdCvpJ)

![Image](https://cdn-media-1.freecodecamp.org/images/xQ6WXzbyd2CoctCHdiKP0Gobe-V8X47BTHTm)
_Activity, calorie burn and sleep analysis on the Fitbit app._

It had been two weeks since my break up with my mechanical watch. Intrigued by the sheer variety of data points Fitbit could capture, an urge began to see what lies hidden behind the data.

![Image](https://cdn-media-1.freecodecamp.org/images/mY1YeWyGdMshlqTrJWGh6Lo-RyMmG7Dv395T)
_The experimentation cycle. [Src](https://thehealthsciencesacademy.org/health-tips/how-to-conduct-an-effective-self-experiment/" rel="noopener" target="_blank" title=")_

I soon began an experiment to see how well I could keep up with the goals that I had defined. I also wanted to know if there were any extraneous factors which influenced these goals. Finally, I wanted to uncover any hidden and interesting findings along the way. I was particularly interested to discover:

* How active are my days? Do I spend a considerable amount of time being sedentary?
* How does this data vary on weekdays vs weekends?
* What factors contribute to the highest calorie burn?
* Which exercises are the best and easiest way to achieve my daily goals?
* Have I been following a steady sleep schedule? What factors influence it?
* Understand the sleep stages and find out what it takes to get a better deep sleep.
* What is the impact of a Netflix binge on weekend sleep?
* Train a simple Machine Learning model to see if there is a hidden pattern to attain better sleep.

I couldn’t find the answers to these from the standard Fitbit app. I needed the raw data.

### Getting the Data

The first task was to figure out ways to extract the data from my device. Scanning through the developer pages, I found that they have a provision of [Web API](https://dev.fitbit.com/build/reference/web-api/) to access the user data. Examining these APIs, I was shocked to see the sheer amount of data that is being captured and saved every minute. Steps covered, calories burned, sleep stages and even [heart rate/minute](https://dev.fitbit.com/build/reference/web-api/heart-rate/) for any-given-day is being recorded!

Sometimes, the seductive lure of knowing about our general wellness makes us forget what personal information we [end up sharing](https://www.bna.com/consumers-wary-healthcare-n57982091088/). Reading through their privacy policies, I found that Fitbit has put in additional checks to keep the data safe. Anyways this requires a separate post of its own, so without digressing from our main goal, let’s continue.

I registered my app and got the necessary client side credentials to begin the data grabbing. After going through the necessary authorization steps, I collected and merged my daily Activity, Sleep and Heart rate data and dumped it in an Excel file. After some data cleansing, the dataset was ready!

![Image](https://cdn-media-1.freecodecamp.org/images/fkeipr40UH05TkJaRBwOsL8wbP2DLSmhbWN2)

![Image](https://cdn-media-1.freecodecamp.org/images/3qRwsTxyxlSj-bS7E7Nrq4cyYnmPjim7Eoeh)
_Sample data grabber session and the corresponding Pandas DataFrame_

_PS. The entire code can be found [here](https://github.com/yashatgit/fitbit-analyzer) along with the [Jupyter notebook](https://github.com/yashatgit/fitbit-analyzer/blob/master/Fitbit_Data_Analysis.ipynb)._

_PPS. Disclaimer: This data analysis is based on a very limited set of data points and will be difficult to generalise to the masses. Please consider it as a fun read!_

### Activity analysis

Fitbit has a wide array of data points to measure daily activity levels. Steps, Calories, and floors are some of the standard measures. It also tracks how many minutes I spend daily being moderately, slightly and very active.

Not fussing on the daily calorie burn, I had kept a goal of attaining 8000 steps each day on my Fitbit device. The graphs below suggested I am averaging about ~7800 steps per day which is quite close to my goal. There are some studies which suggest hitting [10,000](https://blog.fitbit.com/should-you-really-take-10000-steps-a-day/) [steps per day is ideal](https://www.huffingtonpost.ca/leigh-vanderloo/10000-steps-a-day_b_16077702.html) and that shall be the next target.

Tuesdays to Saturdays were the days where I averaged about 40 minutes of _very active minutes —_ which simply translates to [active exercise](https://help.fitbit.com/articles/en_US/Help_article/1853/?l=en_US&c=Topics%3ADashboard&fs=Search&pn=1). Fewer minutes on Sundays were due to purely due to laziness/recovery time. The drop in _active minutes_ on Mondays proves that I am falling for the Monday Blues and guess it’s time to fix that.

![Image](https://cdn-media-1.freecodecamp.org/images/pvzvoW8pbiJ9an-55Rh8CnNqI4BvCxoLynJM)

Analyzing the amount of calories burned per minute for various Activities shows some interesting findings. Though there is a lot of similar data available on internet, it is very difficult to generalize these numbers for everyone. Since a lot of this depends on the fitness levels, demographics, skillset and most importantly how much I enjoy doing some specific exercises.

![Image](https://cdn-media-1.freecodecamp.org/images/YFwjh8mzMQ5EzyNzTR9W2iNUcxJwwbIZwxmA)

It is interesting to see that running helps me burn almost 12 calories per minute. The [math is simple](https://www.dailymail.co.uk/femail/article-3827053/How-exercise-does-burn-favourite-tipple.html): to compensate for a beer, a 10 minute run is what I need.

Tennis — the favorite activity from the lot — takes the second spot. That’s again a win-win scenario! It will be interesting to see if this number changes as I improve my skills.

Swimming numbers were not shocking to me because I am still struggling to keep up with my continuous lap count. And after spending some time in pool, the exercise turns to a leisure activity.

Point to note here is that calories burned should not be the only metric on which these activities can be graded. But, this happens to be the only metric which I can currently measure via Fitbit.

Lastly, it is useful to see how the various data points correlate with each other. Plotting a correlation heat-map helps uncover some findings.

![Image](https://cdn-media-1.freecodecamp.org/images/fV5HQJGs-Wj6sMf0WF2-S6i5yrzAFyzGaesg)

The calories burned is strongly related to amount of _steps_ and _active minutes_. _Minutes sedentary_ has a negative correlation with Weekdays which implies that I spend more time slacking off on weekends.

### Sleep Analysis

Sleep is essential to helping maintain mood, memory, and cognitive performance and there is no running from it. We spend about a third of our life in sleeping. That’s a staggering **26 years spent sleeping in bed**! While metabolism generally slows down, all major organs and regulatory systems continue to function. Hence, it becomes important to get the most out of our sleep.

Reading more on this, I found that there are some standard ways which can help achieve a good night sleep.

* [Following a good sleep schedule](http://time.com/3183183/best-time-to-sleep/)
* [Avoid bright/blue light at night before hitting the bed](https://justgetflux.com/research.html)
* Avoid caffeine later in the day
* Sleep in a cool and dark room
* Getting at-least [7–9 hours](https://www.sleepfoundation.org/how-sleep-works/how-much-sleep-do-we-really-need) of sleep. There are some studies which say that even in [5 hours](https://blog.bulletproof.com/sleep-hacking-1-million-people-prove-sleeping-5-hours-is-healther-than-sleeping-8-hours/) you can achieve the most out of your sleep.

Over the course of this experiment, I tried to follow the above steps to bind myself to a strict sleep schedule. It was time to validate them.

From the graphs below, I found that I was averaging a sleep of 7 hours without much deviation in the numbers. Though I was able to hit bed before 11, the wakeup timings still ranged from 5:30–7:00 AM.

![Image](https://cdn-media-1.freecodecamp.org/images/1aoBJ18QRW91xMe3VeYvnXk0MaJKt34VSQNZ)

![Image](https://cdn-media-1.freecodecamp.org/images/NSDjE1w-cbpmfyQ0s4sW2cJJtmlpNGMEOWgx)

Though the average duration was somewhat similar, the overall sleep quality was not the same. On some days, I was very active even by attaining 6 hours of sleep, while there have been many instances when even after sleeping late, I wasn’t feeling fresh. I found the answer by analyzing the mystic **[sleep cycles](https://www.sleepfoundation.org/how-sleep-works)**.

While we are asleep, our body typically goes through several sleep cycles, alternating between the following stages:

**LIGHT SLEEP:** This stage typically begins within minutes of falling asleep. Breathing and heart rate typically decrease slightly during this stage. Light sleep promotes mental and physical recovery.

**DEEP SLEEP:** Deep sleep typically occurs in the first few hours of sleep. Breathing becomes slower and muscles relax while heart rate usually becomes more regular. When we wake up feeling refreshed in the morning, it is likely that we have experienced solid periods of deep sleep. Deep sleep promotes physical recovery and aspects of memory and learning.

**REM SLEEP:** REM sleep is an active period of sleep marked by intense brain activity. The first phase of REM sleep typically occurs after an initial stage of deep sleep. Breathing is more rapid, irregular and shallow. The eyes move rapidly in various directions, hence the name Rapid Eye Movement — REM Sleep. This is the stage where we generally see dreams in our sleep. REM sleep has been shown to play an important role in mood regulation, learning, and memory.

The plot below shows that on an average, my body spends just about 17% in Deep sleep, 19% REM and the rest in either light or being slightly awake. The date-time plot of Light and Deep sleep shows that these numbers vary a lot.

![Image](https://cdn-media-1.freecodecamp.org/images/5hV7luHn9ANVZ2daqzbNIKec9YOd3t-gaFY9)

![Image](https://cdn-media-1.freecodecamp.org/images/oSi2W4JKlla6RB1ufA0BBWvO-DvS3SOXiy6S)

If we plot the correlation of different sleep stages, we see that time spent in bed is highly correlated with Light sleep but there is no strong correlation with Deep sleep.

![Image](https://cdn-media-1.freecodecamp.org/images/mdlNPY-xnzrhFsQCvhY1BK55IojcCPG7aINE)

This essentially means that just by sleeping more doesn’t always guarantee a good deep sleep. I guess this helps validate the important learning about sleep:

> [It is the quality of sleep that matters and not the quantity.](https://www.sleep.org/articles/quality-quantity-matters-sleep/)

Following a strict sleep schedule on weekdays is easy, but weekends are a different ballgame altogether.

![Image](https://cdn-media-1.freecodecamp.org/images/lP-H1bLB-YwClB0r0vSmoFBCG6Ifq45ul7Gw)

The boxplot above shows Saturdays are the most affected, where the time in bed ranges from 5–9 hours. The Netflix Binge and weekend parties are some of the vices which have affected this routine. On the contrary, the smaller boxplot on Sundays depicts me gearing up for the Monday mornings. It’s interesting to see how these subconscious body behaviours are clearly exposed in these plots.

Finally, I wanted to see if my daily activities had any effect on my sleep. Though I didn’t have much data for the Machine Learning model,  
an initial run showed some interesting results. It predicted that being active in the day and getting to bed before 11PM has some positive contributions to the final deep sleep minutes.

Though it is too soon to validate it, I will be repeating this again once I have some more sleep data and additional features to improve the accuracy of the model. The details can be found in [this Jupyter Notebook](https://github.com/yashatgit/fitbit-analyzer/blob/master/Fitbit_Data_Analysis.ipynb).

#### Was it all worth it?

This experiment has been a rewarding experience. I identified some interesting ways in which my body responds to external stimuli. It is like a machine where tweaking certain knobs can help achieve different results.

Next up in line I plan to set up some improved activity goals. I will also be trying out [some](https://blog.bulletproof.com/binaural-beats-sleep-meditation-benefits/) [biohacks](https://blog.bulletproof.com/how-to-hack-your-sleep-the-art-and-science-of-sleeping/) to see if these have any positive effects on my sleep quality. I am also considering developing a Fitbit alarm app which only wakes me up once I have acquired sufficient amount of quality sleep (not sure if this already exists?).

Finally, I do not intend to label this as an _experiment_ anymore. The daily routine which felt forceful in the beginning has become a habit now. In the past, I’d come across many articles that were studies of the importance of waking up early as well, and finally I embraced it first-hand. This Medium article, which is in fact my first one, is one of the many byproducts of this new found habit.

Thanks for taking the time to go through my analyses. I will be more than thankful to know if you liked it and have suggestion about any improvements in general! :)

