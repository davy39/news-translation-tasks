---
title: How I Passed the CompTIA Linux+ Exam
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-30T10:01:32.000Z'
originalURL: https://freecodecamp.org/news/the-linux-exam-story
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Screen-Shot-2020-04-29-at-10.33.10-PM.png
tags:
- name: comptia
  slug: comptia
- name: 'exam '
  slug: exam
- name: learning
  slug: learning
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'By Clark Jason Ngo

  Summary of this article:


  The backstory: why CompTIA Linux+ exam.

  Review of learning resources: what is good and what is not good.

  Retrospective on studying: what worked and did not work.

  My experience during the exam: how the test...'
---

By Clark Jason Ngo

### Summary of this article:

* The backstory: why CompTIA Linux+ exam.
* Review of learning resources: what is good and what is not good.
* Retrospective on studying: what worked and did not work.
* My experience during the exam: how the test was conducted and how I felt.
* My approach during the exam: what strategies to use and mindset to have.
* Getting an awesome badge: what it looks like and what's in it for me?
* Bonus: as most of my materials are sponsored by the school, I've looked for free content for you to study for the exam, such as [filesystem hierarchy](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard), [basic linux commands](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html#binEssentialUserCommandBinaries), using [AWS EC2 Ubuntu](https://aws.amazon.com/mp/linux/) as your Linux environment.  I also created a flash card in Trello, available [here](https://trello.com/b/viGl7wam/linux-prep).  Disclaimer: free content might not be sufficient. 
* Exam objectives: [Official CompTIA Linux+ Exam Objectives](https://www.comptia.jp/pdf/comptia-linux-xk0-004-exam-objectives.pdf). 

### TLDR exam tips (I had no professional experience with Linux):

* Focus on the Activity Section of the CompTIA Study Guide and follow along with your own Linux environment.
* Practice on Performance-Based Questions (PBQs). They show around 10 choices that all _look_ correct.
* Play around with Linux command combinations using piping (|)
* Configure IP tables, firewall, and troubleshooting.
* Learn the configuration steps, boot process, and backing up files.
* Basic bash scripting and regular expressions.

_Read until the end for tips on how to have the correct mindset and strategies to answer difficult questions. Also, a video of me summarizing this article during a club meeting at our school is available at the bottom of the article. Do check the video out as it has a Q&A section towards the end._

I'd like to start off with a big thank you to [School of Technology and Computing](https://ciae.cityu.edu/programs/) of [City University of Seattle](https://www.cityu.edu/) (CityU). They provided me with a job, career growth, and sponsored my CompTIA learning materials and exam voucher. 

As an F-1 Student Visa holder with limited job opportunities, this allowed me to earn extra income, of which I [donate](https://www.freecodecamp.org/donate/) a portion to freeCodeCamp on a monthly basis. 

This is a loose continuation from my story: _[Why I abandoned my MBA to get a master's in Computer Science](https://www.freecodecamp.org/news/cjn-why-i-abandoned-my-mba-to-get-a-masters-in-computer-science/)_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*cSvQ_M7qvgXFrIrA.jpg)
_City University of Seattle Campus_

## Why CompTIA Linux+?

In July 2019, our school, with the help of our director of external relations, landed a contract with Amazon Web Services (AWS) and Washington Technology Industry Association (WTIA), called the AWS Apprenticeship Program (AAP). 

We had the opportunity to train 23 military veterans and veteran spouses. Their requirement was to pass CompTIA Linux+ Exam and CityU's Full Stack System Developer Program which includes CompTIA Linux+ Exam preparation. Once they met both criteria, they'd be able to transition to on-the-job training with AWS. 

My role at the time was a Lead Teaching Assistant (TA) and I was tasked to help build the Dean's program proposal. I coordinated with 6 other TAs to build the courses, which consisted the following: Linux I, Linux II, Networking, Web Development, JavaScript/TypeScript, Full Stack - MEAN Stack, Python, and Full Stack - Django.

As this was our first contract, we were building the plane while trying to fly it.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-295.png)
_Picture looks fun! But not in real life lol!_

### We utilized the following resources for our Linux Operating System course:

* Textbook: Pro Bash Programming: Scripting the GNU/Linux Shell, Second Edition, by Chris F. A. Johnson, Jayant Varma 
* Student's Linux environment: AWS EC2 Instance with Ubuntu
* Virtual Lab: InfoSec Learning

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-296.png)

### What I learned

* A lot of bash scripting exercises and coding challenges
* How to SSH to a remote server (EC2 Instance)
* Various Linux commands and configuration setups related to CompTIA Linux+

After a few weeks into the program, we researched more and listened to student feedback. Turns out we were doing too much bash scripting and lacked on CompTIA Linux+ Exam preparation.

> The students were in hell during the first few weeks of bash scripting

We immediately partnered with CompTIA to get CompTIA Linux+ Exam Study materials at bulk price. We pivoted hard and changed parts of our program to integrate the new study materials.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-299.png)
_Cool badge_

