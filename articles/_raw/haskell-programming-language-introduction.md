---
title: Haskell Programming Language – How to Install and Use Haskell Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-04T19:57:55.000Z'
originalURL: https://freecodecamp.org/news/haskell-programming-language-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/haskell_freecodecamp.png
tags:
- name: Haskell
  slug: haskell
- name: programming languages
  slug: programming-languages
seo_title: null
seo_desc: 'By MacBobby Chibuzor

  What is Haskell? What is it used for? Why are there relatively few Haskell programmers?
  How can I get started with Haskell?

  If you''re asking yourself these questions, then this article is for you. In it,
  I''ll answer your question...'
---

By MacBobby Chibuzor

What is Haskell? What is it used for? Why are there relatively few Haskell programmers? How can I get started with Haskell?

If you're asking yourself these questions, then this article is for you. In it, I'll answer your questions about the Haskell programming language and demystify it for you.  

You will learn about the Haskell ecosystem and how to set it up for development. You will also learn the beauty of Haskell and where the language can be applied for real world problem solving.

Given the complexity of Haskell, you should know the basics of programming prior to diving into Haskell. It'll also help if you're very comfortable with another functional programming language to best understand Haskell syntax.

# What We'll Cover

* Haskell — A Proper Introduction
* Functional Programming
* Strongly Statically Typed Programming
* The Haskell Ecosystem
* How to Set Up Haskell Development Environment
* The Code Editor
* Hacking into the Beauty of Haskell
* The `ghci` Compiler
* Python vs Haskell – the Easiest vs the Hardest
* Major Use Cases for Haskell
* Web development: Backend with Spock, Frontend with Elm
* Cardano Blockchain Development with Plutus

# Haskell — A Proper Introduction

Haskell is a fully functional programming language that supports lazy evaluation and type classes. 

Haskell forces the developer to write very correct code, which is the quintessential nature of the language.

## Functional Programming

The world of computer programming allows different programming styles: functional, imperative, object-oriented. 

The functional programming style treats functions as the first-class citizens – the most important parts of a program. 

In functional programming languages, functions can be passed as values or data types. Functions can be passed as arguments to other functions, returned as results from functions, and assigned to variables. This promotes code reuse in a single codebase.

Haskell is a functional programming language and it supports these properties. Modern Java, C++, Go, and C# are all tethered to the functional style of programming.

## Strongly Statically Typed Language

Programming languages can either have a dynamic or static type system. In dynamic typing, values are tagged to data types during execution. This is common among languages like Python and JavaScript which allow implicit conversion between data types. 

In static typing, tagging is done during compilation and is common among low-level languages. In statically typed languages, programs are evaluated by the compiler before they are compiled into machine or bytecode and run.

Haskell is statically typed as its programs must be type checked before compilation and execution. Unlike Java and C#, the Haskell compiler only does type checking once, which boosts performance. 

Also, Haskell’s type system is called strong because of the error safety at compile time. As such, a common phrase among Haskell developers is, “Once it compiles, it works.”

# The Haskell Ecosystem

The most challenging aspect of starting out with a new language is configuring the development environment perfectly. 

To install and set up Haskell, you need to grab the entire Haskell ecosystem. The Haskell ecosystem contains:

* The compiler called Glasgow Haskell Compiler (GHC)
* The Interpreter called Glasgow Haskell Interpreter, (GHCi)
* The Stack tool for managing Haskell projects
* Other Haskell packages

