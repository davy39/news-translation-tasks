---
title: What is PHP? How to Write Your First PHP Program
subtitle: ''
author: Michael Para
co_authors: []
series: null
date: '2022-08-03T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-php-write-your-first-php-program
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Untitled-2-1.jpg
tags:
- name: PHP
  slug: php
seo_title: null
seo_desc: 'In this article, you will learn what the PHP programming language is and
  how to write your first program with it.

  History of PHP

  PHP is the most used and popular scripting language generated for web development.
  You can embed it in HTML documents.

  PH...'
---

In this article, you will learn what the PHP programming language is and how to write your first program with it.

## History of PHP

PHP is the most used and popular scripting language generated for web development. You can embed it in HTML documents.

PHP is written in the high-level C programming language. The first generation of PHP was PHP/FI created in 1994 by Rasmus Lerdorf. He wrote it to track visitors to his resume.

The thing that allowed him to easily create the first home page with PHP was the ability to embed the PHP code within HTML markup.

The second generation was released as PHP/FI Version 2 in 1995 which referred to Personal Home Page Tools. At this time PHP depended on a small parser engine to translate and understand a few special instructions and some utilities that were used on the PHP personal home page.

PHP was officially born and become more widely used in 1996. In the beginning, it was being used on more than 15,000 web applications around the world. That number increased to 50,000 the following year.

Currently, PHP is fully dependent on an advanced interpreter called the Zend Engine. To learn more about [what PHP is and how to write an advanced PHP program](https://codedtag.com/php/what-is-php-write-a-program/) you should read more about its syntax.

As I mentioned before, PHP depends on the Zend Engine interpreter. But the question is, what is an interpreter? And how it does work?

In the next section, I'll explain everything from scratch – from the source code to the PHP server response. But before that you have to know the difference between the interpreter and the compiler.

Let's dive right in.

## What's the Difference Between an Interpreter and a Compiler?

The interpreter is a program that takes the source code line by line and translates it into binary bits (0s and 1s) – machine language. During this process, the developer can edit the source code.

It doesn't take long for the interpreter to analyze the code – such as deleting the comments from the source code, whitespaces, and so on. But the overall time for execution is a bit slower.

On the other hand, the compiler is a program that takes the full source code that's already written in a high-level programming language and translates it into binary or machine language.

During this process, you can't edit the source code because it goes in as one piece to the compiler. The compiler is slow to analyze code but translates very quickly.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/WhatsApp-Image-2022-07-27-at-2.34.06-PM.jpeg align="left")

Let's take a more in-depth look at the PHP interpreter to see how it works.

## How Does the PHP Interpreter Work?

As I mentioned before, the PHP interpreter is called the Zend Engine and it has four phases during which it interprets the PHP source code – in this section, we are going to dive more into each phase.

### Lexical Analysis

The PHP interpreter takes the source code from the server and starts the first phase called lexical analysis (or tokenization). In this process, the interpreter removes all whitespaces and comment syntax, searches for any errors in the source code, and then generates a token sequence.

The lexical analysis does not cause any errors during this stage because it is only responsible for producing a token sequence. But it throws a fatal parse error to stop this phase directly if it finds any error in the source code.

### The Parser

In the following step the parser takes over. In this phase, the parser receives the token sequence and sets some of the instructions to create the Zend Engine VM (Virtual Machine) – which is similar to assembly language – to manipulate the token sequence that was already created with the previous stage.

### The Compilation

This phase is already under the parser stage, and here the parser is starting the compilation by generating the AST (Abstract Syntax Tree) – then passing it to the code generator.

The output of the compilation is an intermediate code that already depends on the Zend Engine VM. This is known as Operation Codes (OPCodes). The Opcodes contain some of the instructions to perform all the operations which require the implementation of flow control.

### The Execution

This is the last phase, and here the executor receives the intermediate code that was already generated by the previous stage. It can read these OPCodes from the array of the instructions and then execute them one by one.

Overall, the Zend Engine has two separated functions, compiling and executing, which are zend\_compile and zend\_execute.

In the next section, you are going to write your first PHP program! But before you do that, [you have to install a Wamp (for Windows) or XAMPP (for Linux/MacOS) server](https://www.freecodecamp.org/news/how-to-get-started-with-php/) depending on which operating system you use.

## How to Install XAMPP

In this section, I'll explain the XAMPP server and how to run the PHP server on your local machine.

Firstly, XAMPP is a free software used to create a PHP web server. But What does XAMPP mean?

1. "X" refers to **Operating Systems** such as Windows, Linux, or macOS. So that means we can install the XAMPP server on one of the operating systems we mentioned in this line.
    
2. "A" refers to **Apache**, and that is the PHP webserver software.
    
3. "M" refers to **MariaDB - MySQL**, the database management systems.
    
4. "P" refers to **PHP** (Personal Home Page) – the server-side scripting language that helps us create dynamic web pages.
    
5. "P" refers to **Perl** which is used in web development, network programming, or system administration.
    

So XAMPP refers to all the packages that you need to do web application development.

To install the XAMPP server on your local machine, navigate to the [XAMPP official page](https://www.apachefriends.org/) and download the installer according to your operating system.

Once you've download it, just install the program according to the instructions you read in the installer.

The final result should look like the below image:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-2.png align="left")

*The XAMPP Control Panel*

You only have to click on the "start" button beside the Apache module to run the PHP server.

Let's explore the important folders inside the XAMPP server app.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-3.png align="left")

*XAMPP Important Folders*

The above image shows you all the important folders, but we only need to focus on the "**htdocs**" folder. This folder is the public directory that contains all PHP projects.

So you'll put any new PHP project inside the "**htdocs**" folder. And to open the result on the web browser, you just need to navigate to "**localhost/your\_project\_folder\_name**".

Let's write a PHP program to clarify that.

## How to Write Your First PHP Program

To help you write your first PHP program, we're just going to print a small message – "Hello World".

Firstly, make sure your PHP server is running on your local machine – I am using the XAMPP server on my local machine.

Second, create a folder inside your server app directory and name it [codedtag](http://codedtag.com/).

The below image shows you that my public folder in the XAMPP server app is (**htdocs**) on Windows.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-273.png align="left")

*The public folder of the XAMPP server*

For the next step, create an index page that ends with a PHP extension. Inside the "codedtag" folder, copy-paste the following PHP code:

```php
<?php 
   echo "Hello World";
?>
```

To run the script, open the browser and navigate to **localhost/codedtag**. You will see the print message like the below image:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-274.png align="left")

*The PHP Print Message*

And that's it! You've printed your first PHP program.

## Wrapping Up

In this article, we discussed what PHP is and summarized its history in a few lines. We also learned the difference between the compiler and the interpreter.

Also, we discussed the exact steps of how the PHP interpreter works. To summarize, let’s have a look at the PHP Zend Engine from the top.

1. The first step is lexical analysis. In this stage, the interpreter deletes all whitespaces and comments from the source code and generates a token sequence.
    
2. The next step is called the parser, and here the parser sets the instructions to create the Zend Engine VM to manipulate the token sequence.
    
3. The compilation stage creates and passes the AST (Abstract Syntax Tree) to the code generator and the final compilation output is OPCodes.
    
4. The following step is for the executor, and in this stage the executor is reading and executing the instructions from the array.
    

If you want to learn more about PHP, here's a [full handbook that covers all the basics in depth](https://www.freecodecamp.org/news/the-php-handbook/).

Stay tuned for my next article. You can read more of my articles on [FlatCoding](https://flatcoding.com/).
