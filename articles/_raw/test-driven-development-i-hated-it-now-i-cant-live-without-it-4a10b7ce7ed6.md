---
title: How and why I decided test driven development was worth my time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-12T17:05:53.000Z'
originalURL: https://freecodecamp.org/news/test-driven-development-i-hated-it-now-i-cant-live-without-it-4a10b7ce7ed6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2x368zcCx_aSL57K.
tags:
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: TDD (Test-driven development)
  slug: tdd
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ronauli Silva

  I first read about test driven development (TDD) in some technical reviews blog,
  but I barely read it (or thought about it). Why would people write tests first when
  they already knew the logic?

  So what was this all about? Writing tes...'
---

By Ronauli Silva

I first read about test driven development (TDD) in some technical reviews blog, but I **barely** read it (or thought about it). Why would people write tests first **when they already knew the logic?**

So what was this all about? Writing tests first, incrementally building the logic, and doing it in iterations. The funny thing is, when you give two programmers five minutes to code a simple fibonacci sequence and ask one to do TDD, by the end of the 5 minutes, the programmer doing TDD may say “I have test for it!” But they won’t have finished the code. On the other hand, the other one will have finished the entire fibonacci sequence and will have optimized it.

### **Why use TDD? Aren’t unit tests good enough?**

At the end of last year, I finally met TDD face to face. In a three-month bootcamp session, we were forced to always do things with TDD. I was already struggling enough, and so my brain always rebelled when it came time to write the tests.

Why should we write tests first when I can directly code the logic, my brain asked? Can’t we just write them later? After all functionality is finished?

![Image](https://cdn-media-1.freecodecamp.org/images/1*G2pGmoV1UXUH1izsziJDSw.png)
_How it looks when our TDD mentor convince us_

Let me give you a quick overview of TDD in a nutshell.

Let’s say I’m creating a fibonacci function. I might ask, what is the **simplest** assertion on a fibonacci?   
=> Returns 1 if input is 1.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uXMbt9iEYwdXCIt7ii6Zkg.png)
_Writing test first, no logic coded!_

What is the **simplest solution** for that assertion? The **simplest solution**, I mean it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qajwrX_pTW-3LDFxY_BafQ.png)

Now, next move. What is next simplest assertion for fibonacci?  
=> Returns 2 for inputs = 3

![Image](https://cdn-media-1.freecodecamp.org/images/1*vKLIf8aqUSaylG2UZvP9Zg.png)

Again, let’s fix this very quickly. Just return it and add some branching.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zU1Q78Q9v3SD6LVycIrYfQ.png)

Move to another expectation. Aim for a bigger number. Do it iteratively, incrementally.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vANcpoacacpjY-HbkpEIZA.png)

On and on it goes, until you get the nice solution for your fibonacci function. If you want to practice more, try adding memoization during the process (and don’t forget—with TDD).

Did you notice what we did there? The baby steps, your assertion, and how we define the solution? Your thought process got separated into these five critical points:

**Simple & Incremental Design —** You have to think about what is the simplest thing a particular function could do, and what’s coming next. The fibonacci example describes this point perfectly.

**Assertion —** What is your expectation of that function? And how do you describe that expectation? Will other people understand it quickly?  
Some test libraries provide you with a test description feature. That string is the only verbose thing that explains what your code is doing.

Make sure it’s a good explanation, or you’ll get a call on your holiday because your unreadable test case is failing, and no one knows why.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B7_rBZ57kOtz92rrsWW-KA.png)
_Your assertion and how you state it matters._

**Testable Design** — How should you design it so it can be testable? Take a look at these two snippets below.

The first one:

![Image](https://cdn-media-1.freecodecamp.org/images/1*VYWzFZjaMaZj1EEBZ-TKPg.png)
_Look how messy it is if your code is not testable._

By doing TDD, since you write the test first, you have to make sure that your code is **testable**_._ You can see from the example that you don’t even test your fibonacci function. Instead, you test the **side-effect** of that fibonacci logic in your code, which invokes the console.log function.

The other thing is, you never know which one is failing, the console.log() or your fibonacci block when you refactor it. In this way, TDD leads us to increase modularity in our code.

Now, let’s look at second snippet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I2U7QrcmisWipCcYd_pcUQ.png)

In the second example, we can see that we test the particular fibonacci function, not the other function that spikes on it. We are confident that the function works perfectly under the conditions that we state. We are sure that if the other function invokes our fibonacci and fails, it is not from our code.

**Negatives and Corner Cases** — what do you expect when something’s not right: is it invoked with null? Does it throw an exception? How should it be handled? What could possibly happen in the code? What could be the strangest and weirdest thing that could happen in this loop? What test can catch that?

