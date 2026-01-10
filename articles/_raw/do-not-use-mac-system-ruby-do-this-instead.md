---
title: Don't Use the Mac System Ruby – Use This Instead
subtitle: ''
author: Daniel Kehoe
co_authors: []
series: null
date: '2021-02-10T17:27:03.000Z'
originalURL: https://freecodecamp.org/news/do-not-use-mac-system-ruby-do-this-instead
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/photo-1522776851755-3914469f0ca2.jpeg
tags:
- name: best practices
  slug: best-practices
- name: mac
  slug: mac
- name: Ruby
  slug: ruby
seo_title: null
seo_desc: 'Someone may have once told you, "Don''t use the system Ruby." It''s good
  advice, but why? Let''s find out.

  Which Ruby do you have?

  MacOS comes with a "system Ruby" pre-installed.

  Use the which command to see where Ruby is installed:

  $ which ruby

  /usr/bi...'
---

Someone may have once told you, "Don't use the system Ruby." It's good advice, but why? Let's find out.

## Which Ruby do you have?

MacOS comes with a "system Ruby" pre-installed.

Use the `which` command to see where Ruby is installed:

```bash
$ which ruby
/usr/bin/ruby

```

If you see `/usr/bin/ruby`, it is the pre-installed macOS system Ruby.

It's fine to use the system Ruby for running sysadmin scripts, as long as you don't alter the system Ruby by attempting to update it or add gems. 

But you don't want to use it when you are developing projects in Ruby.

## Ruby for development

For developing projects with Ruby, you should [Install Ruby with Homebrew](https://mac.install.guide/ruby/12.html) or use a version manager such as asdf, chruby, rbenv, or rvm. 

A version manager helps if you're juggling multiple projects and can't update all at once. For a guide that compares version managers and shows the best way to install Ruby, see my article [Install Ruby on a Mac](https://mac.install.guide/ruby/index.html).

But why not use the macOS default Ruby? Let's take a look at the reasons why it's a bad idea to use the Mac default Ruby for development.

### Gem installation hassles

RubyGems are the ready-made software libraries that make development easy and fun in Ruby. Most Ruby projects use at least a few gems.

If you use the Mac system Ruby, running `gem install` will try to save gems to the system Ruby directory `/Library/Ruby/Gems/2.6.0`. That directory is owned by `root`, the system superuser. Ordinary users are not allowed to write to it (and you really shouldn't alter this folder).

If you try to install a gem, for example `gem install rails`, you'll get a permissions error:

```bash
ERROR: While executing gem ... (Gem::FilePermissionError)
You don't have write permissions for the /Library/Ruby/Gems/2.6.0 directory

```

### It violates system security

Unix-based systems are powerful, so there's a workaround. You can install gems as a superuser to override the permissions restriction. But don't do this!

```bash
$ sudo gem install rails

```

Any time you are about to run `sudo`, you should stop and ask if you're about to shoot yourself in the foot. 

In this case, you need `sudo` because you're altering system files that are managed by the OS. Don't do it! You may leave the system in a broken or compromised state. Even worse, a gem might contain malicious code that tampers with your computer.

### Gem management

Experienced developers use [Bundler](https://bundler.io/) to install gems and manage their dependencies. 

Imagine you've got projects that use different versions of a gem (maybe there was a new gem release between your projects). Or maybe two different gems in your project rely on different versions of a dependent gem. 

Bundler uses a Gemfile in your project directory to keep track of the gems you need. If you were to use `sudo` to install gems with the system Ruby, you'd end up with a mess of incompatible gems in the system Ruby directory. 

You can work around the systems permission problem by [installing Bundler](https://bundler.io/doc/troubleshooting.html) with a command that uses your home directory for gems. But it's easier to install Ruby with Homebrew or use a version manager and use the Bundler that comes installed, which will correctly set up your local development environment.

### Use the newest Ruby

When you start a project, use the newest Ruby release (it's 3.0 at the time this was written). 

The system Ruby in macOS Catalina or Big Sur is Ruby 2.6.3, which is old. If you're just starting with Ruby, install with Homebrew and work on a project with Ruby 3.0. When you start building another project, it may be time to install a version manager so you can juggle projects with different Ruby versions.

## MacOS after Big Sur

MacOS Big Sur is now the current version. [Apple says](https://developer.apple.com/documentation/macos-release-notes/macos-catalina-10_15-release-notes):

> _"Scripting language runtimes such as Python, Ruby, and Perl are included in macOS for compatibility with legacy software. Future versions of macOS won’t include scripting language runtimes by default, and might require you to install additional packages."_

If you're reading this at the end of 2021, the system Ruby may already be gone. If not, prepare yourself by installing Ruby with Homebrew or a version manager. 

## Enjoy Ruby

For developers planning to build web applications with Rails, I've written a guide, [Install Rails on a Mac](https://learn-rails.com/install-rails-mac/index.html), which goes beyond [Install Ruby on a Mac](https://mac.install.guide/ruby/index.html) to show how to pick a version manager that will work with Node as well as Ruby.

Enjoy the pleasure of coding in Ruby! After all, it is known as a language dedicated to programmer happiness. But remember, the system Ruby is there for macOS, not for you.