> Good thing our department was practicing Agile methodology and it made us very nimble.

### The new resources are as follows:

* CertMaster Learn - includes eBook, Performance-Based Question (PBQ), and CompTIA Videos (Note: This was last year. If you purchased this year, you won't have the PBQs, but you get a new interface, and an additional practice test).
* CertMaster Practice - multiple-choice questions on steroids. Once you've accumulated a good amount of wrong answers, you'd get feedback on why your answers are wrong and it explains the other choices as well. Then, it pushes your progress bar back.
* CertMaster Labs - shorter lab activities compared to InfoSec Labs.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-298.png)
_The CompTIA Linux+ Learning bundle_

### My thoughts on the new resources

I read the eBook from top to bottom and it was helpful to obtain an overview. However, I wasn't able to retain any knowledge from reading it. I breezed through both the CertMaster Practice and CertMaster Labs and I gained nothing as well. 

> What's wrong with me? Hmm..

Because of an opportunity to teach the JavaScript/TypeScript course in the AAP program and the unfortunate event of my dad's passing, my road to Linux+ Exam was eventually derailed and forgotten.

> Man.... What a bummer...

## Fast forward to the end of the AWS Apprenticeship Program

In November 2019, we successfully transitioned all 23 students! A 100%! We were the only partner school to have done that.

Most credit goes to the School of Technology & Computing Dean's repeated quotes of "leave no man behind" - similar to the soldier's creed: "I will never leave a fallen comrade behind", and "we stay together, we survive" (from the movie Gladiator).

The program's success was largely attributed to TAs, who supported the students since Day 1.

We asked for feedback from our students on what worked and what did not in regards to the CompTIA Linux+ materials. We got the following:

*  Focus on Activity Section of the Study Guide
* Do the virtual labs repeatedly
* Going through the practice exam is not effective
* Watch ITPro.tv videos (which we were not able to provide that time)

I did not study for the Linux+ Exam for several months as I focused on learning the MEAN Stack (especially the Angular front end framework). I regularly tackled leetcode coding challenges to prepare for software developer job interviews. 

I was also finishing my capstone project: [_Software Documentation and Architectural Analysis of Full Stack Development_](https://www.freecodecamp.org/news/cjn-understanding-mean-stack-through-diagrams/), and teaching two classes: Information Systems, and Data Management Communications and Networking.

> No time... no time at all... or was it just excuses?

When I was nearing the end of my last quarter, I felt guilty and started studying again for the Linux+ Exam. 

> This time, a new plan of attack. 

I started reading the eBook again from top to bottom. What was different the second time around was that for every theory, definition, command, option, subcommands, etc. that I'd encounter, I would create a flash card in Trello (available [here](https://trello.com/b/viGl7wam/linux-prep)). I used this to train with friends to do a pop quiz and execute commands in the Linux terminal as well. 

On my own, I would have my own Linux environment following along with the Activity Section of the eBook. This really helped me retain my knowledge on Linux commands and configurations. I also incorporated using Linux commands in my personal laptop with MacBook Pro, as MacOS has Unix-like terminal.

I utilized the CertMaster Practice Exam again. And this time, I had a friend to go over and discuss why each choice was right or wrong, using the process of elimination.

> It seems like doing hands-on and having a discussion with a friend truly helps you master a topic.

I really didn't like the CertMaster Labs and did not use it during my study.

### I hesitated to study the following: 

* bash scripting - I'm a software developer and I know how to code already. I have built bash scripts to boost my productivity, from class notes to web applications.
* version control - I've been using git and GitHub in my classes and personal projects.
* containers and orchestration - I have a good foundation as I've been reading DevOps books.

## The Binge-Worthy ITPro.tv Videos

> I accidentally discovered it. It was timely and effective.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-304.png)
_where you can binge-watch IT videos_

At the start of April 2020, we got news of incoming AAP students. The Dean asked me to check the CompTIA store again for materials, and find out what these ITPro.tv videos were all about. 

At first, I was reluctant to even purchase the videos because I remembered the CompTIA Study Guide having the ITPro.tv logo at the start of their videos. I started calculating the total hours of the CompTIA Study Guide videos. The total duration was only 22 minutes. 

This was a big difference compared to the standalone ITPro.tv videos with 16 hours of content. I went ahead and purchased it (with reimbursement of course).

And boy, I did not regret it. Those videos were fantastic. They dove deeper into the topics and explained the commands throughly with the help of a co-host to ask why we needed to use those commands. 

The average duration of a video is about 15 minutes. A big contrast compared to the other resource, which averaged about 2 minutes per video.

I started picking videos to watch based on the topics that I knew I couldn't explain to anyone. I combined this strategy with the multiple-choice-on-steroids CertMaster Practice to fill in my knowledge gaps.

