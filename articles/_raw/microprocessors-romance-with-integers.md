---
title: Microprocessor's Romance With Negative Integers – The How and Why of CPU Arithmetic
  Design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-28T18:30:45.000Z'
originalURL: https://freecodecamp.org/news/microprocessors-romance-with-integers
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/cover2.jpg
tags:
- name: binary
  slug: binary
- name: cpu
  slug: cpu
- name: Mathematics
  slug: mathematics
- name: systems
  slug: systems
seo_title: null
seo_desc: "By Vivek Agrawal\nOne of the first things we learn about computers is that\
  \ they only understand 0s and 1s, or bits. \nWe humans, on the other hand, communicate\
  \ numbers via the decimal system. This system uses digits from 0 to 9 along with\
  \ plus and minu..."
---

By Vivek Agrawal

One of the first things we learn about computers is that they only understand **0s and 1s**, or **bits**. 

We humans, on the other hand, communicate numbers via the decimal system. This system uses digits from 0 to 9 along with plus and minus signs (+ and -) to denote positive or negative numbers. 

Since computers can use only two digits – 0 and 1 – engineers and mathematicians back in the day designed clever techniques for representing negative numbers and for doing arithmetic with them. Let's explore the beauty of those techniques.

## First, some background on how computers work

Software, images, text, videos, numbers and everything in between are 0s and 1s at the lowest level in our computer.

For images, text, videos and numbers, we have encoding schemes that decide how these stuff will get to 0s and 1s. For example, ASCII and Unicode for text.

The software programs we code get to 0s and 1s via compilers and assemblers. Those set of 0s and 1s known as machine code (or machine instruction) are first stored in our computer's main memory (RAM) before the processor can execute them.

