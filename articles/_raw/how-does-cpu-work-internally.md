---
title: How Does a CPU Work Internally? From Transistors to Instruction Set Architecture
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-07-10T19:14:05.000Z'
originalURL: https://freecodecamp.org/news/how-does-cpu-work-internally
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/1.jpg
tags:
- name: Computers
  slug: computers
- name: cpu
  slug: cpu
- name: hardware
  slug: hardware
seo_title: null
seo_desc: 'The CPU (Central Process Unit) is the brain of a computer, and the main
  connection between software and hardware. It makes it possible to operate software
  on hardware.

  However, how does it work in deep detail? And how can it connect programs to certa...'
---

The CPU (Central Process Unit) is the brain of a computer, and the main connection between software and hardware. It makes it possible to operate software on hardware.

However, how does it work in deep detail? And how can it connect programs to certain computer hardware?

This article aims to make you understand this connection by deeply explaining how a CPU works. This topic is often familiar only to those with a background in computer hardware design from college.

Often, many computer science graduates never have a class in advanced digital logic. So even very experienced programmers may lack an understanding of how a CPU actually processes information.

Although we won't be designing [logic gates from transistors](https://www.homemade-circuits.com/how-to-make-logic-gates-using-transistors/) or [CPU components from logic gates](https://www.techspot.com/article/1830-how-cpus-are-designed-and-built-part-2/), we will cover the key concepts needed to understand how a CPU processes data created by a program written in a programming language.

We will see:

