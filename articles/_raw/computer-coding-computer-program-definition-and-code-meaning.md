---
title: Computer Coding – Computer Program Definition and Code Meaning
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-03T17:32:46.000Z'
originalURL: https://freecodecamp.org/news/computer-coding-computer-program-definition-and-code-meaning
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/alexander-sinn-KgLtFCgfC28-unsplash.jpg
tags:
- name: beginner
  slug: beginner
- name: coding
  slug: coding
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'When you start learning to code, one of the questions you probably ask
  yourself is "What lannguage should I learn first?"

  One of the most exciting – and at times overwhelming – things about learning to
  code is just how much there is to learn.

  But ins...'
---

When you start learning to code, one of the questions you probably ask yourself is "What lannguage should I learn first?"

One of the most exciting – and at times overwhelming – things about learning to code is just how much there is to learn.

But instead of just focusing on learning one specific technology, it can also help to learn the foundations – the building blocks. You can peel back the layers of abstraction to get to know the underlying principles that all technologies have in common.

Understanding what coding is at a fundamental level will make solving problems easier and will give you a better understanding of how different technologies work underneath the hood.

This article goes over the fundamentals of computer coding and what programs are made of, while also giving some suggestions on how to start taking your first steps in learning how to code.

## What is coding? A definition for beginners

Computer coding, also known as computer programming, is a way to tell a computer what to do.

Coding is a way to tell the computer how it should behave overall - the exact actions it needs to take and how to take them in an effective and efficient way.

Specifically, coding is the process of creating and then giving the computer a detailed set of instructions to be carefully executed in sequential order.

The set of instructions are called a **program** or the **code**.

Computers are incredibly clever machines, but they rely on humans for getting things done.

In a nutshell, coding is the art of humans communicating with computers. It helps us solve problems and create helpful new tools for communities, such as apps or websites, and lets us analyze and process large sets of data.

### An overview of the coding process

Coding is all about problem solving.

When writing code, you'll be taking a problem and breaking it down into smaller and smaller steps of action, using logical reasoning, to finally come to a conclusion and solution.

Computers take everything literally and pay extreme attention to detail.

Making a small mistake in your code – such as a typo in a word, a missed semicolon, telling a computer to repeat a certain action but not telling it how and when to stop repeating it – will all result in an error message.

These mistakes are called **bugs** in the code.

The process of identifying the possible mistakes, finding what is causing the problem, and then fixing the mistake so the code works as it was intended to is called **debugging**.

This is a critical part of writing code and learning how to code in general.

### Why algorithms are important in coding

Figuring out the exact instructions to give the computer so it can accomplish specific tasks is the most difficult part of coding and problem solving.

Computers make no assumptions and they do exactly as they are told. This means that there should be no ambiguity in the instructions they receive.

Instructions need to be defined clearly, with the correct number and order of steps the computer should take to solve a problem.

The set of step-by-step, ordered instructions for solving problems and for the computer to complete every single task are called **algorithms**.

Algorithms are sequences of actions that need to be correct, efficient, precise, and to the point, and they should leave no room for misinterpretation.

Algorithms are not only reserved for computers to follow. Humans use algorithms on a daily basis, too.

An example of a type of algorithm we use frequently is following a cooking recipe.

The recipe is the algorithm. You need to follow the series of steps in the recipe in the correct order to get the end result you want.

#### How to write pseudocode to plan out algorithms

The way to organise, plan ahead, and write down the steps you need to follow, or the algorithm, is to first write **pseudocode**.

Pseudocode is an informal way to represent algorithms.

There is no specific syntax to pseudocode. It is written in plain, readable English (or any other natural, human language) using some technical terms.

The purpose of writing it is solely for the programmer to understand the reasoning and logic behind the code/steps that need to be written to solve the problem, using simple phrases.

After doing so,the programmer writes code that is actually executed by the computer.

Pseudocode is a simpler version of computer code and is the first step before any computer code gets written.

For example, say you wanted to write a program that aksed the user to enter their password and checked if it was equal to '1234'. 

If the password was equal to '1234', then you'd let them into the system, otherwise they would be rejected.

A simple version of that written in pseudocode could look something like this:

```
user_password = input: "Please enter your password to sign-in: "

if user_password is equal to '1234'
    let them into the system
else
    tell them they entered the wrong password
```

You can then build on that code later, as you went on.

For example, if they entered the wrong password you could ask them for it again.

If they entered it wrong more than 3 times, they would be rejected from the system.

```
correct_password = 1234
attempts = 0

while conditions are true
     user_password = input: "Please enter your password to sign-in: "
     attempts = attempts + 1
     if user_password is equal to correct_password
         let user in the system and stop the program
     if user_password is NOT equal to correct_password AND attempts is greater than 3
         don't let user in and stop the program
```

## How programming languages bridge the communication gap between humans and computers

### The language computers speak

Computers at their core only speak one language - **binary** or **machine code**.

It's a base-2 numerical system, comprised of only two possible numbers: `0` and `1`.

This ties in well with the fact that computers are powered by electricity, which has only two possible states: `off` and `on`.

Inside computers there are millions of microscopic switches, or *transistors*, that control the ebb and flow of electricity. 

So, essentially computers understand only `no` and `yes`.

Values are represented by transistors being either **off (or 0 or no)** or **on (or 1 or yes)**.

Underneath the hood, everything is represented in that state. 

Binary, or machine language, is the lowest level of language as it's the closest to the machine. 

