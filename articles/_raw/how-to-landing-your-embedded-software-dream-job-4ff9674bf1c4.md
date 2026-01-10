---
title: How to land your dream embedded software job
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T16:39:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-landing-your-embedded-software-dream-job-4ff9674bf1c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*doISq7nDJgKnuvp9UjlALA.jpeg
tags:
- name: careers
  slug: careers
- name: Computer Science
  slug: computer-science
- name: embedded systems
  slug: embedded-systems
- name: interview
  slug: interview
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Rohan Dasika

  Guides on preparing for software interviews are aplenty. Embedded software interviews
  are somewhat similar, but it’s still a different game you have to play.

  There is some helpful material on the Internet and some content for software...'
---

By Rohan Dasika

Guides on preparing for software interviews are aplenty. Embedded software interviews are somewhat similar, but it’s still a different game you have to play.

There is some helpful material on the Internet and some content for software interview prep does carry over. But in general, I wasn’t able to find a comprehensive guide to get me started.

Recruiting and doing interview prep for embedded software over the last 4 months taught me a great deal about how to approach the process. I recently received offers from a few big tech companies. In this post, I’ll be sharing some insights I gained along the way.

I’ll be dividing this post into a couple sections, so feel free to jump around! There are already tons of content on smart ways to recruit, so I’m not going to go into how to get interviews here.

* Content to prepare and review
* The interview itself!

### Picking a language

As a standard, embedded software development is mostly done in C, although C++ is becoming more popular recently. If you’ve taken any computer architecture or embedded systems courses, you’ve probably used one or the other. Make sure you know which language the company you’re interviewing with uses. If you’re more familiar with C++ but they use C, be upfront about that — if you know one, you’ll be able to switch between the two fairly easily.

Since I’m most familiar with C++, companies have allowed me to write code in C++. If necessary, they helped me transition that code to C. For the most part, it doesn’t really make a difference. This is unless you’re working with some specific C++ standard library functions and containers.

Verilog is used mostly for FPGA development. Python is used a fair amount to communicate between the user and the embedded system they’re working on. Chances are you won’t be asked any questions on those.

Same goes with assembly language (thankfully!! ?).

### The basics are the basics

I began the journey in a similar fashion to most computer science students — by reviewing my data structures and algorithms. But soon, I realized that content for embedded software splits off at a certain point. It’s _much_ more focused on computer architecture, operating systems, and some hardware fundamentals than higher level data structures like trees or sorting algorithms.

You deal with lower level code and hardware in embedded software roles. But from a programming standpoint, your data structures and algorithms are still _highly_ relevant. Similar to software interviews, there are tons of resources to help you prepare for the basics! Doing a few problems from each section in [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X) was a good starting point.

