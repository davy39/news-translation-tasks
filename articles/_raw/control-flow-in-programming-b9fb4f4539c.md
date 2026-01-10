---
title: 'How Python makes decisions: an introduction to Control Flow in programming'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T05:01:32.000Z'
originalURL: https://freecodecamp.org/news/control-flow-in-programming-b9fb4f4539c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4AwPR5QPsXwvCaIR3oczxg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ivan Leo

  What is control flow?

  I find it easy to think of control flow in 3 different categories


  Loops ( While, Do while, for )

  Decision-Making ( if-else)

  Exception Handling (Continue, Try-Except, Pass, Break)


  These 3 categories roughly sum up t...'
---

By Ivan Leo

What is control flow?

I find it easy to think of control flow in 3 different categories

1. Loops ( While, Do while, for )
2. Decision-Making ( if-else)
3. Exception Handling (Continue, Try-Except, Pass, Break)

These 3 categories roughly sum up the different options available to us when we talk about Control Flow in most programming languages.

So let’s jump right in.

### Loops

> _Loops are basically a simple set of instructions that gets repeated until a condition is met._

A good analogy to use for a loop is whisking cake batter:

Based on this [recipe](https://thecakeblog.com/2014/08/mixing-up-the-perfect-cake.html), if we use a modern day mixer, 3 minutes is the perfect amount of time to mix the batter. If you were to give instructions to someone using this recipe, it would probably look something like this.

1. Mix eggs, flour and secret recipe
2. Start a stopwatch and begin mixing batter
3. Mix the batter until the stopwatch displays 3 minutes

If we were to translate this into psuedo-code, it would probably look something like this

```
#Start Timer<....code....>time = 0
```

```
While(time != 3 minutes):    time = newvalue    mix batter
```

In this case, we are using **time** to determine if we continue to mix our batter. But this doesn’t really help us take into account specific situations when we use different ingredients.

In this case, we have a few options

1. We could monitor the consistency of the batter
2. OR we could experiment with a whole bunch of ingredients, record the best times for each and then refer to this record each time we mix the cakes.

Now stop for a moment and think, when would we use the first option and when would we use the second option?

< Intentional Blank Left Here . Do stop and think for a while :) >

The first option is more suited towards situations where we might encounter a lot of unpredictable combinations. It therefore makes sense to not only check time but also to add the safeguard of an additional parameter.

The second option is suited towards situations where we encounter repeated instances of multiple combinations. It’s commonly known as dynamic programming.

In Dynamic Programming, each value is calculated once and then stored in a lookup table for future access. This helps to reduce the run time of future operations by reducing the lookup time, since the value doesn’t have to be recalculated, just looked up and returned.

Now let’s convert what we’ve learnt into code and examine what we can implement in python :)

### Code

In python, we have two main tools to use for looping

1. While Loops
2. For Loops

#### **While Loops**

While Loops allows us to run a command indefinitely.

```
x = 1y = 2
```

```
while(x=2):    print("x is looping")
```

```
while(y=2):    print("Y is looping")
```

In the code above, only the second while loop will evaluate while the first will not. When we run the code, we’ll get the following output

```
>>>python runapp.pyY is loopingY is loopingY is loopingY is looping....
```

Here’s what happens for the first variable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*icabgqLnTLvv5Jlr7Ogmhw.png)

As seen above, the while loops does not print x since it does not meet the condition stipulated in the first while loop.

How about the second condition? Well it follows something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*WORh1EJzN6GGPeziMn4pEw.png)

As we can see, the while loop constantly checks if a condition is true and only executes if the specified condition is true.

Here are some common implementations in python:

```
#Asking for User Inputwhile True:    userinput = input("Please Input Your Name: ")    if userinput.isalpha():       break;
```

```
print("Hello %s"%(userinput))
```

```
#Dealing with dynamic Variables (i.e. Parameters that can change )no = int(input("Please Enter the number of Loops: "))i = 0
```

```
while(i<n):    print(i)
```

Let’s look through the two examples.

#### Example 1

This example code (refer above) is a sample of code we could use to grab some user input. As you code more advanced programs, you’ll be able to code more advanced programs that can check user input or do more things with user input, but for now, we’re gonna print “Hello <userinput>”:

```
While True:
```

Since True is always true ( I know it’s a bit counterintuitive but bear with me), this loop will run forever. **True can never not be True**.

```
userinput = input("Please Input Your Name: ")
```

