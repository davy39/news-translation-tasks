---
title: How to Learn Programming – The Guide I Wish I Had When I Started Learning to
  Code
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2021-10-06T15:17:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-programming
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/The-Programming-Guide-I-Wish-I-Had-When-I-Started-1.png
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: learn to code
  slug: learn-to-code
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'Just the thought of learning to code can be very intimidating. The word
  code is mysterious by definition. It implies a technical form of communication that
  computers, and not humans, are meant to understand.

  One way many people start learning to code...'
---

Just the thought of learning to code can be very intimidating. The word **code** is mysterious by definition. It implies a technical form of communication that computers, and not humans, are meant to understand.

One way many people start learning to code is by picking a popular programming language and jumping in head first with no direction. This could take the form of an online coding course, a tutorial project, or a random book purchase on a specific topic.

Rarely do prospective developers start with a roadmap – a bird's eye view of the coding world that outlines a set of relevant programming concepts, languages, and tools that almost 100% of developers use every day.

In this article, I propose one such roadmap. I do this by outlining 14 steps – each one discussing an essential concept, language, or tool – that professional developers use to write code, collaborate, and create professional projects.

I meticulously chose these 14 steps based on my own personal journey learning to code, which spans almost 20 years.

Part of the reason it took me so long to feel comfortable as a developer is that I would learn about specific topics without a broader context of the coding world.

Each of the steps in this article discusses a "coding essential" – something that I believe **is critical to at least know that it exists** at the start of your coding journey.

One final note before listing the steps in the roadmap: of course reading this article will not make you an expert programmer. It isn't meant to. The purpose of this article is to make you aware that each one of these topics exists, and hopefully give you a basic idea of how each one works so you can build on it intelligently going forward.

## 14 Step Roadmap for Beginner Developers

