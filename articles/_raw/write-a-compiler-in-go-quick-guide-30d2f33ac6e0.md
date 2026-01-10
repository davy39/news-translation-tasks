---
title: 'How to write a compiler in Go: a quick guide'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T14:54:04.000Z'
originalURL: https://freecodecamp.org/news/write-a-compiler-in-go-quick-guide-30d2f33ac6e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xwPzWlZJoBbgrtEvwslRdg.jpeg
tags:
- name: compilers
  slug: compilers
- name: golang
  slug: golang
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Joseph Livni

  Compilers are awesome! ? ? ? They combine theory and application and touch on a
  lot of software related topics such as parsing and language construction. At their
  core, compilers are a program that make a program readable by the compu...'
---

By Joseph Livni

Compilers are awesome! ? ? ? They combine theory and application and touch on a lot of software related topics such as parsing and language construction. At their core, compilers are a program that make a program readable by the computer.

The inspiration for this came out of a compilers course I took this past Fall and my love for Go.

This is the guide I wish I had when starting my journey into compilers. There are a lot of books, videos, and tutorials on how to create compilers. The goal of this post is to strike a balance between providing a nontrivial example of some of the things a compiler can do while avoid getting stuck in the weeds. ?

The result will be a compiler that can execute a small made up language.To checkout and run the final project see the instructions below. ?

**Note:** Remember that Go is strict about absolute paths when running this

```
cd $GOPATH/src/github.com/Lebonescogit clone https://github.com/Lebonesco/go-compiler.gitcd go-compilergo test -vgo run main.go ./examples/math.bx
```

#### Outline of the Compiler

* **Lexer/Parser**
* **AST Generator**
* **Type Checker**
* **Code Generation**

#### The Language

The goal of this post is to get you familiar with compilers as quickly as a possible so we’ll keep the language simple. For **Types** we’ll work with `strings`, `integers`, and `bools`. It will have **Statements** that include `func`, `if`, `else`, `let`, and `return`. This should be enough to have fun working with some of the complexities of a compiler.

The first compiler that I built, I completed over the course of two months and took up **1000’s of lines** of code. I took some shortcuts in this post in order to show you the key fundamentals.

Two common components that our language is missing are `classes` and `arrays`. These add additional complications we don’t have time for right now. If it turns out that people really want to know how to handle these elements I’ll write a followup.

Some example code:

```
func add(a Int, b int) Int {    return a + b;}
```

```
func hello(name String) String {    return "hello:" + " " + name;}
```

```
let num = add(1, 2);let phrase = string hello("Jeff");let i = int 0;let result = "";
```

```
if (i == 2) {    result = hello("cat");} else {    result = hello("dog");}
```

```
PRINT(result);
```

#### Quick Setup

The only outside package we need is `**gocc**`**,** which will help build the lexer and parser.

To get it run:

```
go get github.com/goccmack/gocc
```

Make sure the bin folder where gocc is located is in your `**PATH**` **:**

```
export PATH=$GOPATH/bin:$PATH
```

**Note:** If you’re having problems at this stage try running `go env` to make sure that your `$GOROOT` and `$GOPATH` are correctly assigned.

Cool, let’s dive into some code.

#### Building the Lexer

The lexer’s job is to read the program and output a stream of tokens that are consumed by the parser. Each `Token` contains the `type` that the token represents in the language and the string `Literal` of that token.

To identify the pieces of the program we will be using regular expressions. gocc will then convert these regular expressions into a **DFA** (_Deterministic Finite Automata_) which can theoretically run in linear time.

The notation that we’ll be using is **BNF** (_Backus–Naur form_). Don’t confuse this with **EBNF** (_extended Backus–Naur form_) or **ABNF** (_augmented Backus–Naur form_) which have some added features. Keep this in mind when looking at other examples online that could be using other forms which provide more syntactic sugar.

Let’s start with the basics and define what `strings` and `integers` will look like.

Note that:

* All token names must be lower case
* Any key preceded by ‘!’ will be ignored
* Any key preceded by ‘_’ will not by turned into a token
* Any expression enclosed by ‘{‘ `expression` ‘}’ can be repeated 0 or more times

In the below example we are ignoring all white space and have defined an `int` and `string_literal` `token`.

Every language has built in `keywords` that are reserved words that deliver special functionality. But, how will the lexer know whether a `string` is a `keyword` or a user created `identifier`? It handles this be giving preference to the order in which tokens are defined. Therefore, let’s define `keywords` next.

We’ll finish this up by adding the punctuation necessary for expressions.

Cool! Let’s see if this is actually doing what we want with some **unit tests**. Feel free to just paste this part into your IDE. ?

**Note:** It’s generally good practice in Go to place test files in the relevant subdirectory, but for simplicity I’m placing all tests in the root.

To test our **scanner** run:

```
$ gocc grammer.bnf$ go test -v=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/compiler       0.364s
```

Great, we now have a working `**Lexer**` ?

#### Building the Parser

