---
title: Python Program to Print the Fibonacci Sequence
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-27T00:34:03.000Z'
originalURL: https://freecodecamp.org/news/python-program-to-print-the-fibonacci-sequence
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-jeff-wang-462402.jpg
tags:
- name: algorithms
  slug: algorithms
- name: interview questions
  slug: interview-questions
- name: Python
  slug: python
seo_title: null
seo_desc: "By Sonia Jessica \nQuestions about the Fibonacci Series are some of the\
  \ most commonly asked in Python interviews. \nIn this article, I'll explain a step-by-step\
  \ approach on how to print the Fibonacci sequence using two different techniques,\
  \ iteration a..."
---

By Sonia Jessica 

Questions about the Fibonacci Series are some of the most commonly asked in Python interviews. 

In this article, I'll explain a step-by-step approach on how to print the Fibonacci sequence using two different techniques, iteration and recursion. 

Before we begin, let's first understand some basic terminology.

## What is the Fibonacci Sequence?

The [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number) is a sequence of numbers in which a given number is the result of adding the 2 numbers that come before it. And adding the previous 2 numbers some number of times forms a series that we call the Fibonacci Series.

The Fibonacci sequence starts with two numbers, that is 0 and 1. Then every following number is made up of adding the previous two numbers together.

For example, take 0 and 1. They're the first two numbers in the sequence. If you add them together, you get 1. So the sequence starts 0, 1, 1,...

Then, to find the next number, you add the last number you have and the number before it. So 1+1 = 2. So the sequence so far is 0, 1, 1, 2, ... Make sense?

We can represent this more mathematically like 0, 1, (1) - [0 + 1]. Similarly, the next Fibonacci number is - 0, 1, 1, (2) - [1 + 1]. And so on. Here's a diagram showing the first 10 Fibonacci numbers:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Fibonacci-series.png)

This is an example of a Fibonacci series – **0, 1, 1, 2, 3, 5, 8, 13, 21,** **34**. Within this continuous sequence, every individual number is a Fibonacci number. 

Mathematically, the Fibonacci Sequence is represented by this formula: 

**F(n) = F(n-1) + F(n-2)**, where **n > 1**. 

We can use this sequence to find any nth Fibonacci number. 

This fascinating sequence is widely associated with the mathematician Leonardo Pisano, also known as Fibonacci. He was from the Republic of Pisa, which is why he is also known as Leonardo of Pisa. 

Leonardo was known as one of the most talented mathematicians of the middle ages.

## How to Print the Fibonacci Sequence in Python 

You can write a computer program for printing the Fibonacci sequence in 2 different ways:

* Iteratively, and
* Recursively.

Iteration means repeating the work until the specified condition is met. Recursion, on the other hand, means performing a single task and proceeding to the next for performing the remaining task. 

### Here's an iterative algorithm for printing the Fibonacci sequence:

1. Create 2 variables and initialize them with 0 and 1 (first = 0, second = 1)
2. Create another variable to keep track of the length of the Fibonacci sequence to be printed (length)
3. Loop (length is less than series length)
4. Print **first + second**
5. Update **first** and **second** variable (first will point to the second, and the second will point to first + second)
6. Decrement the length variable and repeat from step 3
7. Once the loop terminates, terminate the program

### How the iterative algorithm works:

Consider that we need to print a Fibonacci sequence of length 7. Then the flow of the algorithm will be like this:

|Iterations|Steps Explained|Output|
|----|--------|---------|
|Initial|First = 0, Second = 1|[0, 1]|
|1|Print (first + second) = [0+1] Now variable `first` will point to variable `second`. And second will point to the next Fibonacci number that we calculated above.|[0, 1, 1]|
|2|Print (first + second) = [1+1] Now variable first will point to variable second. And second will point to the next Fibonacci number that we calculated above.|[0, 1, 1, 2]|
|3|Print (first + second) = [1+2] Now variable first will point to variable second. And second will point to the next Fibonacci number that we calculated above.|[0, 1, 1, 2, 3]|
|4|Print (first + second) = [2+3] Now variable first will point to variable second. And second will point to the next Fibonacci number that we calculatod above.|[0, 1, 1, 2, 3, 5]|
|5|Print (first + second) = [3+5] Now variable first will point to variable second. And second will point to the next Fibonacci number that we calculated above.|[0, 1, 1, 2, 3, 5, 8]|


So the final Fibonacci sequence for length 7 will be  **[0, 1, 1, 2, 3, 5, 8]**.

### Iterative Python Code for printing Fibonacci Sequence:

```python
def PrintFibonacci(length):
    #Initial variable for the base case. 
    first = 0
    second = 1

    #Printing the initial Fibonacci number.
    print(first, second, end=" ")

    #decreasing the length by two because the first 2 Fibonacci numbers 
    #already printed.
    length -= 2
    
    #Loop until the length becomes 0.
    while length > 0:

        #Printing the next Fibonacci number.
        print(first + second, end=" ")

        #Updating the first and second variables for finding the next number. 
        temp = second
        second = first + second
        first = temp

        #Decreasing the length that states the Fibonacci numbers to be 
        #printed more.
        length -= 1

if __name__ == "__main__":
    print("Fibonacci Series - ")
    PrintFibonacci(7)
    pass
```

