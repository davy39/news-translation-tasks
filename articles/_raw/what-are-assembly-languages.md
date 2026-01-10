---
title: What are Assembly Languages?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T00:51:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-assembly-languages
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e31740569d1a4ca3bd0.jpg
tags:
- name: programming languages
  slug: programming-languages
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Assembly Language is the interface between higher level languages (C++,
  Java, etc) and machine code (binary). For a compiled language, the compiler transforms
  higher level code into assembly language code.

  Every family of CPUs define their own Instru...'
---

Assembly Language is the interface between higher level languages (C++, Java, etc) and machine code (binary). For a compiled language, the compiler transforms higher level code into assembly language code.

Every family of CPUs define their own Instruction Set Architecture (ISA), a set of basic instructions that the CPU can execute without needing further translation or transformation. The compiler decomposes composite higher level composite instructions into operations available in the ISA. 

Some of the more common ISAS in use today include MIPS, ARM, Intel x86, RISC-V.

Assemblers decompose Assembly instructions into their respective binary representations and replace the generic addresses of assembly code with explicit register and memory addresses of your computer.

Code where execution time and control is crucial can be written directly in assembler. This, however, comes at the cost of prolonging development time, and making development harder. It should also be noted that there has been a large amount of research going into making compilers optimize the code that is generated automatically.

Assembly language is primarily used in the following situations:

* There is a need to use CPU instructions not available in higher-level languages.
* There is no high-level language to program a certain types of processors.
* Implementing a compiler for a higher level language on a new ISA.

![Image of Levels of Code](https://raw.githubusercontent.com/colbybanbury/assemblyPicture/master/Screenshot%20from%202017-10-14%2014-03-06.png)

#### 