Building the `**Parser**` is similar to how we built the `**Lexer**`. We will construct a set of element sequences that when correctly match a stream of tokens produce a grammar. This will also run in linear time by internally converting our **NFA** (_Non-Deterministic Automaton_) grammar to **DFA** (_Deterministic Finite Automaton_).

Let’s keep things simple. What actually is our program? Well, it’s a bunch of `Statements` in which each `Statement` can contain a set of `Statements` and/or `Expressions`. This seems like a good place to start our grammar.

Below is the beginning recursive hierarchy of the program. `Statements` is a sequence of zero or more `Statements` and `Functions` is a list of functions. Our languages requires functions to be defined before other `Statement` types. This will reduce some headache during the type checking phase. `empty` is a keyword in **BNF** that represents an empty space.

But wait! What is a `Statement`? It’s a unit of code that doesn’t return a value. This includes: `if`, `let`, and `return` statements. This is opposed to `Expressions` which do return values. We will get to those next.

Below is our grammar for `Statement` and `Function`. A `StatementBlock` is a larger abstraction that encapsulates a list of `Statements` with braces `{` `}`.

Next lets build out our `Expression` which handles all infix operations such as `+`, `-`, `*`, `&`lt`;`, `&g`t;`, =`=, and`,` and or.

Almost done with a fully working grammar! Let’s wrap things up by defining our parameter insertion. Each `function` can accept any amount of values. When **defining a function** we need to label the argument types in the signature while a **called function** can accept any amount of `Expressions`.

Now that our parser is completed let’s add some code to our driver, `main.go`.

As we progress through the compiler we will add more functionality to this driver.

One of the things challenging about building a parser is that there’re many different ways to define the grammar. ?

We won’t really know how well we did until we get into the next section which uses the output we just generated. The difficulty of building the static type checker will be strongly influenced by our grammar design. Keep your fingers crossed ?.

#### Test Parser

We’ll keep this simple because at this point our parser can still produce false positives. Once we start working on the AST we can check its accuracy.

```
go test -v=== RUN   TestParser--- PASS: TestParser (0.00s)=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/go-compiler        7.295s
```

Congrats ? ? ?! You now have a fully working Lexer and Parser. Time to move onto the AST **(A**bs_tract Syntax Tree)._ 

### Abstract Syntax Tree

The best way to understand an abstract syntax tree is in relation to a parse tree which is what we generated in the last post. A parse tree represents each part of the program that is matched in our grammar.

> By contrast, an AST only contains the information related to type checking and code generation, and skips any other extra content that is used while parsing the text.

Don’t worry if that definition doesn’t makes sense right now. I always learn best by actually coding, so let’s jump into it!

Create a new directory and two new files. `ast.go` will contain our AST generating functions and `types.go` will have the _tree node types_.

```
mkdir astcd asttouch ast.gotouch types.go
```

Like with the parse tree, we will define our structure from top to bottom. Every `node` will either be a `Statement` or `Expression`. Go isn’t object oriented so we’ll use a composition pattern utilizing `interface` and `struct` to represent our `node` categories. Our AST will return a `Program` node that contains the rest of the program. From now on, any struct we created with a `TokenLiteral()` method is a `node`. If that `node` has a `statementNode()` method it will fit the `Statement` interface and if it has a `expressionNode()` method it’s an `Expression`.

In addition, we’ll be adding `json` tags to each struct field to make it easier when we convert our AST into `json` for testing purposes.

Now let’s start building our `Statement` structs based off of the `Statement` and `Node` interfaces.

**_Note:_** `json:"-"` means that the field will be omitted from our json.

Next we need some hooks to connect our `nodes` and `parser`. The code below allows our `Statement` nodes to fit the `Node` and `Statement` interfaces.

We then need the hooks that will be called by the parser.

As you can see, **most of our code** is checking and casting our input type.

These hooks will then be called by the parser in `grammar.bnf`. To access these functions we’ll need to `import "github.com/Lebonesco/go-compiler/ast`.

Now when a piece of grammar is identified, it calls an AST hook and passes in the necessary data to construct a `node`.

As you could imagine, there is a lot of flexibility in how you want to generate your AST. There are **design strategies** that reduce the amount of unique nodes in the AST . However, having more node types will make your life easier when we get to the `typechecker` and `code generation`. ?

This part has a lot of code. However, it’s not very difficult and mostly all the same. The error handling in Go can feel a bit tedious, but in the long run it’ll be worth it when we make a silly mistake. Safety First ?

We’re not going to do anything too crazy with our error handling because I want to save on lines of code. However, if you feel so inclined you can add more descriptive and useful errors.

Let’s move on to `Expressions`!

Fit them into the `Node` and `Expression` interfaces.

And create the `Expression` hooks.

Finally, insert the hooks into the `parser`.

#### Test AST Generator

The test cases for the AST generator are the most tedious to write. But trust me, this is not a part you want to mess up on. If you have problems here, those bugs will rollover into your `type checker` and `code generator`. ?

In my opinion, if code doesn’t have tests it’s broken