Quickly after that, I preferred to use [LeetCode](https://leetcode.com/) due to the capability to run and test instantly. LeetCode is an incredible platform with a great community. In my opinion, has questions _most similar_ to ones you’ll encounter in interviews. It saves all your submitted solutions and calculates runtimes as well. Do most of the “Easy” and a decent portion of the “Medium” questions and you should be okay :)

Additionally, [Geeks For Geeks](http://www.geeksforgeeks.org/) is a great resource with very thorough explanations for hundreds of problems.

#### Carry-over from Software Interviews

The following few topics are very similar to the concepts from software interviews, and these are tested heavily, so make sure you know them well!

* Algorithmic complexity (both time and memory)
* Pointers
* Arrays
* Linked Lists
* Strings (and C-strings)
* Stacks & Queues

The following topics aren’t really tested, but be familiar with them conceptually. Know how they work, their complexities, and how to solve them at a basic level.

* Recursion
* Trees
* Heaps
* Hashing
* Sorting

### Beyond the Software

This is where the real embedded stuff starts!

![Image](https://cdn-media-1.freecodecamp.org/images/H-cg252SKkDHBoTxRqvVExi2Re4dWEbJFJQz)

#### Bit manipulation!!

Know this like the back of your hand.

It’s possibly the **most important** topic of your interviews. On this specific topic, do _all_ the questions on LeetCode.

* Know how negative numbers are represented in binary
* Know the differences between one’s and two’s complements
* Be able to convert between binary, decimal, and hexadecimal
* The XOR operation is _powerful_. Know what all it can do.

[Here’s a great resource](https://discuss.leetcode.com/topic/50315/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently) I used for helpful tips and tricks

### Computer architecture

A close second to bit manipulation.

You probably won’t be asked to implement any of these, but you definitely will be asked about how things work underneath the hood. Some topics to read up on include…

* Important registers and how they work
* Difference between caller-save and callee-save
* How interrupts work
* A basic understanding of instruction pipelines
* Caches, TLBs, and how virtual memory is implemented
* Various types of memory (ROM vs RAM, DDR, EEPROM, Flash, etc)
* Memory padding (instructs & classes)
* What happens when you boot a system

#### Operating Systems

Depending on the company and the role, operating systems can be a _very_ important topic. You won’t be asked to implement any of these, but know how things work at a conceptual level!

* Process vs. Thread
* How multi-threading works
* Real-Time Operating Systems vs traditional OS
* Task scheduling (FIFO, Round Robin, Priority-based)
* How semaphores & mutexes protect data
* Priority inversion, priority inheritance, spinlocks, and deadlocks
* What makes a function ‘reentrant’?
* Critical sections
* Priority levels in microcontrollers (EL0 — EL3)

#### Communication Protocols

Know the benefits and tradeoffs of using the following protocols:

* UART
* SPI
* I2C

Based on your previous experiences, the role you’re applying for, and the company, you may be asked about others as well. Typically, companies don’t expect you to know about these specific protocols and will train you on the job. But having a basic understanding can always help wow the interviewer!

* **Automotive:** CAN, LIN
* **Wireless:** 3G, 4G LTE, basics of 5G, 802.11(Wifi), Bluetooth
* **Networking:** HTTP, TCP/UDP, IP, 802.11(Wifi), Ethernet

#### Hardware Fundamentals

Hardware isn’t tested a whole lot for embedded software, but depending on the role, your level of interaction may vary. Check the job descriptions and talk to people who work there for a better idea!

* Watchdog timers
* Timers in general
* Details about _any_ peripherals you may have used in your projects (accelerometers, any sensors, LiDAR, motors, etc)

### Practicing

**Practice is key** — there’s really no way around that. Make sure to dedicate _at least_ 2 hours a day for interview prep, not including applying for jobs and reaching out to recruiters.

![Image](https://cdn-media-1.freecodecamp.org/images/GT7z8aGsV2fxl4P2D8Vqa7vVGBWppn5wCXMQ)

While practicing on LeetCode, comment your code. Explain your algorithm and the runtime complexities. Every day before you begin coding, review the problems you worked on the previous day. At the end of the week, review every problem you worked on that week. This’ll help you remember the algorithms better and bit by bit, you’ll become a pro at pattern matching.

Embedded interviews tend to be more conceptual than your typical software interviews, due to the nature of some of the topics tested. For these areas, I maintained a Google doc of all the questions that I might be asked, but also all their answers. I also included a link to where I can read more information to be helpful. It helped me stay organized and review faster.

> A lot of people have asked me for the link to the Google doc, so here it is: [Embedded Interview Questions](https://docs.google.com/document/d/18HMyd-lFu1hWiixFLS2Pc7-SgyzDDqitzXbfAnUVeBE/edit?usp=sharing)

### At the interview

You made it — great job!

Take a deep breath. It’s time to put all your hard work to good use. Usually, you and the interviewer will go through a few conceptual questions. You will also discuss your previous experiences and projects. Make sure you’re able to answer questions about your contributions and various challenges you faced in detail.

If this is an interview that’s happening remotely, you’ll probably be asked to code in a shared document. Have some paper ready to jot down important points and diagrams. If it helps, you can also have some notes that you can refer to during the interview. I always keep a sheet of basic algorithmic complexities handy.

Check the timezones. Double check them. Don’t forget to use headphones. Be in a quiet environment so there are no disturbances. Communication issues are only going to make the interview more difficult.

![Image](https://cdn-media-1.freecodecamp.org/images/tz9ML84FNkxqAsD8TFCW47fa9z72LsPIAVqm)

#### When you get the question

Never start coding right away. As important as arriving at the right solution is, the interviewer is really looking at your approach.

Take a second and repeat the question back to the interviewer, just to make sure you both are on the same page. And if there are any misunderstandings, the interviewer can always repeat and clarify any doubts.

Next, understand the scope of the problem

* How big is the input?
* Is it sorted?
* Is there a certain time or memory complexity that you should meet?
* Are there duplicates? Negative values? Empty values?
* Do you have to perform error checking?

Then, walk through your algorithm. Start off with the most basic, brute-force approach. It can be super inefficient and mention that you’re using this as a starting point. Explain the time and memory complexities and why it’s a poor solution.

From there, it’s time to optimize. Generally look for places where you might be storing unnecessary amounts of data or repeating sections of code. For embedded applications, memory is important! Instead of using an array or vector, consider using a bitset. If you’re just dealing with values between 0 and 31, toggle bits in an integer! This is where bit manipulation comes in handy.

It’s important to think out loud while you’re brainstorming. If you’re stuck or heading in the wrong direction, the interviewer can help bring you back on track. Once you’ve both agreed on a solution, then it’s finally time to start coding.

#### Writing code

Reading others’ code isn’t always the most enjoyable thing. Make the job a little easier for your interviewer by using good style. That doesn’t mean that you have to put down _every_ semicolon or bracket, but indent well and use meaningful variable names. Try to write neatly and use the whiteboard space well.

While you’re writing code, keep checking against the algorithm you’ve devised. Similar to the brainstorming phase, _think out loud_. Provide verbal comments to your code. At each step, explain what you’re checking, what you hope to achieve, and any design decisions you make.

After you’re done writing code, don’t say you’re done yet. Take a step back and analyze your code from a high-level perspective. Check the inputs, the outputs, and your logic for any bugs. Be sure to spot any off-by-one errors! Then, walk through the code with a few test cases. If there are any issues that you see, review and rework your code as necessary.

Depending on the interview, you might have one big question or a couple smaller ones. But once the interviewer has agreed with your solution, there is a chance he or she might extend it different parameters. You probably won’t have to rework the code, but you might have to discuss how to change parts of your approach. Like I mentioned before, memory is important in embedded applications. So a common follow-up question is usually about further memory optimization.

### Final Thoughts

The nature of embedded software interviews is heavily dependent on the company and the work they prioritize. Companies working on a specific communication protocol will look for different things than a company developing a real-time operating system or a company working on an IoT product.

I wanted to use this article as a place to share some common themes in the interviews I’ve had, but this is by no means comprehensive. This is intended to be used as a starting point. But please reach out to current employees and check [Glassdoor](https://www.glassdoor.com/index.htm) for more company-specific interview tips.

Interviews are tough, but preparing well and working hard now can help you land a job you love :)

I hope this article helped, and wish you the best of luck!

If you enjoyed this article, please don’t forget to leave a ?. You can also follow me on T[witter](https://twitter.com/rohandasika) or Q[uora:](https://www.quora.com/profile/Rohan-Dasika))

