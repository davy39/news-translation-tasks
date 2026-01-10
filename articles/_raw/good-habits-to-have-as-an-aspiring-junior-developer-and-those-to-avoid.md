---
title: Good habits to have as an aspiring/junior developer - and habits to avoid
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-09-13T10:36:36.000Z'
originalURL: https://freecodecamp.org/news/good-habits-to-have-as-an-aspiring-junior-developer-and-those-to-avoid
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/Good-habits-arrow-6x4.jpg
tags:
- name: best practices
  slug: best-practices
- name: coding
  slug: coding
- name: Habit Building
  slug: habit-building
seo_title: null
seo_desc: 'When you''re learning to code, it can be easy to pick up some nasty habits
  along the way. Here are some tips to avoid common bad habits, and the good habits
  to keep in mind.

  The good habits

  Let''s start with the positive shall we? These are the best ha...'
---

When you're learning to code, it can be easy to pick up some nasty habits along the way. Here are some tips to avoid common bad habits, and the good habits to keep in mind.

## The good habits

Let's start with the positive shall we? These are the best habits that often impress me when working with Junior Developers (and all developers for that matter).

## Commit/Push code often 

Chances are you'll have come across terms like "Git", and "GitHub", "source control" whilst on your coding journey. If you haven't:

1) Where have you been?!?

