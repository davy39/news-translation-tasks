---
title: What is Go? Golang Programming Language Meaning Explained
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-10-07T15:26:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-go-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/golang.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: null
seo_desc: "Go, also known as Golang, is an open-source, compiled, and statically typed\
  \ programming language designed by Google. It is built to be simple, high-performing,\
  \ readable, and efficient. \nIn this article, you'll learn:\n\nWhere Go came from\
  \ and where it ..."
---

Go, also known as Golang, is an open-source, compiled, and statically typed programming language designed by Google. It is built to be simple, high-performing, readable, and efficient. 

In this article, you'll learn:

* Where Go came from and where it is now, 
* Why I think you should learn it, 
* How to install and run it on Windows 10, and
* How to write your first "Hello World" program in Go

## Table of Contents
- [What's the Name? Go or Golang?](#heading-whats-the-name-go-or-golang)
- [How Go Came into Existence](#heading-how-go-came-into-existence)
- [Why you Should Learn Go](#heading-why-you-should-learn-go)
- [How to Install and Run Go on Windows 10](#heading-how-to-install-and-run-go-on-windows-10)
- [How to Write your First Hello World in Go](#heading-how-to-write-your-first-hello-world-in-go)
- [Conclusion](#heading-conclusion)


## What's the Name? Go or Golang?

You might hear the language called both Go and Golang, which might be confusing. I once thought they were names for different languages. But Golang is just another name for Go – and Go remains the official name. 

Golang came from the domain name of the Go official website, golang.org. Which is actually really helpful, because “Golang” is much more searchable than "Go" on Google. So it makes life a little easier for those who might be looking for information on the programming language.

## How Go Came into Existence

The Go programming language was borne because things were getting much more complex in the codebases within Google. 

It was designed by Robert Griesemer, Rob Pike, and Ken Thompson, who all reportedly have a shared dislike for C++.

Go was announced to the public in 2009, and it was made open source in 2012 when its first version, 1.0, was released. 

Go quickly rose in popularity and became many developers' first choice due to its simplicity, readability, efficiency, and concurrent nature. Concurrent means that it can run multiple tasks at the same time.

Go is used for server-side (backend) programming, game development, cloud-based programming, and even Data Science. It is also popular for making command-line tools. 

Today, many tech giants use Go like Google, Netflix, Twitch, Ethereum, Dropbox, Kubernetes, Docker, Heroku, and lots more. 

There’s no surprise that the likes of Kubernetes, Docker, and Heroku are using Go because cloud-based programming is one of the main reasons why Go was designed.

## Why you Should Learn Go

### Easy Learning Curve

Go is one of the simplest programming languages out there. It is easy to pick up especially if you already have knowledge of any other programming language. In my case, I learned the fundamentals of Go in one sitting. 

A lot of developers who use Go and are confident in their teaching abilities say that they can get an absolute beginner to build an app with Go in just a few hours.

The simplicity of Go is one of the main reasons it jumped 5 places from the 10th to 5th most loved programming language according to the 2020 StackOverflow Developer Survey.

### Active Community and Good Documentation

Go has solid and easy-to-read documentation. You can read the documentation on the official website.

Apart from documentation, Go also has a supportive and active community behind it, so you can always get help when you are stuck. 

The hashtag #golang is commonly used on Twitter, so in case you get stuck, you can tweet your question and attached the hashtag to it. 

### You Can Get a lot Done with Go

Go is a multipurpose programming language, meaning you can use it for a number of things such as web development, data science, cloud computing, and more. 

If you want to have a career in cloud-based programming, you should consider learning Go, because platforms such as Amazon Web Services, Kubernetes, and Google Cloud Platform (GCP) all support Go.

### Attractive Wages

According to the 2020 StackOverflow Developer Survey, Go developers are the third-highest paid after Perl and Scala with a median salary of $74K. 

This figure will probably continue to climb, because Go continues to gain more popularity every year and it is in demand. So, if you want to earn more money, you should consider learning Go.

## How to Install and Run Go on Windows 10

To install Go on your Windows machine, you first have to [download Go](https://golang.org/) from the official website. It is available for all popular operating systems. Click on the one that correlates to your OS and install it.

**Step 1**: Before installing Go, open up your command prompt, type “go” and hit enter. You can open the command prompt by entering “cmd” in the Windows Search bar, and then selecting the first app that shows up.

When you enter “go” and hit enter, you should get a message that says “'go' is not recognized as an internal or external command, operable program or batch file”.

![ss-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-1.png)

Don’t worry, this is because you have to install Go by double-clicking on the Installer downloaded from the Go website.

**Step 2**: Double-click on the downloaded installer to install Go. Follow the prompts accordingly and Go will be installed.

![ss-2](https://www.freecodecamp.org/news/content/images/2021/10/ss-2.png)
![ss-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-3.png)

**Step 3**: After installing Go through the installer, head back to the command line and enter “go” again. This time around, you should see several commands available in Go.

![ss-4](https://www.freecodecamp.org/news/content/images/2021/10/ss-4.png)

**Step 4**: But you can’t just start programming in Go like that. You have to set up your Go workspace by configuring environment variables. 

So, head over to your desktop and create the folder “go-workspace”. You can name it whatever you want. This is the folder where your Go projects will be stored. Only when you set the value of the `GOPATH` variable to it. We do this in the next steps.

**Step 5**: Search for “env” on the windows Searchbar and click on “Edit the system environment variables”.

![ss-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-5.png)

**Step 6**: Click on “Environment Variables”.

![ss6-edited-1](https://www.freecodecamp.org/news/content/images/2021/10/ss6-edited-1.jpg)

What you are going to do here is change the value of the `GOPATH` variable to the folder you created in **Step 4**. 

**Step 7**: Make sure “GOPATH” is selected, then click “Edit…”. 

![ss-7edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-7edited.jpg)

**Step 8**: Click on “Browser Directory”.

![ss-8edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-8edited.jpg)

**Step 9**: Select the folder you created in **Step 4**. That is, “go-workspace”, or whatever you named it.

![ss-9edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-9edited.jpg)

Click “Ok”.

![ss-10edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-10edited.jpg)

Click "Ok" again.

![ss-11edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-11edited.jpg)

And "Ok" again.

![ss-12edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-12edited.jpg)

That’s it! You can now start programming in Go on your Windows machine.

## How to Write your First Hello World in Go

**Step 1**: Open up the “go-workspace” folder (or whatever you named it) with VS Code (or your code editor of choice) and create a file named `main.go`. You can name the file whatever you want.

![ss-13](https://www.freecodecamp.org/news/content/images/2021/10/ss-13.png)

**Step 2**: When you hit enter, you will be prompted to install the Go extension for VS Code. Make sure you install it as it will give your code editor some Golang superpowers such as syntax highlighting and snippet suggestions.

You should also be prompted by VS Code to install some more extensions. Install them all. In my case, I installed everything for my VS Code already and all my extensions are in sync, so I didn’t get those prompts.

Paste in the following code in the main.go file (or whatever you named the file):

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

**What’s the code above doing?**

The first line has `package main`. “package” is a collection of files and code every Go file has. Think of `package` as a containing folder for your Go files and codes.

No matter what you named your file, make sure the “package main” is available on top of your code.

After that `fmt` gets brought in. “fmt” is a package from the Go standard library. It is used for formatting strings and printing messages to the command line. It contains methods for doing things in Go. 

One of the methods is `Println`, meaning “print line”, which we will use to print our “Hello World” text.

Inside the function “main”, the `fmt` package was then used to output our “Hello World” text to the console.

To run this code, open up your terminal, type `go run main.go`, and hit enter. If you named your file something else, make it `go run yourFileName.go`.

![ss-14](https://www.freecodecamp.org/news/content/images/2021/10/ss-14.png)

## Conclusion

In this article, you learned about the Go programming language and why it is a good one to know. You also learned how to install Go on a Windows machine and write your first Hello World program in it.

Go is a powerful programming language that is here to stay. It's clear from the 2020 StackOverflow Developer Survey that developers love Go, and its popularity is rising year by year.

Go is definitely worth your time. Now, go learn some Go. 