You can get the one-for-all software package from [www.haskell.org/downloads#platform](http://www.haskell.org/downloads#platform). Haskell, like every other programming language widely adopted, has a database for its libraries, called [Hackage](http://hackage.haskell.org/).

## How to Set Up the Haskell Development Environment

### Linux Environment

If you use a Linux machine, it’s easier to run a shell command. The command below will install the Haskell platform on your machine.

```bash
$ sudo apt-get install haskell-platform

```

Next, type `ghc` on the Linux command line and hit **Enter**. This should prompt whether you install the GHCi interpreter or not. Type Y and hit `Enter`.  You should also install the Cabal build tool by running this chain of commands:

```bash
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:hvr/ghc
$ sudo apt install cabal-install

```

After installation, you should see the following output when you re-run `ghci` on the shell:

```bash
$ ghci
GHCi, version 8.8.4: <https://www.haskell.org/ghc/>  :? for help
Prelude>

```

Run a simple arithmetic to confirm that `ghci` works properly.

### Windows and Mac OS

The Haskell platform can be gotten from the official download page for both Windows and macOS. 

You can install the Cabal libraries tool on Windows from [here.](https://downloads.haskell.org/~cabal/cabal-install-3.6.2.0/cabal-install-3.6.2.0-x86_64-windows.zip) You can install it for macOS [here](https://downloads.haskell.org/~cabal/cabal-install-3.6.2.0/cabal-install-3.6.2.0-x86_64-darwin.tar.xz).

## The Code Editor

Haskell does not have a specially suitable code editor for writing its programs. You can write Haskell code in any of these Code Editors:

* [IntelliJ IDEA](https://www.jetbrains.com/idea/download/download-thanks.html?platform=linux&code=IIC) with the [Haskell Plugin](https://plugins.jetbrains.com/plugin/8258-intellij-haskell) installed
* Visual Studio Code with Haskell plugins installed
* Emacs in Haskell Mode
* Neovim

Alternatively, you can also write Haskell code on a “dumb” code editor like Notepad++ and Sublime Text and then compile with the GHC. 

What Haskell does is condition you to write codes in bits or modules, reiterating over it to make sure each module is correct and perfect for production. Thus, a smart or dumb code editor has minimal impact whatsoever on the finished code.

Feel free to check for extensions in the code editor marketplaces that will make writing Haskell source files a lot easier, like Haskero or [Haskell Runner for VSCode](https://github.com/Meowcolm024/has-go).

# Hacking into the Beauty of Haskell

The beauty of Haskell lies in:

* The logic
* The ease of reading Haskell code like mathematical expressions
* You can specify the probable output for a program and the language does the rest
* Its self-documenting nature
* The magnificent GHCi compiler
* The concept of purity

## The `ghci` Compiler

Unlike other programming languages, the `ghci` compiler allows you to interactively use the compiler.

Also, multi-line coding which isn’t allowed in other compilers is allowed in `ghci`. For example, if you want to write a full script in Python IDLE, you would have to write it step by step, with each line being complete. But Haskell’s compiler makes it possible to do multi-line coding like this:

```haskell
$ ghci
GHCi, version 8.8.4: <https://www.haskell.org/ghc/>  :? for help
Prelude> :{
Prelude| 60 +
Prelude| 30
Prelude| :}
90
Prelude>

```

## Python vs Haskel – the Easiest vs the Hardest

Haskell is considered a very hard language to learn and master. On the other hand, Python is considered the easiest and most useful programming language to use.

Given that a lot of programmers are comfortable with Python programming, it is logical to explain Haskell in terms of Python:

1. Haskell is a functional language, as mentioned before, while Python is a mixture of procedural, object-oriented, and functional programming styles. Haskell has procedural programming support, but the side-effects in the language do not make it easy.
2. Python and Haskell have a strong type system, which means explicit conversions have to be done. However, while Python is dynamically typed, Haskell is statically typed.
3. Python is a lot slower than Haskell.
4. As mentioned earlier, Python is easier than Haskell to learn. The learning curve for Haskell is steep, especially for those with no prior functional programming experience.
5. In terms of library support, Python has more libraries and use-cases than Haskell.

# Major Use Cases for Haskell

The major uses of the Haskell language today include Web Development and Cardano Blockchain Development.

## Haskell for Web Development

You can use Haskell for web development. Just as Python has Flask and Django, Go has Gin, Echo, and Bevel, Haskell has Scotty, Servant, and Yesod all built on top of Wai.

Wai is the Haskell package for managing HTTP requests/responses. Among the three popular Haskell frameworks, Yesod is more of a complete web framework than the others.

Haskell also has the `blaze-html` package used to build HTML files, similar to `gohtml`.

## **Haskell for Cardano Blockchain Development**

Cardano is a new blockchain platform that adopts the Proof-of-Stake consensus algorithm. It is the first to allow peer-review research and it was created to address the downsides of Bitcoin and Ethereum.

The Cardano cryptocurrency, ADA, is a popular coin in Japan, and they have ADA ATMs installed in Tokyo. 

The Cardano blockchain system is written in Plutus, a Haskell-based, Turing-complete programming language. 

Plutus makes use of several tools to build smart contracts on the Cardano blockchain. It has the Plutus Application Backend which provides the environment and tools used to interact with smart contracts. Plutus also provides a fee estimator for in-house cost calculations.

You can preview and run Plutus code on the [Plutus Playground](https://playground.plutus.iohkdev.io/).

Since Haskell is a high assurance language built for users in the financial industry, it tackles the problem of transaction exchanged failures due to bad code, and multi-sig failures that enable hackers to steal digital money.

# Final Words

Thank you for reading this introduction to Haskell and its ecosystem and main uses. I hope you are inspired to start learning more about it.

In my future articles, you will be able to learn the basics of Haskell programming, as well as more about its main use cases.

