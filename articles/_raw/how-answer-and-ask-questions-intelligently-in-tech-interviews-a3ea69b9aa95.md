---
title: How answer — and ask — questions intelligently in tech interviews
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T16:18:44.000Z'
originalURL: https://freecodecamp.org/news/how-answer-and-ask-questions-intelligently-in-tech-interviews-a3ea69b9aa95
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mCXazFWNUP5dbZVQtz1c2Q.jpeg
tags:
- name: interview
  slug: interview
- name: jobs
  slug: jobs
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Salma Elshahawy

  Everyone likes to hop from company to company to find the best position that fits
  them. Currently, I am applying for jobs in companies that have a culture of work/life
  balance.

  I applied for a position as a software engineer at X-c...'
---

By Salma Elshahawy

Everyone likes to hop from company to company to find the best position that fits them. Currently, I am applying for jobs in companies that have a culture of work/life balance.

I applied for a position as a software engineer at X-company. They were the most professional company that I have ever interviewed for. The interviewer was well prepared and left adequate time in our meeting to exchange questions.

In this post, I will share the questions the interviewer asked me (mixed types, behavioral and technical questions). Also, I will share the questions I asked him when it was my turn to ask him some questions.

I decided to document this interview because I believe it was a valuable experience in the technical and behavioral interview. Maybe it will help other engineers to get an idea of how to respond to those kinds of questions.

### Q1: Tell me about yourself

This type of question is asked so you can express yourself in brief and get the full attention of your interviewer. So, you have to practice answering this question before experiencing it. I prefer to write an abstract summary about myself and practice saying it in a maximum of 30 seconds or an elevator pitch.

A1: I am a software engineer with a mechanical engineering background. I am passionate about cleanly written, organized, tested code. I have experience in scripting and functional languages.

I built many SaaS applications including authentication, authorization, and secure payments. I discovered coding through my previous career where I built applications to help in the design process.

Now, I am looking to contribute my range of skills to a team that needs a dedicated performer with a broad grasp of technologies.

### Q2: Describe a situation where you didn’t have any resources, and you had to deliver a fully developed feature in a specific time frame

For this type of question, you have to explain three things to the listener — the issue, the solution, and the action — as a story.

A2: I was supposed to deliver a feature for a sprint in two weeks as a demo. The user story for the task wasn’t clear and not decided yet. Additionally, the product manager was a new hire and had no idea about the suggested feature. Meanwhile, I didn’t have enough resources to identify the inputs, outputs, and dependencies.

Hence, I decided to talk to the product manager and my team leader to brainstorm ideas about shaping a basic user story that could simulate the functionality. We had a user story approved by the product manager. Finally, I started writing business logic that implemented the feature.

### Q3: Tell me about a situation where you had to escalate the issue to a higher authority than you

A3: I had to write unit tests for another developer’s business logic to increase the coverage. There was a bug in the code which caused the unit test for a particular block to always fail.

I started a debugging session to find out where the bug was so I could fix it. I found the bug — a database query. I checked for the feature owner and sent him a detailed email about the problem to fix it. He responded that I had to adjust the unit tests to the code that already existed with the bug because we had a sprint demo the next morning. He wasn’t sure if he could fix it before that.

In that situation, I decided to escalate the issue to our team leader — writing unit tests for a bug is like driving a car in reverse. Our team leader investigated the matter and asked him to fix the business logic.

### Q4: How do you make sure that the instructions given to you are precise and correct?

A4: I can make sure that the instructions are correct by audit and scrutiny. For instance, when I need to learn a new thing from a written tutorial, I try to check the output at each step that I did to make sure it matches what is written in the tutorial.

### Q5: How do you make sure that your data is successfully stored in the database?

A5: There are several ways to do that. I can use a helper method to check that piece of data in the database. If it exists, put a flag and set it to true, else set it to false. Maybe different ways are smarter than this one, but I prefer the visual confirmation.

