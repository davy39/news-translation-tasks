---
title: 7 Questions New Developers Ask When Learning How to Code
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2021-11-15T17:14:32.000Z'
originalURL: https://freecodecamp.org/news/questions-new-developers-ask-when-learning-how-to-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/7-questions-new-developers-ask.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: learning to code
  slug: learning-to-code
- name: programming languages
  slug: programming-languages
seo_title: null
seo_desc: 'If you''re relatively new to coding, you surely have some questions – how
  should you get started, what should you learn first, what does "front-end development"
  really mean...?

  In this article, I''ve shared 7 questions I had when I first started learni...'
---

If you're relatively new to coding, you surely have some questions – how should you get started, what should you learn first, what does "front-end development" really mean...?

In this article, I've shared 7 questions I had when I first started learning to code about 20 years ago (man, now I feel old). And I've answered them as thoroughly as possible to help you start your coding journey.

## What programming language should I learn first?

In my opinion, it doesn't really matter! There are certainly languages that are easier for beginners to pick up, such as Python, Ruby, or JavaScript. But most programming languages have a plethora of things in common, and the core concepts are usually fairly similar.

In most cases, the *syntax* (the keywords, structure, and semantics) of languages differ much more than the underlying concepts.

Once you know the basics of any programming language, it becomes a lot easier to pick up another one. It is also likely that the language you learn first won't be the central one you end up using at your job or side hustle.

For example, I started with Python back in the day, dabbled with JavaScript and PhP, but now use Java for my job and side hustle.

Of course, you probably don't want to start by learning some obscure and difficult language that isn't commonly used. But you really can't go wrong by starting with a popular modern language like Python, Java, Ruby, or JavaScript.

The most important part isn't what language you learn first, but that you *actually start* and incrementally improve your skills over time. In a nutshell, [focus on mastering essential coding concepts](https://initialcommit.com/store/coding-essentials-guidebook-for-developers) as opposed to the syntax of a specific language.

## How do we categorize programming languages?

Although most programming languages have a lot in common, there are many ways to organize languages into various categories.

These categories are used to group together languages with a particular feature or trait, although two languages with an overlapping trait might very well differ with respect to others.

Here are 5 of the most useful programming language categories for new devs to know about:

* Compiled programming languages
    
* Interpreted programming languages
    
* Statically-typed programming languages
    
* Dynamically-typed programming languages
    
* Object-oriented programming languages
    

Below, is a short description of each of these categories, along with a short list of languages in each one.

### Compiled programming languages

A compiled language is one that uses a **compiler** to convert source code (the code you write yourself) into a form the computer knows how to understand (often called **machine code**).

Usually, the output from the compiler is saved in one or more files called **executables**. Executables can be packaged for sale and distribution in standard formats that make it easy for users to download, install, and run the program.

An important characteristic of the compiling process is that the source code is compiled *before* the program is executed by the end user. In other words, code compilation typically takes place separately from program execution.

Popular compiled languages:

* C
    
* C++
    
* Java
    
* Rust
    
* Go
    

### Interpreted programming languages

An interpreted language is one that uses an **interpreter** to convert source code (the code you write yourself) into a form the computer knows how to understand.

An interpreter is a program that takes a set of source code written in a specific programming language, converts it into a form the computer can understand, and immediately executes it in real-time.

A primary difference between compiling and interpreting is that the interpreting process has no gap between code conversion and execution – both of these steps happen at program run time or on-the-fly. Whereas with compiling, the code conversion takes place in advance (sometimes far in advance) of program execution.

Popular interpreted languages:

* Python
    
* JavaScript
    
* Ruby
    

### Statically-typed programming languages

Static-typing means that the data types of the variables in a programming language are known and established at the time the program is compiled. Furthermore, the datatype of a variable is not allowed to change during program compilation or execution.

For example, each time you create a variable in a statically-typed language, you must explicitly specify the datatype of that variable. This datatype could be an integer, string, boolean, and so on. This is called variable **declaration**. Once you declare a variable’s data type, it can only hold that type of data throughout the execution of the program.

Popular statically-typed languages:

* C
    
* C++
    
* Java
    

### Dynamically-typed programming languages

Dynamic-typing means variable data types are established during program execution, also known as **runtime**.

Variable data types are not explicitly stated in the source code and variables can be easily reassigned to store values of any datatype on the fly.

Popular dynamically-typed languages:

* Python
    
* JavaScript
    
* Ruby
    

### Object-oriented programming languages

Object-oriented programming (OOP) is a coding paradigm that allows programmers to create and work with "objects". An object is a representation or model of something the programmer needs to describe via code.

This probably sounds super vague, because it is. Pretty much anything can be modeled as an "object" in code. Objects often represent real things, such as the products for sale in a store or the customers buying those products.

But objects can also represent digital things such as web forms, and even more abstract stuff like URL endpoints, network sockets, and so on.

Object-oriented programming is usually implemented in a language using **Classes**. You can think of a class as a template (or model) for the type of object that is being created.