This allows us to get some input from the user and store it as a string. We create a variable called userinput and store a reference to that stored string in memory. (If you’re unsure about what’s happening here, I’ve written an [article](https://medium.com/@ivanleomk/a-crash-course-in-python-variables-cbad43b4efef) on variables in python, do check it out!)

```
if userinput.isalpha():       break;
```

Now comes the magic sauce. The .isalpha() method allows us to check if a string solely consists of characters.

```
#Sample Output"12a".isalpha() #This returns False"12".isalpha() #This returns False"abc".isalpha() #This returns True
```

Using this function allows us to check if the user has input a proper name that consists solely of characters in the alphabet.

If the user has input a proper name, the break function then allows us to exit the loop.

```
print("Hello %s"%(userinput))
```

This then allows us to execute the final line of code, printing out the string “hello <userName>”.

#### **Example 2 : Looping for a number of Loops**

```
no = int(input("Please Enter the number of Loops: "))
```

This first line of code allows the user to input a certain value from the command line before converting it to an integer. This is done using the int() value.

```
i = 0
```

```
while(i<n):    print(i)
```

Next we initialise a variable i to 0 to keep track of the number of loops we want to run, printing the value of i each time:

```
#Sample OutputPlease Enter the number of Loops: 501234
```

It’s helpful to think of a while loop as such

```
while(test_expression):    <code>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kHHhyQObLXAP3SmoVMqA0A.png)

**For Loops**

For Loops work a little differently than while Loops. Let’s examine the syntax

```
#Normal For LoopFor i in range(1,6,1):    <code>
```

```
#Iteration Loopfor i in [1,2,3,4,5]:    <code>
```

What’s happening here?

When you declare a For loop as seen in the first case , you are invoking what is known as a generator. This generates a list of numbers using the parameters you have specified.

It’s helpful to think of the generator as a function that calls a list for now. While that’s not exactly how it works, it’s a close approximation. More to come on this topic!

```
#This generates a list with values [1,2,3,4,5]For i in range(1,6,1):    <code>
```

This generated list can then be iterated using the inbuilt iteration function in python. This just means that we can call each item in this list in the order they are stored in.

The second example functions in a similar way. In this case however, we explicitly specify the list to be iterated over instead of generating it with the range function.

```
for i in [1,2,3,4,5]:    <code>
```

**Some useful cases**

```
#Printing out items in a list
```

```
x = [...values...]for i in x:   print(i)
```

```
#Iterating Over items in a listy = [x**2 for i in x] #This is also known as list comprehension
```

Let’s examine these cases in greater detail!

**Example 1**

```
x = [....values...]for i in x:
```

In this case, we are initialising a list called x with a certain number of variables. We then proceed to iterate over each value in x.

```
print(i) #This prints out each value of x in its specified order
```

We call each value in x, in this case referred to as i, and print it out.

```
#Sample Outputx  = [1,2,3,4]for i in x:     print(i)
```

```
>>>python app.py1234
```

**Example 2**

```
y = [x**2 for i in x]
```

Let’s try to rewrite this in another form

```
for i in x:    y.append(x**2)
```

```
y = [x**2 for i in x]
```

These 2 are the same thing! However, list comprehensions tend to be faster.

### Decision-Making

What comes to your mind when you think of decision-making while writing a program? For me, it’s definitely decision trees and flowcharts.

While some of these (like the one below) are definitely ridiculous, I think they still offer a useful mental framework to visualise your program flow:

![Image](https://cdn-media-1.freecodecamp.org/images/0*V7qQs8M52EamG3zx)

I’ll use an analogy to talk about this before going on to show how to implement this using if-else and break-continue syntax.

#### Analogy-Time

Imagine that you’re trying to find the perfect restaurant for date night. You want to find something that is affordable and chic

While you’re looking through trip advisor, your thought process would be something like this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S2cZhcS1mOIqMJMTu3SMdA.png)

You would only consider things that were cheap and chic. So every time you looked at a restaurant, you would check to see if it fit your criteria and eliminate those that did not.

Similarly, decision making in a program works the same way. You set a bunch of possible scenarios and your program reacts accordingly.

#### code

Let’s look at a simple program to find numbers which are multiples of two.

```
import random
```

```
x = random.randint(0,1000)
```

```
if x%2==0:
```

```
    print(str(x)+" is a multiple of 2")
```

```
else:
```

```
    print(str(x)+" is not a multiple of 2")
```

How does this program work?

1. We first generate a random number from 0 to 1000
2. We then divide this random number, x, by 2 and check if there is a remainder. ( % returns the remainder of a division )
3. If there is no remainder, we print the statement “X is a multiple of 2”
4. if there is a remainder, we print the statement “x is not a multiple of 2”

We know that all multiples of 2 follow the formula 2i where i is an integer. Therefore all multiples of 2 have to be divisible by 2. Hence, we use that as a way to evaluate if a number is a multiple of 2.

This can be visualised as a decision tree, as seen below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1PJI_rd7EMG5HVr6MFayig.png)

As we can see, an if-else decision loop allows us to account for the values of our variables, allowing our program to return a different output w.r.t their values.

We can also use an if-else loop to account for the type of variables by modifying the above syntax slightly.

```
def checking(n):
```

```
    if type(n) == str:
```

```
        print("String!")
```

```
    elif type(n) == int:
```

```
        print("Integer!")
```

```
    else:
```

```
        print("we're not sure what n is....")
```

```
x = [1,2,3,'a','bac',2.12]for i in x:    checking(i)
```

Pointers to note:

1. We’ve used the elif statement in this context to add an additional possible case of n that we want to account for.
2. We’ve also used type as a condition to evaluate the variable instead of the original use of the value of the variable.

### Exception-Handling

Sometimes in python, you will find that you’ll need to account for exceptions. These could be invalid operations (Eg. trying to divide 0 or stack overflow) or a class of values that you simply aren’t interested in.

In these cases, we can use

1. Continue
2. Pass
3. Try-except
4. Break

I’ll try to give a brief overview of the usage of these exception handling operations.

#### Continue

Look at the code below and try to guess what continue does:

```
y = [1,2,3,4,5,6,6,7,8]
```

```
x = []
```

```
for i in y:
```

```
     if i in x:
```

```
         continue
```

```
     else:
```

```
         x.append(i)     print(i)
```

```
print(x)
```

If you guessed that it basically skips the rest of the chunk of code, you’re right! Continue does just that.

In the code above, we are trying to remove the duplicate values in y. We do so in the code using this process

1. We check if the variable, i, that we are evaluating is within the new list x.
2. If it is within the new list x, we “continue” and proceed to evaluate the next variable within list y.
3. if it is not within the new list x, we do not “continue” and instead proceed to append the variable to list x.

This eventually helps us to remove all the duplicate variables within x.

#### Pass

```
y = [1,2,3,4,5,6,6,7,8]
```

```
x = []
```

```
for i in y:
```

```
    if i in x:
```

```
         pass
```

```
    else:
```

```
         x.append(i)    print(i)
```

```
print(x)
```

If you were to run the code, you would also notice that all of the duplicate variables were printed! This is a key difference between pass and continue.

This difference becomes useful if you are trying to run additional operations on the non-duplicate variables (eg. get a sum).

#### Break

Break does what it says. It breaks your program or sub-program when you meet an exception.

Here’s a useful example of break:

```
x = [1,3,5,7,2,3,5,7]
```

```
count = 0
```

```
for i in range(len(x)):
```

```
if x[i]%2==0:
```

```
    print("There is an even number at index " + str(i))
```

```
    break
```

```
else:
```

```
    continue
```

In this example, we are trying to find the index of the first even number in our list x. Break allows us to do so by exiting the loop prematurely!

#### Try-Except

Try-Except syntax is especially useful when it comes to dealing with errors in reading files or evaluating syntax. Some of the common exception errors are

1. IOError: An inability to open the file
2. ImportError: Python cannot find and open the module you want to import
3. ValueError: When you pass a value into a function with the wrong type or value
4. KeyboardInterrupt: When you prematurely terminate your program
5. EOFerror: When you’ve reached the end of the file

Here’s an example of us trying to check for a ValueError:

```
try:
```

```
    x = int(input("Please input some numbers: "))
```

```
    print(x)
```

```
except ValueError as ve:
```

```
    print("Please input numbers. NUMBERS not letters")
```

This program works because strings and letters cannot be coerced into integers. (Unless they’re integers which have been stored as strings i.e. “2”, “3” etc.)

For those working with importing files, you might be familiar with ImportErrors. These can be accounted for by using the following syntax:

```
try:
```

```
    f = open('nofile.txt')
```

```
except FileNotFoundError:
```

```
    print("Erm...there's no such file man")
```

The Try-except syntax can be thought of as such.

```
try:    <code to be run in a nice world>except <Most Likely Error Name>:    <code to be run in error case 1>except <Another Likely Error>:    <code to be run in another unlikely error>
```

### Conclusion

This sorta sums up basic decision making in Python and many other programming languages. While the exact syntax will definitely differ, the basic principles are roughly the same.

Once you’ve got the hang of control flow, you’ll be able to build programs that will make a big difference and can work the way you want! :)

If you’ll like to read more about Variables in Python, check out an article I wrote on them [here](https://medium.com/@ivanleomk/a-crash-course-in-python-variables-cbad43b4efef)!

