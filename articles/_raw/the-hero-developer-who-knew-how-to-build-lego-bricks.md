---
title: 'The Top Five Developer Skills That''ll Make You a Hero (Hint: Involves LEGOs)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T18:18:57.000Z'
originalURL: https://freecodecamp.org/news/the-hero-developer-who-knew-how-to-build-lego-bricks
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/superman.jpg
tags:
- name: agile development
  slug: agile-development
- name: beginner
  slug: beginner
- name: best practices
  slug: best-practices
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'By Jean-Paul Delimat

  Programming is like building something with LEGOs. Any developer can pick up a brand
  new LEGO set and build it following the instructions. This is very easy. Think of
  it as coding school assignments or entry level tutorials.

  A re...'
---

By Jean-Paul Delimat

Programming is like building something with LEGOs. Any developer can pick up a brand new LEGO set and build it following the instructions. This is very easy. Think of it as coding school assignments or entry level tutorials.

A real software project is different. It is like building a very large castle set. Except it has already been built in the past. Then someone torn it to pieces with a savage kick. The bigger parts remain kind of together. But the smaller parts were completely crushed. Some elements went out the window. 

You get a box containing what's left, but also thousands of pieces from other sets. And the instructions are gone, of course. You can only rely on one picture to know what the castle looks like.

Now that's interesting! Let's see what we can do to work effectively in such an environment.

## **1. Accept the unknowns**

  
The first step of any development task is to understand what you need to do. It sounds obvious. And yet, the bigger the task, the more unknown variables you get. This is the moment to set clear expectations. 

If you have no clue how to get started, there is no point thinking and conceptualizing too long. Start and get your head around the key elements you need. Then think again. If anyone asks you for estimates or a deadline upfront, be open and honest. Some parts of the system you don't know or may not understand. And that's OK. 

Think of platforms like Facebook, Netflix or Oracle. Or any larger enterprise software out there. Very few people can grasp the full scope. The ones who do have either built it or spent years working with it. So first of all, give yourself a break for not knowing everything. And more importantly, accept that you won't know everything.

> _Experienced and productive developers are not better coders. They are better at evaluating what they need to do. And at picking the right strategies to cope with the unknowns._

**LEGO analogy**: Think of the castle set we want to rebuild. Say someone gives you a picture of the castle and the box, and asks you "how much time do you need to build the castle?" There is no good answer to that except "I don't know yet. Let me start and let's see where I am at after a day or two".

The ultimate "I fear the unknowns" approach to this task would be to lay out all the elements from the box on the floor. Try to separate them into the sets they belong to based on color and shape. Then look at the picture and make a mental map on how to assemble the bricks.

This approach is not very effective for two reasons. First, if the castle is too big you'll probably never get there. Second and most important: you can't assess progress. You could be on the right track or not at all. You have no feedback loop.

Another approach would be to start building the castle. As you go you will learn if it is easy to find the pieces you need or not. You will know if the picture shows all the details or if the construction is more complex than it looks. 

Based on this information you'll be able to make a more educated guess on the time and effort it will take to do the job. And if it's worth doing at all. 

If you need it built for tomorrow morning, maybe going to the store and buying the same castle again is a better solution? That's might not be your decision to make, but solutions to a problem does not always come through more code.

## **2. **Accept compromise****

Developers often praise and value "great attention to details". Every job offer out there has this in one form or the other. That's all good. But don't confuse attention to details with stubbornness and perfectionism.

When starting a big task you have to define two versions of it. The first version is the bare minimum you need to verify that things will work the way you think they will.

That's what I call "working horizontally". Each piece of your bigger task is a vertical. You don't have to go deep to get the first results. Focus on the main use case or scenario first. And take it from there.  

The things you can leave behind in the first version:

* error handling
* edge cases
* clean code
* configuration

Don't think of all that and just write the code you need as it flows from your fingers. You should get to a high functional coverage quickly. Sure, it will take a lot of time to move from this first, simplistic version to the final one. So what is the point? 