In our AST test we will construct what our final result should look like. To avoid comparing elements such as `tokens`, that could create false negatives, we convert our result and expected output into json before comparing with a **deep comparison** function, `reflect.DeepEqual()`.

Run Test:

```
go test -v=== RUN   TestAST--- PASS: TestAST (0.00s)=== RUN   TestParser--- PASS: TestParser (0.00s)=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/go-compiler        9.020s
```

Half way to a working compiler! ? While you give this post some ? ? ? don’t forget to give yourself a hand for making it this far.

Let’s add some more code to the driver.

Now onto my favorite part, the **Type Checker**.

### Type Checker

Our type checker will make sure that users don’t write code that conflicts with our **statically typed** language.

The core backbone of our **type checker** will be a combination of data structures that track identifier types, initialization, and valid type operations. This can get vastly more complicated once we start dealing with different levels of scope and classes. However, we’re keeping it as simple as possible. ?

To start:

```
touch checker_test.gomkdir checkercd checkertouch checker.gotouch environment.go
```

`environment.go` will contain all of our helper functions that will be used by our **checker** and **code generator** to access and manipulate our set of variables and corresponding types. Our environment is simple so this will be straight forward.

We’ll begin by setting all of our constant values including **operation types**, **variable types**, and **mapping of each type to its valid methods**.

**Note:** If we had classes in our language our checker would handle this third part rather than us doing it by hand.

The rest of `environment.go` are basic **getters** and **setters** that handle identifiers and functions.

The foundation of our type checker will be a single **dispatch** function, `checker()`, that takes in a `Node` and fires the corresponding checker function

I felt like saving lines of code so we’ll be using a global environment to store our variable types.

**Note:** This wouldn’t be possible if we allowed `Block Statements` and `Functions` to have their own scope or if we were abiding by best practices.

Now eval `Statements`. `Block Statements` are the only statement in which we return a type in order to handle the case when it is inside a function. If there is a `Return Statement` inside the `Block Statement` its type is returned. Otherwise, the `Nothing_Type` is returned.

Onto evaluating `Expressions`. The most complicated part will be `evalFunctionCall()` because it could either be a built in function such as `PRINT()` or user defined.

**Note:** Currently, there is only one **builtin** function. However, more could be easily added given the framework that we’ve built.

Awesome! Let’s add a small snippet to our driver.

#### Test Type Checker

```
go test -v=== RUN   TestAST--- PASS: TestAST (0.00s)=== RUN   TestOperations--- PASS: TestOperations (0.00s)=== RUN   TestIdents--- PASS: TestIdents (0.00s)=== RUN   TestFunctions--- PASS: TestFunctions (0.00s)=== RUN   TestParser--- PASS: TestParser (0.00s)=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/go-compiler        9.020s
```

I made some deliberate choices to leave things out of this language such as `classes`, `for loops`, and function `scope`. Most of the complexities that arise from these occur in the `checker` and `code generator`. If I added those elements this post would be a lot lot longer. ?

### Code Generation

We have finally made it to the last stage! ? ? ?

In order to handle the most cases with the least amount of hassle every `expression` will be assigned to a temporary variable. It might make our generated code look bloated, but it will solve for any nested expressions.

Bloated code won’t have any impact on final program speed because the optimizer will remove any redundancy when we compile our final generated C++ code.

Our generator will look similar to the type checker. The main difference is that we’ll be passing down a `buffer` to store the generated code.

While I chose to compile into C++, you can substitute in any language . The main purpose of this **Go Compiler Guide** was to enable you to be able to understand the pieces well enough to go out and create your own.

To start:

```
touch gen_test.gomkdir gencd gentouch gen.go
```

We’ll begin by importing all of the necessary packages and defining three **utility functions,** `write()` to write generated code to a buffer, `check()`to do error handling, and `freshTemp()`to generate **unique** variable names for temporary variables we create on the fly.

**Note:** It’s generally bad practice to use `panic()`for normal error handling in Go, but I’m tired of writing `if statements`.

Similar to the **checker**, our **generator** has a core dispatch function that accepts a `Node` and calls the corresponding **gen** function.

Let’s generate some `Statements`. `genProgram()` generates necessary headers and `main()` function.

Generating `Expressions` will look very similar to the code above. The main difference is that a `temp` variable is returned representing that expression. This helps us handle more complex `Expression` nesting.

The final piece of code will be our C++ **Builtin types.** Without this nothing will work.

#### Test Code Generator

### Bringing It All Together

We’re now going to combine our **lexer**, **parser**, **AST generator**, **type checker**, and **code generator** into a final runnable program, `main.go`.

**Note:** I’m running this on a Windows so my C++ compiles into `main.exe`. If this doesn’t work for you remove the `.exe` extension.

To find some test programs to run go to `github.com/Lebonesco/go-compiler/examples`.

```
go run main.go ./example/function.bxhello Jeff3
```

And there you have it! We have completed a fully working compiler in Go!

Thank you for taking the time to read this article.

If you found it helpful or interesting please let me know ???.