* [Analogy: Introduction to What Makes CPUs Work](#heading-analogy-introduction-to-what-makes-cpus-work)
* [The Memory Hubs: Understanding RAM and ROM](#heading-the-memory-hubs-understanding-ram-and-rom)
* [The Roadways of Data: Navigating the CPU Data Path](#heading-the-roadways-of-data-navigating-the-cpu-data-path)
* [Traffic Controllers: The Role of State Machines in CPUs](#heading-traffic-controllers-the-role-of-state-machines-in-cpus)
* [Daily Routines: The Fetch-Execute Cycle Explained](#heading-daily-routines-the-fetch-execute-cycle-explained)
* [The Rulebook: Decoding the Instruction Set Architecture (ISA)](#heading-the-rulebook-decoding-the-instruction-set-architecture-isa)
* [From programming languages to machine code](#heading-from-programming-languages-to-machine-code)
* [City Challenges: Addressing CPU Problems](#heading-city-challenges-addressing-cpu-problems)
* [Conclusion: Better control units and data parts](#heading-conclusion-better-control-units-and-data-parts)

I will use the Intel 8008 as a reference. 

<h2 id="analogy">Analogy: Introduction to What Makes CPUs Work</h2>

To understand deeply how a computer works, let's imagine a city as our real-life scenario. We'll compare computer elements to parts of this city.

This way, you get a clearer view of different CPU parts and why they are important. Afterwards, we will look in depth to each of the components

### The Memory Hubs: Understanding RAM and ROM

RAM (Random access memory) is like a city public library: it stores books and information for people to borrow and return as needed.

In a computer, the RAM loads data and instructions from the computer memory needed by the CPU to process data.

ROM (read Only Memory) is like a historical archive in the city: It only stores records that will never change and never be borrowed from the public.

### The Roadways of Data: Navigating the CPU Data Path

The CPU data path is the network of roads in the city. The buses and registers of the CPU data path act like the city's road network.

Just as roads help cars and people move, the CPU data path guarantee the data travels in a efficient manner in the CPU

### Traffic Controllers: The Role of State Machines in CPUs

States machines act as the traffic control systems.

The traffic control system manages the flow of vehicles, and the states machines manage the flow of data according to the instructions provided to the CPU.

### Daily Routines: The Fetch-Execute Cycle Explained

The fetch-execute cycle is the daily commute for city residents.

Every day, people decide where they are going, travel there, perform their tasks and return home. This process is always repeated.

In the same way, the CPU fetches instructions, decodes them, and executes them in a repetitive cycle.

### The Rulebook: Decoding the Instruction Set Architecture (ISA)

The instruction set architecture is like the city transportation law.

The city transportation law shows what is legal to do in the city in relation to the transportation of people.

The instruction set architecture is the set of rules and instructions that the CPU can execute.

<h2 id="memory">The Memory Hubs: Understanding RAM and ROM</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3.jpg)
_Photo by Valentine Tanasovich: https://www.pexels.com/photo/black-and-gray-computer-motherboard-2588757/_

[RAM stands for Random Access Memory and can be used to read and write data.](https://www.freecodecamp.org/news/how-to-access-and-read-ram-contents/)

The CPU gets data from the computer memory to the RAM first to avoid long waiting times.

Then, it uses the data from the RAM to complete the instructions.

They are used in computers and in many electronic devices due to the memory being volatile. It means that the data is only there while the computer is turned on, making it ideal for temporal storage while the device works.

ROM stands for Read Only Memory. In there, there only exist data added during computer manufacturing.

They are widely used in [firmware](https://www.freecodecamp.org/news/what-is-firmware/) for devices, BIOS and small embedded systems.

This is because ROM is non-volatile memory. This means that it remains in memory when the device is powered off, making it very important for permanent data storage.

<h2 id="roadways">The Roadways of Data: Navigating the CPU Data Path</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4.png)
_Photo by Rogeer Marques: https://www.pexels.com/photo/close-up-shot-of-a-chip-processor-11272008/_

The CPU data path is a complex digital circuit with many components that work with one another, such as:

* **Arithmetic Logic Unit (ALU):** Performs arithmetic and logical operations inside the CPU data part.
* **Registers:** Small, fast storage locations for temporary data retrieved from the RAM.
* **Buses:** Data, control and address buses are wires used inside the CPU data path to transfer information.

While CPUs have changed a lot since the Intel 8008, these are some of the components that still serve as the foundation for all CPUs.

Thanks to them, it is possible to let data flow, but not control the actual flow. This is the job of the control unit in the CPU, created in the Intel 8008 as state machines.

<h2 id="traffic">Traffic Controllers: The Role of State Machines in CPUs</h2>

[A state machine is a system that transitions between different states in order to perform tasks.](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/)

They are composed of a number of states and transitions. They were used in the Intel 8008 to create the control unit due to its structure and effective way to manage the sequence of operations needed to process instructions

Each of the states can activate one or many CPU components to process a certain assembly instruction.

This way, certain CPU data path parts are activated for an instruction to be completed.

Additionally, thanks to these state machines, the CPU is complete and can perform all instructions a user wants in a continuous loop called the fetch-execute cycle.

<h2 id="fetch">Daily Routines: The Fetch-Execute Cycle Explained</h2>

The state machine in the CPU controls how the CPU data path works together to perform a given instruction.

Nowadays, every computer receives millions of instructions per second. This way, the state machines act as a loop to get the instructions and execute them.

This process is known as the fetch-execute cycle, where the CPU retrieves and executes instructions:

* **Fetch:** The CPU fetches the instruction from memory.
* **Decode:** The fetched instruction is decoded to determine the required action.
* **Execute:** The decoded instruction is executed using the appropriate CPU components.
* **Write-back:** The result of the execution is written back to memory or a register.

In the fetch stage, the control unit tells the RAM to give the next instruction to the CPU.

In the decode stage, the CPU interprets the instruction, and in the execution stage, it performs the operation. Afterwards, the write-back stage ensures the result is stored correctly.

This cycle continues while the PC is on. This way, in modern processors, processing billions of instructions per second.

### But What About Data from the Keyboard or Mouse?

This data does not come from RAM but is handled through a mechanism called interrupts. While the CPU runs instructions, it can detect when data comes from peripherals.

If this happens, the CPU stops its current task and prioritizes the instructions from the peripherals. Afterwards, the CPU resumes its previous tasks.

There are many ways to manage interrupts, with some of the most popular being:

1. **Polled Interrupts**: The CPU periodically checks if an interrupt has occurred.
2. **Vectored Interrupts**: The interrupting device directs the CPU to the appropriate interrupt service routine.
3. **Prioritized Interrupts**: Interrupts are assigned different priority levels, ensuring critical tasks are handled first.

This way, with these mechanisms, the CPU maintains its performance while interacting the peripherals.

<h2 id="instruction">The Rulebook: Decoding the Instruction Set Architecture (ISA)</h2>

With the control unit, the complete CPU and RAM, it is possible to perform many instructions.

But what instructions can be performed on a given CPU? And how many? This is what the Instruction Set Architecture (ISA) solves.

The ISA defines a set of instructions that a certain CPU can execute. It is what allows programmers to understand what a processor can and cannot do without having to understand all the digital logic hardware inside it.

This way, it acts as an interface between software and hardware.

**Key Aspects of ISA:**

* **Instruction Types:** Includes arithmetic, logical, control, and data transfer instructions.
* **Addressing Modes:** Methods for specifying operands of instructions.
* **Registers:** The set of registers available for use by instructions.

**Common ISAs:**

* **x86:** Widely used in desktop and server processors.
* **ARM:** Dominant in mobile and embedded devices due to its power efficiency.
* **RISC-V:** An open standard ISA designed for a wide range of applications.

Each CPU often has its own version of the instruction-set architecture. And the instruction set architecture is very often defined with the assembly programming languages.

This is why there are so [many versions](https://www.freecodecamp.org/news/what-are-assembly-languages/) of the assembly programming language.

Since each CPU has its own hardware specifications, each will have similar components to other CPUs and, thus, similar assembly programming languages associated.

The choice of ISA impacts the CPU's design, performance, and compatibility with software.

For instance, the complexity of x86 allows for powerful desktop applications, while ARM's simplicity favors energy-efficient mobile devices.

<h2 id="programming">From Programming Languages to Machine Code</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-1.jpg)
_Photo by luis gomes: https://www.pexels.com/photo/close-up-photo-of-programming-of-codes-546819/_

While each processor has its own assembly language, managing code in assembly and writing code in assembly to make big programs can be complex.

It is very complicated, and may lead to wasting time on correcting things and details instead of, in a faster and easier way, managing the development of a program and actually developing it.

To solve this problem, many programming languages were created from assembly. We write the code in the programming languages, and it is then converted to assembly.

This way, instead of spending time on details, it is possible to focus on more important things like system development and algorithm design.

This is the process by which most programming languages convert their code into assembly:

1. Convert the code to assembly code through either a compiler or interpreter.
2. The assembly code is then converted to raw machine code and executed by the CPU.
3. A specific loop in the CPU's state machine is completed.
4. Afterward, the CPU fetches and executes the next instruction.

Let's see two examples of programming languages doing this!

### C Programming Language

The C programming language was created from assembly in the early 1970s. It was created to provide a higher-level language for efficient system-level programming that also allows hardware manipulation.

With a compiler, the C code is converted to assembly and then processed by the complete CPU.

Thanks to this conversion, by writing programs in the C programming language, we can address many problems in a more efficient manner, such as:

* Memory management errors
* Buffer overflows
* Manual optimization issues

Nowadays, even for simpler tasks, the assembly code converted from C compiler is far more efficient and reliable than a human writing the assembly code.

If you want to learn more about the C compiler you can check out:

%[https://www.freecodecamp.org/news/what-is-a-compiler-in-c/]

### Python Programming Language

The Python programming language was created from C in the late 1980s.

Its goal was to provide a user-friendly, high-level programming language that emphasizes readability and simplicity, allowing for rapid application development.

In Python, an interpreter converts the Python code to bytecode line by line.

And this bytecode is converted to machine code in the CPU and processed in the fetch-execute cycle.

This way, it is possible for people to program in an easier way and focus on bigger programs, such as:

* Artificial intelligence models
* Web apps
* Data analysis
* Scientific computing

However, the challenge with the CPUs in all programming languages is that it processes data sequentially.

<h2 id="problems">City Challenges: Addressing CPU Problems</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4-1.jpg)
_Photo by Peng LIU: https://www.pexels.com/photo/timelapse-photography-of-vehicle-on-concrete-road-near-in-high-rise-building-during-nighttime-169677/_

The traditional one core CPU processes data sequentially, instruction after instruction. This becomes a limitation if we have many instructions to process.

This is what GPUs (Graphics processing units) came to fix.  Thanks to GPUs, we can process instructions in parallel, thereby reducing computing time significantly.

With these parallel processing capabilities, it is possible to achieve a much faster computation and improved efficiency in a wide range of applications.

<h2 id="conclusion">Conclusion: Better Control Units and Data Parts</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/5.jpg)
_Photo by Miguel Á. Padriñán: https://www.pexels.com/photo/green-circuit-board-343457/_

In addition to modern CPUs being multicore, advancements in control units and data paths play a critical role in improving processor performance. 

Control units are often designed using microprogramming or hardwired control units. 

Microprogramming offers greater flexibility and easier updates to the control logic, while hardwired control units provide faster performance by directly implementing control signals.

Another significant advancement is the exploration of new materials for transistors in logic gates. 

Instead of relying solely on silicon, researchers are investigating alternative materials to create faster and more efficient processors.

As technology continues to advance, understanding these fundamental concepts will remain essential for both enthusiasts and professionals in the field.

Keeping up with these developments ensures the continued innovation and improvement of CPU design and functionality.

