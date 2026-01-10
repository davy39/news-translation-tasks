---
title: What is the Difference Between Coding and Programming?
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-03-17T16:28:00.000Z'
originalURL: https://freecodecamp.org/news/difference-between-coding-and-programming
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/key-difference-between-coding-and-programming--2-.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
seo_title: null
seo_desc: "It took me a long time to understand what the terms programming and coding\
  \ really meant, and what each field entailed. And I'm sure I'm not the only one\
  \ who felt confused by those two terms when I was new to tech. \nFor a while I thought\
  \ that they wer..."
---

It took me a long time to understand what the terms **programming** and **coding** really meant, and what each field entailed. And I'm sure I'm not the only one who felt confused by those two terms when I was new to tech. 

For a while I thought that they were the same thing, and it took me some time to understand that there are differences between the two "worlds". 

In this article, I'll explain the basic differences between coding and programming and how they work collaboratively to develop apps and sites.  

So let’s explore these terms and how professionals use them by first understanding what they mean.


## What is Coding? 
![what is coding](https://www.freecodecamp.org/news/content/images/2021/10/Untitled-design.png)
You might have seen courses, bootcamps, or articles talk all about coding – so why is the emphasis on this term?

This is because the actual act of coding makes it possible for us to do all the cool stuff we do every day. It lets us use mobile apps, work with different software and operating systems, and even play the games we love or visit the website you are reading this article on. It's all made possible through coding. 

So, what is coding in simple terms?

We can define coding as the act of translating instructions for a computer from human language to a language a machine can understand. This code tells the computer how to behave and what actions to perform.

If you want to become a coder, you'll need to have some basic knowledge about programming language(s). When I say programming languages, I mean languages like: Python, Java, Go, PHP, or JavaScript, just to mention a few.

Below is a good example of some code written in the Python language, that will convert any *PDF* into an *Audiobook*:
```python
import PyPDF2                     # pip install pypdf
import pyttsx3                    # pip install pyttsx3
from tkinter.filedialog import *  # pip install tkinter

book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
```

## What is Programming? 
![what is programming](https://www.freecodecamp.org/news/content/images/2021/10/fresh.png)
You've probably also heard people say, *"I am a programmer"*. And some of them who use this term have an understanding of what the terms means while other don't. If you don't know what exactly programming means, let's try and shed some light by understanding what programming is all about. 

Programming is the process of creating the instructions that will tell the computer how to perform a particular task given to it. You do this using programming languages like: 

![Programming languages](https://www.freecodecamp.org/news/content/images/2021/10/fresh--1-.png)

When we talk about programming, think of something like a remote control for your TV – it will wait for you to give it instructions by pressing different buttons which then tell the TV to perform a specific task (like changing the channel, increasing the volume, and so on). Well, this is the same way programmers can instruct a computer to do various things. 

With programming, you can almost do anything – like programming robots to help with house chores, or even programming self-driven cars like Tesla. 

In order for a programmer to develop a program that will implement their idea, they need to carry out the following steps: 

* Planning the structure of the app (*with the help of tools like Trello*)
* Designing it (*by using tools like Figma or Adobexd*)
* Developing it (*by using their programming language of choice*)
* Testing its features
* Deploying it (*on either free or paid hosting services*)
* Maintaining it after it's finished.

So as you can see, we can say that programming does not only deal with the actual writing of the code. It also involves using data structures and algorithms, and in general dealing with the bigger picture of creating and developing complex systems.

## The Difference between Coding and Programming 
![DIFFERENCES BETWEEN PROGRAMMING AND CODING](https://www.freecodecamp.org/news/content/images/2021/10/fresh--2-.png)
We will divide the differences in four main categories which will help us break down the concepts and understand them better. 

### The terminology

*__Coding__* deals with writing code in a language understood by both machines and humans. The main aim of coding is to provide communication between the two (humans & computers). 

*__Programming__* involves creating an outline and structure for the program’s code that follows certain standards, before the actual code is written to preform the task it needs to perform.

### The tools you use

When it comes to *__coding__*, one of your most important tools will be your text editor (like Notepad, or something more complex and feature-rich like Visual Studio Code, Sublime, Atom, or Vim). 

When you're talking about *__Programming__*, on the other hand, you'll need some additional tools. As a programmer, you'll be performing document reviews, doing lots of planning, thinking about design, and so on. 

To help you with these tasks, you'll use tools like more advanced code editors, analysis tools, debuggers, modelling frameworks, assemblers, modelling algorithms and more.

As a programmer you will need to have a lot of experience using these tools and more exposure to the processes that developers use to build apps and other products.

### Your Level of knowledge

As a *__coder__* having basic knowledge of a programming language and its syntax is a good start. Once you know how to code in one language, it's easier to learn others. And again, your main purpose is on writing the actual code that tells the machine what to do.

On the other hand *__programmers__* need more knowledge to begin with. You'll need to know how to create and work with algorithms, how to design websites, how to debug and test your code, how to manage projects, and of course how to work with programming languages. 

Problem solving, critical thinking and analytical skills are also essential when you're developing complex systems.

### The end product

As a *__coder__* your expected outcome is typically a simple solution that, after compiling, will successfully give your desired output. A good example is the one we gave earlier – converting a PDF into an audio file. 

On the other hand a *__programmers__* will work to give a whole working application or piece of software that people will use in the market. They're also responsible for following up and maintaining what they build to ensure it's running smoothly without any glitches.

## How Coding and Programming Work Together
By this point I hope you are able to tell the difference between coding and programming and what the two deal with. Now, let's see how the two can (and should) work closely together to accomplish a lot. 

To better understand the how, let's begin by providing a real scenario where both coding and programming will be required to work closely to produce a complete working app.

Imagine you have been asked to create an app that will help monitor or keep track of your daily routine or monitor your daily expenses. By using the concepts of the two worlds this is how you will accomplish the task.

You will need a programmer, who will be able to:
* plan the structure of the app (*with the help of tools like Trello*) 
* Write down the main features of the app, what users are expected to use  it for, etc
* Design the app (*by using tools like Figma or Adobexd*) 

After completing these steps, the coder's role comes in play. They take the ideas the programmer creates and transform it into a machine-readable form by writing code to perform the tasks specified. After the magical process of coding, the programmer comes back in play. 

The programmer will then asses the code and check for errors, run tests and check that everything is working correctly and that the code gives the expected result. If all this checks, the application is now ready for deployment and maintenance – which remains in the hands of the programmer.

This simple example explains how the two skills can be used together for productivity.

And just a final point: a "coder" and a "programmer" aren't always two separate people. They can be one and the same person who performs all these tasks.

## Wrap Up

Where do you belong in the two worlds? It took me time to figure out what am really interested in. 

If you are more interested in logic, trying putting your energy into the whole process of programming. If you really just enjoy reading and writing code, then invest your time in coding. 

As we know, computer science is a very wide field and it is still evolving. Work on finding the path you want to explore and focusing on it – just make sure to enjoy it and have fun, too. 

If you are still struggling, I hope this article has shed some light and helped you find your place. 

Thank you for reading this far. If you enjoyed this article, please share it so you can help another developer find their path.

Connect with me at:  [Twitter](https://twitter.com/larymak1) | [LinkedIn](https://www.linkedin.com/in/hillary-nyakundi-3a64b11ab/) | [GitHub](https://github.com/larymak)

Enjoy Coding ❤


