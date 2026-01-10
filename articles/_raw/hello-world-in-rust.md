---
title: Hello World in Rust – Example Program
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-04-08T09:21:17.000Z'
originalURL: https://freecodecamp.org/news/hello-world-in-rust
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Neon-Green-Motivational.png
tags:
- name: beginner
  slug: beginner
- name: Rust
  slug: rust
seo_title: null
seo_desc: 'Starting with a new programming language is like taking your first step
  into a whole new world. One of the very first things you''ll do is write a simple
  program that says "Hello World!".

  Rust, known for being fast and safe, is no exception. Let''s jum...'
---

Starting with a new programming language is like taking your first step into a whole new world. One of the very first things you'll do is write a simple program that says "Hello World!".

Rust, known for being fast and safe, is no exception. Let's jump right in and create our very first Rust program together!

## How to Write a Hello World Program in Rust

First, create a file named `main.rs`. Every Rust program contains `.rs` as its file extension.

Then write the following code in the file:

```rust
// main.rs
fn main() {
	println!("Hello World!");
}

```

In the code above, we are trying to print `Hello World!` in the console or terminal.

## How to Compile Rust Code

In Rust, compiling and running the code are two separate processes.

First, you need to compile the Rust program. To compile it, write the following in the terminal (make sure in the terminal is at at the same directory where the Rust file lives):

```bash
rustc main.rs

```

For now, you won't see any output because the code was just compiled. But one thing you can see in the current directory is that a new executable file has been added with the same name as the Rust file.

## How to Run the Executable File

Now you can run the executable file that gets generated after you successfully compiled the Rust code.

To run the executable file, write the following in your terminal:

```bash
./main

```

You should see an output like this:

```bash
Hello World!

```

## Understanding the Hello World Code in Depth

```rust
fn main() {

}

```

The program starts with a function called `main()`. Every Rust executable code starts execution from the main function. 

The main function can have some parameters inside the `()` parenthesis, but we have no need for them in the code so we left that empty.

Everything that is between the curly braces `{}` is the body of the function. It is necessary to have braces for the body otherwise it'll throw an error.

```rust
fn main() {
  println!("Hello World!");
}

```

This line does the work of printing the "Hello World!" text to the terminal or console.

Here, `println!` is not a function unlike other languages like C, Python, and so on. It is a macro – if there's an `!` symbol at the end of a keyword, then it's a macro.

Finally, we passed the string as argument to the macro and it prints the string to the terminal.

To end the statement in Rust, you must use `;`.If you don't provide the semi-colon at the end of every statement, then it'll throw an error.

## Conclusion

And there we have it – your first Rust program! By printing out "Hello World!" you've dipped your toes into the world of Rust. 

This simple program has given you a taste of Rust's syntax and how it compiles. As you keep going, you'll discover more about Rust's cool features and find out just how powerful it can be. 

Ready to dive deeper? Let's keep exploring!

If you have any feedback, then feel free to DM me on [Twitter](https://twitter.com/introvertedbot) and [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/)

