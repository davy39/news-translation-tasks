---
title: How to Use SonarLint to Write Cleaner Code
subtitle: ''
author: Okosa Leonard
co_authors: []
series: null
date: '2024-01-18T23:58:39.000Z'
originalURL: https://freecodecamp.org/news/use-sonarlint-to-write-cleaner-code
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/slint.jpg
tags:
- name: clean code
  slug: clean-code
- name: Visual Studio Code
  slug: vscode
- name: workflow
  slug: workflow
seo_title: null
seo_desc: 'When you''re building a coding project, the better it is, the more fun
  it''ll be to use. And the prouder you''ll be of your hard work, right?

  Also, writing quality and performant code helps your program or website work as
  expected – which should be ever...'
---

When you're building a coding project, the better it is, the more fun it'll be to use. And the prouder you'll be of your hard work, right?

Also, writing quality and performant code helps your program or website work as expected – which should be every developer's goal.

[SonarLint](https://docs.sonarsource.com/sonarcloud/improving/sonarlint/) is a tool that helps you make sure your code is top-notch. It's like having a friendly guide who checks your code to see if it's well-written and doesn't have mistakes.

## What is SonarLint?

SonarLint is an open-source code analysis tool that helps you find and resolve security and code quality problems in your source code as you're writing it. This plugin works with several integrated development environments (IDEs), including well-known ones like IntelliJ IDEA, Eclipse, and Visual Studio.

SonarLint's main purpose is to give you immediate feedback on possible problems with your code, including security flaws, bugs, and other recommended practices for programming. SonarLint analyzes code in the background while you create or change it in your IDE, giving you instant feedback and frequently exposing problems right in the code editor.

SonarLint is a component of the larger SonarQube ecosystem.

In this article, I'll teach you how to use SonarLint to help you write quality code.

## Why is SonarLint Useful?

Let's imagine that building a website is like constructing a house. You want your house to be safe and well-designed, right? Well, SonarLint is like having a thorough inspector who checks your work as you build, making sure everything is just right.

Here's why SonarLint is important in web development:

1. **Catch Mistakes Early (Code Quality):** Assuming you were building a staircase, and accidentally put a step in the wrong place, SonarLint is like a smart friend who tells you immediately, "Hey, you might have made a mistake here!" It helps catch small errors in your code before they become big problems.
    
2. **Follow the Blueprint (Coding Standards):** When building a house, you follow a blueprint to make sure everything fits together. In coding, there are also rules (like a blueprint) on how to write good code. SonarLint helps you stick to these rules, making your code easy to read and work with.
    
3. **Keep It Secure (Security):** Just like you'd want your house to have good locks on the doors, you'd want your website to be secure. SonarLint checks your code for potential security issues, ensuring there are no "unlocked doors" that could let bad things happen.
    
4. **Work Together Well (Collaboration):** Imagine that each builder in your team used a different kind of tool. It would be chaos! SonarLint helps your team work together smoothly by making sure everyone follows the same coding standards. This way, everyone can understand and contribute to the project easily.
    
5. **Save Time and Effort (Efficiency):** Fixing mistakes after the whole house is built would take a lot of time and effort. SonarLint helps you fix issues as you go, saving you from returning and redoing things. It's like having a helpful friend who stops you from making mistakes in the first place.
    
6. **Learn and Improve (Education):** SonarLint does not only point out mistakes but also explains why they might be a problem. It's like having a coding teacher who helps you understand how to write better code. This way, you learn and become a better developer over time.
    

So, in the world of web development, SonarLint is your coding buddy, and it makes sure your JavaScript "house" is strong, secure, and well-organized from the ground up. It's a valuable tool in your workflow and helps you create high-quality websites that everyone can enjoy.

But you still may be wondering why you need this tool. You have a debugger already installed in your IDE and it can already track the errors in your environment.

Well, integrating SonarLint complements your debugger by focusing on code quality and security during development.

While a debugger helps to find and fix runtime issues, SonarLint analyzes code in real time, identifies bugs and potential vulnerabilities, and enforces coding standards.

You can also customize and configure coding rules based on your project's specific requirements and coding standards.

This proactive approach enhances overall code quality and ensures cleaner, more maintainable code before it reaches the debugging stage. This leads to fewer errors and smoother development workflows.

Before we get into the details of how to set up and use SonarLint, let's look at what makes code high-quality.

## Code Quality Metrics

Be the best cookbook author! When writing code there are specific guidelines you must follow.

Just like when you're cooking up a new recipe or want to follow a traditional one, you should make sure anyone who reads it can follow along, and that the recipe you wrote down results in a good dish.

In the same sense, when writing code, it's always important to make your code readable so that other developers can understand it easily and so your code works as it's supposed to. Code quality metrics are like measuring how well you followed the recipe.

Here's a breakdown:

**Readability (Clarity):** This is similar to making sure your recipe instructions are clear. The code should be easy for others (or future you) to understand.

**Maintainability (Ease of Changes):** If you had to change ingredients in your recipe (code), it should be easy to switch things without chaos.

**Performance (Speed):** As you'd want your meal ready quickly, efficient code is expected to run fast. Code quality metrics check how fast your code is executed.

**Reliability (Consistency):** A good recipe always tastes the same. Similarly, reliable code consistently produces the correct results.

**Security (Safety):** Just like checking if ingredients are safe to eat, code quality metrics look for potential dangers in your code that could be exploited.

These should be your goals when writing quality code. And SonarLint can help you accomplish them.

## How to Set Up SonarLint and Integrate with Your IDE

An IDE (Integrated Development Environment) is a software application that helps developers write and debug code more effectively. IDEs include a code editor and compiler or interpreter.

In this article, you'll see how to install SonarLint using VS Code extensions.

### How to Install SonarLint with VS Code

First, install VS Code or open the application if you've already installed it.

Next, head over to the Extensions tab on VS Code and download the SonarLint extension.

To use the SonarLint extension for JavaScript, TypeScript, or CSS, you should have a minimum version of `14.17.0` of Node.js installed on your system (especially if you want to use [Connected Mode](https://docs.sonarsource.com/sonarlint/vs-code/team-features/connected-mode/) with Sonar Cloud).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonar.png align="left")

*Install SonarLint in VS Code*

Now that you've installed SonarLint, running an analysis on your code should be easy and it should start immediately after you open a new file.

This means SonarLint will start working and catching errors in your code as you write them on your IDE. Now let's look at an example in the next section.

### How to Use SonarLint in Your IDE

Now let's look at how you can get the best out of SonarLint on your IDE. SonarLint is also a wonderful teacher, helping you better understand how to write clean code and giving you more information about why you have an error.

So instead of scouring the web to figure out what's wrong with your code, SonarLint explains why it has given you an error.

Here's an example of how to use it.

To be able to see the interface where we'll be working, open your terminal on VS Code – you can use Ctrl + backtick (\`) to do this. I'm currently working on a project in React.js, and I didn't notice that I have duplicate border property names in my CSS class. Luckily, SonarLint caught this issue.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonarlint.png align="left")

*A CSS error caught by SonarLint*

If you click on the light bulb, you'll see an option to fix the code by deactivating the CSS rule or to be blunt removing the extra border which I have in my CSS class in this instance. There's also another option for opening a description rule so you can understand why you're getting that error.

So SonarLint gives you two options:

1. It offers an option that gives you the ability and resources to understand why you have that error with the "Open description of rule".
    
2. It offers a solution to the error of the code which it has found.
    

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonarlint-another.png align="left")

*Options offered by SonarLint to help fix and understand this problem*

If you click on the open description rule, SonarLint opens another tab in VS Code to help you understand why it has thrown that error and how you can write cleaner/better code.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/sonarlint-teacher.png align="left")

*Tab opened by SonarLint in VSCode to help understand the error*

As you can see, SonarLint is an excellent teacher and your best buddy as you continue to build and work on your IDE.

Another great thing about SonarLint is that it works with multiple programming languages. So whatever programming language you're using, chances are that SonarLint can handle it.

## Conclusion

SonarLint is like having a coding buddy that helps you become a better programmer. As you write code, it's like having a teacher right there with you, pointing out ways to improve.

Imagine having a super-smart friend who does not just spot mistakes but also explains why they're wrong and shows you how to fix them.

Before your code gets to the testing stage, SonarLint checks for mistakes and makes sure your program runs smoothly. It's like having a superpower to catch issues early, saving you time and effort.

But that's not all! SonarLint is also like a security guard for your code. It watches out for any potential weak points that could let bad things happen. By learning from SonarLint, you can write better code and become more aware of keeping your code safe and secure.