2) You can learn about it here: [https://www.freecodecamp.org/news/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba/](https://www.freecodecamp.org/news/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba/)

Source control is a marvellous thing. It's a backup of your code, allows you to track changes, and let's you quickly roll back when you have that "oh s***! everything is broken!" moment whilst coding.

Not to mention it makes life much, much easier when working as part of a team. I can't imagine working on code collaboratively without it - sharing code over email and slack?! ***Quivers***.

A good habit to have is to **commit code often,** even for your own side projects as practice. Personally I like to "**check in**" my code when I have a completed a small part of my project. For example, if I were creating a TODO list app, I would commit and push my code when I have added the '_new todo button'_, or when I've completed the '_checkbox functionality'._ 

There are no hard and fast rules as to _when_ to check in code. Other good times to commit code are:

* If you are about to finish up for the day (see a very important rule below)
* Before you do a major refactor or code change
* If there is a fire in the building (Just kidding, safety first)

There is only 1 important rule to follow when committing code.

> The code must build successfully and the tests must pass

Does that count as 2 rules? Anyways, this is important. Something that is guaranteed to bring any development team to a halt is broken code. So before you commit your code, make sure the code builds and the tests pass!

Lastly, make sure to use **good commit messages**. "Fixed bug" isn't as clear as "Fixed issue with 'save todo' button not calling onClick function correctly". This will not only be helpful for yourself but your teammates as well.

## Use clear naming for variables, functions, and files

Ah naming. The one thing in web development that we all thought was easy, is sneakily difficult at times. Naming is important though, as it makes our code easier to read and understand. 

When choosing a name for your variables, functions and files, try to make it as descriptive as possible. Why?

* It makes it easy to quickly skim over code. If you see a method called `getUsers()` Without having to look at that method, you can be pretty sure that it's going to return a list of users.
* Helps enforce **separation of concerns.** Oooh a fancy new term! Don't worry, this just means keeping related things together. For example in a Node.js app, if you have a `/users` endpoint and a `/products` endpoint, you might keep the `users` logic in the same file ( `usersService.js` for example ) and keep the `products` logic in another file. Wouldn't this make it easier to find things?

Here's a simple function which is badly named (as are the parameter names) can you guess what it does?

```js

const function1 = (x, y) => {
    return x + y
}

```

This function could either **add 2 numbers** or **concatenate 2 strings,** but it's original intent is not clear. Let's say its intention was to add numbers, but another unsuspecting developer comes along and uses it to concatenate 2 strings. It might be ok for now, but later if we refactor this function to _validate the numbers,_  then the code calling this function to concatenate strings will break. Oh no!

Here's the function with better naming:

```js

const addNumbers = (num1, num2) => {
    return num1 + num2
}

```

Now it's a bit clearer on what the function does, and what the parameters are.

## Practice debugging 

Would you believe that web developer's spend just as much time (if not more) fixing bugs? Yes, there will be bugs. And the best way to identify and fix a bug is to **debug the code.** Debugging is the process of "stepping" through your code, line by line, until you discover something you didn't expect. 

Luckily for us web developers, many IDE's come with built in debuggers that makes this really easy (here's a VS Code guide to setting up debugging for different languages. For other IDE's you can check out Google [https://code.visualstudio.com/docs/editor/debugging](https://code.visualstudio.com/docs/editor/debugging))

So how do you effectively debug your code? Here's a few pointers:

* **Replicate the issue** - replicate the bug a few times so you understand exactly what it is that causes the bug
* **Think** - before you dive into the code and start aimlessly scavenging around, stop and think. Why would this be happening? What area's of the code are related to this?
* **Investigate the code** - once you've had an idea of what areas of the code this is likely to affect, start digging in. After reading over the code, you might spot the issue. Hurray! If not, time to get out debugger out.
* **Debug** - Fire up the debugger, and go through the code line-by-line. Keep an eye on variable values (and how they change) and which functions get called (and which don't). Are the correct branches in an `if` statement being called? Are events being triggered correctly? Are calculations being performed correctly?

## Plan before coding 

You have just awoken from a good nights sleep. You're eating breakfast and all of a sudden an awesome new side project idea comes to you. What a fantastic idea it is! A revelation!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-88.png)

You burst out of your chair towards your laptop, cornflakes flying everywhere, and start frantically coding. (Or is this just me? OK moving swiftly along...)

While it is often tempting to jump straight into your IDE and start coding, a bit of planning can go a long way.

* Reduces the amount of "wasted" code 
* Reduces code changes
* Gives you solid goals to work towards
* It's an impressive skill for junior developers to have - it shows your critical thinking!

I won't go into too much detail here, as I've written a more comprehensive article on this topic here: **[How Developers Think: A Walkthrough of the Planning and Design Behind a Simple Web App](https://www.freecodecamp.org/news/a-walk-through-the-developer-thought-process/)**

Here's a quick summary from the above article for now:

* "**What does it do?**" - write out the features you want your app to have
* "**What does it look like?**" - make a quick sketch or wireframe with what your app should look like
* "**How do I position and style the elements?**" - once you have your wireframes, start thinking about how you will position everything on the page
* "**How does it behave?**" - next, start thinking about how your app behaves. Thinking about the features, and what happens when the user clicks and action
* "**What will my code look like?**" - with your behaviours and features in mind, start planning your code. What components will you need? will you need event handlers? state objects?
* "**What do I need to test? And what can go wrong?**" - think about the tests, edge cases and the parts of your code that could go wrong

## The not so good habits

Now let's look at some of not so good habits that are easy to pick up. If you do some of these now, don't panic. We all do at some point! With some practice you can overcome them - and I'll give you some pointers on how to do this.

## Blindly copying and pasting code

Put your hand up if you've ever encountered an issue or got stuck while coding? *_**raises hand*.**_ Obviously, we hit problems all the time whilst coding. It's part of the game and it's our job to figure out how to overcome these problems. 

Most of the time we resort to using Google, StackOverflow, or similar in search of answers to our problems. Now, there is nothing wrong with this approach - arguably, it should be encouraged as it's one the best/quickest way for a developer to solve a problem themselves.

The problem is, when we **copy/paste code blindly without understanding it.** 

> But if it works, what's the problem?!

A valid point. Here's the reasons why this can cause issues:

* What happens when the code has to be changed? It'll be difficult to change code we don't understand
* If we don't understand the code, how can we be sure it truly solves the problem?
* Can we be sure it doesn't affect other parts of the codebase in a negative way?

So, how can we avoid this?

* **Reading** - read through it line by line, and take the time to understand the code
* **Type -** type it out instead of copying and pasting. This will force you can read/analyse each line as you type

There is nothing wrong with copying and pasting, as long as we understand exactly what the code does. If a senior developer is code reviewing our work, and we can't explain what is happening because the code was copy/pasted, that won't look too good.

## Not writing tests

This is arguably the worst habit that can be picked up when learning to code. A lot of tutorials walk us through the "**happy path**" of creating an app, which makes it easy to neglect the test writing. Why are test's so important? 

* **Test's prove your code works**. Nobody can argue about functionality working if the test passes!
* **Makes it easy to check that new features haven't broken anything**. While coding, run your tests regularly. A few tests broken? **You know early in the development process where stuff went wrong.** As opposed to, finding out tomorrow when you come across it by accident
* **A seat belt for refactoring.** Write your code. Write your tests. Refactor your code. Run the tests. Tests pass? Everything still works, happy days! Now try changing your code without having a suite of tests to run. How can you prove **_everything_** works as it should?

So make sure to test your code. You don't have to test things like small side projects all the time, but it's good to practice now an again. When you get a job, you'll be aiming to have test coverage for most of your functionality and features. Practice those tests!

There are many great tutorials on how to test your code, depending on your current projects and tech stack, try Googling "testing with {insert language}" or "How to test {insert language} apps". [Heres a good overview of testing JavaScript](https://medium.com/welldone-software/an-overview-of-javascript-testing-in-2019-264e19514d0a).  


## Leaving out documentation

Documentation. The boring "red tape" that comes with all projects. As someone once said:

> All developers hate writing it, but all developers want it

Which is true. Have you ever returned to an old side project and forgotten what it did? How much harder would it be if you were trying to use a third party library and there was no documentation to explain how it worked? This becomes especially more apparent when working in a large product company. What if another team needs to integrate with your code, but is unsure of the API?

It's important stuff, so here's some tips to practice:

* README's - GitHub lets you add a readme to your project. This is the perfect place to store documentation for the project, as it's easy to find
* Include what the app does and how to run it - This gives the read a good place to start
* Explain other "important things" - such as complicated logic, third party libraries and API's, or configuration settings

---

### **Thanks for reading! Want more articles like this?**

Hopefully this has given you an insight into one creating good coding habits. If you'd like to be updated when I release more articles like this, feel free to join the mailing list over at [chrisblakely.dev](https://www.chrisblakely.dev/#sign-up)! Or reach me over at [Twitter](https://twitter.com/chrisblakely01) if you fancy a chat :)




