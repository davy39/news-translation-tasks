---
title: How to Install Rails on Ubuntu and Update Ruby to the Latest Version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-rails-on-ubuntu-and-update-ruby-to-the-latest-version
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Slice-3-1-.jpg
tags:
- name: Rails
  slug: rails
- name: Ruby
  slug: ruby
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: 'By Adebola Adeniran

  A couple of months ago, when I learned Ruby-on-Rails for the first time, I had to
  work on a collaborative project with a coding partner. We kept running into issues,
  as he had a different version of Rails and Buby setup for the pr...'
---

By Adebola Adeniran

A couple of months ago, when I learned Ruby-on-Rails for the first time, I had to work on a collaborative project with a coding partner. We kept running into issues, as he had a different version of Rails and Buby setup for the project. I couldn't wrap my head around how to install the versions the project needed. 

Here's the guide I wish I had. It also shows you how to switch the version of Ruby or Rails you're using, depending on the projects you're working on.

First, let's get the latest version of Ruby installed. To do this, we need to install a package called **RVM - Ruby version manager.** This package lets us install ANY version of Ruby on our Ubuntu machine and allows us to switch between versions.

All the code here will be run using the Ubuntu CLI/terminal.

## Installing RVM

1. First, we need to install a pre-requisite. Open up your Ubuntu terminal and type the command:

```
sudo apt-get install software-properties-common

```

Next, we need to add the **PPA (Personal Package archive)**. A PPA is how we get files distributed by developers that are yet to make it to the official Ubuntu package/app store. 

It's also a way for developers to distribute the latest versions of their software while waiting for Ubuntu to test and publish that software in the official store.

```
sudo apt-add-repository -y ppa:rael-gc/rvm
```

The command above adds the PPA to the list of locations we can download packages from on our Ubuntu machine.

Next, let's refresh our list of packages by running:

`sudo apt-get update`

Finally, let's install RVM itself.

```
sudo apt-get install rvm
```

Now restart your terminal for your changes to take effect. Then, type `rvm version` and hit `enter` to check that rvm is installed. You should get a response like this:

`rvm 1.29.10 (manual) by Michal Papis, Piotr Kuczynski, Wayne E. Seguin [[https://rvm.io](https://rvm.io)]`

## Installing Ruby 

Now we can install the latest Ruby version which is 2.7.1. Run the command `rvm install 2.7.1`. Alternatively, you can run `rvm install ruby` which will install the latest stable version (this will install v2.7.0).  
  
To see what Ruby versions you have installed, run `rvm ls`. To switch between Ruby versions, run `rvm use <version_number>` (for example, `rvm use 2.7.1`).

## Installing Ruby-on-Rails

The latest version of Rails is at 6.03. Rails is simply a Ruby gem, and with Ruby installed we can install Rails! Run `gem install rails` to install the latest version of Rails.  
  
Finally, to check that all went well, run `rails -v`. You should get `Rails 6.0.3.2` back, as this is the latest version at the time of publishing this article.   
  
You can now start your first Rails project by typing `rails new myapp`.

Hey, you're now on Rails!

