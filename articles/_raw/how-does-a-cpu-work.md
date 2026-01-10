---
title: How does a CPU work?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-18T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-does-a-cpu-work
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_n3hgXdDt8zb5pvjmBi570g.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: cpu
  slug: cpu
- name: programing
  slug: programing
seo_title: null
seo_desc: 'By Milap Neupane

  CPU, also known as the microprocessor is the heart and/or brain of a computer. Lets
  Deep dive into the core of the computer to help us write computer programs efficiently.


  "A tool is usually more simple than a machine; it is general...'
---

By Milap Neupane

CPU, also known as the microprocessor is the heart and/or brain of a computer. Lets Deep dive into the core of the computer to help us write computer programs efficiently.

> *"A tool is usually more simple than a machine; it is generally used with the hand, whilst a machine is frequently moved by animal or steam power."*  
>   
> *– Charles Babbage*

*A* ***computer*** is a **machine** powered mostly by electricity but its flexibility and programability has helped achieve the simplicity of a tool.

**CPU** is the heart and/or the brain of a computer. It executes the instructions that are provided to it. Its main job is to perform arithmetic and logical operations and orchestrate the instructions together. Before diving into the main parts let’s start by looking what are the main components of a CPU and what there roles are:

### Two main components of a processor

* ***Control unit — CU***
    
* ***Arithmetic and logical unit — ALU***
    

#### Control Unit — CU

Control unit CU is the part of CPU that helps orchestrate the execution of instructions. It tells what to do. According to the instruction, it helps activate the wires connecting CPU to different other parts of computer including the **ALU**. Control unit is the first component of CPU to receive the instruction for processing.

There are two types of control unit:

* hardwired **control units**.
    
* microprogrammable (microprogrammed) **control units**.
    

**Hardwired** control units are the hardware and needs the change in hardware to add modify it’s working where as **microprogrammable** control unit can be programmed to change its behavior. Hardwired CU are faster in processing instruction whereas microprogrammable as more flexible.

#### Arithmetic and logical unit — ALU

Arithmetic and logical unit ALU as name suggest does all the arithmetic and logical computations. ALU performs the operations like addition, subtraction. ALU consists of logic circuitry or logic gates which performs these operations.

Most logic gates take in two input and produces one output

Bellow is an example of half adder circuit which takes in two inputs and outputs the result. Here A and B are the input, S is the output and C is the carry.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u-VunK6bUafXlhubpGlNkA.png align="left")

*Source:* [*https://en.wikipedia.org/wiki/Adder\_(electronics)*](https://en.wikipedia.org/wiki/Adder_\(electronics\))

### Storage — Registers and Memory

Main job of CPU is to execute the instructions provided to it. To process these instructions most of the time, it needs data. Some data are intermediate data, some of them are inputs and other is the output. These data along with the instructions are stored in the following storage:

#### Registers

Register is a small set of place where the data can be stored. A register is a combination of **latches**. **Latches** also known as **flip-flops** are combinations of **logic gates** which stores 1 bit of information.

A latch has two input wire, write and input wire and one output wire. We can enable the write wire to make changes to the stored data. When the write wire is disabled the output always remains the same.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5WDU45YAH5CnICZOOvn1Yw.gif align="left")

