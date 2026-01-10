---
title: How to Help Someone with Their Code Using the Socratic Method
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2025-01-07T19:33:01.192Z'
originalURL: https://freecodecamp.org/news/how-to-help-someone-with-their-code-using-the-socratic-method
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/2RRq1BHPq4E/upload/904ec5e77783268f025191b07da29f08.jpeg
tags:
- name: coding
  slug: coding
- name: learning
  slug: learning
- name: freeCodeCamp.org
  slug: freecodecamp
seo_title: null
seo_desc: 'As a programming community, freeCodeCamp helps many people who have questions
  about their code. It can be quite tempting to simply provide the learner with the
  answer and move on, but that’s actually detrimental to the learning process. Here’s
  why:

  W...'
---

As a programming community, freeCodeCamp helps many people who have questions about their code. It can be quite tempting to simply provide the learner with the answer and move on, but that’s actually detrimental to the learning process. Here’s why:

When you give someone the answer, you are depriving them of that “aha” moment. You are removing the opportunity for them to learn how to reach the conclusion through their own thinking, and instead allowing them to progress with minimal effort or thought.

So how can you best help someone with their code?

## What is the Socratic Method?

The Greek philosopher Plato was a student of another philosopher, Socrates. In Plato’s works, he often writes about the debates that Socrates would have with his colleagues and students.

Socrates would begin these discussions by raising common beliefs and scrutinizing them to question their compatibility with other beliefs, and guide people to reach the truth.

But how does that translate to our modern day interactions in a digital age?

Let’s consider a real example from one of our communities:

![A Discord message from the user Razzle Dazzle, reading "How do I find the sum of the numbers in an array?"](https://cdn.hashnode.com/res/hashnode/image/upload/v1736179977371/7e087ee9-4b7e-4321-ade9-18019289320d.png align="center")

You might be tempted to give them the direct answer, such as this code example:

```javascript
const sum = nums.reduce((acc, el) => acc + el, 0);
```

But in doing so, you have performed the logical reasoning on behalf of the learner.

Instead, you should focus on asking pointed questions to *guide* them to the answer. For example, you might start by asking:

> ❓ How would you find the sum of a list of numbers on pen and paper, without code?

It may seem counter-intuitive to ask the learner a question that requires them to step away from the code, but you are actually pointing them to the underlying logic behind their question.

Let’s assume the learner responds with something like:

> I would go through each number, one by one, and add it to the sum of the previous numbers.

As the learner begins answering your questions, the dialogue should progress in this call-and-response format. Your questions should become increasingly narrow and pointed with the learner’s progress toward the solution.

For example, a series of questions might look like:

> Instructor: “Great, now what is an array of numbers?”  
> Student: “A list?”  
> Instructor: “Good! How would you iterate through that list?”  
> Student: “With a for loop.”  
> Instructor: “And what does your loop need to do on each iteration?”  
> Student: “Add the current number to the sum.”  
> Instructor: “Where can you find the sum?”  
> Student: “I could put it in a variable outside the loop.”  
> Instructor: “Great, now you’re ready to try writing the code.”  
> — original example written for this article

At this point, the learner will likely connect the dots and reach the final solution.

## Socrates in Modern Culture

Learning the Socratic method is hard. In fact, many do not encounter it until they reach their university studies. But there are examples found in modern pop culture that can help you understand how the Socratic method works.

The TV show House, M.D. is rife with examples. Take this exchange from the episode titled “Three Stories”:

> House: “Kidney stones would cause what?”  
> Student: “Blood in urine.”  
> House: “What colour is your pee?”  
> Student: “Yellow.”  
> House: “What colour is your blood?”  
> Student: “Red.”  
> House: “What colours did I use?”  
> Student: “Red, yellow, and brown.  
> House: “And brown. What causes brown?”  
> Student: “Waste”.  
> — (Frapier, 2008)¹

You’ll notice how this exchange took place. House’s goal here was not to *give* the learner the answer, but to ask deductive questions to *guide* the learner to reach the answer on their own.

Consider the popular movie The Matrix:

> Morpheus: “Have you ever had a dream, Neo, that you were so sure was real?”  
> Neo: “This can't be…”  
> Morpheus: “Be what? Be real?”  
> Morpheus: “What if you were unable to wake from that dream, Neo? How would you know the difference between the dreamworld and the real world?”  
> — (Wachowski & Wachowski, 1999)²

In this scene, Morpheus is applying the Socratic method to lead Neo to question his perceptions of reality. This is a rather dramatic example, but the premise remains the same: rather than telling the learner how they should think, you guide them to reach the conclusion through their own volition.

Finally, let’s look at an example from Legally Blonde:

> Elle: “Your father was shot while you were in the shower?”  
> …  
> Chutney: “Yes. I was washing my hair.”  
> Elle: “Miss Windham, can you tell us what you'd been doing earlier in the day?”  
> Chutney: “I got up, went to Starbucks, went to the gym, got a perm, and came home.”  
> Elle: “Where you got in the shower.”  
> Chutney: “Yes.”  
> …  
> Elle: “…Had you ever gotten a perm before, Miss Windham?”  
> Chutney: “Yes.”  
> Elle: “How many, would you say?”  
> Chutney: “Two a year since I was twelve. You do the math.”  
> …  
> Elle: “Chutney, why is it that Tracy Marcinko's curls were ruined when she got hosed down?”  
> Chutney: “Because they got wet.”  
> Elle: “That's right. Because isn't the first cardinal rule of perm maintenance that you are forbidden to wet your hair for at least twenty-four hours after getting a perm at the risk of de-activating the ammonium thiglycolate? And wouldn't someone who's had -- thirty perms ? -- throughout her lifetime, be well aware of this rule? And if you, in fact, were not washing your hair, as I suspect you were not, since your curls are still intact, wouldn't you have heard the gunshot?”  
> —(Luketic, 2001)³

The Socratic method can often be seen in law, and this serves as an excellent example. Through this exchange, Elle is not trying to guide Chutney to reach a conclusion, but rather the *spectators* (in this case, the jury). This is an important distinction for a community such as ours: where engaging in a Socratic discussion with one member can actually benefit current and future members who may observe or revisit your conversation.

## Goal of the Socratic Method

It is important to recognize that the goal of the Socratic method is *not* to present a quick exchange of information. Instead, the aim is to first get the learner to realize that they know less than they believe they do, then guide them to the answer through questions that elicit certain thought processes.⁴

When applying this to learning programming, then, it’s important to remember the phrase “challenge your assumptions”. We often assume that we know what the code we have written is doing, so our first step when it is not working is to examine those assumptions.

As we guide learners through the process of debugging, we want to ask questions that do the same. A common question in your repertoire should be “What does this line of code do?”. When the learner answers with information that is inaccurate, respond with questions that drill down into smaller components of the code – break the problem into pieces, per se.

Consider this example:

> Learner: “but maybe that wouldnt work because I need to find the book not the id in the book”  
> Instructor: “Correct. Now, the good news is that we have a function that would ostensibly do that. The bad news is that function doesn't do that. What does that function do instead?”  
> Learner: “returns bookId”  
> — sourced from our Discord community⁵

By asking the question “What does that function do instead?”, the instructor has provided the direction for the learner to reach the correct conclusion without having to provide any specific information. The learner already knew that the function did not perform as expected, and the instructor asked the question to challenge the learner’s assumption that the function *did* perform.

Here’s another example:

> Instructor: “This is the example from the Chalenge (sic). Did you follow that example they gave?”  
> Learner: “yes but i didnt understand the for-in loop, i didnt understand "(const food in refigerator)", having to state the string property name with const or let was confusing (it isnt anymore)”  
> Instructor: “Ok, so lets start here instead of the full solution to the Challenge”  
> Instructor: “What does that code do when you run it?”  
> …  
> Learner: “each of the object's keys were set to the variable food which was made in the for-in loop, it then iterates through the object and logs the key and value assigned to the key?”  
> — sourced from our Discord community⁶

Again we can see how the instructor focuses on asking pointed questions that guide the user toward the solutions *through their own reasoning*.

> ❗ That is the ultimate goal of the Socratic method: to guide the learner to reach the logical conclusion solely through their own reasoning.

## Long-Term Benefits of the Socratic Method

The Socratic method is not solely beneficial for resolving the immediate solution. The deductive reasoning process that is applied in this approach can also serve the learner well over the long-term.

The process of asking a learner questions to challenge their assumptions and knowledge, and guide them to the solution, is something that can be internalized as well. It’s a powerful tool to have in your repertoire for approaching debugging, isolating assumptions, and even learning to articulate an issue.

That is, by walking a learner through this call-and-response conversation, the learner can also walk away with the ability to ask *themselves* these questions. They can take the same process of asking increasingly narrowing questions as a logical pathway and run through it mentally when they encounter future issues with their code (or even in other aspects of life)!

## Conclusion

Providing a solution directly to a learner inhibits their intellectual growth and deprives them of the rewarding experience that comes from reaching their own logical conclusion. By leveraging techniques like the Socratic method, we can foster a stronger and more effective educational environment that allows learners to grow and thrive.

> 💡 If you were sent this article in response to a forum post, Reddit comment, Discord message, or other communication where you gave a fellow learner a working solution, please consider the merits of this method instead.

This approach can seem tedious and lengthy, and at times it is. It is far quicker (and arguably easier) to hand someone the code that resolves their problem.

But that approach, more often than not, harms the learner in the end. And, if you’ll forgive this author for an anecdote, I have seen people get frustrated when they are the subject of a Socratic approach, or lose patience with the back and forth conversation. But I have *never* seen them upset with or disappointed by that end result – the “aha” moment where they deduce the solution to the problem through their own reasoning.

### Sources:

1. ¹ Frapier, M. (2008). Being Nice is Overrated: House and Socrates on the Necessity of Conflict. In *House and Philosophy* (pp. 100–101). John Wiley & Sons, Inc.
    
2. ² Wachowski, L., & Wachowski, L. (Directors). (1999, March 24). *The Matrix* (Z. Staenberg, Ed.). Warner Bros.
    
3. ³ Luketic, R. (Director). (2001, July 13). *Legally Blonde* (A. Brandt-Burgoyne, Ed.). MGM Distribution Co.
    
4. ⁴ Frapier, M. (2008). Being Nice is Overrated: House and Socrates on the Necessity of Conflict. In *House and Philosophy* (p. 103). John Wiley & Sons, Inc.
    
5. ⁵ lightskingeneral & plamoni (2024, January 4). \[Discord conversation\]. Discord. Retrieved 2025, January 6, from [https://discord.com/channels/692816967895220344/718214639669870683/1192488621043888198](https://discord.com/channels/692816967895220344/718214639669870683/1192488621043888198)
    
6. ⁶ lightskingeneral & jeremylt (2023, November 13). \[Discord conversation\]. Discord. Retrieved 2025, January 6, from [https://discord.com/channels/692816967895220344/718214639669870683/1173733715109761065](https://discord.com/channels/692816967895220344/718214639669870683/1173733715109761065)
    

Special thanks to ArielLeslie and JeremyLT for their help with this article.