### Q6: How do you make sure that the output is the exact output in the user story?

A6: When I have my assigned task, I draw a visual flowchart that demonstrates inputs, outputs, and dependencies to make it easy for me to catch up quickly in case I get distracted by other things. Additionally, it will be easy for someone else who isn’t familiar with my business logic to help me in a situation where I get stuck.

### Q7: Tell me in detail about a situation you’ve countered when you decided you should stick to the company’s policy?

A7: I haven’t faced such a situation in my personal experience, but I have seen it happen to one of my team members. He had to make an invocation to an external service to test the business logic and make sure that he got the desired output. To make that external call, you should have a certificate to enable a proxy that will redirect you to external sites. My colleague waited for permission according to the company policy.

> **The interviewer then asked me if you were him, what you would do until you got the permission?**   
> If that happened to me, I would prefer to help other people in their tasks, as I hate to sit around without doing anything.

Then, the interviewer thanked me for my responses and told me that he was ready if I have any questions for him. I believe that the interview is a two-way process. I did my homework and prepared some questions that could help me understand the company culture and if it was a suitable fit for me.

> Note: It is crucial to prepare at least two questions from the job description that are meaningful and thorough that indicate your interest in working on that position.

### Q1: What are your performance metrics that you use to judge if a project/sprint has completed or failed?

In that particular question, I was looking for their quality in implementing features. Do they care about only making a sprint pass or do they care about quality?

### Q2: How do you estimate tasks? And who does the estimation?

I wanted to know if they pushed developers and gave them tasks without asking, or if they didn’t care about a practical time-frame.

> The tasks estimation can be done theoretically using a simple Fibonacci number with a collaboration with developers estimate — mixed between theoretical and real.

### Q3: Who supports project documentation? And How often do they update it?

Here, I wanted to make sure that if I got that job, I wouldn’t be stuck waiting for other people to mentor me and walk me through the project to get familiar. If there was well-written documentation, it would be easy for me or anyone to catch up quickly without pain.

### Q4: What tools do you use to profile your software/project?

Profiling software is necessary because it does two significant things:

1. Bugs can be found early before deploying to the production environment — saves a lot of time.
2. You can optimize your application easily.
3. You can explore the complete flow of the software including database calls, etc.

So, I believe that if they have such a tool, they are a professional company, and I have an opportunity to grow my skills.

> An example of profiling software is [Miniprofiler](https://miniprofiler.com/) for both Ruby and Node.js

### Q5: Do you have any test coverage statistics tools?

My aim with that question was to see how much they care about the code quality. These tools show in detail the coverage for line coverage, which means writing essential test cases.

> Anyone can write code, but good developers care about test cases before they write any line of code. I care about quality.

### Q6: Does your company launch tech talks periodically?

I was curious about whether they care about their developers concerning career growth and improving their engineer’s skills.

### Q7: How flexible is the work schedule? Do you have WFH days?

This questions reveals a lot about the work environment. It gives you a clear picture of what type of company it is. I asked that question after several technical ones to prove myself first to the interviewer. Have their respect first, then ask those personal questions.

### Q8: What do you especially like about the company? And what do you love about your team?

I wanted to see if he likes working at the company or not. As an interviewee, you can know this easily from their tone — either they are happy or neutral. The excitement in the answer will guide you whether this company deserves you or not.

### Closing notes

Leaving a good impression on your interview is imperative. That will make sure your interviewer never forgets you. The conversation is a chance to learn new things from your interviewer. Ask smart questions that will leave a positive impression and will let them know that you will be an added value to the team. Keep asking as long as you have the opportunity. I hope my experience can help other developers in their interviews.

Finally, if you liked my post, please follow me here on [Medium](https://medium.com/@salmaeng71) or leave a comment. You can follow me on twitter [@salmaneg](http://twitter.com/salmaneg). Thanks for reading and good luck with your job hunting!!!

