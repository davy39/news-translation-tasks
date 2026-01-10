---
title: How to Learn Different Tech Stacks IRL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-25T17:11:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-different-tech-stacks
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/ilya-pavlov-OqtafYT5kTw-unsplash-1.jpg
tags:
- name: learning to code
  slug: learning-to-code
- name: 'self-improvement '
  slug: self-improvement
seo_title: null
seo_desc: "By Liz Johnson\nOver the last couple years, I've learned that being a consultant\
  \ means you have to be able to learn new things quickly.  \nAt first, this was really\
  \ scary to me. Now, as someone who has had to learn several new tech stacks over\
  \ the last..."
---

By Liz Johnson

Over the last couple years, I've learned that being a consultant means you have to be able to learn new things quickly.  

At first, this was really scary to me. Now, as someone who has had to learn several new tech stacks over the last year, it’s still a little scary to me. But I’ve also learned several strategies about how to learn things effectively. And that's what we'll cover here.

## Learn the Framework's Supporting Language

Frameworks are written to speed up development in specific languages. Many times, engineers who are learning a new tech stack on a fast paced project will learn the framework before they really learn or understand the language that it’s built for. It makes sense, though, because if you can learn the framework and a little bit of syntax you can usually start operating in the codebase faster. 

When you have deadlines approaching and you need to get stuff out the door quickly, the tendency is to learn exactly what you need to deliver.  “What exactly you need to deliver” is probably open to interpretation and existential debates, but in general, it seems that when engineers figure out the framework they can write enough code to get the thing working.

You will quickly hit a ceiling with this approach, though. I realized this when learning Ruby on Rails. I “learned” Rails before I really learned Ruby. 

Ruby is pretty different from other languages I had operated in before, but because I could find the patterns in the framework I was able to operate in Ruby on Rails ok for a while. Until I couldn't.  

When it came to really understanding Rails so I could get more creative in how I used the framework to fit non-basic needs, I realized that if I didn't know Ruby then I didn't know Rails. Without understanding Ruby, I couldn’t follow the source code to really understand how Rails was built.

In order to learn Ruby, I got a book and started reading. Things started clicking that hadn’t before, and I quickly moved from just being able to “operate” in Rails to actually understanding the parts of Rails I was in. 

I could read and follow the source code because I could read the language it was written in. This meant I could solve less standard problems in clean and effective ways.  

## Read the Docs

Recent framework and library documentation seems to generally be pretty well-written. There’s great descriptions of the things that you can do and then code examples of how to do it. Why would you not want to read that?   
  
Well, it may be because we all have 40 hours in our week that get filled with meetings, code, bugs, failing tests, random machine restarts, deadlines, weird system behavior, and so on. 

It also could be because when we read documentation it doesn’t seem to stick as much as we might hope. We don’t read it and then feel like we can teach it. And after one pass we usually don’t feel like we know everything to write the code we need to deliver by next week.  
  
But reading the documentation will let you know the things that you _can_ do with the framework. You won’t absorb it all and come out an expert, but you can go back to the code you are supposed to write and have some idea of how you might accomplish your task.  

You will likely get stuck again (even though you just read about that thing) and you will go back to the docs again. Then you will read them again, but this time focused on a particular section and you will read them more slowly. You’ll think through each sentence this time and let it sink in. 

Then you’ll go back to your code and know everything! Just kidding. You might still be stuck, but you will try a few things, and then maybe read that one section one more time. And then it will click. It will work. The documentation was right, you CAN do that thing it promised :) And next time you have to do that thing it will seem easy.

If you don't read the docs, you'll develop the tendency to hack at the thing until it works. You will model your patterns not off the patterns that the framework has built and established but rather the patterns that you know from previous experience in other things you think are similar.  

Instead of using the framework to your advantage, you are making more work for yourself (and likely a bigger mess) than if you had never used it at all.

## Don’t Pretend You Get It

If you happen to be lucky enough to get to work with an expert in the framework, don’t ever pretend that you understand things you don’t. This expert probably doesn't have an infinite amount of time to answer your questions, but don’t let yourself settle for “I think it makes sense” if it doesn't. 

With a limited amount of their time, I recommend you take notes on the things that they say and listen as carefully as possible. Re-explain back to them the things that they explain to you and try not to get too shaken up when you ask “Is that right?” and they respond “no”.  It’s better to know that you don’t know right then, rather than wasting time thinking the thing works only to have it not work when you need it the most.

