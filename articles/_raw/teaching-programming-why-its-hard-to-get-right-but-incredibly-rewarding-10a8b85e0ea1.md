---
title: 'Teaching programming: why it’s hard to get right, but incredibly rewarding'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-08T17:58:03.000Z'
originalURL: https://freecodecamp.org/news/teaching-programming-why-its-hard-to-get-right-but-incredibly-rewarding-10a8b85e0ea1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UvcfCAdCIgssSYCSSykrMw.jpeg
tags:
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kristian Freeman

  Over the past year, I’ve had the opportunity to teach programming in a couple of
  different contexts. Towards the beginning of this year, I ran a few sessions of
  a small meetup in Los Angeles, and spoke at a larger, more organized ...'
---

By Kristian Freeman

Over the past year, I’ve had the opportunity to teach programming in a couple of different contexts. Towards the beginning of this year, I ran a few sessions of a small meetup in Los Angeles, and spoke at a [larger, more organized meetup](https://www.meetup.com/socal-react/events/240559282/).

In the second half of the year, through my training company [Bytesized,](https://bytesized.xyz/) I’ve taught a few two-day and four-day comprehensive programming courses, specifically in React and JavaScript. They’ve been incredibly fulfilling experiences, and the primary reason is that _seeing people learn is really exciting_.

If you’re interested in teaching programming, whether as a full-time teacher, or at meetups and user groups, I want to share some of my strategies that I’ve used for teaching programming. Most of these are obvious. In my experience, they’re left by the wayside as people make easy mistakes during their instruction.

#### Sweat the lecture versus coding ratio

My rule of thumb for longer programming instruction is to divide the time you spend lecturing., and the time students spend writing code, 50/50. That is, if you talk for half an hour, introducing new concepts with slides or live demos, the following half an hour should be dedicated to the students writing code.

If you’ve ever been a student in a programming course, you know that this ratio is super important and often ignored. I’ve been in many eight-hour days in programming courses. The teacher spends most of the time fumbling through slides and showing code, but rarely giving you the chance to write code.

Note that this ratio, and this focus on exercises, is different than _following along_. Some self-motivated students will do this, but most students won’t write code unless you explicitly give them time to do it. This is an important distinction. Many students (and teachers) seem to be unaware that engagement happens when students are given “control” over their situation in the course. Even the most motivated student will become bored in a course where they don’t actually get to build things.

This ratio is a suggestion. If anything, I find that 50/50 is rare: as a course increases in length. I find it’s a great idea to shift it closer to 66/33, in favor of exercises. In a recent training engagement, I worked with a number of senior developers. They preferred to be hands-on, writing code themselves.

In this situation, they wouldn’t ask questions during the lecture, but often had follow-up questions as they worked through the exercises. In this particular session, the ratio was more tipped than 50/50, or 66/33: it was probably closer to 80/20!

#### Lead students to the solution, but let them discover it themselves

Exercises can be tricky to write. They need to reference the content that you taught. But also be “complicated” enough that students need to think about the subject, and solve accordingly.

My rule of thumb for writing exercises is to try and push students about 10% out of their comfort zone. Of course, this is hard to measure. The way this usually works out is that I’ll reference a code sample or idea from the lecture, and change it slightly (or expand on it). The students need to grasp it _beyond_ the provided lecture or sample.

For instance, in React training, I’ll demo passing props to a React component, showing a simple string value, and a boolean value:

```
<MyComponent myStringProp="Hello!" /><MyComponent myBoolProp={true} />
```

In the exercise, I’ll then ask students to pass other types as props, such as numbers, arrays, booleans, and objects. Since they’ve seen two examples of _simple_ types being passed into a component, they can extrapolate how to pass, for instance, a number. First, they might try and pass the number in a similar format to the string:

```
<MyComponent myNumValue=3 />
```

This code will return an error, because the number is “unexpected”.

At this point, the student is in a situation where they need to extrapolate what to do, based on the information given. The solution isn’t given to them — instead, the tools to **find** the solution are what have been provided. This is where the learning happens, and I find it often translates to a literal change in expression in students’ faces. Instead of being bored, they’re deeply concentrated on the problem given to them.

Given the second example, many students will then attempt to wrap the number in curly braces.

Thus, writing the correct solution:

```
<MyComponent myNumValue={3} />
```

#### Allow opportunities for “extra credit”

A well-written exercise makes it clear when a student has completed it. In my training, I provide a test suite for each exercise. Students open up the exercise directory, and run make to confirm that they’ve passed the exercises. This flow works well for students, because it’s consistent: they have a clear indication of what success looks like in the exercise.

Equally important are exercises where students can go beyond the stated requirements and explore things that interest them. Recently, a student finished an exercise with React components, and was interested in adding further customization to the component, such as passing in a font and text color.

This idea, which I hadn’t thought of as part of the original exercise, was a perfect way to further explore React components. I’ve since added it as part of the extra credit section of that assignment.

For each exercise, brainstorm one or two extra credit items that students can do to demonstrate their comprehension of the content.

I’m always surprised that many students _love_ the extra credit part of the assignments. Many software engineers are self-motivated, and love having the extra challenge.

#### Create a “from-the-ground-up” exercise

In my experience teaching React, I find that I often need to go back and teach basic JavaScript. Sometimes HTML. This means that the exercises in a training engagement often cover a broad number of topics. Because of this, I’ve recently introduced a “ground-up” exercise. This has been, a massive success. I credit it with my last training engagement being a runaway success.

Take a React training course. We’ll cover JavaScript fundamentals, writing React components in JSX. Towards the end of the course, retrieving data from the Internet.

Each of these exercises is different. By day three or four, when we’re heads-down in React code, students often forget some of the things we covered in the first couple days. For instance, using `.map` or `.find`, or handling scoping errors.

The “ground-up” exercise is designed to pull a portion of each exercise. Give students an extended period of time towards the end of the last day to _write code_.

For many developers, this is the “light-bulb” moment. This is where all the pieces that we’ve covered, some of which seem unnecessary or boring, come together.

In my React course, the “ground-up” exercise is a blog: a complete React application. First, we retrieve data via JSON (using fetch ), parse it, and display it through a deeply-nested component tree. This covers all the basis of what we’ve worked on in the training: not just JavaScript fundamentals. But actually working in a React application in a real-world example.

My favorite moment of my time training students was seeing how successful this exercise was. As we were wrapping up the final day of a training engagement, I attempted to give my last “wrap-up” lecture. Covering some extra resources for learning React, and links to contact me if the students had further questions. Instead of giving this lecture, the students requested more time for the exercise: they just wanted to keep building.

It was awesome!

#### Stay in touch

I try to build in opportunities for students to ask questions during training sessions. I’ll stop for questions at the end of each lecture. Pause during particularly complicated code examples, to ask if people need different explanations of a topic.

For some students, they aren’t comfortable speaking up in class. That’s okay! I encourage you to not force people to talk in class, if they don’t want to.

Instead, make sure to give your students the ability to reach out to you after the training. Whether via email, or an online forum. I’ve had a number of great conversations with students, whether in the form of feedback (make sure to collect feedback!) or further questions about what or how to study next. These conversations have led to concrete improvements in my training materials and presentations.

Always share your slides, and if possible, your code. My training exercises are available to all students, not just during the course, but whenever they need it in the future

Since it’s [an open-source repository,](https://gitlab.com/bytesizedxyz/react-training) they can also practice new exercises that were developed after their training session, or try exercises that we didn’t have time for. In the case of my React training, in particular, the project itself is open-source, so it would feel icky to close off the materials. I challenge you to do something similar, if your training engagements are based on open-source projects.

There’s been few professional experiences that have been as exciting and rewarding to me as teaching people how to code. If you think that you’re an effective communicator and you could be a good teacher, find a local meetup and pitch a twenty minute talk! Meetup organizers are often looking for speakers, and something as simple as _“Lessons learned building my recent project <_x>” can make for a really interesting and memorable talk.

If programming training sounds interesting to you or your team, check out [Bytesized,](https://bytesized.xyz/) my training company. Bytesized provides training in a number of programming languages and frameworks, with a focus in web development — React, Redux, and JavaScript. You can also follow me on [Twitter](https://twitter.com/imkmf)!

