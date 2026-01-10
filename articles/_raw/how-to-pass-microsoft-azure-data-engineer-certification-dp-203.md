---
title: How to Pass Microsoft’s Azure Data Engineer Certification – DP-203 Exam Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-19T16:02:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-microsoft-azure-data-engineer-certification-dp-203
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/ux-g6bea5bfef_1920.jpg
tags:
- name: Azure
  slug: azure
- name: Certification
  slug: certification
- name: data-engineering
  slug: data-engineering
- name: Microsoft
  slug: microsoft
seo_title: null
seo_desc: "By Ryan Dawson\nData Engineering jobs are in high demand. And getting a\
  \ certification in the subject is a good way to learn and to deepen and prove your\
  \ skills. \nEach cloud provider offers a certification specialized to their Data\
  \ Engineering services..."
---

By Ryan Dawson

Data Engineering jobs are in [high demand](https://insights.dice.com/2019/06/04/data-engineer-remains-top-demand-job/). And getting a certification in the subject is a good way to learn and to deepen and prove your skills. 

Each cloud provider offers a certification specialized to their Data Engineering services. They carry weight but are not easy to pass.

The Azure DP-203 is a pretty tough certification to pass. I spent about 20 hrs on an online course, 5hrs on practice exams, about 5 hrs reading, and another few hours figuring out what tools to use, how to sign-up, and so on.

My aim was to get to a pass quickly and I think it can be done quicker than I did it. Here are some tips on getting your Microsoft Azure Data Engineer certification as quickly as possible.

# Pre-requisites

I have background in data engineering but I don’t think it’s required. If you don’t have this background then I’d suggest a [short primer](https://www.xplenty.com/blog/etl-data-warehousing-explained-etl-tool-basics/) on key Data Engineering concepts (OLTP vs OLAP, data warehouses, and data lakes). 

I was also very familiar with cloud computing before the course but not especially familiar with Azure’s core services. If you want a primer on cloud computing then [Microsoft has one](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/).

# How to Study for the DP-203 Exam

### Online Courses

I used a [Udemy course](https://www.udemy.com/course/data-engineering-on-microsoft-azure/) by Alan Rodrigues to work through the content. I liked that it showed the tools in action, illustrated the concepts, and contained exam tips and practice tests. 

There is [official content from Microsoft](https://docs.microsoft.com/en-us/learn/certifications/exams/dp-203) and that looks good too. The official content is a mixture of text and video with more weight towards text, whereas courses like Udemy (and there are plenty of them) are mostly video. 

I would suggest to just pick whatever you like the look of and try not to overthink the decision.

### Books

I also bought a book to read on my kindle but I didn’t get much value from that and would say a course is enough. 

I’d suggest checking when any material was last updated before choosing it, as the course content does change over time and books can get outdated quickly. I do find it helpful to have reading material to complement a course, I think I just didn't pick the right book for me this time.

### Getting Hands-on

Microsoft, on their website, points to an option of instructor-led training but I didn’t do that. I also didn’t do any practical labs in the course that I worked through. 

[Others do recommend](https://dhyanintech.medium.com/how-to-prepare-for-the-azure-data-engineer-associate-certification-4cf122f1937f) getting hands-on. I suspect it depends how much background you have and whether you feel confident that you’ve grasped the material just from watching instructional content. 

Some people take notes while watching videos to help organise thoughts and make sure they’re understanding. I didn’t take notes either, though I have on previous courses.

# How to Practice for the Exam

My top tip is to use the [official practice exam tool](https://uk.mindhub.com/dp-203-data-engineering-on-microsoft-azure-microsoft-official-practice-test/p/MU-DP-203?utm_source=microsoft&utm_medium=certpage&utm_campaign=msofficialpractice). It is worth the cost.

I used practice tests on Udemy and they were helpful. But with those you don’t get feedback until you’ve completed the test. 

When learning I prefer to find out what I’ve got wrong straight away. If I don't find out the answer until the end of a test then I have to remember the context of the question, which involves more effort. I also want to ensure that what lodges in my brain is the right answer and not the wrong one. For that it's better to be corrected quickly.

### Features of the Official Practice Test

The official practice test lets you choose test lengths for however long you’ve got to practice at that moment. You can configure whether it tells you answers straight away or at the end.

![Image](https://lh5.googleusercontent.com/gvuQ1De2BRHBvvXQbJkn6RRXM7EoSA34WPZpxQmO_6VLx-F-toNyLWgjifowqJRyWKEJ2m5A_aaUJ5q7OUu-NWdSeft1xpugLzYi3IIM9XjOgTEbGgvsUUKXmEBnAP4hKm5b_eAP=s0)

The format of the questions matches the exam, which you don’t get with all of the practice exam sites. The exam has some multi-part linked questions and a lot of sites aren’t able to do that.

### Getting Started With the Official Practice Test

The flow to buy and login to the practice test is a bit confusing. You click through from the Microsoft website and buy it from a third-party vendor ([in the UK, where I am, this is mindhub](https://uk.mindhub.com/dp-203-data-engineering-on-microsoft-azure-microsoft-official-practice-test/p/MU-DP-203?utm_source=microsoft&utm_medium=certpage&utm_campaign=msofficialpractice)). But you don’t need a login there and if you do create one you can’t use it to login to the test. 

Instead you login with your Microsoft or GitHub identity to [marketplace.measureup.com](https://marketplace.measureup.com/login) and register a key from the purchase.

### Practice Test Books

I also used a book of practice questions and answers. That way I could do some exam prep away from my laptop. 

There’s several of these books out there and I suspect they’re pretty similar. They’re not as good on quality as the practice test. I found errors like an answer section following a different question than the one it belonged to (which may be a kindle thing). The explanations also aren’t as detailed but it’s still helpful. 

The one I used had a format of question and options on one page and then answers on the next. I would recommend using a book like this.

### Topics I Targeted

There are certain topics that it’s worth getting clear about because it seems to me like they come up a lot and the questions are mostly of a similar format. The ones that stood out for me are:

* Storage tiers. If you know hot, cold and archive you’ll get some marks.
* Star schema.
* Slowly changing dimension types. Wikipedia explains this well.
* Distributions for Synapse dedicated tables. Expect to get asked a question with a big Fact table and small Dimension tables. The dimension tables will want replicated distribution and the big fact table will be hash-distributed with hashing on some foreign key type column used in joins.
* Difference between Synapse (warehouse with some added processing features), Stream Analytics (real-time processing), Data Lake (large-scale unstructured storage), Data Factory (ETL) and Databricks (managed Spark plus notebooks, ML and delta lake).
* When to use Parquet, Avro, Json and CSV formats. (The answer is almost always that parquet is best for querying data at scale but they also like to make sure you know avro is good for timestamped data.)
* The syntax for writing to a file or stream using Spark.

For me these were topics I felt I could bank on. There were other topics I was confident about after practicing, but for some topics there’s lots of different ways the questions can be approached. For these I felt I could see the patterns and they were fairly predictable. It’s reassuring to have some questions you can do from memory without having to think a lot.

### Learning to Analyse Questions

Learning how to read and analyse the questions is a skill. Often the questions contain some incidental detail around a scenario (for example, the fact that it’s a grocery company) and some clues that point to an answer (for example, the size of their sales transaction table). 

I don’t always recognise where a question is going from a first read, so then I find it useful to quickly scan the answers. This is dangerous, though, as then you might find something you recognise and match it to a clue and jump on that. But the questions can require picking up on multiple clues. 

You want to eliminate the wrong answers if you can (which is tricky if you try to go fast). Sometimes there’s also multiple right answers to select and you’ll miss marks if you choose just one when there’s two correct selections (the questions do tell you when you should select multiple but it’s easy to miss if you rush or get tired). 

This is why I recommend the official practice exam tool – it’s great for learning the format of questions and the skill of how to read them.

# When to Tackle the Real Thing

### Can I Learn It All?

The scope of the exam is so broad that it’s hard to really know everything. You’ll even get occasional wildcard questions that bring in Azure services that don’t relate to data. 

When that does happen and you don’t know about those services, you can typically guess your way through it so long as you’re clear enough about the data services.

Cosmos DB is a new part of the Azure data stack. It’s not explicitly part of the syllabus right now but the exam scope is broad and it does creep in. It’s worth knowing a little about it but don’t get sucked into learning all its ins and outs.

If you try to really learn everything that could come up then you’ll have an awful lot to learn. 

Databricks is huge in itself. You don’t need to know any of the Databricks machine learning stuff. You basically just need to know about setting up clusters, working with files in Azure storage using Spark, authentication and differences between Databricks and other Azure services that happen to feature flavours of Spark (Synapse and HDInsights).

### So When Am I Ready?

If you’re doing well consistently on practice exams, you’ve developed a knack for guessing and can make the guesses pretty quick, then you’re ready to give it a go.

But it’s also about your comfort level – don’t let me (or anyone) rush you into doing it before you feel ready.

# How to Tackle the Exam

### Structure and Timing

You don’t get much time per question. For me it was 65 questions in 100 minutes. The total exam time is more than 100 minutes but 100 minutes is the time you get for answering questions. 

Some questions are more than one mark per selection in the answers so the number of questions you get can vary (I believe with the number of marks available staying the same). 

Basically expect to answer roughly one question every 90 seconds or so. But don’t worry about time while first practicing. You’ll get faster with practice.

I actually didn’t finish all the questions. I thought I had finished after about 60 questions and started reviewing answers. Then I realised I had to click through to a separate case study section. This happens right at the end, and although there is guidance I didn’t find it super clear. I didn’t miss out on many marks from it though as it’s not a big section.

### Online Proctored vs Test Centre

Traditionally these kinds of certification tests were taken in test centres under supervision. Now the online proctored versions are popular. This was my first online proctored exam.

When I first looked at the guidance on online proctored exams I thought it sounded complicated. I knew that at a test centre there would be someone in the room the whole time and they'd be watching in case anyone had snuck in notes. I kept wondering how you can replicate this in an online proctored exam?

There are some instructions for the online proctored test about keeping your room clear and showing that you don't have any notes. These confused me and for a while thought I would need to buy an extra webcam to show that my room was clear and that I didn't have any notes at any point. 

But it’s actually much simpler. I only needed to take photos of the room (using a link that gets sent) at the beginning and stay on my main webcam (a built-in one was enough). So it's just a check of the room at the beginning and then you just stay on webcam.

## Good Luck!

I hope this advice is helpful to you and I wish you good luck! Feel free to ask me questions [via Twitter](https://twitter.com/ryandawsongb).

