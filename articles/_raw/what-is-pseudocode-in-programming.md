---
title: What is Pseudocode? How to Use Pseudocode to Solve Coding Problems
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-07-26T19:23:37.000Z'
originalURL: https://freecodecamp.org/news/what-is-pseudocode-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Pseudocode.png
tags:
- name: Problem Solving
  slug: problem-solving
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'You might be wondering what pseudocode is and why it''s so useful for writing
  computer programs.

  But before we jump into pseudocode, let''s refresh our memories about what programming
  and coding are, in the simplest sense.

  Programming is the manifestat...'
---

You might be wondering what pseudocode is and why it's so useful for writing computer programs.

But before we jump into pseudocode, let's refresh our memories about what programming and coding are, in the simplest sense.

Programming is the manifestation of logic. A program is a set of instructions that defines the behaviour of your software application. Writing code is how you implement it for the machine.

## What is Pseudocode?

Pseudocode literally means ‘fake code’. It is an **informal** and **contrived** way of writing programs in which you represent the sequence of actions and instructions (aka algorithms) in a form that humans can easily understand.

You see, computers and human beings are quite different, and therein lies the problem.

The language of a computer is very rigid: you are not allowed to make any mistakes or deviate from the rules. Even with the invention of high-level, human-readable languages like JavaScript and Python, it’s still pretty hard for an average human developer to reason and program in those coding languages.

With pseudocode, however, it’s the exact opposite. You make the rules. It doesn’t matter what language you use to write your pseudocode. All that matters is comprehension.

In pseudocode, you don't have to think about semi-colons, curly braces, the syntax for arrow functions, how to define promises, DOM methods and other core language principles. You just have to be able to explain what you're thinking and doing.

## Benefits of Writing Pseudocode

When you're writing code in a programming language, you’ll have to battle with strict syntax and rigid coding patterns. But you write pseudocode in a language or form with which you're very familiar.

Since pseudocode is an informal method of program design, you don’t have to obey any set-out rules. **You make the rules yourself.**

Pseudocode acts as the bridge between your brain and computer’s code executor. It allows you to plan instructions which follow a logical pattern, without including all of the technical details.

Pseudocode is a great way of getting started with software programming as a beginner. You won’t have to overwhelm your brain with coding syntax.

In fact, many companies organize programming tests for their interviewees in pseudocode. This is because the importance of problem solving supersedes the ability to ‘hack’ computer code.

You can get quality code from many platforms online, but you have to learn problem solving and practice it a lot.

Planning computer algorithms with pseudocode makes you meticulous. It helps you explain exactly what each line in a software program should do. This is possible because you are in full control of everything, which is one of the great features of pseudocode.

## Example of Pseudocode

Pseudocode is a very intuitive way to develop software programs. To illustrate this, I am going to refer back to a very simple program I wrote in my [last article](https://www.freecodecamp.org/news/programming-coding-developement-whats-the-difference/):

When a user fills in a form and clicks the submit button, execute a ValidateEmail function. What should the function do?

1. Derive an email regular expression (regex) to test the user's email address against.
    
2. Access the user's email from the DOM and store it in a variable. Find and use the right DOM method for that task.
    
3. With the email value now accessed and stored, create a conditional statement:
    

* If the email format doesn’t match the rule specified by the regex, access the element with the `myAlert` id attribute and pass in the “Invalid Email” message for the user to see.
    
* Else, if the above condition isn’t true and the email address format actually matches with the regex, check to see if the database already has such an email address. If it already does, access the element with the `myAlert` id attribute and pass in the “Email exists!” message for the user to see.
    
* Now, if both of these conditions aren’t met, (that is the email format matches the regex and the database doesn’t have such an email address stored yet), push the users email address into the database and pass in the “Successful!” message for the user to see.
    

Once you are done outlining the various steps you want your code to take, everything becomes easier and clearer. Now, let’s turn that psedocode into real JavaScript code:

```js
let database = ['test1@gmail.com', 'test2@gmail.com', 'test3@gmail.com'];

function validateEmail() {
    let regexEmail = /^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/;
    let emailAddress = document.getElementbyID('emailFld').value;
    if (!emailAddress.match(regexEmail)) {
        document.getElementbyID('myAlert').innerHTML = "Invalid Email!";
    } else if (database.includes(emailAddress)) {
        document.getElementbyID('myAlert').innerHTML = "Email exists!";
      else {
        database.push(emailAddress);
        document.getElementbyID('myAlert').innerHTML = "Successful!";
        return true;
      }
}
    
document.getElementById("myBtn").addEventListener("click", validateEmail);
```

All you have to do at this stage is find the programming language constructs that will help you achieve each of your steps. Noticed how seamless the transition from pseudocode to actual code became? That’s how effective writing pseudocode can be for program design.

Pseudocode is also a great way to solve programming-related problems when you're struggling with them. For those practising programming in coding challenge platforms like [CodeWars](https://www.codewars.com/dashboard), pseudocode can be of immense help.

## How to Solve Programming Problems with Pseudocode

Solving programming problems can be hard. Not only do you have the logical part to reckon with, but also the technical (code forming) part as well. I recently uncovered a brilliant and effective formula for solving tricky coding problems.

Here are the steps you can follow to solving programming problems with pseudocode:

### Step 1: Understand what the function does

First, you need to understand that all a function does is (optionally) accept data as input, work on the data little by little, and finally return an output. The body of the function is what actually solves the problem and it does so line by line.

### Step 2: Make sure you understand the question

Next, you need to read and understand the question properly. This is arguably the most important step in the process.

If you fail to properly understand the question, you won’t be able to work through the problem and figure out the possible steps to take. Once you identify the main problem to be solved you'll be ready to tackle it.

### Step 3: Break the problem down.

Now you need to break down the problem into smaller parts and sub-problems. With each smaller problem you solve, you'll get closer to solving the main problem.

It helps to represent these problem solving steps in the clearest and most easily understandable way you can – which is psedocode!

* Start solving: open and use tools like Google, Stack Overflow, MDN, and of course freeCodeCamp! :)
    
* For every step of the problem that you solve, test the output to make sure you’re on the right path. Keep solving these small problems until you arrive at the final solution.
    

I picked up this highly effective formula from Aaron Jack and I think you’ll benefit from it. Check out his video about how to solve coding problems:

%[https://www.youtube.com/watch?v=Dblfmk3ATeg&t=526s] 

## Conclusion

As you can see, pseudocode is a very useful strategy for planning computer programs.

Of course, you have to remember that pseudocode is **not a true representation** of a computer program. While using pseudocode to plan your algorithm is great, you will ultimately have to translate it into an actual computer-readable program. This means that you'll eventually need to learn how to program in a real programming language.

Taking up coding challenges online is a great way to learn how to program because, as they say, practice makes perfect. But when you try your next challenge, don’t forget to implement pseudocode in the process!

You can check out some of my other programming-related posts on my personal [blog](https://ubahthebuilder.tech/). I am also available on [Twitter](https://twitter.com/ubahthebuilder).

Thank you for reading and see you soon.

> P/S: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
