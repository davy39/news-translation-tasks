---
title: Blockchain explained by trying to pass a high school math class
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T04:35:30.000Z'
originalURL: https://freecodecamp.org/news/blockchain-explained-by-trying-to-pass-a-high-school-math-class-2322c01ece48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x2gUD6BhNjkF7ac4UEwg5Q.jpeg
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: learning
  slug: learning
- name: privacy
  slug: privacy
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever struggled through a high school math class, then you will be able
  to understand the principles of blockchain technology, which makes Bitcoin possible.

  Have you ever tried to learn the basics of Blockchain by readin...'
---

By Kevin Kononenko

If you have ever struggled through a high school math class, then you will be able to understand the principles of blockchain technology, which makes Bitcoin possible.

Have you ever tried to learn the basics of Blockchain by reading random blog posts and wikis, or watching YouTube videos?

It gets technical **very** quickly. You are quickly presented with concepts like:

_Distributed ledger_

_Cryptographic hash_

_Digital signatures_

Although you can certainly persevere through the initial confusion, you need to understand a series of new technical concepts before you understand the whole system.

#### **Here’s why this is so hard**

Bitcoin (and blockchain) are based on a distributed and decentralized paradigm. We are used to centralized, trustworthy authorities, like banks, healthcare providers, and corporations (yes, we even trust most of them).

Each one of those institutions has complicated systems in place to maintain high quality. In order to maintain these same standards for vital products _without_ the centralized authority…we need new, complicated rules to keep decentralized systems running, too.

So, in this article, I am going to create a new high school called “Distributed High School” that operates using the principles of blockchain. We are going to create a new way to grade assignments from math class using a distributed system. Students will be able to maintain the grading system on their own, without teach involvement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Rj_2EXsXSvtjIL8x.)

**One last note:** Although Bitcoin is probably the most popular application for blockchain technology in 2018, many other industries will likely begin to adopt blockchain over the next five years.

This explanation will translate most directly to Bitcoin, but it will also apply to other types of blockchains. For example, healthcare providers could use a blockchain to securely store individual medical histories.