In the middle of April 2020, I scheduled my CompTIA Linux+ Exam Online Testing. They created the online testing environment due to the pandemic. As it was nearing the scheduled date, I relaxed my study patterns and limited myself to watching the ITPro.tv videos.

## Exam Procedures

The online exam requires you to abide by the following procedures:

* have an internet connection
* have an external webcam or laptop webcam
* have an external microphone or laptop microphone
* have a photo of valid ID
* have pictures of your front, back, left, and right of your own testing environment
* No headphones, and smartphones and electronics should be out of reach

View the full details [here](https://www.comptia.org/testing/testing-options/take-online-exam).

## Exam Time

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-308.png)
_instagram post of my ever supportive partner_

> I totally appreciate the support!

### My Experience with the Online Test App

* The exam was scheduled 12:15 midnight. This was my intention to avoid any noise in the house. 
* The proctor can see you through the webcam, and you can't see them.
* The online testing app slowed and crashed several times. The proctor said it was due to the high volume of test takers.

### What I felt during the exam

The first few questions I got in the exam were Performance-Based Questions. It was freaking hard. I really couldn't answer with 100% confidence. I encountered a problem using Linux commands _grep_ and _awk_ with piping to another command. 

Another problem was about investigating an SELinux policy violation, which requires you have to inspect each command and their respective output to pinpoint which file or directory needed additional configuration.

> If only I had that professional experience, this would have been much easier.

As I went through more questions, I really felt so dumb and lost my confidence. I didn't know how to answer the questions about network, system, or user configurations. In the bash scripting portion, I knew I wasn't really good at RegEx (regular expressions). 

> I had 30 minutes left in my exam and felt like failing...

My thoughts of plan B were coming back – I would just take the exam again. This was partly due to my own perspective in life. I always tell people I'm used to failure and I'm fine failing as long as I can be persistent until I reach my goal. 

Around the 28-minute mark I was about to call it quits, when I heard another voice in my brain (I'm not crazy I tell you. It's the Jedi Mind trick, read _[How to teach yourself to learn again](https://www.freecodecamp.org/news/cjn-how-to-teach-yourself-to-learn-again/)_). 

> The voice said: "don't think about failure now, use the remaining minutes and do your best!"

So I used the remaining time to jump around to different questions until I'd covered them all. This time with more focus. I changed almost 80% of my answers and I started to do the following strategies to increase my chances of getting the right answer:

* Process of elimination - I removed choices that I knew were totally wrong.
* I stuck with what I knew - I didn't choose an answer if I didn't know what it meant.
* Deeper focus - I read word by word and tried to use both comprehension and logical thinking.
* Eyes closed, mind opened - I convinced myself that I'd studied really hard for this exam so it must be stored in my brain somewhere. With that in mind, I tried to retrieve those memories to achieve 100% confidence in some questions that I had around 70% confidence answering.

I kept repeating these strategies until the last minute. 

## Exam Results

The exam ended and I passed – 739 out of 1000! A passing grade point is 720. After 30 minutes, I got an email from CompTIA.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-312.png)
_my cool instagram post celebrating my achievement_

I will still be humbled and say to people that I got lucky. But for myself, I won't say I got lucky because I changed most of my answers using a better mindset and more effective strategies.

## Lessons Learned

* I should really stop taking these exams when I don't have professional experience yet. Why? I encountered the same kind of difficulty and failed my AWS Developer Certification Exam before (here's the article: _[I failed my AWS Developer Exam. What now?](https://www.freecodecamp.org/news/cjn-i-failed-my-aws-developer-exam/)_). 
* In studying, I should've done more assessment early on to focus on my knowledge gap instead of speeding through all the materials.
* During the exam, I needed to remind myself this is my reality now. What can I do to be great in this situation? This mindset is something I can apply to my current work as well.
* Remember to have study sessions with friends or colleagues, as you'll have the chance to grow your knowledge exponentially.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-284.png)
_quote from Gladiator (2000) movie_

## What now, Clark?

I rejoined CityU as a full-timer with a position of Program Manager for AWS Apprentice Program (Full Stack Web Systems Developer) last April 20, 2019. 

With the Linux+ Certified under my belt, I have gained additional experience, along with my previous experience being a TA Lead with the same program. It's allowed me to better lead, teach, and mentor the new cohort. This includes my team that includes new TAs that I know for sure will be more successful than I was.

I will do my best to keep teaching and mentoring students while sharpening my software development skills, as I'm still on a journey to find a software developer job in the tech industry. I know it's hard coming from a non-tech background to transition, but we'll all get there in time.

To my readers, thank you for reading my article. I really want to focus more on technical articles but I couldn't let a good story slip away.=)

Connect with me in LinkedIn [here](https://www.linkedin.com/in/clarkngo/).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-322.png)
_I couldn't decide on my LinkedIn headline lol_

**Article Video Summary and Q&A**

%[https://youtu.be/5evBAfJi4l0]