![A diagram showing fetch decode execute cycle](https://www.freecodecamp.org/news/content/images/2021/01/fetch-decode-exec.png)
_The fetch decode execute cycle architected by Sir [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann). Every digital computer follows this cycle to run machine code._

The processor starts the execution cycle by **fetching** the instructions from the main memory, then the control unit of the processor **decodes** those instructions into two parts – operation code (opcode) and operands. 

The opcode decides the further action that needs to be performed like ADD (addition), JMP (jump), INC (increment) and so on. The operands are the values (or memory locations) on which that operation will be performed. 

The decoded instructions are sent to the Arithmetic and Logic Unit (ALU) for **execution**. In the ALU, the instruction is executed based on the opcode on the operands and the result is stored back in the memory. 

For example, the assembly code `ADD eax, 42` is first turned into machine code (0s and 1s) by the assembler. Then it is stored into the main memory before the fetch-decode-execute cycle can begin. 

When the fetching of the machine code for `ADD eax, 42` from the memory finishes, the instruction is decoded. The decoded output says that the opcode is `ADD` and the operands are `eax` and `42`.  

`eax` is a register – a memory location inbuilt into the processor that can be accessed instantaneously by the processor. The `eax` register is called an accumulator in most processors. 

The `ADD eax, 42` assembly code is designed to add 42 to the current value of the `eax` register (accumulator) and stores that sum in `eax`. It is `eax = eax + 42`. 

Suppose that currently `eax` is 20. This means that the value of `eax` after executing `ADD eax, 42` will be 20 + 42 = 62.

![Two men operating EDVAC computer](https://www.freecodecamp.org/news/content/images/2021/01/Edvac-1.jpg)
_EDVAC was one of the earliest electronic binary computer built for the U.S. Army's Ballistics Research Laboratory. ([Image source](https://en.wikipedia.org/wiki/EDVAC#/media/File:Edvac.jpg), Public Domain)._

The design of early computers such as EDVAC started with the desire to make tedious mathematical calculations easier and faster. 

The whole responsibility of making computers compute lay on the shoulders of adders – circuits that add two numbers. This is because sophisticated operations like subtraction, multiplication, and division utilize adders in their circuits.  

Ultimately computers are just a fast arithmetic machines with logic capabilities. Understanding the challenges and the beauty of binary arithmetic design (of positive and especially negative integers) is **one of the most fundamental concepts in a computer processor**. 

Let's first see how decimal numbers are represented in binary and how to add two binary values. Then we will start exploring the beauty.      

## How the binary system works

If I tell you to read out `872500`, you will likely say **872.5K**. Let's take a look at how our minds do this.

![The procedure we humans use to read decimal numbers](https://www.freecodecamp.org/news/content/images/2021/01/decimal_sys_img-2.png)

We assign the one's place to the first digit from the right, then the ten's place to the second from the right, the hundredths to the third, and so on, growing each time by power of 10. 

These powers of 10 in each place are the weights of the places. The weight of the hundredth place is one hundred. We multiply the digits in each place by their place's weight and sum them all up to get a complete number.

In the above diagram, you can see that the growth of each place's weight is in the powers of 10, starting from `10^0` and going through `10^5`. That's why decimals are called a base ten system.

![The procedure via which computers read binary codes](https://www.freecodecamp.org/news/content/images/2021/01/binary_sys_img-2.png)

In binary, each place's weight grows by a power of 2. This means that the place's weight starts from `2^0` and ends at `2^something`. That's the only difference.

`00110101` in decimal translates to 53. Computers interpret binary in the same way as we humans interpret decimals, that is multiplying each place's digit by its weight and summing them up.

### How to add 1s and 0s

Addition works in binary pretty much the same way as it's done in decimals. Let's see that through an example. We'll add two binary numbers: `1101` (13) and `1100` (12).

![Step one of addition of 1101 and 1100 that is one plus zero](https://www.freecodecamp.org/news/content/images/2021/01/1-1.png)

As we do in the decimal system, we start from the one's place (`2^0`). Adding 1 and 0 gives us 1. So we put a 1 there. Stay with me and you'll get the whole picture.

![Step two of addition of 1101 and 1100 that is zero plus zero](https://www.freecodecamp.org/news/content/images/2021/01/2-1.png)

0 plus 0 is 0. Moving on.

![Step three of addition of 1101 and 1100 that is one plus one](https://www.freecodecamp.org/news/content/images/2021/01/3-2.png)

1 plus 1 is 2. And 2 in binary is represented as `10`. We carry 1 to the next place and keep 0 as a result of the current place we are in. Isn't this the same as exceeding 9 in a place in decimal addition? 

![Step four of addition of 1101 and 1100 that is one plus one plus one of carry row](https://www.freecodecamp.org/news/content/images/2021/01/4-1.png)

We have two 1s there and one 1 that was carried forward from the previous place, so there are a total of three 1s. Their sum will be 3, and in binary 3 is `11` so we write `11`. The final result comes out to be `11001` or 25 in decimal form, which is indeed 13 + 12.

The above computation assumes that we have five bits available to store the result. If a 4-bit computer does this addition, then it will only have four bits available to store the result. 

That fifth bit will be called an **overflow** in 4-bit computers. In integer arithmetic, the overflow bit is ignored or discarded. So we would have got `1001` (9) as our result if we were using a 4-bit computer.

## The beauty of binary arithmetic design

Two important terms we need to understand before we move forward are **least significant bit** and **most significant bit**.

![The least significant and the most significant bit in a byte word](https://www.freecodecamp.org/news/content/images/2021/01/lsb_msb-1.png)

The bit on the **rightmost is the least significant bit** because it has the smallest place weight (`2^0`). And the bit on the **leftmost is the most significant bit** as it has the highest place weight (`2^7`).

If the world only had positive numbers, then this would have been the end of this article (because we have already learned how to represent decimals in binary and how to add them in binary). 

Thankfully, we have negative numbers, too. 

The beauty of the CPU's arithmetic design rests in negativeness. 

So how do computers represent negative numbers, and how does arithmetic on negative numbers work? Let's see an encoding approach to this problem.

Please note that in the below sections we will be working with a 4-bit computer to understand the concepts, meaning the fifth bit will be treated as an overflow. The same principles apply to all the CPU architectures like 16-bit, 32-bit or 64-bit to do arithmetic.

### The sign magnitude encoding approach

![The leftmost bit in a four bit binary is the sign bit and the remaining three represents magnitude](https://www.freecodecamp.org/news/content/images/2021/01/sign-bit01-1.png)

`1101` in decimal form would be -5 in this encoding scheme. The leftmost or the most significant bit is the sign bit. It tells the processor about the sign of the number – that is, whether the number is positive or negative. 

`0` in the sign bit represents a positive value and `1` represents a negative value. The remaining bits tells us the actual magnitude.

In `1101`, the sign bit is `1`, so the number is negative. `101` equals 5 in decimal. So `1101` will compute to -5 in decimal.

![All numbers that are possible with four bits using sign bit encoding scheme](https://www.freecodecamp.org/news/content/images/2021/01/4bit-1.png)
_All possible numbers that can be represented by four bits with sign bit encoding scheme_

In the above diagram you can see all the integers that can be represented by four bits using this encoding approach. All looks good up to this point. 

But if we look closely, we can see a very serious design issue in this encoding scheme. Let's face that issue.

Let's add a positive and a negative number. For example we'll add +4 and -1. Our answer should be `(+4) + (-1) = (+3)` that is `0011`.

![Adding +4 and -1 in binary resulting in -5 when using sign bit encoding scheme](https://www.freecodecamp.org/news/content/images/2021/01/signbitproblem.png)

See, the result is `1101` (-5). The actual answer should be `0011` (+3). If we were to implement this approach on a processor then we would need to add logic to deal with this issue, and engineers hate additional complexity in their logic. 

As we add more circuits, the power consumption increases and performance suffers. 

This might sound like a trivial issue for modern transistor-based computers. 

But think of early computers like EDVAC which was run on thousands of vacuum tubes consuming power in kilowatts operated by hundreds of people a day. And the government spent millions to build them. 

In those days putting additional circuits and vacuum tubes meant thousands of dollars and serious maintenance trouble.   

So engineers had to think of a smarter encoding design. 

Now, the time has come to reveal the beauty that will tackle this problem and make our system simpler, more performant, and less power hungry.

### A beautiful encoding system enters and the CPU shines ❤️

In this encoding scheme, like in the previous one, the leftmost bit acts as a sign bit – but with some art involved to represent negative numbers.

The positive numbers are represented in the exact same way as the previous encoding scheme: a leading `0` followed by remaining bits for the magnitude. For example, in this encoding scheme too, 6 will be represented as `0110`. 

To represent a negative number, a two step math process is run in its positive counterpart. Meaning to represent -6 we will do a two step math process on +6 to get to -6 in binary. 

Let's see how -6 will encode to binary:

![An illustration of bits getting inverted](https://www.freecodecamp.org/news/content/images/2021/01/invert-1.png)

In the previous sign magnitude approach, to calculate the negative of +6, we would have simply changed the sign bit from `0` to `1`. `0110` (+6) would become `1110` (-6).

In this new encoding scheme, we first invert the bits. Changing zeros to ones and ones to zeros. `0110` (+6) becomes `1001`. Inverting the bits is called "one's complement", so here we have calculated one's complement of `0110` resulting in `1001`. Then...

![Adding binary one to 1001, resulting in 1001](https://www.freecodecamp.org/news/content/images/2021/01/-6-1.png)

We add `0001` (+1) to the one's complement we got from step one (`1001`). The result **`1010` will be the binary representation of -6. This encoding scheme is called two's complement.** So keep in mind that calculating two's complement of a positive integer gives us its negative counterpart.  

![Steps of calculation of the two's complement of 0110](https://www.freecodecamp.org/news/content/images/2021/01/twocomplementshort-4.png)

Inverting bits gives us the one's complement. Adding one to the one's complement gives us the two's complement of the original bits we started with. Simple, right?

![All possible numbers that can be represented by four bits with two's complement encoding scheme](https://www.freecodecamp.org/news/content/images/2021/01/2complement.png)
_All possible numbers that can be represented by four bits with two's complement encoding scheme_

Now, let's see why this encoding scheme is so beautiful. We'll add `0100` (+4) and `1111` (-1).

![Addition of 0100 and 1111 when using two's complement encoding scheme](https://www.freecodecamp.org/news/content/images/2021/01/2complesolution.png)

See, we get the accurate result with the two's complement encoding scheme. Now we can add integers without worrying about their signs. 

We've learned how a negative integer can be represented in 0s and 1s via two's complement encoding. Now suppose we execute `ADD eax, -3` and the current value in the eax register is -1. So the value in eax after the execution of `ADD eax, -3` will be -4 (which is `1100` in two's complement encoding). 

When the operating system retrieves `1100` from eax to present the result to the user, how does the operating system decode `1100` to decimal? Or suppose if we as a programmer come across `1100`, how can we figure out what number `1100` represents? 

Of course we cannot keep on calculating two's complement of each positive integer to see when we hit `1100`. That will be too slow.   

Programmers and the OS use a beautiful property of two's complement to decode the binary into decimal. 

When we calculate two's complement of a positive number, we get its negative counterpart. Well, **the reverse is also true** – which means calculating two's complement of a negative number will give us its positive counterpart. We will see the why of this in a minute. 

First, let's understand how the OS or a programmer will decode `1100` to decimal.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/2complementexample-1.png)

On retrieving `1100` from the eax register, the OS sees `1` as sign bit that signals that the integer is negative. Two's complement of `1100` is calculated that gives the positive counterpart of `1100` which comes out as `0100` (+4). The OS then prepends a negative sign on the positive counterpart and returns the final answer as -4. Re-read this paragraph once again and you'll get a better understanding.

Then the CPU smiles and says goodbye to the beauty for today ;) 

The CPU has gone to its house to meet its mother. Now we have plenty of time to discuss the inner workings of the art of two's complement.

## Why and how does two's complement encoding work?

If I tell you to find the negative of a number, say +42, what's the simplest way to find the negative of +42? 

Arguably, the simplest way is to subtract the number from 0, right? `0 - (+42) = -42`. If we repeat this, we get back to the positive value, `0 - (-42) = +42`. This is all the math that two's complement is built upon.

![Subtracting 0101 from 10000 resulting in 1011](https://www.freecodecamp.org/news/content/images/2021/01/zerominusnum-1.png)

We are doing `10000` (0 in decimal since the leftmost 1 is an overflow) minus `0101` (+5). We get `1011` that is -5 in decimal in two's complement encoding. Ignore how subtraction is done. That's not important. Understanding the intuition behind two's complement is important.

`10000` can be written as `1111 + 0001` (try adding these two, you will get `10000`). So actually we are doing:

```
        10000       -   0101
=>  (1111 + 0001)   -   0101

```

Rearranging the above equation we can write it as:

```
    (1111 + 0001)  -  0101
=>  (1111 - 0101)  +  0001

Step 1: subtract 0101 from 1111

        1 1 1 1
       -0 1 0 1
       ---------
        1 0 1 0
        
       see, subtracting 0101 from 1111 is equivalent 
       to inverting the bits of 0101, as we got 1010 as a result. 

  
       
Step 2: add 0001 to the above result  

        1 0 1 0  ---> result of step 1
       +0 0 0 1
       ---------
        1 0 1 1      
       
       we get 1011 that is -5 in two's complement encoding.      

```

Did you see that the two's complement system fundamentally does 0 minus the number? Inverting the bits and adding one is a fast and clever way to subtract the number from 0. 

This is the reason we get the positive of a negative number and negative of a positive number when we calculate its two's complement – because we are actually subtracting the number from 0 (`0 - number`). 

Computers in the 1900s used to have just the addition arithmetic logic because the two's complement encoding scheme is so beautiful that subtraction can easily be performed. 

For example, to subtract 12 from 100, the CPU computes two's complement of +12 that produces -12 then we add -12 to 100 giving us the required output.  
  
Why don't we directly subtract from 0 to find the negative of a number or vice versa in binary? 

Because subtraction is a slow and complicated process (thanks to borrowing) so our computer will need an expensive subtraction circuit if we go that way. Imagine subtracting from 0 every time we want to represent a negative integer. It'll be a nightmare for us and for our computers as well!

The two's complement encoding is a more performant solution, leads to a simple circuit design, and saves a lot of money. This is because we don't need an expensive circuit for subtraction and there's no additional logic to deal with the arithmetic of + and - integers. Just plain addition and we get to do both – add and subtract. 

So let's appreciate our computer designers for this beautiful encoding scheme – **the two's complement ❤️.**  

## Final words

I promised myself that I would never charge for any learning material I produce. Whatever I do for education, whether it be a simple article or a course or an ebook, will always be 100% free and open. 

I post useful resources and share meaningful thoughts on [my Twitter account](https://twitter.com/vkwebdev). You can follow me there and send me a DM if you learned something new from this article. It'll make my day :)

Every developer, every author, and every human being learns from someone. I believe the people and resources we learn from should be cited and spread. This encourages those good ones to do more for all of us. So here are my good ones.

[Animesh of mycodeschool](https://www.youtube.com/watch?v=zxb8DvLUqcM) taught me many programming concepts better than anyone else including the concepts I wrote about in this article.

[André Jaenisch](https://jaenis.ch/), my mentor and friend, without his reviewing efforts and constant support I would not have written this article.

Happy learning!