If you are looking for a more technical explanation, this [20 minute animated YouTube video](https://www.youtube.com/watch?v=Lx9zgZCMqXE) on Bitcoin is probably my favorite.

### The centralized way to manage a high school

Imagine that you are a freshman in high school, and you are taking the algebra class for all 9th graders. In order to pass the class, you need to get a sufficient score on homework assignments, quizzes, and tests. There are 30 total students in your class.

All of this is managed by one centralized authority: the teacher. This one person will grade all your assignments, deliver your report cards each quarter, and make sure that nobody is cheating on tests (which would ruin the integrity of the class).

![Image](https://cdn-media-1.freecodecamp.org/images/0*UaeN6iaCD0UUJ6-t.)

Although this is the system that we are all accustomed to, it actually has some inherent flaws.

1. **It can be inefficient:** when you give 30 tests to a teacher all at once, they can sometimes take a week to get them back to you — because it takes forever to grade 30 tests!
2. **Sometimes it’s risky:** sometimes a teacher might loses a student’s test. Or paper tests can get ruined by floods or other natural disasters. These things happen. And teachers handle so many assignments that there will probably be some errors along the way.
3. **Corruptible:** Have you ever been the troublemaker in the class? When the teacher sits down to grade your test, they may take one look at the name on the top of the test, and become instantly biased while grading the test. Sometimes this is hard to avoid (human nature and all that jazz).
4. **Costly:** All that time spent grading tests is time that could be spent doing other, more productive things. This is also probably the teacher’s least favorite part of the job. They probably became a teacher so they could help students learn, not spend all their “free” time grading tests. Instead, your parents’ taxpayer dollars are going towards an activity that could be much improved.

You can see similar issues with other centralized systems. For example, although we trust banks with our hard-earned money, the banking industry helped cause the [2008 financial crisis](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%932008) through risky practices that required a massive taxpayer-funded bailout.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-Jp5sc1d8PL_JreA.)

Although we trust doctors, [medical error is the third-leading cause of death in the United States](https://www.usnews.com/news/articles/2016-05-03/medical-errors-are-third-leading-cause-of-death-in-the-us), behind heart disease and cancer. Many of those errors might be caused by important medical data being inaccessible to doctors.

So, back to high school math class. You might be wondering… how the heck are we going to solve all these problems by removing the influence of the teacher, the one person with the most expertise in this system? How would we prevent it from becoming anarchy?

![Image](https://cdn-media-1.freecodecamp.org/images/0*BmLmZP9UAVLDbv49.gif)

That is where the blockchain concept comes in. Before I get into the specific way we will use blockchain to create a new way to run Distributed High School, you should know that each blockchain has specific rules that are instituted by its creator.

In Bitcoin’s example, that would be “[Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto)” who wrote the original white paper and created the rules (algorithms) that allow it to operate without human intervention.

In our school example, we are going to have an exceptionally forward-thinking principal that has changed the rules.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4p657mzLzJjE13V-.)

### Creating a blockchain for distributed high school

While a teacher grades tests and manages grades in private, a blockchain makes all transactions public. So, blockchain doesn’t rely on any central authority aside from the person who created it.

If you haven’t already guessed it, that means that in Distributed High School, we are going to start by having the 9th-grade students grade each other’s tests!

Let’s say it is test day, and the class period is an hour long. Students neatly stack their tests on top of the teacher’s desk when they finish.

But, instead of taking all of the tests home for grading, the teacher jumbles all of them into a big pile, and asks each student to take a random test and grade it with an answer key.

This is known as a **transaction**. This is the fundamental unit that makes up a blockchain. Let’s say that one student, Andy, gave another student, Alice, a grade of 84. In this case, Andy is the **sender** and Alice is the **recipient**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*t2VhNUww6r7ioUsE.)

In Bitcoin terms, this would not be random: you know where you are sending money!

![Image](https://cdn-media-1.freecodecamp.org/images/0*QRWwpy7J6et9kjFV.)

So far, we have solved the speed and cost problems. Teachers no longer need to spend time on grading, and each student can grade one other test pretty quickly. But, there is a huge potential for fraud. This is pretty close to anarchy. There needs to be a network of responsible people that will keep all participants honest.

Here’s where the principal’s policies come in. The principal controls the one thing that everyone cares about: the grading system. At Distributed High School, the principal decides to allow seniors (12th graders) to run this blockchain system in exchange for a reward.

If a senior reviews 20 of these graded tests in 1 day, they can enter into a competition to get **10 points added to one of their own tests**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1SnDo-1Zf1wigpvx.)

That set of 20 transactions is known as a **block**, and we will eventually show how all blocks work together to form a **blockchain**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*AKHGsWEryV33QBrV.)

So why can only seniors do this? And why must it be a competition?

It must be seniors, because the principal needs participants who are going to be able to handle the workload of grading tests every day (if they want to). If the system slows down, then nobody would have their tests validated and logged, which would be a complete failure.

And it must be a competition so that the point system is not completely devalued. Imagine if every senior reviewed their 20 tests and received 10 points on their own test? Grade inflation would be rampant, similar to the way that currency inflation increases when the government prints more money. There must be a competition for a scarce number of points. I’ll share the terms of the competition later.

The principal is not forcing any senior to participate, but there is a strong incentive for them to do so.

