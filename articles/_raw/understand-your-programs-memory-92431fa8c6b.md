---
title: How to understand your program’s memory
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-20T18:15:08.000Z'
originalURL: https://freecodecamp.org/news/understand-your-programs-memory-92431fa8c6b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*VHc4F6eq1k7ZiOnT.jpg
tags:
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: software
  slug: software
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Tiago Antunes

  When coding in a language like C or C++ you can interact with your memory in a more
  low-level way. Sometimes this creates a lot of problems you didn’t get before: segfaults.
  These errors are rather annoying, and can cause you a lot o...'
---

By Tiago Antunes

When coding in a language like C or C++ you can interact with your memory in a more low-level way. Sometimes this creates a lot of problems you didn’t get before: **segfaults**. These errors are rather annoying, and can cause you a lot of trouble. They are often indicators that you’re using memory you shouldn’t use.

One of the most common problems is accessing memory that has already been freed. This is memory that you’ve either released with `free`, or memory that your program has automatically released, for example from the stack.

Understanding all this is really simple and it will definitely make you program better and in a smarter way.

### How is the memory divided?

![Image](https://cdn-media-1.freecodecamp.org/images/6xEDNU7MCJLyXyOTKwWtml4uq6-mJLcTC221)
_High stands for **high addresses**_

Memory is divided in multiple segments. Two of the most important ones, for this post, are the **stack** and **heap**. The stack is an ordered insertion place while the heap is all random — you allocate memory wherever you can.

Stack memory has a set of ways and operations for its work. It’s where some of your processor’s registers information gets saved. And it’s where relevant information about your program goes — which functions are called, what variables you created, and some more information. This memory is also managed by the program and **not** by the developer.

The heap is often used to allocate big amounts of memory that are supposed to exist as long as the developer wants. That said, **it’s the developer’s job to control the usage of the memory on the heap**. When building complex programs, you often need to allocate big chunks of memory, and that’s where you use the heap. We call this **Dynamic Memory**.

You’re placing things on the heap every time you use `malloc` to allocate memory for something. Any other call that goes like `int i;` is stack memory. Knowing this is really important so that you can easily find errors in your program and further improve your Segfault error search.

### Understanding the stack

Although you may not know about it, your program is constantly allocating stack memory for it to work. Every local variable and every function you call goes there. With this, you can do a lot of things — most of them are things that you did not want to happen — like buffer overflows and accessing incorrect memory.

So how does it really work?

The stack is a LIFO (Last-In-First-Out) data structure. You can view it as a box of perfectly fitted books — the last book you place is the first one you take out. By using this structure, the program can easily manage all its operations and scopes by using two simple operations: **push** and **pop**.

These two do exactly the opposite of each other. Push inserts the value to the top of the stack. Pop takes the top value from it.

![Image](https://cdn-media-1.freecodecamp.org/images/1Xc0oMmDVCRDzuluEcIFY5tJdBJ5POqDFLxx)
_Push and Pop operations._

To keep track of the current memory place, there is a special processor register called **Stack Pointer**. Every time you need to save something — like a variable or the return address from a function — it pushes and moves the stack pointer up. Every time you exit from a function, it pops everything from the stack pointer until the saved return address from the function. It’s simple!

To test if you understood, let’s use the following example (try and find the bug alone ☺️):

![Image](https://cdn-media-1.freecodecamp.org/images/7qQgG58GTkftIbYS7OjWQNZeJDEO002WSn8J)
_Everything looks ok — until you run it._

If you run it, the program will simply segfault. Why does this happen? Everything looks in place! Except about… the stack.

When we call the function `createArray`, the stack:

* saves the return address,
* creates `arr` in stack memory and returns it (an array is simply a pointer to a memory location with its information)
* but since we didn’t use `malloc` it gets saved in stack memory.

After we return the pointer, since we don’t have any control over stack operations, the program pops the info from the stack and uses it as it needs. When we try to fill in the array after we returned from the function, we corrupt the memory — making the program segfault.

### Understanding the heap

In opposition to the stack, the heap is what you use when you want something to exist for some time independently of functions and scopes. To use this memory, the C language **stdlib** is really good as it brings two awesome functions: `malloc` and `free`.

**Malloc** (memory allocation) requests the system for the amount of memory that was asked for, and returns a pointer to the starting address. **Free** tells the system that the memory we asked for is no longer needed and can be used for other tasks. Looks really simple — as long as you avoid mistakes.

The system can’t override what developers asked for. So it depends on us, humans, to manage it with the two functions above. This opens the door for one human error: Memory Leaks.

Memory Leak is memory that was requested by the user that was never freed — when the program ended or pointers to its locations were lost. This makes the program use much more memory than what it was supposed to. To avoid this, every time we don’t need an heap allocated element anymore, we free it.

![Image](https://cdn-media-1.freecodecamp.org/images/bQ9wKhnYnJ10TyPVzva87ePnOCJCbL92il57)
_Pointers: bad vs good._

In the picture above, the bad way never frees the memory we used. This ends up wasting 20 * 4 bytes (int size in 64-bit) = 80 bytes. This might not look that much, but imagine not doing this in a giant program. We can end up wasting gigabytes!

Managing your heap memory is essential to make your programs memory efficient. But you also need to be careful on how you use it. Just like in stack memory, **after the memory is freed, accessing it or using it might cause you a segfault.**

### Bonus: Structs and the heap

One of the common mistakes when using structs is to just free the struct. This is fine, **as long as** we didn’t allocate memory to pointers inside the struct. If memory is allocated to pointers inside the struct, we first need to free them. Then we can free the entire struct.

![Image](https://cdn-media-1.freecodecamp.org/images/UyQVaM0D6gOZitzmY7KCpqLgIlsOaLt5ORHh)
_Look at how I used free_

### How I solve my memory leak problems

Most of the time when I program in C I’m using structs. Therefore I always have two mandatory functions to use with my structs: the **constructor** and the **destructor**.

These two functions are the only ones where I use mallocs and frees on the struct. This makes it really simple and easy to solve my memory leaks.

(If you would like to know more about making code easier to read, [check my post on abstraction](https://medium.com/@tm.antunes/make-your-code-understandable-by-using-abstraction-4b522307130c)).

![Image](https://cdn-media-1.freecodecamp.org/images/LGoJhYkKmZZpPOOYOLSGZcuQHiTGpJS-GADL)
_A way to create, and a way to destroy!_

### A great memory management tool — Valgrind

It’s hard to manage your memory and make sure that you handled everything correctly. A great tool to validate if your program is behaving correctly is [Valgrind](https://en.wikipedia.org/wiki/Valgrind). This tool validates your program, telling you how much memory you allocated, how much was freed, if you tried to write in an incorrect memory area… Using it is a great way to validate if everything is ok, and one should use it to avoid security compromises.

![Image](https://cdn-media-1.freecodecamp.org/images/sN5lRHdCPsyLAicAokhZ4q4kDVgYrodPwh8l)
_An example of using valgrind, giving you information about what went wrong_

### Don’t forget to follow me!

Besides posting here on Medium, I’m also on [Twitter](https://twitter.com/tm_antunes).

If you have any questions or suggestions, don’t hesitate to contact me.