A class contains a set of **attributes** (properties or characteristics) that define each object of the class. Classes also contain a set of **methods** (functions) that allow operations to be performed on specific objects of the class.

For example, a "Product" class might have the following attributes:

* Product SKU (unique identifier for each product)
    
* Product name (descriptive name for each product)
    
* Product type
    
* Product price
    
* Product discount
    

As mentioned, a class is really just a template for *creating objects*. Creating an object using a class as a template is known as **instantiation**. You can create as many objects as you want from the same class, and each object created is known as an **instance** of that class. The instance is usually stored as a variable in code that you can use as you need it by interacting with its attributes and methods.

Continuing with our example, you can use our "Product" class above to create multiple objects of type "Product". Each product would have its own set of attribute values, such as SKU, name, type, price, and discount.

Representing structured sets of data in this object-oriented fashion can be a very intuitive way for programmers to write and organize their code. This is likely because humans tend to be naturally good at thinking in terms of identifiable entities that exist in the real world.

## What's the difference between front-end, back-end, and full-stack development?

As a newer dev, you've likely browsed job opportunities in tech and noticed frequent mention of the terms "front-end", "back-end" and "full-stack".

These terms generally refer to the part of the application you'll be working on. Moreover, they also imply that you'll be working on a software application, usually a web application or mobile app.

The front end refers to the parts of the application that users (also known as "clients") interact with directly. For a web application, the front end is the collection of webpages (and functionality) that are presented in the user's browser. For a mobile app, the front end is the set of screens that the user interacts with on their mobile device.

Development tasks related to the front end include user experience design, user interface creation, client-side networking, integration and use of client-side libraries, and collecting/validating/submitting user input.

As a front-end dev, you'll implement these tasks primarily using HTML to define the structure of web pages, CSS to add styling, and JavaScript to add interactivity.

The back end refers to the parts of the application that run behind the scenes and aren't presented directly to the user/client.

The back end typically includes a web server which handles HTTP connections received from the front-end client (usually a web browser). The web server handles these connections and directs them to the back-end code which performs the logic necessary to respond to the client. This part of the back end is called **routing** or the **API (application programming interface)**.

The back-end code itself is traditionally a standalone monolith codebase that is deployed as a single unit. But depending on the application's architecture, the back-end code can operate as a set of **serverless** functions running on a cloud service as opposed to a standalone codebase.

The back-end code validates user input, applies business logic, interacts with data storage such as a database, and crafts a response that gets sent back to the front-end client.

Now that we've covered the front end and back end, full-stack development is easy! :) Full stack simply includes both the front end AND back end! The term "full stack" comes from the term "stack" which is a shortened form of "software stack". The software stack is the collection of tools, frameworks, programming languages, and operating systems that are used to support an application.

## What are some popular software stacks?

Now that we know what a software stack is, we'll briefly discuss some popular options for you to choose from.

### LAMP Stack (Linux, Apache, MySQL, PHP)

The LAMP stack is a time-tested and industry standard back-end stack that uses the Linux operating system as its foundation. On top of that, you use an Apache webserver to handle web requests and direct them to a PHP codebase. Data is stored in a MySQL database, which is a free and open-source (FOSS) relational database platform.

This stack is great for fairly standardized content-serving websites like blogs.

You might notice that I didn't explicitly mention any front-end tools as being a part of this stack – so this means that LAMP is a back-end stack.

### MEAN Stack (MongoDB, Express.js, Angular.js, Node.js)

The MEAN stack is a more modern stack that uses the MongoDB unstructured database platform for storing data. You use Express.js as the back-end web framework and Angular.js for the front end. Finally, you use Node.js to run JavaScript on the back end.

A major benefit of the MEAN stack is that all components are designed to natively operate using the JavaScript programming language, via JSON (JavaScript Object Notation).

Note that this stack's components are geared toward both the front end (Angular.js) and back end (MongoDB, Express.js, Node.js), so MEAN can be considered full stack.

### MERN Stack (MongoDB, Express.js, React.js, Node.js)

As you can probably see, the MERN stack is very similar to the MEAN stack except it uses React.js library as the front end instead of Angular.js.

This stack is well suited to devs who like React for its flexible and intuitive style of creating user interfaces.

### Notable frameworks

I wanted to take a brief moment to point out two other popular backend *frameworks* (not stacks) that you can incorporate or swap out for specific components of the stacks mentioned above.

**Spring Boot** is a Java framework (technically a special case of the broader Spring Framework) that is excellent for developing back-end Java code for web applications and mobile apps. If you are new to Java coding, I highly recommend you check it out.

**Django** is a Python framework that is specifically crafted for use with the Python programming language. If you prefer building web apps in Python, it is definitely worth looking into.

## How do devs collaborate on code without being in the same room?

When I started coding, I opened up a Python text editor on my local machine and created a single file which grew to contain all the code for my project. I quickly found that this became unruly, so I split my code up into several Python `.py` files (or modules as they are known).

