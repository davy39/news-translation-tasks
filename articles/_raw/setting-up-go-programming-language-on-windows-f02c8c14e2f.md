---
title: How to set up Go for Windows — a quick and easy guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T20:56:25.000Z'
originalURL: https://freecodecamp.org/news/setting-up-go-programming-language-on-windows-f02c8c14e2f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2kWUABWRtX3H8y5f.
tags:
- name: Go Language
  slug: go
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Linda Gregier

  Another great language to add to your full-stack developer tool belt is the simple
  and productive general-purpose programming language of Go.

  Through a project started in 2007, Go came to fruition through the efforts of some
  Google p...'
---

By Linda Gregier

Another great language to add to your full-stack developer tool belt is the simple and productive general-purpose programming language of Go.

Through a project started in 2007, Go came to fruition through the efforts of some Google programmers. They took great care in Go’s design to make it clear and consistent in its language features and standard libraries, making Go easy and _fun_ to use.

It’s open-source at it’s best…but don’t forget: it’s case-sensitive!

![Image](https://cdn-media-1.freecodecamp.org/images/1*zkig49mHmtgZkGu3KcEngw.png)
_Go installation avators_

So let’s get started on the Microsoft Windows 10 operating system. You’ll see just how easy this really is — only a basic working knowledge of GitHub and the command prompt is required. Sure there are other ways of installing and running the program, but with limited coding background I felt this set of instructions was the easiest to understand and follow.

Be sure to follow these steps in their entirety as well as in the **correct order (as listed)** to save yourself from having to uninstall Go and spend a few hours troubleshooting any installation-related issues.

### Phase 1: Install the following in this order

1. As Go uses open-source (FREE!) repositories often, be sure to install the Git package [here](https://git-scm.com/download/win) first.
2. Navigate to the Go installation website [here](https://golang.org/doc/install). Download and install the latest 64-bit Go set for Microsoft Windows OS.
3. Follow the instructions on the Go installation program.
4. Run the Command Prompt on your computer by searching for “cmd”. Open the command line and type: “go version”
5. The output after entering _go version_ should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*-j7JjyJSN3DqxEdO4lrjTw.png)

### Phase 2: Creating your Go work-space

First, confirm your Go binaries: go to your computer’s Control Panel, then to System and Security > System > Advanced system settings, and on the left-hand pane click the Advanced tab. Then click on Environmental Variables on the bottom-right-hand side. Ensure Path under System Variables has the “C:\Go\bin” variable in it.

Then create your Go work-space. This will be in a separate and new folder from where the Go installation files are saved. For example, your G installation files were saved under the path C:\Go and you are creating your Go work-space under C:\Projects\Go

In your new Go work-space folder, set up three new folders:

![Image](https://cdn-media-1.freecodecamp.org/images/1*I3BO4S6FQ6keH6o75ATuBg.png)
_bin, pkg, src_

### Phase 3: Create the GOPATH environment variable

Create the GOPATH variable and reference your newly-created Go work-space. Go back to your Control Panel and navigate to System and then Environmental Variables. Then under System Variables click on New.

Next to Variable Name, enter “GOPATH,” and next to Variable Value enter “C:\Projects\Go”

![Image](https://cdn-media-1.freecodecamp.org/images/1*EdndcOEfhY8DWreAWXjung.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ErNq0vYJQeTJadnJZczBtw.png)

To check that your path has been set correctly, enter “echo %GOPATH%” on the command line.

### Phase 4: Test and ensure

Now you’re ready to verify that all is working correctly by opening the command line and typing: `go get github.com/golang/example/hello`

Wait for the code to be entirely implemented (this could take a few seconds), then enter in the following in the command line: `%GOPATH%/bin/hello`

If the installation was successful, you should get the following return message: “Hello, Go examples!”

![Image](https://cdn-media-1.freecodecamp.org/images/1*EXG3IKaDbFqJ3qMpD_n08Q.png)

I hope you are successful. And if you run into any errors or confusing messages, comment below with the results of this command line: “go env”

Inspiration for this article came from the following on-line resources which were very easy to understand and helpful when setting up Go on my Windows operating system:

[Wade Wegner’s visually-simple & stylistic article](http://www.wadewegner.com/2014/12/easy-go-programming-setup-for-windows/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*z6i4jwGkvPE3S21x_PmvMw.png)

And now you’re ready to become a “Gopher”!