That's a safer way to progress. You want to verify your assumptions. As smart and capable as you may be, designing and conceptualizing can only take you so far. Get your hands dirty. It will give you more knowledge and insight than any "thinking it through".

This is the same principle that applies to MVPs for new products or features in business. The approach also has the advantage that you can show your first version and get feedback. Or ask questions. It's easier to brainstorm on existing code than on a drawing or concept.  

**LEGO analogy:** You are building the tower of the castle. On the picture the high tower walls are made of interlaced grey and white bricks. There is a princess locked in the tower and a dragon on the roof.

You find the princess and the dragon but it would take you ages to find the grey and white bricks you need. The right approach is to build the wall using any bricks, and place the princess and the dragon. You can leave a TODO like "Improve the bricks of the wall".

The idea is that you have identified a problem: it's going to be difficult to build the perfect wall. Let's accept that and move on to discover all the other obstacles we don't know about yet. Accepting the compromise prevents you from getting stuck.

Even if you never get to the TODO, you can tell your customer: "Here is the full castle. We know we have to improve the tower wall, but it's built". This is much better than "We are heavily delayed because it took us ages to find the right bricks for the tower. But look, the tower is perfect and exactly as on the picture you sent us. Now we'll get to the rest of the castle".

> _Important: don't confuse compromise and sloppiness._

The key elements of the tower are the princess and the dragon. Don't put a farmer in the tower and a cat on the roof and think that's an OK compromise. It won't work :)

## **3. Start with the outside world**

There are many things you can control. And things you can't. I learned that the hard way on one of my first assignments as a developer ten years ago. The task was to integrate an external API and process the data. I had one week. It was a very reasonable timeline, even for an inexperienced guy like me.

Here is what I did (and what you shouldn't do):

It's Monday morning. I've read the API documentation for 10 minutes. It seems very easy. I create a test data set and moving on to write the code to process it. I will test with the real API once I'm done.

Wednesday morning and I'm almost done. I think my code is clean and well designed and everything (it wasn't). Now I just need to integrate the API and I'll probably finish ahead of time. I can't help but think that "I am awesome".

I quickly get to the API part. I'm trying to reach it with my code. Except I can't. Something is wrong. I waste the whole day double checking everything. Using different API clients. No progress. The day flashes and it is Wednesday evening now.

 **I am stuck, and I feel quite the opposite of awesome.**

I get to work on Thursday and ask a colleague for help. He tells me that access to the API may be IP restricted and that I have to contact the company to white-list our IPs. Good, I have a way forward.

I send an email to the company owning the API. It's like 8AM. I foolishly expect a quick answer and resolution within minutes. I sweat all morning and at noon I finally pick up the phone and call the support number. I explain my problem and try to highlight the best I can how big an "emergency" it is (it wasn't).

The guy on the other side of the line explains me that the white-listing time is usually 1 or 2 days. Now I am depressed. 1 or 2 days? How is this possible? My task is the most important in the world (only to me of course) and they tell me "1 or 2 days"? 

All of a sudden I am not ahead anymore. I am late. I failed. I go to my boss and tell him I screwed up. I should have checked the API Monday morning. I would then have requested access the same day and I would have written my code in the meantime. He just smiles back as a "Yes you should have".

I finally get access on Friday and have to stay very late to finish the job. I adapt my code to the many surprises the API data bring. Good bye well-designed and clean code. I will justify it later saying "There was no time for that" (there was). 

In my naïveness of the time, I felt the access thing and wrong documentation were very bad luck. Now I can tell it was business as usual.

The lesson is to start with what you can't control. Confirm every assumption you have about the environment. Use manual and low cost ways to try things out as early as possible.

**LEGO analogy**: Imagine you are building the castle and things are running smoothly. You now have mixed the box about 100 times looking for pieces. You can't help thinking "I never came across that huge orange dragon sitting on the tower on the picture". 

