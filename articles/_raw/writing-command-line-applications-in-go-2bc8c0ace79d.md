---
title: How to write fast, fun command-line applications with Golang
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-24T04:29:16.000Z'
originalURL: https://freecodecamp.org/news/writing-command-line-applications-in-go-2bc8c0ace79d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8Y-A5uFE028SqeflYpJ-7Q.png
tags:
- name: golang
  slug: golang
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Peter Benjamin

  A while back, I wrote an article about “Writing Command-Line Applications in NodeJS”.

  I love JavaScript, Node.JS, npm, and the whole ecosystem. To me, nothing feels more
  natural than writing modern JavaScript applications with ES6 o...'
---

By Peter Benjamin

A while back, I wrote an article about “[Writing Command-Line Applications in NodeJS](https://medium.freecodecamp.com/writing-command-line-applications-in-nodejs-2cf8327eee2)”.

I love JavaScript, Node.JS, npm, and the whole ecosystem. To me, nothing feels more natural than writing modern JavaScript applications with ES6 or TypeScript.

But, lately, I’ve needed to leverage multi-processor (parallel) concurrency. Due to NodeJS’s single-threaded event loop, NodeJS is concurrent, but not parallel. NodeJS does not support parallel concurrency “out of the box”.

#### Why Go?

The Go language (often referred to as “Golang”), will utilize all cores of a machine by default. Go also brings the following benefits:

* Type safety (e.g. you cannot pass a string to a function that’s expecting a number — the compiler will complain)
* Easy refactoring (e.g. changing a function or variable name will propagate that change throughout the project)
* Speed and performance out-of-the-box
* Procedural programming paradigm is certainly much easier to reason about
* Easy deployments (just deploy the single binary file and done!)
* Standard style (Go is opinionated about formatting and comes with tooling to automate this)
* … and many more!

**Note:** It’s important for new developers **not** to be intimidated by new concepts. Embrace that uncomfortable feeling you get when you face a new challenge. It means you’re learning, growing, and improving. A key trait of successful developers is _persistence_.

Here’s what you’ll learn by following along with this article:

1. Namespaces
2. Imports
3. Variables
4. Structs
5. Functions
6. References and Pointers
7. **_If_** conditions
8. **_For_** loops

### Getting Started

In order to avoid bloating this article by having to support different commands for 3 different platforms, I will assume that you’re following along on [Cloud9](http://c9.io). Cloud9 is an online IDE (integrated development environment) — basically, it’s awesome sauce!

#### Install

Go already comes pre-installed on Cloud9’s _blank U_buntu workspaces. So, you can skip this step.

If you want to follow along on your local computer, you can [download and install Go](https://golang.org/dl/).

#### Setup

Go requires you to setup your environment in a particular way.

* You must have a home for all your Go projects. Go calls this home a **_workspace_**. The workspace must contain 3 directories: _bin_ (for binaries), _pkg_, and _src_ (for source code):

```bash
$ pwd
/home/ubuntu/workspace

$ mkdir {bin,src,pkg}
```

* Go assumes that each project lives in its own repository, so we need to further organize our _src_ directory into:

```bash
$ mkdir -p src/github.com/<your_github_username>/<project_name>
```

**Note:** If you’re a _gitlab_ or a _bitbucket_ user, simply change _github.com_ with the appropriate name (e.g _gitlab.com_ or _bitbucket.org_ respectively).

There is a reason for this directory structure. Go doesn’t have a centralized code repository, like NPM, or RubyGems. Go can fetch source code from online VCS (version control systems) directly and, when it does, it will download the source code in the correct path. For example, the following command:

```
$ go get golang.org/x/tools/cmd/goimports
```

will tell Go to contact golang.org, then download the source under:

```bash
<your_go_workspace>/src/golang.org/x/tools/cmd/goimports
```

Which, in return, enables Go to find third-party packages and libraries when you import them into your project.

* Lastly, we need to setup our _GOPATH_ environment variable. In Cloud9 Ubuntu, just add the following at the end of _.bashrc_:

```
# in ~/.bashrc
...
export GOPATH="/home/ubuntu/workspace"
export PATH="$PATH:$GOPATH/bin"
```

Then, save the file and run the following command in the terminal:

```bash
source ~/.bashrc
```

* To verify that Go is working on Cloud9 and that our GOPATH is set up correctly:

```bash
$ go version
go version go1.6 linux/amd64

$ go get golang.org/x/tools/cmd/goimports
$ goimports --help
usage: goimports [flags] [path ...]
...
```

For more information on Golang setup, visit [the official “Getting Started” doc](https://golang.org/doc/code.html).

### Let’s Go!

Our Goal: to build a minimal CLI app to query [GitHub](https://api.github.com/) [users](https://api.github.com/users).

Let’s create a repo for this project on Github.com. Call it **gitgo**. Then clone it:

```bash
$ cd $GOPATH/src/github.com/<your_github_username>
$ git clone git@github.com:<your_github_username>/gitgo.git
```

#### A Go primer

Let’s create our first file, call it **_main.go_**, and write the following code (don’t worry, we’ll cover each line):

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World")
}
```

#### Breaking it down…

```
package main
```

* This is a namespace declaration. Namespaces are just a way for us to group logic and functionality. You’ll see how namespaces will help us a little bit later.
* The word **_main_** is a keyword. It tells the GO compiler that our code is intended to run as an **_application_** not as a **_library_**. The difference is that **_applications_** are used directly by our users, whereas **_libraries_** can only be imported and used by other pieces of code.

```
Import “fmt”
```

* Import statement. This imports the “[fmt](https://golang.org/pkg/)” (short for “format”) package from the [standard library](https://golang.org/pkg/).

```
func main()
```

* **_func_** is the keyword to define or declare a function in GO.
* The word **_main_** is a special keyword in GO. It tells the GO compiler that our application starts here!

```
fmt.Println(“Hello, World”)
```

* This is pretty self-explanatory. We’re using the **Println** function from the **fmt** package we imported earlier to… well… print line.

Notice that the first letter of function **Println** is upper-case. This is GO’s way of exporting variables, functions, and other stuff. If the first letter of your function or variable is upper-case, it means you’re making it accessible to external packages or namespaces.

#### Let’s Run It!

```bash
$ go run main.go
Hello, World
```

Awesome! You’ve written your first GO application.  
What just happened? Well, GO compiled _AND_ executed the application in memory! Pretty fast, huh?

#### Let’s Build It!

```bash
$ go build     # generates executable binary in your local directory 
$ ./gitgo
Hello, World
```

Sweet! You’ve just built your first GO application. You can send just that**one** file to your friends and family and they can run it and get the **same results**. Of course, if they’re running Windows, this application will not work, because we built it for Linux/Unix. So, let’s build it for Windows:

```bash
$ GOOS=windows go build -o forecaster.exe main.go
```

There you go! Now, you’ve created an application for Windows. Pretty neat, huh?

In fact, you can cross-compile that application to a wide range of platforms (e.g. Windows, Linux, OS X) and architectures (e.g. i386, amd64). You can see the full list here: [https://golang.org/doc/install/source#environment](https://golang.org/doc/install/source#environment)

#### Let’s Install It!

If you want your application to be accessible from anywhere on your system:

```
$ go install
```

That’s it. Now, you can call your application from anywhere:

```bash
$ gitgo
Hello, World
```

At this point, it would be a good idea to check your work into GitHub:

```bash
$ git add .
$ git commit -am "Add main.go"
$ git push
```

Awesome! But so far, our application doesn’t do anything really. This exercise was just meant to get our feet wet and give us an idea of what it’s like to code in Go.

#### Now, let’s dive into our CLI app!

We envision the interaction with our app to look something like

```bash
$ gitgo -u pmbenjamin
# or...
$ gitgo --user pmbenjamin,defunkt
```

Now that we have a direction, let’s start creating those flags.

We could use the **_flag_** standard library in Go, but, with trial-and-error and a little bit of Googling, you will discover that the standard **_flag_** library does not support the long-flag syntax (via double-dash). It only supports single dashes.

Luckily, someone already solved this with a GO library. Let’s download it:

```bash
$ go get github.com/ogier/pflag
```

Now, let’s import it in our project:

```go
import (

    "github.com/ogier/pflag"
)
```

In GO, the last element of the import statement is the namespace we use to access library’s functions:

```go
func main() {
    pflag.SomeFunction()
}
```

If we prefer to use a different name, we can alias our package names at import:

```go
import (

    flag "github.com/ogier/pflag"
)
```

This will allow us to do:

```go
func main(){
    flag.SomeFunction()
}
```

Which is what you see in the [official examples](https://github.com/ogier/pflag).

Let’s create the variables that will hold the data from the user input:

```go
import (...)import (
...
)

// flags
var (
   user  string
)

func main() {
...
}
```

A couple of things to point out here:

* We’ve declared our variables _outside_ of `func main()`. This allows us to reference these variables in other functions beside `func main()`. This might feel weird to you, because you don’t want to pollute the global namespace. But, trust me, this is perfectly OK in Go. We’re scoped just to the current namespace.
* Go is a statically-typed language, which means that you have to specify the type of data that will be stored in each variable (hence the `string` keywords)

Now that you’ve declared your variables, let’s declare your flags and bind/map each flag to the appropriate variable:

```go
import (
    ...
)

// flags
var (
    ...
)

func main() {
 flag.Parse()
}

func init() {
 flag.StringVarP(&user, "user", "u", "", "Search Users")
}
```

#### Breaking it down…

```
func init()
```

* **init** is a special function in GO. GO executes applications in the following order:  
1. Imports statements  
2. Package-level variables/constants declarations  
3. init() function  
4. main() function (if the project is to be treated as an app)
* All we are trying to do is initialize the flags once

```go
flag.StringVarP(&user, "user", "u", "", "Search Users")
```

* From the **flag** package/library, we are using the **StringVarP()** function.
* `StringVarP()` does 3 things:   
1. it tells GO that we will be evaluating expecting a **String**,  
2. it tells GO that we want to bind a **Var**iable to this flag, and  
3. it tells GO that we want to have a **P**osix-compliant flag (e.g. double-dash and single-dash flag)
* `StringVarP()` takes 5 arguments in this order:  
1. the variable we want to bind this flag to,  
2. the double-dash flag,  
3. the single-dash flag,  
4. the default value to use if flag is not explicitly called,  
5. and the description of this flag
* `&user` means that we are passing a reference (a.k.a. memory address) of the **user** variable. OK, before you start freaking out about references and memory addresses, let’s just break this concept down further…
* In many languages, like JavaScript and Ruby, when you define a function that takes an argument then call the function and pass it an argument, you’re essentially creating a new copy of the variable that you’re passing in as an argument. But, there are times when you don’t want to pass a copy of data. Sometimes, you need to operate on the original data.
* Hence, if you pass the data by **value**, you’re essentially creating another copy of the data and passing that copy around, whereas if you pass the variable by **reference** (aka by its memory address), then you’re passing the original data.
* In GO, you can get the memory address of almost anything by pre-pending the ampersand (&) symbol.

```go
flag.Parse()
```

* Parse the flags.

#### Let’s test our work…

```bash
$ go run main.go # nothing happens
$ go run main.go --help
Usage of /tmp/go-build375844749/command-line-arguments/_obj/exe/main:
  -u, --user string
        Search Users
exit status 2
```

Great. It seems to be working.

Notice the weird **_/tmp/go-build…_** path? That’s where our application was compiled and executed dynamically by Go. Let’s build it and test it:

```bash
$ go install -v
$ gitgo --help
Usage of gitgo:
  -u, --user string
        Search Users
```

**Pro-Tip:** When building or compiling binaries, always prefer `go install` over `go build`. `go install` will cache non-main packages into `$GOPATH/pkg` , thus resulting in faster build times than `go build`.

#### Core Logic

Now that we’ve initialized our flags, let’s start implementing some core functionality:

```go
func main() {
 // parse flags
 flag.Parse()
 
 // if user does not supply flags, print usage
 // we can clean this up later by putting this into its own function
  if flag.NFlag() == 0 {
     fmt.Printf("Usage: %s [options]\n", os.Args[0])
     fmt.Println("Options:")
     flag.PrintDefaults()
     os.Exit(1)
  }
  
  users = strings.Split(user, ",")
  fmt.Printf("Searching user(s): %s\n", users)
  
}
```

Note that there are no parentheses around **if** conditionals in Go.

#### Let’s test our work…

```bash
$ go install
# github.com/pmbenjamin/gitgo
./main.go:15: undefined: fmt in fmt.Printf
./main.go:15: undefined: os in os.Args
./main.go:16: undefined: fmt in fmt.Println
./main.go:18: undefined: os in os.Exit
./main.go:21: undefined: fmt in fmt.Printf
./main.go:24: undefined: fmt in fmt.Printf
```

I intentionally wanted to show you the experience of the Go compiler when it complains that you did something wrong. It’s important that we’re able to understand these error messages to fix our code.

So, the compiler is complaining that we’re using the `Println` function from the **fmt** package, but that package is undefined. Same with `Exit` from **os** package.

Turns out, we just forgot to import some packages! In a normal IDE (e.g. Atom, VS-Code, vim, emacs …etc), there are plugins that you can install in your editor that will dynamically and automatically import any missing packages! So, you don’t have to import them manually. How awesome is that?

For now, let’s add the correct import statements ourselves. Remember the `goimports` tool we installed earlier?

```bash
$ goimports -w main.go # write import stmts back in main.go!
```

And re-build and re-test app:

```bash
$ go install

$ gitgo
Usage: gitgo [options]
Options:
  -u, --user string
        Search Users

$ gitgo -u pmbenjamin        
Searching user(s): [pmbenjamin]
```

Yes! It works!

What if the user wants to query multiple users?

```bash
$ gitgo -u pmbenjamin,defunkt
Searching user(s): [pmbenjamin defunkt]
```

That seems to work too!

Now, let’s start getting actual data. It’s always good practice to encapsulate different functionalities into separate functions to keep our code base clean and modular. You can put that function in **main.go** or in another file. I prefer a separate file, because it will make it our application modular, re-usable, and easily testable.

For the sake of time, here is the code along with comments to explain.

[https://gist.github.com/petermbenjamin/8aeece9305bb44282799384365ab3a3c#file-user-go](https://gist.github.com/petermbenjamin/8aeece9305bb44282799384365ab3a3c#file-user-go)

#### The gist is this:

1. In `user.go`, we send an HTTP GET request with the username
2. Then, we read the response body and store the data in `resp`.
3. It’s best practice to close the response body with `defer` statement to clean up after our function has failed or completed.
4. Then, we parse the JSON data with `json.Unmarshal` function, store the parsed user data in `user` variable, and return it.
5. In `main.go`, we loop over the `users` array, execute `getUser()` for each user, and output the data we want.

### Future Enhancements

This project was just a quick introductory guide for beginners. I know this project can be written a bit more efficiently.

In my next article, I plan on diving into new concepts, like concurrency (GoRoutines), channels, testing, vendoring, and writing Go Libraries (instead of applications).

In the meantime, the full project code can be found [here](https://github.com/pmbenjamin/gitgo).

Feel free to contribute by opening GitHub issues or submitting PRs.

