---
title: Rust for Beginners – Get Started with the Most Loved Programming Language
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-18T22:09:21.000Z'
originalURL: https://freecodecamp.org/news/rust-getting-started-with-the-most-loved-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/rust-2.jpg
tags:
- name: programming languages
  slug: programming-languages
- name: Rust
  slug: rust
seo_title: null
seo_desc: 'Rust has been voted Stack Overflow’s most loved programming language for
  five years in a row. This article will tell you why Rust is awesome.

  Rust is a systems programming language that you can use to write applications with
  high performance. Rust is...'
---

Rust has been voted Stack Overflow’s most loved programming language for five years in a row. This article will tell you why Rust is awesome.

Rust is a [systems programming language](https://www.techopedia.com/definition/9616/system-programming) that you can use to write applications with high performance. Rust is used by some of the top tech companies like Dropbox and Cloudflare to deliver speed and concurrency to their customers.

For the last five years in a row, Rust has been voted as the most loved programming language. 

But chances are, you might not have worked with Rust. Or worse, you might not have heard of it before. So let's learn more about it.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-5.png)
_StackOverflow 2020 Survey_

## Why Rust?

Let’s look at why a developer would choose Rust.

Typical programming languages like Python and C++ abstract a lot of details away from developers. 

If you are a junior developer working on a simple web application, this might not an issue. You just want to find a solution to a problem.

For large scale applications that millions of users will use on a daily basis, the ‘problem-solving’ approach will not work. More users consume more system resources. And more resources mean bigger bills for your company.

This is where Rust shines. Rust combines ease of programming with access to core system configurations. Rust is built with memory-safety, concurrency, and security from the ground up.

> Rust is a “systems programming language that focuses on speed, memory safety, and parallelism”.

Rust is also considered to be a great alternative for C++. Rust offers high performance in addition to helping you [eliminate common bugs caused by languages like C++.](https://polyfloyd.net/post/how-rust-helps-you-prevent-bugs/)

Now that you know what Rust can do for you, let's look at Rust in detail.

##  Origins

Rust is an open-source programming language. It was first introduced to the world in 2010 by Graydon Hoare, while he was working at Mozilla. Shortly after, Mozilla began sponsoring this project and is still a core contributor to Rust.

Rust started gaining popularity over the years. Even Microsoft uses Rust to build secure and safety-critical software components.

##  Core Features

Let's look at some core features that make Rust stand out from other programming languages.

### Performance

Rust was built to be high performance form the ground up. Rust offers fine-grained control of memory management and has a minimal standard library.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/performance.png)
_Source: Figma_

If you look at some of the [metrics shared by Figma](https://www.figma.com/blog/rust-in-production-at-figma/), they had incredible improvements in performance once they switched to Rust.

Rust’s low memory footprint also makes it an ideal choice for embedded systems programming. You can use Rust to write software for IoT devices like home automation hubs, smart security systems, and so on.

### Security

One of the major reasons Microsoft decided to root for Rust is its security. 

The majority of vulnerabilities in Microsoft software were due to poor memory management in C & C++. This lead to simple yet powerful exploits like the [Buffer Overflow exploit](https://www.imperva.com/learn/application-security/buffer-overflow) that had crippled Windows for years.

So Microsoft decided to look for the best alternative to C++. And they found Rust.

Using Rust eliminates an entire class of security vulnerabilities from software applications. This helps companies build applications with better performance and higher security.

### Concurrency

Concurrency is when two or more tasks start, run, and complete in overlapping time. Database operations are a great example to explain concurrency.

When thousands of users are using your application at the same time to perform different actions, your database handles them concurrently. Concurrency is a key concept when it comes to scaling applications.

Concurrency and parallelism are also built into Rust. Rust solves most of the concurrency problems during compile time by using the concept of Ownerships. [Learn how Rust handles concurrency here](https://doc.rust-lang.org/book/ch16-00-concurrency.html).

## Working With Rust

Now that you understand the core features of Rust, let's write a few lines of code. You can [find installation instructions here](https://www.rust-lang.org/tools/install) if you want to try out Rust on your computer.

Let's start with a simple “Hello World!” function.

```rust
// Main function
fn main() {
	println!("Hello World!");
}
```

Yep. That's pretty much it. Let's try to add two numbers.

```rust
// Main function
fn main() {
	let a = 100;
    let b = 200;
    println!("Result is {}",a+b);
}
```

Again, pretty standard. Now let's look at an array operation.

```rust
// Main function
fn main(){
	let arr:[i32;4] = [1,2,3,4];
    println!("array size is {}",arr.len());
}
```

If you look at line 3, we use “:[i32;4]”. Here we tell Rust that we are declaring an array of length 4 with 32-bit integers.

Declaring data types in detail is a key factor in improving the performance of a program. You are helping the compiler save time by explicitly declaring what type of data you are about to assign to a variable.

Letting the compiler figure out the data type is one of the main reasons you run into performance issues while scaling your application. 

Also, [Rust is a statically typed language](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages), which means it must know the types of all variables at compile time.

Though Rust is syntactically similar to C and C++, don't let its simplicity fool you. Rust does come with a steep learning curve. But it is totally worth it once you get a good grasp of the basics.

## Who Uses Rust?

Now that you have a good grasp of what Rust is, let's look at who uses Rust.

### Microsoft

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-6.png)

Once a fierce adversary of open source, Microsoft is now an avid contributor to a number of open-source projects. Their .net core project is one of the most popular open-source frameworks used by developers today.

Microsoft has chosen Rust for security and performance-critical applications. Rust is also used extensively in Azure, especially in its [IoT Edge platform](https://azure.microsoft.com/en-in/services/iot-edge/) to run AI applications on IoT devices.

### Dropbox

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-7.png)

Dropbox uses Rust to improve its data center efficiency. Rust is now powering core services of Dropbox serving more than 500 million users. 

Dropbox [recently wrote a detailed article](https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine) on how they re-wrote their core engine.

In Dropbox’s own words,

> Rust has been a force multiplier for our team, and betting on Rust was one of the best decisions we made.

Rust was also a contributing factor that helped Dropbox move its infrastructure from AWS to its own data centers.

### Figma

![Image](https://www.freecodecamp.org/news/content/images/2020/08/figma.png)

---

Figma is a cloud-based designing and prototyping tool that you can use in your browser. It is an excellent tool for designing, prototyping, and exporting your designs into code. [Learn more about Figma here](https://www.figma.com/).

Concurrency is crucial for a collaborative tool where many users will be working on a single design at a time. Figma used Rust to write a high-performance server that helped them scale their product and achieve the performance they were looking for.

[Here is the article Figma wrote](https://www.figma.com/blog/rust-in-production-at-figma/) about their experience with Rust.

## TL;DR

Rust is a systems programming language that has been voted as [StackOverflow’s most loved programming languages](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/), four years in a row. 

Rust gives you control over low-level details and provides remarkable improvements in speed and stability. 

It has helped companies like Dropbox, Figma, and Microsoft build better applications for their customers.

The language is being increasingly adopted by companies looking to scale their applications with higher performance and concurrency. Sounds interesting? [Start learning Rust here](https://doc.rust-lang.org/stable/rust-by-example/).

---

_I regularly write about Machine Learning, Cyber Security, and DevOps. You can signup for my_ [_weekly newsletter_](https://www.manishmshiva.com/) _here._