You ignore that information to focus on the good progress you have. That's human. Moving forward is more exciting than dealing with problems. At the end you'll have to acknowledge that the dragon is missing. And tell your customer very late that the bigger piece of the set will not be present. That's not good.

The thing to do instead is to follow up on that hint: "Where is the dragon?". Spend the time needed to be 100% sure it's not there. Raise the issue right away. Tell your customer "Hey, there is no dragon in the box. I can't make up a dragon out of the other bricks. What do we do?" 

People are surprisingly OK with problems when they know early enough. Discovering problems early opens more possible solutions. "Shall we continue knowing there is no dragon?" "Can we buy the dragon alone?" "I can see a dinosaur in the box. Can we use it instead?"

## **4. **Draw a clear line****

When you start working on a new feature for an existing system, start by defining how it interfaces with the existing code. Of course you should try and follow SOLID principles etc. but the key part is simpler than that. Just try to make the touching surface as low as possible.

The simple process of clearly defining the cut will improve your solution. It will force you force you to tackle the key questions: _How will the users or system use my code?_ _What inputs will I get? What outputs should I produce?_ It helps you keep your eyes on the ball. 

This is even more true if you don't know much about the system you are working with yet. It is a good opportunity to explore the unknowns before diving into what you know already.

It also makes it easy to turn the feature on or off. You can use a boolean flag or a more advance feature toggle mechanism.

**LEGO analogy**: Say you need to build an extension of the castle. Requirements are rather high level so there is plenty of room for creativity. You can't touch the existing castle though. 

You could go and build a great extension only to find out there is no space to attach it to the castle anywhere. That's unfortunate. You'll have to quickly alter your extension to make it fit somehow. 

The right approach would be to think of the touching surface first. Where will the extension be on the castle? What bricks can I attach it to? What form do they have? Put together the few bricks of the extension attaching it to the castle. Verify they plug for a solid connection. From there you can freestyle any extension you want.

## **5. Don't be too DRY**

DRY stands for Don't Repeat Yourself. That is probably the easiest rule to follow. As soon as you see duplicated lines of code, you make an abstraction. It can be a base class, a helper method, whatever.

What happens then? The next person comes and the common code needs to change to cover more cases. They add parameters and if statements to cope with the emerging complexities. Soon, the 5 initial and simple lines become 30 lines and it's difficult to figure out what is happening. 

**Poor readability is not a good trade for code repetitions.**

It would have been better to keep the duplicated lines. You could then change each instance at will.

The next time you reach for "abstraction over repetition", ask yourself: how many times did you see someone go back from an abstraction? Like removing a base class and putting the common code back to the inheriting classes. I bet the answer is never. 

The reason is abstractions and design patterns in general are cool and sophisticated. And if one exists then "there must be a good reason". So once you introduce the abstraction, there is a good chance it will stay there forever.

Does this mean you should never use abstractions? No. User abstractions when they fit requirements. Things like:

* "We want to log every call to this method with inputs outputs"
* "We want to log every HTTP requests with data a, b, c"
* "Every time a user is created we need to do this and that

These are good candidates for abstraction and there are many more examples. But notice how the requirements are more technical than business related (logging, security, analytics, etc.). It is rare that abstraction friendly requirements are part of your business domain. 

Why? Because the business domain is close to the real world. And that we can't control. Assumptions made at the beginning of a project often fall short pretty soon. Don't over engineer code just to avoid repetition.

**LEGO analogy**: None. There is no DRY concept in Lego bricks.

# **Takeaways**

  
Working smart is not about better code. It is about figuring out what needs to be done, and safely progressing toward the goal. 

Large and challenging development tasks will carry unknowns. Embrace it. Learn to work with it.

You will be more productive if you keep things simple and align expectations for the outcome with your team, boss, customer, and ideally everybody.

Thanks for reading!

Originally published on [The Fire CI Blog](https://fire.ci/blog/the-hero-developer-who-knew-how-to-build-lego-bricks/).