If you don’t have time to re-explain ideas or concepts back, take their recommendations and capture the key words from the things they proposed. Then you should read at greater length about those topics and ideas. Finally, take what you read, the problem that you had, and the things they said and see if you can succinctly summarize the problem and the solution and why you landed on that solution. 

If you feel comfortable, and your explanation is indeed succinct, send that explanation in a message to them asking them to confirm your understanding. I’ve yet to find a person who doesn’t receive that well enough to at least respond “yes you got it” or “no not quite”.

If you aren’t lucky enough to have the expert, have the same resistance to “just sort of getting it” as you read about the framework or look through the source code. You won’t be able to ask someone “Is that right?” but you can still check your understanding. 

## Find the Debugger and the REPL

If you can figure out how to run the application and set a breakpoint, you have just set yourself up to be able to learn so much more so much faster! 

Breakpoints let you stop the flow of execution in what you think is the flow of the application. If you want to validate that a function is getting hit, and that its input is equal to a certain value on a certain iteration, setting a breakpoint in the function can tell you if you things are flowing the way you expect. Breakpoints let you run the code one line at a time and inspect the outputs so that you can understand each step. 

Print statements aren’t as good, but can suffice if you need them. Breakpoints will change your life in the best way and it’s really important you figure out how to get a hold of them.

[REPL’s](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) are also your friend. REPL stands for Read-Eval-Print Loop. These are small environments set up to run commands in the language or framework that you are working in.  

I used this a lot when I was learning list comprehensions in Python. I could run a simple example to assess my understanding that looked something like this:

```
> my_list = [1, 3, 5]
> doubled_values = [ num*2 for num in my_list ]
> print(doubled_values)
> [2, 6, 10]
```

If what you are trying to test requires a lot of data setup a unit test would be better. But if you think you understand how something works but want to check your understanding, it's a great idea to fire up the REPL and build a small example.  

Think about what you expect to happen when you run certain commands and then run them to see if what you expected was what ended up happening. If the result was totally unexpected then you essentially just asked “Is that right?” and the computer told you “no”. 

## Learn How to Test It

This one feels really hard when you are learning a new framework/language because the test framework is yet again different and new. But if you can write good tests for the thing you are trying to deliver, then you can fumble through the implementation and feel confident that you are still getting what you need. 

Tests are especially helpful when operating a new tech stack because you will not write your code the best way the first time (this is probably always true but definitely true in new frameworks). You will want to give yourself space to rework things and refactor as you go.  

Solid tests will allow you that flexibility. They will give you more space to try things, break things, and fix things while you get yourself more comfortable in the code.

## And Repeat

I’ve wished a million and two times that “I knew it all by now”. Because every single step above will likely make you feel uncomfortable. You may go through all of the above steps and learn how to do one thing in the framework really well. The next time you have to do it you won’t even think about it. You’ll just do it.

And then you will need to do the next thing. And then you will have learned enough things that you get by for a while feeling pretty good. Until you hit the next thing you have to learn and you need to feel uncomfortable again. And it will happen again and again and again for a really long time (or maybe forever? I haven’t reached the end yet).

 But each time it seems to feel a little easier and a little quicker to get to the information you need. It used to take you several days to get one small thing working and now it takes you half a day. But you were so busy learning and delivering that you forgot that it used to take you 4 days to do what you can now do in 4 hours. 

So the last, and perhaps most important, thing in learning new tech stacks (and learning new anything) is to remember where you started. It’s easy for the sea of things to learn to feel infinite. It’ll feel like you’re never making progress unless you look backwards. You’ll remember how far you’ve come and you’ll feel like you can keep moving forward doing more. 

Slowly you will realize that you can enter unknown situations and feel confident that you can build not only a solution but the best solution. And this feeling is worth the hours you poured over the docs and banged your head against the wall on things that wouldn’t work. You can build amazing things and that’s so awesome!

As you get closer to that version of you that can build anything, remember to thank the co-workers or friends who have taught you and cheered you on as you learned. You wouldn’t be building these things without them.

And as you continue, you’ll start teaching others. And when they ask you “Is that right?” you will kindly respond “no” and re-explain it in all its complexities just one more time. 🙂

