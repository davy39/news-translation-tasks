---
title: The Top 8 Things I Learned From 4000 Rust Developers
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2020-05-24T17:57:05.000Z'
originalURL: https://freecodecamp.org/news/8-things-i-learned-from-4000-rust-developers
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/learn-rust-20-seconds-1.gif
tags:
- name: codespaces
  slug: codespaces
- name: programming languages
  slug: programming-languages
- name: Rust
  slug: rust
- name: Visual Studio Code
  slug: vscode
- name: Web Applications
  slug: web-applications
- name: WebAssembly
  slug: webassembly
seo_title: null
seo_desc: 'Do you know that most Rust programmers are working on web applications?
  ? Rust is challenging, but also rewarding and great fun! Learn Rust by example,
  or ?open this GitHub repo to get started in VSCode.

  Rust is one of the hottest ? programming langu...'
---

Do you know that most Rust programmers are working on web applications? ? Rust is challenging, but also rewarding and great fun! Learn [Rust by example](https://rust-by-example-ext.com/), or ?open [this GitHub repo](https://github.com/second-state/learn-rust-with-github-actions) to get started in VSCode.

Rust is one of the hottest ? programming languages today. It is StackOverflow's [most beloved programming language](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/) for the past 4 years. Yet, it still has a reputation as the programming language for alpha geeks.

By [some estimate](https://s3-eu-west-1.amazonaws.com/vm-blog/uploads/2020/04/DE18-SoN-Digital-.pdf), there are 600,000 Rust developers world-wide, which is a significant number. But it's still dwarfed when compared with tens of millions of JavaScript, Java, and Python developers.

Who are those Rust developers? What are they using Rust for? Why do they love Rust so much? And most important, how do you join their ranks and see for yourself why Rust is so beloved? Don't get left behind.

In order to answer those questions, the Rust community has conducted annual developer surveys from rust-lang.org since 2016. The site recently released its [2019 survey results](https://blog.rust-lang.org/2020/04/17/Rust-survey-2019.html) based on responses from nearly 4000 Rust developers. Here are the top 8 things I learned from the survey.

## ??‍? Rust is for professional programmers

The Rust programming language is not designed to be “[easy to get started](https://www.secondstate.io/articles/a-rusty-hello-world/)”. Rather, it is designed to be powerful and safe at the same time. It aims to be the developer productivity language for professional programmers. It is challenging, fun, and rewarding. That shows in the survey.

Very few respondents call themselves as Rust experts. Most people rate their Rust expertise as 7/10 or below, despite the fact that over 68% of them write Rust code on a weekly basis. It is clearly a language that takes time to master and excel.

> About 37% of Rust users felt productive in Rust in less than a month of use - this is not too different from the percentage last year (40%). Over 70% felt productive in their first year. Unfortunately, like last year, there is still a struggle among users - 21% indicated they did not yet feel productive.

At the same time, when asked why not using Rust on some projects, the learning curve is cited as the #2 most common reason. The #1 reason, of course, is the company’s decision whether to use a particular programming language in a project.

## ? Documentation is critical for adoption

How do developers overcome Rust's learning curve and fall in love with it? Well, not unexpectedly, most developers cited “better documentation” as the driver for adoption.

But true to “professional programmers”, the most sought after Rust documentation is intermediate-level content that helps developers improve their Rust skills and productivity.

While the survey is biased toward developers who already knew the basics of Rust, it seems that there is a thirst for knowledge and self-improvement in this crowd.

## ? Developers do not want tomes of text

Traditional software documentation typically consists of entire books and websites. New generations of developers want more and better documentation. As a “new” language, Rust is already leading the innovation when it comes to programming language documentation.

For example, the Rust compiler is a self-documenting tool. One of the most unique and beloved features of Rust is its aggressive compiler that helps you ensure correctness and safety before the program even runs. As a result, Rust developers can write highly performant yet safe programs.

When you encounter a compiling error in Rust, the compiler gives you an immediate explanation of the error, and suggestions on how to fix the error based on the context of your program.

[This starter project](https://github.com/second-state/learn-rust-with-github-actions) in GitHub gets you started with the Rust compiler and the Cargo system without having to install any software toolchain. You can use the VSCode online IDE directly with this project.

Rust documentation web sites like [docs.rs](http://docs.rs) and [Rust by Example](https://doc.rust-lang.org/rust-by-example/) (and its [Extended Edition](https://rust-by-example-ext.com/)) use the [Rust Playground](https://play.rust-lang.org/) to run Rust example code directly from the browser. Those interactive books are much better than simple text.

However, as the survey finds out, developers want more. Developers are thirsty for more video content, for example. We can look forward to more coding videos and live broadcasts from the community soon.

## ?️ Most people use Rust for web apps, srsly!

As a system-level language intended to replace C and C++, most people assume that Rust would be used in infrastructure programming, such as operating systems, native libraries, and runtime platforms.

Yet, the survey clearly shows that by a large margin, most Rust developers today are working on web app backends. No wonder crates like [hyper](https://docs.rs/hyper/0.13.5/hyper/), [actix-web](https://github.com/actix/actix-web), and [Rocket](https://rocket.rs/) are among the most popular with Rust developers.

To be sure, most software developers are working on web applications. It is not surprising that, as Rust gains mainstream adoption, Rust projects will mirror the bigger software industry.

However, that does present opportunities for projects and tools that integrates Rust into popular web application runtimes. For example, the [Rust + JavaScript hybrid application](https://www.secondstate.io/articles/getting-started-with-rust-function/) approach is gaining momentum.

## ? Blockchain is a Rusty hotbed

When it comes to infrastructure software, Rust really shines as a programming language for blockchain systems.

For all software related industry sectors, the survey shows that blockchain only ranks the 35th for all software developers, but 11th for Rust developers. That is in no small part due to aggressive Rust adoption by large blockchain projects such as [Polkadot / Substrate](https://www.parity.io/), [Oasis](https://www.oasislabs.com/), [Solana](https://solana.com/), and [Second State](https://www.secondstate.io/) etc.

In many ways, blockchains are perfect fit for Rust. Blockchains represent the community effort to re-build the internet infrastructure in a decentralized manner. They require high performance software that is also very safe. If you are interested in a career as a blockchain engineer, Rust is a must-have skill today.

## Rust ❤️ WebAssembly

The survey reveals that WebAssembly is a popular runtime environment for Rust programs. Rust and WebAssembly were both invented at Mozilla.

Rust is focused on performance and memory safety, while WebAssembly is focused on performance and runtime safety. As a runtime container, WebAssembly also makes Rust programs cross-platform and more manageable. There are indeed a lot of synergy between the two technologies.

WebAssembly was originally invented as a client side virtual machine to run in-browser applications. But as Java and JavaScript before it, WebAssembly is now making the migration from the client side [to the server side](https://www.secondstate.io/articles/why-webassembly-server/).

Rust-in-WebAssembly bodes well with the trend of accelerating Rust adoption on backend web applications. You can get started with Rust and WebAssembly application development from a starter project in [this GitHub repository](https://github.com/second-state/ssvm-nodejs-starter).

## ? Asynchronous programming is taking off

In recent years, two new programming languages have gained significant traction among developers. One is Rust, and the other is Go. A big part of their success is their superior support for concurrency programming models.

In fact, an early tagline of Rust is "fearless concurrency". It promises developer productivity in writing asynchronous multi-threaded programs optimized for today’s multi-core CPU architectures. As Node.js demonstrated, easy asynchronous programming is crucial for a language or framework’s success on the server side.

The survey shows that 4 of the 10 most important Rust crates (ie third party libraries), [tokio](https://tokio.rs/), [async](https://docs.rs/crate/async-std/1.4.0), [futures](https://docs.rs/futures/0.3.4/futures/), and [hyper](https://hyper.rs/), are frameworks for asynchronous multi-thread applications.

## ? R, Python, and JavaScript

As the adoption of Rust grows, developers increasingly need to integrate Rust programs with programs written in other languages. In the past, C and C++ were the most common languages to “talk” to Rust as they are all used in infrastructure software projects.

As Rust grows into application software projects, more language level interfaces and bridges are needed now. A good example is the [Rust JavaScript bridge](https://www.secondstate.io/articles/rust-functions-in-nodejs/) that supports [Rust functions in Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/) applications.

The survey found that, besides C/C++ and JavaScript, Rust developers are interested in integrating with R and Python. That indicates developer interests in machine learning, big data, and artificial intelligence (AI) applications. In fact, many Python and R machine learning and statistical packages are implemented in native binary modules.

Rust is one of the best programming languages to write native modules. [This example](https://github.com/second-state/rust-wasm-ai-demo) shows how to use [Rust to execute Tensorflow models in a Node.js](https://www.secondstate.io/articles/artificial-intelligence/) application. In the future, we envision such Rust modules to run in high performance managed containers such as WebAssembly.

## Conclusion

2019 was a year of growth and incremental improvements for Rust. As Rust becomes a mainstream programming language, we look forward to more documentation, more tools, more ecosystem support, more interoperability with other languages, and a gentler learning curve.

And most important of all, we are eager to make more friends and have fun with the most beloved programming language in the world!

## About the author

Dr. Michael Yuan is the [author of 5 books](http://www.michaelyuan.com/) on software engineering. His latest book [Building Blockchain Apps](https://www.buildingblockchainapps.com/) was published by Addison-Wesley in Dec 2019. Dr. Yuan is the co-founder of [Second State](https://www.secondstate.io/), a VC-funded startup that brings WebAssembly and Rust technologies to [cloud](https://www.secondstate.io/articles/why-webassembly-server/), [blockchain](https://docs.secondstate.io/), and [AI](https://github.com/second-state/rust-wasm-ai-demo/blob/master/README.md) applications. It enables developers to deploy fast, safe, portable, and serverless [Rust functions on Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/).

<iframe src="https://webassemblytoday.substack.com/embed" width="480" height="320" style="border:1px solid #EEE;background:white"></iframe>

Prior to Second State, Dr. Yuan was a long time open source contributor at Red Hat, JBoss, and Mozilla. Outside of software, Dr. Yuan is a Principal Investigator at the National Institutes of Health, with multiple research awards on cancer and public health research. He holds a PhD in astrophysics from the University of Texas at Austin.
