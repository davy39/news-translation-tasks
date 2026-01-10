---
title: 'Problem-solving with Honest Abe: let’s sum all prime numbers up to n'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T12:08:59.000Z'
originalURL: https://freecodecamp.org/news/problem-solving-with-honest-abe-lets-sum-all-prime-numbers-up-to-n-4c140273b8dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MZTE3Hr9MY3Ia_YUa9Sddg.jpeg
tags:
- name: creativity
  slug: creativity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Daniel Weiner

  Follow along as Honest Abe solves an intermediate algorithm challenge using the
  basic software development principles


  _Back in the day, we called it math [link](http://www.publicdomainpictures.net/pictures/80000/nahled/abraham-linco...'
---

By Daniel Weiner

#### Follow along as Honest Abe solves an intermediate algorithm challenge using the basic software development principles

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Back in the day, we called it math [link](http://www.publicdomainpictures.net/pictures/80000/nahled/abraham-lincoln-clipart.jpg" rel="noopener" target="_blank" title=")_

Say the challenge is this:

Sum all the prime numbers up to and including the provided number.

A prime number is defined as **a number greater than one and having only two divisors, one and itself.** For example, 2 is a prime number because it’s only divisible by one and two.

The provided number may not be a prime.

How would Honest Abe solve this problem?

### Honest Abe thinks big picture

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Take time to understand the problem[ link](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/SDLC_-_Software_Development_Life_Cycle.jpg/764px-SDLC_-_Software_Development_Life_Cycle.jpg" rel="noopener" target="_blank" title=")_

> “Give me six hours to chop down a tree and I will spend the first four sharpening the axe.” — Honest Abe

Before diving into code, Honest Abe likes to **formulate requirements** and **determine specifications**. He learns as much as possible about the problem, and figures out exactly the problem that needs to be solved. Until he fully understands the problem, he cannot begin to solve it.

He also needs to determine exactly what the program will accomplish. He focuses on **what** want the program will accomplish, rather than **how** it will work. For simple programs, this involves describing the inputs and outputs and how they relate to one another.

For this problem, the input will be some number (n), an integer. The output will be the sum of all the prime numbers from 2 through n (there are no prime numbers less than 2). The problem explains prime numbers, and Abe feels comfortable with that definition.

### Honest Abe starts with paper and pencil

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_An algorithm is a recipe? Maybe[ link](https://c2.staticflickr.com/4/3059/3073489187_bd76ae6747_z.jpg?zz=1" rel="noopener" target="_blank" title=")_

Abe doesn’t just jump right into coding. The next step is to create the overall structure of the program. This is where he determines **how** the program accomplishes its task.

The main job here is to **design the algorithm(s)** that will meet the specifications. The algorithm will often be written in **pseudocode**, or a precise English description of what the program does. This helps Abe communicate algorithms without the extra mental overhead of getting the details right in any particular programming language.

Here’s an algorithm to sum all primes up to n:

* Input n as an integer
* Find primes up to n
* Find sum of all primes found

Abe knows that he can revisit this pseudocode as he implements the design.

### Honest Abe loves Python Tutor

![Image](https://cdn-media-1.freecodecamp.org/images/sh59wqAG42mQr3Pn7lW8qrRgHbRUYF65QuWu)
_An artist is only as good as his or her tools [link](https://c1.staticflickr.com/4/3132/2504310138_f7d3e1aec3_b.jpg" rel="noopener" target="_blank" title=")_

Abe knows he has many options where he could code, including an editor such as Sublime, or an IDE such as Visual Studio Code, or even directly in a provided coding panel (like the one provided by freeCodeCamp).

Abe really prefers pythontutor.com.

Here’s an example of how Python tutor works:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Coding in Python3 using Python tutor_

Python tutor is a very intuitive interface to enter code into an editor. It allows Abe to visualize the execution of a program, without needing to learn about a debugger or an IDE. He can even set break points simply by clicking on lines of code (the break point here is marked in red). Despite the name, Python tutor is also compatible with Java, JavaScript, Ruby, and other programming languages.

### Honest Abe uses Incremental Development

![Image](https://cdn-media-1.freecodecamp.org/images/HQwGLbkuoBxjAJnid24NeBJNW09lqyrrpTzp)
_This makes things more clear [link](http://3vwizk2qtr8l3diwrm3r2ba0-wpengine.netdna-ssl.com/wp-content/uploads/2011/10/convergent-vs-divergent2.jpg" rel="noopener" target="_blank" title=")_

Unlike many lectures, tutorials, and textbooks, code that Honest Abe writes himself doesn’t come completely assembled as a working program. Although sometimes he thinks it would be nice if it did.

Therefore, Honest Abe practices incremental development.

Rather than writing a complete function, program, or whatever he’s working on, Honest Abe will write small pieces of code first, make sure those work, then link those together into a bigger program. He is, therefore, developing his program in **increments**_._

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Incremental development to get an integer from the user_

In this example, Honest Abe starts with a small version of the code, getting input from the user. He inserts a print statement to make sure that this is working. The final version of the code is commented out below to show how he might go from one increment into a larger block of code.

### Honest Abe practices Defensive Programming

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Now that’s some self-defense [link](https://pixel.nymag.com/imgs/fashion/daily/2016/11/18/18-womens-self-defense.w710.h473.jpg" rel="noopener" target="_blank" title=")_

Honest Abe knows that users can’t be trusted to follow the instructions provided by his program. He has to put protections in place in case users input bad values. In this case, bad values would be anything other than a positive integer.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Catching bad user input — floats, characters, and negative ints_

The try / except block seen above, encapsulated in the readInt function, catches any user input that is not a positive integer, and finally returns the user input once an integer is entered properly.

### Honest Abe starts with a brute force solution

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_“Make it correct, make it clear, make it concise, make it fast. In that order.” Wes Dyer_

Honest Abe’s first priority is to get the program to produce a correct result. He relies on a brute force, exhaustive enumeration approach, iterating over all of the numbers from five through the user input, checking to see if each is prime.

He knows that two and three are primes, so if either of those are the user input, he adds those to sum.

He also optimizes for the inner loop by only searching from two through the square root of i.

This gives the correct result, but Honest Abe knows he can do better. This would be terribly slow on large inputs.

### Honest Abe studies The Classics

![Image](https://cdn-media-1.freecodecamp.org/images/Nj8BvK6MWqypP2T1Wq16-W8jOmNAusjLrt5s)
_Sieve of Eratosthenes [link](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#/media/File:Sieve_of_Eratosthenes_animation.gif" rel="noopener" target="_blank" title=")_

Attributed to the ancient Greek mathematician, Eratosthenes, this is an efficient algorithm for finding prime numbers up to any given limit.

It iteratively marks multiples of each prime as not prime, starting with the first prime number, 2. For instance, 4, 6, 8 etc. are marked as not prime up to the limit. Then, returning to the beginning of the list, 3 is marked as prime. 6 has already been marked as not prime, so 9 is marked as not prime, followed by 12, 15, etc. until the sequence is finished.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Sieve of Eratosthenes in pythontutor_

Honest Abe starts by initializing a list with the values True of length num. He sets the first two values of the list to False because neither 0 nor 1 are prime. He then creates a variable sum with an initial value of 0, which will increase with each prime number found.

Using the enumerate function in Python, Honest Abe first checks if the value in the list a is set to True, meaning that this is a prime number. If it is, he sum increases by that amount.

He then iterates, starting from i*i (a small optimization), through num, incrementing by i, changing the value at each list index to False.

For instance, the 0 and 1 are both set to False, so those values do not enter the inner for loop.

2 is set to True, so 2 gets added to sum. Then, starting at 4, list indices get set to False, including 6, 8, 10, etc, until the loop is finished.

Then i increments to 3, which is set to True, and the process above repeats itself.

Honest Abe knows there are [more efficient](https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n) implementations, but the tradeoff in efficiency will be explainability, so he will leave it to the reader to further explore these algorithms.

### Honest Abe tests his program

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Move away from pythontutor for testing_

Normally, Abe would do unit testing before integration testing.

Testing, however, is a very large subject best left for other articles.

Abe, instead, just wants to make sure that his program works as intended.

He uses pytest and tests his program on a series of positive integers.

He feels confident that his program provides the correct answers.

### Honest Abe’s Favorite Resources

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Life long learning [link](http://maxpixel.freegreatpicture.com/static/photo/1x/Education-Learn-School-Classroom-Learning-1959551.jpg" rel="noopener" target="_blank" title=")_

[Teach yourself programming in ten years](http://norvig.com/21-days.html) — Peter Norvig

[Stanford Programming Methodology](https://www.youtube.com/playlist?list=PL84A56BC7F4A1F852)

[MIT Python](https://www.youtube.com/playlist?list=PL57FCE46F714A03BC)

[Harvard CS50](https://www.youtube.com/channel/UCcabW7890RKJzL968QWEykA)

Thanks for reading! Good luck on your journey!

Enjoy this [comic](https://zenpencils.com/comic/asimov/) as well about lifelong learning.

