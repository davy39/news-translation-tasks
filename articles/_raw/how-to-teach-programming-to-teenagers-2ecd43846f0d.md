---
title: How to Teach Programming to Teenagers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T14:24:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-teach-programming-to-teenagers-2ecd43846f0d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FNZLxkvfXe2PAIlT8pbf3w.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: teaching
  slug: teaching
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sean Choi

  In the past, many enthusiastic parents have approached me and asked me how I learned
  to code in the beginning — mainly with the interest in finding ways to help their
  children how to code. And every time, I didn’t have a clear answer for...'
---

By Sean Choi

In the past, many enthusiastic parents have approached me and asked me how I learned to code in the beginning — mainly with the interest in finding ways to help their children how to code. And every time, I didn’t have a clear answer for them, because I learned to code at a much later age than most of the children of these parents. In the interest of helping these parents, I also tried to find resources that are made to help the children learn to code.

I discovered that there are a lot of resources help K-6 students learn how to code. Some examples include [Scratch](https://scratch.mit.edu/about) and the Hour of Code in [Code.org](https://code.org/) which are quite useful for someone new to get acquainted with programming.

Through these platforms, students write simple programs that make graphical creatures move or build simple games and learn the basic tools of programming — such as loops and conditionals — while building useful problem-solving skills. The major strength of these platforms is the visual feedback from the platform, which really helps the students stay constantly engaged with the curriculum and the exercises.

However, teaching programming to teenagers over the 6th grade is a completely different beast. [This article](https://www.geekwire.com/2018/new-research-finds-95-teens-access-smartphone-45-online-almost-constantly/) shows that over 95% of teenagers today have access to smartphones. So, the visual feedback from Scratch or Code.org no longer wows them. In fact, I discovered that the teenagers actually find them quite mundane and childish.

Instead, teenagers want to build or do something _REAL_ that they can showcase. Such as building and launching a real iPhone app or their own website or hacking into some system. But how can you get someone who just finished a set of Scratch exercises to building an iPhone app, while getting them constantly engaged to finish it?

So, I wanted to share my experiences in teaching programming to 4 teenagers over the course of two years. The students started out having a different range of programming skills, personalities, and expectations. Therefore, to keep everyone engaged, I had to go through various trials to find the teaching materials that worked for everyone.

The main goal of this article is to share what I learned and the trials that were successful, in the hopes of helping other teenagers learn to love programming.

# Teenagers have High Expectations

I learned that teenagers absorb new technology like dry sponges. While adults may be quite okay with being a technically bit out-of-date, teenagers bet their lives on being cool and following the latest trend out there. I found that teenagers tend to use the coolest and latest apps even before they make it to TechCrunch or CNBC headlines.

In fact, it was my students who introduced me to a bunch of [.io games](https://www.crazygames.com/c/io) and [HQ Trivia](https://en.wikipedia.org/wiki/HQ_Trivia). So, it’s important that what they learn is _COOL_, and something that they can share with their friends.

The first thing they asked when I started the programming class was “Can we Hack stuff? Like websites and iPhone APPs?”.

So, I told them we should first learn HTML and CSS to learn how to hack a website and showed them this:

```
<!DOCTYPE HTML>
<html>  
<head><title>Hello World!</title></head>  
<body><h1>Hello World!</h1></body>
</html>
```

I explained what each of these tags meant and how they will show up on a page. I loaded a page with this `hello.html` and all their expectations of seeing a cool web page went down the drain. They were immediately bored.

However, I continued the class to teach them more HTML, CSS and basic JavaScript. I felt that by teaching them more HTML, CSS and JavaScript and learning the techniques to build some example websites, they would feel more engaged. However, I was wrong.

Even after series of building simple websites and deploying them over [Firebase](https://firebase.google.com/), they kept on saying they wanted to do something more _REAL_ and something they could show their friends.

# Teaching them to do Something REAL

I realized that there are many ways to do something real, and it was not at all creating software with cute GUI or teaching them new data structures, or getting some material from Harvard CS50 and showing them.

I decided it would be best to use hardware and make the students physically feel what they had coded. My two choices were [Raspberry Pi](https://amzn.to/2PLBxk1) and [Arduino](https://amzn.to/2CK7eEc).

Raspberry Pi is a miniature computer that runs its own version of Linux, and is capable of running most programming languages. You can purchase various peripherals that can be controlled via your own custom software.

Arduino is more involved. It is as an open-source hardware platform, and many companies build various kits, such as [Smart Autonomous Car](https://amzn.to/2PJHWfu) and [Quadruped Robot](https://amzn.to/2RQTaNu).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/smart-car.jpeg)
_Smart car we built using Arduino_

Using Raspberry Pi, we built a [weather station](https://amzn.to/2pTtXoN) that detects temperature and air pressure of the surrounding area and sends them to a cloud database. Then, the students were able to view the weather data through an online graphing tool. We also programmed simple utility functions, such as changing temperature units and finding min/max/average temperature, to post to the database. These exercises helped the students learn simple data structures and algorithms, such as arrays, dictionaries and sorting.

After this, we moved on to building the Arduino-based autonomous car. Each student had sample code that made the cars move and detect obstacles. Then, we built a maze and gave a prize to the student who made the car that got out of the maze first.

The students naturally discussed among themselves which logic would help the car move out of the maze most efficiently. And they found it pretty cool that their algorithm immediately was learned and executed by the car that they built. Most importantly, the students really enjoyed it, since it was real and tangible.

We also did some exercises in learning the basics of hacking! Similar to [LeetCode](https://leetcode.com/), which is aimed at helping participants learn how to solve interview problems, there are many tools built to help students learn the basics of hacking. For example, [HackThis](https://www.hackthis.co.uk/) is a nice website that gives you a series of challenges that you can view and solve on your browser. It requires you to use many of existing browser tools, such as Chrome dev tools, to find deficiencies that you can take advantage of to gain access into the system.

The students really loved this exercise, because solving these exercises made them feel like spies in Mission Impossible. After finishing the challenge, they actually went ahead into real websites (I made sure they didn’t do something illegal…) and tried to find loopholes that they could use.

Once they are more prepared and learn the basic Linux concepts, I am planning to teach them more advanced hacking concepts with [Kali](https://www.kali.org/) Linux, which I think will be even more exciting.

# Competition as a Learning Tool

![Image](https://www.freecodecamp.org/news/content/images/2020/07/clash-of-code.png)
_Clash of Code to start the day_

Finally, the last thing I learned was that the teenagers are quite competitive. They like exercises that gave them immediate feedback, such as giving them a score, a badge, or placing them on a real scoreboard.

The best platform I found that incentivized the students was [CodingGame](https://www.codingame.com/start). They would solve each programming exercise and level up in the process. The exercises also have some nice visual components to them, enabling the students to be quite engaged to the exercises.

We would also start the day by doing a session of [Clash of Code](https://www.codingame.com/multiplayer/clashofcode), which is a quick 5 minute live programming challenge between other online users, and the students would sometimes win against other players that had higher levels than they did! It really got them pumped up to start another day of learning to program.

# Final Thoughts

Teaching programming is fun and educational. Not only do you learn how to teach another person, but it also gives you a chance to be in the students’ shoes. You learn to understand how others think about a problem and realize that there are many different ways to perceive the same problem. You also learn how to describe problems in ways that the students would enjoy thinking about. Also, personally, I think teaching helps you become a more understanding and patient person.

I hope you can also let me know how you helped others join the world of programming. For those of you who are starting out in the journey of helping others to learn to program, I really hope that this article gave some takeaways for your own curriculum.

Thank you for reading!

