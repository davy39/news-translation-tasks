---
title: How to Install Go in Arch Linux Using Pacman
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T20:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-go-in-arch-linux-using-pacman
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e65740569d1a4ca3ce4.jpg
tags:
- name: ArchLinux
  slug: archlinux
- name: golang
  slug: golang
seo_title: null
seo_desc: "Using the Arch Linux Package Manager (pacman) is the easiest way to install\
  \ Go. Based on the Arch Linux philosophy of providing new software versions very\
  \ fast, you will get a very current version of Go. \nBefore you can install the\
  \ Go package, you ha..."
---

Using the Arch Linux Package Manager (`pacman`) is the easiest way to install Go. Based on the Arch Linux philosophy of providing new software versions very fast, you will get a very current version of Go. 

Before you can install the Go package, you have to bring the system and all of your installed packages up to date. However, before updating your system and its packages, remember to check the [Arch Linux home page](https://www.archlinux.org/) first. Any out-of-the-ordinary steps that you have to do to prevent packages from breaking will be listed in a post there.

Once you've confirmed that it's safe to update your system, just run the following command:

```sh
$ sudo pacman -Syu
```

Remember that the `-S` flag is used to install a single package or a list of packages, the `y` option refreshes the list of all Arch Linux packages, and the option `u` upgrades all packages that are out of date.

After your system is completely up to date, install Go with the following command:

```sh
$ sudo pacman -S go
```

### Check the installation and version of Go

To check if Go was successfully installed, run:

```sh
$ go version
> go version go1.13.8 linux/amd64
```

This will print the installed version of Go to the console, while at the same time making sure the installation went smoothly.

## More info about Go:

[Learn Go in this free video course](https://www.freecodecamp.org/news/go-golang-course/)

[How to build a photo feed with Go and Vue.js](https://www.freecodecamp.org/news/how-to-build-a-photo-feed-with-go-and-vue-js-9d7f7f39c1b4/)

## More info about Arch Linux:

[How to install Arch Linux from scratch](https://www.freecodecamp.org/news/installing-arch-linux-from-scratch-b595095ddd48/)

## Bonus: How to Install Go on Ubuntu / Linux Mint:

Using Ubuntu’s Source Package Manager (`apt`) is the easiest way to install Go. While Arch Linux's `pacman` is on the bleeding edge, packages installed using `apt` and its variants are often several versions behind. 

The benefit of this approach is stability – while you won't be able to install the latest and greatest version of any package, you can be certain that your system won't break.

First, update your system with the following commands:

```sh
$ sudo apt update
$ sudo apt upgrade
```

Then install Go by running:

```sh
$ sudo apt install golang-go
```

### Check the installation and version of Go

To check if Go was successfully installed, open your terminal and run:

```sh
$ go version
```

This will print the installed version of Go to the console.

## Bonus: How to Install Go on macOS:

### **Installing Go in Mac OS X using Package Installer**

From the [golang’s download page](https://golang.org/dl/), get the Mac package installer (ending in .pkg) and run it.

![screenshot of golang's download page as of this writting, highliting link](https://raw.githubusercontent.com/AlexandroPerez/resources/master/img/mac_package_installer.jpg)

### Check the installation and version of Go

To check if Go was successfully installed, open your terminal and run:

```sh
$ go version
```

This will print the installed version of Go to the console.

### Installing Go in Mac OS X using tarball

You can get the link to the Mac OS tarball archive from the Latest Stable section of the [golang download page](https://golang.org/dl/).

![screenshot of golang's download page as of this writting, highliting link](https://raw.githubusercontent.com/AlexandroPerez/resources/master/img/mac_tarball.jpg)

### Installation Process

In this installation process we’ll use the latest stable version as of this writing (Go 1.9.1). For a newer or older version simply replace the link in the first step. Check the [golang download page](https://golang.org/dl/) to see what versions are currently available.

##### **Installing Go 1.9.1**

```text
$ curl -O https://storage.googleapis.com/golang/go1.9.1.darwin-amd64.tar.gz
$ sudo tar -C /usr/local -xzf go1.9.1.darwin-amd64.tar.gz
$ export PATH=$PATH:/usr/local/go/bin
```

### Check installation and version of go

To check if Go was successfully installed, use:

```sh
$ go version
```

This will print the installed version of Go to the console.


