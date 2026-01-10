---
title: Things I’ve learned from pair programming interviews
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T04:44:55.000Z'
originalURL: https://freecodecamp.org/news/things-ive-learned-from-pair-programming-interviews-35a4db7d7443
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P1P5XR1y56_5siutQwz0Yg.jpeg
tags:
- name: interview
  slug: interview
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eumir Gaspar

  Some companies prefer to pair program with candidates to get a feel for working
  with them while gauging their skills. I have been in a couple of those companies,
  and more often than not, one of my tasks was to be the pair in those int...'
---

By Eumir Gaspar

Some companies prefer to pair program with candidates to get a feel for working with them while gauging their skills. I have been in a couple of those companies, and more often than not, one of my tasks was to be the pair in those interviews.

In my previous job with a consulting company, we had teams for each project. Some projects had [NDAs](https://en.wikipedia.org/wiki/Non-disclosure_agreement), and as such, anyone joining that team had to sign in. This led to difficulties in using those codebases when pairing with potential employees. As a result, we mostly paired on either internal projects or on projects where the client was okay with showing code to candidates.

I was usually on the teams with no NDAs, so whenever we had candidates, I was the main pair. Being in that company for five years, you can only imagine how many candidates there were. There were times when, during my work week, I was pairing with a different person each day!

![Image](https://cdn-media-1.freecodecamp.org/images/ywut-FyD8IRcc5ksSvQxxUjGD2cP--aWJshd)
_Photo by [Unsplash](https://unsplash.com/@helloquence?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Helloquence</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

We also do pair programming in my current company. Since I have been practicing pair programming since 2010, it has become natural to me.

**But the one thing to remember about these interviews is that it goes both ways**: the interviewer learns about the interviewee’s skills and personality, while the interviewee learns about whom they will be working with and what a typical work day looks like.

So here are the lessons I learned from pair programming interviews, both as the interviewee and interviewer. Hopefully this will help you have a better idea for your next interview.

### Be prepared

If there’s one thing that you can take away from this, please let it be this one. It may seem obvious that, as in any interview, you **HAVE** to be prepared — but I just felt that I needed to emphasize this point.

**As an interviewer**, look through your candidate’s CV, résumé, or source code if they have submitted it. This will help you set your own expectations for their skill level and personality, which will help when communicating with them. Knowing that you have the same hobbies could be a good ice breaker!

**As an interviewee**, go to the company’s website and read / click through. I have been in a situation where I applied as a web developer, and the first question thrown at me was, “So, have you seen our website? What do you think can you do to improve it?” Suffice it to say, I botched that interview. So please, at the very least, have a look at their website. Review your code if you submitted it and double check everything.

### Relax and be yourself.

This may sound like generic advice, but it is much more important for a pair programming session compared to a general or technical interview. Why? Simply because, in some general interviews, an HR person talks to you and gauges your personality for the duration. While you would be in the same company as they are, you won’t be directly working with them every day.

In a pair programming session, if the company does pair programming most of the time anyway, you would likely be working closely with your interviewer as part of your job. That is the main difference.

This works for both the interviewer and interviewee. Like in any relationship, it’s hard to have a long term relationship if you build it based on only part of the picture. Your foundation will be a shaky ground of uncertainty, and sooner or later it will come out and might result in some problems.

### Ask questions!

**As an interviewer**, be aware that most of the time the candidate will be nervous. While asking too many questions can potentially scare them away, not asking any questions puts you in the dark and wastes your day of pairing.

I’ve learned to list down a set of questions that I get to ask during the day of pairing. The list does not have to be in order, and you do not have to ask them all in one go. Most of the questions will come up while you are pairing, but it’s best to have them written down just in case.

**As an interviewee**, remember that some interviewers EXPECT you to ask questions. Not asking means you are not interested (why are you applying anyway?) or you know everything (which you don’t).

Whenever I pair with someone, I take note of when they ask a question and how often. Questions can range from simple syntax questions like “What was the first argument for `each_with_index` again?” to work-related questions like “Do you usually pair every day?”

### There are no right or wrong solutions

For me, it’s just a matter of getting the job done. While I expect candidates to be at their best, I do understand that they will be nervous which might slightly affect their thinking.

I mean, having mental blocks during an interview is pretty common (at least for me). I’ve paired with a range of people from new grads, to juniors, mid-level developers and even seniors, and I myself sometimes black out.

Case in point: when I was being interviewed for my current job (I already had more than six years of Ruby experience at that point), I was chugging along with a simple exercise and I totally forgot how to create a `Hash`. Like, I just went, “Um. Wait how do I do that again? Um, can I Google something?” Pretty embarrassing, but when I asked, my pair also just blanked out so we both Googled it together. Fun times.

![Image](https://cdn-media-1.freecodecamp.org/images/2X5hh9vayh8zpNssY2faVijPDvEfEg40Tm5b)
_Photo by [Unsplash](https://unsplash.com/@punttim?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tim Gouw</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

**As an interviewer**, don’t be stuck to the notion of your own solution to a problem. There are 11287398173 ways to write FizzBuzz and your solution is (probably) not the best one there is. Instead, be more open to other solutions and judge them as best you can.

When I do pairing interviews, I usually have an answer in mind when I ask a question, but I listen and see what the interviewee’s answer is, because it is almost never the same answer as mine. You’ll be surprised at how creative people can get!

**As an interviewee**, be aware of this fact and just do your thing. Don’t get stuck worrying that you won’t be efficient (unless that was the interview question!) but at the same time, don’t be sloppy. If you come in to a pairing session for a company that does [TDD](https://technologyconversations.com/2013/12/20/test-driven-development-tdd-example-walkthrough/)/[BDD](https://en.wikipedia.org/wiki/Behavior-driven_development), for your sake, start with tests first! They will be looking for that (I do!) and you could end up at the bottom of the pile if you just smash things out.

### Treat this as a normal pairing day

Based on my initial experience, I treated it as a technical interview. I sat beside the candidate and took notes while they typed out their thoughts.

But this is NOT how I usually pair, and when I realized that, I changed my ways. When someone was stuck, I would nudge them along without exactly giving the answer. I’d ask some probing questions like “What is the error message?” or “What do you think is the problem?” or “What could you do to fix it?”

**As an interviewer**, let your candidate drive 90% of the time — but never 100%. That gives off the impression that it is a stricter tech interview (you’re just beside them looking at their every move — which actually makes concentrating harder). Have a go with the keyboard a bit and let them talk you through their solution. This will put them at ease.

**As an interviewee**, don’t just start typing the moment the keyboard is given to you. Start discussing your solution first. Ask your partner if they want to have the keyboard while you let them know your thoughts. Remind yourself that this is more of a pairing “test drive” instead of a tech interview. Which brings me to the next point …

### Talk to your partner

![Image](https://cdn-media-1.freecodecamp.org/images/EKqRVi430sijnizB8oOYok095A4cOqNlAldh)
_Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel.com</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

This is the first thing I check when I do pairing interviews. In my previous company, I usually started the day by explaining what the app we’re working on does, what the feature I am working on is, and what we’re supposed to do. I then started typing out my specs and let the candidate have the reigns.

I would pay attention to see what they did: sometimes they just went ahead and started typing, others they would think silently first, and still others would straight up ask questions about the problem or let me know their solutions.

In my current company, the pair session usually focuses on a given problem. I give the candidate the problem to read and then I wait. If they start typing without saying anything, that is already a red flag for me. I give points to people who get a pen and paper and start explaining their solution to me with diagrams.

**As an interviewer**, it is important to keep the conversation going to let the candidate feel that it is a pairing session. At this point in time, you two are a single unit. You should both be able to communicate well with each other and bounce ideas back and forth.

Of course, there will be times your candidate will need to think by themselves, so let them have that as well. Find the balance between keeping up the conversation and letting them focus and solve the problem.

**As an interviewee**, always let your partner know what you plan to do and what your solution is. This lets them know that you recognize the fact that this is a pairing session and that you can communicate your ideas well. This also gives them the feeling that you plan things carefully, instead of [going YOLO](https://hackernoon.com/could-yolo-driven-development-be-a-thing-fa1c12242188).

### It’s okay to take a moment to think

In contrast to the above statement, you also should be able to have the time to think silently. It is absolutely okay to have [dead air](https://en.wikipedia.org/wiki/Dead_air). You are not in a radio station after all.

**As an interviewer,** you will rarely have to do this. But if you are in my situation, where you are pairing with a candidate on a feature you’re actually implementing, then you too will need time to think. Just let your partner know about this and it should be fine.

**As an interviewee**, you can let your partner know that you will need a bit of time to think and that you will let them know your solution after. This shows that you are acknowledging their presence and that you will be communicating your thoughts after you process them. Communication is key!

### Final thoughts

These are just some things I learned. Hopefully they can help you in your next interview. While this is not a comprehensive list about how to ace a pairing interview, I think that it can help candidates (and first time interviewers as well!) in their interviews.

Good luck! And also remember that no matter what happens, you will come out of that interview having learned something — and that is what matters.