![Image](https://cdn-media-1.freecodecamp.org/images/1*M1cysq3GcCAVSGTSyCT1Bg.png)
_How many possibilities are there?_

**Boundaries** — Should you expect that from your function? Are you sure it’s not another class’s responsibility?

![Image](https://cdn-media-1.freecodecamp.org/images/0*o6kKa-ib3wswzKqe.jpg)

### My issues with TDD

Yes, it is slow indeed. Sometimes, your time is doubled since you’re writing both tests and logic at the same time. This makes how you use your keyboard important (typing speed, better shortcut usage, and so on).

And even worse —when the requirements change—you have to refactor or delete and rewrite test code you worked hard on. Which means that tests code is code you write that is more likely to be deleted in the future. And you are doing it, iteratively. DELETES. CODES. REWRITES. AGAIN. IN A LOOP!

**Think about it. Why would you write code that is more likely to be deleted?**

“Nope, that’s enough of this TDD thing. I’ll do it when I find a strong reason why I should spend time writing code I’m likely to delete”, I said to myself.

**And that was right before I unconsciously started digging my own grave.**

### Why I changed my mind

The enlightenment came about two months later, when I was assigned to a group that did not implement TDD well at all.

I mean, they implemented TDD, **but** they left the tests broken. They didn’t bother to fix those failing test cases (which often broke because the requirements had changed). And this happened because of the most cliche reason in the world: they didn’t have time. They had to make deadlines.

After looking at the situation, I mumbled “Look, see! This TDD doesn’t work in the production world!” It made me question many things: is this TDD worth fighting for? Is TDD worth the time? Does it even deliver any business value?

After a while, I realized that the problems were growing exponentially, tasks were getting delayed, chaos was reigning, and the developer experience was getting really bad — all because they implemented TDD poorly and halfheartedly. It was **even worse than not writing tests at all.**

Here are some of the issues it caused:

* When I added a new feature or refactored things, I didn’t know whether that code was failing or not because the test was already failing.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qL_hflKv-kH7IOjxfnqQqg.png)
_We do not know which tests do I fails on, because almost all of it already failing before! -_-_

* We were forced to have high threshold on code coverage. And make no mistake, programmers are smart and **sneaky**. They write tests with no expectations, like smoke tests. And that was the **only** test they had on that particular logic. It was like, we only knew it was failing after everything was on fire. How dangerous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gq_uwGye0DYRcXA822w1fA.png)
_Always passing, anyway! All hail code coverage!_

* We used CI/CD for deployment. And we always deployed even though it was failing, which was scary: You never knew whether your production itself was failing, or if it was because you didn’t fix the tests.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g_0sJ3rQKpauqi3wuLzD0g.png)
_Test is failing, deploy anyway!_

![Image](https://cdn-media-1.freecodecamp.org/images/0*8R6C2z00Z6f7F7fC.jpg)

* After production, we ended up fixing strange and completely out-of-mind bugs. We had never even thought of those strange conditions before. (Ever find a situation when something in a try-catch block is failing but not throwing an exception?)

Oh, the horror!

After analyzing the situation, doing it in iterations, and reflecting on it, I realized that TDD is actually a golden nugget. If done right, it can make us better developers.

### Why I now love TDD

#### **With TDD, you have fewer bugs**

**You’ll hardly miss things that you can catch with your tests**.

When you get a requirement, you write a test for it first. Then you run the test, and see if it fails first. When you add the logic, you see if it passes.

**Seeing it fail is important, because you know what broke your code**. In the long run, this practice ensures that all lines in your code are well-tested.

#### **TDD saves you lot of time _(in the future)_**

CI/CD relies heavily on tests. If you write the wrong tests (or too few tests) you already wasted five hours to find what errors it couldn’t catch. If you write good tests, and spend just five more minutes writing deeper and more complete conditions of your code, you’ll save time debugging it in the future.

#### **TDD deals with the human aspects of coding**

The main ones being negligence and forgetfulness. If you write all the logic directly, by the end of, say, line 190, you may forget why you multiplied a variable by 100 at line 19.

But, by doing it incrementally and stating the assertion of our code, we gradually build our understanding. This makes us understand the code and its behaviors better.

As a bonus, we have sort of living and functional documentation of our code. You can see which test is failing if you delete the previous line, and you instantly know why.

#### **TDD helps you focus**

Programmers tend to write too much code, or write code that does too much. Or they try to plan for conditions that never exist. Often, when my team practiced pair pairing, I discovered that TDD allowed us to write less code compared to other teams that didn’t do TDD. While coding, we were focused on getting the test case passed — nothing less, nothing more.

#### **TDD also benefits your brain**

You have proof of your code’s readiness for production, even before deploying it. You don’t have to worry about things you already tested for before. You don’t have to brag to your project manager about how project is going, because you can show them that the tests are passing!

![Image](https://cdn-media-1.freecodecamp.org/images/0*m9IeLR30F2AAtlwu.jpg)

However, TDD is not **always** your silver bullet. It takes time. You have to set up the project — such as the environment, mocks, and stubs — even before you start doing anything.

But remember, time spent on writing tests is not wasted time. It’s the time you invest now to save your time later. It’s the investment you make on the system you build, as you build code on top of more code. And you want to make its foundation as solid as possible. TDD gives you that.

In the end, it could cost you a fortune if you **don’t** do TDD. **It may take time, but it is good for you and your team in the long run.**

