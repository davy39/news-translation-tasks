---
title: Go (Golang) Programming Language
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T22:07:00.000Z'
originalURL: https://freecodecamp.org/news/go-golang-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/golang-gopher-2.jpg
tags:
- name: golang
  slug: golang
- name: programming languages
  slug: programming-languages
seo_title: null
seo_desc: "Go (or golang) is a programming language created at Google in 2007 by Robert\
  \ Griesemer, Rob Pike, and Ken Thompson. It is a compiled, statically-typed language\
  \ in the tradition of Algol and C. \nGo has garbage collection, limited structural\
  \ typing, me..."
---

**Go** (or **golang**) is a programming language created at Google in 2007 by Robert Griesemer, Rob Pike, and Ken Thompson. It is a compiled, statically-typed language in the tradition of Algol and C. 

Go has garbage collection, limited structural typing, memory safety, and CSP-style concurrent programming features added. The compiler and other language tools originally developed by Google are all free and open source. 

Go's popularity is increasing fast. It is a great choice for building web applications.

For more information head to [Go’s Homepage](https://golang.org/). Want a quick tour of Go? Check out the docs [here](https://tour.golang.org/welcome/1).

Now let's see how to install and get started with Go.

## **Installation**

### Install Golang with Homebrew:

```bash
$ brew update
$ brew install golang
```

### **Installing Go on MacOS using a tarball**

#### **Link to tarball**

You can get the link to the MacOS tarball archive from the Latest Stable section of the [golang download page](https://golang.org/dl/).

#### **Installation Process**

In this installation process we’ll use the latest stable version as of this writing (go 1.9.1). For a newer or older version simply replace the link in the first step. Check the [golang download page](https://golang.org/dl/) to see what versions are currently available.

##### **Installing Go 1.9.1**

```text
$ curl -O https://storage.googleapis.com/golang/go1.9.1.darwin-amd64.tar.gz
$ sudo tar -C /usr/local -xzf go1.9.1.darwin-amd64.tar.gz
$ export PATH=$PATH:/usr/local/go/bin
```

### **Install Golang on Ubuntu with apt**

Using Ubuntu’s Source Package Manager (apt) is one of the easiest ways to install Go. You won’t get the latest stable version, but for the purpose of learning this should be enough.

```sh
$ sudo apt-get update
$ sudo apt-get install golang-go
```

#### **Check the installation and version of Go**

To check if go was successfully installed, run:

```sh
$ go version
> go version go1.9.1 linux/amd64
```

This will print the version of Go that's installed to the console. If you see a version of Go, you'll know that the installation went smoothly.

## Setup the workspace

### Add Environment variables:

First, you’ll need to tell Go the location of your workspace.

We’ll add some environment variables into shell config. One of does files located at your home directory bash_profile, bashrc or .zshrc (for Oh My Zsh Army)

```bash
$ vi .bashrc
```

then add those lines to export the required variables

#### **This is actually your .bashrc file**

```bash
export GOPATH=$HOME/go-workspace # don't forget to change your path correctly!
export GOROOT=/usr/local/opt/go/libexec
export PATH=$PATH:$GOPATH/bin
export PATH=$PATH:$GOROOT/bin
```

## Create your workspace

### Create the workspace directories tree:

```bash
$ mkdir -p $GOPATH $GOPATH/src $GOPATH/pkg $GOPATH/bin
$GOPATH/src : Where your Go projects / programs are located
$GOPATH/pkg : contains every package objects
$GOPATH/bin : The compiled binaries home
```

## The Golang Playground

Learning how to install Go on your local machine is important. But if want to start playing with Go right in your browser, then Go Playground is the perfect sandbox to get started right away! 

Just open a new browser window and go to the [Playground](https://play.golang.org/).

Once there you’ll get the buttons:

1. Run
2. Format
3. Imports
4. Share

The **Run** button just sends the instructions for compiling the code you wrote to the Google servers that run the Golang back end.

The **Format** button implements the idiomatic formatting style of the language. You can read more about it [here.](https://golang.org/pkg/fmt/)

**Imports** just check what packages you have declared within import(). An import path is a string that uniquely identifies a package. A package’s import path corresponds to its location inside a workspace or in a remote repository (explained below). You can read more [here](https://golang.org/doc/code.html#ImportPaths).

With **Share** you get a URL where the code you just wrote is saved. This is useful when asking for help showing your code.

You can take a more in-depth [Tour of Go here](https://tour.golang.org/welcome/4) and learn more about the playground in the article [Inside the Go Playground](https://blog.golang.org/playground).

## Go Maps

A map, called a _dictionary_ in other languages, “maps” keys to values. A map is declared like this:

```go
var m map[Key]Value
```

This map has no keys and no keys can be added to it. To create a map, use the `make` function:

```go
m = make(map[Key]Value)
```

Anything can be used as a key or as a value.

## Modifying maps

Here are some common action with maps.

### Inserting/Changing elements

Create or change element `foo` in map `m`:

```go
m["foo"] = bar
```

### Getting elements

Get element with key `foo` in map `m`:

```go
element = m["foo"]
```

### Deleting elements

Delete element with key `foo` in map `m`:

```go
delete(m, "foo")
```

### Check if a key has been used

Check if key `foo` has been used in map `m`:

```go
element, ok = m["foo"]
```

If `ok` is `true`, the key has been used and `element` holds the value at `m["foo"]`. If `ok` is `false`, the key has not been used and `element` holds its zero-values.

## Map literals

You can directly create map literals:

```go
var m = map[string]bool{
	"Go": true,
	"JavaScript":false,
}

m["Go"] // true
m["JavaScript"] = true // Set Javascript to true
delete(m, "JavaScript") // Delete "JavaScript" key and value
language, ok = m["C++"] // ok is false, language is bool's zero-value (false)
```

## More info about Go:

* [Learn Go in 7 hours with this free video course](https://www.freecodecamp.org/news/go-golang-course/)
* [How to build a Twitter bot](https://www.freecodecamp.org/news/creating-a-twitter-bot-from-scratch-with-golang-e1f37a66741/) with Go

  


  