Instructions are represented only in numbers, sequences of 0s and 1s (also known as binary digits), which directly control the computer's CPU ( Central Processing Unit). Each machine architecture has it's own unique machine language.

This language is incredibly fast as there is no need for any kind of conversion – but it's not easy for humans to use.

It's error prone and time consuming. 

Binary was used in the early days of computing, but these programs written in binary were tricky to understand and read.

There was a need for languages that were easily understood and interpreted by both humans and computers.

Throughout the years, programming languages have evolved. These evolutions are called levels, or *generations*.

Binary is the first generation of programming languages (or 1GL).

As programming languages progressed throughout history and new ones were developed, they started to look more like the languages humans use.

### Introduction of Assembly Language

The second generation of programming languages was Assembly language (2GL), which was a major leap forward and improvement in writing programs compared to using machine language.

It was still a very low-level language, but Assembly introduced alphabetical letters to programs, otherwise known as *mneumonic codes*, which made it easier to understand and use. 

In Assembly there is a strong correspondence between the instructions used in the language and the underlying computer's architecture.

So, there is a correlation between the mneumonics in the language, and the machine's native binary instructions.

Assembly introduced a translator, called an *assembler*, to convert programs written in it to machine language (since that is the only language computer programs can be executed in).

Assembly was more readable and easier to use and debug, but it was still very error prone and tiresome to write programs in.

### The introduction of higher level programming languages

Following Assembly language, the third generation programming languages (3GL) came along. 

They paved the way to a new style of programming, making it more accessible to people and moving further from the native language of machines.

These languages were called higher level languages - that is languages that are easier for humans to read, write, and understand, since they resemble an English-like way of writing.

They are machine independent, with more levels of abstraction away from the machine.

Translators called *compilers* were introduced to translate the code programmers wrote in such a language (also known as source code) to machine executable binary code.

Such languages included BASIC, FORTRAN, COBOL, PASCAL, and others that are popular and frequently used to this day, like C, C++, Java, and JavaScript.

Fourth generation languages followed (4GL), which were faster and even easier to use, with more layers of abstractions from the computer. And they looked more and more like human languages.

They increased productivity as programmers no longer had to take the time to tell the computer *how* to solve a problem. 

Instead, they focused on just telling the computer *what* to do, without the additional steps on *how* to do it.

Fourth generation languages include scripting languages such as Python and Ruby, but also query languages, used to retrive data from databases, such as SQL (Structured Query Language).

Finally, fith generation programming languages (5GL) are based on Artificial Intelligence.  

Computers are trained to learn how to solve problems, without the programmer needing to write algorithms.

Some of the languages used include Prolog and Mercury.

## Why should you learn to code?

Coding is a powerful tool.

It allows you to solve a problem in unique and creative ways and gives you the chance to bring an idea to life.

By learning to code you may be able to make a dream of yours a reality and bring a vision you have to fruition.

Coding also helps you understand the constantly changing digital world around you.

Pretty much everything you use on a daily basis runs on code - from looking for directions to a particular destination, to ordering items online, to apps that track the steps you have taken that day.

Coding is used in every single industry, so knowing at least the basics of coding will give you that extra competitive edge when looking for a new role or for a promotion.

Also, there's no shortage of IT and programming jobs out there right now. On the contrary they are growing and that growth doesn’t seem to be easing off anytime soon (despite theories that Artificial Intelligence will eventually replace programmers).

Besides these reasons to learn to code, coding makes for a fun new hobby and productive passtime. 

Coding is for everyone no matter their age, their background, or where they are in life. 

You don’t need a four year college degree to get started. You can [begin learning for free](https://www.freecodecamp.org/learn/), from the comfort of your own home. 

Anyone can learn to code if they want to.

## How to start coding

There are many programming languages out there, and as a newbie it can get overwhelming choosing the first one to learn.

To get started, think of a problem you want to solve and then research what technology would help you reach your goal.

For example, if you want to create a personal website, you wouldn't start by learning Java or C++.

A good starting point for beginners could be the following:

- HTML (Hyper Text Markup Language), which is the bones of every webpage. It displays all kind of content you see on websites - from text, to links, images and videos.
- CSS (Cascading Style Sheets), which makes the HTML look pretty. It is used to change the font styles and colors of websites, and also it is used to make a website responsive and usable on every device.
- JavaScript, which adds functionality and interactivity to otherwise static web pages.

freeCodeCamp has a well thought out and extensive, interactive curriculum. It helps learners take their first steps in coding and helps them land a job with the new skills they acquire.

Check out the [Responsive Web Design Certification](https://www.freecodecamp.org/learn/2022/responsive-web-design/), where you'll build  projects that you can add to your portfolio to showcase your skills to potential employers.

freeCodeCamp also has a [YouTube channel](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) with free, full-length courses on a wide variety of tech topics.

And there's also the friendly freeCodeCamp community that can help you when you get stuck and support you throughout your coding journey. So make sure to engage in the [forum](https://forum.freecodecamp.org/) when you need help.

## Wrapping Up

Coding is a skill that cannot be learnt overnight, so don't rush the process!

Like learning any new language, learning to code takes time,patience, consistent practice and lots of trial and error.

As quoted by Beverly Sills, and shown on [freeCodeCamp](https://www.freecodecamp.org/learn/) as one of the inspirational quotes:

> There are no short cuts to any place worth going.

Thanks for reading!