In Bitcoin, each block has a limit of 1 megabyte (MB) of data. As of late 2017, the average transaction included about 500 bytes of data, so a block typically contained about 2000 transactions ([source](https://arstechnica.com/tech-policy/2017/12/bitcoin-fees-are-skyrocketing/)).

![Image](https://cdn-media-1.freecodecamp.org/images/0*S2XeukezziEmbTz-.)

### An introduction to the distributed ledger

Now we know how one test gets graded (a transaction) and the incentives in place for the seniors to maintain the system with integrity: they get more points by reviewing and validating more tests. But we are still missing the entire distributed infrastructure for how this work actually gets done.

Let’s say that 10 seniors took the principal up on his offer. They want to be part of this competition to earn more points on their own tests. Another set of 10 seniors decides to volunteer to help maintain the system, but not participate in the competition. This is simply out of support for the distributed system, and part of the spirit of the movement towards open-source grading.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2aTv7QNJDk-Z1VVC.)

Each one of those seniors is a [**full node**](https://bitcoin.org/en/full-node) in the network. They communicate in real-time about new transactions and blocks.

The 10 seniors that decided to participate in the competition are called **miners**. They build blocks with transactions available in the **mempool**, the reservoir of unconfirmed transactions.

When a student, like Andy, finishes grading a test, the student broadcasts an **unvalidated transaction** to the network of seniors. Each full node shares it around with everyone else, like a rumor. It becomes part of the mempool.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oRwV9z9DSPTj0oeH.)

Every node must **validate** the transaction first. In other words, they determine whether it was possible or not. In this example, validation could mean confirming that the grader actually graded the test correctly by punching in all the final answers into your calculator. We will get into the other part of validation in a little bit.

After validation, each miner has the opportunity to build their own block out of 20 tests, or transactions.

But wait! On test days, 30 new transactions should be added to the network, since there are 30 students in the class. How do the miners choose the transactions to add to their block?

The answer is a **transaction fee**. Each **sender** must attach a transaction fee to their transaction to compensate the miners for their work. So, the miners usually just choose to put all the transactions with the highest fees into their blocks immediately. Since this operates on supply and demand, they can include the transactions with lower fees on days when there are fewer tests to validate.

In our school example, this transaction fee could be a point off the sender’s test to donate to the miner. It would not come off of Alice’s (the recipient’s) test. In Bitcoin, it would be a small fraction of a Bitcoin, like 0.000003 BTC. The sender pays the fee since that is the easiest way to handle the logistics.

![Image](https://cdn-media-1.freecodecamp.org/images/0*G4LLKTQ0ZbDOUa2z.)

At this point, each miner has their block of 20 validated transactions that they would like to add to the blockchain. Now, it is time for the competition to see which of the 10 miners will get their blocks accepted and be awarded the points from the principal.

![Image](https://cdn-media-1.freecodecamp.org/images/0*llDVmllWBaTLR4U3.)

One last thing. You are starting to see the amount of _redundancy_, or repeated work. Each proposed block will have many transactions (tests) in common. That is a security measure necessary for running a distributed system. If all the nodes are validating transactions separately, that makes it much harder to cheat the system.

### The race for proof of work

Imagine that after all this work to create a block of 20 transactions, the principal then shared a 12th-grade level math problem to every miner. The person that solved the problem first was awarded all the points and had their block confirmed.

This would mean that the “rich get richer,” and it would skew the incentives for the whole system.

Every day, the top math students would have an excellent chance at winning the competition, and the rest of the seniors would have little to no chance. Soon, most miners/seniors would stop participating since they would never receive any points.

So, instead, our principal is going to set up a scavenger hunt in the school every night. Importantly, the scavenger hunt has **nothing** to do with a miner’s math ability. This encourages everyone to continue to mine.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qr4WFhLdSP25-2cA.)

The principal will hide a trophy somewhere in the school. The students must race around until they find it, and then yell so that the rest of the students throughout the school can confirm that they found it and go home. Since this principal has some magical foresight abilities, he hides the trophy in a perfect place so that it will take r**oughly an hour to find each night.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*KInaCht6IDVdOhgP.)

Does this sound arbitrary? In other words, does it feel like it came out of nowhere?

Well, it must be unrelated to the test-validation so that it can level the playing field. This is known as “[proof of work](https://en.bitcoin.it/wiki/Proof_of_work)” in Bitcoin. It is an algorithm that is difficult to solve, but easy for the other nodes to confirm once it is solved. Each Bitcoin miner must guess numbers until they choose the right one that solves the puzzle. In Bitcoin, a new block is confirmed every 10 minutes, on average.

Keep in mind, Bitcoin miners are really massive computers that look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*-l7_x9hWb_TnXykS.)
_[Image credit](https://medium.com/@lopp/the-future-of-bitcoin-mining-ac9c3dc39c60" rel="noopener" target="_blank" title=")._

The algorithm also gets gradually more difficult over time as more miners join the network. If there are more miners, that means there will be more guesses, so the challenge must get more difficult if Bitcoin wants to continue to confirm a block every 10 minutes.

This example demonstrates how Bitcoin (and our school example) force every miner to compete against the rest of the network. Once a miner solves the puzzle, they share their answer with the rest of the network, which can be quickly confirmed. After the nodes reach a **consensus**, or over 50% agree that the block is **confirmed**, it can be added to the blockchain.

This has motivated some miners to form **guilds**. In our school example, this means that a few of the students would agree to split the points once one of them finds the trophy. It simply increases the probability that the first one to find the trophy will be a member of their team.

In Bitcoin, the total computing power that is working on solving this “proof of work puzzle” is called the [**hash rate**](https://bitcoin.org/en/vocabulary#hash-rate). The largest Bitcoin guilds control about 10% of the hash rate, which still gives the rest of the miners a good chance to solve the puzzle. If a guild contained 50% of the hash rate, there would be less incentive for others to continue to mine.

Once a block is confirmed, the miner receives the prize (10 points on a test) and all the transaction fees from the confirmed transactions. Transactions that were not part of the block then return to the **mempool** to be included in a future block.

### Building a blockchain

So far, we have covered most of the steps that go into adding one more block to the blockchain. But, we have not covered the whole point of building a blockchain itself.

A blockchain has a simple three-level structure. A series of transactions make up a block. And a series of blocks make up a blockchain.

Although you can certainly divide a blockchain into pieces based on timing, usually, each individual node (senior) will maintain the full history of the blockchain, or the **ledger**.

In our high school example, we are looking at a 9th-grade class. So, the full history of the class could be all of the grades from all of the students in the entire class, from kindergarten until today. Since we are adding blocks at a 1-day interval, and there are approximately 180 days in the school year, that would mean that the blockchain contains about 1700 blocks.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YdtjX9-71kre2aca.)

Each block has a unique ID, which, due to a “[hash function](https://www.coindesk.com/information/how-do-bitcoin-transactions-work/)”, depends on the block ID of the previous block. That is what secures the blockchain: there is no such thing as block substitution, or rewriting history, because it will change the block ID of every subsequent block.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IDnKIxaCaRxsE8RU.)

Since our education example uses one-day intervals, you might think, _“Oh, it should be easy to create a unique ID for each block, since each date only occurs once!”_

But, that would introduce a security vulnerability. If a miner was able to introduce a new block somewhere in the middle of the chain, it would not break the pattern! The deviant miner would easily be able to replicate the block ID, and none of the following blocks would change their value, since dates follow a dependable pattern that can be easily replicated.

Here is a [hash generator that you can play around with](http://www.miraclesalad.com/webtools/sha256.php). I wish there was some wonderful analogy I could give you for the block order, but unfortunately, that is the point of the hash function. It makes it very, very hard to imitate and replace blocks (impossible, as far as we know). So, I will add some random strings to show what is going on.

![Image](https://cdn-media-1.freecodecamp.org/images/0*c9DDWVUYJU9Gf_lL.)

We are going to cover privacy in the next section, because right now, it looks like every 12th grader can see the entire grade history of each 9th grader. That is not what we want!

But, on the plus side, the distributed ledger allows each individual senior to ensure the validity of the graded tests as they circulate around the network.

This ordering system is **relative**, rather than absolute. The order of the blocks matters much more than the times that they were added to the chain. Timestamps, as we discussed above, are too easy to copy and imitate.

Let’s give an example of what is known as a **double spend attack**. Let’s say that one of your classmates takes a math test on a Monday, and knows that she did poorly. One of your classmates grades that version of the test and then broadcasts it to the nodes, per usual.

Your classmate who did poorly studies like crazy that night, and then shows up the next day to take the same test with another class. Maybe the teacher didn’t notice her there the day before — so she is able to convince the teacher that she was not present on the previous day. Remember, the teacher has no role in grading tests, so the teacher cannot quickly reference the previous day’s exams. The student is allowed to take the test again, and submits it with the rest of the class.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PEQrhnTmZhPyNDwZ.)

Here are the latest options for blocks from the blockchain, with Alice’s attempt to override her previous grade.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YEn6fQq_eZvWuSyl.)

Oh, by the way, Alice will now need to become a miner on the network and participate in the scavenger hunt. She is now the 11th miner on this network.

The rule is that the “longest chain wins.” That means that on Day 11, the rest of the network may be working on adding a new block with the latest set of transactions. But Alice will be working on “**forking**” the chain, and adding a new set of transactions for day 10 with 19 transactions in common, and her new test score as a replacement for the old test score.

Forking means that she is attempting to build a new longest chain, as opposed to the chain that the rest of the network assumes is the longest.

If she can win the scavenger hunt that day, and then come back the next day and win it again, she would have the longest chain.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ssSrX9xeV-rGw8D7.)

This is part of the value of the “proof of work” system. Since Alice is one of 11 miners on the network, she has an approximately 1% chance of solving two blocks in a row. There is a 99% chance that she will put in all that work just to get nothing. Not a great incentive.

This is also why the block IDs and previous block IDs are a better labeling scheme than a specific date. If Alice wins the race on the day that she secretly takes the test a second time, all the new tests from that day will still be eventually stored in the blockchain. They will just need to wait one more day.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_P5KrKwCU2FuXkYG.)

### Introducing public and private keys

So far, we have covered all the mechanics that will allow the students of Distributed High School to manage their own grades. We are missing just one major thing: privacy!

Right now, the grades of each individual student are exposed forever on the blockchain. If this were a currency, it would be easy to figure out how much money each person had. That is not what we want.

At the same time, the transparency is a great way to keep individual people accountable for unfair grading and other fraudulent practices.

This is why Bitcoin uses a cryptographic system with **public and private keys**. In high school, you are probably used to the lockers that line pretty much every hallway.

![Image](https://cdn-media-1.freecodecamp.org/images/0*lWOuvJJs7uvVxzK4.)

Well, in Bitcoin, there are an (essentially) unlimited number of private-public key combinations. So instead, imagine that this high school’s walls are lined with the little mailboxes that you see in an apartment building.

![Image](https://cdn-media-1.freecodecamp.org/images/0*SaCRqoGbn9LGrNZw.)

And they cover every wall in this whole dang school. And, since there are an unlimited total number of lockers, each student in the school can own an unlimited number of lockers. In math terms:

_Unlimited/30 students = Unlimited_

Have you seen [Harry Potter and the Order of the Phoenix](https://en.wikipedia.org/wiki/Harry_Potter_and_the_Order_of_the_Phoenix_(film))?

![Image](https://cdn-media-1.freecodecamp.org/images/0*lhLjy4ByrTRhb22J.)

It’s like the scenes from the “[Hall of Prophecy](http://harrypotter.wikia.com/wiki/Hall_of_Prophecy)” — seemingly limitless.

But anyway…

For the sake of simplicity, let’s assume that each student gets 1 mailbox for each grade in school (9th-12th) during which they took tests. If a student is in 9th grade, that means they are using their 9th grade locker.

Let’s return to our transaction, where Andy grades Alice’s test.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Pz1ZwzVBr9c_TYNt.)

Our **full nodes**, the wonderful seniors, must first evaluate whether Andy is qualified to be grading 9th grade math tests. Andy needs to prove himself.

Here’s an issue: if Andy happily announces to the network that he has graded Alice’s assignment, he risks exposing Alice. What if she got a failing grade? She doesn’t want the whole world to know that, forever!

So, he must broadcast while keeping both of them anonymous. He can randomly slip a note to one of the nodes…just like most rumors in 1980's high school movies start!

![Image](https://cdn-media-1.freecodecamp.org/images/0*t4cxM7jDV10lZAZQ.gif)

Then the full node would share this rumor with the rest of the network.

This is where our **public keys** come into play. When Andy slips a note about his graded test to the network, he is really saying:

* My current mailbox address is 126900trl.
* In order to prove that I was there on test day, here is the answer key that the teacher gave me to grade this specific test (**digital signature**).
* Also, in order to prove that I am indeed a 9th grader in algebra class, here are the final exam scores from math class each year from grades 1–8, and the answer key for each of those tests (**transaction chain**).
* I am going to be delivering the test to mailbox 856734pok

![Image](https://cdn-media-1.freecodecamp.org/images/0*EgJPXleu1fqn6T4N.)

This is answering two key questions:

1. Is the sender the actual person that he/she claims to be?
2. Is the sender qualified to be the sender (grade the test)?

In order to answer the first question, Bitcoin uses a **digital signature**. The digital signature is unique to every transaction and is formed with a hash of the transaction ID and private key. In this case, that is kind of like the test key: you can only own it if you were there on the specific test day and the teacher gave it to you.

For the second question, remember that in Bitcoin there is no concept of an “account” or “account balance.” If there was, Andy could just share an ID number that proved he was qualified.

In order to prove that this particular public key (Andy’s public key) has the sufficient approval, he must share a test history that every full node can validate. That way, everyone can validate that he completed 1st-8th grade. Andy must also provide the answer key for each of those tests to prove that he was in the room at that time. This is called the **transaction chain.** I will not cover it here, but it is an important part of validation.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_CQr2_5Bm1-pJBYh.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*TuGPI64sSgjzdV5O.)
_[Image credit](https://www.cryptocompare.com/wallets/guides/how-do-digital-signatures-in-bitcoin-work/" rel="noopener" target="_blank" title=")._

After Andy’s transaction is **validated** and then included in a block that has been **confirmed**, he can go drop the test off in Alice’s mailbox without public knowledge.

As you noticed in the transaction above, Andy had to access tests from the last 8 years! This locker system only allows Andy to access his tests.

Andy has a set of 8 **private keys**. Every time he started a new year, he opened another locker and put his grades from that year in the locker.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3PLQPo9mhRE477b0.)

Others can slide his latest test results into his locker, but only he can then retrieve the results.

Bitcoin software like [Coinbase](http://coinbase.com/) allows you to create many public/private key combinations within your wallet. This improves security. You never want to give away your private keys, which are the only way to access the Bitcoins that have been transferred to you. Unlike a traditional bank, there is nobody to turn to if you forget or lose a private key. The Bitcoin will be locked up.

### Final Thoughts

To recap, we have:

* Tests (Transactions)
* Answer keys (Digital signatures)
* 9th graders (senders and recipients)
* 12th graders (full nodes)
* Principal (blockchain creator)
* Unlimited mailboxes (public/private keys)
* No teachers grading tests (centralized authority)
* No report cards (Accounts/account balances)

Much of this system revolves around the concept of being “trustless,” as you have probably seen by the careful checks and balances and incentive structures. In the traditional playbook for administrating banking or public education, trust in a central authority plays a huge role. In order to give that control back to individual people, there must be a huge amount of redundancy from the nodes to prevent fraud, as well careful security protocols to prevent hackers from infiltrating the system.

But, this distributed system could revolutionize the way that many industries handle their data, and could help prevent industrial accidents, medical malpractice, and financial ruin.

If you haven’t already noticed, there is a huge amount of duplicated work across all the full nodes. Between validating and confirming transactions, as well as guessing answers to the “proof of work” as quickly as possible, the system consumes plenty of energy. [According to one estimate](https://arstechnica.com/tech-policy/2017/12/bitcoins-insane-energy-consumption-explained/), the Bitcoin network consumes as much energy as the country of Denmark! But, this is also necessary to form a consensus and maintain the integrity of mining.

### Get More Visual Explanations

Did you enjoy this tutorial? Give it a clap, leave a comment, or sign up here to get my latest technical explanations:

