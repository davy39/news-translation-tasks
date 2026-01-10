---
title: Learning to code? First, learn to solve the problem.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T18:37:53.000Z'
originalURL: https://freecodecamp.org/news/learning-to-code-first-learn-to-solve-the-problem-128475b91301
coverImage: https://cdn-media-1.freecodecamp.org/images/1*90OqH2-MZ4cdAHmbOgStrQ.jpeg
tags:
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Geshan Manandhar

  Most of the tutorials you have read or watched before now usually do one thing,
  spoon-feeding.

  This is “OK” to learn a new thing, but not good when you need to solve a real task.

  A task usually involves reaching a goal by overcomi...'
---

By Geshan Manandhar

Most of the tutorials you have read or watched before now usually do one thing, spoon-feeding.

This is “OK” to learn a new thing, but not good when you need to solve a real task.

A task usually involves reaching a goal by overcoming a problem. This post unveils the most important “tip” for all beginner software engineers.

#### TL;DR

> _First, solve the problem. Then, write the code. — John Johnson_

In other words, work the solution out on paper in steps. Then start writing the code for it. Don’t get tangled in the code and software design first.

### So, what happens?

Many times I hear beginners and junior software engineers say: “I could follow the tutorial and thought I understood the concept. But when I tried to do a similar thing on my pet project, I could not do it.”

This happens for two reasons.

First, you lost your train of thought somewhere and could not establish a chain.

Second, you were so tangled in the code that the main problem you were trying to solve fell out of focus.

This problem also happens for Software Engineers and even Senior Software Engineers.

The good thing is that with experience, you know when to stop or take a break. Then, come back to the problem with a different prescription and find a solution faster.

Many of you can relate to this: You were trying so hard to fix an issue for hours. You took a break or slept over it, and next session the solution was there in minutes.

This is not magic. This is looking at the problem from another viewpoint.

### Let’s illustrate with an example

You have to do a task — for example, create a refund with payments.

You are given the database schema. This is a back-end task and you need to create a POST /refunds API that can create the refund and its related payments. The database structure is as below:

![Image](https://cdn-media-1.freecodecamp.org/images/0*DBOwDM4Gq6DJ00sg.png)

A refund always has a reason, such as ‘damaged goods’ or ‘late delivery’.

You could discuss the API payload with one of the team members. You might agree on the below JSON payload:

#### The usual scenario

What most beginner software engineers will do is start scanning the codebase, if there is one. They will immediately start writing some code. If there is any testing culture in place, maybe they write some automated test code.

This is where most beginner and even some experienced software engineers slip. **Don’t write code when you have not solved the problem.**

#### The appropriate step

The most appropriate step is to sit down and solve the problem on paper in steps.

So you ask yourself what you need to do. You come up with a plan in steps and tweak it.

If you have someone senior in your team, you can validate your steps and get feedback.

This will also decrease the code review time. Both of you have already agreed on the modality of the solution.

#### So how to do it

The task described earlier is to write a create/POST API where Refunds with payments can be created.

Each refund can have a maximum of two payments. One is of type ‘cash’ and the other is of type ‘credit’. It can also be one refund with only one payment of either cash or credit. This is how I would have written the following steps on paper:

1. Create a method to get the data from the controller sent by the user
2. Validate all the input for values, refund types, and reasons.
3. If all validation passes, generate a random alphanumeric number of length 10 which is not existing in the refund table (recursive check)
4. If validation fails to respond with a proper validation failure message, decide on response structure
5. Start a database transaction
6. Insert the refund related values of `refund_nr`, `reason_reason`, `is_premium_customer` to the `refund` table
7. On insert success, get the id of the last insert
8. With the refund_id, insert payment related values of fk_refund, fk_item, amount, is_cash to the `payment` table
9. If all went well commit the database transaction
10. If there was any issue, rollback database transaction
11. Respond with success or failure message depending on the database transaction’s success with proper structure
12. Wire up the controller and this method

### Follow the plan in steps, now write the code

After you have a step by step plan you can start writing code. Then, you can go more in-depth on the method names, how to get the database connection and other details.

Depending on the language and framework you can also decide where should the validation code stay.

You could even write tests if the company and culture supports and encourages it.

When your solution is evident in your mind and you have a step-by-step action plan on paper, you can now write code.

You can even break up the parts in ways that will be easier to finish and wire up.

For example, the testing logic can be something that can be written separately and tested on its own. It is thinking about independent parts that can be wired up together to form the solution.

### Conclusion

When you face your next task, don’t start writing code from the get-go.

First, get a hold of the problem then devise a solution with steps. This is best done away from a screen on paper.

Then, refine your solution and discuss with someone. When you are satisfied, translate that solution to code. This is a bit methodical but very effective.

> Code is always a medium to the solution, not the solution itself.

You can read more of my blog posts _at [geshan.com.np](https://geshan.com.np/blog/2018/12/the-most-important-tip-for-beginner-software-engineers-is/)._

