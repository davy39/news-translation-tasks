---
title: I crunched the data from every episode of Netflix’s Ultimate Beastmaster
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-29T04:59:58.000Z'
originalURL: https://freecodecamp.org/news/i-crunched-the-data-from-every-episode-of-netflixs-ultimate-beastmaster-71e91e471574
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pa3ZXPlXVGBZok_qoexcIQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Life lessons
  slug: life-lessons
- name: sports
  slug: sports
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kande Bonfim

  There’s a new show on Netflix called Ultimate Beastmaster. It’s basically a clone
  of American Ninja Warrior: strong people running through crazy hard obstacle courses.

  I decided to dive in and give the show the full data science treat...'
---

By Kande Bonfim

There’s a new show on Netflix called Ultimate Beastmaster. It’s basically a clone of American Ninja Warrior: strong people running through crazy hard obstacle courses.

I decided to dive in and give the show the full data science treatment. Fair warning if you haven’t watched the show yet — **there are spoilers here**.

Here we go.

### The participants

There are **10 episodes**. **9** of them presenting **12 new participants each**. **108 people** jumping like crazy trying to be the next **Ultimate Beastmaster** while you eat a family-sized Cheetos**.**

The following graph gives a big picture of what happened in the show. **I’m excluding the final here, because we’ll talk about it separately later in this article.**

