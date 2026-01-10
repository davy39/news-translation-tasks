---
title: Macho programmers, drum memory and a forensic analysis of 1960s machine code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T11:40:08.000Z'
originalURL: https://freecodecamp.org/news/macho-programmers-drum-memory-and-a-forensic-analysis-of-1960s-machine-code-6c5da6a40244
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ch1IHMJg5qHV050mUiLjDw.jpeg
tags:
- name: history
  slug: history
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By David Nugent

  Real programmers don’t use PASCAL

  Programmers today build distributed applications and artificial neural networks.
  They use functional reactive programming, open source web frameworks, and serverless
  environments. Yet, impostor syndro...'
---

By David Nugent

### Real programmers don’t use PASCAL

Programmers today build distributed applications and artificial neural networks. They use functional reactive programming, open source web frameworks, and serverless environments. Yet, impostor syndrome is real, and programmers still criticize each other for not being “real programmers.”

I worked as a docent for the Computer History Museum for years. The trope of a “real programmer” has been around since the beginning of software. And I can prove it with a story.

The story starts with a 1983 letter, [Real Programmers Don’t Use PASCAL](http://web.mit.edu/humor/Computers/real.programmers), written by Ed Post. The letter was published in Datamation, and discussed the “macho” side of programming. It needled those who disparage higher-level language users as **not** “real programmers.”

[The Story of Mel](http://www.catb.org/jargon/html/story-of-mel.html) is an online response to that letter. It was posted to Usenet on May 21, 1983 by [Ed Nather](https://en.wikipedia.org/wiki/Ed_Nather).

Mel and Ed were colleagues at a typewriter company that had branched out into building computers. Their breakout success was the [LGP-30](http://www.computerhistory.org/revolution/early-computer-companies/5/116): a [drum memory computer](https://en.wikipedia.org/wiki/Drum_memory) with a Flexowriter keyboard and paper tape reader. (The header image in this article is the dashboard of an LGP-30.) Mel was assigned to rewrite a popular program for the successor computer, the RPC-4000.

> Port? What does that mean?

After Mel left the company, Ed was tasked to rewrite part of this program. In the story, he discovers an infinite loop in the code, which somehow doesn’t prevent the program from functioning:

> Perhaps my greatest shock came when I found an innocent loop that had no test in it.  
> No test. None.  
> Common sense said it had to be a closed loop, where the program would circle, forever, endlessly.  
> Program control passed right through it, however, and safely out the other side.

Ed discovered that the closed loop was causing an overflow, that rewrote the instruction code. The outcome of the overflow was a **jump** instruction, moving control of the program to a different memory location.

It’s a great story. But does it check out?

### Forensic code analysis: Does the story check out?

Our first step is to look for technical details of the machine the program was written for. While the story makes extensive mention of the LGP-30, the program was actually running on an RPC-4000. (Remember, it needed to be re-written for this new machine.)

Both machines used drum memory for program storage. (Fun fact: the rough equivalent of your modern hard drive was drum memory, paper tape, punch cards or magnetic tape!) A single line of electromagnetic heads would read/write data as the drum spun at a constant velocity underneath them. Here is a visual reference:

![Image](https://cdn-media-1.freecodecamp.org/images/zJIzg5uyEQoFMEUDYz9gmS1SWMgNoRgksyeg)
_Memory drum diagram. Source: [RPC-4000 Manual](https://archive.org/details/bitsavers_royalPrecirogrammingManual_8537458" rel="noopener" target="_blank" title=")_

Data was stored and retrieved from the various sectors and tracks of the drum. To find out more about the format of the data, we can consult [the RPC-4000 programming manual](https://archive.org/details/bitsavers_royalPrecirogrammingManual_8537458), which archive.org has scanned and preserved online.

On page 20 of the manual, we find the following data word diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/7vhFSaJoslnlHki9MxXaOymDWxKfin32mF7X)
_RPC-4000 Word Format Diagrams_

The command word breaks down into:

* 5 bits for the command
* 13 bits for the track/sector location of the operand
* 13 bits for the track/sector of the next command’s address

Bit 31 is the **index tag** which, when set, activated the index register:

> [The index register] allowed the programmer to write a program loop that used an indexed instruction inside; each time through, the number in the index register was added to the address of that instruction, so it would refer to the next datum in a series.

The story mentions that the “index bit” is _“_the bit that lay between the address and the operation code in the instruction word_.”_ Yet, the diagram above shows that the index tag bit is actually at bit 31, past the command and addresses. Personally, I chalk this up to a mis-remembering by the author in the years between when he reviewed the code and when the story was recorded.

Luckily, this doesn’t affect the overflow aspect of the story. Since the instruction word was being pulled into memory and incremented, the index bit would still need to be set **on** in order for the increment to overflow the **Next Address**.

To re-create the instruction words in the loop, we need to know more about how the program operated. Here is a quote from the critical part of the story:

> He had located the data he was working on near the top of memory —   
> the largest locations the instructions could address —   
> so, after the last datum was handled, incrementing the instruction address would make it overflow.  
> The carry would add one to the operation code, changing it to the next one in the instruction set: a jump instruction.  
> Sure enough, the next program instruction was in address location zero, and the program went happily on its way.

### Hypothetical implementation: “Show me the bits!”

Here is a potential instruction that may be the **jump instruction** referenced in the story:

![Image](https://cdn-media-1.freecodecamp.org/images/YTmPExJNbmY8-Kx2r3UTaJSJ311QxjRn2Fc4)

We can see the command bits are **10111**. If **Branch Control** is off, “the next instruction is that specified in the Next-address field.” So one hypothetical situation would be that, after the overflow, the register (using pipes to denote separations between bitfields) read:

**10111 | 0000000| 0000000 | 0**

Extrapolating back, prior to the increment and overflow, the register would have read:

**10110 | 1111111 | 1111111 | 1**

One interesting side effect of working through this implementation is that the instruction used doesn’t really matter. Each instruction in the RPC-4000 includes the address of the next instruction. An overflow in the index bit into the next address field will result in a jump to that address irrespective of the command bits.

### Epilogue

![Image](https://cdn-media-1.freecodecamp.org/images/MiGjYka4199vjdbxDAskYWf9anRYPPUg72Ev)
_Group photo from the August 1956 Librazette_

Mel Kaye (pictured standing, rightmost) continued working and eventually retired. A fan named Anthony Cuozzo posted in 2014 that he tried to get into contact with Mel:

> I did eventually manage to get in contact with Mel, but I scared him away, unfortunately. That’s a story for another day… :-/ ([source](https://news.ycombinator.com/item?id=7869771))

Out of respect for Mel’s privacy, I won’t post any personal information, and stick to the program and the story. If anybody knows how Mel feels about his internet fame, I’d love to hear from you.

> I haven’t kept in touch with Mel, so I don’t know if he ever gave in to the flood of change that has washed over programming techniques since those long-gone days. I like to think he didn’t. — Ed Nather

_Further sources:_

* [_Wikipedia’s page on the Story of Mel_](https://en.wikipedia.org/wiki/The_Story_of_Mel)
* [_Mel’s manual for the RPC-4000 blackjack game_](http://bitsavers.trailing-edge.com/pdf/royalPrecision/RPC-4000/programWriteups/W1-01.0_Blackjack_Game.pdf)
* [_The Truth Never Gets in the way of a Good Story_](https://books.google.com/books?id=PhkINW48_J0C) _by Jan Howard Brunvand_

[Dave](https://twitter.com/drnugent) works developer relations at IBM. For some reason, IBM does not have an SDK for the RPC-4000.

