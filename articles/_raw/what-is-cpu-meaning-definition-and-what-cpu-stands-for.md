---
title: What is CPU? Meaning, Definition, and What CPU Stands For
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-16T22:53:22.000Z'
originalURL: https://freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/niek-doup-Xf071ws2Icg-unsplash.jpg
tags:
- name: Computer Science
  slug: computer-science
- name: cpu
  slug: cpu
seo_title: null
seo_desc: 'Every single computing device has a CPU.

  You may have heard of this tech term before, but what is it exactly? What is a CPU
  and how does it work?

  In this beginner-friendly article you''ll learn the basics on what a CPU actually
  is, and I''l give you an...'
---

Every single computing device has a CPU.

You may have heard of this tech term before, but what is it exactly? What is a CPU and how does it work?

In this beginner-friendly article you'll learn the basics on what a CPU actually is, and I'l give you an overview of how it works.

## What is a CPU and where do you find it in a computer?

CPU is short for Central Processing Unit. It is also known as a processor or microporcessor.

It's one of the most important pieces of hardware in any digital computing system – if not the most important.

Inside a CPU there are thousands of microscopic *transistors*, which are tiny switches that control the flow of electricity through the integrated circuits.

You'll find the CPU located on a computer's *motherboard*.

A computer's motherboard is the main circuit board inside a computer. Its job is to connect all hardware components together.

Often referred to as the brain and heart of all digital systems, a CPU is responsible for doing all the work. It performs every single action a computer does and executes programs.

### What are computer programs and where are they stored?

There is a program for everything a CPU does.

You have a program that lets you use your web browser or a word processor. You have one that performs mathematical operations on a calculator or lets you type letters and characters on a keyboard. And there are programs that manage clicking and selecting elements with a computer mouse and pressing down on your laptop's touchpad. 

Whatever it may be, there is a program for all computer activities.

Programs are sets of instructions that need to be executed in sequential, logical order and be followed precisely step-by-step.

They are written in a human-readable language – a programming language – by a programmer.

Computers don't understand programming languages directly, so they need to be translated to a form that is easier understood.

That form is called machine language or binary.

Binary is a *base two* numerical system. It's comprised of only two numbers: 0 and 1.

This reflects and ties in well with the only two possible states transistors  have to control the ebb and flow of electricity – they are either on (1) or off (0).

So, under the hood, programs are stored as sequences of bits. Bits are another name for binary digits (sequences of 1s and 0s).

Programs are stored permanently and long term in a storage device, whether it's a HDD (Hard Disk Drive) or SSD (Solid State Drive).

These are non-volatile types of memory, meaning they store data even when the power is off.

While a program is up and running and currently being used, though, all of its data is stored in the main, primary, memory or RAM (Random Access Memory).

This type of memory is volatile, and all data is lost when the power shuts off.

## What does a CPU do?

In a nutshell, a CPU is responsible for handling the processing of logical and mathematical operations and executing instructions that it is given.

It can execute millions of instructions per second – but can carry out only one instruction at a time.

It first receives some type of input, typically from an input device (such as a monitor display screen, a keyboard, a mouse, or a microphone) or from an application/system software program (like your web browser or operating system).

Then the CPU is in charge of four tasks:

1) **Fetching** instructions from memory, in order to know how to handle the input and know the corresponding instructions for that particular input data it received. Specifically, it looks for the address of the corresponding instruction and forwards the request to the RAM. The CPU and RAM constantly work together. This is also called *reading from* memory.
2) **Decoding** or translating the instructions into a form the CPU can understand, which is machine language (binary).
3) **Executing** and carrying out the given instructions.
4) **Storing** the result of the execution back to memory for later retrieval if and when requested. This is also called *writing to* memory.

Finally, there is an output of some kind, such as printing something to the screen.

The process described above is called the **fetch-execute** cycle, and happens millions of times per second.

![Screenshot-2021-10-25-at-5.30.18-PM](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-10-25-at-5.30.18-PM.png)

## The main parts of a CPU

Now you know the basic tasks a CPU performs for every operation happening on a computer, what are the parts of the CPU that help get that work done?

Below are some of the important components within it:

- **CU** (short for Control Unit). It regulates the flow of input and output. It's the part that fetches and retrieves the instructions from main memory and later decodes them.
- **ALU** (short for Artithmetic Logic Unit). The part where all the processing happens. Here is where all mathematic calculations take place, such as addition, subtraction, multiplication, and division, as well as all the logical operations for decision making, such as comparing data.
- **Registers**. An extremely fast memory location. The data and instructions that are currenlty being processed during the fetch-execute cycle are stored there, for quick access by the processor.

## What are CPU cores?

Earlier you learned that a CPU can typically perform just one action at a time.

It executes one instruction at a time and it does this with with the help of physical cores. 

Essentially, a core is a CPU itself, a separate device inside the main CPU chip. This means that it has the ability to do just one thing at a time.

However, modern computers have the ability to support more than one core inside the main chip. 

The more cores a CPU has, the greater the computational power and the more tasks that can be running and completed simultaneously, making the CPU a serial multitasker.

For example, there are dual-core CPUs, meaning there are two CPUs on the same chip and can run two instructions at the same time.

Quad-core CPUs mean there are four CPUs on the same chip, hexa-core CPUs mean there are six cores, and so on.

### What is hyperthreading?

Modern CPUs also support a technology called hyperthreading.

The way this works is that a single physical core appears as multiple physical cores, making the Operating System think there are more cores than there actually are. This in turn makes the computer think it has more power than it actually has.

So, in addition to the physical cores mentioned in the section above, there are also these virtual cores, or threads as they are also called.

They aren't actual physical cores, but they appear to be so.

The combination of both physical and virtual cores make the execution time of programs even faster and give CPU even more computational power.

## Conclusion

Thanks for reading and making it to the end! Hopefully you now have a better understanding of what CPUs are, what they do, and why they're so important. 

If you want to know more about computer basics, have a look [at this guide which goes over the basic parts of a computer](https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/).

Happy learning!


