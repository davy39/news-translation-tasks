---
title: Programming VS Coding VS Development – What's the Difference?
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-07-20T20:04:12.000Z'
originalURL: https://freecodecamp.org/news/programming-coding-developement-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Programming-vs-coding.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'In my very early days as a budding web developer, I made a fairly common
  mistake.

  On Facebook, I sent a friend request to a senior software engineer (I wasn''t aware
  of his position at the time) and started a chat with him thereafter. Done with greeti...'
---

In my very early days as a budding web developer, I made a fairly common mistake.

On Facebook, I sent a friend request to a senior software engineer (I wasn't aware of his position at the time) and started a chat with him thereafter. Done with greetings and pleasantries, I curiously asked him this: “So are you a coder?”

That stirred up a response I wasn’t expecting and I got a schooling that I was more than happy to receive.

A lot of people do this very same thing – they use the terms **"programmer"**, **"coder"** and **"developer"** synonymously. But do these three terms mean the same thing?

Well, not quite.

## What is Programming?

Programming is logic. Programming is thinking.

Programming is making decisions, or telling the computer what decisions to make under different circumstances. Once you've clicked the red button, you can program a computer/browser to access data and make a network request.

**Here is a grossly simplified example of a program:**

*If an email supplied by a user isn’t following the conventional format (i.e it misses the ‘@’ and ‘.com’), display an error message. Else, take the email and check if it already exists in the database. If it already exists, display a customized message to the user. Else, store the email in the database and display a success message.*

This is simple logic and has nothing to do with code (yet). Of course, the more complex the application, the more thinking you need to do.

Programming makes use of your critical thinking skills and ability to solve logical problems. It all about thinking up and creating the network of possible decisions a computer or browser should make ([also known as algorithms](https://www.freecodecamp.org/news/algorithm-definition/)).

In fact, you can do programming in English because it has nothing to do with any particular language.

This brings us to the second term: coding.

## What is Coding?

I will call coding a subset of programming. Coding encompasses the following topics and activities:

* Programming languages
    
* A language's syntax and how it differs from other language's syntax
    
* Code arrangement
    
* Code optimization
    
* Debugging
    
* Writing and running tests
    
* Creating and using libraries and frameworks
    

And so on.

> You can be a programmer without being a coder, but you cannot be a coder without being a programmer.

While a programmer simply has to think and build a logical framework of decisions for the application, a coder has to implement that logic with a particular programming language in a standard, efficient way.

A coder has to become familiar with code syntax and be up-to-date with newer and recommend ways of writing code.

A coder has to be good at technical tasks like testing, debugging, and so on.

Code is simply the language a machine understands. To implement an application, you have to take the set of instructions created by a programmer and make it understandable by the machine. That is the act of coding.

Using the same example of email validation and storage, let's implement that logic in JavaScript code:

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

Now we have coded that programming logic for a web browser to execute. In other words, we have **programmed** the browser engine to **make decisions**. This wouldn't have been possible without writing code.

Not all types of code can be used to code programs/instructions. An [example of such code is HTML](https://www.freecodecamp.org/news/the-html-handbook/).

## What is Software Development?

So now you might be wondering, **what is software development?** According to [Wikipedia](https://en.wikipedia.org/wiki/Software_development), software development is:

> "the process of conceiving, specifying, designing, programming, documenting, testing, and bug fixing involved in creating and maintaining applications, frameworks, or other software components.
> 
> Software development is a process of writing and maintaining the source code, but in a broader sense, it includes all that is involved between the conception of the desired software through to the final manifestation of the software, sometimes in a planned and structured process.
> 
> Therefore, software development may include research, new development, prototyping, modification, reuse, re-engineering, maintenance, or any other activities that result in software products."

As you can see from the above extensive definition, development is bigger than just programming and coding. It’s all about creating a solution to a real life problem by building an application which solves that problem, maintaining that application, marketing it, researching mays to optimize it, and so on.

Development has to take into consideration the end user, DevOps (a portmanteau of “development” and “operations”), team management, and many other things.

A developer analyzes everything that is required to create a proposed application and also oversees that development process.

A great example of a software developer would be a technical startup founder.

They conceive an application as a software product which will be a valuable service to people in real life. They undertake the process of bringing that conception to life, including the actual programming and coding of the application.

Then they oversee the maintenance of the application. They might even fund research to improve the performance and efficiency of their company's service and so on.

Development is the full package.

## My Thoughts about Programming vs Coding vs Development

Your mindset is very important. Think of software development as a process which should always start with programming. You will be better off training yourself as a programmer before becoming a coder.

Admittedly, some people actually learn how to program by studying simple loops and code. That is also good. That is why I advise newcomers to take [Data Structures and Algorithm courses](https://www.freecodecamp.org/news/data-structures-and-algorithms-in-javascript/).

Making a clear distinction between these three terms can help you learn software development faster. It'll help you know what to prioritize in your learning. And it'll let you look at the whole process of software development from a different perspective.

On a lighter note, it can help you avoid awkward situations with developers who love their titles a little too much. :)

Recently I came across a YouTube video which aptly distinguishes the difference between the three terms. I think you might benefit from it:

%[https://www.youtube.com/watch?v=CIRGjwYgdT4] 

## Conclusion

Programming is all about conceiving a network of logical patterns that defines the behaviour of your application.

Coding involves implementing the set of instructions in a form that a machine understands and in a way that is optimal.

Development is about delivering a proper product and maintaining it. Development encompasses the processes of creating a complete package to the pleasure and satisfaction of end users.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/programming-vs-coding-vs-deve.png align="left")

*Quick summary note*

I hope you gained some insight from this article. This topic has been a subject of huge debate and you might disagree with me on some points, which is totally fine. I am just sharing my opinion on the matter.

You can check out some of my other posts on my personal [blog](https://ubahthebuilder.tech).

Thank you for reading.

> P/S: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