When I coded with a friend, they would usually be sitting there behind me while I typed, or I would be sitting there behind them. If we needed to exchange code snippets or files, we would just send them back and forth via email.

It was years before I learned how devs successfully collaborate while coding, and that it is often done remotely.

The key to successful code collaboration is learning to use a **Version Control System (VCS)**. A VCS is a tool that tracks changes that multiple developers make to code files over time, and enables developers to efficiently work together on the same set files.

Version control systems create a **repository** that stores the data necessary to recreate any version of the code files as they existed at specific points in time. This is called **version control**.

Version control systems are very versatile tools, since they serve multiple useful functions for development teams:

* Tracks changes made to code files
    
* Allows devs to easily share their changes with others and access changes made by others
    
* Offers simple ways for merging code changes made by multiple devs or teams
    
* Provides a full-history backup of a project's code as it evolves over time, and a way to efficiently restore any previous version of the code
    
* Allows developers to easily manage code conflicts made on the same lines of the same files
    
* Provides various other tools to improve team collaboration and efficiency
    

[There are many version control systems out there](https://initialcommit.com/blog/Technical-Guide-VCS-Internals), but you've almost certainly heard of one: GitHub.

Actually, GitHub itself is *not* a version control system. GitHub is a company that provides online hosting for projects using version control. GitHub gets its name from the specific version control system that it uses: **Git**.

[The first version of Git](https://initialcommit.com/store/baby-git-guidebook-for-developers) was created in 2005, and it has evolved into by far the most well-known and most popular version control system on the planet. Git is used by the vast majority of development teams today, and it is an [essential tool to learn if you plan on coding professionally](https://initialcommit.com/store/coding-essentials-guidebook-for-developers).

## Does it matter what operating system I use?

When it comes to learning to code for the first time, I would answer this question similarly to the first in this list. I think what matters much more than which operating system you have, is that you get started learning as soon as possible with what you have.

That being said, I feel my answer would be a cop-out if I leave it at that. Let's assume you're trying to make an active decision about what OS to choose for coding work.

Taking into account the fact that there are many subjective reasons people prefer *their* operating system, in my opinion an operating system that provides access to a quality command-line terminal can be very useful to wrap your head around.

For that reason, my preference is using [Unix-like](https://en.wikipedia.org/wiki/Unix-like) operating systems such as a Linux flavor or MacOS if possible for development work. Full disclosure – I develop mostly on MacOS.

My reasoning for this is that learning to work on the command-line (much like learning to use Git) is an [essential coding skill to learn](https://www.freecodecamp.org/news/how-to-learn-programming/). A fully featured and intuitive command line is a core part of software development. In my opinion, Linux and MacOS better incorporate modern command lines than Windows.

## What text editor or IDE should I use?

Text editors and IDE's (Integrated Development Environments) have evolved massively over the years, and developers pick favorites for many reasons.

One reason could be that a particular editor or IDE was created specifically for a particular programming language or framework. Another could be that your company uses a specific editor, so that is the one you learned and stuck with. I found this reason to be especially true in my experience.

If you are primarily working with interpreted, dynamically-typed languages such as Python, JavaScript, Ruby, or PHP, I recommend that you start with a GUI-based editor such as Sublime Text or Visual Studio Code. These are two of the most popular text editors out there and provide a plethora of features and customizations to make your life easier as a developer.

If you work with Java, I recommend either Eclipse or IntelliJ IDEA which offer a multitude of features specifically crafted for working in the Java ecosystem.

Finally, regardless of which editor you choose for your main dev work, I recommend that you learn [a bit of Vim](https://initialcommit.com/blog/7-versatile-vim-commands). Vim is a text editor that is meant to be used directly within your command-line terminal. It definitely takes more time to get used to since you have to learn to use Vim's keyboard commands to interact with your files instead of point-and-click with your mouse.

But in my experience is well worth it. Even if you only learn the basic commands, these will help you immensely if you find yourself browsing through a non-GUI terminal at work, and need to inspect or modify some files.

I highly recommend the built-in Vimtutor program that is downloaded automatically when you install Vim. It walks through the basic directly in your command-line terminal.

## Summary

In this article, I discussed 7 questions commonly asked by new coders. We cast a fairly wide net, covering questions about programmings language selection, software dev stacks, operating systems, and text editors.

If there are any questions you have that I didn't cover, feel free to message me at [jacob@initialcommit.io](mailto:jacob@initialcommit.io).

## Next steps

If you got value out of this article, I wrote a book called [Coding Essentials Guidebook for Developers](https://initialcommit.com/store/coding-essentials-guidebook-for-developers) which has 14 chapters, each covering a core coding concept, language, or tool.

Topics include computer architecture, the Internet, Command Line, HTML, CSS, JavaScript, Python, Java, SQL, Git, and more.

These topics were meticulously selected to help put together a bigger picture of the development puzzle, instead of focusing on one topic in depth. This might be a good resource for you to check out if you got value out of this article.