[Output](https://www.interviewbit.com/snippet/242ec6ca5cec8a2fcaf6/) for length 7:

```python
Fibonacci Series - 
1 1 2 3 5 8
```

**Explanation of the Code:**

In the above code, first we have defined a function that will print the Fibonacci series. It accepts a parameter for the length, and the function needs to print the Fibonacci series.

Next, we have created 2 variables that contain the initial 2 Fibonacci values, that is 0 and 1.

Then we printed the first 2 values [0, 1] and decremented the length by 2, because 2 values were already been printed.

We will run a loop for the remaining length time, and each time print the next Fibonacci value by adding the previous 2 terms that are stored in the first and second variables (that we created initially to keep track of the previous 2 values).

Update the first and second values that will point to the previous 2 values [first = second, and second = previous first + second].

The loop will run until the length becomes 0, which states that the required length of the Fibonacci sequence is printed.

Then we call the function defined for printing Fibonacci from the main function by passing the argument of the required length to be printed. And there you have it!

There is another approach for printing the Fibonacci sequence using the help of recursion. So let’s understand that approach, too.

### Recursive Algorithm for printing the Fibonacci Sequence: 

* Accept the value of the previous first and second Fibonacci number as the length to be printed.
* Check if the length is 0 then terminate the function call.
* Print the Fibonacci value by adding the previous 2 values received in the parameter of the function (first and second).
* Recursively call the function for the updated value of the first and second, as well as the decreased value of length.

For this recursive function call, we need to pass the initial value of Fibonacci, that is (0 and 1), in the first and second variables.

To help you understand this algorithm better, let’s see the Python implementation of the algorithms. Then we'll look at an example so you can see how this recursive algorithm works.

### Recursive Python Code for Printing the Fibonacci Sequence:

```
def PrintFibonacci(first, second, length):

    #Stop the printing and recursive calling if length reaches 
    #the end.
    if(length == 0):
        return

    #Printng the next Fibonacci number.
    print(first + second, end=" ")

    #Recursively calling the function by updating the value and 
    #decrementing the length.
    PrintFibonacci(second, first+second, length-1)

if __name__ == "__main__":
    #Print initial 2 values.
    print(0,1,end=" ")

    #Calling the Function to print the remaining length 
    #fibonacci series
    PrintFibonacci(0,1,7-2)
```

[Output](https://www.interviewbit.com/snippet/1e85af84b1916aed890b/):

```python
For Length 7 
1 1 2 3 5 8

For Length 10
1 1 2 3 5 8 13 21 34
```

**Explanation of the code:** 

First, we created a function and perform recursion on it. In that function, we accepted the value of the previous 2 Fibonacci numbers to calculate the current Fibonacci number. And we have a length that keeps track of the base case.

For the base case of recursion, we are checking if the length reaches 0. If it does, then we will terminate the recursive call.

In other cases, we are printing the Fibonacci number by adding the previous 2 Fibonacci numbers. 

And then we recursively call the function to print the next Fibonacci value by updating the previous 2 values and decrementing the length.

Now let’s visualize the recursive calls of this function with the help of a recursion tree. The length we want printed is 7.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/length-to-be-printed-is-7.png)

Before the recursive call is made, the main function prints the initial 2 values, 0 and 1. And then it passes these values to the recursive function.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/main-function-prints-the-initial-2-values.-0-and-1.png)

The Recursive function is printing the value (0 + 1) and recursively calls with the next updated value.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Recursive-function-is-printing-the-value--0---1-.png)

Then the recursive function is printing the value **(1 + 1)** and recursively calls with the next updated value.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-1-2-3-.png)

Now the recursive function is printing the value **(1 + 2)** and recursively calls with the next updated value.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-2-3-2-.png)

And then the recursive function is printing the value **(2 + 3)** and recursively calls with the next updated value.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-3-5-1-.png)

Now the recursive function is printing the value **(3 + 5)** and recursively calls with the next updated value.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-5-8-0-.png)

Finally, the last call is made. And the length is 0, so it will terminate the recursive call again and the series is printed on the console.

## Time Complexity Analysis 

### For the Iterative Approach

In the Iterative algorithm, we are looping until the length becomes 0. In the loop, we are performing a constant time operation of printing the value and updating the variables.  

If we consider that length to be n, then the time complexity will be **O(n)**. 

### For the Recursive Approach

In the recursive approach, we are calling recursive functions up to the given length number of times. We are also doing a simple constant operation of printing.

 So in this also if we consider the length to be n numbers, then the time complexity will be **O(n)**.

## Space Complexity Analysis

### For Iterative Approach 

In the iterative approach we haven't taken the extra memory to accept the two variables that keeps track of the previous two Fibonacci numbers and the constant to any number of the series length. So the space complexity will be constant O(1).

### For the Recursive Approach

In the recursive approach, we are calling the functions of the length number of times. We know that the recursion internally uses a call stack. 

So if we consider that to be memory taken by the program, then the recursive call is made the length number of times. Then the space complexity will be O(n). 

## Conclusion 

The Fibonacci sequence is the series of numbers in which every number is the addition of its previous two numbers. 

Fibonacci sequences are found not only in mathematics but all over the natural world – like in the petals of flowers, leaves or spines of a cactus, and so on. 

It's also a commonly asked interview question – so it's good to know how it works.

I took inspiration from this post from [InterviewBit](https://www.interviewbit.com/python-interview-questions/).