*An SR latch, constructed from a pair of cross-coupled* [*gates*](https://en.wikipedia.org/wiki/NOR_gate)

CPU has registers to store the data of output. Sending to main memory(RAM) would be slow as it is the intermediate data. This data is send to other register which is connected by a **BUS**. A register can store instruction, output data, storage address or any kind of data.

#### Memory (RAM)

Ram is a collection of register arranged and compact together in an optimized way so that it can store a higher number of data. RAM(Random Access Memory) are volatile and it’s data get’s lost when we turn off the power. As RAM is a collection of register to read/write data a RAM takes input of 8bit address, data input for the actual data to be stored and finally read and write enabler which works as it is for the latches.

### What are Instructions

Instruction is the granular level computation a computer can perform. There are various types of instruction a CPU can process.

Instructions include:

* Arithmetic such as **add** and **subtract**
    
* Logic instructions such as **and**, **or**, and **not**
    
* Data instructions such as **move**, **input**, **output**, **load**, and **store**
    
* Control Flow instructions such as **goto**, **if … goto**, **call**, and **return**
    
* Notify CPU that the program has ended **Halt**
    

Instruction are provided to computer using assembly language or are generated by compiler or are interpreted in some high level languages.

These instruction are hardwired inside CPU. ALU contains the arithmetic and logical where as the control flow are managed by CU.

In one **clock cycle** computers can perform one instruction but modern computers can perform more than one.

A group of instructions a computer can perform is called an **instruction set**.

### CPU clock

**Clock cycle**

The speed of a computer is determined by its clock cycle. It is the number of **clock periods** per second a computer works on. A single clock cycles are very small like around 250 \* 10 \*-12 sec. Higher the clock cycle faster the processor is.

CPU clock cycle is measure in gHz(**Gigahertz**). 1gHz is equal to 10 ⁹ Hz(**hertz**). A hertz means a second. So 1Gigahertz means 10 ⁹ cycles per second.

The faster the clock cycle, the more instructions the **CPU** can execute.Clock cycle = 1/clock rateCPU Time = number of clock cycle / clock rate

This means to improve CPU time we can increase clock rate or decrease number of clock cycle by optimizing the instruction we provide to CPU. Some processor provide the ability to increase the clock cycle but since it is physical changes there might be over heating and even smokes/fires.

### How does an instruction get executed

Instructions are stored on the **RAM** in a sequential order. For a hypothetical CPU Instruction consists of **OP** code(operational code) and **memory or register address**.

There are two registers inside a Control Unit **Instruction register(IR)** which loads the OP code of the instruction and **Instruction address register** which loads the address of the current executing instruction. There are other registers inside a CPU which stores the value stored in the address of the last 4 bits of a instruction.

Let’s take an example of a set of instruction which adds two number. The following are the instructions along with there description:

**STEP 1 — LOAD\_A 8:**

The instruction is saved in RAM initially as let’s say &lt;1100 1000&gt;. The first 4 bit is the op code. This determines the instruction. This instruction is **fetched** into the **IR** of the control unit. The instruction is **decode** to be load\_A which means it needs to load the data in the address 1000 which is the last 4 bit of the instruction to register A.

**STEP 2 — LOAD\_B 2**

Similar to above this loads the the data in memory address 2 (0010) to CPU register B.

**STEP 3** **— ADD B A**

Now the next instruction is to add these two numbers. Here the CU tells ALU to perform the add operation and save the result back to register A.

**STEP 4 — STORE\_A 23**

This is a very simple set of instruction that helps add two numbers.

We have successfully added two numbers!

#### **BUS**

All the data between CPU, register, memory and IO devise are transferred via bus. To load the data to memory that it has just added, the CPU puts the memory address to address bus and the result of the sum to data bus and enables the right signal in control bus. In this way the data is loaded to memory with the help of the bus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N5wkXycN_ceV9HByxQUzCA.png align="left")

*Source:* [*https://en.wikipedia.org/wiki/Bus\_(computing)*](https://en.wikipedia.org/wiki/Bus_\(computing\))

#### Cache

CPU also has mechanism to prefetch the instruction to its cached. As we know there are millions of instruction a processor can complete within a second. This means that there will be more time spent in fetching the instruction from RAM than executing them. So the CPU cache prefetches some of the instruction and also data so that the execution gets fast.

If the data in cache and operating memory is different the data is marked as a **dirty bit**.

#### **Instruction pipelining**

Modern CPU uses **Instruction pipelining** for parallelization in instruction execution. Fetch, Decode, Execute. When one instruction is in decode phase the CPU can process another instruction for fetch phase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FJxls8ZBHc3l3tTKxrO6Sg.png align="left")

*Source:* [*https://en.wikipedia.org/wiki/Instruction\_pipelining*](https://en.wikipedia.org/wiki/Instruction_pipelining)

This has one problem when one instruction is dependent on another. So processors execute the instruction that are not dependent and in different order.

#### Multi core computer

It is basically the different CPU but has some shared resource like the cache.

### Performance

Performance of CPU is determined by it’s execution time. Performance = 1/execution time

let’s say it takes 20ms for a program to execute. The performance of CPU is 1/20 = 0.05msRelative performance = execution time 1/ execution time 2

The factor that comes under consideration for a CPU performance is the instruction execution time and the CPU clock speed. So to increase the performance of a program we either need to to increase the clock speed or decrease the number of instruction in a program. The processor speed is limited and modern computer’s with multi core can support millions of instructions a second. But if the program we have written has a lot of instructions this will decrease the overall performance.

**Big O notation** determines with the given input how the performance will be affected.

There are a lot of optimization done in CPU to make it faster and perform as much as it can. While writing any program we need to consider how reducing the number of instruction we provide to CPU will increase the performance of computer program.

---

Also Posted on Milap Neupane Blog: [How Does a CPU work](https://milapneupane.com.np/2019/07/06/how-does-a-cpu-work/)