1. [Familiarize Yourself with Computer Architecture and Data Basics](#heading-1-familiarize-yourself-with-computer-architecture-and-data-basics)
    
2. [Learn How Programming Languages Work](#heading-2-learn-how-programming-languages-work)
    
3. [Understand How the Internet Works](#heading-3-understand-how-the-internet-works)
    
4. [Practice Some Command-Line Basics](#heading-4-practice-some-command-line-basics)
    
5. [Build Up Your Text Editor Skills with Vim](#heading-5-build-up-your-text-editor-skills-with-vim)
    
6. [Take-up Some HTML](#heading-6-take-up-some-html)
    
7. [Tackle Some CSS](#heading-7-tackle-some-css)
    
8. [Start Programming with JavaScript](#heading-8-start-programming-with-javascript)
    
9. [Continue Programming with Python](#heading-9-continue-programming-with-python)
    
10. [Further Your Knowledge with Java](#heading-10-further-your-knowledge-with-java)
    
11. [Track Your Code using Git](#heading-11-track-your-code-using-git)
    
12. [Store Data Using Databases and SQL](#heading-12-store-data-using-databases-and-sql)
    
13. [Read About Web Frameworks and MVC](#heading-13-read-about-web-frameworks-and-mvc)
    
14. [Play with Package Managers](#heading-14-play-with-package-managers)
    

Without further ado, let's start at the top!

## 1) Familiarize Yourself with Computer Architecture and Data Basics

One of the wonderful things about modern programming languages is that they enable us to create fancy applications without worrying about the nitty-gritty details of the hardware behind the scenes (for the most part).

This is called **abstraction** – the ability to work with higher-level tools (in this case programming languages) that simplify and narrow down the required scope of our understanding and skills.

However, that doesn't mean it's useless to know the basics of the metal that your code is executing on. At the very least, being aware of a few tidbits will help you navigate workplace conversations about high CPU and memory usage.

So, here is a bare minimum of computer architecture basics to get you started:

Your computer's most important parts live on **microchips** (also known as **integrated circuits**).

Microchips rely on an electrical component called a **transistor** to function. Transistors are tiny electrical switches that are either off (0) or on (1) at any given time. A single microchip can contain millions or billions of tiny transistors embedded on it.

Most modern computers have a microchip called the **Central Processing Unit (CPU)**. You can think of it as the computer’s brain. It handles most of the number crunching and logical tasks that the computer performs.

Each CPU has something called an **instruction set**, which is a collection of binary (zeros and ones) commands that the CPU understands. Luckily, we don't really need to worry about these as software devs! That is the power of abstraction.

If the CPU is the logical center of the brain, it is useful to have memory as well to store information temporarily or for the long term.

Computers have **Random Access Memory (RAM)** as "working memory" (or short-term memory) to store information that is actively being used by running programs.

RAM is made up of a collection of **memory addresses**, which can be used to store bits of data. In older languages like C, programmers do have access to working directly with memory addresses using a feature called **pointers**, but this is rare in more modern languages.

Finally, we'll touch on a component you're surely familiar with – the hard drive. In our analogy of the brain, this represents long-term memory. A hard drive is an internal or external device that stores data that should persist even after the computer is turned off.

Before moving on to more details about programming languages, let's spend a second talking about data. But what exactly do we mean by the word **data**?

At a high level, we think of things like text documents, images, videos, emails, files, and folders. These are all high-level data structures that we create and save on our computers every day.

But underneath the hood, a computer chip (like a CPU or RAM chip) has no idea what an "image" or a "video" is.

From a chip’s perspective, all of these structures are stored as long sequences of ones and zeros. These ones and zeros are called **bits**.

Bits are commonly stored in a set of eight at a time, known as a **byte**. A byte is simply a sequence of eight bits, such as `00000001`, `01100110`, or `00001111`. Representing information in this way is called a **binary representation**.

## 2) Learn How Programming Languages Work

In the previous section, we mentioned that most computers rely on a CPU, and a CPU can understand a specific set of instructions in the form of ones and zeros.

Therefore, we could theoretically write code that tells the CPU what to do by stringing together long sequences of ones and zeros in a form the CPU understands. Instructions written in binary form like this are called **machine code**.

Sounds horrible to work with, doesn't it? Well it probably is, but I wouldn't know since I mostly use higher-level programming languages like JavaScript, Python, and Java.

A **higher-level programming language** provides a set of human-readable keywords, statements, and syntax rules that are much simpler for people to learn, debug, and work with.

Programming languages provide a means of bridging the gap between the way our human brains understand the world and the way computer brains (CPUs) understand the world.

Ultimately, the code that we write needs to be translated into the binary instructions (machine code) that the CPU understands.

Depending on the language you choose, we say that your code is either **compiled** or **interpreted** into machine code capable of being executed by your CPU. Most programming languages include a program called a **compiler** or an **interpreter** which performs this translation step.

Just to give a few examples – JavaScript and Python are interpreted languages while Java is a compiled language. Whether a language is compiled or interpreted (or some combination of the two) has implications for developer convenience, error handling, performance, and other areas, but we won't get into those details here.

## 3) Understand How the Internet Works

Whatever type of programming you aspire to do, you'll run into situations where it helps to know how computers interact with each other. This typically occurs over the Internet.

The Internet is nothing more than a global collection of connected computers. In other words, it is a global network. Each computer in the network agrees on a set of rules that enable them to talk to each other. To a computer, "talking" means transferring data.

As we discussed in the previous section, all types of data – web pages, images, videos, emails, and so on – can all be represented as ones and zeros.

Therefore, you can think of the Internet as a very large set of computers that can transfer ones and zeros amongst themselves, in a way that preserves the meaning of that data. The Internet is nothing more than a digital conversation medium.

If the Internet is just a big conversation arena, let’s define the conversation participants.

First, an analogy: most human conversations require at least two participants. In most cases, one person initiates the conversation and the other person responds, assuming they are both present and available.

In Internet speak, the computer initiating the conversation is called the **client**. The computer responding or answering is called the **server**.

For example, let’s say you open a web browser and go to "www.google.com". In this scenario, your web browser is the client. By extension, you can also think of the computer you are working on as the client.

In a more abstract sense, YOU are the client because you are the one initiating the conversation. By typing "www.google.com" into the search bar and clicking , your browser is requesting to start a conversation with one of Google’s computers.

Google’s computer is called the server. It responds by sending the data required to display Google’s web page in your browser. And voilà! Google’s web page appears in front of your eyes. All Internet data transfers utilize this sort of client/server relationship.

## 4) Practice Some Command-Line Basics

The **Command Line** can be intimidating at first glance. It is often featured in movies as a cryptic black screen with incomprehensible text, numbers, and symbols scrolling by. It is usually associated with an evil hacker or genius techie sidekick.

The truth is that it doesn’t take a genius to use or understand the command line. In fact, it allows us to perform many of the same tasks that we are comfortable doing via a point-and-click mouse.

The main difference is that it primarily accepts input via the keyboard, which can speed up inputs significantly once you get the hang of it.

You can use the Command Line to browse through folders, list a folder’s contents, create new folders, copy and move files, delete files, execute programs, and much more. The window in which you can type commands on the Command Line is called a **terminal**.

Let's walk through a short tutorial of basic navigation commands that will give you a feel for working on the command line.

Once you open your terminal, a typical first question is "*Where am I"?* We can use the `pwd` command (which stands for "Print Working Directory") to figure that out. It outputs our current location in the file system which tells us which folder we are currently in.

Try it yourself:

### How to Use the Command Line

If you’re on a Mac, open the Terminal app, which is essentially a Unix Command Line terminal.

If you’re running an operating system without a GUI (Graphical User Interface), like Linux or Unix, you should be at the Command Line by default when you start the computer. If your flavor of Linux or Unix does have a GUI, you’ll need to open the terminal manually.

At the prompt, type `pwd` and press &lt;ENTER&gt;. The Command Line will print out the path to the folder that you’re currently in.

By default, the active folder when opening the Command Line is the logged-in user’s home directory. This is customizable in case you want the convenience of starting in a different location.

For convenience, the home directory can be referenced using the tilde `~` character. We will use this in a few examples going forward.

Now that we know what folder we’re in, we can use the `ls` command to list the contents of the current directory. The `ls` command stands for "List".

Type `ls` and press &lt;ENTER&gt;. The contents (files and subfolders) that reside in the current directory are printed to the screen.

Rerun the previous command like this `ls -al` and press &lt;ENTER&gt;. Now we will get more details about the directory contents, including file sizes, modification dates, and file permissions.

The hyphen in the previous command allows us to set certain flags that modify the behavior of the command. In this case we added the -a flag which will list all directory contents (including hidden files) as well as the -l flag which displays the extra file details.

Next, we can create a new folder using the `mkdir` command, which stands for "Make Directory". Below we create a new folder called "testdir".

Type `mkdir testdir` and press &lt;ENTER&gt;. Then type `ls` and press &lt;ENTER&gt;. You should see your new directory in the list.

To create multiple nested directories at once, use the `-p` flag to create a whole chain of directories like this: `mkdir -p directory1/directory2/directory3`

The Command Line isn’t that useful if we can only stay in one location, so let’s learn how to browse through different directories in the file system. We can do this via the `cd` command, which stands for "Change Directory".

First, type `cd testdir` and press &lt;ENTER&gt;. Then type `pwd` and press &lt;ENTER&gt;. Note the output now shows that we are inside the "testdir" directory specified in the cd command. We browsed into it!

Type `cd ..` and press &lt;ENTER&gt;. The `..` tells the Command Line to browse backwards to the parent directory.

Then type `pwd` and press &lt;ENTER&gt;. Note the output now shows that you are back in the original directory. We browsed backwards!

Next we’ll learn how to create a new empty file in the current directory.

Type `touch newfile1.txt` and press &lt;ENTER&gt;. You can use the `ls` command to see that the new file was created in the current directory.

Now we’ll copy that file from one folder to another using the cp command.

Type `cp newfile1.txt testdir` and press &lt;ENTER&gt;. Now use the `ls` and `ls testdir` commands to see that the new file still exists in the current directory and was copied to the "testdir" directory.

We can also move files instead of copying using the `mv` command.

Type `touch newfile2.txt` and press &lt;ENTER&gt; to create a new file. Next, type `mv newfile2.txt testdir` and press &lt;ENTER&gt; to move the file into the "testdir" folder.

Use the `ls` and `ls testdir` commands to confirm that the file has been moved into the "testdir" folder (it should no longer appear in the original location you created it, since it was *moved* not copied).

The `mv` command can also be used to rename files.

To do that, type `touch newfile3.txt` and press &lt;ENTER&gt; to create a new file. Then type `mv newfile3.txt cheese.txt` and press &lt;ENTER&gt; to update the file’s name. Use `ls` to confirm that the filed was renamed.

Finally, we can delete files and folders using the `rm` command.

Type `rm cheese.txt` and press &lt;ENTER&gt; to remove the file. Use `ls` to confirm the file was removed.

Type `rm -rf testdir` and press &lt;ENTER&gt; to remove the "testdir" directory and its contents. Use `ls` to confirm the directory was removed.

Note that we need to use the `-rf` flags when removing directories. This forces the removal of the folder and all of its contents.

## 5) Build Up Your Text Editor Skills with Vim

At this point, we’ve covered the basics of the Command Line and seen a few examples of how we can work with files without a mouse.

Although we now know how to create, copy, move, rename, and delete files from the Command Line, we haven’t seen how we edit the content of text files in the terminal.

Working with text files in the terminal is important because computer code is nothing more than text saved in an organized set of files.

Sure we could use a fancy text editor like Microsoft Word (or more likely specialized code editors like Sublime or Atom) to write and edit our code, but this is not required. The terminal is often the most convenient place to write and edit code since we usually already have it open to run commands!

There are several excellent text editors created specifically for this purpose, and I recommend [learning the basics of one called Vim](https://www.freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor/).

Vim is one of the oldest text editors around and it is a time-tested gem. Vim stands for "***VI*** i\*\**M*\*\*proved" since it is the successor to a tool called ***Vi***.

As mentioned, Vim is a text editor that was built to run directly in the terminal, so we don’t need to open a separate window to work in or use a mouse at all. Vim has a set of commands and modes that allow us to conveniently create and edit text content using only the keyboard.

Vim [does have bit of a learning curve](https://www.freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae/), but with a little bit of practice, the skills you learn will pay dividends throughout your coding career.

Vim is installed by default on many operating systems. To check if it’s installed on your computer, open the Command Line and type `vim -v`.

If Vim opens in your terminal and shows the version, you’re good to go! If not, you’ll need to install it on your system. (Note that you can quit Vim by typing `:q!` and pressing ). For more information on installing Vim, see https://www.vim.org.

In my opinion, the quickest and easiest way to learn how to use Vim is to use their built-in tutorial, the **VimTutor**. To run it, ensure that Vim is installed on your system, open the Command Line, type `vimtutor`, and press .

It is such a good tutorial that there is no reason for me to waste time trying to explain it here. So go do the VimTutor, like now! See you in the next section.

If you still have energy left after you've completed the VimTutor, check out [these 7 Vim commands that will dramatically improve your productivity](https://initialcommit.com/blog/7-versatile-vim-commands) as you get started with Vim.

## 6) Take-up Some HTML

You can think of HTML – short for **H**yper**T**ext **M**arkup **L**anguage – as the bones of a web page. It determines the structure of the page by specifying the elements that should be displayed and the order that they should be displayed in.

Every web page that you’ve ever visited in your browser has some HTML associated with it. When you visit a web page, the web server hosting the web page sends over some HTML to your browser. Your browser then reads it and displays it for you.

Most web pages contain a fairly standard set of content, including a title, text content, links to images, navigation links, headers and footers, and more. All of this information is stored as HTML that defines the structure of the page.

One thing to keep in mind is that HTML is not technically a programming language, although it is often referred to as "HTML code".

As we’ll see later, other programming languages enable us to write code that **does stuff**, such as running a set of instructions in sequence. HTML doesn’t **do** anything. We don’t run or execute HTML. HTML just sits there in a file and waits to be sent to a web browser which will display it to the end-user.

In fact, HTML is basically just data. It is data that defines what a web page should look like, nothing more.

So how do you write HTML? HTML uses a standard set of **tags** (basically just labels) to identify the available elements that make up a web page. Each tag is defined using angle brackets.

For example, the **title** tag is defined as `<title>My Page Title</title>` and the **paragraph** tag is defined as `<p>A bunch of random text content.</p>`.

Each HTML element is made up of a starting tag and an ending tag. The starting tag is just the tag label in between angle brackets, like this:

`<tagname>`

This opens the new HTML tag. The ending tag is essentially the same, but it uses a forward slash after the first angle bracket, to mark it as an ending tag:

`</tagname>`

Any text between the two tags is the actual content that the page will display.

Let’s cover a couple of the most common tags in use. The first is the `<html>` tag. This defines the start of an HTML page. A corresponding `</html>` tag (note the forward slash) defines the end of the HTML page. Any content between these tags will be a part of the page.

The second is the `<head>` tag. This defines additional information that the browser will use to understand the page. Most of the content in this tag is not displayed to the user. A corresponding `</head>` tag defines the end of the HEAD section.

Previously, we saw the `<title>` tag. It defines the title of the web page, which the browser will display in the browser tab. This tag needs to be placed inside the `<head>...</head>` section.

Next is the `<body>` tag. All content inside this tag makes up the main content of the web page. Putting these four tags together looks something like this:

```html
<html>
    
    <head>
        <title>My Page Title</title>
    </head>
        
    <body>
        <p>A bunch of random text content.</p>
    </body>

</html>
```

The simple HTML snippet above represents a simple web page with a title and a single paragraph as body content.

This example brings up a point we didn’t mention in the last section. HTML tags can be nested inside each other. This just means that HTML tags can be placed inside other HTML tags.

HTML provides many other tags to provide a rich set of content to web users. We won't cover them in detail here, but below is a short list for reference:

* `<p>`: A paragraph of text starting on a new line.
    
* `<h1>`: A page heading usually used for page titles.
    
* `<h2>`: A section heading usually used for section titles.
    
* `<hx>`: Where *x* is a number between 3 and 6, for smaller headings.
    
* `<img>`: An image.
    
* `<a>`: A link.
    
* `<form>`: A form containing fields or inputs for a user to fill out and submit.
    
* `<input>`: An input field for users to enter information, usually within a form.
    
* `<div>`: A content division, used to group together several other elements for spacing purposes.
    
* `<span>`: Another grouping element, but used to wrap text phrases within another element, usually to apply specific formatting to only a specific part of the text content.
    

## 7) Tackle Some CSS

A web page without CSS – or **C**ascading **S**tyle **S**heets – is like a cake without frosting. A frosting-less cake serves its purpose, but it doesn’t look appetizing!

CSS allows us to associate style properties such as background color, font size, width, height, and more with our HTML elements.

Each style property tells the browser to render the desired effect on the screen. Like HTML, CSS is not technically a programming language. It doesn’t let us perform actions, it simply lets us add styles to bare bones HTML.

Let’s see how to associate CSS styles with our HTML elements. There are three pieces to this puzzle:

**The CSS selector:** Used to identify the HTML element or elements we want the style to apply to.

**The CSS property name:** The name of the specific style property that we want to add to the matched HTML elements.

**The CSS property value:** The value of the style property we want to apply.

Here is an example of how these pieces come together to set the color and font size of a paragraph:

```css
p {
  color: red;
  font-size: 12px;
}
```

Let’s start at the beginning, before the curly braces. This is where the CSS selector goes. In this case, it is the letter **p** which indicates the `<p>` (paragraph) HTML tag. This means that the styles inside the curly braces will apply to all `<p>` tags on the web page.

Let’s move on to what goes inside the curly braces – the styles we want to apply to the targeted elements.

Here we find pairs of CSS properties and values, separated by a colon. The properties (in this case "color" and "font-size") are on the left. The values of these properties (in this case "red" "12px") are on the right. A semicolon ends each property/value pair.

You can probably see how this works. The snippets of CSS code above tell the browser to use red, 12px size letters for all the text placed inside `<p>` tags.

So how does an HTML page know to include these CSS styles? Enter the `<link>` HTML tag. Usually, CSS styles are created in separate files (**.css** files) from the HTML. This means we need some way to import them into our HTML files so the browser knows that the styles exist.

The `<link>` element exists for this purpose. We include `<link>` elements in the `<head>` section of HTML files which allow us to specify the external CSS files to import:

```css
<head>

    <title>My Page Title</title>

    <link rel="stylesheet" type="text/css" href="/home/style.css">

</head>
```

In this example, we are importing the CSS styles specified by the **href** attribute, in this case the file */home/style.css*.

In the next 3 sections, we'll (finally) dive into some more technical programming languages!

We'll go over a general overview of JavaScript, Python, and Java, as well as walk through some of the essential coding concepts common to the 3 languages. We will compare and contrast the language features and example code so you can hopefully get a well-rounded understanding of the basics of all three.

## 8) Start Programming with JavaScript

Let’s start by answering the following question: if we can use HTML to build the structure of a web page and CSS to make it look pretty, why do we need JavaScript?

The answer is that we technically don’t. If we are happy with a static site that sits there and looks pretty, we are good to go with just HTML and CSS.

The keyword here is "static". If, however, we want to add dynamic features to our web pages, such as changing content and more complex user interactions, we need to use JavaScript.

### What is JavaScript?

So what exactly is JavaScript? JavaScript is a programming language that was created specifically for websites and the Internet. As we mentioned in section 2, most programming languages are either compiled or interpreted, and programs are typically run in a standalone manner.

JavaScript is somewhat unique in this respect in that it was designed to be executed directly inside web browsers. It allows us to write code representing sets of actions that will be executed on our web pages to make our sites much more dynamic.

You can either write JavaScript code in text files named with a `.js` extension or inside `<script>` tags directly in the HTML.

For many years, JavaScript code was primarily relegated to running inside web browsers. But the **Node.js** project changed this paradigm by creating a standalone JavaScript environment that could run anywhere.

Instead of being trapped in a browser (that is, client-side), Node.js can be installed locally on any computer to allow the development and execution of JavaScript code. You can also install Node on web servers which allows you to use JavaScript as backend code for applications instead of simply as web browser frontend code.

Now that we've covered some background, let's dive into a few basics of the JavaScript language.

### Variables and Assignment in JavaScript

Variables possibly represent the most fundamental concept in programming. A variable is simply a name or placeholder that is used to reference a particular value.

The word **variable** implies that the stored value can change throughout the execution of the program.

You can use variables to store numbers, strings of text characters, lists, and other data structures that we will talk more about in a minute.

All programming languages use variables, but the syntax varies between different languages.

Variables are useful since we can reference their values throughout our code. This enables us to check their values as needed and perform different actions depending on how the variable’s value changes.

In JavaScript, we declare variables using the `let` keyword, like this: `let x;`.

This declares x as a variable that we can use in our code. Note that we added a semicolon at the end of the line. In JavaScript (and many other languages) semicolons are used to specify the end of each code statement.

Now that we have created the variable *x*, we can assign a value to it using the equals sign, also called the **assignment operator**: `x = 10;`

Here we assigned the number 10 to the variable named *x*. Now any time we use *x* in our code, the value 10 will be substituted in.

Both variable declaration and assignment can be done in one line as follows:

```javascript
let x = 10;
```

### Data Types in JavaScript

In the last section, we stored an integer (whole number) value in the variable named *x*. You can also store decimal numbers, or **floating-point numbers** as they are known. For example, we could write: `let x = 6.6;`.

The different types of values we can store in variables are called **data types**. So far we have only seen numeric data types (integers and floating-point numbers), but we are just scratching the surface. We can store text data in variables as well.

In coding terminology, a piece of text is called a **string**. We can store a string value in our variable x by surrounding it in either single or double quotes:

```javascript
let x = 'Hello there!';

let y = "Hey bud!";
```

The next data type we’ll discuss is the **boolean**. A boolean can only hold one of two values, `true` or `false` – and they must be all lowercase. In JavaScript, true and false are two keywords used specifically as values for boolean variables:

```javascript
let x = true;

let y = false;
```

Note that the values `true` and `false` don’t appear within quotes the way strings do. If we surround them with quotes, the values would be strings, not booleans.

We often use booleans to control the flow of programs in conditional (if/else) statements which we’ll learn about next.

### Program Flow Control Statements in JavaScript

Now that we have an understanding of variables and the basic JavaScript data types, let’s take a look at some things we can do with them.

Variables aren't that useful without being able to tell our code to do something with them. We can make our variables do things by using **statements**.

Statements are special keywords that allow us to perform some action in our code, often based on the value of a variable we have defined. Statements let us define the logical flow of our programs, as well as perform many useful actions that will dictate how our programs work.

#### If / Else Statement

The first statement we’ll discuss is the `if` statement. The `if` statement allows us to perform some action only when a desired condition is true. Here is how it works:

```javascript
let x = 10;

if ( x > 5 ) {
    console.log('X is GREATER than 5!');
} else {
    console.log('X is NOT GREATER than 5!');
}
```

We defined a variable called *x* and set its value to 10. Then comes our `if` statement. After the keyword `if`, we have a set of parentheses containing the condition to evaluate, in this case, `x > 5`. We just defined *x* to equal 10, so we know that this condition is true in this example.

Since the condition in the parentheses is true, the code between the curly braces will be executed, and we will see the string "X is GREATER than 5!" printed to the screen. (We didn't discuss the meaning of `console.log()`, so for now just know that it prints the value in the parentheses to the screen).

In the same example, we also included an `else` statement. This allows us to execute specific code in the event that the condition in the condition is `false`.

#### While Loops

The next type of statement we’ll discuss is the **while loop**. Loops enable us to repeat a block of code as many times as we desire, without copying and pasting the code over and over again.

For example, let’s assume we need to print a sentence to the screen 5 times. We could do it like this:

```javascript
console.log('This is a very important message!');
console.log('This is a very important message!');
console.log('This is a very important message!');
console.log('This is a very important message!');
console.log('This is a very important message!');
```

This works fine for only 5 messages, but what about 100, or 1000? We need a better way to repeat pieces of code multiple times, and loops allow us to do this. In coding terminology, repeating a piece of code multiple times is called **iteration.**

This following `while` loop will continue running the block of code inside it as long as the specified condition remains true:

```javascript
let x = 1;

while ( x <= 100 ) {
    
    console.log('This is a very important message!');
    
    x = x + 1;
    
}
```

In this example, we initialize *x* to the value of 1. Then we write a `while` loop. Similar to the `if` statement, we add a condition in parentheses. In this case the condition is `x <= 100`. This condition will be `true` as long as *x* is less than or equal to 100.

Next we specify the block of code to execute in the curly braces. First, we print out our message to the console. Then we increment *x* by 1.

At this point the loop attempts to re-evaluate the condition to see if it’s still `true`. Variable *x* now has a value of 2 since it was incremented in the first loop run. The condition is still `true` since 2 is less than 100.

The code in the loop repeats until *x* gets incremented to the value of 101. At this point, *x* is greater than 100 so the condition is now `false`, and the code in the loop stops executing.

### The HTML