![Image](https://cdn-media-1.freecodecamp.org/images/RbyZfyraQX0dRfMsjClCjW0PjFYP96nZ8Nw8)
_The Ultimate Scatterplot_

Now let's get dive into the data.

#### Gender

Unfortunately, there's still a huge difference in the number of men and women in the _Ultimate Beastmaster_. Only **22 women** faced the beast. **That's 20.4% percent of the competitors.**

It gets even worse: All the women were eliminated in the first (81%) and second level (13%). The only exception was the young student ?? Si**lke Sollfrank (1**8 yrs) that got eliminated on Level 3. That's it. No **woman in the finals.** ?

![Image](https://cdn-media-1.freecodecamp.org/images/XYwzjvaesGvfUcrRQLwMubJc9rfjNYaYB-SI)
_?? Mi**mi Bonny w**as one of the 5 **woman eliminated on Throat Erosion w**here competitors must use an industrial trampoline to jump and grab a lever releasing a climbing wall. Th**is obstacle eliminated just women.**_

**That made me think about how the show should handle with some advantages the average male body has over the female’s in this competition. **Some obstacles were way too hard to beat if you are shorter than average**.**

![Image](https://cdn-media-1.freecodecamp.org/images/egTuXWCMEdvy6UgtbgIMILIXiUcIsg6g3cI-)
_This is not a music wave. It's a histogram._

#### **Age**

**The age of the participants varies **from 18 to 40 years** (29.1 Avg.). The five youngest ones are German (no clue why).**

**The Beastmasters — the winners of each episode — are aged **20 to 35 year sold** (28.1 on average). Being too young or too old doesn't help.**

![Image](https://cdn-media-1.freecodecamp.org/images/AZTwswy4QZOAk37Qg12FtWmtAvmpF6IVlhgS)
_Yeah, no Japanese in the finals… ???_

#### **The finals**

**?? USA brought 3 beastmasters. ?? Germany and ?? South Korea, 2. But it only took one ?? Brazilian to win the Ultimate Beastmaster prize.**

**Yes, I'm Brazilian too, and now I feel better about the **7x1** we took from Germany in the World Cup.**

### **Points**

![Image](https://cdn-media-1.freecodecamp.org/images/oqBK9E9HUbcOrYpYuZrufAt0sfEwUb5YVFAK)

![Image](https://cdn-media-1.freecodecamp.org/images/mMkIVHhV73tqcyRie7B78PWYb0QuGinAThdP)
_Points acquired by each competitor along the tv show._

**Note that there's a **soft tendency of dropping your score once you’re older**.**

> **Correlation of age and points: **-0.24****

### **Competition Funnel**

![Image](https://cdn-media-1.freecodecamp.org/images/fvvS6isat1bauHbT1WATABJFmisqF-rfduQh)
_**? Eliminated — ?** Cl**assified**_

### **The Levels**

**Let's take a deeper look into each level of the competition and their main causes of failing.**

### **Level 1**

![Image](https://cdn-media-1.freecodecamp.org/images/Mwopr9Bq3nZJbcm2O0UQLvCqmve4d5p3fO2i)
_Main causes of failing ordered by position in level 1._

**Only **5** **(4.6%)** participants were able to accomplish the first level. The most difficult parts of the track are:**

1. **Energy Coils** 30.6%
2. **Mag Wall** 27.8%
3. **Faceplant** 22.2%

**Brandon Douglass ?? is** the ONLY ONE that failed in Br_ain Matter._ He is the tiny red line in the chart.

**The average time spent on this track is **2'54** and for accomplishing it is **5'29**. ?? Fe**lipe Camargo is** the fastest to finish it: 5'**10 ?. And** the quickest to fail is a Brazilian competitor too: ?? **Karine Abrahim faile**d in 0'18.******

**39.3** is the average points per person in this track and it varies **from 10 to 70** points. **Nobody got all the 80 points available in this level**.

### **Level 2**

![Image](https://cdn-media-1.freecodecamp.org/images/GhCt1PUXocBYGvlGjdpZVMQM3j8eKeI5W3Dc)
_Main causes of failing ordered by position in level 2._

**?? Taeho Kwon wa**s the only one to complete the second level (he made it in 4'**28).**

**Main causes of failing:**

1. **Dreadmills** 27.8%
2. **Spinal Ascent** 22.2%
3. **Stomach Churn** 19.4%

**Points**: from **20 to 220** (**109.1 in average**).

**Time:** from **1'01 to 9'53** (**4'08 in average**).

### **Level 3**

![Image](https://cdn-media-1.freecodecamp.org/images/iwaqGm6KvKNgd3QmxnssjPVcYg6uStgvQv1z)
_Main causes of failing ordered by position in level 3._

**?? He**eyong Park wa**s the only one to accomplish this level (he made it in 6'**19).****

**Main causes of failing:**

1. **Ejector ⚠️** 40%
2. **Bungee Beds** 20%
3. **The Extractor** 13.3%

**Points**: from **90 to 340** (**186.6 in average**).

**Time:** from **0'03 to 12'48** (**2'17 in average**).

### **Which country won?**

**What if the Ultimate Beastmaster were a competition between the countries instead of individuals? Which country performed the better result?**

**Taking the average score by country, we can get the result: ?? So**uth Korea won the Ultimate Beastmaster!****

**`+-----------------+-------------+----------+`**  
**`|    Country      | Avg. Points | Position |`**  
**`+-----------------+-------------+----------+`**  
**`| ??South Korea   |       117.2 | 1st      |`**  
**`| ??Germany       |         110 | 2nd      |`**  
**`| ??United States |       105.5 | 3rd      |`**  
**`| ??Mexico        |       100.5 | 4th      |`**  
**`| ??Brazil        |        96.1 | 5th      |`**  
**`| ??Japan         |        69.4 | 6th      |`**  
**`+-----------------+-------------+----------+`**

### **The Finalists**

**`+------------------+-----+--------------------------+---------+`**  
**`|       name       | age |           job            | country |`**  
**`+------------------+-----+--------------------------+---------+`**  
**`| Felipe Camargo   |  24 | Professional Climber     | Brazil  |`**  
**`| David Manthei    |  20 | Architecture Student     | Germany |`**  
**`| Philip Meyer     |  23 | Soldier                  | Germany |`**  
**`| Roberto Perez    |  25 | Student                  | Mexico  |`**  
**`| Heeyong Park     |  34 | Ice Climber              | Korea   |`**  
**`| Hyunho Kim       |  30 | Crossfit Coach           | Korea   |`**  
**`| Steven Tucker    |  29 | Rock Climbing Instructor | EUA     |`**  
**`| Jonathan Collins |  33 | Track Coach and Model    | EUA     |`**  
**`| Ken Corigliano   |  35 | Air Force Major          | EUA     |`**  
**`+------------------+-----+--------------------------+---------+`**

**We can clearly see why the finalists got the Beastmaster title. Their average of points is **265** against **88.7** of the other competitors.**

### **The dataset**

**This article is based on the data gathered by me, and it’s available for further expansion if you want to help or just try some analysis. Also, the dataset is available on [Kaggle](https://www.kaggle.com/kandebonfim/ultimate-beastmaster).**

**Discovered something new?** My twitter is [@kandebonfim](https://twitter.com/kandebonfim).

